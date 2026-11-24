# Text review of the skills and the global rules, 2026-11-24

This is an in-depth `maintain-skills` review. Four fresh reviewers read all of the skill text, the README, this repository's `AGENTS.md`, `LICENSES.md`, and `.codex/config.toml`, the scripts, the routing cases, and the user's global rules (archon `data/home/.codex/AGENTS.md` at `7e18c57`). They split the work by area:

- Cross-session skills: `collect`, `spawn`, `yield`, `handoff`, `warmup`, and the shared scripts.
- The other conversation skills, the docs skills, `teach`, and the global rules.
- Delivery, investigation, and planning.
- Workflow, the repository docs, and the routing cases.

Each reviewer had the 2026-11-09 text review, the declined list, the open trials, and the global-rule changes since archon `7865b69`. The main session checked the high-severity findings against the files. Line numbers are as of master `eec50c6`.

All areas were clean on the following: invocation settings agree across all 29 skills, links and symlinks resolve, no retired skill is referenced, the README catalog lists all 29 skills, and script usage in the text matches the scripts. The only items from the 2026-11-09 review to regress are the ones in item 1, which followed a rule that has changed since. Items marked [archon] change the global rules and go to archon as a handoff.

Each item gives the main session's recommendation.

## Decisions

Status: all items decided on 2026-11-24 and applied on branch `text-review-2026-11-24`, except item 6, which the user dropped because `tidy-docs` already preserves unresolved decisions. Items 39 to 43 went to archon as a handoff, and the user installed them. Changes to the proposals:

- Item 1: the user found the questions-first order confusing because a question came before the context it needed. The global Writing rule now says to put the most important parts first and to give each part enough context to be understood on first read (second archon handoff). `implement` and `queue-work` refer to it instead of copying the old order. `recap` keeps its own order.
- Item 14: after one restart on its tier, a stuck item is judged again and moved to a stronger tier, the most capable one when unsure.
- Items 17 and 18: the docs document everything `agent-joins.sh` relies on. `routing-test.sh` relies on undocumented output, which the user accepted. It names that output in a header note and has a test.
- Item 27: the user removed the read-only limit on `scripts/sync-skills.sh` for Codex.
- Item 12: `warmup` matches `handoff-<repository>-from-*` and confirms the target from the handoff's title line.

## Changes to behavior

