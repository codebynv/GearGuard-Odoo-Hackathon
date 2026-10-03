# Error Handling Reference

## Validation failures

Show a clear user-facing message and prevent the invalid operation.

Examples include:

- duplicate equipment identifiers,
- invalid workflow transitions,
- incomplete repair information,
- invalid maintenance dates.

## Workflow failures

Keep the record in a consistent state. Do not silently continue after a failed business-rule check.

## Automation failures

Scheduled maintenance generation should be observable so operators can identify failed or incomplete automation.

## Principle

Validation should happen as close as practical to the operation that can violate the business rule.
