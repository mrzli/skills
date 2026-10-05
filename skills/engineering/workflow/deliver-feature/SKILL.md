---
name: deliver-feature
description: Coordinate a feature through clarification, planning, implementation, verification, and authorized delivery. Use when the user wants the whole feature completed across multiple tasks rather than manually driving each activity.
---

Carry the feature to the user's requested endpoint using the relevant skills. Choose activities based on the work. A small change does not need every stage or a separate artifact for each one.

## Establish the outcome and state

Read the request, existing feature artifacts, project instructions, and working tree. Identify acceptance criteria, current progress, and the endpoint: verified local code, a pull request, or a release. Honor existing authorization. The skill's name alone does not authorize a push, merge, or deployment.

Reuse the current specification and plan when they remain accurate. For work spanning tasks or sessions, keep a durable progress record in the existing plan or `.scratch/delivery/<feature-slug>.md`. Record artifact links, decisions, task dependencies and status, relevant revisions, verification evidence, and the next action. On resumption, reconcile the record with actual repository and external state before repeating work.

## Choose the necessary activities

- Use [shape-feature](../../planning/shape-feature/SKILL.md) for unresolved user behavior or scope.
- Use [investigate](../../investigation/investigate/SKILL.md) to gather evidence for a concrete unknown, and [design](../../planning/design/SKILL.md) for consequential technical choices.
- Use [write-spec](../../planning/write-spec/SKILL.md) when agreed requirements need a durable specification, and [plan](../../planning/plan/SKILL.md) when the work needs a task breakdown.
- Use [implement](../../delivery/implement/SKILL.md) for each ready task. Pass its scope, requirements, prerequisites, and verification expectations.
- Use [review-code](../../delivery/review-code/SKILL.md) for review and [release](../../delivery/release/SKILL.md) when the requested endpoint includes an authorized release.

Read the applicable skill before using it. Carry its output into the next activity rather than asking the user to restate information. If a skill is unavailable, perform the bounded activity directly when feasible and report material limitations.

Ask for user judgment only when evidence cannot resolve a consequential decision. Continue independent work while waiting. Reuse settled decisions and update affected artifacts when new evidence requires a change of approach. Do not quietly expand the feature.

## Execute and integrate

Work on tasks whose prerequisites are satisfied. Use sequential execution by default. If delegation is separately authorized and useful, give each worker a bounded task and coordinate shared files, branches, and state. Skills define the procedure. Continuation and concurrency depend on the tools actually available.

Update task status from evidence, not intent. Capture blockers precisely and switch to independent work when possible. Inspect failures and change the approach rather than repeating ineffective actions without new evidence.

After the tasks are integrated, verify the feature's acceptance criteria and important interactions across task boundaries. Reuse valid task checks and reviews. Add an integrated review for consequences they did not cover. Resolve blocking findings and rerun affected checks after corrections.

## Finish or hand off

Proceed to the authorized endpoint once its prerequisites are met. Complete preparation before requesting any missing external-action approval. Keep local completion distinct from release completion.

Finish when the requested endpoint and acceptance criteria are evidenced. If a decision, access limitation, or session boundary prevents completion, save the exact state, remaining work, and next action. Report what was delivered, supporting verification, and unresolved limitations without marking blocked or unverified work complete.
