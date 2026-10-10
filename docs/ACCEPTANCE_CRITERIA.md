# Acceptance Criteria

## Equipment

- Equipment records have valid identifiers.
- Duplicate identifiers are rejected.
- Equipment status is visible to operators.

## Maintenance requests

- Requests reference valid equipment.
- Invalid state transitions are rejected.
- Repair completion records a resolution.
- Equipment state remains consistent with maintenance work.

## Preventive maintenance

- Due plans are discoverable.
- Scheduled generation is observable.
- Repeated execution does not create unintended duplicates.

## Dashboard

- Metrics reflect persisted records.
- Critical and overdue work is easy to identify.
