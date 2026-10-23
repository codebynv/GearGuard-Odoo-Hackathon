# Odoo Multi-Company Checks

When the deployment uses multiple companies, verify:

- records are scoped to the intended company,
- users cannot read or modify another company's restricted records,
- company-dependent fields use the correct context,
- reports and dashboard counts respect access rules,
- automated jobs use an explicit company context.

Run checks with representative non-admin users in a configured Odoo environment.