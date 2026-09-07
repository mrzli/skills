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

### Notes

Use this document for working notes, user preferences, and information that does not fit elsewhere.

Location: `notes.md`.

#### Format

```md
Notes: <topic-name>

Add content in any suitable form, including paragraphs and sections.
```

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

## Process

Start from what the user wants to learn and already understands. Use conversation context. Ask one question at a time when needed.

Teach one small concept at a time with a concrete example. Invite the user to explain it back or try a small exercise, then give feedback and adapt to their understanding.

Connect each lesson to the user's purpose. Periodically recap what they have learned and suggest what to learn next.
