---
name: guide
description: Help choose the next engineering activity or skill from the user's situation. Use when the user asks where to start, what to do next, or how to use the engineering skills, rather than asking to execute an already chosen task.
---

Recommend a useful next step without requiring the user to understand the skill catalogue first. Use the supplied situation, or the current conversation if none is supplied. Guidance alone does not start implementation or a delivery workflow.

## Understand where the user is

Identify the desired outcome, what is already settled or completed, and what currently prevents progress. Use relevant conversation and existing project artifacts before asking the user to repeat information. Inspect only enough context to choose the next activity; a routing question does not require a full codebase review.

A new project may have no repository, specification, or technical choices yet. Start from the idea and explain the next activity in ordinary language. If a missing distinction would change the recommendation, ask one focused question, offering concrete possibilities when helpful.

## Choose the next activity

Use the map below as a starting point. Read the recommended skill before describing its behavior or invoking it, and check its availability in the current environment. If it is unavailable, explain the activity directly and make the limitation clear.

| Situation | Skill |
| --- | --- |
| Establish a new project's purpose, users, and first useful scope | [start-project](../../planning/start-project/SKILL.md) |
| Clarify what one feature should do and what it excludes | [shape-feature](../../planning/shape-feature/SKILL.md) |
| Answer a concrete unknown with evidence or an experiment | [investigate](../../investigation/investigate/SKILL.md) |
| Choose a technical approach or resolve design tradeoffs | [design](../../planning/design/SKILL.md) |
| Preserve agreed requirements and acceptance criteria | [write-spec](../../planning/write-spec/SKILL.md) |
| Divide agreed work into verifiable tasks and dependencies | [plan](../../planning/plan/SKILL.md) |
| Build a clear, scoped change | [implement](../../delivery/implement/SKILL.md) |
| Assess an existing change before proceeding | [review-code](../../delivery/review-code/SKILL.md) |
| Diagnose and repair unexpected behavior | [fix-bug](../../delivery/fix-bug/SKILL.md) |
| Improve selected code structure while preserving behavior | [refactor](../../delivery/refactor/SKILL.md) |
| Publish or deploy verified work to a specified target | [release](../../delivery/release/SKILL.md) |
| Have the agent coordinate a feature across activities and tasks | [deliver-feature](../deliver-feature/SKILL.md) |
| Find structural problems worth addressing in existing code | [review-architecture](../../investigation/review-architecture/SKILL.md) |
| Assess whether the product helps its intended users | [review-product](../../investigation/review-product/SKILL.md) |
| Improve the development process after observed friction | [improve-workflow](../improve-workflow/SKILL.md) |
| Review the skill collection or compare it with external skill repositories | [maintain-skills](../maintain-skills/SKILL.md) |

Choose the activity that resolves the immediate obstacle. Evidence gathering precedes decisions that depend on it; settled decisions do not need another interview. A small, clear change can go directly to implementation without separate design, specification, or planning documents.

Distinguish advice from execution: `guide` recommends a route, while `deliver-feature` manages authorized work along it. A request to fix a bug belongs with `fix-bug`; a request to understand the cause without edits belongs with `investigate`. Recommend a conversation or explanation when no specialized workflow is needed. Broader uncertainty or sustained learning may fit `explore` or `teach` if available.

## Make the recommendation usable

Lead with one recommended next step, why it fits, and what the user should get from it. Provide a copyable invocation tailored to their situation, such as `$start-project Help define the first useful version of my personal budgeting app`. Refer to existing artifacts when relevant rather than making the user restate their contents.

Keep the answer short. Show a longer route or alternatives only when the user asks or when a meaningful choice needs explanation. Treat any route as adaptable, not a mandatory sequence.

Finish once the user knows what to do next. When the user has also asked you to proceed, use the chosen skill within that authorization; otherwise leave the example ready for them to invoke. Recommending a skill does not grant additional permissions or require creating a tracking document.
