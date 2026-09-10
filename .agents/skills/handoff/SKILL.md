---
name: handoff
description: Compact the current session into a format suitable for handoff to another agent.
---

Summarize the current conversation in a handoff document so a fresh agent can continue the work.

Include a "suggested skills" section naming the skills the next agent should use.

Do not duplicate content already captured in other artifacts (specs, plans, ADRs, issues, commits, diffs). Reference them by path or URL instead.

Redact any sensitive information, such as API keys, passwords, or personally identifiable information.

Treat any arguments as the next session's focus and tailor the document accordingly.

Save the document in the operating system's temporary directory, outside the current workspace. Print its contents to the console.
