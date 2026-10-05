---
name: review-architecture
description: Assess an existing codebase's structure and identify evidence-backed improvement opportunities. Use for architectural friction, coupling, unclear responsibilities, or difficulty changing and testing a subsystem, rather than review of one diff.
---

Produce a scoped assessment and prioritized recommendations. Architecture review identifies worthwhile work. It does not automatically redesign or refactor the codebase.

## Select the scope

Use the subsystem, concern, or pain point named by the user. If none is given, inspect project purpose, recent change history, and recurring maintenance problems to choose a useful starting area. State the scope and widen it only when necessary to understand dependencies.

Read project instructions, terminology, relevant architectural decisions, and the code itself. Trace representative flows across interfaces, state ownership, persistence, and external dependencies. Use diagrams only when they clarify relationships better than prose.

## Assess the structure

Look for concrete friction: one policy duplicated across callers, a routine change scattered across unrelated areas, hidden coupling, unclear ownership, or interfaces that force callers to understand internal details. Examine how tests exercise behavior and whether the structure makes realistic verification difficult.

Ground each concern in specific files, call paths, examples, or historical changes. Distinguish architectural causes from isolated implementation defects, missing tests, or a lack of documentation. File size, number of modules, or deviation from a favorite pattern is not sufficient evidence on its own.

Evaluate proposed improvements against the system's actual scale, constraints, and maintenance needs. Prefer concentrating related behavior and simplifying interfaces over adding layers by default. Include the option of retaining the current structure when the migration cost exceeds the likely benefit.

Respect existing decisions and explain why new evidence warrants revisiting one. Investigate uncertain performance or operational claims rather than attributing them to architecture without evidence. Separate observed problems from speculative future concerns.

## Recommend next steps

For each worthwhile candidate, report the affected area, evidence, concrete consequence, proposed direction, expected benefit, migration cost, compatibility risk, and verification needs. Rank by expected value and strength of evidence. A short list or no recommended changes is a valid result.

Recommend a bounded next action: further investigation, technical design, or a selected refactor. Keep a broad assessment distinct from committing to a replacement architecture. Preserve relevant behavior constraints for the next skill.

Return a concise assessment. For a substantial review or requested record, use the project convention or `.scratch/architecture/<descriptive-slug>.md`. Finish with the strongest recommendation and what would need to be learned before acting, including limitations of the reviewed scope.
