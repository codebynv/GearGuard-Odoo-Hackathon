# Odoo Testing Notes

When changing an Odoo model or workflow:

- Test model constraints as well as form behavior.
- Verify access using a non-administrator role.
- Cover state transitions and invalid transitions.
- Check related records and company boundaries.
- Include regression tests for fixed defects.
- Record any checks that require a configured Odoo instance.

A form that looks correct does not prove server-side rules are enforced.