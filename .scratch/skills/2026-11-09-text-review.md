# Text review of the skills and the global rules, 2026-11-09

In-depth `maintain-skills` review. Four fresh reviewers read all skill text, the README, this repository's `AGENTS.md` and `LICENSES.md`, the scripts, and the user's global rules (archon `data/home/.codex/AGENTS.md` at `7865b69`), split by area: conversation and learning; delivery, investigation, and planning; workflow; docs, shared files, scripts, and the global rules. Each had the 2026-11-02 text review, the declined list, and the open trials. The main session verified the high-severity findings against the files. Line numbers are as of master `288ee4a`.

All four areas: no retired skill is referenced, all links and symlinks resolve, and invocation settings agree across all 29 skills. No item from the 2026-11-02 review regressed. Items marked [archon] change the global rules and go to archon as a handoff.

Dropped: the docs reviewer reported the deployed `~/.codex/AGENTS.md` as behind archon. It is identical to archon's copy.

Each item gives the main session's recommendation.

## Decisions

The user approved every item as recommended on 2026-11-09, with item 4 narrowed: `review-code`, `review-architecture`, and the `queue-work` report lead with what the user needs, but `recap` keeps its state-first order, because a recap's answer is the current state and `pending` already gives the view of what waits on the user. Added to the [archon] items:

62. Global `:11` names both the answer and the waiting questions as what comes first. Proposed: "Start with what the user asked for, then the questions waiting on them, unless a question blocks the answer."

## Decisions that change approved behavior

