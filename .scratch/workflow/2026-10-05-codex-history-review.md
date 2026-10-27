# Codex workflow retrospective, 2026-10-05

## Scope and method

Used the repository-local `skills/engineering/workflow/improve-workflow/SKILL.md`. The initial review produced recommendations. The user subsequently authorized the general skill updates and delegated the Archon-specific change to another agent. See the outcome below.

Screened all 130 rollout files found under `~/.codex/sessions`, covering July 11 through October 5, 2026. The state database indexes the same 130 files, all present: 127 root sessions and three subagent sessions. Of the root sessions, 96 contain extracted user messages. The rest have no user messages in the rollout. Excluding subagent copies and deduplicating identical timestamp/text pairs yielded 2,204 user-message candidates. Embedded environment, skill, and AGENTS instructions were excluded from that count where identifiable. These are screening counts, not counts of failures or independent tasks.

Also screened the 1,971 entries in `history.jsonl` and reconciled the thread-history database's 98 projected threads with the rollouts. One additional session appears only in the short history, reporting a stale branch indicator. Its assistant response is unavailable. Other unmatched short-history entries mostly contain invocation markup, partial input, or transcribed replies. No archived-session directory or additional rollout location was found in the home-directory filename search.

Automated screening covered the complete available corpus. Close reading focused on correction sequences, adjacent assistant responses, relevant tool calls, and contrasting successful outcomes. This was not a line-by-line audit of every tool result. Keyword matches included ordinary questions and requested refinements, so they were not counted as failures. Voice corrections, changed preferences, and deliberate step-by-step review were not treated as agent errors by default. No chat contents were sent to external services.

Compared incidents with repository history, captured skill reads where available, current skill contents, the installed skill checkout, and relevant current project documentation. A skill's existence in Git does not prove it was available or loaded during a session. Absence of a recent complaint does not prove a fix works. Historical attribution is uncertain where the logs do not establish the loaded version.

## Recommended changes

### 1. Make historical attribution explicit in improve-workflow

At review time, the skill asked for the instructions in effect and existing findings, but did not explicitly separate an obsolete problem, an uninstalled fix, a missing instruction, and a failure to follow an existing instruction.

Suggested addition under "Examine the evidence":

> For historical reviews, compare incidents with the instructions and versions available at the time, later fixes, and the version currently installed. Distinguish unresolved gaps from already-addressed issues, deployment gaps, and failures to follow existing guidance. An old failure alone does not justify another instruction.

Evidence: the October 3 discovery failure prevented new engineering skills from being available in some sessions. The later clarification-length change addresses earlier complaints. Today's installed checkout still lacks the new maintenance workflow. Treating these as current skill defects would produce misleading recommendations.

Benefit: fewer redundant rules and more accurate recommendations. Cost: one short paragraph. Version investigation should remain proportional to the review. Evaluation: replay an incident before a known fix, one using a stale installation, and one occurring despite an existing instruction. The review should classify them differently and avoid proposing the same correction twice. This review demonstrates the classification manually, not through an independent behavioral test.

### 2. Persist Archon's test-profiling preference in Archon

On October 3, a small workspace-list change triggered full profiled test runs. The agent generalized an earlier request to profile tests, then acknowledged the user's correction: profile the tests only when explicitly asked. [User correction and following acknowledgement](/home/mrzli/.codex/sessions/2026/10/03/rollout-2026-10-03T09-04-53-01a10094-7d5f-7ae1-b59e-82ab21cae09b.jsonl:1334)

At review time, `archon/docs/archon-cli-development.md` documented `ruby tests/profile.rb` alongside ordinary verification without this restriction. A search of Archon's Markdown did not find the explicit-request rule.

Suggested change in that document's Verification section:

> Run `ruby tests/profile.rb` only when the user explicitly requests test profiling. Use the ordinary test commands for routine verification.

