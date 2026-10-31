---
name: spawn
description: Open a fork in a new terminal tab to discuss one point there, started from a short brief or from a full copy of the conversation, and later bring the result back with yield and collect.
argument-hint: "[full] [point, such as an ID like F2]"
disable-model-invocation: true
---

Open a fork of this session in a new terminal tab, so the user can discuss one point there while this session continues. Forks can spawn forks of their own, from a brief or as a full copy.

Forks only discuss. The script tells each fork not to change the checkout and blocks the file-editing tools there. A fork may still write temporary files outside the checkout, such as a throwaway script in its session scratch folder, because they cannot mix with changes in the checkout. Changes the user approves in a fork pass up through [yield](../yield/SKILL.md), and the main session, the one that is not a fork, implements them when it runs [collect](../collect/SKILL.md). All changes to the checkout then happen in one session. Handoffs to other repositories pass up the same way. A fork writes none. When the user asks for one or the work calls for one, the fork notes only which repository it is for and what change it should ask for, and the main session writes the handoff.

The argument names the point, usually an ID from this conversation, such as F2 or B7d2, and sometimes free text. Record the fork's topic as the ID plus a few words, such as `F2: zoom cap`, because the ID alone means nothing outside this conversation.

## Brief (default)

The fork is a new session that starts from a brief instead of the whole conversation. If no point is given, ask the user which one.

Write the brief in Markdown, kept short. It holds what the fork needs to discuss the point well and nothing else:

- The point, with its ID in this conversation, and what the user wants from the discussion.
- The decisions, constraints, and rejected options that bear on it, with the IDs this conversation uses for them.
- Pointers to the relevant files, commits, records, or handoffs, rather than their contents.

Pass it on standard input to [agent-joins.sh](scripts/agent-joins.sh) `spawn TOPIC` without showing it to the user or asking for approval.

## Full copy

With `full`, the fork is a copy of this whole conversation. Run [agent-joins.sh](scripts/agent-joins.sh) `spawn --full`, adding the topic if a point is given, so the fork is told to focus on it.

## After spawning

The script names the fork after this session, such as `Claude-1` for the first fork of `Claude` and `Claude-1-1` for a fork of that, records it, and opens it in a new herdr or tmux tab. If it reports that the agent or terminal is unsupported, tell the user and stop.

Treat spawning like a command: write nothing to the user before or after it, and report only a failure. The user runs [yield](../yield/SKILL.md) in the fork to pass its results up, and [collect](../collect/SKILL.md) here or in any session above to take them in.

Codex is not supported yet. The script needs Codex's own session ID to fork it exactly with `codex fork <id>`, and it is not known whether Codex exposes that ID to commands.
