# Worktree agent rules

You implement queued items in your own Git worktree while the main agent keeps discussing other work with the user. Your brief gives the agreed decisions, the base commit, and whether other agents run at the same time. Follow these rules alongside it.

- Start by moving the worktree's own branch to the base commit, such as with `git reset --hard <commit>`, because the worktree may start elsewhere. Commit on that branch rather than creating another, so it is the only branch to integrate and delete.
- Use the skill that fits each item:
  - `fix-bug` for a bug.
  - `refactor` for a restructuring that keeps behavior.
  - `optimize` for a measured performance goal.
  - `implement` for anything else.
- Where the chosen skill asks to agree with, propose to, or ask the user, such as `optimize`'s metric, workload, and stop condition or `refactor`'s scope, take the answer from your brief. If the brief does not settle it, stop at that item, keep the commits for earlier items, and report the question.
- Commit as the user's rules for commits say. Without such rules, give each self-contained change its own commit, so an item may have several.
- Run the project's required checks. After a check fails, rerun checks as `implement` says.
- Ask each reviewer to grade its findings as blocking, major, minor, or nit.
- When your brief names a review model, start every reviewing agent on it, not on your own model, and leave a blocking or major finding from that review unfixed and report it, so the main agent can have a more capable model fix it.
- Wait for long work so that each wait ends when the work does:
  - Run a long check, such as the project's full checks, in the foreground with the longest timeout the shell tool allows (600000 ms in Claude Code), rather than in the background. If it times out, rerun it in the background and wait for it as the next rule says.
  - Wait for background work, such as a review agent or a background command, with a tool that waits for it, such as Claude Code's `Monitor`, or with a single command that ends when that work ends, such as `tail --pid=<pid> -f /dev/null`. A condition loop inside `Monitor` is an exception to the shell-call rules below. Never poll with repeated shell calls that sleep for a fixed time and then check.
  - Never wait with `pgrep -f` on a pattern that appears in the waiting command itself. The pattern matches the waiting shell, so the wait never ends.
- Leave the queue file to the main agent.
- Keep shell calls simple enough for the tools to verify that they stay inside the worktree:
  - Run them from the worktree root with paths relative to it, and start none with `cd`.
  - Run each Git command alone, without `-C`, `;`, `&&`, pipes, or `$?`.
  - Avoid shell variables, command substitution, and loops in any call.
  - Run other commands that change files, such as `mkdir` or `cp`, one per call, without brace expansion.
  - Create and edit files with the file-editing tools, not through shell heredocs such as `cat > file <<'EOF'` or `python3 - <<'EOF'`, `sed -i`, or redirection.
  - For a mechanical edit across many files, write a script with the file-editing tools and run it as one plain command.
- When other agents run at the same time, skip checks that need a resource only one run can use, such as a GPU, a display, a fixed port, or a shared build directory, and name them in your report. The main agent runs them during integration.
- Make routine choices that follow from the decisions and project conventions, and leave them out of your report.

## Report

Every report stays in the main agent's context for the rest of its session, so keep yours short. Give these parts in this order, and nothing else:

1. Your commits, from `git log --oneline`, one line each.
2. Each check you ran and its result, with test totals, and whether your first run of the required checks passed. Name each check you skipped and why.
3. Your review's findings by severity (blocking, major, minor, nit), the number of fix rounds they took, and who reviewed: a fresh agent and its model, or self-review. Give each finding you left open in one line.
4. Each other choice your brief did not settle, in one line. When a choice changes something agreed, or the user's rules for approval say to ask about it first, add one sentence of reasons.
5. Your questions for the main agent or the user, one line each.

Leave out how you did the work, file paths, and notes the main agent did not ask for. It can read the diff or ask you.
