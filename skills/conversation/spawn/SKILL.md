---
name: spawn
description: Open a fork of the current conversation in a new terminal tab, to discuss one topic there and later bring the result back with yield and collect.
argument-hint: "[topic]"
disable-model-invocation: true
---

Open a fork of this conversation in a new tab, so the user can discuss one topic there while this tab continues. A fork is a copy of the conversation so far that continues as its own session. Forks can spawn forks of their own.

Run [agent-joins.sh](../../shared/scripts/agent-joins.sh) `spawn`, with the topic as an argument if the user gave one. Do not make up a topic. The script names the fork after this tab, such as `Claude-1` for the first fork of `Claude` and `Claude-1-1` for a fork of that, records it, and opens it in a new herdr or tmux tab. If it reports that the agent or terminal is unsupported, tell the user and stop.

Report the fork's name. Tell the user to run [yield](../yield/SKILL.md) in the fork to pass its results up, and [collect](../collect/SKILL.md) here or in any tab above to take them in. Then continue this conversation.

Codex is not supported yet. The script needs Codex's own session ID to fork it exactly with `codex fork <id>`, and it is not known whether Codex exposes that ID to commands.
