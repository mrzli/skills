---
name: tidy-docs
description: Review and tidy documentation, including skills and AGENTS.md files, across a repository or selected scope.
argument-hint: "Scope to tidy. Defaults to the entire repo."
---

## Scope

Use the supplied scope, or the entire repo if none is provided.

Scope limits which documentation files may be modified. Include hidden directories unless excluded by the scope. Skip generated files, dependencies, and version-control internals.

Read outside the edit scope as needed to understand the repo, unless the user excludes those files from reading too.

## Process

Apply [writing-text](../writing-text/SKILL.md) and other relevant writing skills to each document.

Resolve inconsistencies and outdated links. Preserve behavior, requirements, and invocation settings.

Update evolving documents, such as specs, tasks, and improvement notes, to reflect the repo's current state. Distinguish intended behavior from implemented behavior. Preserve unresolved requirements and decisions.
