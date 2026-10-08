---
name: optimize
description: Improve a measured performance metric, such as latency, frame time, throughput, or memory, through measured keep-or-revert attempts. Use for slowness or resource use the user wants reduced, or a performance target to reach.
---

Move one metric toward a target with evidence for every kept change. A correctness bug that happens to be slow belongs to [fix-bug](../fix-bug/SKILL.md).

## Define the target

Read project instructions and the code on the slow path. Name the metric, the direction that counts as better, and a workload that reproduces the user's complaint. Use realistic data size, state, and concurrency. If no workload reproduces the complaint, fix the reproduction before optimizing.

Agree on a stop condition that pairs a target with a minimum number of attempts, so an early lucky result does not end the work. Use the user's numbers when given. Otherwise propose them.

## Build the measurement

Create one repeatable command that runs the workload and prints the metric. Show that it separates the slow case from an easier case, then freeze it for the rest of the work. Vet it with [measurement.md](references/measurement.md) before relying on its numbers.

Record the baseline and a passing run of the checks that must keep passing. Locate where the time or resource goes with a profiler or counters, in runs you do not report, and map the hot path to source before forming hypotheses.

## Attempt, measure, keep or revert

Make one change per attempt, based on a hypothesis that names a specific mechanism. Try ideas in this order, cheapest first:

1. Avoid work whose result nothing uses.
2. Avoid repeating work, for example by caching.
3. Do less of it.
4. Do it later, or off the critical path.
5. Do it concurrently.
6. Make it cheaper.

Measure each attempt with the frozen command and run the checks. Keep a change only when the metric moves past run-to-run variation and the checks pass. Otherwise revert it completely. Never stack untested changes. Correctness and simplicity outrank the metric, so revert a win that breaks behavior, and keep a simplification that holds the number.

Commit each kept change separately, following the user's and project's conventions. Log every attempt, kept or reverted, in `.scratch/perf/<slug>.md` with the hypothesis, before and after values, and verdict.

On a stall, try a different category of idea or reread the hot path before concluding. Stop when the stop condition is met or the remaining ideas cost more than they would save. Do not relax the target to meet it.

## Report

Give the metric and target, baseline and final values with the change, the number of attempts kept and reverted, each kept change in one line, the log path, and the most promising untried idea.
