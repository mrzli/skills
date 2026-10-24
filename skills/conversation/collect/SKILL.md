---
name: collect
description: Take in the notes yielded by forks below this tab, at any depth, and apply them to the current work. Use in a tab whose forks, opened by spawn, have run yield.
disable-model-invocation: true
---

Bring the results of forks below this tab into the conversation. Each fork wrote its note with [yield](../yield/SKILL.md).

Run [agent-joins.sh](scripts/agent-joins.sh) `collect`. It prints the notes that are new or changed since this tab last collected, from children, grandchildren, and further down, and records them as read. A note stays until every tab above its fork has collected its latest version.

Keep the reply very short: one line per collected note, saying only what happened, such as `Claude-2 (FF1): resolved, design in docs/design/stock-exclusions.md`, or `No new notes.` Do not summarize the decisions. The notes are now in the conversation. Apply their decisions to the current work from here on, and refer to them when they become relevant.

The one exception is a tree the script reports as inactive for 14 days. Ask in one line whether to delete it, and on a yes run the script's `prune` command with the tree's top tab. Do not prune without the user's answer.

Durable decisions belong in the project's tickets or documentation, not only in the conversation.
