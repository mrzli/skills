---
name: recap
description: Summarize where the current work or discussion stands, including decisions, open questions, and what is done or remaining. Use when the user asks to recap, relist, reiterate, or catch up on what was discussed or what is left, asks for the status or where things stand, wants a recap of one topic, asks only for what is waiting on them, such as what they need to answer or do, or asks only for the progress of queued work, such as what is done and what remains or how long the rest will take.
argument-hint: "[scope, such as a topic, plan, group, 'status', 'mine' for only what waits on the user, or 'progress' for only the progress of queued work]"
---

Bring the user up to date so they can continue without rereading the conversation. Assume they have not read anything since their last message.

## Gather the state

Use the argument to narrow the scope. Otherwise cover the whole effort under discussion, not just the latest batch.

Read the existing specification, design record, plan, progress record, or task list when one exists, such as a `.scratch/delivery/` queue file or the project's backlog. Combine it with what was raised, agreed, rejected, deferred, or dropped in the conversation. Check the repository state, such as branches, commits, and the working tree, where status depends on it. Report from evidence, not intent.

## Report

Choose the parts that fit the scope, omitting empty ones. A discussion of a design usually needs its decisions and open questions. A backlog usually needs item status.

- **Current state of the topic:** what was decided and how the pieces fit, in plain words. Restate content the user may have skimmed rather than only pointing to it.
- **Rejected options,** briefly, when they explain a decision.
- **Open questions,** with the options and your recommendation.
- **Waiting on the user:** decisions, approvals, or actions only they can take, including ones raised before their last message. Leave out choices the user has accepted, as the user's rules for approval say. Without such rules, keep every choice until the user answers it.
- **Item status,** grouped as:
  - Done, with the merge or commit state.
  - In progress, including unmerged branches and work awaiting review.
  - Remaining, in recommended order with blockers.
  - Dropped or deferred, only when the user decided this.

Keep each item short, and keep the identifiers already in use. Give each item listed by number or ID a description of a few words, so the user can tell what it is about without asking. Mark decisions and items found only in the conversation, not in a written record. Flag anything whose status is uncertain.

End with the recommended next step. Update an existing record only if the user asks.

## Waiting on the user only

When the argument asks for it, such as `mine` or `pending`, or the user asks only for what waits on them, such as "list everything I need to answer", report only:

- **Answers needed:** each open question, choice, or approval waiting on the user, with its ID, a few words saying what it is, and the recommended option. Put first what blocks the most work.
- **Things to do:** actions only the user can take, such as pushing, running a command, or discussing in a fork.
- **Running:** at most one line naming what is in progress, so the user knows it needs nothing from them.

Leave out decisions already made, finished work, and background. This is the "Waiting on the user" part of the report alone, with the same rules for IDs and accepted choices, plus the running line. End with the recommended next step.

## Progress only

When the argument asks for it, such as `progress`, or the user asks only for the progress of queued work, such as "what's done and what remains" or "how long will it take", report only:

- **Done:** each finished item of the queue or queues, one line each with its ID and a few words.
- **Running:** the items in progress.
- **Remaining:** the items not yet started, in the order they will start, one line each with an estimate, followed by a total for the remaining work.
- **May be added:** work that waits to be slotted in, such as a design still being discussed in a fork, with its estimate when known.

Base each estimate on the measured times of earlier items of similar size, such as those recorded in a queue file. Say when there are too few measurements and an estimate is a guess. When the argument names one queue, report only that queue. Follow the same rules for IDs as the full report. End with the next step that needs the user, if there is one.
