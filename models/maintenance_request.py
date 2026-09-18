from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class MaintenanceRequest(models.Model):
    _name = 'gearguard.request'
    _description = 'Maintenance Request'
    _order = 'priority desc, scheduled_date asc, request_date desc'
    _rec_name = 'subject'

    subject = fields.Char(string='Issue / Request', required=True, index=True)
    equipment_id = fields.Many2one('gearguard.equipment', string='Equipment', required=True, ondelete='cascade', index=True)
    technician = fields.Char(string='Assigned Technician', index=True)
    request_date = fields.Date(string='Request Date', default=fields.Date.context_today, required=True, index=True)
    scheduled_date = fields.Date(string='Scheduled Date', index=True)
    completed_date = fields.Date(string='Completed Date', readonly=True)
    priority = fields.Selection([('0', 'Low'), ('1', 'Normal'), ('2', 'High'), ('3', 'Critical')], default='1', string='Priority', index=True)
    state = fields.Selection([('new', 'New'), ('progress', 'In Progress'), ('done', 'Repaired'), ('cancelled', 'Cancelled')], default='new', required=True, string='Status', index=True)
    description = fields.Text(string='Issue Description')
    resolution = fields.Text(string='Resolution / Work Done')
    is_overdue = fields.Boolean(string='Overdue', compute='_compute_is_overdue', search='_search_is_overdue')

    @api.constrains('scheduled_date', 'request_date')
    def _check_dates(self):
        for record in self:
            if record.scheduled_date and record.scheduled_date < record.request_date:
                raise ValidationError('Scheduled Date cannot be before Request Date.')

    @api.constrains('state', 'resolution')
    def _check_resolution(self):
        for record in self:
            if record.state == 'done' and not record.resolution:
                raise ValidationError('Please record the resolution before marking a request as Repaired.')

    @api.depends('scheduled_date', 'state')
    def _compute_is_overdue(self):
        today = fields.Date.context_today(self)
        for record in self:
            record.is_overdue = bool(record.scheduled_date and record.scheduled_date < today and record.state in ('new', 'progress'))

    def _search_is_overdue(self, operator, value):
        if operator not in ('=', '!='):
            raise ValidationError('Overdue only supports = and != searches.')
        domain = [('scheduled_date', '<', fields.Date.context_today(self)), ('scheduled_date', '!=', False), ('state', 'in', ('new', 'progress'))]
        return domain if (operator == '=' and value) or (operator == '!=' and not value) else ['|', ('scheduled_date', '>=', fields.Date.context_today(self)), ('scheduled_date', '=', False)]

    def action_start(self):
        for record in self:
            if record.state != 'new':
                raise UserError('Only new maintenance requests can be started.')
            record.write({'state': 'progress'})
            record.equipment_id.write({'status': 'maintenance'})
        return True

    def action_repair(self):
        for record in self:
            if record.state != 'progress':
                raise UserError('Only in-progress requests can be repaired.')
            if not record.resolution:
                raise UserError('Add the resolution / work completed before repairing this request.')
            record.write({'state': 'done', 'completed_date': fields.Date.context_today(record)})
            equipment = record.equipment_id
            equipment.write({'status': 'active', 'last_maintenance_date': fields.Date.context_today(record)})
            if not equipment.next_maintenance_date:
                equipment.write({'next_maintenance_date': fields.Date.add(fields.Date.context_today(record), months=3)})
        return True

    def action_cancel(self):
        for record in self:
            if record.state in ('done', 'cancelled'):
                continue
            record.write({'state': 'cancelled'})
            equipment = record.equipment_id
            other_open = self.search_count([('equipment_id', '=', equipment.id), ('id', '!=', record.id), ('state', 'in', ('new', 'progress'))])
            if not other_open and equipment.status == 'maintenance':
                equipment.write({'status': 'active'})
        return True
