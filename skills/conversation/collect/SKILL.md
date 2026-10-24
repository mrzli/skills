---
name: collect
description: Take in the notes yielded by forks below this tab, at any depth, and state what they mean for the current work. Use in a tab whose forks, opened by spawn, have run yield.
disable-model-invocation: true
---

Bring the results of forks below this tab into the conversation. Each fork wrote its note with [yield](../yield/SKILL.md).

Run [agent-joins.sh](../../shared/scripts/agent-joins.sh) `collect`. It prints the notes that are new or changed since this tab last collected, from children, grandchildren, and further down, and records them as read. A note stays until every tab above its fork has collected its latest version.

For each note, state its decisions and what they mean for the current work, including anything they change in what this conversation planned or agreed. For a changed note, say what changed since the version this conversation already knew. List what is still open. If there are no new notes, say so.

Pass on the script's other messages:

- A note kept because tabs in between have not collected it yet.
- A tree with no activity for 14 days. Ask whether to delete it, and on a yes run the script's `prune` command with the tree's top tab. Do not prune without the user's answer.

Durable decisions belong in the project's tickets or documentation, not only in the conversation.
