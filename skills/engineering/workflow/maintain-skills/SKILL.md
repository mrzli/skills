---
name: maintain-skills
description: Review a skill collection for useful additions, improvements, overlap, and retirement, including names, descriptions, invocation settings, usage, routing tests, and comparison with external skill repositories. Use for repertoire reviews or collection-level problems. Use improve-workflow to diagnose friction in completed work.
---

Keep the collection useful for the user's actual activities. Review the requested collection or subset and recommend evidence-backed changes. A review produces recommendations. Apply changes when already authorized.

## Establish the evidence

Read the relevant skill descriptions and bodies, collection conventions, prior reviews, and available examples of use. Identify the user's recurring activities, missing support, confusing choices, and maintenance burden. When called from another workflow, reuse its findings and limit the review to the affected responsibilities.

Distinguish lack of use from lack of opportunity. If relevant work occurred, determine whether a skill was undiscoverable, deliberately avoided, or unhelpful. Do not infer usage from installation or invent usage counts when records are unavailable. Rare but valuable activities can justify retaining a skill.

Check each skill's name, description, and invocation settings. The name should match the skill's current responsibility. The description should state when to use the skill in words users actually say. Invocation settings should match for every agent the collection supports, such as `disable-model-invocation` for Claude Code and `allow_implicit_invocation` in `agents/openai.yaml` for Codex. Let the agent load a skill implicitly when it can recognize the situation from the request. Keep a skill user-invoked when starting it is the user's decision.

When local transcripts are available, run [skill-usage.sh](scripts/skill-usage.sh) on the collection root, excluding the collection's own repository with `--exclude-cwd`. It counts sessions that invoked or read each skill in Claude Code and Codex transcripts. Save its output in the maintenance record, because transcripts can expire. Counts show recorded use, not opportunity.

## Explore sources

Use the repositories and collection subsets named by the user. Otherwise use [sources.md](references/sources.md). Keep that list extensible as the user adds sources. Record the last reviewed revision or date and inspected scope in the maintenance record, so later reviews can resume without treating a partial review as complete.

For external comparison, inspect current upstream skill instructions and required companions. Narrow candidates by relevance before reading in depth. On repeat reviews, prioritize changes since the recorded revision. Record what was actually inspected and any access gaps. An unavailable source does not prevent reviewing the local collection.

Compare candidates by trigger, outcome, procedure, dependencies, and stopping point. Shared vocabulary or steps alone do not establish redundancy. Consider whether a coordinator can reuse existing skills, and whether a small local improvement would deliver the candidate's benefit. Account for required tools, maintenance cost, and licensing when adapting external material.

## Choose changes

Use these decisions as appropriate:

- Keep a skill with a distinct useful role, even if rarely needed.
- Improve useful skills whose triggers, instructions, or outputs cause demonstrated problems.
- Add a skill for a relevant unmet need when it contributes a reusable procedure beyond an ordinary prompt.
- Merge skills when their situations and outcomes substantially coincide and separation causes confusion.
- Retire a skill when its need has disappeared, another skill fully covers it, or its costs outweigh its value. Propose retirement for a skill that saved usage records show unused for several months, unless reviewed work shows a missed opportunity or the user expects its activity to recur. The user decides.
- Trial a plausible addition or change when evidence is insufficient. Name a representative task and the signal for keeping, revising, or reverting it.

For each recommendation, give the evidence, benefit, overlap or replacement implications, and evaluation method. Prioritize a small useful set. Keeping the collection unchanged is valid. Distinguish observed problems from hypotheses and avoid treating popularity or upstream changes as a reason to install or overwrite local skills.

## Apply and evaluate

For authorized changes, use [writing-skills](../../../docs/writing-skills/SKILL.md). Preserve useful local adaptations. Update affected references, catalogue entries, and discovery links using repository conventions. Check callers before merging or retiring skills. Keep retired content recoverable through version control or the existing archive convention.

Validate skill structure and links, check routing against representative requests, and exercise changed mechanics where applicable. Separate these checks from evidence of improved outcomes in later use.

To check routing, keep realistic requests that do not name a skill, with the skills that should load, in the collection's routing cases file, or `.scratch/skills/routing-cases.tsv` if none exists. Include near-misses that should route elsewhere. [routing-test.sh](scripts/routing-test.sh) runs each request in a fresh session that cannot edit files, in a temporary worktree, and reports which skills actually loaded. It uses the skill copies installed for the agent, so test changed skills after they are installed. Each case costs a full agent run. After skills change and are installed, run the cases for the changed skills, and add cases for new skills. Run the full file only when the user asks. Treat a skill as unavailable rather than missed when the installed copy lacks it.

Save substantial reviews in the existing maintenance record or `.scratch/skills/<descriptive-slug>.md`, including source revisions, decisions, evidence gaps, and follow-up criteria. Reuse that record on later reviews. Finish with recommendations or applied changes, validation, and the next evaluation point. Do not schedule recurring reviews unless requested.
