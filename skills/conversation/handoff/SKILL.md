---
name: handoff
description: Compact the current session into a handoff document so another agent can continue the work. Use when the user wants to continue in a new session on this or another machine, or when agreed work must be passed to a session in another repository, optionally for a given scope or focus.
argument-hint: "[same or other machine] [scope or next focus]"
---

## Argument

The argument can specify the target, the scope, or both, in any order:

- **Target:** whether the next session runs on the same machine or another one. Default to the same machine.
- **Scope:** which part of the conversation or work to hand off, or what the next session will focus on. Default to the whole current conversation.

If the handoff is to the same machine, save the document in the operating system's temporary directory (`$TMPDIR`, else `/tmp`), outside the project, and report its path. If the handoff is to another machine, give the whole document in your reply, so the user can copy it.

## Content

Summarize the current conversation in a handoff document so a fresh agent can continue the work.

Include a "suggested skills" section naming the skills the next agent should use.

Refer to items as the user's rules for IDs say for files that outlive the session. Without such rules, name each item by its record and number, such as "backlog 12", rather than by an ID from this conversation.

Reference existing artifacts (specs, plans, decision records, issues, commits, and diffs) by path or URL instead of duplicating their content. Assume another machine has the same repository. For local resources outside the repository, summarize them or include their full contents if very short.

For work passed to another repository, ask only for the change to that repository's files, not for applying or deploying it, because its instructions decide how and when a change is applied.

Redact any sensitive information, such as API keys, passwords, or personally identifiable information.

When a scope is given, cover that part of the work and the context it depends on, and leave out unrelated threads.

## In a fork

In a fork opened by `spawn`, pass a handoff to another repository up as spawn says for forks, instead of writing it.
