# Skill collection state

Where the collection stands, for the next `maintain-skills` review. Keep only what is still open or still guides decisions. Dated reviews in this folder are history, with the evidence behind each decision. The latest is the [2026-11-02 review](2026-11-02-collection-review.md).

## Last in-depth text review

2026-11-02, [text review](2026-11-02-text-review.md), against archon `965ca62` and the skills at master `446260d`. Recommend the next one when the global rules or many skills have changed substantially since then.

## Next review

Start from Matt Pocock `4ae2317`, pstack `ae5650f`, and transcripts after 2026-11-02. Most 10-27 trials barely ran, because the longest session used older skill copies, so judge them again.

## Open trials

| Change | Since | Keep if | Revise or revert if |
| --- | --- | --- | --- |
| `recap` has a view of only what waits on the user, and the user-invoked `pending` runs it (handoff from trading-app) | 11-02 | Requests like "list everything I need to answer" get the short view, and the user uses `/pending` | The view drops something the user needed, or `pending` goes unused |
| `recap` has a progress view that gives each item's time, estimates for running and remaining items, and totals of work time and wait time. The user-invoked `progress` runs it, and `queue-work` records each item's times (handoff from trading-app) | 11-04 | Requests like "what's done and what remains" get the short view, its estimates come close to the real times, and the user uses `/progress` | Estimates stay far off despite recorded times, the time records bloat the queue file, or `progress` goes unused |
| Skills refer to other skills by name, not by path, and fix-bug and optimize share `measurement.md` through `skills/shared/references/` | 11-04 | No more failed reads of paths like `~/.claude/skills/delivery/refactor/SKILL.md`. Before, 4 queue-work implementers in one trading-app session failed to read one | Agents fail to find a skill by name, or skip a named skill they should have read |
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

Watch without a change: responses that are too long ("put this simply").

## Declined

Do not propose these again without new evidence:

- `tdd`: `implement` already asks for a failing test first when it helps, and for tests through stable interfaces. The user rejected a mandatory test-boundary gate on 10-05.
- Formal verification (`create-formal-verification-skill`, `statechart`): no need yet. Revisit if trading-app's storage or fetcher gains concurrency or invariants that tests reach poorly.
- Principle skills, multi-model or cloud orchestration, PR stacks, `why`, and video or diagram catch-ups such as `ketchup-video`: they don't fit solo terminal work, or the global `AGENTS.md` and existing skills cover them.
- Covered locally: `ketchup` and `recall` (`recap`), `bro` (`clarify`), `in-your-own-words` (`restate`), and `sharpen` (`restate`, `guide`, and `design`).

## Retired

The user retired these to keep the collection to what they use, and wants them back when they would help. Each review checks the reviewed work for these situations, and recommends restoring a skill when the situation came up and the work went worse without it. Restore one with `git checkout <commit>^ -- <path>`, finding its path with `git show --stat <commit>`. Restore a retired mode from the same commit's diff of its skill and scripts. Restore its README, `guide`, and caller references from the same commit's diff, then follow the repository's steps for a skill change.

| Skill | Retired in | Situation it covered | Representative request |
| --- | --- | --- | --- |
| `deliver` | `99703ea`, 2026-11-02 | Hand over a whole feature or backlog to run unattended through every stage | "Go through the whole review backlog, implement each item, and get it all done." |
| `write-spec` | `0503470`, 2026-11-02 | Agreed behavior needs a durable specification with acceptance criteria to guide implementation | "Write down what we agreed about the indicator panel so it can guide implementation." |
| `plan` | `0503470`, 2026-11-02 | Agreed work is too large for one change and needs tasks with dependencies | "Break the renderer unification into tasks we can do one by one." |
| `shape-feature` | `0503470`, 2026-11-02 | A feature idea needs its user problem, scope, and exclusions pinned down before design | "I want to add drawing tools to the chart, but I'm not sure what exactly they should do yet." |
| `start-project` | `0503470`, 2026-11-02 | A new project needs its purpose, users, and first useful scope | "I'm thinking of starting a new app for tracking my workouts. Help me figure out what it should be." |
| `prototype` | `0503470`, 2026-11-02 | A UI or interaction choice needs alternatives the user can try. `design` now builds a small disposable demonstration itself | "Show me two or three ways the crosshair tooltip could look so I can pick one." |
| `review-product` | `0503470`, 2026-11-02 | Judge whether a product helps its users, from feedback and usage | "Is this chart app actually useful for how I trade? What should I improve or drop?" |
| `release` | `0503470`, 2026-11-02 | Publish a version or deploy by a procedure, then verify the result. mrzli.github.io deploys through a GitHub Action | "Publish the setup changes to the main machine and check they applied." |
| `create-verification` | `0503470`, 2026-11-02 | Agents need a scripted way to drive the real application, when the user checks behavior by hand | "I keep having to check the chart by hand after every change, can agents check it themselves?" |
| `explore` | `0503470`, 2026-11-02 | A vague interest or difficulty with no goal yet | "I'm kind of interested in something around music, not sure what." |
| `spawn full`, a mode of `spawn` | `dda0bac`, 2026-11-04 | A fork needs the whole conversation rather than a brief. None of the 47 recorded forks used it. A built-in clone, `claude --resume <id> --fork-session`, with a same-machine handoff back covers the need | "Fork this whole conversation so I can dig into F2 with everything we said." |

## Method notes

- `skill-usage.sh` counts sessions, and nested forks share them, so it undercounts `spawn`, `yield`, and `collect`. It excludes this repository, where `maintain-skills` and `writing-skills` are used. Claude Code transcripts begin on 2026-10-06, when the user started using Claude, and are kept for 365 days. Codex transcripts go back to 2026-07.
- Routing cases run in fresh sessions, so they cannot reproduce misses in long sessions, such as `recap` not loading. Use transcript audits for those.
