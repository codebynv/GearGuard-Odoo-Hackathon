# Odoo Record Rule Review

When changing access rules, verify:

- which model and records the rule covers,
- whether the rule is global or group-specific,
- how multiple applicable rules combine,
- company boundaries and allowed companies,
- read, write, create, and unlink behavior,
- behavior for users with multiple roles.

Test with representative non-admin users in a disposable database. Confirm server-side access, not only menu or view visibility.