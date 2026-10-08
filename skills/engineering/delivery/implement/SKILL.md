---
name: implement
description: Build and verify a scoped code change from a request, specification, or task. Use when the user is ready to implement agreed behavior.
---

Deliver the requested change with verification evidence. A clear request is enough. A separate specification or ticket is optional.

## Establish scope

Read applicable project instructions, the request and referenced artifacts, and the relevant code and tests. Inspect the working tree so existing changes remain distinguishable from your work.

Identify the intended behavior, completion criteria, and how to verify them. Resolve routine implementation choices from the repository. Ask only when an unresolved decision materially affects behavior, scope, or compatibility and cannot be settled from available evidence. Continue independent work while that decision is pending. Do not add fallbacks, aliases, or deprecated paths for callers inside the repository. Update the callers instead.

For work with several steps, keep a short plan or update the supplied task artifact. If implementing one task from a larger plan, use the surrounding plan as context and keep execution within the assigned scope.

## Build and verify

Work in small, verifiable increments using the project's conventions and existing abstractions. Include documentation, configuration, and migration changes needed to make the requested behavior usable. Keep unrelated cleanup separate.

Choose checks that demonstrate observable behavior and protect affected existing behavior. For a reproducible bug, establish the failure before changing the code. Add regression coverage where practical. Use a failing test first when it provides a useful check of the change. Follow any project requirement for test-driven development.

Test through stable interfaces, with expected results derived from requirements or known examples. Avoid tests that merely repeat the implementation. Small documentation or configuration edits may need direct inspection or a focused check rather than new tests.

Run focused checks during implementation. Before completion, run the project's required checks and broader tests appropriate to the affected behavior. For changes whose correctness is not established by automated tests, inspect or exercise the relevant application behavior too.

Investigate failures and fix those caused by the change. Distinguish existing failures and environment limitations from regressions, and report what remains unverified. Passing a narrow check does not establish completion of unrelated acceptance criteria.

## Review and finish

Review the complete change, including new files, against the request and project conventions. Use `review-code` if it is available. Otherwise perform this review yourself and identify it as self-review. Supply the reviewer with the intended behavior, change scope, and verification results.

Resolve actionable findings within scope, then rerun affected checks after corrections. Record consequential findings outside scope instead of silently expanding the task.

Finish when the requested behavior is implemented, relevant verification has passed, and no known blocking review findings remain. If a blocker prevents completion, state the remaining work and the specific evidence or decision needed to proceed. For work continuing across sessions, update the existing task artifact or a concise progress note with completed work, verification, and next steps.

Report what changed, the checks performed and their results, and any remaining limitations. Follow the user's and project's instructions for commits and delivery. Invoking this skill alone does not request a commit, push, pull request, or release.
