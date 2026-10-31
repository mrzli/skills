---
name: collect
description: Take in the notes yielded by the sessions below this one, at any depth, apply them to the current work, queue the changes agreed in them to implement now, and write the handoffs they call for. Use in a session whose forks, opened by spawn, have run yield.
disable-model-invocation: true
---

Bring the results of the sessions below this one into the conversation. Each fork wrote its note with [yield](../yield/SKILL.md).

Run [agent-joins.sh](scripts/agent-joins.sh) `collect`. It says whether this session is the main session or a fork, prints the notes that are new or changed since this session last collected, from the sessions below it at any depth, and records them as read. A note stays until every session above its fork has collected its latest version.

Keep the reply very short: one line per collected note, saying only what happened, such as `Claude-2 (FF1): resolved, design in docs/design/stock-exclusions.md; queued Claude-2/FF1a; handoff Claude-2/FF1b at /tmp/handoff-Claude-2-FF1b.md`, or `No new notes.` Do not summarize the decisions. The notes are now in the conversation. Apply their decisions to the current work from here on, and refer to them when they become relevant.

## Agreed items

A note's "Agreed to implement" items were approved by the user in the fork, and each has a source ID, such as `Claude-1/F2a`.

In the main session, implement the items marked `now` through [queue-work](../../engineering/workflow/queue-work/SKILL.md) without asking for approval again. Add the items marked `backlog` to the project's backlog and start none of them. Every yield repeats the fork's whole picture, so check each item's source ID against the queue:

- Not in the queue: add it, and start it once it is ready.
- In the queue with the same decision: skip it.
- In the queue with a changed decision, not yet started: update the queued decision.
- In the queue with a changed decision, already started or integrated: add it as a new item.

If an item conflicts with a decision made in this session since the fork was spawned, ask about it in one line instead of queuing it.

## Handoffs

A note's "Handoffs needed" items each name a target repository and the change a handoff should ask for, and each has a source ID. In the main session, write each handoff with [handoff](../handoff/SKILL.md) from its item, name the file after the source ID with `/` replaced by `-`, such as `handoff-Claude-2-FF1b.md`, and give its path. Every yield repeats the fork's whole picture, so check for that file first:

- No file: write it.
- A file that asks for the same change: skip it.
- A file that asks for a different change: write a new file with the note's version added, such as `handoff-Claude-2-FF1b-v3.md`, because a session in the other repository may already have used the old one. Say in its line that it changed.

## In a fork

Implement nothing and write no handoffs, because forks do not change the checkout and the main session writes every handoff. Carry the agreed items and needed handoffs into this fork's next [yield](../yield/SKILL.md).

## Inactive trees

In any session, the script may report a tree as inactive for 14 days. Ask in one line whether to delete it, and on a yes run the script's `prune` command with the tree's main session. Do not prune without the user's answer.

Durable decisions belong in the project's tickets or documentation, not only in the conversation.
