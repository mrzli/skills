# Feature map

A feature map lists the application's user-facing features and how to verify each one. It is cheaper to read than the code and keeps verification consistent across agents.

Store it beside the verification skill as `features/README.md` plus one file per feature. Start with the three to five most important features, identified from menus, commands, routes, or documentation.

The README states the baseline: how to launch with disposable data, the seed data, the doctor check, and driving conventions such as preferring accessible names and restoring seeded data after a change.

Each feature file answers, from the user's point of view:

- **Sub-features:** the distinct behaviors to verify.
- **How to reach it:** every user entry point, such as a button, a shortcut, or a command.
- **Driving it:** preconditions, then each step as an action, the exact tool command, and the observable result that proves it. End with the evidence to capture.
- **Gotchas:** traps that cause false passes or failures.

Verifying one convenient entry point is incomplete when the map lists others. If seed data lacks a precondition a step needs, report the failure and note the reason under gotchas. Never weaken a step to make it pass.
