# Improving teach

Remaining proposals from our discussion. Remove items once implemented in `teach`. Keep the skill simple and refine it through use. These notes do not authorize implementing every proposal.

## Unfinished sections

1. **Process:** Define progression, review, workspace selection on resumption, and completion checks. The remaining flow is outlined below.
2. **Documents:** Specify how numbered lesson and record filenames are assigned.
3. **Source use:** Explicitly use reliable resources to prepare lessons.
4. **Interaction:** Answer direct questions directly. Let the teacher suggest lessons, practice, or review while the user can redirect or skip activities. Avoid making every response a quiz.

## Learning flow to add

The existing workspace setup and basic teaching loop need these additions:

1. Use the lesson outcome to guide examples and practice. Decide whether to clarify, practice more, or move on based on the user's response.
2. Revisit relevant earlier material when resuming, when a lesson depends on it, or when a misunderstanding appears.
3. Locate the matching workspace in a new session. Ask which workspace only when the match is unclear.
4. Periodically assess the mission's success conditions. Suggest completion when the user demonstrates the intended outcomes, or revise the direction with them.

Proposed relationship: one workspace supports multiple lessons. A lesson may include practice and review, span sessions, or share a session with other lessons. Define these terms in the skill if useful.

## Open decisions

1. Decide how HTML exercise results reach the learning records or progress file.
2. Clarify whether lesson independence means no prerequisite knowledge or only no need to open earlier lesson files. The prerequisite map must respect that choice.
3. When revising the protected TODO section, reconcile `MISSION.md` with `mission.md`, the undefined `GLOSSARY.md` with HTML reference materials, and `Status: superseded by LR-NNNN` with the record template's `status: superseded by ####`. The protected text remains unchanged.

## Sources of ideas

Matt Pocock's [teach skill](https://github.com/mattpocock/skills/blob/main/skills/productivity/teach/SKILL.md) informed lesson outcomes, recall, reliable sources, learning records, HTML lessons, references, and shared assets. His [learning-record format](https://github.com/mattpocock/skills/blob/main/skills/productivity/teach/LEARNING-RECORD-FORMAT.md) distinguishes demonstrated learning from exposure and routine activity logs.

The explicit learning map, resume checkpoint, and flexible artifact creation were our proposed adaptations. The immediate use case is learning how skills support software development, beginning with the overall process.
