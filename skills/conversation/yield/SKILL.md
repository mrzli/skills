---
name: yield
description: Write a short note of what a forked conversation resolved, for the thread it was forked from to take in with collect. Use in a fork opened by spawn when its topic is done.
argument-hint: "[focus]"
disable-model-invocation: true
---

Record what this fork resolved, so the thread it came from can take it in with [collect](../collect/SKILL.md) without the user copying summaries.

1. Read the environment variable `AGENT_PARENT_SESSION`. If it is not set, this thread was not opened by [spawn](../spawn/SKILL.md). Say so and stop.
2. Find the repository's shared Git directory with `git rev-parse --path-format=absolute --git-common-dir`. It is the same from every worktree. If the current directory is not in a Git repository, say so and stop.
3. Write the note to `<shared Git directory>/agent-joins/<AGENT_PARENT_SESSION>/<topic-slug>.md`, creating the directories as needed. If that file holds another fork's note, add a numeric suffix to the name.
4. Tell the user the note's path and to run `collect` in the parent thread.

Keep the note short. Include:

- The topic.
- The decisions, each with its reason.
- What is still open.
- Files changed and commits made, if any.
- This fork's own session ID, so the user can return to it. In Claude Code, it is `CLAUDE_CODE_SESSION_ID`.

Use the argument, if given, to narrow or focus the note.
