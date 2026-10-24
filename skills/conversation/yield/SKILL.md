---
name: yield
description: Write a short note of what a forked conversation has resolved, for the tabs above it to take in with collect. Use in a fork opened by spawn, once or again whenever its results change.
argument-hint: "[focus]"
disable-model-invocation: true
---

Record what this fork has resolved so far, so the tabs it came from can take it in with [collect](../collect/SKILL.md) without the user copying summaries. Each fork has one note. Yielding again replaces it with the latest state, so write the whole picture each time, not only what changed.

Write the note in Markdown, kept short:

- The topic.
- The decisions, each with its reason. Refer to the parent's items by the parent's IDs, such as those in the fork's brief, so the note reads in the parent's terms.
- What is still open.
- Files changed and commits made, if any.

Use the argument, if given, to narrow or focus the note.

Pass the note on standard input to [agent-joins.sh](../../shared/scripts/agent-joins.sh) `yield`. The script adds the fork's name, parent, session ID, and version. If it reports that this tab is not a fork opened by [spawn](../spawn/SKILL.md), tell the user and stop.

Report the note's version and the tabs above that can collect it.
