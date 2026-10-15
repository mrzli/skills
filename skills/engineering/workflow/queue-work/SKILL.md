---
name: queue-work
description: Keep discussing upcoming work items with the user while a background agent implements the agreed ones, one batch at a time. Use when the user wants to agree on items in conversation without waiting for each implementation.
disable-model-invocation: true
---

Let the user keep deciding the next work items while the items already agreed are implemented in the background. The user decides what is agreed and when a batch starts. Discussion can run ahead of implementation, but implementation is a single queue.

## Keep a queue

Keep the queue in a temporary plan file that follows the project's conventions for plans, or in `.scratch/delivery/<slug>.md` if the project has none. For each item, record:

- The agreed decision, with exact names, values, and choices, so an implementer can act without the conversation.
- Its status: agreed, in progress, integrated, or blocked.
- Its commit, once integrated.

Add an item only when the user has agreed to it. A question is not approval, and approving one item does not approve others. When later discussion changes an item that is not yet implemented, update its decision. When it changes an item already in progress or integrated, add a new item.

## Run a batch

Start a batch only when the user asks, such as "do the next three agreed items". Run one implementer at a time. Items often touch the same files, so parallel implementers would conflict.

Start a background agent from the tip of the user's branch, so it builds on integrated work. Give it its own worktree and build directory when the tools allow. Pass it the agreed decisions themselves, not only a pointer to the queue. Tell it to:

- Use [implement](../../delivery/implement/SKILL.md) for each item in order, with one commit each, and run the project's required checks.
- Leave the queue file to the main agent.
- Make routine choices that follow from the decisions and project conventions, and list every choice the decision did not settle.
- Stop at an item that needs a choice the user would make, such as a name, user-visible behavior, an interface, or scope. Keep the commits for earlier items, and report the question.

If background agents are unavailable, say so and implement the batch in the foreground.

While the batch runs, keep discussing the next items and adding agreed ones to the queue. Avoid running checks that need a resource the implementer is using exclusively, such as a GPU, a display, a port, or a build directory.

## Integrate and report

When the implementer finishes, read each commit's diff against its agreed decision. Use [review-code](../../delivery/review-code/SKILL.md) when a commit goes beyond its decision or the implementer reports a finding it did not resolve. Bring the commits onto the user's branch following the user's integration rules, rerun the required checks if integration changed them, and update the queue. Then remove the worktree and delete the implementer's branch.

Report for each item what changed, its commit, and the checks and their results. List every choice the implementer made beyond the agreed decision, or state that there were none. Raise any blocking question in the discussion.

Follow the user's and the project's branch and commit conventions. Merge only when the user asks. When the queue is done, finish the plan file as the project's conventions say, such as moving lasting decisions into the permanent docs and deleting the plan.
