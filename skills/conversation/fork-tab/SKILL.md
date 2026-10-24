---
name: fork-tab
description: Open a fork of the current conversation in a new terminal tab, to discuss one topic there and later hand the result back with conclude and join.
argument-hint: "[topic]"
disable-model-invocation: true
---

Open a fork of this conversation in a new tab, so the user can discuss one topic there while this thread continues. A fork is a copy of the conversation so far that continues as its own session. When the topic is done, the user runs [conclude](../conclude/SKILL.md) in the fork and [join](../join/SKILL.md) here.

Take the topic from the argument, or from the conversation if none is given. Keep it to a few words, since it becomes the tab label and the fork's session name.

Run [open-fork.sh](scripts/open-fork.sh) with the topic as its only argument. It detects the agent and the terminal multiplexer from the environment, opens a tab in the current directory that starts the fork, and passes this session's ID to the fork as `AGENT_PARENT_SESSION`. It supports Claude Code inside herdr or tmux. If it reports that the agent or multiplexer is unsupported, tell the user and stop.

Report the tab label, and tell the user to run `conclude` in the fork when its topic is done and then `join` here. Then continue this thread.

Codex is not supported yet. `conclude` addresses each note to the parent's session ID, so the script needs Codex's own session ID, which `codex fork <id>` would then fork exactly. It is not known whether Codex exposes that ID to commands, and `codex fork --last` alone cannot address the notes.
