---
name: teach
description: Teach the user a topic through a multi-session course of lessons and practice, tracked in .scratch/learn/. Use when the user wants to learn a subject or skill over time.
argument-hint: "[topic]"
disable-model-invocation: true
---

Teach the topic over multiple sessions, preserving the user's learning state in a workspace.

## Teaching workspace

Create a learning workspace in `.scratch/learn/<topic-slug>`, or resume the existing workspace for that topic. It stays in use while the course continues, so do not remove it as finished work.

All learning document paths below are relative to that workspace. Format links refer to files beside this skill.

- `MISSION.md`: The user's reason for learning, which grounds all teaching. Use [MISSION-FORMAT.md](./MISSION-FORMAT.md).
- `RESOURCES.md`: Trusted sources and communities for knowledge and wisdom. Use [RESOURCES-FORMAT.md](./RESOURCES-FORMAT.md).
- `./learning-records/*.md`: Non-obvious lessons, key insights, and prior knowledge that guide future sessions. Use [LEARNING-RECORD-FORMAT.md](./LEARNING-RECORD-FORMAT.md) for their content and filenames.
- `./lessons/*.html`: Lessons, the main unit of instruction. See [Lessons](#lessons).
- `./reference/*.html`: Attractive, printable summaries for quick lookup. See [Reference documents](#reference-documents).
- `./assets/*`: Reusable components shared across lessons. See [Assets](#assets).
- `GLOSSARY.md`: The topic's canonical terms, created when the user understands the first one. Use [GLOSSARY-FORMAT.md](./GLOSSARY-FORMAT.md).
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

## The mission

Tie every lesson to the user's reason for learning. Use the mission's real-world goals to keep lessons concrete and decide what to teach next.

If the mission is unclear or `MISSION.md` is not populated, first ask why the user wants to learn the topic.

Confirm with the user before changing the mission as their skills and knowledge develop. Update `MISSION.md` and add a learning record to capture the change.

## Zone of proximal development

Each lesson should challenge the user just enough to extend their current abilities.

The user may specify exactly what they want to learn. Otherwise, read their learning records and use the mission to choose the most relevant topic within their current reach.

## Lessons

Each lesson should teach one focused skill tied to the mission, with only the knowledge needed to acquire it. Keep it quick to complete, within the user's working-memory limits, and aimed at one tangible outcome they can build on.

Save each lesson as one HTML file in `./lessons/`, named `0001-<dash-case-name>.html`, incrementing the number each time. Keep its instruction self-contained while linking shared assets.

Use clean, readable typography and layout that support later review, in the style of Edward Tufte, with dense, clear content and little decoration.

Each lesson should:

- Teach the required knowledge, then guide practice through an interactive feedback loop.
- Link via HTML anchors to other lessons and reference documents.
- Recommend the best primary source found on the topic to read or watch.
- Remind the user to ask the teaching agent follow-up questions about anything unclear.

If possible, open the lesson file for the user with a CLI command.

### Knowledge

Gather knowledge from trusted resources first and track them in `RESOURCES.md`. Until it is well populated, focus on finding high-quality resources. Do not rely on what you remember from training.

Link to external sources to support every claim in a lesson.

### Skills

Use quizzes, light in-browser tasks, or guided real-world steps such as yoga poses. Each activity should give feedback on the user's performance as immediately as possible, ideally automatically.

For quizzes, give all answer options of a question the same number of words and, if possible, characters. Vary which position holds the correct answer across questions. Do not reveal the answer through formatting or order.

## Assets

Store reusable components in `./assets/`: stylesheets, quiz widgets, simulators, diagram helpers, and anything else another lesson could reuse.

Before authoring a lesson, inspect `./assets/` and reuse existing components. Put new reusable components there and link to them. Never inline code a future lesson would duplicate.

Create a shared stylesheet as the workspace's first component and link it from every lesson for consistent styling. Add reusable components as the workspace grows.

## Acquiring wisdom

Wisdom comes from testing skills outside the learning environment. When a question calls for wisdom, attempt an answer, then direct the user to a reputable community where they can learn from practice and other people.

Communities may include forums, subreddits, local interest groups, or real-world classes within the user's budget. Look for reputable communities the user can join, and respect a preference not to join one.

## Reference documents

Create reference documents alongside lessons, and link to them from lessons. Compress the essential knowledge into attractive, readable HTML documents designed for frequent lookup and printing.

Examples include cheat sheets, programming syntax and snippets, algorithms and flowcharts, yoga poses and sequences, and fitness exercises and routines. For a topic with specialized terminology, add a printable version of `GLOSSARY.md`.

Once `GLOSSARY.md` exists, follow its terminology in every lesson.
