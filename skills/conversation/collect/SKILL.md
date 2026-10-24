---
name: collect
description: Take in the notes yielded by forks below this tab, at any depth, apply them to the current work, and queue the changes agreed in them. Use in a tab whose forks, opened by spawn, have run yield.
disable-model-invocation: true
---

Bring the results of forks below this tab into the conversation. Each fork wrote its note with [yield](../yield/SKILL.md).

Run [agent-joins.sh](scripts/agent-joins.sh) `collect`. It says whether this tab is a top tab or a fork, and prints the notes that are new or changed since this tab last collected, from children, grandchildren, and further down, and records them as read. A note stays until every tab above its fork has collected its latest version.

Keep the reply very short: one line per collected note, saying only what happened, such as `Claude-2 (FF1): resolved, design in docs/design/stock-exclusions.md; queued Claude-2/FF1a`, or `No new notes.` Do not summarize the decisions. The notes are now in the conversation. Apply their decisions to the current work from here on, and refer to them when they become relevant.

## Agreed items

A note's "Agreed to implement" items were approved by the user in the fork, and each has a source ID, such as `Claude-1/F2a`.

In a top tab, implement them through [queue-work](../../engineering/workflow/queue-work/SKILL.md) without asking for approval again. Every yield repeats the fork's whole picture, so check each item's source ID against the queue:

- Not in the queue: add it, and start it once it is ready.
- In the queue with the same decision: skip it.
- In the queue with a changed decision, not yet started: update the queued decision.
- In the queue with a changed decision, already started or integrated: add it as a new item.

If an item conflicts with a decision made in this tab since the fork was spawned, ask about it in one line instead of queuing it.

In a fork, implement nothing, because forks do not change the checkout. Carry the agreed items into this fork's next [yield](../yield/SKILL.md).

The one exception is a tree the script reports as inactive for 14 days. Ask in one line whether to delete it, and on a yes run the script's `prune` command with the tree's top tab. Do not prune without the user's answer.

Durable decisions belong in the project's tickets or documentation, not only in the conversation.
