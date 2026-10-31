---
name: guide
description: Help choose the next engineering activity or skill from the user's situation. Use when the user asks where to start, what to do next, or how to use the engineering skills, rather than asking to execute an already chosen task.
---

Recommend a useful next step without requiring the user to understand the skill catalog first. Use the supplied situation, or the current conversation if none is supplied. Guidance alone does not start implementation or a delivery workflow.

## Understand where the user is

Identify the desired outcome, what is already settled or completed, and what currently prevents progress. Use relevant conversation and existing project artifacts before asking the user to repeat information. Inspect only enough context to choose the next activity. A routing question does not require a full codebase review.

A new project may have no repository, specification, or technical choices yet. Start from the idea and explain the next activity in ordinary language. If a missing distinction would change the recommendation, ask one focused question, offering concrete possibilities when helpful.

## Choose the next activity

Use the map below as a starting point. Read the recommended skill before describing its behavior or invoking it, and check its availability in the current environment. If it is unavailable, explain the activity directly and make the limitation clear.

| Situation | Skill |
| --- | --- |
| Establish a new project's purpose, users, and first useful scope | [start-project](../../planning/start-project/SKILL.md) |
| Clarify what one feature should do and what it excludes | [shape-feature](../../planning/shape-feature/SKILL.md) |
| Answer a concrete unknown with evidence or an experiment | [investigate](../../investigation/investigate/SKILL.md) |
| Try an interaction, compare UI alternatives, or explore a logic model before implementation | [prototype](../../investigation/prototype/SKILL.md) |
| Choose a technical approach or resolve design tradeoffs | [design](../../planning/design/SKILL.md) |
| Preserve agreed requirements and acceptance criteria | [write-spec](../../planning/write-spec/SKILL.md) |
| Divide agreed work into verifiable tasks and dependencies | [plan](../../planning/plan/SKILL.md) |
| Build a clear, scoped change the user waits for | [implement](../../delivery/implement/SKILL.md) |
| Assess an existing change before proceeding | [review-code](../../delivery/review-code/SKILL.md) |
| Diagnose and repair unexpected behavior | [fix-bug](../../delivery/fix-bug/SKILL.md) |
| Reduce a measured performance cost, such as latency or frame time | [optimize](../../delivery/optimize/SKILL.md) |
| Improve selected code structure while preserving behavior | [refactor](../../delivery/refactor/SKILL.md) |
| Publish or deploy verified work to a specified target | [release](../../delivery/release/SKILL.md) |
| Have the agent coordinate a feature or backlog across activities and tasks | [deliver](../deliver/SKILL.md) |
| Implement agreed items in the background while the discussion continues | [queue-work](../queue-work/SKILL.md) |
| Find structural problems worth addressing in existing code | [review-architecture](../../investigation/review-architecture/SKILL.md) |
| Assess whether the product helps its intended users | [review-product](../../investigation/review-product/SKILL.md) |
| Give agents a scripted way to drive the real application and capture evidence | [create-verification](../create-verification/SKILL.md) |
| Improve the development process after observed friction | [improve-workflow](../improve-workflow/SKILL.md) |
| Review the skill collection or compare it with external skill repositories | [maintain-skills](../maintain-skills/SKILL.md) |

Neighboring skills are easy to confuse:

- An interface, data shape, or module boundary belongs to `design`, even when it feels like a product question. `shape-feature` decides user-visible behavior and scope. `interrogate` stress-tests a decision the user has already proposed.
- Explaining how existing code works belongs to `clarify` or `investigate`. Trying alternatives belongs to `prototype`.
- Where the current work or discussion stands, including its decisions and status, belongs to `recap`. Restating the user's goal from their own words belongs to `restate`. Continuing in another session belongs to `handoff`. Getting back into a project after a break belongs to `warmup`. Discussing one topic in its own session and bringing the result back belongs to `spawn`, `yield`, and `collect`.
- `deliver` carries agreed work to its endpoint on its own. `queue-work` keeps the user deciding each item while the agreed ones are implemented in the background.

Choose the activity that resolves the immediate obstacle. Evidence gathering precedes decisions that depend on it. Settled decisions do not need another interview. A small, clear change can go directly to implementation without separate design, specification, or planning documents.

Distinguish advice from execution: `guide` recommends a route, while `deliver` manages authorized work along it. A request to fix a bug belongs with `fix-bug`. A request to understand the cause without edits belongs with `investigate`. Recommend a conversation or explanation when no specialized workflow is needed. Broader uncertainty or sustained learning may fit `explore` or `teach` if available.

## Make the recommendation usable

Lead with one recommended next step, why it fits, and what the user should get from it. Provide a copyable invocation tailored to their situation, such as `$start-project Help define the first useful version of my personal budgeting app`. Refer to existing artifacts when relevant rather than making the user restate their contents.

Keep the answer short. Show a longer route or alternatives only when the user asks or when a meaningful choice needs explanation. Treat any route as adaptable, not a mandatory sequence.

Finish once the user knows what to do next. When the user has also asked you to proceed, use the chosen skill within that authorization. Otherwise leave the example ready for them to invoke. Recommending a skill does not grant additional permissions or require creating a tracking document.
