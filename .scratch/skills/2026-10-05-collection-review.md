# Skill collection review, 2026-10-05

## Initial recommendation

Keep the current 27 skills. No addition, merge, or retirement is justified by the available use evidence. The strongest conditional trial is a small, persistent decision map for an effort that spans sessions and still has unresolved direction. Trial that procedure on real work before creating a dedicated skill.

The initial invocation authorized a review, which added only this maintenance record. The user subsequently requested a dedicated prototype skill, as recorded below.

## Evidence and scope

Local baseline: `e33c7ffa1a876991bcfcf549e58a565e7a5750e2`, with a clean working tree at review start. Reviewed the collection's descriptions and bodies using this session's reads and the preceding documentation review. Reused [engineering progress](../engineering-skills-progress.md), [original goals](../skills-review-goals.md), and the [history retrospective](../workflow/2026-10-05-codex-history-review.md). This was not a second audit of the raw chat histories.

The available evidence shows recurring implementation, debugging, explanation, handoff, and skill-maintenance work. It does not provide reliable per-skill usage or opportunity counts. Installation and discovery links are not usage evidence. Rare activities such as releases therefore remain eligible for retention.

The recent failures to apply writing guidance preceded the final verification instruction in `fe9f7fe` and the repository-wide cleanup in `e33c7ff`. The last cleanup provides one successful execution example, not proof that future mistakes are eliminated. Keep that correction under observation instead of adding another rule now. The user intentionally manages synchronization of the user installation separately. The Archon-specific profiling preference remains delegated elsewhere.

## External source baseline

