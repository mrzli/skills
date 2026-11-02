---
name: writing-skills
description: Use when writing, editing, or reviewing agent skills.
---

Read and apply [writing-text](../writing-text/SKILL.md) to the target document.

Make the description clear about when to use the skill. In the body, define the intended outcome and how the agent can tell it has done enough. For exploratory work, a useful next step or an explicitly deferred decision may be enough.

Include the steps and constraints needed to guide behavior. Leave routine choices to the agent, and prescribe a fixed sequence or format only when it serves the task. Preserve existing invocation settings unless changing them is part of the request.

Keep shared guidance in one authoritative place and reference it instead of repeating it. When a skill runs another skill for part of its work, do not repeat that skill's fallbacks for that part. Move substantial guidance for optional cases into supporting files, with clear instructions for when to read them. Keep simple skills self-contained.

When the user's own agent instructions state a rule the skill depends on, refer to it, such as "as the user's rules for approval say", instead of copying it. Add a one-line fallback for when no such rule exists. Do not contradict those instructions, and do not name their file, so the skill works without them. Check where each rule belongs. When a rule must apply whatever the agent is doing, propose it for the user's instructions instead of putting it only in the skill. When a rule in the user's instructions matters only within one skill, propose moving it into that skill.

Put steps that need no judgment, such as parsing transcripts or a fixed sequence of commands, into a script in the skill's `scripts/` directory, as `warmup` does with `scripts/last-session.sh`. Say in the skill when to run it and what the agent decides from its output.

Keep a script or a reference file in its own skill until a second skill needs it. Then move a script to `skills/shared/scripts/` and a reference file to `skills/shared/references/`. Give each skill that uses it a relative symbolic link in its own `scripts/` or `references/` directory, such as `scripts/agent-joins.sh` pointing to `../../../shared/scripts/agent-joins.sh`, and refer to the file by that local path in the skill's text.

Skills are installed as links to their folders, side by side, and agents tend to resolve `..` in a skill's paths as text, from the installed link's location. A path to another skill, such as `../yield/SKILL.md`, still works because that skill is installed beside it. A path to anything else outside the skill's folder, such as `../../shared/`, does not. A symbolic link inside the skill's folder resolves from the real folder. A script that calls another script must first find its own real location, such as with `realpath` or `os.path.realpath(__file__)`, because `cd` and some path functions resolve `..` from the link's location.
