# Maintenance State Matrix

For each maintenance-request state, document:

- allowed next states,
- roles permitted to make the transition,
- required fields before transition,
- notifications or side effects,
- behavior for repeated requests.

Test invalid transitions through the server-side model, not only by hiding UI actions. Keep this matrix aligned with the implemented workflow.
