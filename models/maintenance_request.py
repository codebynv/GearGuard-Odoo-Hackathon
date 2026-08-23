from odoo import fields, models


class MaintenanceRequest(models.Model):
    _name = 'gearguard.request'
    _description = 'Maintenance Request'
    _order = 'priority desc, request_date desc'

    subject = fields.Char(string='Issue / Request', required=True)
    equipment_id = fields.Many2one(
        'gearguard.equipment',
        string='Equipment',
        required=True,
        ondelete='cascade',
    )
    technician = fields.Char(string='Assigned Technician')
    request_date = fields.Date(
        string='Request Date',
        default=fields.Date.context_today,
        required=True,
    )
    scheduled_date = fields.Date(string='Scheduled Date')
    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Normal'),
        ('2', 'High'),
        ('3', 'Critical'),
    ], default='1', string='Priority')
    state = fields.Selection([
        ('new', 'New'),
        ('progress', 'In Progress'),
        ('done', 'Repaired'),
        ('cancelled', 'Cancelled'),
    ], default='new', required=True, string='Status')
    description = fields.Text(string='Issue Description')
    resolution = fields.Text(string='Resolution / Work Done')

    def action_start(self):
        self.write({'state': 'progress'})
        self.mapped('equipment_id').write({'status': 'maintenance'})

    def action_repair(self):
        self.write({'state': 'done'})
        self.mapped('equipment_id').write({'status': 'active'})

    def action_cancel(self):
        self.write({'state': 'cancelled'})
