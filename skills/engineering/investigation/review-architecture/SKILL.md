---
name: review-architecture
description: Assess an existing codebase's structure against the project's architecture rules and identify evidence-backed improvement opportunities. Use for a periodic structural review, architectural friction, coupling, unclear responsibilities, code that breaks the project's rules, or difficulty changing and testing a subsystem, rather than review of one diff.
---

Produce a scoped assessment, a summary of the modules in scope, and prioritized recommendations. The summary and the rule check let a reader who has not read the code judge its structure. Architecture review identifies worthwhile work. It does not automatically redesign or refactor the codebase.

## Select the scope

Use the subsystem, concern, or pain point named by the user. If none is given, inspect project purpose, recent change history, and recurring maintenance problems to choose a useful starting area. State the scope and widen it only when necessary to understand dependencies.

Read project instructions, terminology, relevant architectural decisions, and the code itself. Collect the project's architecture rules from its `AGENTS.md` files and its architecture or conventions documents, such as rules about mutability, global state, or which modules may depend on a framework. Trace representative flows across interfaces, state ownership, persistence, and external dependencies. Use diagrams only when they clarify relationships better than prose.

## Summarize the modules

Summarize the modules in every review. For a whole-system review, cover each top-level module. For a scoped review, cover the modules in scope and name the neighbors they depend on. For each module, give its purpose, public types or interfaces, which module owns its state, what is mutable, any global state, and its external dependencies, such as a framework or a service. Use a dependency graph the project generates when one exists. Keep the summaries separate from the findings, and write them so a reader can follow them without opening the code.

## Check the project's rules

Check the code in scope against each collected rule. Report each violation with the rule, its source, and the files or call paths that break it. When the project states no architecture rules, say so and judge the structure by general principles.

## Assess the structure

Look for concrete friction: one policy duplicated across callers, a routine change scattered across unrelated areas, hidden coupling, unclear ownership, or interfaces that force callers to understand internal details. Examine how tests exercise behavior and whether the structure makes realistic verification difficult.

Ground each concern in specific files, call paths, examples, or historical changes. Distinguish architectural causes from isolated implementation defects, missing tests, or a lack of documentation. File size, number of modules, or deviation from a favorite pattern is not sufficient evidence on its own.

Evaluate proposed improvements against the system's actual scale, constraints, and maintenance needs. Prefer concentrating related behavior and simplifying interfaces over adding layers by default. Weigh migration cost as the user's rules for recommendations say. Without such rules, weigh one-off migration work far below the lasting benefit. Include the option of retaining the current structure when the benefit does not justify the migration.

Respect existing decisions and explain why new evidence warrants revisiting one. Investigate uncertain performance or operational claims rather than attributing them to architecture without evidence. Separate observed problems from speculative future concerns.

## Recommend next steps

Report rule violations as findings, ranked with the other candidates. For a violation that the project should accept instead of fixing, recommend changing the rule. For each worthwhile candidate, report the affected area, evidence, concrete consequence, proposed direction, expected benefit, migration cost, compatibility risk, and verification needs. Rank by expected value and strength of evidence. A short list or no recommended changes is a valid result.

Recommend a bounded next action: further investigation, technical design, or a selected refactor. Keep a broad assessment distinct from committing to a replacement architecture. Preserve relevant behavior constraints for the next skill.

Return the module summaries, then a concise assessment. For a substantial review or requested record, use the project convention or `.scratch/architecture/<descriptive-slug>.md`. Finish with the strongest recommendation and what would need to be learned before acting, including limitations of the reviewed scope.
