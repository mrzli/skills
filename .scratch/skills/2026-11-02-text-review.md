# Text review of the skills and the global rules, 2026-11-02

Backlog 1. Three fresh reviewers read all skill text, the README, this repository's `AGENTS.md`, and the user's global rules (archon `data/home/.codex/AGENTS.md` at `965ca62`), split by area: conversation and learning, engineering, and docs with `maintain-skills` and the global rules. The main session verified the high-severity findings against the files. Line numbers are as of master `446260d`.

No retired skill is referenced anywhere, and all links resolve. Items marked [archon] change the global rules and go to archon as a handoff.

## Decisions

The user approved everything below on 2026-11-02, with these refinements from the discussion:

- 1: approved as proposed.
- 2: approved. Design findings do not block. They go to the user as recommended changes, and an accepted one becomes a new item.
- 3: approved as proposed, with the [archon] part.
- 4: approved. The README follows the skill.
- 5: approved, reworded so the global rules name no skill: "When a skill for writing text is available, apply it to responses as well as documents."
- 6: approved. The general rule goes to the global Code design section, after the paragraph on giving data with a different role its own type: "When you rename or change something that code inside the repository uses, update every caller. Do not leave aliases, fallbacks, or deprecated paths behind for them. Keep a compatible form only for consumers outside the repository, for persisted data, or when the user asks." Its fallback lives only in `implement` ("Keep compatibility as the user's rules for code design say. Without such rules, update callers inside the repository instead of adding aliases, fallbacks, or deprecated paths."). `refactor` keeps only its migration-across-commits part, and `design` keeps only its "no transitional layers" sentence, pointing to the rule.
- 47, added: [archon] the global rules name no specific skill or script. They describe the kind of skill to use.
- 48, added: when a skill runs another skill for part of its work, it does not repeat the other skill's fallbacks. Remove such redundant copies, such as `refactor`'s "build the better one" and the stop-and-ask fallback in `worktree-agent.md`, and add the rule to `writing-skills`.
- 49, added: `spawn` owns the fork rules (forks only discuss and do not change the checkout, and handoffs to other repositories pass up to the main session, which writes them). The fork script's prompt stays as the enforced copy. `handoff`, `yield`, and `collect` keep one-line pointers, and the README describes the behavior without restating the rule. `handoff` is a general skill, not a companion of `spawn`. Its pointer covers only its use inside a fork.
- 50, added: `writing-skills` describes shared references in `skills/shared/references/`, linked from each skill's own `references/` folder, analogous to shared scripts. A file moves there only once a second skill needs it.
- 7 to 46: approved.

### Proposed decisions

1. **Commits in `implement`.** `implement:36` says invoking the skill "does not request a commit", while the global rules say to give each self-contained change its own commit, and `optimize` and `worktree-agent.md` always commit. Proposed: "Commit as the user's and project's rules for commits say. Without such rules, do not commit unless asked. Push, open a pull request, or release only when asked."
2. **Are design findings in `review-code` blocking?** `review-code:37` calls them "a recommended change, not an optional improvement" without saying whether they block integration, and the global rules integrate only when no blocking findings remain. Proposed: not blocking. They go to the user as recommended changes, and an accepted one becomes a new item.
3. **Fork item IDs in `collect`.** `collect:11` shows fork IDs such as `Claude-2/FF1a`, while the global rules say to give reported items IDs in the session's scheme and not pass on the report's numbering. Proposed: `collect` gives each collected item a session ID and keeps the source ID beside it as a tracking key, such as `queued G3 (Claude-2/FF1a)`, and [archon] the global rule allows the original numbering beside the new ID as a reference.
4. **When `queue-work` starts.** The README says "Once I agree to an item, queue-work hands it to a background agent", while the skill starts a batch only on an explicit request or `collect`'s `now` items. Proposed: the README follows the skill.
5. **[archon] Response-writing rules.** `writing-text` applies to responses but loads only when it triggers. Proposed: one global line, "Write responses as the writing-text guidance describes: concise, plain words, and no em dashes or semicolons where a period or comma works."
6. **[archon] In-repository compatibility.** `implement:12`, `design:10`, and `refactor:20` each state "no aliases or deprecated paths for callers inside the repository". Proposed: one global Code design rule, "Do not keep aliases, fallbacks, or deprecated paths for callers inside the repository. Update the callers. Keep a compatible form only for consumers outside it, persisted data, or when the user asks.", with the skills referring to it.

## Fixes that keep the approved meaning

### Contradictions with the global rules

7. `implement:12` and `:18`: "Propose changes outside the request instead of making them" and "Keep unrelated cleanup separate" conflict with the global rule to fix departures in each unit you change and to rename on your own judgment. Add "except the fixes the user's rules ask for in the code you change", and "Keep unrelated cleanup in its own commit."
8. `implement:12`: the fallback asks about choices that affect names, then lists names among mechanical consequences. Use "uses of a name the change renamed".
9. "the user's rules for choices" (`implement:12`, `recap:22`, `queue-work:44`) matches no global section. Use "the user's rules for approval". Also "the user's rules for response size" (`interrogate:8`): use "the user's rules for writing".
10. `queue-work:40`: an item implemented in the foreground is "not reviewed again", but that review may be a self-review, and the global rules require a non-author before the main branch. Add "unless that review was a self-review".
11. `optimize`: commits kept changes with no review step. Add a `review-code` step.
12. `queue-work:46`: "merge only when the user asks" is ambiguous next to the fast-forwards at `:40`, and nothing covers starting on the main branch. Replace with "start from a branch other than the main branch, and bring the user's branch into the main branch only when the user asks".
13. `review-architecture:12` and `:20`: collect the user's code design rules too, not only the project's.
14. `improve-workflow:26`: add the user's own instructions as a level for corrections, handed to the repository that manages them.
15. `handoff`: refer to items as the user's rules for IDs say for files that outlive the session.
16. `spawn:10` and `shared/scripts/agent-joins.sh:176`: forks may not write in the checkout, but the global rules send transient files to `.scratch/temp/` inside it. Say forks write temporary files outside the checkout.

