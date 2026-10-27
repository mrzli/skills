# Skill collection review, 2026-10-27

Follows the [2026-10-20 review](2026-10-20-collection-review.md). The user's decisions, applied on branch `skills-review-2026-10-27`:

- 1: approved. The implementer rules moved to `queue-work/worktree-agent.md`, which each implementer reads from its installed path instead of getting a copy in its brief. `implement` stays the per-item procedure. The file also forbids shell variables, command substitution, and loops in any call, which caused 62 refusals.
- Topic B, added in discussion: choices beyond approval in three levels. Routine choices are not listed. Easily reversed choices are listed once and count as accepted when the user's next reply does not object. Decisions are asked first and stay open until answered. The global rule is handed off to archon in `/tmp/handoff-archon-choice-levels.md`. `recap` leaves out choices accepted that way, and the `queue-work` report follows the user's rules for reporting choices.
- 2: approved. The `recap` description adds status and single-topic recaps, with a new routing case.
- 3: approved. `yield` marks each agreed item `now` or `backlog`, `collect` queues only `now` items and adds the rest to the project's backlog, and `queue-work` and the README follow.

## Scope and sources

- The resolved skill was `skills/engineering/workflow/maintain-skills/SKILL.md`. The installed copy is identical.
- Matt Pocock's skills: `5beb35b` to `59db609`. The only in-scope change is to `setup-matt-pocock-skills`, which configures his own issue trackers and has no local counterpart.
- pstack: `88d4751` to `519d36a`. Read `ketchup-video` (`3c0fdb4`) and the `reflect` plugin-cache fix (`7054003`). Screened the `statechart` series (`eb4db2b` to `740d2c0`), the `swarm`, `worktree-audit`, and `watch-pr` fixes, and the version bumps by title.
- Transcripts from 2026-10-20 12:47 UTC to 2026-10-27: 789 user messages in about 50 main sessions in trading-app, archon, learning, trading-fetch-eodhd, flashcards-be, and mrzli-github-io, plus 77 trading-app subagents, 68 of them in worktrees. The one Codex session was a `spawn` environment probe, which is development work. A subagent audited them. The stale `queue-work` copy in session `fc6d8081` was spot-checked: 6 compactions, the old git-only sentence 20 times, and no shell-forms sentence from the skill.
- Invocation settings agree between `disable-model-invocation` and `agents/openai.yaml` for every skill that has both.

## Usage since 2026-10-20

From `skill-usage.sh --since 2026-10-20 --exclude-cwd <this repo> skills`. Skills with no use are omitted.

```txt
skill                invoked  read  last
design               1        0     2026-10-20
review-architecture  1        0     2026-10-26
review-code          1        0     2026-10-25
queue-work           1        2     2026-10-25
clarify              2        0     2026-10-22
improve-workflow     2        0     2026-10-26
optimize             2        0     2026-10-27
warmup               2        0     2026-10-26
investigate          3        0     2026-10-27
collect              3        1     2026-10-26
glossary             3        1     2026-10-25
spawn                3        1     2026-10-27
writing-text         3        1     2026-10-26
fix-bug              3        2     2026-10-25
writing-agents       4        0     2026-10-26
recap                4        1     2026-10-27
handoff              4        4     2026-10-27
yield                19       1     2026-10-26
implement            64       5     2026-10-27
```

The script counts fewer `spawn` and `collect` uses than the audit (17 `/spawn`, 14 `/collect`), likely because nested forks share transcripts. Never used since the collection began: `maintain-skills` outside this repository, `prototype`, `release`, `review-product`, and `start-project`. The collection is four weeks old, so none meets the several-months retirement threshold.

## Evaluation of the 2026-10-20 changes

