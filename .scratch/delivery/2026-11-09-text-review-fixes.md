# Queue: apply the 2026-11-09 text review

Applies the approved items of [the 2026-11-09 text review](../skills/2026-11-09-text-review.md). Item numbers in parentheses are the review's. Base: branch `text-review-2026-11-09`. N = 4.

Implementers do not run `tidy-docs`, `sync-skills.sh`, or routing cases. The main agent runs them once after all items are integrated, since each is repository-wide.

## 1. Delivery skills

- Decision: review items 1 (`implement` part only), 5, 32, 35, 36, 37, 38, 40, and 41 (the `implement:23` and `refactor:18` parts).
- Footprint: `skills/engineering/delivery/{implement,fix-bug,refactor,optimize}/`.
- Depends on: none. Model: haiku.
- Status: integrated. Commits 8972c0a..abe90d7, follow-up 3963faf. Times: not recorded per item. Measurements: haiku; review opus, 1 major left for integration (resolved by item 2), 1 fix round; checks none required.

## 2. Review and planning skills

- Decision: review items 1 (`review-code` part), 2, 3, 4 (`review-code` and `review-architecture` only), 6 (`review-code` owns the scale), 7, 39, 41 (the `design`, `review-code`, `review-architecture` parts), 42, 43 (skill part only), 44.
- Footprint: `skills/engineering/delivery/review-code/`, `skills/engineering/planning/design/`, `skills/engineering/investigation/{investigate,review-architecture}/`.
- Depends on: none. Model: haiku.
- Status: integrated. Commits d8c52b6..e712dd3, follow-up 2387b1c (severity grades rewritten for code), e6963cd. Times: not recorded per item. Measurements: haiku; review opus, 0 blocking, 0 major, 4 minor, 4 nit, 1 fix round.

## 3. queue-work

- Decision: review items 4 (`queue-work` report part), 6 (callers refer to `review-code`'s scale), 11, 12, 13, 14, 34, 41 (`queue-work:65`, `:67`), 52, 53, 54, 55.
- Footprint: `skills/engineering/workflow/queue-work/`.
- Depends on: none. Model: haiku.
- Status: integrated. Commits eb825ac..584e1ed, follow-up 3963faf. Times: not recorded per item. Measurements: haiku; review opus, 0 blocking, 0 major, 2 minor, 2 nit, 1 fix round.

## 4. maintain-skills, improve-workflow, guide, old reviews

- Decision: review items 15, 16, 17, 18 (skill part), 56, 57. Item 16 includes judging which dated reviews in `.scratch/skills/` and `.scratch/workflow/` have nothing open and nothing pointing to them, and removing those.
- Footprint: `skills/engineering/workflow/{maintain-skills,improve-workflow,guide}/` (not their scripts), `.scratch/skills/`, `.scratch/workflow/`.
- Depends on: none. Model: opus (item 16 needs judgment on open items).
- Status: integrated. Commits ecbb868..1cb7e7d, follow-up 9bbbfef. Times: not recorded per item. Measurements: opus; review opus, 0 blocking, 0 major, 1 fix round.

## 5. Conversation and learning skills

- Decision: review items 8, 9 (keep `.scratch/learn/`, say it stays in use while the course continues), 33, 45, 46, 47, 48, 49, 51.
- Footprint: `skills/conversation/`, `skills/learning/`, `skills/shared/scripts/agent-joins.sh`.
- Depends on: none. Model: haiku.
- Status: integrated. Commits 55019a6..a6bba5b, follow-up b2e477c. Times: not recorded per item. Measurements: haiku; review opus, 0 blocking, 0 major, 1 minor left (fixed in b2e477c), 1 fix round; bash -n passed.

## 6. Docs skills, repository files, shared reference

- Decision: review items 19, 20, 21, 22, 23, 24, 58, 59, 60, 61.
- Footprint: `skills/docs/`, `AGENTS.md`, `scripts/sync-skills.sh`, `skills/shared/references/measurement.md`.
- Depends on: none. Model: haiku.
- Status: integrated. Commits 0e11dd1..1e3acdc. Times: not recorded per item. Measurements: haiku; review opus, 0 blocking, 0 major, 0 fix rounds; unittest 13 OK first run.

## 7. Transcript-reading scripts

- Decision: review item 10. The user accepts relying on the undocumented transcript layouts. Add to each script that reads them a header comment naming the relied-on layout, and a small fixture test.
- Footprint: `skills/conversation/warmup/scripts/`, `skills/engineering/workflow/maintain-skills/scripts/skill-usage.sh`, `skills/engineering/workflow/improve-workflow/scripts/`, new test files beside them.
- Depends on: 4 and 5 (same skill folders). Model: opus (test placement is open).
- Status: integrated. Commits 66d0c88..cf38a68, follow-up dc94afb (folder naming bug confirmed by experiment). Times: not recorded per item. Measurements: opus; review opus, 1 major left (fixed in dc94afb), 1 fix round; tests failed first run on a real bug, then 22 OK.

## 8. README

- Decision: review items 18 (README part), 43 (`README:117`), 50, and catalog entries that items 1 to 6 change.
- Footprint: `README.md`.
- Depends on: 1 to 6. Model: haiku.
- Status: integrated. Commits 56d1e93, 062890f, follow-up 25d155a. Times: not recorded per item. Measurements: haiku; review opus, 0 blocking, 0 major, 2 nit, 0 fix rounds.

## 9. archon handoff

- Decision: review items 25 to 31 and 62, as a handoff to archon. Written by the main agent.
- Footprint: a handoff file outside this repository.
- Depends on: none.
- Status: done. Handoff at /tmp/handoff-archon-text-review-2026-11-09.md.

Times: the queue started at 21:07, and all items were integrated by 21:22, with items 1 to 4 running first, then 5 and 6, then 7 and 8. Per-item times were not recorded.

After integration: tidy-docs (a2dcf67), routing cases added (d2895b6), sync-skills made no changes. A fresh opus agent reviewed the main agent's follow-up commits in about 48 seconds: no blocking or major findings, three nits fixed as suggested in ae266f7.
