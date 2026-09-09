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

### Learning Map

Outline what to learn and in what order, guided by the mission and the user's starting knowledge.

Location: `learning-map.md`.

#### Format

```md
# Learning map: <topic-name>

## Topics

List the main topics, intended outcomes, and any prerequisite knowledge in a suggested learning order. Link to lessons as they become available.
```

#### Rules

- **Provisional, mutable.** Start with a brief outline. Update it as understanding, goals, or priorities change.
- **Focused.** Include topics that support the mission. Keep current lesson status in `progress.md`.

### Progress

Keep the current learning position and enough context to resume in another session. Use learning records for lasting insights and evidence of understanding.

Location: `progress.md`.

#### Format

```md
# Progress: <topic-name>

## Current activity

Identify the lesson, practice, or review and its intended outcome. Link to relevant files.

## Where we stopped

Briefly describe what was covered or attempted, unfinished work, and unresolved questions. Link to relevant learning records without repeating them.

## Next step

Suggest the next activity and explain why it fits.
```

#### Rules

- **Current state.** Update after meaningful learning steps and before pausing when possible. Replace stale status instead of accumulating a session log.
- **Accurate.** Distinguish material presented from understanding demonstrated. Do not infer mastery from exposure.
- **Resume.** Read this file with the mission, learning map, and relevant learning records before continuing an existing workspace.

### Lessons

A lesson is the main unit of instruction in the learning process.

Make each lesson openable with a CLI command.

Location: `lessons/####-<kebab-cased-lesson-name>.html`

#### Format

- One HTML file per lesson.
- Link to other lessons and reference materials.
- Recommend the highest-quality primary resource available to read or watch, if any.
- Remind the user to ask the teaching agent follow-up questions about anything unclear.

#### Rules

- **Single concept.** Cover one focused concept without depending on other lessons.
- **Attractive and readable.** Use attractive, clean, readable styling and layout.
- **Short.** Keep lessons quick to complete and within the learner's working-memory limits.
- **Small goal.** Give the user one tangible outcome they can build on.

### Reference Materials

Summarize the essential information from lessons for quick lookup.

Examples:

- Cheat sheets.
- Syntax, code snippets, reference algorithms.
- Exercises and routines for fitness.
- Glossaries.

Location: `reference/*.html`.

#### Format

- HTML document.

#### Rules

**Attractive, readable, and printable.** Make materials easy to use for quick reference.

### Assets

Share reusable images, stylesheets, widgets, simulators, and diagrams across lessons and reference materials.

Use one main stylesheet for all lessons and one for all reference materials to keep styling consistent. Use the same stylesheet for both when appropriate.

Location: `assets/*`.

### Learning Records

Keep a long-term record of what the user has learned to guide future teaching.

Each record can capture:

- Non-obvious lessons.
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

- In 1–3 sentences, describe what was learned or what prior knowledge was established, and why it matters for future lessons.

## Evidence (optional)

- Describe how understanding was demonstrated or prior knowledge was reported, such as an answer, completed exercise, or user statement.
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
