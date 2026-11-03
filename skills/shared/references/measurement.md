# Vetting a performance measurement

Check a performance number before reporting it or acting on it. Answer each question with evidence from a run, not from reading the code.

Before running, write down the claim you expect to make, such as "rendering a frame of the largest dataset takes 30% less time". Read the measurement code and note what it times and what it ignores. Check the machine's load, and interleave the sides if background work cannot be stopped.

1. **What limits it?** Name the resource or code path that bounds the result, using a profile or counters, not a guess. If a change did not move the number, the limiter explains why.
2. **Does it run like the real thing?** Measure release builds with production settings, data, and versions on every side. A debug build or default setting on one side compares configurations, not implementations.
3. **Is it physically plausible?** Compare the result with hardware limits and with the time the changed piece took. Removing a piece that takes 10% of the run can make it at most about 11% faster. A result beyond a limit measured something else.
4. **Did anything fail?** Count errors and check that outputs are correct. Failures are often faster or slower than successes.
5. **Does it reproduce?** Run each side at least five times, alternating the sides. Report the median and the range. Treat a gap smaller than the run-to-run variation as no measurable difference.
6. **Does it matter?** Report a micro result as a share of the end-to-end time the user waits on.
7. **Did the work happen inside the timed region?** Asynchronous work, such as queued GPU commands, deferred tasks, or unawaited results, can finish after the clock stops. Synchronize before stopping the timer.

Report the verdict first: faster, slower, no measurable difference, or inconclusive. Give the number with its unit, run count, range, and limiter. Call a result inconclusive when the limiter is unknown, a side ran untuned, or questions 4 and 7 were not checked.

A quick estimate the user asked for may use one run. Still check questions 4 and 7, and say it was one run.
