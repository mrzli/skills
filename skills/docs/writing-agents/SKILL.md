---
name: writing-agents
description: Use when writing, editing, or reviewing AGENTS.md files.
---

Read and apply [writing-text](../writing-text/SKILL.md) to the target document.

Capture project conventions, constraints, and non-obvious context that affect the agent's work. Prefer information the agent cannot easily discover from the repository over descriptions of files, commands, or configuration it can inspect.

When the project has checks, state which ones each kind of change requires, such as documentation only, configuration, code, and before a merge. When a new worktree's build directory can be seeded from an existing checkout to avoid a full build, say how and what makes a copy unsafe.

When the project has a glossary, point to it and say to read it before naming a concept.

Keep repository-wide guidance in the root `AGENTS.md` and directory-specific guidance near the work it governs. Check applicable parent instructions before adding local guidance.

Keep each instruction in one authoritative place. Reference existing guidance instead of repeating it, and state when linked material should be read. Add detail only when it changes how the agent should work.

