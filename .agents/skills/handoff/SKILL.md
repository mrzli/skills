---
name: handoff
description: Compact the current session into a format suitable for handoff to another agent.
argument-hint: Same machine or different one?
---

## Argument

Use the argument to determine whether the handoff is to the same machine or another one. Default to the same machine.

If the handoff is to the same machine, save the document in the operating system's temporary directory, outside the current workspace. If the handoff is to another machine, print the handoff content to the console.

## Content

Summarize the current conversation in a handoff document so a fresh agent can continue the work.

Include a "suggested skills" section naming the skills the next agent should use.

Reference existing artifacts (specs, plans, ADRs, issues, commits, and diffs) by path or URL instead of duplicating their content. Assume another machine has the same repository. For local resources outside the repository, summarize them or include their full contents if very short.

Redact any sensitive information, such as API keys, passwords, or personally identifiable information.

If the user also specifies the next session's focus, tailor the document accordingly.