Benefit: preserves a concrete preference across sessions without weakening testing. Cost: one sentence in the existing project documentation. This applies to profiling Archon's tests, not all performance diagnosis and not all repositories. Evaluation: after a small workspace change, run the relevant ordinary checks. After an explicit test-profiling request, use the profiler. No further regression was confirmed after the correction, so this is a persistence gap, not proof of repeated post-fix failure.

### 3. Consider a small clarify trial, not another length rule

Some explanation failures were about the missing mechanism or an incorrect referent, not verbosity. The September 22 breakpoint discussion repeatedly restated what the hook achieved before making the build-time CSS and runtime media-query sequence explicit. On October 3, the CLI discussion initially conflated an actual controller program with a similarly named skill. The agent corrected that interpretation after several exchanges. [Breakpoint explanation sequence](/home/mrzli/.codex/sessions/2026/09/21/rollout-2026-09-21T08-30-13-01a0c2a8-6ec5-7161-9d93-d27fe7421f81.jsonl:6418), [Correction of the CLI interpretation](/home/mrzli/.codex/sessions/2026/10/03/rollout-2026-10-03T09-04-59-01a10094-933c-77a3-a591-35606e6d0bb4.jsonl:120)

The October 3 `clarify` update adds the roughly 300-word limit, natural splitting, and pauses. It does not specifically address checking the referent when repeated explanations fail. A possible trial addition is:

> If the user still does not understand, identify the missing distinction or mistaken assumption before rephrasing again. For mechanisms, name the concrete parts and trace one input through what each part does; check the code or source when the explanation depends on it.

Benefit: fewer rounds of shorter but unhelpful paraphrases. Cost: a short conditional instruction. Confidence is moderate: the clearest examples predate the latest update, and that update may already help. Evaluate on a future mechanism question before treating this as a required change. Do not tighten the length limit or rewrite the whole skill on this evidence.

## Problems that do not justify another generic skill rule now

| Pattern | Evidence and current status | Recommendation |
| --- | --- | --- |
| Long explanations | Repeated requests for smaller chunks before October 3. `a4ef16a` adds explicit chunking and a soft word limit. The installed copy includes this change. | Keep the current rule and observe later use. |
| Missing nested engineering skills | Archon discovered only shallow skill directories. Fixed by `a669629` on October 3. The session verified all 26 then-existing skills. | Do not reopen the recursive-discovery fix. |
| Ambiguous local versus installed copies | Addressed here by `92dbb26`. Tidy/sync ordering is now in `201b382`. | Keep these project instructions. |
| Unnecessary infrastructure | September objections to one-time migration code and redundant installation. October 5 validator expansion was reverted. Current `improve-workflow`, `design`, and authoring guidance already favor small corrections and reuse. | Follow existing guidance and inspect recorded solutions before proposing tooling. Do not add a validator or another maintenance system. |
| Tests that prove their fakes | Archon's October 3 cleanup removed assertions about simulated third-party internals and simplified fixtures. Current `implement` already requires observable behavior and checks beyond insufficient automated tests. | Keep behavior-focused verification. Do not infer that all mocks or tests are wasteful. |
| Real application failures despite green tests | October 3 VS Code integration used outdated Hyprland dispatchers. Initial checks simulated the commands. The later fix checked the installed API and live compositor. October 4 Herdr stop/start exposed a path different from kill/start, then gained targeted regression coverage. | For affected integrations, verify the actual contract and exact lifecycle being changed. Existing skills already support this. Do not require broad end-to-end suites for every edit. |
| Repeated permission prompts | Several incidents concerned actual sandbox/configuration boundaries. Skills-repo Git permissions and chart GUI execution were subsequently repaired and checked after restart. | Distinguish technical permission boundaries from redundant conversational approval. A generic "never ask" rule would not solve the former. |
| Slow responses | Complaints occur in multiple periods, including October 4. For the simple Linux-portability question, the recorded delay contains no intervening tool calls that establish excessive browsing or testing as its cause. | Do not claim a proven latency cause or prescribe new automation. Avoid unnecessary work, but measure causes separately if investigating latency. |

