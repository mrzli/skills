---
name: writing-skills
description: Use when writing, editing, or reviewing agent skills.
---

Read and apply [writing-text](../writing-text/SKILL.md) to the target document.

Make the description clear about when to use the skill. In the body, define the intended outcome and how the agent can tell it has done enough. For exploratory work, a useful next step or an explicitly deferred decision may be enough.

Include the steps and constraints needed to guide behavior. Leave routine choices to the agent, and prescribe a fixed sequence or format only when it serves the task. Preserve existing invocation settings unless changing them is part of the request.

Keep shared guidance in one authoritative place and reference it instead of repeating it. Move substantial guidance for optional cases into supporting files, with clear instructions for when to read them. Keep simple skills self-contained.

Put steps that need no judgment, such as parsing transcripts or a fixed sequence of commands, into a script in the skill's `scripts/` directory, as `warmup` does with `scripts/last-session.sh`. Say in the skill when to run it and what the agent decides from its output. When a second skill needs the same script, move it to `skills/shared/scripts/`, and give each skill that uses it a relative symbolic link in its own `scripts/` directory, such as `scripts/agent-joins.sh` pointing to `../../../shared/scripts/agent-joins.sh`. Refer to the script by that local path in the skill's text. Until then, keep a script in its own skill. Skills are installed as links to their folders, side by side, and agents tend to resolve `..` in a skill's paths as text, from the installed link's location. A path to another skill, such as `../yield/SKILL.md`, still works because that skill is installed beside it, but a path to anything else outside the skill's folder, such as `../../shared/`, does not. A symbolic link inside the skill's folder resolves from the real folder. A script that calls another script must first find its own real location, such as with `realpath` or `os.path.realpath(__file__)`, because `cd` and some path functions resolve `..` from the link's location.