1. **Report order under the revised Writing rule** (`implement:45`, `queue-work:82`, `recap:19-22`). The global rules now start with what the user asked for and put waiting questions next, or first only when one blocks the answer. The 11-09 item 4 put questions first under the old rule. Proposed: `implement` and the `queue-work` item report lead with the result, then the questions, as the user's rules for writing say, and put the questions first without such rules. `recap` keeps state first, then item status, then "Waiting on the user" with "Open questions" folded in (except questions not yet ready for the user), then rejected options. Recommend: yes.
2. **Lasting structure inside an approved item** (`implement:14-20`, `refactor:18-20`, `review-code:24`). The new Approval rule asks before a new package, service, or module even inside an approved item. `implement` never reaches that ask. Proposed: a bullet in `implement` that asks before such structure as the user's rules for approval say, and `review-code` checks for new structure the request did not approve. Recommend: yes.
3. **`optimize` approval and report** (`optimize:25`, `:33`, `:41`). It edits code directly, so `implement`'s approval text does not apply. An attempt such as a cache can add structure or change visible behavior. Its commit rule has no fallback, unlike `implement`. Proposed: ask before an attempt that adds lasting structure or changes user-visible behavior, report choices and questions as `implement` does, and commit only when asked without rules. Recommend: yes.
4. **`fix-bug` and `refactor` reports** (`fix-bug:30`, `refactor:28`). They replace `implement`'s report and drop its open questions, choices, and kind of review. Proposed: report as `implement` does, plus the cause and evidence for `fix-bug`, and what became simpler and the evidence that behavior is preserved for `refactor`. Recommend: yes.
5. **`glossary` edits on a question** (`glossary:45`, `:49`). The skill edits entries when the user asks what a term means, against "a question is not a request to act". `clarify` only offers. Proposed: propose a sharper definition or a clearer name, and change the entry once the user agrees. Recommend: yes.
6. **`tidy-docs` and choice levels** (`tidy-docs:21`, `:25`). The repository runs it over everything, `.scratch/` included, after each skill change. It reports edits but ignores the ask levels for docs aligned with code that may be wrong, and for records that would present undecided items as decided. Proposed: report edits as the user's rules for approval say, and without them list every edit and ask before those two kinds. Recommend: yes.
7. **`collect` can re-queue integrated items** (`collect:25-31`). `finish-queue.sh` deletes the finished queue file, so a later yield's `now` item is "in neither" and runs again. Proposed: also search finished queues in Git history, such as `git log -S '<source ID>' -- <queue location>`, and treat a match as integrated. Recommend: yes.
8. **A focused yield drops items** (`yield:22` against `:8`). The note replaces the previous one, so narrowing it loses agreed items. Proposed: the argument focuses the decisions and open points, and every agreed item and needed handoff stays. Recommend: yes.
9. **`collect` reply puts IDs inside sentences** (`collect:15`). This goes against the ID rule. Proposed: one line per note, then one sub-bullet per new ID that starts with the ID. Recommend: yes.
10. **`collect` in a fork records decisions in the checkout** (`collect:17`, `:45-47`). Proposed: in a fork, record nothing in the checkout and carry durable decisions into the next note. Recommend: yes.
11. **Withdrawn items** (`collect:25-31`). An item missing from the fork's latest note stays queued or backlogged. Proposed: when an item is not yet started or is in the backlog, its source ID is from this note's fork, and the note lacks it, ask in one line. Judge only by the note of the fork named in the source ID. Recommend: yes.
12. **Handoff file names** (`handoff:14`, `collect:37-43`, `warmup:13`). No skill sets a name that the target repository can find. Proposed: `handoff` owns `handoff-<target>-from-<source>-<slug>.md`, `collect` extends it with the tree ID and source ID, and `warmup` looks for `handoff-<this repo>-*`. Recommend: yes. This does not touch the open `handoff` trial.
13. **`warmup` retrospective trigger** (`warmup:27`). Retrospective records are removed once closed, so `warmup` finds none and suggests one each time. Proposed: also use the date of the latest commit that touched `.scratch/workflow`. Recommend: yes.
14. **`queue-work` takeovers** (`queue-work:22`, `:60`). The measurements record restarts and takeovers, but no step says when they happen. Proposed: when an implementer stalls or fails the same way twice, restart it once on its tier, then give the item to the next tier from its base commit and record it. Recommend: yes.
15. **Queued investigations have no route** (`queue-work:41`, `worktree-agent.md:6-10`). The top tier names investigations, but implementers choose only among `fix-bug`, `refactor`, `optimize`, and `implement`. Proposed: add `investigate` to that list. Recommend: yes.
16. **Pacing an in-depth review's decisions** (`maintain-skills:40`). The 11-09 review put 61 items to the user at once. Proposed: put the decisions to the user as the user's rules for writing and approval say, starting with the one that blocks the most. Recommend: yes.

## Undocumented behavior (ask)

17. **`routing-test.sh`** (`:77-94`). It parses Claude's stream-json `init` skills field, injected `<skill>` blocks, and Codex `--json` items. It has no header note and no test, unlike the scripts from 11-09 item 10. Recommend: check the docs, and if these are undocumented, accept them with a header note and a fixture test.
18. **`agent-joins.sh`** (`:69`, `:180-190`). It relies on `CLAUDE_CODE_SESSION_ID` and on `--disallowedTools 'Edit(//path/**)'` covering every editing tool. Recommend: the same as item 17.

## Gaps and stale text

