# Skill changes

When repository-local and user-installed skills share a name, use the repository-local copy under `.agents/skills/`. When testing a skill, report the resolved `SKILL.md` path.

After every skill change, including additions, edits, renames, and removals, run `bash scripts/sync-skills.sh` from the repository root to synchronize discovery links in `.agents/skills` and `.claude/skills`.
