from odoo import fields, models


class Equipment(models.Model):
    _name = 'gearguard.equipment'
    _description = 'Equipment'
    _order = 'name'

    name = fields.Char(string='Equipment Name', required=True)
    asset_code = fields.Char(string='Asset Code', required=True, copy=False)
    serial_number = fields.Char(string='Serial Number')
    location = fields.Char(string='Location')
    department = fields.Char(string='Department')
    maintenance_team = fields.Char(string='Maintenance Team')
    status = fields.Selection([
        ('active', 'Active'),
        ('maintenance', 'Under Maintenance'),
        ('retired', 'Retired'),
    ], default='active', required=True, string='Equipment Status')
    last_maintenance_date = fields.Date(string='Last Maintenance')
    next_maintenance_date = fields.Date(string='Next Maintenance')
    notes = fields.Text(string='Notes')
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ('asset_code_unique', 'unique(asset_code)', 'Asset Code must be unique.'),
    ]
