# Engineering skills progress

## Decisions

On 2026-10-02, the user authorized implementing all remaining skills on a new branch, with one commit per skill. This supersedes the earlier instruction to wait for review between skills. Prefer concise instructions while retaining the detail needed for reliable execution. Use Matt Pocock's local clone at `/home/mrzli/projects/cloned/skills` for ideas, not as a prescribed workflow.

Skills should work individually and compose later. Avoid unnecessary human gates, mandatory planning documents for small changes, and dependencies on skills that do not yet exist. Keep project-specific commands and conventions in the project.

The learning handoff is `/tmp/software-engineering-flow-handoff-wb0g9t9d.md`. Its detailed mapping is `/home/mrzli/projects/personal/mrzli/learning/.scratch/learn/software-engineering-flow/reference/skill-map.html`. Names and grouping below supersede the earlier names in those references.

## Implemented skills and commits

| Order | Group | Skill | Status |
| --- | --- | --- | --- |
| 1 | delivery | implement | Committed as ff6d342; real-task evaluation pending |
| 2 | delivery | review-code | Committed as 8b20bf5; real-task evaluation pending |
| 3 | planning | write-spec | Committed as df7f048; real-task evaluation pending |
| 4 | planning | plan | Committed as a6fa869; real-task evaluation pending |
| 5 | planning | shape-feature | Committed as 2f94814; real-task evaluation pending |
| 6 | investigation | investigate | Committed as 7737504; real-task evaluation pending |
| 7 | planning | design | Committed as 2d9c775; real-task evaluation pending |
| 8 | delivery | fix-bug | Committed as 5292e24; real-task evaluation pending |
| 9 | delivery | refactor | Committed as 62ec0c2; real-task evaluation pending |
| 10 | delivery | release | Committed as 6700d6b; real-task evaluation pending |
| 11 | workflow | deliver-feature | Committed as 60bfb01; real-task evaluation pending |
| 12 | planning | start-project | Committed as 4481a22; real-task evaluation pending |
| 13 | investigation | review-architecture | Committed as 3561798; real-task evaluation pending |
| 14 | investigation | review-product | Committed as db6b08b; real-task evaluation pending |
| 15 | workflow | improve-workflow | Committed as 6be9dcd; real-task evaluation pending |

Paths follow `skills/engineering/<group>/<skill>/SKILL.md`. The sync script supports recursive discovery and flat destination links. All 15 skills are now implemented. The remaining 12 skills were developed on `engineering-skills`, each in its own commit with a README entry. The original checkpoint after four skills was superseded by the user's request to finish the set; real-task evaluation is still recommended.

## Implement design

Location: `skills/engineering/delivery/implement/SKILL.md`.

References inspected: Matt's engineering `implement`, `implement-spec`, `tdd`, and `code-review`, plus the learning map. Retained scoped implementation, incremental verification, behavior-focused tests, and review with correction. Kept large task-graph orchestration out of this skill.

Differences from Matt: accepts a clear request without requiring tickets; follows project testing requirements without a mandatory interview about test boundaries; supports self-review until `review-code` exists; does not prescribe commits or parallel agents. No additional reference files or metadata are needed for this first version. Automatic discovery remains enabled by default.

## Review code design

Location: `skills/engineering/delivery/review-code/SKILL.md`.

Reference: Matt's `skills/engineering/code-review/SKILL.md`. Retains review against both requirements and project conventions. Replaces mandatory issue-tracker setup, parallel agents, fixed smell catalogue, and separate verbatim reports with a self-contained review and prioritized evidence-backed findings.

Supports working-tree changes including relevant untracked files, as well as commits, branches, and pull requests. Infers scope when clear and asks only for consequential ambiguity. Accepts conversation requirements without a formal spec. Standalone review reports findings; an enclosing implementation task can authorize corrections. No mandatory subagent dependency; self-review must be identified.

