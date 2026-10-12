---
name: clarify
description: Explain a topic, how something works, or part of the conversation more clearly. Use when the user asks what something means or how it works, or says they do not understand. Defaults to the last response.
argument-hint: "[topic or conversation scope]"
---

Explain the topic or portion of the conversation specified by the argument. If no argument is provided, re-explain your last response.

Give the context needed to understand it, use plain language, and explain unfamiliar terms. Follow the project's terminology where available. Use a small example if it helps.

If the question may have been misread, state your reading of it in one line before explaining. When the user asks a direct question, such as whether they are right, answer it first with yes, no, or partly, then explain.

If the user still does not understand, identify the missing distinction or mistaken assumption before rephrasing again. For mechanisms, name the concrete parts and trace one input through what each part does. When the explanation depends on code, documents, earlier conversation, or other sources, check them before explaining rather than relying on memory or names. Point to where each important claim comes from, such as a file and symbol or a quoted earlier statement, and say what you could not verify instead of filling the gap.

Keep each response within roughly 300 words, allowing modest overruns to finish a coherent explanation. This is a soft limit per response, not a target length or a limit on the total explanation.

Split longer explanations along their natural structure, starting with an overview and moving into smaller topics as needed. For a codebase, these might be architecture, subsystems, directories, files, or sections within a file. Split large topics further when needed. Even the overview can span multiple responses. Requests for more detail should add parts rather than substantially lengthen individual responses.

Stop at a natural boundary after each part. If more remains, briefly indicate the next logical topic and wait for the user to continue, redirect, or ask a follow-up.
