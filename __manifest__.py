{
    'name': 'GearGuard - Smart Equipment Maintenance Tracker',
    'version': '2.0.0',
    'summary': 'Equipment lifecycle, preventive maintenance and maintenance operations',
    'description': """
GearGuard manages equipment, maintenance requests, preventive maintenance plans,
operational KPIs and maintenance workflows from one Odoo application.
    """,
    'category': 'Operations/Maintenance',
    'author': 'GearGuard Team',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/maintenance_cron.xml',
        'views/equipment_view.xml',
        'views/maintenance_request_view.xml',
        'views/maintenance_request_graph.xml',
        'views/maintenance_plan_view.xml',
        'views/maintenance_dashboard_view.xml',
        'views/gearguard_menu.xml',
    ],
    'installable': True,
    'application': True,
}
