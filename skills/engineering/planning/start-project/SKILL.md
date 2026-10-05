---
name: start-project
description: Define a new software project's purpose, users, first useful scope, and success criteria. Use when establishing or revisiting project direction before feature design and implementation.
---

Produce a project brief that guides what to build and why. Project definition may end in a recommendation to investigate further or not build yet. It does not by itself request scaffolding, provisioning, or application implementation.

## Understand the purpose

Read the user's idea, existing notes, and any related product or repository context. Establish the intended users, the problem they face, their current alternatives, and why solving it matters. Separate observed needs from assumptions and desired features from the outcomes they serve.

Ask focused questions about missing goals and constraints. Offer concrete examples when the user does not yet know the options. Prioritize decisions that determine direction. Defer detail that depends on learning from the first useful version.

Identify constraints that materially shape the project, such as available time, budget, deployment environment, integration needs, data handling, and maintenance responsibility. Do not infer an organization-scale process for a solo project or require a commercial business case for a personal tool.

## Define the first useful version

Describe a small coherent outcome that would be worth using, with essential user journeys and explicit exclusions. State observable success criteria: what a user should be able to accomplish and what evidence would show the project is worthwhile.

Identify the riskiest assumptions and how to test them cheaply. Where need or feasibility is uncertain, recommend an interview, prototype, investigation, or other concrete learning step before committing to a large build. Keep proposed technologies distinct from requirements and avoid selecting a stack without a relevant reason.

Establish enough terminology and boundaries to avoid conflicting interpretations. Respect existing project commitments when revisiting direction and make any proposed change to them explicit.

## Save the brief

Update an existing project brief or follow the requested destination and repository convention. Otherwise save `docs/project-brief.md`. Include purpose, users, current alternatives, initial scope, exclusions, success criteria, constraints, and open assumptions in a format proportional to the project.

Record which decisions are agreed, which are proposals, and which require evidence. End with the next useful step: shape the first feature when direction is clear, or investigate the most consequential unknown. Finish when the brief can guide that step without pretending the entire roadmap is settled.