- **One git command per call, and the 10-21 shell-forms rule:** works when it reaches implementers. With the full shell-forms sentence, refusals were 0.62 per worktree agent (16 agents), against 1.2 before. After the first compaction on 10-25, the long trading-app session ran on its 10-19 copy of `queue-work`, and refusals rose to 3.06 per agent (35 agents, 107 refusals). Remaining shapes: `cd` with Python heredocs (47), chained git (35), shell variables (33), loops (29), `cat >` heredocs (7).
- **Own branch (10-25):** worked once the main agent added it to prompts itself. All 28 implementers from 10-25 17:21 reset their own branch. Earlier that day six created new branches.
- **Footprints include docs:** no stale docs found after a queued item. Keep.
- **Implicit `queue-work` (trial):** "queue up FS1" (10-24 20:29) and "If you need to do backlog 53, queue it up" (10-27 11:10) queued without foreground work. No case of queueing when the user wanted it now. Keep.
- **Global ID and response-size rules:** IDs were at line starts. "What is X" questions continue, but they ask what an item means. Length complaints continue: 10-24 13:52 after 459 words, and "put this simply" on 10-24 22:44. Watch.
- **Rerun only the failed check:** the instruction disappeared from prompts after 10-26 11:37, the same staleness as above. One implementer ran the full verify 19 times for 6 commits.

## Observed friction

1. **Stale skill after compaction.** See the evaluation above. It caused most refusals in the period and the dropped check rule.
2. **`recap` underloads.** About 14 recap or status requests against 4 loads, including "Give me a recap for levels" (10-24 20:30). One inline recap was incomplete (10-24 12:52): "That's not all of it. I remember discussing test tickers."
3. **`collect` starts work the user meant for the backlog.** "/collect … don't start implementation" (10-25 18:17) and "don't implement theme change yet, just add it to the backlog" (10-26 15:21).
4. Once each: a mechanical doc sync offered as an optional item (10-24 13:54), an unrequested backlog addition (10-24 12:54), and `fix-bug` loaded from a pasted handoff that asked for analysis only (10-24 20:58).

Positives: forks were used heavily, including nested ones, and `collect` held back agreed changes that conflicted with merged work. `optimize` measured and discarded a precompiled-headers trial against the user's 15% bar. The user approves in bulk by ID.

## Recommendations

| # | Change | Evidence | Kind |
| --- | --- | --- | --- |
| 1 | **`queue-work`: implementers read their rules from a file.** Move the implementer rules into a companion file. Each brief gives its installed path and tells the implementer to read it first. | Friction 1 | Observed, frequent |
| 2 | **`recap` description (trial).** Add "status" and "where we are" phrasing, and a routing case for a recap of one topic. | Friction 2 | Observed, one bad outcome |
| 3 | **`yield` and `collect`: implement now or later.** `yield` records whether the user agreed to implement each item now or only to add it to the backlog. `collect` starts only the first. | Friction 3 | Observed twice |

Evaluation:

- 1: refusals per worktree agent stay near 0.6 after compactions, and no implementer creates a branch.
- 2: keep if recap requests in long sessions load `recap`. Revert if it loads for requests to explain one item, which belong to `clarify`.
- 3: no "don't implement yet" after `/collect`.

## Declined

- `ketchup-video`: a video catch-up does not fit terminal sessions, and `recap` covers the need.
- `statechart`: it depends on TLA+ models, which the 10-20 review declined.
- `reflect` plugin-cache routing: no in-place edits of installed skills were observed. The global rule on managed files covers it.
- Retirements: none qualify yet.

## Unused skills and upstream workflows

Discussed with the user after the decisions. No change now.

- Matt Pocock's flow runs through specs, tickets, and pull requests. pstack adds many parallel agents with required verification, and principles as separate skills. The user's flow runs in the conversation: items get IDs and are approved in bulk, forks handle side discussions, and `queue-work` implements in the background. That explains the low use of `write-spec`, `plan`, and `shape-feature`.
- `deliver`: largely replaced by `queue-work`. The user steers by ID rather than handing over a whole effort, and the one overnight run on 10-19 went through `queue-work`. Consider merging it into `queue-work` or retiring it at the next review.
- `explore`: user-invoked and meant for when the user has no clear goal yet, which is rare. Keep, since it is about 100 words.
- `create-verification`: set up once per project, so low counts are expected. Worth one real trial in trading-app if UI behavior is still checked by hand. The user has not decided on the trial.
- `prototype`: design questions so far were settled by discussion and benchmarks. Keep for visual or interaction questions.
- `start-project` and `release`: rare by nature. Keep. `maintain-skills` and `writing-skills` are used in this repository, which the usage counts exclude.
- Both upstream collections have a `tdd` skill. No observed need yet, so do not add one without evidence.

## Next review

Start from Matt Pocock `59db609`, pstack `519d36a`, and transcripts after 2026-10-27. Decide on `deliver`, and check whether `create-verification` was tried in trading-app.
