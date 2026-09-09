# Improving teach

Remaining proposals from our discussion. Remove items once implemented in `teach`. Keep the skill simple and refine it through use. These notes do not authorize implementing every proposal.

## Unfinished sections

1. **Process:** Define lesson outcomes, progression, review, progress recording, resumption, and completion checks. The remaining flow is outlined below.
2. **Documents:** Fill the Lessons, Learning Records, and Reference Materials placeholders with their purposes, formats, and rules for creating, reading, and updating them. Decide whether to add a learning map or separate progress document.
3. **Source use:** Explicitly use reliable resources to prepare lessons.
4. **Interaction:** Answer direct questions directly. Let the teacher suggest lessons, practice, or review while the user can redirect or skip activities. Avoid making every response a quiz.

## Learning flow to add

The existing workspace setup and basic teaching loop need these additions:

1. Build a provisional learning map from the mission and the user's starting knowledge. Show topics, prerequisites, and a suggested order.
2. Choose one concrete outcome for the next lesson: something the user should be able to explain or do afterward.
3. Use the outcome to guide examples and practice. Decide whether to clarify, practice more, or move on based on the user's response.
4. Save meaningful progress, distinguishing material introduced from understanding demonstrated. Record gaps and the next activity.
5. Revisit relevant earlier material when resuming, when a lesson depends on it, or when a misunderstanding appears. Adjust the map as needed.
6. In a new session, locate the workspace, read its mission, map, and progress, and suggest where to continue. Ask which workspace only when the match is unclear.
7. Periodically assess the mission's success conditions. Suggest completion when the user demonstrates the intended outcomes, or revise the direction with them.

Proposed relationship: one workspace supports multiple lessons. A lesson may include practice and review, span sessions, or share a session with other lessons. Define these terms in the skill if useful.

## Missing document descriptions

Names and formats below are candidates, not final decisions.

1. **Learning map (`learning-map.md`):** Topics, prerequisites, lesson outcomes, and suggested order. Revise as understanding and priorities change.
2. **Progress or resume record (`progress.md`):** Current lesson and outcome, material introduced, demonstrated understanding, unresolved questions, and next activity. Save enough to resume without the previous conversation.
3. **Learning records (`learning-records/*.md`):** Capture demonstrated understanding, disclosed prior knowledge, corrected misconceptions, and mission changes that affect future teaching. They could also replace a separate progress record if they retain unresolved difficulties, unfinished work, and a next step. They may link to supporting artifacts when useful as evidence.
4. **Lessons (`lessons/*`):** Focused explanations, examples, and exercises worth retaining. Decide whether lessons require files and whether to use HTML.
5. **References (`reference/*`):** Created summaries, cheat sheets, and glossaries for lookup across lessons. Distinct from the external sources in `resources.md`.

## Open decisions

1. Recommended smallest next addition: a concrete outcome for each lesson. No new files are needed.
2. Agree on a learning map before lessons, or let a small initial map develop during learning?
3. Start with learning records that include resume information, use one progress file, or keep both with distinct roles? No choice has been finalized.
4. Save progress automatically after meaningful steps, on request, or at session end? Saving during learning would support interrupted sessions.
5. Use conversational lessons, saved HTML lessons, or choose per lesson? If HTML is used, decide how browser exercise results reach the progress record.

## Sources of ideas

Matt Pocock's [teach skill](https://github.com/mattpocock/skills/blob/main/skills/productivity/teach/SKILL.md) informed lesson outcomes, recall, reliable sources, learning records, HTML lessons, references, and shared assets. His [learning-record format](https://github.com/mattpocock/skills/blob/main/skills/productivity/teach/LEARNING-RECORD-FORMAT.md) distinguishes demonstrated learning from exposure and routine activity logs.

The explicit learning map, resume checkpoint, and flexible artifact creation were our proposed adaptations. The immediate use case is learning how skills support software development, beginning with the overall process.
