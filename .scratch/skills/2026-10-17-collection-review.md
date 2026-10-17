# Skill collection review, 2026-10-17

Follows the [2026-10-14 review](2026-10-14-collection-review.md) and the [check-cost record](../workflow/2026-10-16-check-costs.md). Recommendations only. Nothing has been applied yet.

## Scope and sources

- The resolved skill was `skills/engineering/workflow/maintain-skills/SKILL.md`. The installed copy is identical.
- Matt Pocock's skills: no changes since `49dd158`.
- pstack: `1e5c90a` to `101b274`. Read `e5136d8` (four principles restated as reasoning), `99743e9` (cuts to interrogate, swarm, and two principles), and `afd51cf` (ketchup with screenshots and diagrams). `6ce45c5` and `182f2ce` are a version bump and Claude Code packaging, screened by title.
- Transcripts after 2026-10-14: nine Claude sessions in qt-market-chart, archon, and learning, plus qt-market-chart implementer subagents. There were no Codex sessions. A subagent audited them. The quotes for items 17 and 18, the warmup mismatch, and the git refusals were spot-checked.
- Invocation settings: Claude Code and Codex agree for every skill. A missing `agents/openai.yaml` defaults to implicit invocation.
- Routing tests were not run, because no skill changed.

## Usage since 2026-10-14

From `skill-usage.sh --since 2026-10-14 --exclude-cwd <this repo> skills`. Skills with no use are omitted.

```txt
skill                invoked  read  last
deliver              0        1     2026-10-15
clarify              1        0     2026-10-15
design               1        0     2026-10-16
guide                1        0     2026-10-14
investigate          1        0     2026-10-16
plan                 1        0     2026-10-14
recap                1        0     2026-10-16
restate              1        0     2026-10-14
tidy-docs            1        0     2026-10-15
warmup               1        0     2026-10-17
queue-work           1        2     2026-10-16
handoff              2        0     2026-10-16
review-code          2        0     2026-10-15
glossary             4        0     2026-10-16
writing-agents       4        1     2026-10-16
writing-text         4        1     2026-10-15
implement            23       1     2026-10-16
```

All time, never invoked or read outside this repository: `improve-workflow`, `maintain-skills`, `optimize`, `prototype`, `release`, `review-product`, `start-project`, `writing-skills`. The collection is under three weeks old, and the reviewed work offered no clear opportunity for any of them.

## Observed friction

1. **Worktree git refusals.** In 24 qt-market-chart transcripts, about 150 git commands from worktree-isolated implementers were refused with "too complex to verify that it stays inside the worktree … Split it into plain, separate commands". Each refusal costs a retry. At 10-16 22:28 UTC the user asked "Why does this issue keep happening?" about a related guard on the main checkout.
2. **Leftovers returned as questions.** At 10-15 20:59 UTC: "item 17. Fix it. I mean, you should have automatically fixed this. If there was a problem, keep things in sync, right? That should be a normal rule." Then "18 just fix, again". The project added a rule to its `code-style.md`.
3. **Relisted items lacked context.** The user asked for the remaining items more than ten times in one session. `recap` loaded twice. At 10-15 20:40 UTC: "Give me a very quick description of each of those so that I know what it's related to without having to ask to clarify every time."
4. **`warmup` read the wrong session.** At 10-17 06:11 UTC, `/warmup` ran in the resumed main session. The script skipped it as the current session and printed the end of the fork instead. The skill says `--skip 0` only "if the user was already working in the current session".
5. **An unflagged own choice.** At 10-16 20:17 UTC: "Why did you also add settings local JSON?" The agent had added an unrequested `.gitignore` line. The rule to list choices beyond approval lives only in qt-market-chart's private memory (`feedback-flag-own-choices`), so other projects do not see it.
6. Smaller: `writing-agents` did not load for an edit to the global `AGENTS.md` in archon (10-15 16:15 UTC). An agent assumed a dictation error for "herdr", which was meant literally.

Positives:

- Parallel `queue-work` ran three times. Footprints held, with no conflicts, and one conflicting pair was serialized correctly.
- After the check-cost fixes, time in checks fell from 30–69% to 20–33% of implementer time. No check failed after `6b1a5d1`, so the rerun-only-the-failure rule is untested.
- `glossary` produced `docs/glossary.md` and a terminology cleanup. `handoff` loaded on its own and worked.
- The question-is-not-a-request rule held in four checked instances.
- Private memory no longer collects design notes. Older notes were moved to project documents.

These were not exercised: `deliver`, `optimize`, `create-verification` (explained, then "Forget about that"), and build seeding beyond the one run after the fix.

## Recommendations

| # | Change | Evidence | Kind |
| --- | --- | --- | --- |
| 1 | **`queue-work`: tell implementers how to run git.** In each brief, say to run git as plain, separate commands from the worktree root, without `cd`, `-C`, `&&`, or pipes. | Friction 1 | Observed, frequent |
| 2 | **`warmup`: handle resumed sessions.** Pass `--skip 0` when the current session already holds earlier work, such as a resumed or continued session. Check that the printed session is not a fork of it. | Friction 4 | Observed once, cheap |
| 3 | **`recap`: describe each listed item.** When relisting items by number or ID, give each a few-word description. | Friction 3 | Observed |
| 4 | **Global rule to flag own choices,** through archon. Move the qt-market-chart memory rule into the global `AGENTS.md`: list each choice made beyond what the user approved when reporting a change. | Friction 5, and 10-11 | Observed twice |
| 5 | **`implement`: finish mechanical consequences.** Fix in-scope consequences of the agreed change, such as stale references, names, and documentation, instead of asking about them. Ask only about choices. Trial it. | Friction 2 | One observation |
| 6 | **`fix-bug`: when a guard is a fix.** Add that handling a state is the fix when the system may legitimately be in that state. When the state should never occur, find what produced it. | pstack `e5136d8` | Hypothesis, cheap |

Recommendations 4 and 5 pull in opposite directions. Item 5 covers mechanical consequences of an agreed change. Item 4 covers design choices.

Evaluation:

- 1: the next parallel `queue-work` run has few or no refusals.
- 2: the next `/warmup` in a resumed session summarizes that session.
- 3: no request for descriptions of relisted items.
- 5: keep if users stop sending "just fix" for leftovers. Revert if agents make unflagged non-mechanical changes in the name of consistency.
- 6: no regression in `fix-bug` routing. The outcome signal is rare.

## Declined

- Moving parallel guidance into a shared reference for `queue-work` and `deliver`, deferred. `deliver` has a single sentence on delegation and has never delegated, so little is duplicated yet.
- Retiring `create-verification`. It is five days old. The user doubted its benefit once, so ask before its next review.
- pstack's test-principle rewrite. `implement` already asks for tests through stable interfaces with expected results from requirements.
- ketchup screenshots and diagrams. These rely on rendering that terminal sessions lack.

## Next review

Start from Matt Pocock `49dd158`, pstack `101b274`, and transcripts after 2026-10-17. Check the evaluations above, the check-cost evaluation, and real use of `deliver`, `optimize`, and `create-verification`.
