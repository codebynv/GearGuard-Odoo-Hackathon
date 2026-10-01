# GearGuard Workflow Reference

## Equipment lifecycle

    Active
      ↓
    Under Maintenance
      ↓
    Active

Equipment enters maintenance when active work starts and returns to the active state after repair.

## Maintenance request lifecycle

    New
      ↓
    In Progress
      ↓
    Repaired

A request may also be cancelled where the workflow permits it.

## Business-rule checkpoints

- Equipment identifiers should remain unique.
- Invalid state transitions should be rejected.
- Repair completion should include a resolution.
- Due maintenance should remain visible to operators.
- Preventive plans can create requests through scheduled automation.

## Demo focus

A useful end-to-end demonstration is:

Equipment → Request → Start Work → Resolution → Repaired → Dashboard update.
