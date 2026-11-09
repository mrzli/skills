---
name: tidy-docs
description: Review and tidy documentation, including skills and AGENTS.md files, across a repository or selected scope. Use when asked to tidy, clean up, or check documentation for consistency, outdated content, or wording.
argument-hint: "[scope, default: the entire repository]"
---

## Scope

Use the supplied scope, or the entire repository if none is provided.

Scope limits which documentation files may be modified. Include hidden directories unless excluded by the scope. Skip generated files, dependencies, and version-control internals.

Read outside the edit scope as needed to understand the repository, unless the user excludes those files from reading too.

## Process

Apply the `writing-text` skill and other relevant writing skills to each document. Before finishing, check each edited document against them, including prose punctuation. Reading the guidance alone does not complete the review.

Resolve inconsistencies and outdated links. Preserve behavior, requirements, and invocation settings.

Update evolving documents, such as specs, tasks, and improvement notes, to reflect the repository's current state. Distinguish intended behavior from implemented behavior. Preserve unresolved requirements and decisions.

Leave dated records, such as reviews and handoffs, as written, except their status.

Finish when every document in scope passes the writing checks and no inconsistency or outdated link remains. Report the edits and anything left unresolved.