Checked upstream HEAD with `git ls-remote` and inspected a temporary clone at [Matt Pocock's revision 24fe0ef](https://github.com/mattpocock/skills/tree/24fe0ef7737efae15c87225755e9f6f5965e4888). Scope was `skills/engineering` and `skills/productivity` only. The existing local reference clone was clean at `d81f3a183412e71a5b1e84ca21bc1a35eea03a60` and was left untouched.

Screened descriptions for all 20 engineering and seven productivity skills. A file-content comparison of both directories found only `ask-matt/SKILL.md` changed between those revisions. That change recommends a retrospective after a bug fix. It does not establish a missing capability here, since `improve-workflow` already covers that activity.

Read candidate bodies for `wayfinder`, `ask-matt`, `triage`, `wizard`, `domain-modeling`, `tdd`, `prototype`, `pr`, `research`, `grilling`, `wait-what`, `writing-for-agents`, and `handoff`. Read the Wayfinder local tracker conventions, domain glossary and ADR formats, prototype UI and logic guides, writing skill mechanics, and phase-boundary guide. Remaining candidates were screened by description and prior comparison notes, not fully re-audited. Triage and wizard helpers, TDD companions, and remote tracker adapters were not audited for adoption or executed.

The upstream license is MIT. Any future adaptation must retain applicable copyright and permission notices. No upstream content was copied into a skill in this review. The upstream invocation-mechanics guidance was treated as that collection's assumptions, not as verified behavior of every agent environment.

## Decisions and overlap

| Area | Assessment | Decision and next evidence |
| --- | --- | --- |
| Engineering execution | `implement`, `fix-bug`, and `refactor` share execution but add different inputs and completion criteria. The latter two already call `implement`. `deliver-feature` coordinates broader work. | Keep. On the next bug or refactor, check whether the caller carries its constraints into implementation without duplicating review. Merge only if actual use shows the distinction adds no value. |
| Planning | `start-project`, `shape-feature`, `design`, `write-spec`, and `plan` produce different decisions or artifacts. They permit small tasks to skip unnecessary stages. | Keep. Watch whether a small request reaches implementation without an unnecessary planning sequence. Shared questions alone are not a reason to merge. |
| Maintenance | `improve-workflow` diagnoses friction in completed work. `maintain-skills` evaluates collection boundaries and external candidates. | Keep both. This review exercised upstream comparison and recorded a source baseline. It does not yet prove that its recommendations improve outcomes. |
| Writing | `writing-text` supplies shared prose guidance, `writing-skills` and `writing-agents` specialize it, and `tidy-docs` applies cleanup to a selected scope. | Keep. These are composition relationships. During the next three naturally occurring skill edits, check repository-wide cleanup, prose review, then sync. Revisit only a demonstrated remaining failure. |
| Conversation and learning | `clarify`, `restate`, `explore`, `interrogate`, `handoff`, and `teach` serve explanation, intent confirmation, exploration, deliberate stress-testing, transfer, and sustained learning. | Keep. Do not import `wait-what`, `handoff`, or another interview wrapper for already-covered outcomes. Evaluate the recent `clarify` trial on a mechanism explanation before changing it again. |

## Conditional additions

### Decision mapping across sessions

[Wayfinder](https://github.com/mattpocock/skills/blob/24fe0ef7737efae15c87225755e9f6f5965e4888/skills/engineering/wayfinder/SKILL.md) maintains a destination, decision dependencies, resolutions, and questions not yet precise enough to schedule. It stops when the route is clear. It supports a local Markdown tracker as well as configured remote trackers.

There is meaningful overlap with `start-project`, `interrogate`, `investigate`, and `plan`, but no local skill explicitly owns that persistent exploration map. Wayfinder would coordinate those activities rather than subsume them. Its direct adoption also brings tracker conventions, companion skills, research delegation, and a one-ticket-per-session rule, with an exception for research. Those costs are not justified merely by wanting clearer project planning.

Trial a single local map on the next genuinely uncertain effort spanning at least two sessions. Use existing skills to resolve its questions. Keep the procedure if the second session can identify the next unblocked question and resume without reconstructing settled decisions. Consider a dedicated skill only if this recurs. Evidence of interest exists in this conversation, but evidence of repeated lost decision state does not.

### Domain modeling and interactive prototypes

`domain-modeling` adds active terminology checks against code and persistent domain definitions. Local planning skills address terminology and record decisions, but do not supply the same dedicated glossary procedure. This review deferred it until conflicting domain terms repeatedly caused design mistakes.

Update, 2026-10-16: a different failure appeared first. In qt-market-chart, terms clear to the agent, such as "inspection" and "engine", stayed opaque to the user across sessions, and a naming pass did not catch them because the names were accurate. The skills consumed terminology, but none created or maintained it. The glossary part of `domain-modeling` was adapted as `glossary`, without its ADR part, with code names allowed in entries and `docs/glossary.md` as the default location. `start-project`, `design`, `shape-feature`, `refactor`, `clarify`, and `writing-agents` point to it. `teach` keeps its own glossary format for learning workspaces.

`prototype` offers concrete UI alternatives and interactive state demonstrations beyond the general experiments in `investigate` and sketches in `design`. On the next design decision that words cannot settle, use a disposable demonstration through those existing skills. A useful trial resolves the stated choice without leaving prototype scaffolding in production. Add a separate skill if repeated requests benefit from a consistent procedure. No such gap was confirmed by this review.

## Defer or decline

- Defer `triage` until incoming external issues or PRs create an actual classification and follow-up burden. Its state machine is distinct, but that workload is not established here.
- Defer `wizard` until a substantial human-only setup sequence recurs. The prior objection to permanent one-off setup machinery argues for a task-local solution first.
- Decline a separate `tdd` import now. Local implementation already requires observable behavior and independent expected results. Upstream's mandatory confirmation of test boundaries would add a gate the user previously rejected.
- Decline `pr` as a default template. Its mandatory visual and risk sections add structure without a demonstrated PR-writing problem. Reuse concise project-specific PR conventions.
- Keep `to-questionnaire` excluded according to the user's earlier preference. Do not install the upstream setup workflow merely to obtain already-covered engineering skills.

## Verification and resumption

This was a static responsibility comparison, not behavioral testing of upstream skills. No skill code, invocation settings, discovery links, or installed copies changed. Local links in this record and diff whitespace were checked. No skill-change tidy/sync cycle was triggered by adding a review record alone.

On the next review, start from upstream `24fe0ef7737efae15c87225755e9f6f5965e4888`, inspect relevant changes since that revision, and revisit the trial criteria only when new work supplies evidence. The [2026-10-08 review](2026-10-08-collection-review.md) superseded the guidance on retirement. Reviews now save usage counts and may propose retiring skills unused for several months. No recurring review was scheduled.

## Authorized prototype addition

After reviewing the overlap, the user explicitly requested a dedicated [prototype](../../skills/engineering/investigation/prototype/SKILL.md) skill. The collection now has 28 skills. This supersedes the recommendation to defer that addition, without establishing its effectiveness on real tasks.

The skill uses Matt Pocock's `prototype`, `UI.md`, and `LOGIC.md` at the revision above as idea sources. It retains interactive comparisons, visible state, and disposable artifacts in one self-contained procedure. It follows project conventions, permits proportional verification, and leaves production implementation to `implement`. It does not impose tracker setup, a fixed UI switcher, or throwaway branches. `guide`, `design`, and `investigate` now route to it where appropriate. Existing MIT attribution remains in `LICENSES.md`.

Evaluate the next UI comparison and state-model demonstration for ease of running, useful feedback, honest simulation boundaries, and a clear conclusion or unresolved question. Structural validation and manual scenario review do not replace those real-task trials.
