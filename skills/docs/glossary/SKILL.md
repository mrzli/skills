---
name: glossary
description: Create and maintain a project's glossary, the agreed names and short definitions of the concepts used to discuss the product. Use when a project concept is introduced, named, or renamed, when the user finds a project term unclear, or when terms in discussion conflict with the glossary or the code.
---

Keep the project's glossary accurate, so that the user and agents call each concept by one name and can look up what it means. Finish when every term settled, renamed, or found unclear in the current work has an up-to-date entry.

## What belongs

A term is a concept needed to talk about the product's behavior or structure, such as a processing stage, an element the user sees, or a kind of record. Leave out general programming concepts, such as timeouts or error types, and code identifiers that do not name a concept people discuss, such as a builder class.

## Where it lives

Follow the project's convention. Otherwise use `docs/glossary.md`, created when the first term is settled. When creating it, add a pointer to it in the project's `AGENTS.md`.

## Entry format

```md
# Glossary

{One sentence on what the project is.}

## Terms

**Invoice** (`Invoice`):
A request for payment sent to a customer after delivery.
_Avoid_: bill, payment request
```

- Choose one term per concept, preferring the name the user finds clearest. List rejected synonyms under `_Avoid_`.
- No two concepts share a name. A term differs from the project's other terms, unless it reuses a general word as the next item allows. It differs from the built-in names of the frameworks and languages it is used with, without exception. When a new or existing term clashes, propose renaming whichever of the two fits its concept worse. Rename an existing term only once the user agrees, as the user's rules for approval say. Without such rules, ask before renaming an existing term.
- A general word used as a term, such as "source" for a data source, always means the term's concept when it stands alone. Another concept may still use the word where its context always marks it:
  - Such contexts include a field inside one file format and a qualified name like "log source". If that concept has its own entry, its term is the qualified name.
  - Record the other use in a sentence after the term's definition, so readers are not misled.
  - Avoid the reuse where both meanings meet, such as a log entry about loading data that has both a field for the part of the app that wrote it and a field for the data source. If they come to meet later, rename the reuse.
- Define what the concept is in one or two sentences, using other glossary terms where they apply.
- Give the code name when one exists, so readers can find it. Leave out other implementation details.
- Group terms under subheadings when clusters form. A flat list is fine otherwise.
- Describe the current state. Change an entry for a rename in the same change that renames the concept, and move the old name under `_Avoid_`.

## Keep it current

Read the glossary before naming a concept, and check a new name against the built-in names of the frameworks and languages it is used with. Use the glossary's terms in code, documentation, and conversation.

Update an entry as soon as its term is settled, renamed, or found unclear. Do not batch updates until the end of the work.

When a term in the discussion conflicts with the glossary, point out the conflict and settle which meaning is intended. When the user states how a concept works, check that the code agrees and raise any contradiction.

A name that is clear to the agent can still be opaque to the user. When the user asks what a term means or says they keep forgetting it, sharpen the definition or agree on a clearer name with the user.
