# GearGuard Demo Checklist

Use this checklist to verify the main maintenance workflow before a demo or submission.

## Equipment

- [ ] Create an equipment record with a unique asset code.
- [ ] Confirm duplicate asset codes or serial numbers are rejected.
- [ ] Verify equipment status and maintenance dates are displayed correctly.

## Maintenance workflow

- [ ] Create a maintenance request linked to equipment.
- [ ] Start the request and confirm the equipment moves to Under Maintenance.
- [ ] Attempt an invalid workflow transition and confirm it is rejected.
- [ ] Complete a repair with a resolution note.
- [ ] Confirm the repaired equipment returns to Active.

## Preventive maintenance

- [ ] Create a preventive maintenance plan.
- [ ] Set a due date and recurrence.
- [ ] Run the scheduled job or equivalent cron action.
- [ ] Confirm a maintenance request is generated for a due plan.

## Dashboard

- [ ] Verify equipment counts match the underlying records.
- [ ] Verify open and critical request counts.
- [ ] Verify overdue requests are visible.
- [ ] Check Graph and Pivot views for maintenance data.

## Final sanity check

- [ ] No secrets or local environment files are committed.
- [ ] Changes are tested in the Odoo environment before submission.
