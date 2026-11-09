---
name: writing-skills
description: Use when writing, editing, or reviewing agent skills.
---

Read and apply the `writing-text` skill to the target document.

Make the description clear about when to use the skill. In the body, define the intended outcome and how the agent can tell it has done enough. For exploratory work, a useful next step or an explicitly deferred decision may be enough.

Include the steps and constraints needed to guide behavior. Leave routine choices to the agent, and prescribe a fixed sequence or format only when it serves the task. Preserve existing invocation settings unless changing them is part of the request. Set them for every agent the collection supports, such as `disable-model-invocation` in the frontmatter and `allow_implicit_invocation` in `agents/openai.yaml`, and keep them in agreement.

Keep shared guidance in one authoritative place and reference it instead of repeating it. Move substantial guidance for optional cases into supporting files, with clear instructions for when to read them. Keep simple skills self-contained.

When the user's own agent instructions state a rule the skill depends on, refer to it, such as "as the user's rules for approval say", instead of copying it. Add a one-line fallback for when no such rule exists. When a skill runs another skill for part of its work, do not repeat that skill's fallbacks for that part. Do not contradict those instructions, and do not name their file, so the skill works without them.

Check where each rule belongs:

- When a rule must apply whatever the agent is doing, propose it for the user's instructions instead of putting it only in the skill.
- When a rule in the user's instructions matters only within one skill, propose moving it into that skill.

Put steps that need no judgment, such as parsing transcripts or a fixed sequence of commands, into a script in the skill's `scripts/` directory, as `warmup` does with `scripts/last-session.sh`. Say in the skill when to run it and what the agent decides from its output.

Keep a script or a reference file in its own skill until a second skill needs it. Then move a script to `skills/shared/scripts/` and a reference file to `skills/shared/references/`. Give each skill that uses it a relative symbolic link in its own `scripts/` or `references/` directory, such as `scripts/agent-joins.sh` pointing to `../../../shared/scripts/agent-joins.sh`, and refer to the file by that local path in the skill's text.

Skills are installed as links to their folders, side by side, and agents resolve `..` in a skill's paths as text, from the installed link's location. A path that leaves the skill's category folder, such as `../../shared/`, therefore does not resolve, and a path to a skill in the same category breaks once either skill moves. Refer to another skill by its name instead, such as `yield` or the "Progress only" view of the `recap` skill. Agents find installed skills by name, and the name stays valid when a skill moves to another category folder. Write "the `glossary` skill" rather than the bare name where the name could be read as a command, a file, or an ordinary word. Refer to files in the skill's own folder by a relative path, such as `scripts/last-session.sh`.

A symbolic link inside the skill's folder resolves from the real folder. A script that calls another script must first find its own real location, such as with `realpath` or `os.path.realpath(__file__)`, because `cd` and some path functions resolve `..` from the link's location.