Evidence for this table: [Nested discovery diagnosis and repair](/home/mrzli/.codex/sessions/2026/10/03/rollout-2026-10-03T08-01-17-01a1005a-40c6-7b31-8152-dd1b1af82e8e.jsonl:46), [Hyprland failure and diagnosis](/home/mrzli/.codex/sessions/2026/10/03/rollout-2026-10-03T06-50-10-01a10019-246d-7b90-a044-a446197dfa66.jsonl:337), [Herdr repeat-start follow-up](/home/mrzli/.codex/sessions/2026/10/04/rollout-2026-10-04T14-12-38-01a106d4-9781-7822-95ff-f0678f5e90b1.jsonl:269), [GUI permission verification after restart](/home/mrzli/.codex/sessions/2026/10/04/rollout-2026-10-04T15-11-21-01a1070a-5b55-7d21-aefb-ec0a84d2d7e4.jsonl:1882), [Linux portability question and delay](/home/mrzli/.codex/sessions/2026/10/03/rollout-2026-10-03T17-52-22-01a10277-6a0a-7c40-a781-3c77d62d2af0.jsonl:608), [Validator reconsideration](/home/mrzli/.codex/sessions/2026/10/05/rollout-2026-10-05T03-41-14-01a109b8-e58f-77a1-969f-a67d964e3c84.jsonl:377). Earlier complexity objections: [One-time cleanup in permanent setup](/home/mrzli/.codex/sessions/2026/09/03/rollout-2026-09-03T15-08-12-01a06762-53db-70e3-aed1-dcc88552a09a.jsonl:1975), [Check existing packages before adding installation](/home/mrzli/.codex/sessions/2026/09/13/rollout-2026-09-13T02-33-12-01a0982e-b3af-7f13-a38f-6f83e56cefd3.jsonl:406).

## Deployment state

At review time, the user-installed checkout at `~/.local/share/archon-skills` was at `a4ef16a`. Its `guide` and `improve-workflow` differed from this repository, and `maintain-skills` was absent. The other 24 skill entrypoints matched.

The user confirmed that this difference is intentional while updating skills locally and will synchronize the user installation separately. It is not an outstanding problem. No user-installed files were changed here.

## Practices worth retaining

The October 4 chart performance repair used a measured baseline, identified the rendering bottleneck, compared the changed implementation, and distinguished frame timing from input latency. The user then confirmed that the application felt smooth. This supports focused profiling when performance is the reported problem. It does not support profiling every small edit. [Measurements and their limits](/home/mrzli/.codex/sessions/2026/10/04/rollout-2026-10-04T15-11-21-01a1070a-5b55-7d21-aefb-ec0a84d2d7e4.jsonl:794), [User confirmation](/home/mrzli/.codex/sessions/2026/10/04/rollout-2026-10-04T15-11-21-01a1070a-5b55-7d21-aefb-ec0a84d2d7e4.jsonl:861)

The October 3 Archon cleanup also preserved meaningful coverage while reducing fixture coupling, and the October 4 Herdr repair extended an existing test instead of adding a stress-test framework. Keep those proportional approaches.

## Outcome and next evaluation

The user authorized the general updates on 2026-10-05:

- Added historical attribution and explicit uncertainty about unverified versions to [improve-workflow](../../skills/engineering/workflow/improve-workflow/SKILL.md).
- Added the conditional mechanism-explanation guidance to [clarify](../../skills/conversation/clarify/SKILL.md) as a trial. Its existing length and splitting rules remain in place.
- The user delegated the Archon-specific profiling preference to the agent working in Archon. Its completion has not been checked here.

No new skill, merged skill, removed skill, or validation framework was added. The general updates and this report were committed in `abc1c82`. Review the next few uses against the evaluation criteria above before claiming that the changes improve outcomes.
