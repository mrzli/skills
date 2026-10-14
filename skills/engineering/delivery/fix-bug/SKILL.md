---
name: fix-bug
description: Diagnose unexpected software behavior, repair its cause, and verify the fix. Use for a reported failure or regression when the user wants it fixed, rather than only investigated.
---

Carry the reported problem through diagnosis, repair, verification, and review. Respect a narrower request for diagnosis only by returning findings before editing production code.

## Establish the failure

Read the report, relevant instructions, code, tests, and available logs. Establish expected versus actual behavior, affected inputs and environment, and recent changes where relevant. Inspect existing working-tree changes before making your own.

Build the smallest useful reproduction or check that detects the reported symptom. Confirm that it fails for the relevant reason, rather than because of unrelated setup problems. Use an existing test, a CLI or API invocation, a browser interaction, or a focused harness as appropriate. Prefer a fast, repeatable signal, but do not demand perfect minimization before useful investigation can proceed.

For intermittent failures, capture the conditions and failure rate over repeated trials. For performance regressions, establish a comparable baseline and workload, and vet measurements with [optimize's measurement checks](../optimize/references/measurement.md). Use [optimize](../optimize/SKILL.md) instead when the goal is improving performance rather than restoring it. Keep captured evidence relevant and exclude secrets from shared logs and artifacts.

## Diagnose before repairing

Trace the failing path and form explanations with testable predictions. Use targeted inspection, instrumentation, experiments, or history to distinguish plausible causes. Change one relevant variable at a time when testing a hypothesis and update the explanation when evidence disagrees. When evidence refutes a hypothesis, revert the changes it motivated.

If reproduction is unavailable, continue useful static analysis or log inspection, but distinguish a suspected cause from a confirmed one. Identify the specific access, input, or evidence needed to verify it. Do not present a speculative edit as a proven repair or modify a live environment without authorization.

## Repair and verify

Use [implement](../implement/SKILL.md) for the bounded repair, carrying forward the cause, expected behavior, reproduction, and constraints. Correct the cause rather than merely suppressing the symptom. Include other affected paths when they share that cause and remain within scope.

Turn the reproduction into regression coverage where practical. Establish that the check detects the original failure and passes after the repair. Rerun the original scenario as well as relevant neighboring behavior and project checks, using the project's verification skill when one exists. For intermittent or performance problems, compare equivalent trials and report the limits of the evidence.

Remove temporary instrumentation you added or retain it only when it has an explicit ongoing purpose. Preserve useful reproduction artifacts in the project's test or scratch conventions and keep unrelated user work intact.

Complete the implementation review and address its findings without duplicating a review already performed by `implement`. When finding the cause required a deep investigation, propose a cheap, always-present signal that would have shown it at first look, such as a log line, an assertion, or a diagnostic.

Report the cause and evidence, the repair, verification results, and any remaining uncertainty. Completion requires evidence that the reported behavior is corrected. Otherwise state the unresolved verification or blocker.
