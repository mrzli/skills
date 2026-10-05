---
name: prototype
description: Build a disposable, interactive demonstration to explore a UI, workflow, or logic model before committing to implementation. Use when the user needs to see alternatives or try behavior to resolve a design question.
---

Produce a runnable artifact that helps answer a specific design question. Match its fidelity to the decision, and make its assumptions and simulated behavior visible.

## Frame the question

Read the request, relevant project instructions, existing interfaces, and prior decisions. Identify what the user needs to compare or experience and what observation would settle the question. Reuse established requirements rather than reopening them.

Choose the smallest useful form. For appearance or interaction choices, build UI alternatives. For rules, state transitions, or data relationships, build a demonstration the user can manipulate. Combine them only when the question requires both. Ordinary measurements and technical feasibility experiments belong with [investigate](../investigate/SKILL.md).

## Build the demonstration

Use the project's prototype convention, or `.scratch/prototypes/<descriptive-slug>/` when none exists. Prefer a self-contained file when it can represent the behavior honestly. Use the existing stack when integration context matters. For an existing UI, preserve representative surrounding layout and data density so alternatives can be judged in context. Keep temporary routes or variants isolated from normal production behavior.

Keep setup minimal and provide an exact command or file to open. Label the artifact as a prototype and state the question it explores. Use synthetic or appropriate local data and in-memory state by default. Simulate external writes. If real persistence or integration is essential to the question, use an isolated test environment and state its limits.

### UI alternatives

When comparing designs, offer a few meaningfully different layouts or interaction approaches, usually two or three. Use the same representative content so the comparison is fair. A single approach is enough when the question is about trying a specific interaction.

Make alternatives easy to switch between or view side by side. Exercise the states that influence the choice, such as dense content, empty results, errors, or a narrow viewport. Explain the practical tradeoff behind each alternative rather than varying only colors or copy.

### Logic and state

Expose the relevant state in the user's terminology, with controls for actions and a reset to a known starting point. Keep the model separate from its display so a rendering shortcut does not silently determine the rules.

Provide a normal scenario and the awkward sequences that prompted the question. Show invalid actions and their consequences clearly. Distinguish a model's simulated result from evidence about the real system.

## Check and hand over

Run the artifact and exercise its main controls, variants, and representative scenarios with the available tools. Check enough to trust the demonstration without building a production test suite. For logic that informs the decision, compare important results with an independently worked example or stated requirement. Report any interaction you could not verify.

Present the artifact, how to run it, what to try, and the question feedback should answer. Separate observations from preferences and untested assumptions. If the user has not tried it, finish with a usable demonstration and the decision still open. Do not invent a winner or wait indefinitely for feedback.

Once feedback or evidence settles the question, record the conclusion and reasons in the existing design or investigation record, linking the artifact. Keep useful prototypes in the project's scratch or archive convention. Remove temporary integration changes when their role is complete and the artifact remains recoverable.

Production work uses [implement](../../delivery/implement/SKILL.md) when authorized, carrying forward the chosen behavior and verification needs. Treat prototype code as material to reassess, not as verified production code. Creating a prototype alone does not request deployment, publication, or a commit.
