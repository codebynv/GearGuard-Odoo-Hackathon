# Maintenance Edge Cases

Test these scenarios when changing maintenance workflows:

- request references missing equipment,
- duplicate equipment identifier,
- invalid state transition,
- repair completed without a resolution,
- preventive plan is not yet due,
- scheduled action runs more than once,
- dashboard has no maintenance records.

Verify that invalid actions are rejected and persisted records remain consistent.
