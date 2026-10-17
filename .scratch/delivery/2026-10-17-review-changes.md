# Queue: 2026-10-17 review changes

Source: [2026-10-17 collection review](../skills/2026-10-17-collection-review.md), recommendations 1–6. Branch `skills-review-2026-10-17`. Mode: parallel.

Repository-wide steps from `AGENTS.md` (tidy-docs, `scripts/sync-skills.sh`, routing cases) run in the main agent after integration, because every item would touch the same files.

| # | Decision | Footprint | Depends on | Status | Commit |
| --- | --- | --- | --- | --- | --- |
| 1 | `queue-work`: each implementer brief says to run git as plain, separate commands from the worktree root, without `cd`, `-C`, `&&`, or pipes. | `skills/engineering/workflow/queue-work/SKILL.md` | — | integrated | `16b67d9` |
| 2 | `warmup`: pass `--skip 0` when the current session already holds earlier work, such as a resumed or continued session. Check that the printed session is not a fork of the current one. | `skills/conversation/warmup/SKILL.md` | — | integrated | `dc52a2d` |
| 3 | `recap`: when relisting items by number or ID, give each a few-word description. | `skills/conversation/recap/SKILL.md` | — | integrated | `48875cd` |
| 5 | `implement`: fix in-scope mechanical consequences of the agreed change, such as stale references, names, and documentation, instead of asking about them. Ask only about choices. Trial. | `skills/engineering/delivery/implement/SKILL.md` | — | integrated | `bc25ec7` |
| 6 | `fix-bug`: handling a state is the fix when the system may legitimately be in that state. When the state should never occur, find what produced it. | `skills/engineering/delivery/fix-bug/SKILL.md` | — | integrated | `235865e` |
| 4 | Global rule to flag own choices beyond approval, moved from qt-market-chart memory to the global `AGENTS.md`. | archon, by handoff | — | handed off, `/tmp/handoff-archon-flag-own-choices.md` | |

No footprint conflicts. Tidy-docs changed only `warmup` wording, folded into its commit. Routing case added in `b13a007`.