1. **Review brief sized to the change** (`review-code:8`, `:31`, `:33`, `implement:35`). The 11-06 global rule matches the brief to the change's size and risk. Neither skill says so, and `review-code:33` invites reproducing any finding. Proposed: "Size the brief as the user's rules for reviews say. Without such rules, for a small, low-risk change, ask it to read the diff and the code it affects, without broad test reruns or experiments." Recommend: yes.
2. **Undocumented behavior** (`design:24`, `investigate:20`, `:28`, `review-code:25`). The 11-05 global rule needs the user's acceptance before relying on undocumented behavior, but `design` lets an experiment settle a choice. Proposed: `investigate` says whether documentation states a behavior or only an experiment or the source shows it; `design` relies on undocumented behavior only as the user's rules say, asking first without them; `review-code` checks for reliance on it. Recommend: yes.
3. **Design that grows** (`design:10`, `:32`). The 11-03 global rule asks for a first slice that later slices extend, with complicated neighboring changes as backlog items. Proposed: `design` refers to it, with that fallback. Recommend: yes.
4. **Lead with what the user needs** (`review-architecture:42`, `review-code:42`, `recap:17-22`, `queue-work:71`). The 11-09 global rule starts a response with the answer or the questions waiting on the user. These reports put them last. Proposed: `review-architecture` leads with the strongest recommendation, `review-code` with whether blocking findings exist, `recap` with what waits on the user (folding "Open questions" into it, except questions not yet ready for the user), and `queue-work` each item's report with its questions. Recommend: yes.
5. **`implement` report** (`implement:41`). It has no place for choices beyond the request or for open questions, so `fix-bug` and `refactor` lack them too. Proposed: "Put open questions first. Report what changed, your choices beyond the request as the user's rules for approval say, the checks performed and their results, and any remaining limitations. Without such rules, list every choice beyond the request." Recommend: yes.
6. **One severity scale** (`review-code:37-40`, `queue-work:60`, `worktree-agent.md:14`). `review-code` has only blocking and optional, and callers restate "blocking, major, minor, or nit". Proposed: `review-code` owns the four-level scale and callers refer to it. Recommend: yes.
7. **Design work in progress** (`design:32`). A design with open questions goes to `docs/design/`, while the global rules keep work in progress in `.scratch/`. Proposed: keep it in `.scratch/design/<slug>.md` or the project's convention, and move accepted decisions to the project's design records. Recommend: yes.
8. **`yield` and accepted choices** (`yield:14`). Only explicitly approved changes go in the note, so a listed choice the user did not object to is lost. Proposed: include choices accepted as the user's rules for approval say, with the explicit-only fallback. Recommend: yes.
9. **`teach` workspace** (`teach:3`, `:12`). `.scratch/learn/<topic-slug>` is work in progress under the global rules, so cleanup may remove a running course, and a course lands in whatever repository is open. Options: keep it and say it stays in use while the course continues, or move it outside project repositories. Recommend: keep it, with the note, since courses run in a chosen repository.
10. **Transcript layouts** (`warmup/scripts/last-session.sh`, and likely `maintain-skills/scripts/skill-usage.sh` and `improve-workflow`'s `repeated-steps.py`). They read Claude Code and Codex transcript files, whose layout is undocumented. The global rule needs the user's acceptance, a note naming the relied-on behavior, and a test. Recommend: accept, and add a header comment and a small fixture test to each script.
11. **Checks during integration** (`queue-work:46`, `:67`). The main agent runs checks during integration, but avoids them while any implementer runs, which is usually the case. Proposed: run them once no implementer runs, record which integrated items await them, and run them at the latest before the main branch. Recommend: yes.
12. **Second review of a cheaper implementer's open findings** (`queue-work:57`). Since the model trial, cheaper implementers leave blocking and major findings open by design, so each such item gets a full extra `review-code` run besides the fix review. Proposed: exclude findings left open as the brief says. Recommend: yes.
13. **Numbered queue items** (`queue-work:13-22`). The queue file is committed, and the global rules number a plan's items in the file. Proposed: each item has its number in the queue. Recommend: yes.
14. **Docs move in its own commit** (`queue-work:77`, `finish-queue.sh:13`). Moving lasting decisions into permanent docs lands in the commit that removes the queue, which hides a reviewable change in a `.scratch/` commit. Proposed: commit the docs move on its own first. Recommend: yes.
15. **In-depth review brief** (`maintain-skills:31-39`). The steps omit what this review's reviewers needed: the previous text review, declined items and open trials, changes to the user's instructions since then, and logic gaps such as steps that cannot be followed. Proposed: add them. Recommend: yes.
16. **Removing old reviews** (`maintain-skills:69`, `improve-workflow:42`, `collection-state.md` header). Dated reviews stay as history, while the global rules remove a `.scratch/` record once nothing in it is open or points to it. Proposed: both skills remove an earlier review once nothing in it is open and the maintenance record no longer points to it, and the header says so. Then remove the reviews from 10-05 to 10-27 that qualify. Recommend: yes.
17. **`guide` coverage** (`guide:3`, `:18-30`). It routes neither `glossary` nor `tidy-docs`, and its description says "the engineering skills". Proposed: add both rows and say "the skills". Recommend: yes.
18. **`improve-workflow` "smallest"** (`improve-workflow:6`, `README:53`). "Find the smallest useful correction" ranks by effort, against the global quality rule. Proposed: "Find the correction that best prevents the observed friction, without adding rules or tooling the evidence does not need", and the README names the user's own instructions as a target. Recommend: yes.
19. **`glossary` renames** (`glossary:31`). The agent renames whichever clashing term fits worse, including an existing one, while the global rules ask before renaming a glossary term. Proposed: propose the rename, and rename an existing term only once the user agrees. Recommend: yes.
20. **`tidy-docs` and dated records** (`tidy-docs:21`). It updates evolving documents to the current state, which could rewrite dated reviews and handoffs. Proposed: "Leave dated records, such as reviews and handoffs, as written, except their status." Recommend: yes.
21. **Invocation settings for new skills** (`writing-skills:10`). Only `maintain-skills` checks that `disable-model-invocation` and `allow_implicit_invocation` agree. Proposed: `writing-skills` sets both for every new skill. Recommend: yes.
22. **Sentence length** (`writing-text`). Reviews flag long sentences "as writing-text describes", but it has no such rule. Proposed: "Keep sentences short. Split a sentence that carries several separate points." Recommend: yes.
23. **Required checks for scripts** (`AGENTS.md`). `scripts/tests/test_sync_skills.py` exists, but no rule runs it. Proposed: after changing `scripts/sync-skills.sh`, run `python3 -m unittest discover scripts/tests`. Recommend: yes.
24. **`skills/experimental` exclusion** (`scripts/sync-skills.sh:38`). It skips a directory that does not exist and no doc mentions. Proposed: remove it. Recommend: yes.

## [archon] Global rules

25. `:39` against `:13`: ask-level questions all go first, but a response gives one heavy question. Proposed for `:39`: "When several are heavy, ask the one that blocks the most and list the rest as questions still to come." Recommend: yes.
26. `:38`: "at most a listed choice", followed by when to ask, contradicts itself, and the bullet holds five rules. Proposed: keep the bullet to listing and acceptance, and move the design-change and docs-gap rules to a paragraph after the list that says when each becomes ask-level. Recommend: yes.
27. `:87` "Merge only when the user asks" reads as covering the fast-forwards of `:89`. Proposed: "Bring commits into the main branch only when the user asks." Recommend: yes.
28. `:39` repeats `:11` on questions first. Proposed: "put these questions first, as 'Writing' describes". Recommend: yes, together with 25.
29. `:59` assumes a backlog, and "its design" is unclear. Proposed: "an item in the project's backlog, or a record in `.scratch/` when it has none", and "record the design it was meant to have". Recommend: yes.
30. `:55` overlaps `:51` and `:57`. Proposed: fold it into `:53`. Recommend: yes.
31. `:95`: unclear whether "report how long the review took" covers helper commits brought onto the working branch. Proposed: say "commits brought into the main branch". Recommend: yes.

## Fixes that keep the approved meaning

High:

32. `implement:16`, `:37`: the exception covers only "the user's rules for code design", so the agent proposes renames and docs, comments, or tests that lag behind the code, which the global rules have it make. Fix: "except the changes the user's rules say to make on your own judgment, such as fixes in the code you change, renames, and docs, comments, or tests brought in line with the code", and `:37` records only out-of-scope findings those rules do not cover.
33. `collect:15`: new IDs come with no words on what they are, against the global ID rule. Fix: `queued G3 (Claude-2/A1a), cap zoom at 400%`, plus "Give each new ID a few words on what it is, as the user's rules for IDs say."
34. `worktree-agent.md:38`: report part 4 assumes the implementer made an ask-level choice, against `:11` and the global "Do not make these choices yet". Fix: "Each other choice your brief did not settle, in one line. Do not make a choice that changes something agreed or that the user's rules for approval say to ask about first. Stop at that item as the rule on the chosen skill's questions says, and give it under 5."

Medium and low:

35. `implement:14`: reads as always asking. Fix: "take, list, or ask about it as the user's rules for approval say", and split the fallback into a list.
36. `refactor:20`: renames a concept without asking. Fix: rename a project-wide concept only once the user agrees, then update the glossary.
37. `fix-bug:24-30`: regression coverage and removing instrumentation run after `implement`'s review. Fix: pass both to `implement`, and drop the duplicate sentence at `:30`.
38. `optimize:3`, `:6`: a performance regression has two owners. Fix: a regression the user wants restored belongs to `fix-bug`, also in the description.
39. `review-code:25`: add the user's rules for code design to what it checks.
40. `fix-bug:26`: repeats `implement`'s verification text. Fix: "Rerun the original scenario and relevant neighboring behavior."
41. Rule names matching no global section: "design choices" and "recommendations" (`implement:23`, `refactor:18`, `design:16`, `review-code:29`, `review-architecture:32`) become "recommendations and designs". "Reviewing fixes" and "integrating commits" (`queue-work:65`, `:67`) become "Git and checks".
42. `review-code:29`: move the "better when" sentence after the fallback.
43. `review-architecture:3`, `README:117`: name the user's architecture rules too.
44. `review-architecture`: `:16` "the state it uses and which module owns it", `:40` name `investigate`, `design`, or `refactor`, `:38` change a rule "in the place that defines it".
45. `spawn:41`: the Codex sentence is left from `spawn full`. Fix: "Codex is not supported yet. The script finds a main session by its session ID and blocks file editing in forks with Claude Code's tool settings, and it is not known whether Codex offers either."
46. `collect:25-31`: check the latest item with a source ID, so a re-added item is not added again.
47. `warmup:17`: "a fork of it" collides with spawn's forks. Fix: "not a newer session, such as one opened by `spawn`".
48. `clarify:11`: order the one-line reading, then yes, no, or partly, then the explanation.
49. `agent-joins.sh` usage text: the brief is saved to a file the fork reads, session names include Claude2, and colons join clauses at `:16` and `:56`.
50. README: Forks step 4 also backlogs items; `:47` yield works only in a fork, collect in a fork and the main session above it; `:3` "The largest group covers software engineering"; `:77` collect also applies decisions.
51. `teach`: "explainers" becomes "lessons" in `GLOSSARY-FORMAT.md` and `RESOURCES-FORMAT.md`, the bold lead-ins in `LEARNING-RECORD-FORMAT.md:35-38` end with a period, and `SKILL.md:84` says all answer options of a question get the same number of words.
52. `queue-work:60`: "as the report below says" does not land. Fix: "Design findings go to the user as recommended changes, as `review-code` says."
53. `queue-work:34`: clarify which model applies to what, and when the review model is this session's.
54. `queue-work:67`: delete the implementer's branch with `git branch -d`.
55. `worktree-agent.md:26`: `sed -i` reads as a heredoc. Fix: "nor through `sed -i` or redirection".
56. `improve-workflow:26`, `:28`: "highest level" and "narrowest level" mean different things. Fix: "Fix it with the strongest mechanism that works".
57. `maintain-skills:31` names steps that do not exist ("the usage and source steps"), and `:66` makes a worktree only in a Git repository.
58. `sync-skills.sh:48`: move the comment on supporting directories above `:39`.
59. `tidy-docs`: bracket-form argument hint, and a finish criterion.
60. `measurement.md:9`: "can cut the run time by at most 10%", and drop the repeated "interleave the sides" at `:5`.
61. `AGENTS.md:13`: the handoff sentence repeats the global rules. Fix: "as the user's rules for other repositories say".
