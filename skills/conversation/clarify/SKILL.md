---
name: clarify
description: Explain a topic, how something works, or part of the conversation more clearly. Use when the user asks what something or an item ID means, such as "what is X", "clarify X", "explain X", "in plain words", or ELI5, asks how something works or whether their understanding is right, or says they do not understand. Defaults to the last response.
argument-hint: "[topic or conversation scope]"
---

Explain the topic or portion of the conversation specified by the argument. If no argument is provided, re-explain your last response.

Give the context needed to understand it, use plain language, and explain unfamiliar terms. Follow the project's terminology where available. Use a small example if it helps. When the user asks what a project term means or says they keep forgetting it, offer to add or sharpen its entry using the `glossary` skill.

If the question may have been misread, state your reading of it in one line. Then answer any direct question, such as whether they are right, with yes, no, or partly, then explain.

For mechanisms, name the concrete parts and trace one input through what each part does. When the explanation depends on code, documents, earlier conversation, or other sources, check them before explaining rather than relying on memory or names. Point to where each important claim comes from, such as a file and symbol or a quoted earlier statement, and say what you could not verify instead of filling the gap.

When an explanation shows that a name misled the user, propose a better name and leave the rename until they agree. If they are still lost, make the proposal only once they follow.

Keep each response within roughly 300 words, allowing modest overruns to finish a coherent explanation. The limit is deliberately shorter than for other responses, because an explanation is meant for someone who is already struggling to follow. It is a soft limit per response, not a target length or a limit on the total explanation.

When the user says they are lost or still do not understand, apply these rules until they say they follow:

- Keep each response within roughly 100 words.
- Answer one point, and put it first. Leave the rest for later responses.
- Do not ask the user to decide or approve anything. Make any offer, such as a glossary entry, once they follow.
- Make that point a correction to the user's model of the topic, such as a missing distinction or mistaken assumption, then say what you took that model to be.
- If you cannot tell what the model is, ask for it in place of the correction. Still answer a direct question first.
- Do not explain the structure of your own explanation or proposal, and do not rephrase the earlier explanation.

Split longer explanations along their natural structure, starting with an overview and moving into smaller topics as needed. For a codebase, these might be architecture, subsystems, directories, files, or sections within a file. Split large topics further when needed. Even the overview can span multiple responses. Requests for more detail should add parts rather than substantially lengthen individual responses.

Stop at a natural boundary after each part. If more remains, briefly indicate the next logical topic and wait for the user to continue, redirect, or ask a follow-up.
