# Improving teach

Remaining proposals from our discussion. Remove items once implemented in `teach`. Keep the skill simple and refine it through use. These notes do not authorize implementing every proposal.

## Current direction

The active [teach skill](../.agents/skills/teach/SKILL.md) creates or resumes a learning workspace in `.scratch/learn/<lesson-slug>`. It uses `MISSION.md`, `RESOURCES.md`, learning records, HTML lessons and references, shared assets, a glossary, and notes.

The [experimental design](../experimental/skills/teach/SKILL.md) adds a learning map, a progress checkpoint, and an explicit activity flow. That flow is incomplete. The remaining notes below concern this design and possible future work, not additional requirements for the active skill.

The [world-capitals workspace](learn/world-capitals/NOTES.md) now provides a practical trial: 24 lessons, shared quiz assets, references, and learning records through 0113. Its [coverage audit](learn/world-capitals/COVERAGE.md) records 195 countries and 199 tested pairs, including capital roles and government seats. Cumulative review continues, and retention across a known break remains untested. Use this experience to evaluate further structure.

## Experimental design: remaining work

1. **Process:** Fill the Choose next activity, Check completion, and Learning loop TODOs. The remaining flow is outlined below.
2. **Documents:** Specify how numbered lesson and record filenames are assigned.
3. **Interaction:** The model manages teaching and document updates. The user provides goals, attempts learning activities, and controls direction. Answer direct questions directly, ask one question at a time when needed, and avoid making every response a quiz. Clarify these roles when completing the loops.

## Learning flow to add

The entry, orientation, and direction-update steps need these remaining activity and learning-loop details:

1. Choose new learning, practice, or review from the mission, learning map, demonstrated understanding, and unresolved gaps. Use one concrete outcome to guide explanation, examples, practice, and feedback. Decide whether to clarify, practice more, or move on based on the user's response.
2. Revisit relevant earlier material when resuming, when a lesson depends on it, or when a misunderstanding appears.
3. Periodically assess the mission's success conditions. Suggest completion when the user demonstrates the intended outcomes, or revise the direction with them.

Proposed relationship: one workspace supports multiple lessons. A lesson may include practice and review, span sessions, or share a session with other lessons. Define these terms in the skill if useful.

## Open decisions

1. Decide how HTML exercise results reach the learning records or progress file. The world-capitals trial shows copyable results for the user to paste into chat, then the agent records demonstrated knowledge. It does not write browser results directly to workspace files. Decide whether to retain this approach in the experimental design.
2. Clarify whether lesson independence means no prerequisite knowledge or only no need to open earlier lesson files. The prerequisite map must respect that choice.
3. When revising the protected TODO section, reconcile `MISSION.md` with `mission.md`, the undefined `GLOSSARY.md` with HTML reference materials, and `Status: superseded by LR-NNNN` with the record template's `status: superseded by ####`. The protected text remains unchanged.

## Sources of ideas

Matt Pocock's [teach skill](https://github.com/mattpocock/skills/blob/main/skills/productivity/teach/SKILL.md) informed lesson outcomes, recall, reliable sources, learning records, HTML lessons, references, and shared assets. His [learning-record format](https://github.com/mattpocock/skills/blob/main/skills/productivity/teach/LEARNING-RECORD-FORMAT.md) distinguishes demonstrated learning from exposure and routine activity logs.

The explicit learning map, resume checkpoint, and flexible artifact creation were our proposed adaptations. The originally proposed use case was learning how skills support software development, beginning with the overall process. The current repository trial covers world capitals.
