---
name: teach
description: Teach the user a new skill or concept, within this workspace.
argument-hint: "What would you like to learn about?"
---

Teach the topic over multiple sessions, preserving the user's learning state in a workspace.

## Teaching Workspace

Create a learning workspace in `.scratch/learn/<lesson-slug>`, or resume the existing workspace for that topic.

All learning document paths below are relative to that workspace. Format links refer to files beside this skill.

- `MISSION.md`: The user's reason for learning, which grounds all teaching. Use [MISSION-FORMAT.md](./MISSION-FORMAT.md).
- `RESOURCES.md`: Trusted sources and communities for knowledge and wisdom. Use [RESOURCES-FORMAT.md](./RESOURCES-FORMAT.md).
- `./learning-records/*.md`: Non-obvious lessons, key insights, and prior knowledge that guide future sessions. Use [LEARNING-RECORD-FORMAT.md](./LEARNING-RECORD-FORMAT.md) for content and sequential filenames such as `0001-<dash-case-name>.md`.
- `./lessons/*.html`: Lessons, the main unit of instruction. See [Lessons](#lessons).
- `./reference/*.html`: Attractive, printable summaries for quick lookup. See [Reference Documents](#reference-documents).
- `./assets/*`: Reusable components shared across lessons. See [Assets](#assets).
- `GLOSSARY.md`: Canonical terminology, once a glossary is created. Use [GLOSSARY-FORMAT.md](./GLOSSARY-FORMAT.md).
- `NOTES.md`: User preferences and working notes to consult when designing lessons and teaching.

## Philosophy

Support three kinds of learning:

- **Knowledge**, drawn from high-quality, trusted resources.
- **Skills**, acquired through relevant interactive lessons based on that knowledge.
- **Wisdom**, developed by interacting with other learners and practitioners.

The balance varies by topic. Theoretical physics may emphasize knowledge, while yoga may emphasize skills.

Distinguish **fluency strength**, or immediate recall, from **storage strength**, or long-term retention. Fluency can create an illusory sense of mastery. Build retention through:

- Retrieval practice: recalling from memory.
- Spacing: distributing practice over time.
- Interleaving: mixing related topics, for skills practice only.

Keep explanations easy to understand so they leave working memory available for learning. Use effortful retrieval during practice to make skills durable and flexible.

## The Mission

Tie every lesson to the user's reason for learning. Use the mission's real-world goals to keep lessons concrete and decide what to teach next.

If the mission is unclear or `MISSION.md` is not populated, first ask why the user wants to learn the topic.

Confirm with the user before changing the mission as their skills and knowledge develop. Update `MISSION.md` and add a learning record to capture the change.

## Zone Of Proximal Development

Each lesson should challenge the user just enough to extend their current abilities.

The user may specify exactly what they want to learn. Otherwise, read their learning records and use the mission to choose the most relevant topic within their current reach.

## Lessons

Each lesson should teach one focused skill tied to the mission, with only the knowledge needed to acquire it. Keep it quick to complete, within the user's working-memory limits, and aimed at one tangible outcome they can build on.

Save each lesson as one HTML file in `./lessons/`, named `0001-<dash-case-name>.html`, incrementing the number each time. Keep its instruction self-contained while linking shared assets.

Use beautiful, clean, readable typography and layout that support later review. Think Tufte.

Each lesson should:

- Teach the required knowledge, then guide practice through an interactive feedback loop.
- Link via HTML anchors to other lessons and reference documents.
- Recommend the best primary source found on the topic to read or watch.
- Remind the user to ask the teaching agent follow-up questions about anything unclear.

If possible, open the lesson file for the user with a CLI command.

### Knowledge

Gather knowledge from trusted resources first and track them in `RESOURCES.md`. Until it is well populated, focus on finding high-quality resources. Do not rely on your parametric knowledge.

Link to external sources to support every claim in a lesson.

### Skills

Use quizzes, light in-browser tasks, or guided real-world steps such as yoga poses. Each activity should give feedback on the user's performance as immediately as possible, ideally automatically.

For quizzes, each answer should have exactly the same number of words and, if possible, characters. Vary which position holds the correct answer across questions. Do not reveal the answer through formatting or order.

## Assets

Store reusable components in `./assets/`: stylesheets, quiz widgets, simulators, diagram helpers, and anything else another lesson could reuse.

Before authoring a lesson, inspect `./assets/` and reuse existing components. Put new reusable components there and link to them. Never inline code a future lesson would duplicate.

Create a shared stylesheet as the workspace's first component and link it from every lesson for consistent styling. Add reusable components as the workspace grows.

## Acquiring Wisdom

Wisdom comes from testing skills outside the learning environment. When a question calls for wisdom, attempt an answer, then direct the user to a reputable community where they can learn from practice and other people.

Communities may include forums, subreddits, local interest groups, or real-world classes within the user's budget. Look for reputable communities the user can join, and respect a preference not to join one.

## Reference Documents

Create reference documents alongside lessons, and link to them from lessons. Compress the essential knowledge into attractive, readable HTML documents designed for frequent lookup and printing.

Examples include cheat sheets, programming syntax and snippets, algorithms and flowcharts, yoga poses and sequences, fitness exercises and routines, and glossaries.

Glossaries are an essential reference for topics with specialized terminology. Once a glossary exists, follow its terminology in every lesson.
