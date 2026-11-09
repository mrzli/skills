---
name: implement
description: Build and verify a scoped code change from a request, specification, or task. Use when the user is ready to implement agreed behavior and waits for the result, such as a one-off request. For agreed items in an ongoing discussion or a whole backlog, use queue-work.
---

Deliver the requested change with verification evidence. A clear request is enough. A separate specification or ticket is optional.

## Establish scope

Read applicable project instructions, the request and referenced artifacts, and the relevant code and tests. Inspect the working tree so existing changes remain distinguishable from your work.

Identify the intended behavior, completion criteria, and how to verify them. Resolve routine implementation choices from the repository.

- When the evidence cannot settle a decision, take, list, or ask about it as the user's rules for approval say. Without such rules:
  - Ask only about decisions that affect names, user-visible behavior, interfaces, scope, compatibility, or persisted data.
  - Answer a question and wait.
  - Treat approval as covering only what was approved.
- Continue independent work while a decision is pending.
- Fix mechanical consequences of the agreed change within scope, such as stale references, uses of a name the change renamed, and documentation, instead of asking about them or reporting them as open questions. Ask or propose only when a consequence involves a choice.
- Propose changes outside the request instead of making them, except the changes the user's rules say to make on your own judgment, such as fixes in the code you change, renames, and docs, comments, or tests brought in line with the code.
- Keep compatibility as the user's rules for code design say. Without such rules, update callers inside the repository instead of adding aliases, fallbacks, or deprecated paths. Keep a compatible form only for consumers outside the repository, persisted data, or an explicit user request.

For work with several steps, keep a short plan or update the supplied task artifact. If implementing one task from a larger plan, use the surrounding plan as context and keep execution within the assigned scope.

## Build and verify

Before settling on an approach, compare it with the realistic alternatives and build the better one, as the user's rules for recommendations and designs say. Without such rules, build the better one even when it takes more effort, unless the extra effort is large compared with the gain. Work in small, verifiable increments using the project's conventions and existing abstractions. Report deviations from an agreed design instead of absorbing them silently. Include documentation, configuration, and migration changes needed to make the requested behavior usable. Keep unrelated cleanup separate, in its own commit when committing.

Choose checks that demonstrate observable behavior and protect affected existing behavior. For a reproducible bug, establish the failure before changing the code. Add regression coverage where practical. Use a failing test first when it provides a useful check of the change. Follow any project requirement for test-driven development.

Test through stable interfaces, with expected results derived from requirements or known examples. Avoid tests that merely repeat the implementation. Small documentation or configuration edits may need direct inspection or a focused check rather than new tests.

Run focused checks during implementation. Before completion, run checks as the user's rules for checks say. Without such rules, run the project's required checks for this kind of change and broader tests appropriate to the affected behavior. For changes whose correctness is not established by automated tests, inspect or exercise the relevant application behavior too. Use the project's verification skill or documented verification procedure when one exists.

Investigate failures and fix those caused by the change. After a fix, rerun checks as the user's rules for checks say. Without such rules, rerun only the failed check until it passes, then run the change's required checks once more. When a verification setup itself fails or gives implausible results, check the observation method before concluding the application is wrong. Distinguish existing failures and environment limitations from regressions, and report what remains unverified. Passing a narrow check does not establish completion of unrelated acceptance criteria.

## Review and finish

Have the complete change, including new files, reviewed against the request and project conventions with `review-code`, giving it the intended behavior, change scope, and verification results. Size the review brief as the user's rules for reviews say. Without such rules, follow what `review-code` describes for a change of this size and risk. Without `review-code`, give the same to a fresh agent to review when the tools allow, and otherwise review the change yourself and identify the result as self-review. Report whether a fresh agent reviewed the change or it was self-review.

Resolve actionable findings within scope, then rerun affected checks after corrections. Record only out-of-scope findings that the user's rules do not cover, instead of silently expanding the task.

Finish when the requested behavior is implemented, relevant verification has passed, and no known blocking review findings remain. If a blocker prevents completion, state the remaining work and the specific evidence or decision needed to proceed. For work continuing across sessions, update the existing task artifact or a concise progress note with completed work, verification, and next steps.

Put open questions first. Report what changed, your choices beyond the request as the user's rules for approval say, the checks performed and their results, and any remaining limitations. Without such rules, list every choice beyond the request. Commit as the user's and the project's rules for commits say. Without such rules, do not commit unless asked. Push, open a pull request, or release only when asked.
