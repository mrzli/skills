# Skill collection review, 2026-10-20

Follows the [2026-10-17 review](2026-10-17-collection-review.md). The user's decisions, applied on branch `skills-review-2026-10-20`:

- 1, one git command per call: `e7ebe27`.
- 2, revised to searching the whole repository, including docs and comments, for the names an item changes: `09ce310`. The 10-18 footprint did include docs. A search found six more places, and the implementer got them about 20 seconds after it started, so it is unknown whether it would have found them alone.
- 3, extended: `queue-work` has one mode, up to N items at once, 4 by default (`cfaa276`). Agents can load it, and "queue this" starts the item (`eefac1f`). It is the default for agreed items in an ongoing discussion, while `implement` stays the route for one-off requests the user waits on (`4df1ee2`).
- 4, handed off for archon in `/tmp/handoff-archon-response-rules.md`. Response size is judged by how much the user must take in, with about 400 words of prose as a rough check, not a limit. Measured reactions were 384 words "a lot", 603 words "a lot", and 425 words with one question praised.
- `create-verification`: keep for now. The user hasn't tried it yet while adapting the workflow. Retirement stays possible if it remains unused once the workflow settles.

## Scope and sources

- The resolved skill was `skills/engineering/workflow/maintain-skills/SKILL.md`. The installed copy is identical.
- Matt Pocock's skills: `49dd158` to `5beb35b`. The only change is to `skills/in-progress/chief-of-staff`, which is outside the reviewed directories.
- pstack: `101b274` to `88d4751`. Read the `ketchup` changes (`16541c6`, `bc14437`), `create-formal-verification-skill` (`4382e68`), and its maintenance companion (`7b353f7`). The `sharpen` back-and-forth, the packaging fixes, and the version bumps were screened by title.
- Transcripts from 2026-10-17 14:30 UTC to 2026-10-20 12:47 UTC: twelve Claude sessions in trading-app, trading-fetch-eodhd, archon, and learning, plus about 75 implementer subagents. There were no Codex sessions. A subagent audited them. Five quotes and the trading-app memory files were spot-checked.
- qt-market-chart was renamed to `trading-app` on 10-17. The 36 routing cases with the old path could not run. Commit `e6e6c79` points them at the new path.

## Usage since 2026-10-17

From `skill-usage.sh --since 2026-10-17 --exclude-cwd <this repo> skills`. Skills with no use are omitted.

```txt
skill                invoked  read  last
plan                 0        1     2026-10-17
writing-skills       0        1     2026-10-17
clarify              1        0     2026-10-18
tidy-docs            1        0     2026-10-17
improve-workflow     1        2     2026-10-18
writing-text         1        2     2026-10-19
fix-bug              2        0     2026-10-19
guide                2        0     2026-10-19
investigate          2        0     2026-10-19
writing-agents       3        0     2026-10-19
warmup               4        1     2026-10-19
handoff              5        0     2026-10-19
queue-work           5        0     2026-10-19
design               7        1     2026-10-20
glossary             8        2     2026-10-19
implement            46       0     2026-10-20
```

## Routing

Three cases for skills changed on 10-17 (`plan` and `improve-workflow`), with the installed skills. All three passed, including the new repeated-steps case.

```txt
case  expected          loaded            verdict
1     plan              plan              pass
2     improve-workflow  improve-workflow  pass
3     improve-workflow  improve-workflow  pass
```

## Evaluation of the 2026-10-17 changes

- **`queue-work` git rule:** implementers followed it. Single plain git commands rose from 31 to 294. Refusals fell from about 3.3 per worktree agent to 1.2. The remaining refusals are mostly calls that combine git with `; echo $?`, Python heredocs that mention git, and two `git -C` runs on the shared checkout. Revise.
- **Build seeding:** 42 of 43 trading-app worktrees seeded their build, against 6 of 26 before. Three seeded builds were stale, and the project fixed that in its own tooling on 10-18. Keep.
- **Rerun only the failed check:** compliance was mixed. One implementer ran the full `verify` six times in 20 minutes. Time in checks stayed at about 27% of implementer time. Keep, and watch.
- **`warmup`:** it summarized the right session when fresh and when resumed. The retrospective suggestion fired when no record existed, and not after one was made. Keep.
- **`recap` descriptions:** relisted items had short descriptions, and no one asked for them. Keep. `recap` itself did not load for about ten relist requests in long sessions, but the inline lists were good.
- **`implement` mechanical consequences (trial):** no "just fix" from the user, and no unflagged change made in the name of consistency. One miss was upstream of the implementer. The main agent's footprint for a queued item left out docs that described the old import form, and the user had to ask (10-18 09:35). Keep the trial running.
- **`improve-workflow` scan:** used once (10-18 15:57). It ran `repeated-steps.py` and saved the output, and two tooling items came of it and were approved. Keep.
- **`fix-bug` guard note:** not observable yet.

