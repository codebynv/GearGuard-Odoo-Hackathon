from odoo import api, fields, models


class MaintenanceDashboard(models.TransientModel):
    _name = 'gearguard.dashboard'
    _description = 'GearGuard Maintenance Dashboard'

    total_equipment = fields.Integer(compute='_compute_metrics')
    active_equipment = fields.Integer(compute='_compute_metrics')
    equipment_in_maintenance = fields.Integer(compute='_compute_metrics')
    maintenance_due = fields.Integer(compute='_compute_metrics')
    open_requests = fields.Integer(compute='_compute_metrics')
    critical_requests = fields.Integer(compute='_compute_metrics')
    overdue_requests = fields.Integer(compute='_compute_metrics')

    @api.depends()
    def _compute_metrics(self):
        Equipment = self.env['gearguard.equipment']
        Request = self.env['gearguard.request']
        today = fields.Date.context_today(self)
        for record in self:
            record.total_equipment = Equipment.search_count([('active', '=', True)])
            record.active_equipment = Equipment.search_count([('active', '=', True), ('status', '=', 'active')])
            record.equipment_in_maintenance = Equipment.search_count([('active', '=', True), ('status', '=', 'maintenance')])
            record.maintenance_due = Equipment.search_count([('active', '=', True), ('status', '!=', 'retired'), ('next_maintenance_date', '!=', False), ('next_maintenance_date', '<=', today)])
            record.open_requests = Request.search_count([('state', 'in', ('new', 'progress'))])
            record.critical_requests = Request.search_count([('state', 'in', ('new', 'progress')), ('priority', '=', '3')])
            record.overdue_requests = Request.search_count([('state', 'in', ('new', 'progress')), ('scheduled_date', '!=', False), ('scheduled_date', '<', today)])
