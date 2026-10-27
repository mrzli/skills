---
name: queue-work
description: Keep discussing upcoming work items with the user while background agents implement the agreed ones in parallel, in dependency order. Use by default to implement agreed items during an ongoing discussion, and when the user asks to queue work or do it in the background.
argument-hint: "[N]"
---

Let the user keep deciding the next work items while the items already agreed are implemented in the background. The user decides what is agreed and when a batch starts. Discussion can run ahead of implementation.

Run up to N ready items at once, or 4 when N is not given. The user can change N during the session.

## Keep a queue

Keep the queue in a temporary plan file that follows the project's conventions for plans, or in `.scratch/delivery/<slug>.md` if the project has none. If that location is ignored by Git, choose a tracked one, since the final state is committed. For each item, record:

- The agreed decision, with exact names, values, and choices, so an implementer can act without the conversation.
- Its footprint: the files and areas it is expected to touch, estimated from the decision and a search of the whole repository, including docs and comments, for the names and forms it changes.
- The earlier items it depends on.
- Its status: agreed, in progress, integrated, or blocked.
- Its commit, once integrated.
- Its source ID, when it came from a fork's note through [collect](../../../conversation/collect/SKILL.md), such as `Claude-1/F2a`.

Make an item depend on an earlier item that is not yet integrated when it builds on that item's result, when their footprints overlap, or when either changes something many files rely on, such as a specification, a shared interface, or the build configuration. When unsure, add the dependency. An item is ready when the user has agreed to it and its dependencies are integrated. Update the dependencies whenever an item is added or changed.

Add an item only when the user has agreed to it. A question is not approval, and approving one item does not approve others. An item marked `now` in a note taken in with collect is agreed, because the user approved it in the fork. When later discussion changes an item that is not yet implemented, update its decision. When it changes an item already in progress or integrated, add a new item.

## Run a batch

Start a batch only when the user asks to implement or queue agreed items, such as "queue this" or "do the next three agreed items", or when collect brings in agreed items marked `now`. Start ready items from the batch in queue order, up to N at once, and start more as items are integrated and their dependents become ready.

Give each item its own background agent, started from the tip of the user's branch, with its own worktree and build directory when the tools allow. When the project documents how to seed a new worktree's build directory, such as by copying the main checkout's, seed it that way, or tell the agent to, before its first build. Otherwise the build starts empty. A chain of dependent items may go to one agent in order. Pass the agreed decisions themselves, not only a pointer to the queue, and the hash of the tip of the user's branch as the base commit. Tell each agent to:

- Start by moving the worktree's own branch to the base commit, such as with `git reset --hard <commit>`, because the worktree may start elsewhere. Commit on that branch rather than creating another, so it is the only branch to integrate and delete.
- Use [implement](../../delivery/implement/SKILL.md) for each item, with one commit each, and run the project's required checks.
- Leave the queue file to the main agent.
- Keep shell calls simple enough for the tools to verify that they stay inside the worktree. Run them from the worktree root with paths relative to it, and start none with `cd`. Run each Git command alone, without `-C`, `;`, `&&`, pipes, or `$?`. Run other commands that change files, such as `mkdir` or `cp`, one per call, without brace expansion or shell variables. Create and edit files with the file-editing tools, not through shell heredocs such as `cat > file <<'EOF'` or `python3 - <<'EOF'`, `sed -i`, or redirection. For a mechanical edit across many files, write a script with those tools and run it as one plain command.
- Make routine choices that follow from the decisions and project conventions, and list every choice the decision did not settle.
- Stop at an item that needs a choice the user would make, such as a name, user-visible behavior, an interface, or scope. Keep the commits for earlier items, and report the question.

Checks that need a resource only one run can use, such as a GPU, a display, a fixed port, or a shared build directory, must not overlap. When several implementers run, tell them to skip those checks and name them in their report. The main agent runs them during integration. While any implementer runs, the main agent avoids those checks too.

If background agents are unavailable, say so and implement the batch in the foreground. If they cannot run concurrently, run them one at a time.

While a batch runs, keep discussing the next items and adding agreed ones to the queue.

## Integrate and report

Integrate finished items one at a time, in dependency order. Read each commit's diff against its agreed decision. Use [review-code](../../delivery/review-code/SKILL.md) when a commit goes beyond its decision or the implementer reports a finding it did not resolve. Bring the commits onto the user's branch following the user's integration rules. Rerun the required checks if integration changed the commits, and run any checks the implementer skipped. Update the queue, remove the worktree, delete the implementer's branch, and start items that became ready.

A conflict or failing check between items run in parallel means their footprints were misjudged. Record the dependency, and report the miss so later estimates improve.

Report for each item what changed, its commit, and the checks and their results. List every choice the implementer made beyond the agreed decision, or state that there were none. Raise any blocking question in the discussion.

Follow the user's and the project's branch and commit conventions. Merge only when the user asks. When the queue is done, finish the plan file as the project's conventions say. Otherwise move lasting decisions into the permanent docs, commit the plan file in its final state so the queue stays in history, and delete it in the next commit.
