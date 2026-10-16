---
name: shape-feature
description: Turn a feature idea into a clear user problem, desired behavior, and bounded scope. Use when a proposed feature needs clarification before design, specification, or implementation.
---

Clarify one feature until its purpose and boundaries are usable for the next step. Start from the existing conversation, product context, and relevant code or documentation.

## Understand the need

Establish who needs the feature, what they are trying to accomplish, how they do it today, and what should improve. Distinguish evidence of a problem from assumptions about users. Use concrete examples to uncover what broad phrases such as "support sharing" actually require.

Look up facts available in the repository rather than asking the user to supply them. Ask focused questions about unresolved product judgment, explain the tradeoff, and offer a recommendation when useful. Reuse answers already given. Resolve the most consequential uncertainties first rather than exploring every conceivable branch.

## Bound the feature

Describe the main user journey and relevant alternatives, permissions, failure cases, and compatibility expectations. Choose the smallest useful scope that still solves the stated problem. Record explicit exclusions and what success would look like in observable terms.

Separate required outcomes from suggested implementations. Investigate technical uncertainty when it changes feasibility or scope. Leave routine technical choices for design or implementation. Use an example or sketch to make a consequential choice concrete, without turning clarification into production coding.

Keep agreed decisions, working assumptions, and open questions distinct. Ask for a decision when competing interpretations would produce materially different features. Low-impact details can be deferred explicitly. Uncertainty that changes the feature's purpose or required behavior cannot be silently treated as agreement.

## Capture the result

Summarize the problem, intended users, chosen scope, key behavior, success criteria, exclusions, and remaining questions. Keep this in the existing feature artifact when one exists. Record each new or renamed concept using [glossary](../../../docs/glossary/SKILL.md). For a discussion alone, a concise response is enough. Save a separate brief when requested or needed for a handoff, following project conventions or `.scratch/features/<descriptive-slug>.md`.

Finish when there is enough shared understanding for the intended next step, or explain the specific decision or evidence still needed. Recommend design for unresolved technical choices, or specification when the behavior is settled. Shaping alone does not request implementation or creation of tracker issues.