### Inconsistencies and gaps between skills

17. `collect:19-24`: the duplicate check covers only the queue, so re-collecting a changed note adds `backlog` items again. Check source IDs against the backlog too.
18. `worktree-agent.md:6`: split the bullet so "Without such rules" clearly belongs to commits. `:7`: reword the rerun line without the colon and without restating the fallback.
19. `review-code:8`: "You make the corrections" conflicts with a report-only review. Use "You make any corrections that are authorized."
20. `fix-bug:6`: send diagnosis-only requests to `investigate`, as its description and `guide` do. `:30`: replace the circular review sentence with "Address the findings of `implement`'s review."
21. `recap:13` and `warmup:13`: `.scratch/plans/` is stale. Name `.scratch/delivery/` queue files and the project's backlog.
22. `writing-skills:12`: add the reverse placement rule, moving a global rule that matters only within one skill into it. `maintain-skills:26`: refer to `writing-skills` instead of copying its rule.
23. `maintain-skills:47`: say cases are added with the change and run after install, matching `AGENTS.md:9`, and explain the conversation-request exception.
24. `implement:24` and `fix-bug:26`: "the project's verification skill" is left from `create-verification`. Use "the project's verification skill or documented verification procedure".
25. `collect:42`: move the durable-decisions sentence out of "Inactive trees" and refer to the user's rules for project knowledge.
26. `restate`: stop and wait for confirmation before acting on the restatement.
27. `warmup:15`: say the session check applies to `--skip 0` and what to do when it fails.
28. `teach:12`: `<lesson-slug>` should be `<topic-slug>`. `:22` and `:104-106` describe two glossaries. The mission-change rule is stated three times, and the record numbering twice. `LEARNING-RECORD-FORMAT.md:21` and `:48` disagree on the status form.
29. `glossary:34`: the pending-rename sentence contradicts itself.
30. Invocation files: `recap`, `glossary`, `maintain-skills`, and most engineering skills lack `agents/openai.yaml`. Add `allow_implicit_invocation: true` for consistency.
31. `guide`: name `pending`, separate `clarify` from `investigate`, and show both invocation syntaxes in the example.
32. `refactor:18`: link `design`. `design:30`: separate the reference from its fallback.
33. `improve-workflow:18`: the fallback restates part of the global tooling rule.
34. Repository `AGENTS.md:3` names only `.agents/skills/`. `:7` repeats the tidy-docs default.
35. `tidy-docs:3` lacks a use-when clause, and it says "repo". `:17` and `:23` invoke `writing-text` twice.
36. `writing-text`: move the qualifiers sentence, order the simplify step before the final check, cover quotation marks, and move "forced contrasts" into `tells.md`.
37. `LICENSES.md:3`: name the skills based on Matt Pocock's.

### Wording

38. Colons joining clauses: `spawn:34`, `yield:24`, `LEARNING-RECORD-FORMAT.md:3`, `improve-workflow:26`. Long sentences: `collect:9`, `collect:28`, `review-code:29`, `queue-work:30`, `writing-skills:12`, `writing-skills:14`. The comma chain in `recap:23`.
39. "fork" for a context-copied subagent (`interrogate:28`, `queue-work:30`) collides with spawn's forks. Use "not one that copies this conversation".
40. `teach`: title-case headings, "Think Tufte.", "parametric knowledge", a question as its argument hint, and an unclear glossary line.
41. `interrogate:13,19`: the emoji before the ID, a " - " dash, and bold on ordinary terms.
42. `handoff:16` "print to the console" and "workspace", `handoff:24` "ADRs", `clarify:15` (say the shorter limit is deliberate), descriptions of `spawn` and `pending`, `worktree-agent.md:11` (whether routine choices are listed), the `repeated-steps.py` docstring, and the varying "the user's and project's" phrasing.

## [archon] Global-rule wording

43. `:89` vs `:91`: committing a generating script needs no approval, unlike tooling proposals. Say so.
44. `:45-55`: the Quality of choices paragraphs overlap. Fold `:53` into `:47`. Consider retitling the section "Quality of recommendations and designs".
45. `:83`: split the review paragraph at "Treat each fix for a finding".
46. `:9`, `:23`, `:31`, `:41`, `:63`, `:79`, `:99`: small wording fixes, such as an unclear "Then", "the recommendation" without an antecedent, and "the user's branch" undefined.

## Routing after install

With the fixes and the in-depth mode installed at `5e77bc9`, all nine cases for `fix-bug`, `investigate`, `tidy-docs`, and `maintain-skills` passed, including the new ones: diagnosis only loads `investigate` and not `fix-bug`, an in-depth review request loads `maintain-skills`, and tidying skill docs loads `tidy-docs` and not `maintain-skills`. `spawn` and `pending` are user-invoked, so no case can load them.
