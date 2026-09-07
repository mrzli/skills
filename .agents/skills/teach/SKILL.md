---
name: teach
description: Help the user learn a topic or ability through small explanations, examples, and practice.
argument-hint: What would you like to learn?
---

## Name

Create a short name about the topic, can be a single word or few words, but keep it very short, few words at most. You will need to derive a kebab-cased name as well.

Example:

- Topic name: `German grammar`
- Kebab cased topic name: `german-grammar`

## Persistence

You need to store documents related to this learning topic. Put it inside `./.scratch/learn/<kabab-cased-topic-name>` directory.

All document paths from now on will be relative to the above directory.

## Documents

### Notes

Generic document that contains information that does not fit anywhere else.

You can use it for your internal notes and user preferences, and anything else that seems appropriate.

Location: `notes.md`.

#### Format

```md
Notes: <topic-name>

Here goes the content. It can have abritrary form, can include paragraphs and sections.
```

### Mission

Document that stores fundamental information about why this topic should be learned and constraints.

Location: `mission.md`.

#### Format

```md
# Mission: <topic-name>

## Why

1-3 sentences. The concrete real-world goal the user is laerning this for. What benefit do they gain by learning this topic? Avoid abstract framings like "to understand X", ask for underlying outcome.

## Success conditions

List of specific, observable things user is able to do after learning. One thing per list item.

## Constraints

Learning preferences, and anything that bounds the approach.

## Out of scope

List of topics to be excluded from this learning scope.
```

#### Rules

- **One mission.** If the user wants to learn about something else, use another learning workspace.
- **Explicit purpose.** Interview the user until he can clearly say why he wants to learn this topic.
- **Concrete goals.** "Be able to list capitals of all countries" instead of "learn more geography". 
- **Mutable.** User's goals, scope, and learning path are allowed to change. When it changes, update the document.
- **Concise.** Keep the mission statement and goals brief and to the point. Avoid unnecessary details.

## Process

Start from what the user wants to learn and already understands. Use conversation context. Ask one question at a time when needed.

Teach one small concept at a time with a concrete example. Invite the user to explain it back or try a small exercise, then give feedback and adapt to their understanding.

Connect each lesson to the user's purpose. Periodically recap what they have learned and suggest what to learn next.
