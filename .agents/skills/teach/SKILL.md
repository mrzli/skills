---
name: teach
description: Help the user learn a topic or ability through small explanations, examples, and practice.
argument-hint: What would you like to learn?
---

## Name

Create a topic name of one or a few words and derive its kebab-cased form.

Example:

- Topic name: `German grammar`
- Kebab-cased topic name: `german-grammar`

## Persistence

Store learning documents in `./.scratch/learn/<kebab-cased-topic-name>/`.

All document paths below are relative to this directory.

## Documents

### Mission

Record the reason for learning this topic and the constraints.

Location: `mission.md`.

#### Format

```md
# Mission: <topic-name>

## Why

In 1–3 sentences, state the concrete outcome the user wants and how learning this topic will help. Ask for the outcome behind abstract goals such as "to understand X".

## Success conditions

List specific, observable things the user should be able to do after learning. Use one item per outcome.

## Constraints

Record learning preferences and limits on the approach.

## Out of scope

List topics excluded from this learning scope.
```

#### Rules

- **One mission.** If the user wants to learn about something else, use another learning workspace.
- **Explicit purpose.** Interview the user until they can clearly state why they want to learn this topic.
- **Concrete goals.** Use observable outcomes, such as "Be able to list the capitals of all countries."
- **Mutable.** Update the document when the user's goals, scope, or learning path changes.
- **Concise.** Keep the mission statement and goals brief.

### Lessons

Lesson is a main unit of instruction within the learning process.

Should be openable by running a CLI command.

Location: `lessons/####-<kebab-cased-lesson-name>.html`

#### Format

- One HTML file per lesson.
- Have links to other lessons and reference materials.
- Recommend a single, highest-quality primary resource to read or watch if available.
- Have reminder to ask followup questions to the agent. Agent is the teacher that can resolve anything the user finds unclear.

#### Rules

- **Single concept.** One lesson should cover one tightly-scoped knowledge fragment and not depend on other lessons.
- **Beautiful and readable.** Should have beautiful, clean and readable styling and layout.
- **Short.** Completable very quickly. Considerate of learners small working memory.
- **Small goal.** Should give a user a single tangible win he can build on.

### Reference Materials

Raw units of learning, compressed essence of a lesson.

Examples:

- Cheat sheets.
- Syntax, code snippets, reference algorithms.
- Exercises and routines for fitness.
- Glossaries.

Location: `reference/*.html`.

#### Format

- HTML document.

#### Rules

**Beautiful, readable and pritable.** Easy to use as quick reference.

### Assets

Share reusable images, stylesheets, widgets, simulators, and diagrams across lessons and reference materials.

Use one main stylesheet for all lessons and one for all reference materials to keep styling consistent. Use the same stylesheet for both when appropriate.

Location: `assets/*`.

### Learning Records

Persistent information about what user has learned. Important for driving learning process.

Each can capture some of:

- Non-obvious lesson.
- Key insights.
- Stated prior knowledge.

Location: `learning-records/####-<kebab-cased-record-name>.md`

#### Format

```md
(optional frontmatter, use when necessary)
---
status: active (default) | superseded by ####
---

# Learning record: <short-title-on-what-was-learned>

## Summary

- 1-3 sentences. What was learned, or what prior knowledge what established. Why it matters for future lessons.

## Evidence (optional)

- How the user demonstrated understanding. A question answered, exercize completed, a statement by the user.
```

### Resources

List resources the user can explore for further learning.

Location: `resources.md`.

#### Format

```md
# Resources: <topic-name>

## Recommended

List recommended resources.
```

#### Rules

- **Reliable sources.** Prefer primary sources, recognized experts, peer-reviewed work, and communities with strong moderation. Avoid marketing.
- **Describe entries.** Include a link, a short description of one sentence, and a `Use for: <purpose>.` sentence for each entry.
- **Gaps.** Record areas without good resources in a separate `## Gaps` section.
- **Prune.** Aggressively remove incorrect, outdated, low-quality, or broken resources.
- **Exclusions.** Record resources the user has excluded in a separate `## Exclusions` section.

### Notes

Use this document for working notes, teaching preferences, and information that does not fit elsewhere.

Location: `notes.md`.

#### Format

```md
Notes: <topic-name>

Add content in any suitable form, including paragraphs and sections.
```

## Process

Start from what the user wants to learn and already understands. Use conversation context. Ask one question at a time when needed.

Teach one small concept at a time with a concrete example. Invite the user to explain it back or try a small exercise, then give feedback and adapt to their understanding.

Connect each lesson to the user's purpose. Periodically recap what they have learned and suggest what to learn next.

## [TODO Process, MODELS DO NOT EDIT]

### Reference documents

While creating lessons, you should also create reference documents. Lessons can reference these documents - they are useful for tracking raw units of knowledge useful across lessons.

Glossaries, in particular, are an essential reference. Once one is created, it should be adhered to in every lesson.

### Assets

Reuse is the default, not the exception. Before authoring a lesson, read ./assets/ and build from the components already there. When a lesson needs something new and reusable, write it as a component in ./assets/ and link to it; never inline code a future lesson would duplicate.

### Learning records

These should be used to calculate the zone of proximal development.

#### When to write a learning record

Write one when any of these is true:

1. **The user demonstrated genuine understanding of something non-trivial**: not just exposure, but evidence they can use the concept correctly. This sets a new floor for what to teach next.
2. **The user disclosed prior knowledge**: "I already know X." Record it so future sessions don't re-teach it. Also record the _depth_ claimed.
3. **A misconception was corrected**: the user previously believed something wrong and now sees why. These are high-value: they predict future stumbling blocks for related topics.
4. **The mission shifted in response to learning**: the user discovered they cared about something different than they thought. Cross-link to [[MISSION.md]] and update it.

##### What does _not_ qualify

- Material that was merely covered. Coverage is not learning. Wait for evidence.
- Anything already captured tersely in [[GLOSSARY.md]] as a term definition. Don't duplicate.
- Session-by-session activity logs. Learning records are not a journal: they are decision-grade insights.

#### Supersession

When a later record contradicts an earlier one (the user's understanding deepened or corrected), mark the old record `Status: superseded by LR-NNNN` rather than deleting it. The history of how understanding evolved is itself useful signal.
