# Learning Record Format

Learning records live in `./learning-records/` and use sequential numbering: `0001-slug.md`, `0002-slug.md`, etc. Create the directory lazily: only when the first record is written.

Like architectural decision records, they capture non-obvious lessons, key insights, and stated prior knowledge that guide future sessions. Use them to assess the user's zone of proximal development.

## Template

```md
# {Short title of what was learned or established}

{1-3 sentences: what was learned (or what prior knowledge was established), and why it matters for future sessions.}
```

A single paragraph is enough. Record what is now known and why it changes what to teach next.

## Optional sections

Include these only when useful. Most records won't need them.

- **Status** frontmatter (`active | superseded by LR-NNNN`): useful when an earlier understanding turns out to be wrong and is replaced.
- **Evidence**: how the user demonstrated the understanding (a question answered, an exercise completed, prior experience cited). Useful when the claim might be revisited.
- **Implications**: what this unlocks or rules out for future sessions. Worth recording when non-obvious.

## Numbering

Scan `./learning-records/` for the highest existing number and increment by one.

In supersession status, `LR-NNNN` refers to the record whose filename starts with `NNNN-`. For example, `LR-0002` refers to `0002-<slug>.md`.

## When to write a learning record

Write one when any of these is true:

1. **The user demonstrated understanding of something non-trivial**: evidence they can use the concept correctly establishes a new starting point for future teaching.
2. **The user disclosed prior knowledge**: "I already know X." Record it so future sessions don't re-teach it. Also record the _depth_ claimed.
3. **A misconception was corrected**: the user previously believed something wrong and now sees why. Record it to anticipate difficulties with related topics.
4. **The mission shifted in response to learning**: the user discovered they cared about something different than they thought. Confirm the change with the user, update `MISSION.md`, and link to it from the record using `../MISSION.md`.

### What does _not_ qualify

- Material that was merely covered. Coverage is not learning. Wait for evidence.
- Term definitions already captured in `GLOSSARY.md`. Don't duplicate them.
- Session-by-session activity logs. Keep records focused on insights that guide future teaching.

## Supersession

When a later record contradicts an earlier one because the user's understanding deepened or was corrected, mark the old record `Status: superseded by LR-NNNN`. Keep the old record to preserve how their understanding evolved.
