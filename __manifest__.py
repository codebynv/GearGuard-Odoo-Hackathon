{
    'name': 'GearGuard - Smart Equipment Maintenance Tracker',
    'version': '1.1.0',
    'summary': 'Centralized equipment and maintenance request tracking',
    'description': """
GearGuard provides a lightweight maintenance workflow for organizations
that need visibility over equipment, repair requests, technicians and status.
    """,
    'category': 'Operations/Maintenance',
    'author': 'GearGuard Team',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/equipment_view.xml',
        'views/maintenance_request_view.xml',
        'views/gearguard_menu.xml',
    ],
    'installable': True,
    'application': True,
}