## Observed friction

1. **Queueing intent missed.** At 10-18 08:00 the user interrupted with "I just wanted to queue this work". `queue-work` is user-invoked, so the agent could not load it and started the work in the foreground.
2. **IDs buried in prose.** At 10-20 08:43: "I don't know what AG1 or AG2 is." The IDs appeared only in parentheses at the ends of paragraphs. Also 10-18 12:56: "I do not understand O1".
3. **User preferences in one project's memory.** trading-app's private memory holds two general preferences that other projects don't see. `no-speculative-structure` says to ask before adding a permanent module only to demonstrate a capability (10-18 12:06). `response-size` says to judge a response by its total text, so a heavy question goes alone (10-19 21:52). Responses were too long twice (10-17 14:32, 10-19 11:22).
4. **Docs missing from a footprint.** See the `implement` evaluation above.
5. Resolved since by global rules: a cheaper option recommended over a better one (10-18 16:18), and a home-directory file edited in place instead of through archon (10-18 16:29, 10-19 19:39).

Positives:

- An overnight queue (10-19 23:15 to 10-20 02:30) finished four pieces of work with a clear morning report.
- Choices beyond approval were listed consistently.
- Agents confirmed before pushing and before deleting files on an external drive.
- The proactive-handoff rule was followed while it was still a draft.

Not exercised: `deliver`, `optimize`, `create-verification`, and `plan` as a loaded skill. At 10-19 22:59 an agent said it would use `plan`, then wrote the plan straight into the queue file.

## Recommendations

| # | Change | Evidence | Kind |
| --- | --- | --- | --- |
| 1 | **`queue-work`: one git command per shell call.** Reword the rule so each call runs one git command and nothing else, with no `cd`, `-C`, `;`, `&&`, pipes, or `$?`. | Remaining refusals | Observed, frequent |
| 2 | **`queue-work`: footprints include docs.** Count the docs and conventions that describe what the item changes as part of its footprint. | Friction 4 | Observed once, cheap |
| 3 | **Let agents load `queue-work` (trial).** Allow implicit invocation so "queue this" can add an item. The skill already reserves starting a batch for the user. Existing near-miss case 37 checks that it does not load for "implement now". | Friction 1 | Observed once |
| 4 | **Global rules,** by handoff to archon. (a) Put each ID at the start of its bullet or line, never only inside a sentence. (b) Move the two trading-app preferences, no speculative structure and response size, into the global `AGENTS.md`. Then delete the memory notes. | Frictions 2 and 3 | Observed twice each |

Evaluation:

- 1: refusals per implementer fall well below 1.2 in the next parallel run.
- 2: no user prompt to update docs after a queued item.
- 3: keep if "queue this" adds an item without starting work, and case 37 still passes. Revert if `queue-work` loads for requests to implement now.
- 4: no "what is X1" questions, and no complaint about long responses.

## Declined

- `ketchup`'s rule to list every waiting item. The global ID rule and `recap` already cover it.
- `create-formal-verification-skill`. No observed need yet. It is worth revisiting if trading-app's storage or fetcher gains concurrency or invariants that tests reach poorly.
- Changing `recap` or `clarify` routing. They did not load in long sessions, but the inline answers were good, as on 10-14.
- `create-verification`: the 10-17 review said to ask the user before this review. Asked as a question, not a recommendation.

## Next review

Start from Matt Pocock `5beb35b`, pstack `88d4751`, and transcripts after 2026-10-20 12:47 UTC. Check the evaluations above, and real use of `deliver`, `optimize`, `create-verification`, and `plan`.
