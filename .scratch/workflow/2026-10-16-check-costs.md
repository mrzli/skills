# Cheaper checks

Source: qt-market-chart's backlog item "Which checks run when" (branch `backlog-check-costs`). During a `queue-work` batch of renames with six parallel implementers, checks took 40.6 of 86 implementer minutes (47%).

## Causes and where each was fixed

1. Format and lint ran after every change, Markdown included. Fixed in the project's `AGENTS.md`, "Required checks", by kind of change.
2. The agent ran functional checks for documentation changes. Fixed in the project's rule, which is now explicit.
3. `clang-tidy` analyzed every file on every run. Fixed in the project's lint script with a cache.
4. Each implementer's worktree started with an empty build directory. Skills: `queue-work` now seeds it when the project documents how. The copy procedure stays in the project, because its safety depends on the build (embedded paths, touching files that differ, no build running in the source checkout).
5. After a failure, the whole set ran again. Skills: `implement` now reruns only the failed check, then the change's required checks once.

For new projects, `writing-agents` asks for required checks by kind of change and, where it applies, how to seed a worktree's build. Nothing was added to `start-project` or the global `AGENTS.md`.

## Evaluation

Next `queue-work` batch with parallel implementers in a project that documents build seeding:

- Keep if implementers seed their build directory and the share of time in checks drops well below 47%.
- Revise if implementers skip seeding or rerun the full set after a single failed check.
- Revise if a seeded build produces a stale or wrong result.

Also check whether qt-market-chart's `AGENTS.md` gains a seeding instruction, since `queue-work` only seeds when the project documents it.
