# Skill collection state

Where the collection stands, for the next `maintain-skills` review. Keep only what is still open or still guides decisions. Dated reviews in this folder are history, with the evidence behind each decision. The latest is the [2026-10-27 review](2026-10-27-collection-review.md).

## Next review

Start from Matt Pocock `59db609`, pstack `519d36a`, and transcripts after 2026-10-27.

## Open trials

| Change | Since | Keep if | Revise or revert if |
| --- | --- | --- | --- |
| `queue-work` implementers read [worktree-agent.md](../../skills/engineering/workflow/queue-work/worktree-agent.md) from the installed skill | 10-27 | Refusals stay near 0.6 per worktree agent, including after compactions, and no implementer creates its own branch | Implementers cannot read the file, or refusals return to about 3 |
| `collect` queues only `now` items from `yield`, and backlogs the rest | 10-27 | No "don't implement yet" after `/collect` | Items the user wanted now land in the backlog |
| Choice levels in the global `AGENTS.md`, `recap`, and the `queue-work` report | 10-27 | Fewer confirmations, and recaps stop repeating accepted choices | A decision the user should have seen goes unasked |
| `recap` description covers status and single-topic recaps | 10-27 | Recap requests in long sessions load `recap`. Before, it was 4 of about 14 | It loads for requests to explain one item, which belong to `clarify` |
| A working design with a clearly better alternative is a recommended change in `review-code`, and `queue-work` judges implementers' choices by the user's rules | 10-27 | Reviews and reports recommend design changes that the user takes up, without the user first asking for a better design | Reviews fill up with optional notes about style, or a clearly better design still goes unmentioned |
| `implement` fixes mechanical consequences instead of asking | 10-17 | No "just fix it" from the user, and no unflagged change in the name of consistency | Either appears |

Watch without a change: responses that are too long ("put this simply"), and implementers rerunning the full verify after one failed check.

## Pending decisions

- `deliver`: never loaded, and `queue-work` covers its main job. Decide whether to fold its unattended long-run guidance into `queue-work` and retire it.
- `create-verification`: worth one real trial in trading-app if UI behavior is still checked by hand. The user has not decided.

## Declined

Do not propose these again without new evidence:

- `tdd`: `implement` already asks for a failing test first when it helps, and for tests through stable interfaces. The user rejected a mandatory test-boundary gate on 10-05.
- Formal verification (`create-formal-verification-skill`, `statechart`): no need yet. Revisit if trading-app's storage or fetcher gains concurrency or invariants that tests reach poorly.
- Principle skills, multi-model or cloud orchestration, PR stacks, `why`, and video or diagram catch-ups such as `ketchup-video`: they don't fit solo terminal work, or the global `AGENTS.md` and existing skills cover them.
- Covered locally: `ketchup` and `recall` (`recap`), `bro` (`clarify`), `in-your-own-words` (`restate`), and `sharpen` (`restate`, `guide`, and `design`).

## Keep, rarely used

`explore`, `prototype`, `start-project`, `release`, and `review-product` have little or no recorded use, because their activities have not come up. `maintain-skills` and `writing-skills` are used in this repository, which the usage counts exclude. Retire none before several months without use.

## Method notes

- `skill-usage.sh` counts sessions, and nested forks share them, so it undercounts `spawn`, `yield`, and `collect`. Transcripts before 2026-10-06 have expired.
- Routing cases run in fresh sessions, so they cannot reproduce misses in long sessions, such as `recap` not loading. Use transcript audits for those.
