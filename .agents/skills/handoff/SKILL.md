---
name: handoff
description: Compact the current session into a format suitable for handoff to another agent.
argument-hint: Same machine or different one?
---

## Argument

Argument specifies whether the handoff is to the same machine or another one. If nothing is provided, default to same machine.

If the handoff is to the same machine, save the document in the operating system's temporary directory, outside the current workspace. If the handoff is to another machine, print the handoff content to the console.

## Content

Summarize the current conversation in a handoff document so a fresh agent can continue the work.

Include a "suggested skills" section naming the skills the next agent should use.

Do not duplicate content already captured in other artifacts (specs, plans, ADRs, issues, commits, diffs). Reference them by path or URL instead. This is true even if handoff is for another machine. Another machine is assumed to have the same repo. The only exception are local resources outside of repo. Try to summarize those or copy them entirely if they are very short.

Redact any sensitive information, such as API keys, passwords, or personally identifiable information.

Treat any arguments as the next session's focus and tailor the document accordingly.
