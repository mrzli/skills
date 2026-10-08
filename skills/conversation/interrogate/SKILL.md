---
name: interrogate
description: Interrogate the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-test their thinking, or uses any 'interrogate' trigger phrases.
---

Interview the user until you reach a shared understanding. Map decisions and their dependencies as a **design tree**.

Work in **rounds**. The **frontier** contains all unresolved decisions whose prerequisites are settled. Ask about every decision in the frontier in one round. Number each question, give your recommended answer, and wait for the user's answers.

Use this format:

```
❓ **Q1** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <your recommended answer>

---

❓ **Q2** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <your recommended answer>
```

Word each question so that answering "yes" accepts your recommendation.

After each round, update the tree from the user's answers and recompute the frontier. Defer questions that depend on unresolved answers to a later round.

Find facts you can look up rather than asking the user for them. When a question needs a fact from the environment, such as a file or available tool, dispatch a sub-agent to investigate. Treat the investigation as an unresolved prerequisite: defer dependent questions until it reports, and ask the remaining frontier questions now. Put every decision to the user and wait for their answer.

Finish when every branch has been explored and no unresolved decisions, investigations, or silent assumptions remain. An empty frontier alone is not enough if prerequisites are still unresolved. Do not act on the resulting plan until the user confirms the shared understanding.
