---
name: spawn
description: Open a fork in a new terminal tab to discuss one point there, started from a short brief or from a full copy of the conversation, and later bring the result back with yield and collect.
argument-hint: "[full] [point, such as an ID like F2]"
disable-model-invocation: true
---

Open a fork of this tab in a new terminal tab, so the user can discuss one point there while this tab continues. Forks can spawn forks of their own, from a brief or as a full copy.

The argument names the point, usually an ID from this conversation, such as F2 or B7d2, and sometimes free text. Record the fork's topic as the ID plus a few words, such as `F2: zoom cap`, because the ID alone means nothing outside this conversation.

## Brief (default)

The fork is a new session that starts from a brief instead of the whole conversation. If no point is given, ask the user which one.

Write the brief in Markdown, kept short. It holds what the fork needs to discuss the point well and nothing else:

- The point, with its ID in this conversation, and what the user wants from the discussion.
- The decisions, constraints, and rejected options that bear on it, with the IDs this conversation uses for them.
- Pointers to the relevant files, commits, records, or handoffs, rather than their contents.

Show the brief to the user and wait for their corrections or approval, because it is all the fork will know. Then pass it on standard input to [agent-joins.sh](../../shared/scripts/agent-joins.sh) `spawn TOPIC`.

## Full copy

With `full`, the fork is a copy of this whole conversation. Run [agent-joins.sh](../../shared/scripts/agent-joins.sh) `spawn --full`, adding the topic if a point is given, so the fork is told to focus on it.

## After spawning

The script names the fork after this tab, such as `Claude-1` for the first fork of `Claude` and `Claude-1-1` for a fork of that, records it, and opens it in a new herdr or tmux tab. If it reports that the agent or terminal is unsupported, tell the user and stop.

Report the fork's name. Tell the user to run [yield](../yield/SKILL.md) in the fork to pass its results up, and [collect](../collect/SKILL.md) here or in any tab above to take them in. Then continue this conversation.

Codex is not supported yet. The script needs Codex's own session ID to fork it exactly with `codex fork <id>`, and it is not known whether Codex exposes that ID to commands.
