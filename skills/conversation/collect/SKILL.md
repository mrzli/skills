---
name: collect
description: Take in the notes left by this thread's finished forks and state what they mean for the current work. Use in a thread whose forks, opened by spawn, have run yield.
disable-model-invocation: true
---

Bring the results of this thread's finished forks into the conversation. Each fork wrote its note with [yield](../yield/SKILL.md).

1. Find the repository's shared Git directory with `git rev-parse --path-format=absolute --git-common-dir`. If the current directory is not in a Git repository, say so and stop.
2. Read the notes in `<shared Git directory>/agent-joins/<own session ID>/`. In Claude Code, the own session ID is `CLAUDE_CODE_SESSION_ID`. If there are no notes, say so and stop.
3. For each note, state its decisions and what they mean for the current work, including anything they change in what this thread planned or agreed. List what is still open.
4. Delete each note once it is taken in, and the folder once it is empty. Keep no archive. The decisions are now in the conversation, and durable ones belong in the project's tickets or documentation.
