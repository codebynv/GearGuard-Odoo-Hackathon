# Maintenance SLA Calculation

Before implementing SLA metrics, specify:

- the event that starts the timer,
- the event that stops or pauses it,
- business hours versus calendar hours,
- treatment of weekends and holidays,
- timezone used for calculations,
- behavior when timestamps are missing.

Use fixed example timestamps to calculate expected results independently. Keep the dashboard metric consistent with the documented policy and the stored event history.