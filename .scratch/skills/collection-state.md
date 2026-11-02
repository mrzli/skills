# Skill collection state

Where the collection stands, for the next `maintain-skills` review. Keep only what is still open or still guides decisions. Dated reviews in this folder are history, with the evidence behind each decision. The latest is the [2026-11-02 review](2026-11-02-collection-review.md).

## Next review

Start from Matt Pocock `4ae2317`, pstack `ae5650f`, and transcripts after 2026-11-02. Most 10-27 trials barely ran, because the longest session used older skill copies, so judge them again.

## Open trials

| Change | Since | Keep if | Revise or revert if |
| --- | --- | --- | --- |
| `clarify` description names "what is X", "clarify X", "explain X", "in plain words", and ELI5 | 11-02 | Explanation requests load `clarify`. Before, it was 2 of about 70, including a literal "clarify B2" | Loads stay rare, or it loads for recaps |
| Global rule: say what kind each introduced item is and why it matters (archon handoff) | 11-02 | No more "what is this, a bug or an improvement?" in forks | The frustration continues, or item introductions grow long |
| Global rule: a small file or helper that improves the design is made and listed, not asked about (archon handoff) | 11-02 | No "if it's an improvement, just do it" replies | A lasting change the user wanted to see goes unasked |
| `worktree-agent.md`: rerun only the failed check | 11-02 | Implementers run the full verify about once per fix cycle | Full reruns after each fix continue |
| `queue-work` implementers pick `fix-bug`, `refactor`, or `optimize` per item, and `deliver` is retired | 11-02 | Implementers use the matching skill, and no request goes unserved for lack of `deliver` | Implementers misjudge the kind of item, or the user asks for an unattended whole-effort run |
| `queue-work` and `interrogate` start subagents with a fresh context | 11-02 | Implementers never start as forks of the conversation | Briefs miss context that forks used to carry |
| `review-code` checks secrets, unexplained behavior, and unexplained content in every review, and runs in a fresh agent when it can. `implement` reports which kind of review ran, and `queue-work` reviews an item again unless a fresh agent reviewed it | 10-30 | Reviews run in a fresh agent and report safety findings when there are any, and integration does not review the same commits twice | Reviews fill up with speculative safety notes, reviews never run in a fresh agent, or the same commits are reviewed twice |
| `queue-work` implementers read [worktree-agent.md](../../skills/engineering/workflow/queue-work/worktree-agent.md) from the installed skill | 10-27 | Refusals stay near 0.6 per worktree agent, including after compactions, and no implementer creates its own branch | Implementers cannot read the file, or refusals return to about 3 |
| `collect` queues only `now` items from `yield`, and backlogs the rest | 10-27 | No "don't implement yet" after `/collect` | Items the user wanted now land in the backlog |
| Choice levels in the global `AGENTS.md`, `recap`, and the `queue-work` report | 10-27 | Fewer confirmations, and recaps stop repeating accepted choices | A decision the user should have seen goes unasked |
| `recap` description covers status and single-topic recaps | 10-27 | Recap requests in long sessions load `recap`. Before, it was 4 of about 14 | It loads for requests to explain one item, which belong to `clarify` |
| A working design with a clearly better alternative is a recommended change in `review-code`, and `queue-work` judges implementers' choices by the user's rules | 10-27 | Reviews and reports recommend design changes that the user takes up, without the user first asking for a better design | Reviews fill up with optional notes about style, or a clearly better design still goes unmentioned |

Watch without a change: responses that are too long ("put this simply"), and implementers rerunning the full verify after one failed check.

## Pending decisions

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

- `skill-usage.sh` counts sessions, and nested forks share them, so it undercounts `spawn`, `yield`, and `collect`. Claude Code transcripts begin on 2026-10-06, when the user started using Claude, and are kept for 365 days. Codex transcripts go back to 2026-07.
- Routing cases run in fresh sessions, so they cannot reproduce misses in long sessions, such as `recap` not loading. Use transcript audits for those.
