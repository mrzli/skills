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

TODO

### Learning Records

TODO

### Reference Materials

TODO

### Assets

Share reusable images, stylesheets, widgets, simulators, and diagrams across lessons and reference materials.

Use one main stylesheet for all lessons and one for all reference materials to keep styling consistent. Use the same stylesheet for both when appropriate.

Location: `assets/*`.

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

### Assets

Reuse is the default, not the exception. Before authoring a lesson, read ./assets/ and build from the components already there. When a lesson needs something new and reusable, write it as a component in ./assets/ and link to it; never inline code a future lesson would duplicate.