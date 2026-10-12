# Skill collection review, 2026-10-12

Follows the [2026-10-08 collection review](2026-10-08-collection-review.md) and the [pstack review](2026-10-08-pstack-review.md). This review produced recommendations only.

## Scope and sources

- The resolved skill was the repository copy `skills/engineering/workflow/maintain-skills/SKILL.md` on the unmerged `pstack-source-review` branch. The installed copy is the older master version.
- Local baseline was `pstack-source-review` at `3ea4cc1`. That branch is not merged or installed, so sessions since 2026-10-08 used the master versions. `optimize`, `deliver`, and the new descriptions had no opportunity to be used.
- Matt Pocock's skills: `f3fc563` to `49dd158`. Only `wizard/template.sh` changed, and `wizard` is declined.
- pstack: `ccb5507` to `1b6d44f`. Inspected the `create-verification-skill` and `unslop` diffs and the new `ketchup` skill. The other changes are Cursor plumbing, token distillation, and `why` and `reflect` edits. They were screened by commit title only.
- Transcripts: 11 Claude sessions and 3 subagent files modified since 2026-10-08 12:00, covering qt-market-chart, archon, learning, and repos. There were no Codex sessions. A subagent audited them. Six key quotes were spot-checked against `d2621042`. Routing tests were not run, because the changed skills are not installed.

## Usage since 2026-10-08

Output of `skill-usage.sh --since 2026-10-08 --exclude-cwd <this repo> skills`, counting sessions:

```txt
skill                invoked  read  last
deliver              0        0     never
design               0        0     never
explore              0        0     never
guide                0        0     never
improve-workflow     0        0     never
interrogate          0        0     never
investigate          0        0     never
maintain-skills      0        0     never
optimize             0        0     never
plan                 0        0     never
prototype            0        0     never
release              0        0     never
restate              0        0     never
review-architecture  0        0     never
review-product       0        0     never
shape-feature        0        0     never
start-project        0        0     never
writing-agents       0        0     never
writing-skills       0        0     never
writing-text         0        1     2026-10-10
clarify              1        0     2026-10-11
fix-bug              1        0     2026-10-08
handoff              1        0     2026-10-08
recap                1        0     2026-10-11
refactor             1        0     2026-10-09
teach                1        0     2026-10-12
tidy-docs            1        0     2026-10-10
write-spec           1        0     2026-10-10
implement            3        0     2026-10-12
review-code          4        0     2026-10-10
```

This is too short a window for retirement decisions.

## Observed friction

1. **"Recap" usually meant the discussion, not the status.** In qt C `d2621042`, `/recap` returned item status twice. The user then asked to "reiterate what we discussed… where did we left off with the render itself?" (10-09 07:14) and "describe the architecture of the renderer, desired one". On 10-10 09:51 they said: "I'm not reading everything that you say so I'll ask you to recap and even repeat some of the things that you said before". Many plain "relist" requests were answered without any skill.
2. **Decisions were scattered.** A multi-day architecture effort had no written plan or decision record. Recaps said items came "from our conversation rather than a written plan". On 10-11 17:47 the user said it was "wildly out of sync with the spec… spread this out all over the place".
3. **Questions were treated as approval, and changes were made that nobody asked for.** On 10-11 17:51 the user said: "I didn't ask you to do that. I asked you whether this is something…". At 15:57 they asked: "Why the fuck did you change it?" The agent admitted the change was for "convenience". At 17:40 the agent had treated approval of one item as approval of a whole spec.
4. **`clarify` skipped the direct answer.** On 10-08 20:56 the user said: "Am I or am I not correct on this? Finally."
5. **Visual results were checked by hand.** An HTML artifact failed in dark theme twice before the user caught it. Pan speed was tuned by feel.
6. **Misheard dictation led to a destructive action.** The agent read "search" as "merge", then merged and deleted branches (10-10 05:26).
7. **A project rule was saved to private memory instead of the project** (10-08 15:15).
8. **Branch and commit rules were followed unevenly.** One session left edits uncommitted on master, and in another the user had to suggest a new branch.

Positives: performance work was measured properly, with profiles, a baseline, and before-and-after runs, even without `optimize`. Teach, handoff, and the archon chain of write-spec, implement, and review-code all worked without friction.

## Recommendations

| # | Change | Evidence | Kind |
| --- | --- | --- | --- |
| 1 | **Widen `recap` to discussions.** Cover the decisions made, the current state of the topic, rejected options, open questions, and anything waiting on the user, plus item status when the work has items. The argument picks the focus. Take `ketchup`'s rule to assume the user read nothing since their last message, and its action-item summaries. | Friction 1, four instances in one session | Observed |
| 2 | **Keep a decision record during long design discussions.** In `design`, and in `deliver` for backlogs, write each agreed decision to the spec or design record when it is made. `recap` reads it. | Friction 2 | Observed once, with high cost |
| 3 | **A question is not approval.** In `implement` and `deliver`, answer a question and wait. Approval of one item covers only that item. Propose changes outside the request instead of making them. | Friction 3, three instances | Observed |
| 4 | **`clarify` answers a direct question first,** such as yes, no, or partly, then explains. | Friction 4 | Observed once |
| 5 | **Add the `create-verification` skill** from the earlier proposal. Add upstream's new readiness rule: launch must reach a usable state from empty data, not just a running process. Also add its stand-in caveat. Include visual checks such as light and dark themes. | Friction 5, the Xvfb history, and pstack's verification emphasis | Observed need. Trial on qt-market-chart. |

Outside this repository, for the global `AGENTS.md` through archon:

- Confirm destructive or hard-to-reverse actions, such as merging or deleting branches, when the request may have been misheard in dictation. Friction 6.
- Put project rules in the project's `AGENTS.md`, not in private memory. Friction 7.

## Declined or deferred

- `ketchup` as a separate skill. Recommendation 1 folds its useful parts into `recap`.
- Upstream `unslop` wording changes. Our `tells.md` is already rewritten in local style.
- Retirement. The usage window is four days, and the newest skills are not installed.

## Next steps

After the user installs `pstack-source-review`, run the routing cases for the changed skills. On the next review, start from Matt Pocock `49dd158`, pstack `1b6d44f`, and transcripts after 2026-10-12.
