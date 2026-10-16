---
name: design
description: Choose a technical approach for a scoped change by comparing meaningful alternatives and their tradeoffs. Use when interfaces, data, architecture, or migration choices need resolution before implementation.
---

Produce a technical decision that fits the requirements and existing system. Keep the depth of design proportional to the consequences and reversibility of the choice.

## Understand the constraints

Read the request or specification, project instructions, relevant code, tests, and existing architectural decisions. Identify required behavior, compatibility obligations, operating constraints, and the decision that remains open. Treat backward compatibility as an obligation only for consumers outside the repository, persisted data, or an explicit user requirement. Otherwise, design the target directly without transitional layers. Preserve settled product choices. Expose contradictions rather than silently redesigning the feature.

Inspect the current approach before introducing a new abstraction or dependency. Trace who calls the affected interfaces and what they rely on, including errors, ordering, data ownership, and side effects. Resolve factual uncertainty through inspection or focused investigation.

## Compare approaches

Consider the simplest viable change and materially different alternatives where there is a real tradeoff. An obvious, reversible choice may need only a short rationale. For consequential choices, compare options against the actual constraints, including implementation cost, compatibility, operational burden, maintainability, and verification.

Favor interfaces that hide complexity from callers and keep related behavior understandable in one place. Add abstractions for demonstrated variation or complexity, rather than hypothetical future flexibility. Use the project's terminology, and record each new or renamed concept using [glossary](../../../docs/glossary/SKILL.md). A particular design vocabulary or pattern is not a requirement.

For a new interface, write two or three realistic call sites before the types and fit the types to them. Reject shapes that offer two ways to do one task, require keeping parallel lists in sync by hand, expose internals to callers, or give one piece of state more than one writer.

Describe the important interfaces, state transitions, data changes, and failure behavior. Include migration, rollout, and recovery where the design affects existing users or stored data. Use a small diagram, contract, or code sketch when it makes the decision clearer than prose.

Identify how the design can be tested through observable behavior. If a choice depends on uncertain feasibility or performance, gather evidence with a focused experiment before presenting it as settled. Separate evidence, assumptions, and expected benefits.

Use [prototype](../../investigation/prototype/SKILL.md) when choosing an approach requires trying an interaction or comparing concrete UI or logic alternatives. Supply the decision, constraints, and unresolved question, then use the demonstration and feedback as evidence for the design.

## Record the decision

Recommend an approach with its reasons, rejected alternatives, and remaining risks. Make routine technical choices within the authorized scope. Ask for user judgment when alternatives materially change product behavior, cost, compatibility, or an established commitment that the evidence cannot settle.

Record accepted decisions in the existing specification or project design records. When a design is worked out in conversation across several exchanges or sessions, write each decision to the record when it is agreed, not at the end, and note rejected options and open questions there too. For a substantial standalone decision with no established location, save `docs/design/<descriptive-slug>.md`. Label unresolved proposals as such. Keep task breakdown in the implementation plan rather than duplicating it here.

Finish when the next implementer can understand the chosen approach, constraints, verification strategy, and remaining blockers. Design alone does not request production implementation.
