---
name: plan
description: Break agreed engineering work into manageable, verifiable tasks with explicit dependencies. Use when a specification or scoped change is too large to implement as one piece, or when an existing implementation plan needs revision.
---

Produce an executable work plan from the request, specification, or agreed conversation. Planning organizes work. It does not authorize implementation or settle unresolved product choices by assumption.

## Understand the work

Read the source requirements, applicable project instructions, existing plans, and enough code to understand the affected areas. Identify acceptance criteria, constraints, and what is already implemented. Reuse established decisions rather than reopening them without evidence.

Separate implementation work from unknowns that prevent planning it. Resolve factual questions by inspection. Where a consequential decision remains open, record a bounded investigation or decision task and block only the tasks that depend on its answer.

## Divide and order

Prefer small, complete slices of behavior that can be implemented and verified independently. Include the code, tests, documentation, and configuration each slice needs. Avoid splitting by technical layer when that leaves several tasks unable to demonstrate anything useful on their own.

Use structural or migration tasks when a complete behavior slice is impractical. For broad compatibility changes, consider adding the new form, migrating consumers, then removing the old form. State when intermediate steps require a shared integration point rather than claiming each is independently releasable.

For each task, provide:

- A stable identifier and a title describing the outcome.
- Scope and links to the relevant requirements or decisions.
- Observable completion criteria and appropriate verification.
- Genuine prerequisites, including unresolved decisions, or an explicit statement that it can start now.

Choose tasks small enough to understand and finish without reconstructing the entire effort. One task is valid for a small change. Dependencies express necessity, not a preferred ordering. Distinguish independent work from tasks that would conflict over shared files or state.

## Save and check

Update the existing plan or follow the requested destination and project convention. Otherwise save one Markdown plan to `docs/plans/<descriptive-slug>.md`. Split it only when the size or workflow warrants it. Creating external tickets requires authorization. Preserve completed work and evidence when revising a plan.

Check that every in-scope acceptance criterion is covered, dependencies are acyclic and resolvable, and tasks have enough context to execute. Identify the tasks ready to start and any blocked work. Include final integration and verification where individual task checks cannot establish the overall outcome.

Finish with the plan link, recommended starting task, and blocking decisions. Leave execution to the user or the calling delivery workflow.
