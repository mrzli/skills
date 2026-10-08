# Engineering skills progress

## Decisions

On 2026-10-02, the user authorized implementing all remaining skills on a new branch, with one commit per skill. This supersedes the earlier instruction to wait for review between skills. Prefer concise instructions while retaining the detail needed for reliable execution. Use Matt Pocock's local clone at `/home/mrzli/projects/cloned/skills` for ideas, not as a prescribed workflow.

Skills should work individually and compose later. Avoid unnecessary human gates, mandatory planning documents for small changes, and dependencies on skills that do not yet exist. Keep project-specific commands and conventions in the project.

The learning handoff is `/tmp/software-engineering-flow-handoff-wb0g9t9d.md`. Its detailed mapping is `/home/mrzli/projects/personal/mrzli/learning/.scratch/learn/software-engineering-flow/reference/skill-map.html`. Names and grouping below supersede the earlier names in those references.

## Implemented skills and commits

| Order | Group | Skill | Status |
| --- | --- | --- | --- |
| 1 | delivery | implement | Committed as ff6d342. Real-task evaluation pending |
| 2 | delivery | review-code | Committed as 8b20bf5. Real-task evaluation pending |
| 3 | planning | write-spec | Committed as df7f048. Real-task evaluation pending |
| 4 | planning | plan | Committed as a6fa869. Real-task evaluation pending |
| 5 | planning | shape-feature | Committed as 2f94814. Real-task evaluation pending |
| 6 | investigation | investigate | Committed as 7737504. Real-task evaluation pending |
| 7 | planning | design | Committed as 2d9c775. Real-task evaluation pending |
| 8 | delivery | fix-bug | Committed as 5292e24. Real-task evaluation pending |
| 9 | delivery | refactor | Committed as 62ec0c2. Real-task evaluation pending |
| 10 | delivery | release | Committed as 6700d6b. Real-task evaluation pending |
| 11 | workflow | deliver (formerly deliver-feature, renamed 2026-10-08) | Committed as 60bfb01. Real-task evaluation pending |
| 12 | planning | start-project | Committed as 4481a22. Real-task evaluation pending |
| 13 | investigation | review-architecture | Committed as 3561798. Real-task evaluation pending |
| 14 | investigation | review-product | Committed as db6b08b. Real-task evaluation pending |
| 15 | workflow | improve-workflow | Committed as 6be9dcd. Used in the 2026-10-05 retrospective, with findings below |
| 16 | workflow | guide | Committed as 799d5d6. Used for skill comparison in the 2026-10-05 session |
| 17 | workflow | maintain-skills | Committed as 604e369. Initial collection review recorded on 2026-10-05 |
| 18 | investigation | prototype | Added at the user's request. Real-task evaluation pending |

Paths follow `skills/engineering/<group>/<skill>/SKILL.md`. The sync script supports recursive discovery and flat destination links. The original 15 skills are implemented and merged into `master`. `guide`, `maintain-skills`, and `prototype` were added afterward at the user's request. The remaining 12 original skills were developed on `engineering-skills`, each in its own commit with a README entry. The original checkpoint after four skills was superseded by the user's request to finish the set. Broader real-task evaluation is still recommended.

## Implement design

Location: `skills/engineering/delivery/implement/SKILL.md`.

References inspected: Matt's engineering `implement`, `implement-spec`, `tdd`, and `code-review`, plus the learning map. Retained scoped implementation, incremental verification, behavior-focused tests, and review with correction. Kept large task-graph orchestration out of this skill.

Compared with Matt's skill, this skill accepts a clear request without requiring tickets. It follows project testing requirements without a mandatory interview about test boundaries. It uses `review-code` when available, with self-review as a fallback. It does not prescribe commits or parallel agents. No additional reference files or metadata are needed for this first version. Automatic discovery remains enabled by default.

## Review code design

Location: `skills/engineering/delivery/review-code/SKILL.md`.

Reference: Matt's `skills/engineering/code-review/SKILL.md`. Retains review against both requirements and project conventions. Replaces mandatory issue-tracker setup, parallel agents, fixed smell catalogue, and separate verbatim reports with a self-contained review and prioritized evidence-backed findings.

Supports working-tree changes including relevant untracked files, as well as commits, branches, and pull requests. Infers scope when clear and asks only for consequential ambiguity. Accepts conversation requirements without a formal spec. Standalone review reports findings. An enclosing implementation task can authorize corrections. No mandatory subagent dependency. Self-review must be identified.

Validation: all eight sync tests and the diff whitespace check passed. Both discovery links resolve to the new skill. Manually checked scope handling, missing requirements, standalone versus implementation-authorized fixes, and compatibility with `implement`. The initial validation attempt lacked PyYAML. This is now resolved by using `/usr/bin/python3`. No independent behavioral evaluation has been performed. Syncing initially required escalation. The later permission configuration now permits writes to the discovery directories.

## Write spec design

Location: `skills/engineering/planning/write-spec/SKILL.md`.

Reference: Matt's `skills/engineering/to-spec/SKILL.md`. Retains synthesis of established intent, codebase context, design commitments, testing expectations, and explicit scope. Uses observable acceptance criteria and a flexible document structure instead of an extensive required user-story list. Allows focused clarification and marks blocking unknowns rather than inventing agreement. No issue-tracker prerequisite or automatic publication. Defaults to the project convention or `docs/specs/<descriptive-slug>.md`. Does not perform planning or implementation.

