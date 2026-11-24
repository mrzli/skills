---
name: handoff
description: Write a handoff document so another agent can continue the work, either the current session's work on this or another machine, or agreed work for a session in another repository, even a single setting or rule change. Use for every handoff, including one the user's rules call for without being asked. A handoff can be limited to a given scope or focus.
argument-hint: "[same or other machine] [scope or next focus]"
---

## Argument

The argument can specify the target, the scope, or both, in any order:

- **Target:** whether the next session runs on the same machine or another one. Default to the same machine.
- **Scope:** which part of the conversation or work to hand off, or what the next session will focus on. Default to the whole current conversation. For work passed to another repository, default to that work.

If the handoff is to the same machine, save the document in the operating system's temporary directory (`$TMPDIR`, else `/tmp`), outside the project, and report its path. Name it `handoff-<target>-from-<source>-<topic>.md`, with the target and source repositories' directory names and a short topic, such as `handoff-archon-from-skills-response-order.md`, so a session in the target repository can find it. A handoff within one repository has the same target and source. If the handoff is to another machine, give the whole document in your reply, so the user can copy it.

## Content

Write a handoff document that summarizes the work in scope, so a fresh agent can continue it. Start it with a title line that names the target repository, such as `# Handoff: one ordering rule for responses (for archon)`.

Include a "suggested skills" section naming the skills the next agent should use.

Refer to items as the user's rules for IDs say for files that outlive the session. Without such rules, name each item by its record and number, such as "backlog 12", and describe any other item in words, rather than by an ID from this conversation.

Reference existing artifacts (specs, plans, decision records, issues, commits, and diffs) by path or URL instead of duplicating their content. Assume another machine has the same repository. For local resources outside the repository, summarize them or include their full contents if very short.

For work passed to another repository, ask only for the change to that repository's files, not for applying or deploying it, because its instructions decide how and when a change is applied.

Redact any sensitive information, such as API keys, passwords, or personally identifiable information.

Cover the scope's part of the work and the context it depends on, and leave out unrelated threads.

## In a fork

In a fork opened by the `spawn` skill, pass a handoff to another repository up as that skill says for forks, instead of writing it.
