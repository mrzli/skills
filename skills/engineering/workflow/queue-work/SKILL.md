---
name: queue-work
description: Keep discussing upcoming work items with the user while background agents implement the agreed ones in parallel, in dependency order. Use by default to implement agreed items during an ongoing discussion, and when the user asks to work through several agreed items or a whole backlog, queue work, or do it in the background.
argument-hint: "[N]"
---

Let the user keep deciding the next work items while the items already agreed are implemented in the background. The user decides what is agreed and when a batch starts. Discussion can run ahead of implementation.

Run up to N ready items at once, or 4 when N is not given. The user can change N during the session.

## Keep a queue

Keep the queue in a temporary plan file that follows the project's conventions for plans, or in `.scratch/delivery/<slug>.md` if the project has none. If that location is ignored by Git, choose a tracked one, since the final state is committed. For each item, record:

- Its number in the queue, as the user's rules for IDs say for plans. Without such rules, number items in the order they are added.
- The agreed decision, with exact names, values, and choices, so an implementer can act without the conversation, including, for a performance item, the metric, workload, and stop condition.
- Its footprint: the files and areas it is expected to touch, estimated from the decision and a search of the whole repository, including docs and comments, for the names and forms it changes.
- The earlier items it depends on.
- Its status: agreed, in progress, integrated, or blocked.
- Its commits, once integrated.
- Its times, on one line: when it started, when it was integrated, and the time between them. Record the implementer's run time and the integration's time separately when the tools report them, such as an agent's reported run time. These measured times are what later estimates of the remaining items are based on.
- Its measurements, on one line: the implementer's model, the findings of its review by severity (blocking, major, minor, nit), how many fix rounds they took and whether a fix escalated to the most capable model, whether the implementer's first run of the required checks passed, and the implementer's cost or tokens when the tools report them. Across many items, these show whether a cheaper implementer model holds up against items run on the most capable one.
- Its source ID, when it came from a fork's note through `collect`, such as `Claude-1/A1a`.

Make an item depend on an earlier item that is not yet integrated when it builds on that item's result, when their footprints overlap, or when either changes something many files rely on, such as a specification, a shared interface, or the build configuration. When unsure, add the dependency. An item is ready when the user has agreed to it and its dependencies are integrated. Update the dependencies whenever an item is added or changed.

Add an item only when the user has agreed to it, as the user's rules for approval say. Without such rules, a question is not approval, and approving one item does not approve others. An item marked `now` in a note taken in with `collect` is agreed, because the user approved it in the fork. When later discussion changes an item that is not yet implemented, update its decision. When it changes an item already in progress or integrated, add a new item.

## Run a batch

Start a batch only when the user asks to implement or queue agreed items, such as "queue this" or "do the next three agreed items", or when `collect` brings in agreed items marked `now`. Start ready items from the batch in queue order, up to N at once, and start more as items are integrated and their dependents become ready. Record each item's start time in the queue when it starts.

Give each item its own background agent with a fresh context, not one that copies this conversation, unless it is a small change that goes to a fork, as below. Start it from the tip of the user's branch, with its own worktree and build directory when the tools allow. When the project documents how to seed a new worktree's build directory, such as by copying the main checkout's, seed it that way, or tell the agent to, before its first build. Otherwise the build starts empty. A chain of dependent items may go to one agent in order.

A small change, a few lines in one unit with no open design question, goes to a background fork of this session instead when the tools can fork, such as Claude Code's `fork` agent type. The fork already has the context, so it skips a fresh agent's start-up, which can take longer than the edit itself. Start it in its own worktree as above. It runs on this session's model and does not review its own commits, as `worktree-agent.md` says. Larger items keep fresh agents, whose independent context is worth the start-up.

When the agent tool lets the caller choose a model, start each implementer on the cheapest capable model, such as Haiku in Claude Code. Use the most capable model for bugs, performance work, and items whose decision leaves design questions open, and note the model and the reason in the item's decision. An item may name another model the same way. A chain of items runs on the most capable model any of its items needs. A fork runs on this session's model, which follows from sending the item to a fork, not from a model choice. Do not choose the model by an item's size or apparent complexity, since neither predicts where a cheaper model misses. The review model is the most capable model available, or this session's model when the tool offers no choice. Run each review of an implementer's commits on it, never on a cheaper implementer's model.

Pass each agent a brief with:

- The agreed decisions themselves, not only a pointer to the queue.
- The hash of the tip of the user's branch as the base commit.
- Whether other agents run at the same time.
- Whether the agent is a fork of this session.
- The review model, when the implementer runs on a cheaper one.
- An instruction to read [worktree-agent.md](worktree-agent.md) first and follow it, with that file's absolute path in this skill's installed directory.

