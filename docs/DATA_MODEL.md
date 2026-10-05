# Data Model Notes

The core domain connects equipment, maintenance requests, and preventive plans.

    Equipment
       │
       ├── Maintenance Requests
       │
       └── Preventive Plans

## Integrity rules

- Equipment identifiers should remain unique.
- Requests should reference valid equipment.
- Workflow state should remain consistent with the equipment state.
- Preventive schedules should produce actionable due dates.

Business rules should be enforced by the Odoo model layer rather than only by the interface.
