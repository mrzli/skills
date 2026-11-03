---
name: collect
description: Take in the notes yielded by the sessions below this one, at any depth, apply them to the current work, queue the changes agreed in them to implement now, and write the handoffs they call for. Use in a session whose forks, opened by spawn, have run yield.
disable-model-invocation: true
---

Bring the results of the sessions below this one into the conversation. Each fork wrote its note with `yield`.

Run [agent-joins.sh](scripts/agent-joins.sh) `collect`. It says whether this session is a main session or a fork and gives its tree's ID, the start of the main session's session ID. It prints the notes from the sessions below this one, at any depth, that are new or changed since this session last collected, and records them as read. A note stays until every session above its fork has collected its latest version.

Give each collected item an ID in this session's scheme, as the user's rules for IDs say, and keep its source ID beside it as a tracking key, such as `G3 (Claude-2/FF1a)`. Without such rules, refer to each item by its source ID alone.

Keep the reply very short: one line per collected note, saying only what happened, such as `Claude-2 (FF1): resolved, design in docs/design/stock-exclusions.md; queued G3 (Claude-2/FF1a); handoff G4 (Claude-2/FF1b) at /tmp/handoff-trading-app-1a2b3c4d-Claude-2-FF1b.md`, or `No new notes.` Do not summarize the decisions. The notes are now in the conversation. Apply their decisions to the current work from here on, and refer to them when they become relevant.

Record durable decisions from the notes as the user's rules for project knowledge say. Without such rules, put them in the project's tickets or documentation, not only in the conversation.

If an agreed item or a needed handoff conflicts with a decision made in this session since the fork was spawned, ask about it in one line instead of queuing or writing it.

## Agreed items

A note's "Agreed to implement" items were approved by the user in the fork, and each has a source ID, such as `Claude-1/F2a`.

In the main session, implement the items marked `now` through `queue-work` without asking for approval again. Add the items marked `backlog` to the project's backlog with their source IDs, and start none of them. Every yield repeats the fork's whole picture, so check each item's source ID against the queue and the backlog:

- In neither: add it to the queue or the backlog, as its mark says.
- In the queue or the backlog with the same decision and mark: skip it.
- In the backlog, or in the queue and not yet started, with a changed decision or mark: update it there, and move it between the queue and the backlog when its mark changed.
- In the queue with a changed decision, already started or integrated: add it as a new item.
- In the queue, already started or integrated, with the same decision but now marked `backlog`: ask about it in one line.

Start each queued item once it is ready.

## Handoffs

A note's "Handoffs needed" items each name a target repository and the change a handoff should ask for, and each has a source ID. In the main session, write each handoff with the `handoff` skill from its item, and give its path. Name the file after this repository's directory, the tree's ID, and the source ID, with `/` replaced by `-`, such as `handoff-trading-app-1a2b3c4d-Claude-2-FF1b.md`. Fork names repeat across repositories and after a prune, so the repository and the tree's ID keep the files apart across repositories and main sessions.

Every yield repeats the fork's whole picture, so check the latest file for that source ID first. The first file has no number and counts as 1, and the latest is the one with the highest number:

- No file: write it.
- A file that asks for the same change: skip it.
- A file that asks for a different change: write a new file with the next free number added, such as `handoff-trading-app-1a2b3c4d-Claude-2-FF1b-2.md`, because a session in the other repository may already have used the old one. Say in its line that it changed.

## In a fork

Implement nothing and write no handoffs, as `spawn` says for forks. Carry the agreed items and needed handoffs into this fork's next `yield`.

## Inactive trees

In any session, the script may report a tree as inactive for 14 days. Ask in one line whether to delete it, and on a yes run the script's `prune` command with the name of the tree's main session. Do not prune without the user's answer.
