---
name: tidy-docs
description: Review and tidy documentation, including skills and AGENTS.md files, across a repository or selected scope.
argument-hint: "Scope to tidy. Defaults to the entire repo."
---

## Scope

Use the supplied scope. If none is provided, include the entire repo.

Scope limits which documentation files may be modified. Include hidden directories unless excluded by the scope. Skip generated files, dependencies, and version-control internals.

Read outside the scope as needed to understand the current state of the repo.

## Process

Apply the relevant skills to each document as if creating or modifying it.

Resolve inconsistencies and outdated links. Preserve behavior, requirements, and invocation settings.

Update evolving documents, such as specs, tasks, and improvement notes, based on the current state of the repo. Distinguish intended behavior from implemented behavior. Preserve unresolved requirements and decisions.
