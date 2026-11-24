# Queue: 2026-11-24 text review fixes

Items from the [2026-11-24 text review](../skills/2026-11-24-text-review.md) that the user approved on 2026-11-24. Review numbers refer to that record. Branch `text-review-2026-11-24`. The main agent runs `tidy-docs`, `scripts/sync-skills.sh`, and the routing-case update once after all items are integrated.

Not queued yet: review items 1, 7, 14, 17, 18, and 27 are under discussion, and items 6, 9-13, 15, and 16 await the user's answer. The main agent writes the archon handoff for items 39-43.

## 1. Approval and reports in the delivery skills

- Decision: review items 2, 3, 4, 32, 33, and the `refactor:20` part of item 37, as the record proposes. Do not change the order of `implement:45`'s report (review item 1 is still open).
- Footprint: `implement`, `refactor`, `review-code`, `optimize`, `fix-bug` SKILL.md files.
- Depends on: none. Model: Sonnet (judgment across several skills).
- Status: in progress.

## 2. Docs skills

- Decision: review items 5, 31, 38, and the `glossary:31` part of item 37.
- Footprint: `glossary`, `writing-agents`, `writing-skills`, `clarify` SKILL.md files.
- Depends on: none. Model: Haiku (contained docs).
- Status: in progress.

## 3. Cross-session skills

- Decision: review items 8 and 34.
- Footprint: `yield`, `spawn`, `handoff`, `warmup` SKILL.md files, and the usage text of `skills/shared/scripts/agent-joins.sh`.
- Depends on: none. Model: Haiku (contained docs).
- Status: in progress.

## 4. Planning, investigation, guide, and routing cases

- Decision: review items 19, 20, 21, 22, 23, and 36.
- Footprint: `design`, `investigate`, `review-architecture`, `guide` SKILL.md files, and `.scratch/skills/routing-cases.tsv`.
- Depends on: none. Model: Haiku (contained docs).
- Status: in progress.

## 5. queue-work wording

- Decision: review items 24, 25, and 35.
- Footprint: `queue-work/SKILL.md`, `queue-work/worktree-agent.md`.
- Depends on: none. Model: Haiku (contained docs).
- Status: in progress.

## 6. Script fixes and tests

- Decision: review items 26 and 30.
- Footprint: `maintain-skills/scripts/skill-usage.sh`, `scripts/tests/test_skill_usage.py`, `scripts/tests/test_agent_joins.py`.
- Depends on: none. Model: Haiku (contained code and tests).
- Status: in progress.

## 7. The 10-16 check-costs record

- Decision: review item 28. Judge the record's open evaluation from trading-app's queue measurements, then remove it, or report why it should stay.
- Footprint: `.scratch/workflow/2026-10-16-check-costs.md`, README link to `.scratch/workflow` if it becomes stale.
- Depends on: none. Model: Opus (investigation).
- Status: in progress.
