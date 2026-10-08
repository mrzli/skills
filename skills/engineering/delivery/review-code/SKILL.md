---
name: review-code
description: Review a code change for correctness, alignment with the request, and project conventions. Use for a diff, commit, branch, pull request, or uncommitted work, including review during implementation.
---

Produce actionable findings about the requested change. A standalone review reports findings. Edits require a request to fix them or an enclosing implementation task that already authorizes corrections.

## Establish the review scope

Use the change scope supplied by the user or calling workflow. Otherwise, infer it from the active task and working tree. For uncommitted work, include staged changes, unstaged changes, and relevant untracked files. For a branch or pull request, identify the intended base and comparison point. Ask only if materially different scopes remain plausible.

State the scope being reviewed. Validate any supplied revision before relying on its diff. Keep committed changes and local edits distinguishable. Inspect the file versions actually under review. If there is no change in scope, report that rather than silently expanding the review.

Read applicable project instructions and the originating request, specification, or task. A clear conversation request can supply the requirements. If intended behavior is unavailable, review what can be established from the code and project context, and identify the requirements you could not assess.

## Examine the change

Read the full diff, new files, and enough surrounding code, callers, and tests to understand the effect. Follow affected interfaces beyond changed lines when needed to check compatibility and regressions. Concentrate on problems introduced or exposed by this change. Distinguish pre-existing issues.

Check both:

- **Intended behavior:** requirements and acceptance criteria are met, relevant failure cases are handled, existing behavior remains compatible where required, and changes stay within scope.
- **Engineering quality:** correctness, project conventions, maintainability, and meaningful verification. Examine security, data integrity, performance, and operational concerns where the changed behavior makes them relevant.

Treat complexity, duplication, and naming as findings when they have a concrete cost or violate an applicable convention. Separate those judgments from demonstrated defects. Prefer useful evidence over stylistic preferences or a fixed catalogue of code smells.

Check that tests exercise the intended behavior and could detect relevant failures. A test that would still pass if the code under test returned nothing does not verify behavior. Read supplied verification results and run focused checks when they can resolve a concern. State which checks you ran, which results were supplied by others, and what remains unverified. Passing tests alone do not establish that the requirements are met.

Investigate suspected problems before reporting them. Trace a realistic failing case, reproduce it where practical, or explain the code path and evidence. When evidence is incomplete, make the uncertainty explicit rather than presenting a guess as a defect. For a risky change, name the fact its safety depends on and how it was established: asserted, located in code, reasoned through, or demonstrated by running it. Look beyond symbol search for affected persisted formats, file or protocol contracts, configuration, and readers in other languages.

## Report and follow through

Present findings in priority order. For each, give the affected file and location, the triggering situation, the consequence, and the supporting evidence or requirement. Suggest a correction when useful. Keep optional improvements separate from issues that should block completion, and avoid duplicating the same underlying problem across findings.

Finish with a concise assessment of requirements coverage, blocking findings, and verification limitations. If no actionable findings remain, say so without implying that unverified behavior is proven correct. Identify a review of your own implementation as self-review.

When corrections are already authorized, address findings within scope and recheck the affected behavior and diff. Otherwise, return findings to the user or calling workflow. A follow-up review verifies the actual corrections and their consequences before marking findings resolved.
