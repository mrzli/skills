# Skill collection review, 2026-10-08

Follows the [2026-10-05 review](2026-10-05-collection-review.md). The user approved all recommendations. They were applied on branch `skills-review-2026-10-08`, one commit per change, as listed in [Applied changes](#applied-changes). Installed copies were not changed.

## Scope and sources

- Local baseline was `98585d3`, with a clean tree and 28 skills. The resolved skill was `skills/engineering/workflow/maintain-skills/SKILL.md`. The user-installed copy is identical.
- Upstream: [Matt Pocock's skills](https://github.com/mattpocock/skills), diffed from `24fe0ef7737efae15c87225755e9f6f5965e4888` to `f3fc5632f401156837ee3872f14fe33ccf1024ea` within `skills/engineering` and `skills/productivity`. A new `skills/in-progress/chief-of-staff` skill falls outside the source scope and was not read.
- Use evidence: Claude and Codex transcripts modified since 2026-10-05, covering archon, qt-market-chart, learning, omarchy-lab, and this repository. A subagent audited them. Key quotes were spot-checked against the transcripts. Codex skill use was inferred from SKILL.md reads, so it is noisy.

## Observed use

Skill use rose after the global "check available skills first" instruction was added on 2026-10-07. The qt-market-chart backlog session then used guide, plan, fix-bug, implement, design, investigate, refactor, tidy-docs, and review-code consistently. Earlier sessions show default behavior instead:

- A broad review ran without review-architecture. The agent later said it "fell back on my default approach".
- Fixes ran without fix-bug or implement.
- One session said it would use fix-bug but never read the skill.

Handoff and teach each ran once without friction. Prototype has not been used since it was added, so its trial is still open.

## Recommendations

| # | Change | Evidence | Kind |
| --- | --- | --- | --- |
| 1 | **Improve `plan` reporting.** Lead with the plan's level structure, meaning workstreams or milestones and then tasks. Report a short top-level summary and the blocking questions in chat, not the whole plan. | qt C `d2621042`, 10-07: "I don't want to read through all of it. Give me … 10,000 feet". The user also asked "were there not wider things to do, and these steps 1 through 5 are just one of the wider steps." | Observed, twice in one session |
| 2 | **Trial a `recap` skill** for backlog status. It should list what is done, in progress, and remaining from the plan file or conversation, concisely, without restating goals. `restate` covers goals, not progress. | "relist" or a similar request came about 8 times in archon C `8aa0fbb4` and about 6 times in qt C `d2621042`. The user typed `/recap`, which does not exist, and `/restate` was followed by "relist". | Observed, recurring across two projects |
| 3 | **Record cross-project preferences in global instructions, not skills.** These are US English spelling and the per-item delivery pattern: a separate branch per group, one commit per item, and a merge only when the user asks. | The user asked for US English in qt C, 10-07 16:04. The delivery pattern was repeated across archon and qt. | Observed preferences. They are not skill responsibilities. |
| 4 | **Optional upstream micro-edits.** In `teach`, vary which position holds the correct quiz answer. In `interrogate`, word each question so that "yes" accepts the recommendation. In `handoff`, report the saved file path. | Upstream commits `ad5400b`, `95249b0`, and `4f4e943`. No local failure was observed. | Hypothesis. Low cost. Applied on approval. |

Evaluation:

1. On the next large plan, the user should be able to approve or redirect from the summary alone without asking for altitude.
2. In the next multi-item session, the user should use `recap` instead of repeated "relist" prompts, with no "wasn't there more" corrections. Retire `recap` if it is not used across two such sessions.
3. Later replies should use US spelling, and delivery should follow the pattern without reminders.
4. Revert an edit if it causes awkward output, such as forced yes/no wording in `interrogate`.

### Skills above `plan`

The user asked whether a skill above `plan` should own the higher-level view.

- `start-project`, `shape-feature`, and `write-spec` define scope and requirements. They do not list work.
- `deliver-feature` coordinates execution. It already keeps a progress record with task status and the next action.

No skill produces a higher-level breakdown above `plan`, so plan grouping belongs in `plan` itself. In qt C `d2621042`, 10-07 14:36–14:38, the plan was in fact the whole plan. The user's confusion came from its levels: a batch, then step 3, then the renderer and builders inside step 3.

The recap need overlaps with the `deliver-feature` progress record. That session did not use `deliver-feature`, because the work was a backlog of mixed review findings rather than one feature. The user approved both: `deliver-feature` now covers a backlog of related items, and `recap` reads its record or plan when one exists.

## Keep, no change

- **Design-stage skills** are interrogate, shape-feature, design, and prototype. One session went through four of them in five minutes, then asked for guide, which routed correctly to design (Codex `10-05T07-28`). The confusion happened once, and guide resolved it. Watch whether it recurs before changing descriptions.
- **Clarify.** Frustration in the same session came from misread questions about the renderer, and the user typed "clarify" in plain words. The skill already requires finding the missing distinction and checking code, but it was not loaded. Inline slash commands also misfired once ("/clarify" without its argument). These are invocation problems, not content problems.
- **Tidy-docs.** The failure to apply writing-text predates `fe9f7fe`. No failure has been observed since.
- **Fix-bug, review-code, and the rest of the upstream diff.** These were declined. Local fix-bug already requires that "the check detects the original failure". Local review-code already reads all applicable conventions. Upstream wayfinder, to-tickets, and setup changes are specific to trackers.

## Applied changes

On branch `skills-review-2026-10-08`:

- `maintain-skills` gained [skill-usage.sh](../../skills/engineering/workflow/maintain-skills/scripts/skill-usage.sh). Reviews save its output and propose retiring skills unused for several months. The user decides each retirement. This responds to the user's wish to eventually delete skills they will not use.
- `plan` groups tasks into phases or workstreams and reports a top-level summary.
- New [recap](../../skills/conversation/recap/SKILL.md) skill. Implicit invocation is allowed so that plain "relist" requests can route to it.
- `deliver-feature` covers backlogs, routes bug and refactor items to `fix-bug` and `refactor`, and follows branch and commit conventions. `guide` and the README were updated to match.
- `teach`, `interrogate`, and `handoff` received the upstream micro-edits, with upstream commits cited in the commit messages.

Changes left to the user outside this repository:

- Add US English and the branch-per-group workflow to the global `~/.codex/AGENTS.md`.
- Raise Claude Code transcript retention with `cleanupPeriodDays` in `~/.claude/settings.json`. The default deletes transcripts after 30 days, and the earliest Claude transcript is from 2026-10-06.
- Sync the installed copies under `~/.local/share/archon-skills`.

## Usage baseline

Output of `skill-usage.sh --exclude-cwd <this repo> skills` on 2026-10-08, before `recap` existed. "Invoked" and "read" count sessions. Claude transcripts begin on 2026-10-06 and Codex transcripts in July 2026. Reads include agents loading a skill as guidance from another skill. For example, `writing-text` is read by the writing skills and is rarely invoked directly.

```txt
skill                invoked  read  last
improve-workflow     0        0     never
maintain-skills      0        0     never
prototype            0        0     never
recap                0        0     never
release              0        0     never
review-product       0        0     never
start-project        0        0     never
writing-skills       0        0     never
explore              0        1     2026-10-04
write-spec           0        2     2026-10-04
deliver-feature      0        3     2026-10-05
writing-agents       0        9     2026-10-07
writing-text         0        42    2026-10-07
tidy-docs            1        0     2026-10-07
shape-feature        1        1     2026-10-05
fix-bug              1        3     2026-10-07
refactor             1        3     2026-10-07
plan                 1        4     2026-10-07
review-architecture  2        3     2026-10-06
design               2        5     2026-10-07
investigate          2        10    2026-10-07
implement            2        12    2026-10-07
guide                3        5     2026-10-07
teach                4        3     2026-10-07
handoff              4        5     2026-10-04
interrogate          5        3     2026-10-05
restate              7        3     2026-10-06
clarify              10       6     2026-10-08
review-code          12       10    2026-10-07
```

Never used so far: improve-workflow, maintain-skills (outside this repo), prototype, release, review-product, start-project, and writing-skills (outside this repo). Most are tied to rare activities or are only weeks old. They are not retirement candidates yet.

## Evidence gaps and next review

There are no per-skill opportunity counts. Prototype, recap, and the design-stage routing still lack real-task evidence. On the next review, start from upstream `f3fc563` and local transcripts after 2026-10-08. Rerun the usage script and compare it with the baseline above. Revisit the 2026-10-05 trial criteria as work supplies evidence. No recurring review was scheduled.
