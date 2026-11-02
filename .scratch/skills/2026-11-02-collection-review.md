# Skill collection review, 2026-11-02

Follows the [2026-10-27 review](2026-10-27-collection-review.md). The user's decisions, applied on branch `skills-review-2026-11-02`:

- 1, 4, and 5: approved and applied in this repository.
- 2: approved as a trial. 2, 3, and 6 are handed off to archon in `/tmp/handoff-archon-items-and-improvements.md`.
- 6: the user types "elif" for ELI5, so it is a shorthand rather than a mishearing. It still goes beside the dictation list.
- `deliver`: retired. `queue-work` already keeps a queue file and checks each item as it integrates, so the only part it lacked was choosing the skill per item. Implementers now pick `fix-bug`, `refactor`, or `optimize` per item, and `implement` otherwise. A backlog mode that proposes items to run in parallel waits until the need recurs.

- Collection usefulness, discussed after the review: the user retired the nine skills from the 10-02 engineering set that had little or no use: `write-spec`, `plan`, `shape-feature`, `start-project`, `prototype`, `review-product`, `release`, `create-verification`, and `explore`. The set was built by Codex from a map of the whole engineering process, not from observed needs, and a month of use showed which parts fit. They are listed in [collection-state.md](collection-state.md) with the situations to watch for, and `maintain-skills` now checks for those situations.

## Scope and sources

- The resolved skill was `skills/engineering/workflow/maintain-skills/SKILL.md`. The installed copy is identical.
- Matt Pocock's skills: `59db609` to `4ae2317` (5 commits). In scope: `7739eae` and `a496f55` (subagents get a fresh context, not a fork). `5ae4816` and `4ae2317` are under `skills/in-progress/`, outside the scope. `d1478fc` changes only versioning.
- pstack: `519d36a` to `ae5650f`. Only `ab1f702` (`interrogate` rework into reproduced-only code review) and `c742dd6` (orchestrate playbook rewrite) touch `pstack/`. The rest add third-party MCP plugins.
- Transcripts from 2026-10-27 12:00 UTC to 2026-11-02: 33 main sessions in trading-app (20), archon (10), mrzli.github.io, and learning, with 720 user messages and 106 subagents, 71 of them in worktrees. One trading-app session, `fc6d8081`, began before the window and ran on its old skill copies throughout, with 5 compactions in the window. No Codex sessions. A subagent audited them, and the `clarify B2` miss was spot-checked.
- Invocation settings agree between `disable-model-invocation` and `agents/openai.yaml` for every skill.

## Usage since 2026-10-27

From `skill-usage.sh --since 2026-10-27 --exclude-cwd <this repo> skills`. Skills with no use are omitted.

```txt
skill                invoked  read  last
improve-workflow     1        0     2026-11-02
optimize             1        0     2026-10-27
shape-feature        1        0     2026-10-28
clarify              2        0     2026-11-02
design               2        0     2026-11-02
glossary             2        0     2026-10-31
queue-work           2        4     2026-11-02
investigate          4        0     2026-11-02
warmup               4        0     2026-11-02
recap                4        1     2026-11-02
collect              4        4     2026-11-02
writing-text         4        5     2026-11-02
handoff              5        1     2026-11-02
spawn                5        4     2026-11-02
review-architecture  6        2     2026-11-02
writing-agents       7        1     2026-11-02
yield                17       4     2026-10-31
review-code          25       4     2026-11-02
implement            48       3     2026-11-02
```

Unused in the period: `create-verification`, `deliver`, `explore`, `fix-bug`, `guide`, `interrogate`, `maintain-skills`, `plan`, `prototype`, `refactor`, `release`, `restate`, `review-product`, `start-project`, `teach`, `tidy-docs`, `write-spec`, and `writing-skills`. The audit counted 17 `/collect`, 13 `/yield`, and 12 `/spawn`, more than the script, as before.

## Evaluation of open trials