19. `design:28`: the fallback names only a backlog. Add "or a `.scratch/` record when the project has none". Recommend: yes.
20. `investigate:30`, `review-architecture:42`: give the saved record's path in the report, and label `review-architecture`'s recommendations in the record as proposals until accepted. Recommend: yes.
21. `review-architecture:38`: a rule defined in another repository changes there through a handoff, as the user's rules for other repositories say. Recommend: yes.
22. `guide:18-45`: route `writing-text`, `writing-agents`, and `writing-skills`. Recommend: yes.
23. `routing-cases.tsv:44` expects `handoff` for discussing a topic separately, while `guide:44` says that belongs to `spawn`. Proposed: `guide` says `spawn` is the user's to start, and `handoff` covers it otherwise. Recommend: yes.
24. `worktree-agent.md:3`: the list of brief contents leaves out the review model. Recommend: add it.
25. `queue-work:88`: unclear whether `finish-queue.sh` runs when the project has its own conventions. Split into the two cases. Recommend: yes.
26. `skill-usage.sh:95`, `:37`: `--exclude-cwd` matches a string prefix, so it also drops sibling folders, and `-h` exits 2. Match the folder exactly or as a parent, and exit 0. Recommend: yes, then run `scripts/tests`.
27. `.codex/config.toml:11` makes `scripts/sync-skills.sh` read-only for Codex with no reason given, while "Script changes" expects agents to edit it. It was added deliberately in `b0e6cf7`. Recommend: add a comment with the reason, which only the user knows.
28. `.scratch/workflow/2026-10-16-check-costs.md` has been open since 10-16, and nothing points to it. Recommend: judge it from trading-app's queue measurements and remove it.
29. `collection-state.md` has no open trial for the three implementer tiers (`bde9410`). Recommend: add one. Keep it if cheaper-tier items rarely need takeovers or redos and costs drop. Revise it if takeovers or redos are frequent on a tier, or if the kind of work is hard to judge before queuing.
30. `scripts/tests/test_agent_joins.py` does not cover `collect`'s new or changed detection, the "via" order, note deletion, or `prune`. Recommend: add fixture tests.
31. `writing-agents`: it has no finish check, and `:10` says "before a merge". Recommend: add "Finish when every instruction lives in one place and each one changes how the agent works", and say "before commits go into the main branch".

## Wording

32. `optimize:3`: "rather than restoring a regression" attaches to "attempts". `:22`: "cheapest first" reads as effort. Proposed: "Not for restoring a regression, which belongs to `fix-bug`", and "starting with those that remove the most work". Check routing after the description change. Recommend: yes.
33. `refactor:18`: "minimal unnecessary abstraction" becomes "without unnecessary abstraction". Recommend: yes.
34. Cross-session nits: move `spawn:21` next to `:17`, give the `spawn:29` fallback for parts too, add "describe any other item in words" to the `handoff:22` fallback, drop the repeat in `handoff:12` and `:30`, give decision steps IDs in `warmup:25`, and fix two phrasings in the `agent-joins.sh` usage (`:13-14`, `:24`). Recommend: yes.
35. `queue-work:68` and `worktree-agent.md:16`: "the more capable model" and "a more capable model" become "the most capable model". `queue-work:43`: "An item may name another model the same way" becomes "The user may name a different model for an item. Note it in the decision too." Recommend: yes.
36. Routing cases: add a `writing-text` case. Keep the `!`-only cases for user-invoked skills (`:22`, `:26`, `:43`, `:45`), knowing that they fail only if the agent reads that skill. Recommend: yes.
37. `glossary:31` holds five rules in one bullet, and its fallback repeats the rule, as does `refactor:20`. Split it, and write "Rename an existing term as the user's rules for approval say. Without such rules, only once the user agrees." Recommend: yes.
38. `clarify:24`: write "name the part of their model it corrects". `writing-skills:25`: make the paragraph's five rules a list. Recommend: yes.

## Global rules [archon]

39. `G:39` has "ask the one that blocks the most and list the rest as questions still to come", which `interrogate:8` cites as a Writing rule. Proposed: move it into Writing (`G:13`) for all questions, and have `G:39` refer to Writing. Recommend: yes.
40. "Unit" is undefined, and `G:33`, `G:59`, and `G:73` disagree on its size. Under `G:73`, a shared helper inside an existing module needs an ask, while `G:33` says it is not structure. Proposed: define a unit once at the start of Code design, write `G:33` as "a new package, service, or module", and write `G:73` as "when no shared module fits". Recommend: yes.
41. "A few words beside each ID" appears in `recap`, `collect`, and `spawn`, while `G:19` and `G:21` give it only at an item's introduction and a topic's first mention. Proposed: give every ID a few words at its first mention in each message, and have the skills refer to that rule. Recommend: yes.
42. `G:97`: drop "because nobody reads it as current truth", since `G:43` treats `.scratch/` records as able to present decisions. Recommend: yes.
43. `G:75`: split the looks sentence, which holds three rules and a connector colon. Recommend: yes.
