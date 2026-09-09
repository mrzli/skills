# Improving teach

Remaining proposals from our discussion. Remove items once implemented in `teach`. Keep the skill simple and refine it through use. These notes do not authorize implementing every proposal.

## Unfinished sections

1. **Process:** Define progression, review, resume information, resumption, and completion checks. The remaining flow is outlined below.
2. **Documents:** Decide whether to add a learning map or separate progress document. Specify how numbered lesson and record filenames are assigned.
3. **Source use:** Explicitly use reliable resources to prepare lessons.
4. **Interaction:** Answer direct questions directly. Let the teacher suggest lessons, practice, or review while the user can redirect or skip activities. Avoid making every response a quiz.

## Learning flow to add

The existing workspace setup and basic teaching loop need these additions:

1. Build a provisional learning map from the mission and the user's starting knowledge. Show topics, prerequisites, and a suggested order.
2. Use the lesson outcome to guide examples and practice. Decide whether to clarify, practice more, or move on based on the user's response.
3. Save unresolved gaps, unfinished work, and the next activity in a form suitable for resuming.
4. Revisit relevant earlier material when resuming, when a lesson depends on it, or when a misunderstanding appears. Adjust the map as needed.
5. In a new session, locate the workspace, read its mission, map, and progress, and suggest where to continue. Ask which workspace only when the match is unclear.
6. Periodically assess the mission's success conditions. Suggest completion when the user demonstrates the intended outcomes, or revise the direction with them.

Proposed relationship: one workspace supports multiple lessons. A lesson may include practice and review, span sessions, or share a session with other lessons. Define these terms in the skill if useful.

## Missing document descriptions

Names and formats below are candidates, not final decisions.

1. **Learning map (`learning-map.md`):** Topics, prerequisites, lesson outcomes, and suggested order. Revise as understanding and priorities change.
2. **Progress or resume record (`progress.md`):** Current lesson and outcome, material introduced, demonstrated understanding, unresolved questions, and next activity. Save enough to resume without the previous conversation.
## Open decisions

1. Agree on a learning map before lessons, or let a small initial map develop during learning?
2. Start with learning records that include resume information, use one progress file, or keep both with distinct roles? No choice has been finalized.
3. Save progress automatically after meaningful steps, on request, or at session end? Saving during learning would support interrupted sessions.
4. Decide how HTML exercise results reach the learning records or resume information.
5. Clarify whether lesson independence means no prerequisite knowledge or only no need to open earlier lesson files. The proposed prerequisite map must respect that choice.
6. When revising the protected TODO section, reconcile `MISSION.md` with `mission.md`, the undefined `GLOSSARY.md` with HTML reference materials, and `Status: superseded by LR-NNNN` with the record template's `status: superseded by ####`. The protected text remains unchanged.
7. Resolve whether temporary resume notes belong in learning records, since the protected draft excludes routine activity logs.

## Sources of ideas

Matt Pocock's [teach skill](https://github.com/mattpocock/skills/blob/main/skills/productivity/teach/SKILL.md) informed lesson outcomes, recall, reliable sources, learning records, HTML lessons, references, and shared assets. His [learning-record format](https://github.com/mattpocock/skills/blob/main/skills/productivity/teach/LEARNING-RECORD-FORMAT.md) distinguishes demonstrated learning from exposure and routine activity logs.

The explicit learning map, resume checkpoint, and flexible artifact creation were our proposed adaptations. The immediate use case is learning how skills support software development, beginning with the overall process.
