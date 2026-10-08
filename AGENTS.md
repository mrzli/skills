# Skill changes

When repository-local and user-installed skills share a name, use the repository-local copy under `.agents/skills/`. When testing a skill, report the resolved `SKILL.md` path.

After every skill change, including additions, edits, renames, and removals:

1. Run the repository-local [tidy-docs](skills/docs/tidy-docs/SKILL.md) skill with the entire repository as its scope, including documentation in hidden directories. Treat its cleanup edits as part of the same change. Do not invoke it recursively for its own edits.
2. Run `bash scripts/sync-skills.sh` from the repository root to synchronize discovery links in `.agents/skills` and `.claude/skills`.
3. Add or update routing cases for the changed skills, following [maintain-skills](skills/engineering/workflow/maintain-skills/SKILL.md). Run them once the user has installed the changes.
