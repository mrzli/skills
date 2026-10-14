# Skill collection review, 2026-10-14

Follows the [2026-10-12 review](2026-10-12-collection-review.md). This review produced recommendations only.

## Scope and sources

- The resolved skill was `skills/engineering/workflow/maintain-skills/SKILL.md`. The installed copy is identical, at `ce45880`.
- Matt Pocock's skills: no changes since `49dd158`.
- pstack: `1b6d44f` to `1e5c90a`. Read the new `sharpen` and `in-your-own-words` skills and the `principle-fix-root-causes` change. `ketchup` was shortened, and the other changes are Cursor orchestration, screened by commit title.
- Transcripts since 2026-10-12 14:00: five Claude sessions in qt-market-chart, archon, and learning, plus qt-market-chart subagents. There were no Codex sessions. A subagent audited them. Quotes and the count of memory writes were spot-checked.
- Routing: 28 cases for skills changed since the last run, using Claude Code with the installed skills. Five cases for unchanged skills were skipped.

## Usage since 2026-10-12

Sessions with any use, from `skill-usage.sh --since 2026-10-12 --exclude-cwd <this repo> skills`:

```txt
skill                invoked  read  last
writing-text         0        1     2026-10-12
design               1        0     2026-10-13
refactor             1        0     2026-10-13
teach                1        0     2026-10-12
writing-agents       1        0     2026-10-12
implement            2        0     2026-10-14
review-code          2        0     2026-10-14
```

## Routing results

```txt
case  expected                    loaded            verdict  request
1     fix-bug                     fix-bug           pass     The chart stutters and jumps when I zoom past the last bar. 
2     fix-bug                     -                 missed   ./bin/check started failing after the last commit, sort it o
3     clarify                     investigate       missed   How does zooming work in the chart right now?
4     clarify                     clarify           pass     I don't get what the renderer's primitives are, explain it a
5     investigate                 -                 missed   Before we pick a line rendering approach, find out whether Q
6     optimize                    optimize          pass     Rendering feels slow with large datasets, I want frames well
7     fix-bug,!optimize           -                 missed   Panning got much slower since yesterday's renderer change, i
8     refactor                    -                 missed   ChartState.cpp has grown too big, split it up without changi
9     implement                   -                 missed   Add a keyboard shortcut that resets the zoom to show all bar
10    design                      design            pass     I need to decide what the API between the geometry builders 
11    shape-feature               shape-feature     pass     I want to add drawing tools to the chart, but I'm not sure w
12    interrogate,!shape-feature  interrogate       pass     Here's my plan: one shared renderer, primitives are rect, po
13    prototype                   -                 missed   Show me two or three ways the crosshair tooltip could look s
14    plan                        plan              pass     Break the renderer unification into tasks we can do one by o
15    review-code                 -                 missed   Review the changes on this branch before I merge.
16    deliver                     -                 missed   Go through the whole review backlog, implement each item, an
17    guide                       guide             pass     I have this chart app half built, what should I do next?
18    recap                       recap             pass     Relist what is left from the backlog.
19    !handoff                    recap             pass     Summarize what we did so far.
20    !restate                    -                 pass     so like the thing with the lines and the renderer and the um
21    tidy-docs                   tidy-docs         pass     The docs in this repo are a mess, tidy them up.
22    writing-agents              -                 missed   Update AGENTS.md so it says to run the tests before committi
23    improve-workflow            improve-workflow  pass     The agent keeps forgetting to run the formatter before commi
24    !teach                      -                 pass     What is the capital of Australia?
25    !explore                    -                 pass     I'm kind of interested in something around music, not sure w
26    recap                       recap             pass     Reiterate what we discussed about the renderer architecture 
27    clarify                     -                 missed   Am I right that the builders run before the renderer, or not
28    !create-verification        -                 pass     I keep having to check the chart by hand after every change,
```

There were 19 passes and 9 misses. Every missed run completed normally, within budget. The script runs cases in plan mode, where the agent writes a plan instead of acting. Seven misses are skills used while doing work: `fix-bug` twice, `refactor`, `implement`, `review-code`, `deliver`, and `writing-agents`. Plan mode probably suppresses them, so these misses do not show that the skills are skipped in normal use. The test runs wrote ten plan files to `~/.claude/plans`, which were removed.

## Observed friction

1. **Project knowledge went to private memory.** After the global rule "Put rules that apply to a project in that project's AGENTS.md" was loaded on 10-12, the qt-market-chart session made 30 memory tool calls. Its memory now holds design notes and answers, including a 26 KB `engine-design-user-notes`, that belong in project documents. The rule names only rules, not decisions or notes.
2. **A question was treated as permission.** At qt-market-chart 10-12 15:27, the user said: "Why are you doing anything? I didn't tell you to do anything." The agent had answered a question and then acted on its own "I'll go ahead". This session still had the old `implement` loaded, so it does not test the new skill rule. The failure happened in conversation, outside any skill.
3. **Skills went unused in a long conversational session.** Requests suited to `recap`, `clarify`, and `tidy-docs` were answered inline. The answers had the right structure and drew no complaints, so the cost was low. Fresh-session routing loads `recap` and `clarify` for similar requests.

Positives:

- `design` recorded configuration decisions as they were agreed.
- Agents stated their reading of possibly misheard words.
- All merges and branch deletions were requested explicitly.
- The archon AGENTS.md change followed the branch and commit rules.

These were not exercised: `optimize`, `create-verification`, `deliver`, the new `recap` and `clarify` behavior in real use, and the no-legacy default.

## Recommendations

| # | Change | Evidence | Kind |
| --- | --- | --- | --- |
| 1 | **Fix the routing test method.** Run cases in the default permission mode with edit tools disallowed, so the agent starts the work and loads action skills, but cannot change files. Headless runs deny other unapproved tools. Run in a temporary git worktree as a second safeguard. Rerun the nine missed cases to compare. | Seven of nine misses are action skills under plan mode | Test defect, likely |
| 2 | **Broaden the global memory rule,** through archon. Project knowledge, such as rules, decisions, design notes, and conventions, belongs in the project's documents. Private memory holds only the user's personal preferences. | Friction 1 | Observed |
| 3 | **Add a global rule that a question is not a request to act,** through archon. Answer and wait, and do not treat your own "I'll go ahead" as permission. | Friction 2, and 10-11 in the previous review | Observed twice |
| 4 | **Route correctness checks to `clarify`.** Add "or asks whether their understanding is right" to its description. Accept `investigate` as well as `clarify` for the "how does zooming work" case, since both fit. | Routing cases 3 and 27 | Hypothesis, cheap |
| 5 | **`fix-bug`: propose a cheap check that shows the cause early.** When the deciding fact took a deep investigation, propose a cheap, always-present signal that would have shown it at first look, such as a log line, assertion, or diagnostic. | Upstream `36cecbf` | Hypothesis, cheap |

Outside this repository: move the qt-market-chart memory notes into that project's design documents. This is a qt-market-chart task.

## Declined

- `in-your-own-words` matches local `restate`, which confirms the existing design.
- `sharpen` reframes a task before starting. There is no evidence of need, and `restate`, `guide`, and `design` cover parts of it.
- The shortened `ketchup`. There is no complaint about `recap` length yet.

## Next review

Start from Matt Pocock `49dd158`, pstack `1e5c90a`, and transcripts after 2026-10-14. Check real use of `optimize`, `create-verification`, `deliver`, and the new `recap` and `clarify` behavior.