Do not copy the rules of `worktree-agent.md` into the brief, so each agent reads the current version even when this session's copy of the skill is older. In the brief, do not ask for a longer report than `worktree-agent.md` sets. When you need more detail on an item, read its diff or ask its implementer.

Checks that need a resource only one run can use, such as a GPU, a display, a fixed port, or a shared build directory, must not overlap. When several implementers run, they skip those checks and name them in their report, as `worktree-agent.md` says. The main agent runs them once no implementer runs, and records in the queue which integrated items still await them. Run them at the latest before the user's branch goes into the main branch.

If background agents are unavailable, say so and implement the batch in the foreground, choosing the skill per item as `worktree-agent.md` says. If they cannot run concurrently, run them one at a time.

While a batch runs, keep discussing the next items and adding agreed ones to the queue. When an item runs past about twice its estimate, or the user asks how long is left, check its agent's actual state, such as its commits, its worktree's status, and its checks' log, and report it. Past about twice its estimate, report that state rather than a new estimate.

## Integrate and report

Integrate finished items one at a time, in dependency order. Read each item's diff against its agreed decision. Decide whether to review it with `review-code`:

- Use `review-code` unless the implementer reports that a fresh agent on the review model reviewed its commits. You did not write an item a fresh background agent implemented, so your review of it is independent.
- Always review a fork's commits with `review-code` on the review model. A fork shares this session's context, so `review-code` runs the review in a fresh agent.
- Also use it when an item's commits go beyond its decision or the implementer reports a finding it did not resolve, other than a blocking or major finding it left for the more capable model as `worktree-agent.md` says when its brief names a review model.
- An item you implemented in the foreground was already reviewed through `implement`, so do not review it again unless that review was a self-review.

Grade each review's findings on `review-code`'s severity scale, or have its reviewer grade them. Design findings go to the user as recommended changes, as `review-code` says. Without a model choice, every fix runs on the session's model. Otherwise, fix the findings of your review, and those the implementer left unresolved, by their severity:

- Give minor findings and nits to an agent on the implementer's model, such as the implementer resumed with them.
- Run the fix of a blocking or major finding on the most capable model. If a blocking or major finding remains after that fix and the implementer ran on a cheaper model, have the most capable model redo the item from its base commit. Otherwise, report the remaining finding to the user.

Review each fix on the review model as the user's rules for Git and checks say. Without such rules, review every fix. Always review the fix of a blocking or major finding, to decide whether the item must be redone.

Take an implementer's commits from its branch in Git, never from a hash in its report, since a reported hash may be wrong. Bring them onto the user's branch as the user's rules for Git and checks say. Without such rules, fast-forward, rebasing onto the branch tip first if it moved, and rerun the required checks if rebasing changed the commits. Record the checks it skipped for a shared resource in the queue, to run as the rule on shared-resource checks under "Run a batch" says. Run the rebase, the checks it reruns, any other checks it skipped, and the fast-forward as one background command, so the user can keep writing while they run, and report when it ends. If it stops on a conflict or a failing check, handle that in the foreground as the rules above say, then run the rest in the background again. Update the queue, including the item's times and measurements, remove the worktree, delete the implementer's branch with `git branch -d`, and start items that became ready.

A conflict or failing check between items run in parallel means their footprints were misjudged. Record the dependency, and report the miss so later footprint estimates improve.

Start each item's report with its questions and the choices to ask about, then what changed, its commits, and the checks and their results. Report and judge the choices the implementer made beyond the agreed decision as the user's rules for approval say. Without such rules, list every one, and recommend changing any that `review-code` would report as a design finding. State when there were none. Raise any blocking question in the discussion.

Follow the user's and the project's rules for branches and commits. Without such rules, start from a branch other than the main branch, and bring the user's branch into the main branch only when the user asks. Run that merge and the checks it reruns as a background command too.

## Finish the queue

When the queue is done, finish the plan file as the project's conventions say. Without such conventions, record each item's final status and move lasting decisions into the permanent docs. Commit the move of lasting decisions into the permanent docs on its own first, after the checks the project requires for it. Stage only changes that belong with removing the queue, such as a closed backlog item, and run the checks the project requires for them. Then run [finish-queue.sh](scripts/finish-queue.sh) with the plan file's path. It commits the plan file alone, so the queue stays in history, and skips that commit when the file has no changes. It then deletes the file in a second commit together with everything else staged. Pass `--record-message` and `--remove-message` when the project's commit conventions call for messages other than the ones it derives from the file name, and `--trailer` for each trailer the commits need. Check the files it lists for each commit. If a commit fails, fix the cause and rerun the same command.
