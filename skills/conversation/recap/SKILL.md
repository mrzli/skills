---
name: recap
description: List what is done, in progress, and remaining in the current work. Use when the user asks to recap, relist, or summarize the status of a multi-item effort or backlog.
argument-hint: "[scope, such as a plan, group, or topic]"
---

Give the user a current, complete status of the work, so they can choose what to do next without rereading the conversation.

## Gather the state

Use the argument to narrow the scope. Otherwise cover the whole effort under discussion, not just the latest batch.

Read the existing plan, progress record, or task list when one exists, such as a `docs/plans/` file or a `.scratch/delivery/` record. Combine it with items raised, agreed, deferred, or dropped in the conversation. Check the repository state, such as branches, commits, and the working tree, where status depends on it. Report status from evidence, not intent.

## Report

List the items in these groups, omitting empty groups:

- **Done**, with the merge or commit state when relevant.
- **In progress**, including unmerged branches and work awaiting review.
- **Remaining**, in recommended order, marking blocked items and what blocks them.
- **Dropped or deferred**, only when the user decided this in the current effort.

Keep each item to one line, and keep the identifiers already in use. Mark items found only in the conversation, not in a written plan. Flag any item whose status is uncertain.

End with the recommended next item. Update an existing progress record only if the user asks.
