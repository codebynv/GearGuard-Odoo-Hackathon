# Maintenance Workflow Test Plan

Verify the maintenance request lifecycle against the implemented states.

- Create a request with valid data.
- Reject missing required fields.
- Confirm only permitted roles can change protected fields.
- Verify invalid state transitions are rejected.
- Confirm list and dashboard counts reflect saved records.
- Check that a failed save does not show a success message.

Run these checks in a configured test database and document any environment-specific prerequisites.