- **Implementers read `worktree-agent.md` (10-27):** barely exercised. The 5 implementers with the current skill read the file and had 0.4 refusals per agent. The stale session's 43 implementers had 3.2, mostly `cd` with Python heredocs (58) and chained git (29). Behavior after compaction is untested with the new file. No queue-work implementer created its own branch. Keep the trial.
- **`collect` queues only `now` items (10-27):** no "don't implement yet" in 17 collects. One item the user wanted now was recommended for the backlog (10-31 14:45), in the stale session. Keep.
- **Choice levels (10-27):** no recap repeated an accepted choice, and no decision went unasked. Over-asking continues for improvements: "C20 - If this is an architectural improvement just do it" (11-02 14:33, after the agent asked because a small helper "adds a lasting file"), and similar replies on 10-27 19:09, 10-31 03:20, and 10-31 12:09. See recommendation 3.
- **`recap` description (10-27):** about 17 recap or status requests against 5 loads, such as "where are we?" (10-30 23:06) and "what are the remaining things to do" (11-02 13:58). It never loaded for a request to explain one item. Most misses were in the stale session. Keep the trial.
- **`review-code` safety and fresh agents (10-30):** about 48 reviews, all in fresh agents, each with a one-line safety statement and no speculative notes. No double reviews. The user found 47 seconds too long for a trivial docs change (11-02 11:25), which led to the `.scratch/` exemption in the global rules. Keep.
- **Design alternatives in reviews (10-27):** reviews raised design fixes the user accepted, such as JP3a (10-31 10:58). No complaint of a missed better design after 10-27 19:14. Keep.
- **`implement` fixes mechanical consequences (10-17):** no "just fix it" for mechanical consequences, and no unflagged consistency change. Close the trial as kept.

Watch items:

- **Length:** median 227 words before a user message, 90th percentile 411. Complaints: "can this be more concise? I can't read all that" (10-27 22:33, after 357 and 462 words), "there is too much information" (10-28 15:01, 487 words), "I am losing the thread" (10-27 20:55, 364 words).
- **Full verify reruns:** continue with the current skill. An implementer in `c27957a6` ran the full verify 10 times. `worktree-agent.md` does not mention the rule. See recommendation 4.

## Observed friction

1. **`clarify` almost never loads.** About 70 requests to explain against 2 loads, including the literal "clarify B2" (11-02 11:22, confirmed), "clarify IZ1", and "clarify JR2B1".
2. **Unexplained items in forks.** 15 messages of frustration, such as "I have no fucking idea what is this. Is this a bug? Is this an improvement?" (10-31 01:20), "IG1 - also wtf is this?" (10-30 23:22), and repeated "Explain like I'm stupid". Hypothesis: items appear without saying what kind they are or why they matter.
3. **Over-asking about improvements.** See choice levels above.
4. **Dictation:** "elif" for ELI5 (10-28 15:11, 11-02 12:15, 11-02 14:42).
5. **Stale skills in a long session,** as on 10-27. The user ended that session with `/improve-workflow`.

Positives: reviews caught real errors, including 3 factual errors in a docs note. Queues finished cleanly, and finishing a queue is now scripted (`finish-queue.sh`). Bulk approval by ID works.

## Recommendations

| # | Change | Evidence | Kind |
| --- | --- | --- | --- |
| 1 | `clarify` description: name the phrasings users use, such as "explain X", "what is X", "clarify X", "ELI5", "in plain words", or an item ID alone with a question | Friction 1 | Observed, frequent |
| 2 | Global rule (archon handoff): when introducing an item, say in a few words what kind it is, such as a bug, an improvement, or a design choice, and why it matters | Friction 2 | Hypothesis, frequent symptom |
| 3 | Global rule (archon handoff): "large or lasting structure" means a new module, package, or service. A small file or helper inside a change that improves the design is made and listed as a choice | Friction 3 | Observed, 4 times |
| 4 | `worktree-agent.md`: after a failed check, rerun only that check, as the user's rules for checks say, with the fallback | Watch item | Observed |
| 5 | `queue-work` and `interrogate`: start subagents with a fresh context, not a fork of the conversation | Matt Pocock `7739eae` | Upstream, small |
| 6 | Dictation list (archon handoff): "elif" for ELI5 | Friction 4 | Observed, 3 times |

## Declined

- pstack orchestrate retries and worker accounting: no stalled or failed implementers observed. Adopt only with such evidence.
- pstack reproduced-only review: `review-code` already investigates before reporting, and the safety trial shows no speculative noise. A ready fix if that changes.
- `principle-explain-the-number`, autopilot playbooks, and goal restatement in briefs: principle skills and PR stacks are declined, and `optimize`, `restate`, and `queue-work` cover the rest.

## Pending decisions

- `deliver`: still never loaded. On 11-02 14:43 the user asked to "review the backlog, recommend things that can be done in parallel … consider automatically doing some things … whether this would be a skill", which is the opening for folding `deliver`'s unattended guidance into `queue-work`.
- `create-verification`: not tried. UI checks in trading-app ran through QML tests, with no manual checks seen, so the need is weaker than assumed.
