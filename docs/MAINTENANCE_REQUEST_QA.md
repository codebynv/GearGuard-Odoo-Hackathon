# Maintenance Request QA

Check the implemented request lifecycle.

- Create a request with valid required fields.
- Reject missing equipment or invalid dates.
- Verify role restrictions on state changes.
- Confirm invalid transitions are rejected by the model.
- Check saved values after reopening a record.
- Confirm dashboard counts match persisted records.

Run these checks against a configured test database; this document alone does not establish that they pass.