Validation: all eight sync tests and the diff whitespace check passed. Both discovery links resolve to the new skill. Manually checked scope handling, missing requirements, standalone versus implementation-authorized fixes, and compatibility with `implement`. The initial validation attempt lacked PyYAML; this is now resolved by using `/usr/bin/python3`. No independent behavioral evaluation has been performed. Syncing initially required escalation; the later permission configuration now permits writes to the discovery directories.

## Write spec design

Location: `skills/engineering/planning/write-spec/SKILL.md`.

Reference: Matt's `skills/engineering/to-spec/SKILL.md`. Retains synthesis of established intent, codebase context, design commitments, testing expectations, and explicit scope. Uses observable acceptance criteria and a flexible document structure instead of an extensive required user-story list. Allows focused clarification and marks blocking unknowns rather than inventing agreement. No issue-tracker prerequisite or automatic publication. Defaults to the project convention or `docs/specs/<descriptive-slug>.md`. Does not perform planning or implementation.

Validation: diff whitespace check passed and both discovery links were verified. Manually reviewed handling of a clear small request, blocking unknowns, existing specifications, and implementation handoff. The initial validator limitation is resolved by using `/usr/bin/python3`. No independent behavioral evaluation has been performed.

## Reference mapping for the remaining skills

Matt's operational files were read from the local clone as source material, not executed as skills.

| Our skill | Reference and adaptation |
| --- | --- |
| plan | `to-tickets`: verifiable behavior slices and real dependencies; local plan by default, no mandatory tracker or approval round. |
| shape-feature | `grill-with-docs`, `domain-modeling`, and the learning map: focused clarification and explicit scope, without exhaustive interviewing. |
| investigate | `research` and `prototype`: primary evidence and focused experiments; no mandatory background agent or production edits. |
| design | `codebase-design`: useful interfaces and localized complexity, with broader compatibility and operational considerations; no imposed vocabulary. |
| fix-bug | `diagnosing-bugs`: symptom-specific reproduction, evidence-led diagnosis, regression verification; static investigation remains useful when reproduction is unavailable. |
| refactor | `codebase-design`, `implement`, and `to-tickets`: preservation contracts and incremental migration; reuses our implementation skill. |
| release | No direct equivalent in the inspected set; `pr` and the learning map inform evidence and recovery considerations. Uses project-specific delivery procedures. |
| deliver-feature | `implement-spec` and `ask-matt`: coordination and dependencies; sequential by default, durable progress, selective stages, no automatic tracker/branch/deployment assumptions. |
| start-project | `wayfinder`, `grill-with-docs`, and the learning map: direction and uncertainty; produces a brief without scaffolding a project. |
| review-architecture | `improve-codebase-architecture`: evidence of structural friction and prioritized candidates; no mandatory HTML, deep-module terminology, or automatic redesign. |
| review-product | No direct equivalent; follows the learning map's product-outcome responsibility and explicitly distinguishes observed use from heuristic assessment. |
| improve-workflow | `retro` and the learning map: evidence-based corrections, appropriate automation, and an explicit later evaluation point. |

## Validation

- All 15 engineering skills pass the bundled skill validator using `/usr/bin/python3`; its system environment includes PyYAML.
- All local skill references and README links resolve.
- The 12 skill implementation commits each contain one new skill and a README update; these notes are preserved in a separate documentation commit.
- All eight sync tests pass. Both discovery directories contain valid links for all 15 engineering skills; repeat sync makes no changes.
- Sync completed in the sandbox without approval under the updated permission profile.
- Diff whitespace checks pass. Instructions were manually reviewed for scope, outputs, authorization boundaries, and composition. This is not independent behavioral evaluation or proof of real-task effectiveness.

## Resume

The permission configuration is committed as b0e6cf7. It selects `local-development`, permits Git and skill-discovery writes, and protects the sync script from edits. The user requested retaining these scratch notes in version control when merging the work into `master`.

Try the skills on real work. In particular, exercise a small request through implementation, a multi-task feature through coordination, a bug with incomplete reproduction evidence, and release preparation without publication authorization. On 2026-10-02, the user authorized merging the work into `master` and deleting the development branch. No push was requested.

The productivity review is complete: `clarify` and the writing skills were updated, and `interrogate` was deliberately left unchanged.
