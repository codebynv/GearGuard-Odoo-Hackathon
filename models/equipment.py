from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Equipment(models.Model):
    _name = 'gearguard.equipment'
    _description = 'Equipment'
    _order = 'name'
    _rec_name = 'name'

    name = fields.Char(string='Equipment Name', required=True, index=True)
    asset_code = fields.Char(string='Asset Code', required=True, copy=False, index=True)
    serial_number = fields.Char(string='Serial Number', index=True)
    location = fields.Char(string='Location', index=True)
    department = fields.Char(string='Department', index=True)
    maintenance_team = fields.Char(string='Maintenance Team')
    status = fields.Selection([
        ('active', 'Active'),
        ('maintenance', 'Under Maintenance'),
        ('retired', 'Retired'),
    ], default='active', required=True, string='Equipment Status', index=True)
    last_maintenance_date = fields.Date(string='Last Maintenance')
    next_maintenance_date = fields.Date(string='Next Maintenance', index=True)
    notes = fields.Text(string='Notes')
    active = fields.Boolean(default=True, index=True)
    request_ids = fields.One2many('gearguard.request', 'equipment_id', string='Maintenance Requests')
    request_count = fields.Integer(string='Requests', compute='_compute_request_count')
    open_request_count = fields.Integer(string='Open Requests', compute='_compute_request_count')
    maintenance_due = fields.Boolean(string='Maintenance Due', compute='_compute_maintenance_due', search='_search_maintenance_due')

    _sql_constraints = [
        ('asset_code_unique', 'unique(asset_code)', 'Asset Code must be unique.'),
        ('serial_number_unique', 'unique(serial_number)', 'Serial Number must be unique when provided.'),
    ]

    @api.depends('request_ids.state')
    def _compute_request_count(self):
        for record in self:
            record.request_count = len(record.request_ids)
            record.open_request_count = len(record.request_ids.filtered(lambda request: request.state in ('new', 'progress')))

    @api.depends('next_maintenance_date', 'status')
    def _compute_maintenance_due(self):
        today = fields.Date.context_today(self)
        for record in self:
            record.maintenance_due = bool(
                record.status != 'retired'
                and record.next_maintenance_date
                and record.next_maintenance_date <= today
            )

    def _search_maintenance_due(self, operator, value):
        if operator not in ('=', '!='):
            raise ValidationError('Maintenance Due only supports = and != searches.')
        due_domain = [('next_maintenance_date', '<=', fields.Date.context_today(self)), ('next_maintenance_date', '!=', False), ('status', '!=', 'retired')]
        return due_domain if (operator == '=' and value) or (operator == '!=' and not value) else ['|', ('next_maintenance_date', '>', fields.Date.context_today(self)), ('next_maintenance_date', '=', False)]

    def action_view_requests(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Maintenance Requests',
            'res_model': 'gearguard.request',
            'view_mode': 'tree,form',
            'domain': [('equipment_id', '=', self.id)],
            'context': {'default_equipment_id': self.id},
        }
