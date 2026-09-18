from odoo import api, fields, models
from odoo.exceptions import ValidationError


class MaintenancePlan(models.Model):
    _name = 'gearguard.plan'
    _description = 'Preventive Maintenance Plan'
    _order = 'next_run_date, name'

    name = fields.Char(required=True, index=True)
    equipment_id = fields.Many2one('gearguard.equipment', required=True, ondelete='cascade', index=True)
    frequency = fields.Selection([
        ('monthly', 'Monthly'),
        ('quarterly', 'Quarterly'),
        ('half_yearly', 'Every 6 Months'),
        ('yearly', 'Yearly'),
    ], required=True, default='quarterly')
    next_run_date = fields.Date(required=True, default=fields.Date.context_today, index=True)
    active = fields.Boolean(default=True)
    instructions = fields.Text()

    @api.constrains('next_run_date')
    def _check_date(self):
        for record in self:
            if not record.next_run_date:
                raise ValidationError('Next run date is required.')

    def action_generate_request(self):
        self.ensure_one()
        request = self.env['gearguard.request'].create({
            'subject': 'Preventive Maintenance: %s' % self.name,
            'equipment_id': self.equipment_id.id,
            'scheduled_date': self.next_run_date,
            'priority': '1',
            'description': self.instructions or 'Scheduled preventive maintenance.',
        })
        months = {'monthly': 1, 'quarterly': 3, 'half_yearly': 6, 'yearly': 12}[self.frequency]
        self.next_run_date = fields.Date.add(self.next_run_date, months=months)
        return {
            'type': 'ir.actions.act_window',
            'name': 'Maintenance Request',
            'res_model': 'gearguard.request',
            'res_id': request.id,
            'view_mode': 'form',
        }

    @api.model
    def cron_generate_due_requests(self):
        today = fields.Date.context_today(self)
        for plan in self.search([('active', '=', True), ('next_run_date', '<=', today)]):
            plan.action_generate_request()
        return True
