---
name: refactor
description: Improve the structure of a selected area of code while preserving its intended observable behavior. Use for a scoped restructuring, simplification, or internal migration whose purpose is maintainability rather than new functionality.
---

Deliver a structural improvement with evidence that required behavior is preserved. Start from a selected problem; if the target or benefit is unclear, inspect the area and recommend a bounded scope before a broad rewrite.

## Define what must stay the same

Read project instructions, relevant design decisions, the code, callers, and tests. State the structural problem and the concrete improvement sought, such as reducing duplicated policy or concentrating a change in one place.

Identify observable contracts: results, errors, side effects, persisted formats, public interfaces, and relevant ordering or performance expectations. Distinguish required behavior from an accidental implementation detail. Treat an intentional behavior change or bug fix as separate scope, with its own requirements and evidence.

Inspect the working tree and establish a verification baseline. Add characterization coverage when important behavior is untested, using representative cases at stable interfaces. Record uncertainty instead of assuming that existing tests cover every contract.

## Restructure incrementally

Choose a target structure that addresses the demonstrated problem with minimal unnecessary abstraction. Use design work when interface or ownership decisions are consequential. A small refactor may need only a short explanation.

Use [implement](../implement/SKILL.md) for execution, supplying the preservation constraints and baseline checks. Prefer small transformations that keep checks passing. For widespread changes, introduce a compatible form, migrate consumers, and remove the old form only after confirming no required consumers remain. Account for external consumers when repository search cannot establish that fact.

Keep unrelated formatting, dependency updates, and feature additions out of the refactor. Update tests that depend on removed internals while retaining equivalent behavioral coverage; deleting inconvenient assertions is not evidence of preservation.

## Verify the result

Compare the result against the baseline contracts and exercise affected callers, integration paths, and migration behavior as needed. Measure performance when the refactor affects a relevant performance constraint. Passing unit tests alone may not establish compatibility.

Complete the review in `implement`, checking both preservation and whether the new structure addresses the original problem. Report what became simpler, what verification supports behavior preservation, and any remaining compatibility or coverage limits. Finish only when the scoped improvement is achieved without known unintended behavior changes.