Validation: diff whitespace check passed and both discovery links were verified. Manually reviewed handling of a clear small request, blocking unknowns, existing specifications, and implementation handoff. The initial validator limitation is resolved by using `/usr/bin/python3`. No independent behavioral evaluation has been performed.

## Reference mapping for the remaining skills

Matt's operational files were read from the local clone as source material, not executed as skills.

| Our skill | Reference and adaptation |
| --- | --- |
| plan | `to-tickets`: verifiable behavior slices and real dependencies, local plan by default, no mandatory tracker or approval round. |
| shape-feature | `grill-with-docs`, `domain-modeling`, and the learning map: focused clarification and explicit scope, without exhaustive interviewing. |
| investigate | `research` and `prototype`: primary evidence and focused experiments, no mandatory background agent or production edits. |
| design | `codebase-design`: useful interfaces and localized complexity, with broader compatibility and operational considerations, no imposed vocabulary. |
| fix-bug | `diagnosing-bugs`: symptom-specific reproduction, evidence-led diagnosis, regression verification. Static investigation remains useful when reproduction is unavailable. |
| refactor | `codebase-design`, `implement`, and `to-tickets`: preservation contracts and incremental migration. Reuses our implementation skill. |
| release | No direct equivalent in the inspected set. `pr` and the learning map inform evidence and recovery considerations. Uses project-specific delivery procedures. |
| deliver-feature | `implement-spec` and `ask-matt`: coordination and dependencies, sequential by default, durable progress, selective stages, no automatic tracker/branch/deployment assumptions. |
| start-project | `wayfinder`, `grill-with-docs`, and the learning map: direction and uncertainty. Produces a brief without scaffolding a project. |
| review-architecture | `improve-codebase-architecture`: evidence of structural friction and prioritized candidates, no mandatory HTML, deep-module terminology, or automatic redesign. |
| review-product | No direct equivalent. Follows the learning map's product-outcome responsibility and explicitly distinguishes observed use from heuristic assessment. |
| improve-workflow | `retro` and the learning map: evidence-based corrections, appropriate automation, and an explicit later evaluation point. |

## Original implementation validation (2026-10-02)

- All 15 engineering skills pass the bundled skill validator using `/usr/bin/python3`. Its system environment includes PyYAML.
- All local skill references and README links resolve.
- The 12 skill implementation commits each contain one new skill and a README update. These notes are preserved in a separate documentation commit.
- All eight sync tests pass. Both discovery directories contain valid links for all 15 engineering skills. Repeat sync makes no changes.
- Sync completed in the sandbox without approval under the updated permission profile.
- Diff whitespace checks pass. Instructions were manually reviewed for scope, outputs, authorization boundaries, and composition. This is not independent behavioral evaluation or proof of real-task effectiveness.

## Guide design

Location: `skills/engineering/workflow/guide/SKILL.md`. Reference: Matt's `ask-matt`, read again for this addition. Provides situation-based routing across all 15 engineering activities, reads only the recommended skill, and gives one concrete next step with a tailored invocation. Supports projects without a repository and questions without an explicit argument. Keeps advice separate from execution, respects an accompanying request to proceed, and allows ordinary conversation when a skill adds no value. No mandatory tracker, document, or multi-stage process.

Validation: bundled validator and diff whitespace check passed. All 15 routing links resolve and both discovery links were verified. Manually reviewed routing for a new project, a small agreed change, diagnosis without edits, and advice with or without authorization to proceed. Real-session behavioral evaluation remains pending.

## Maintenance additions (2026-10-05)

`guide` was committed as 799d5d6. `maintain-skills` was added in 604e369 and linked from `guide` and `improve-workflow`. It reviews collection-level gaps, overlap, and retirement candidates. Small corrections within one skill remain direct work for `improve-workflow`.

The initial external idea source is Matt Pocock's engineering and productivity directories. The extensible list lives in [sources.md](../skills/engineering/workflow/maintain-skills/references/sources.md). The [initial collection review](skills/2026-10-05-collection-review.md) records the inspected upstream revision, scope, and remaining evidence gaps.

The retrospective identified ambiguity between repository-local and user-installed copies with identical names. [AGENTS.md](../AGENTS.md) now contains the local-copy preference and the synchronization requirement, committed as 92dbb26 and 1c12c4c respectively.

A proposed repository-owned validator, dependency environment, and tests were implemented but removed before commit at the user's request. Keep validation proportional to observed problems. The failed external-validator invocation used a Python interpreter without PyYAML. `/usr/bin/python3` has PyYAML on this machine, reconfirmed on 2026-10-05. This is an environment-specific fact, not a dependency guarantee for other machines.

## Current next step

Evaluate the recommendations from the initial collection review and try `prototype` on a UI comparison and an interactive logic demonstration. Continue trying the other skills on real work. In particular, exercise a small request through implementation, a multi-task feature through coordination, a bug with incomplete reproduction evidence, and release preparation without publication authorization. A successful invocation alone does not establish a skill's effectiveness.

The original development branch was merged into `master` and deleted with the user's authorization on 2026-10-02. No push was requested. The permission configuration was committed as b0e6cf7. The user requested retaining these scratch notes in version control when merging the work into `master`.

The productivity review is complete: `clarify` and the writing skills were updated, and `interrogate` was deliberately left unchanged.
