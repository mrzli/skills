---
name: warmup
description: Help the user get back into the current project after a break, with a very short summary of where the work stopped and a few small steps to rebuild context. Use when the user returns to a project after a day or more away.
disable-model-invocation: true
---

Get the user back into the current project quickly. Read only enough to know where the work stopped, not the whole history. Make no changes.

## Find where the work stopped

Read these, stopping once the picture is clear:

- The project's plan, queue, or progress files, such as `docs/plans/` files or `.scratch/delivery/` records, and any handoff document for this project.
- The current branch, recent commits, unmerged branches, and uncommitted changes.
- The end of the previous agent session in this project. Run [last-session.sh](scripts/last-session.sh) from the project root. It prints the last messages of the most recent earlier Claude Code or Codex session, without tool output. If the current session already holds earlier work, such as when it was resumed or continued, pass `--skip 0` to print the current session instead. Check that the printed session ends with this request, so it is not a fork of the current one.

Prefer written records and the repository over the session when they disagree, and mention the mismatch.

## Summarize and give steps

Write at most five short lines: what the user was doing, where it stopped, and what is waiting on them.

Then give three to five small steps in order, from easy to slightly harder. Each step names one concrete thing to look at or do, such as a commit, a file, a check to run, or a pending decision, and says what the user will know afterward. Use the project's real names and commands. Prefer steps that are part of the real work, such as reviewing the last commit or settling the next decision, over exercises. End with the step that starts the next piece of work.

If the project has had activity in the last four weeks but its latest retrospective record from [improve-workflow](../../engineering/workflow/improve-workflow/SKILL.md) is older than that, or there is none, add one line suggesting a retrospective with `improve-workflow`.

Stop after the steps. Wait for the user to start.
