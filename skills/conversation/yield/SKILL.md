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
- Agreed to implement: each change the user explicitly approved in this fork, with the exact names, values, and choices an implementer needs without the conversation. Give each a source ID made of this fork's name and the item's ID, such as `Claude-1/F2a`, and keep it unchanged in later versions of the note. Give an item without an ID in the conversation the next free one. Leave out changes that were discussed but not approved.
- What is still open.

When this fork has collected notes from forks below it, carry their agreed items into this note with their source IDs unchanged, so they reach the top tab.

Use the argument, if given, to narrow or focus the note.

Pass the note on standard input to [agent-joins.sh](scripts/agent-joins.sh) `yield`. The script adds the fork's name, parent, session ID, and version. If it reports that this tab is not a fork opened by [spawn](../spawn/SKILL.md), tell the user and stop.

Treat yielding like a command: write nothing to the user before or after it, and report only a failure.
