---
name: improve-workflow
description: Examine completed engineering work and improve the process based on observed friction. Use for a retrospective, recurring agent mistakes, weak verification, unnecessary handoffs, or problems with skills and tooling.
---

Find the smallest useful correction to how work is performed. Base recommendations on actual work and the instructions in effect, rather than designing an ideal process from scratch.

## Examine the evidence

Use the named session, change, or recurring problem. Default to the current work when the scope is clear. Read relevant conversation or logs, task artifacts, diffs, verification results, and the skills or project instructions that governed the work.

For historical reviews, compare incidents with the instructions and versions available at the time, later fixes, and the version currently installed. State uncertainty when the evidence cannot establish a version. Distinguish unresolved gaps from already-addressed issues, deployment gaps, and failures to follow existing guidance. An old failure alone does not justify another instruction.

Describe the observed friction and its consequence: repeated clarification, wasted investigation, missed requirements, rework, tool failures, or weak verification. Separate a one-off mistake from a recurring pattern and distinguish observed facts from explanations that still need testing.

Trace the problem to its source. Consider unclear requirements, missing information, conflicting instructions, poor activity boundaries, unavailable tools, and checks that existed but were not run. Inspect existing automation before proposing a duplicate check or new tool.

When local transcripts are available, run [repeated-steps.py](scripts/repeated-steps.py) with `python3 -I` for the project, using `--since` to limit the period. It counts the shell steps that agents repeated by hand across the project's Claude Code and Codex sessions: chains, loops, output filters, and runs of two to four steps. The script only counts. Group steps that were done in different ways, drop those already covered by the project's tooling, and propose tooling for the rest only as the user's or project's rules for proposing tooling allow. Before proposing, check the project's backlog for an earlier "not now" or "don't ask again". Save the script's output in the improvement record.

## Choose a correction

Consider clarifying or removing an instruction, improving access to evidence, changing a skill's inputs or outputs, moving a step, or automating a reliable check. Add, merge, or remove skills only when their responsibilities justify it. Retaining the current process is a valid recommendation.

When the evidence calls for reviewing skill boundaries, missing capabilities, or overlapping responsibilities across the collection, use [maintain-skills](../maintain-skills/SKILL.md). Pass the observed friction, affected skills, and existing authorization. Use its findings in the correction. Handle a small correction within one skill directly, without expanding it into a collection review.

Prefer a deterministic check for a recurring mechanical error when its maintenance cost is justified. Fix it at the highest level that works, in this order: structure that makes the mistake impossible, types, a lint whose message names the fix, a test, then documentation. Show that a new check catches a real past instance. Use guidance for decisions that require judgment. Put a correction at the narrowest appropriate level: project-specific behavior belongs in the project, while a reusable skill change should be supported by a general need.

For each proposal, state the evidence, suspected cause, change, expected benefit, cost, and how to evaluate it. Prioritize a small number of corrections. Treat broad changes based on one incident as hypotheses, and preserve useful flexibility rather than adding universal rules for every failure.

## Apply and evaluate

A retrospective request produces recommendations. If corrections are already authorized, make the scoped changes using the relevant authoring or implementation guidance. Validate the changed mechanics and check for conflicts with existing instructions. Preserve unrelated user choices and invocation settings.

Test the correction against a representative scenario where practical. Record what was tested and what still needs observation in later work. Distinguish a successfully applied edit from evidence that it improves outcomes. Define the signal that would justify retaining, revising, or reverting it.

Save substantial findings and follow-up criteria in the project's improvement record or `.scratch/workflow/<descriptive-slug>.md`. Finish with the chosen correction or recommendation, validation results, and the next evaluation point. Do not leave an active task running merely to wait for future sessions to supply evidence.
