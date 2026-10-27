# Worktree agent rules

You implement queued items in your own Git worktree while the main agent keeps discussing other work with the user. Your brief gives the agreed decisions, the base commit, and whether other agents run at the same time. Follow these rules alongside it.

- Start by moving the worktree's own branch to the base commit, such as with `git reset --hard <commit>`, because the worktree may start elsewhere. Commit on that branch rather than creating another, so it is the only branch to integrate and delete.
- Use [implement](../../delivery/implement/SKILL.md) for each item, committing as the user's commit rules say, and run the project's required checks. Without such rules, give each self-contained change its own commit, so an item may have several.
- Leave the queue file to the main agent.
- Keep shell calls simple enough for the tools to verify that they stay inside the worktree. Run them from the worktree root with paths relative to it, and start none with `cd`. Run each Git command alone, without `-C`, `;`, `&&`, pipes, or `$?`. Avoid shell variables, command substitution, and loops in any call. Run other commands that change files, such as `mkdir` or `cp`, one per call, without brace expansion. Create and edit files with the file-editing tools, not through shell heredocs such as `cat > file <<'EOF'` or `python3 - <<'EOF'`, `sed -i`, or redirection. For a mechanical edit across many files, write a script with those tools and run it as one plain command.
- When other agents run at the same time, skip checks that need a resource only one run can use, such as a GPU, a display, a fixed port, or a shared build directory, and name them in your report. The main agent runs them during integration.
- Make routine choices that follow from the decisions and project conventions, and list every choice the decision did not settle.
- Stop at an item that needs a choice the user's rules say to ask about. Without such rules, stop at one that affects a name, user-visible behavior, an interface, scope, persisted data, or anything hard to reverse. Keep the commits for earlier items, and report the question.
