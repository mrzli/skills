---
name: interrogate
description: Question the user in structured rounds about their plan, decision, or idea until every branch is resolved. Use when the user wants their own thinking challenged or stress-tested.
---

Interview the user until you reach a shared understanding. Map decisions and their dependencies as a **design tree**.

Work in **rounds**. The **frontier** contains all unresolved decisions whose prerequisites are settled. Size each round as the user's rules for response size say, asking first about the decisions others depend on. Without such rules, ask about every decision in the frontier in one round. Give each question an ID as the user's rules for IDs say. Without such rules, number the questions Q1, Q2, and so on across the session, without restarting. Give your recommended answer to each, and wait for the user's answers.

Use this format:

```
❓ **<ID>** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <your recommended answer>

---

❓ **<ID>** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <your recommended answer>
```

Word each question so that answering "yes" accepts your recommendation.

After each round, update the tree from the user's answers and recompute the frontier. Defer questions that depend on unresolved answers to a later round.

Find facts you can look up rather than asking the user for them. When a question needs a fact from the environment, such as a file or available tool, dispatch a sub-agent to investigate. Treat the investigation as an unresolved prerequisite: defer dependent questions until it reports, and ask the remaining frontier questions now. Put every decision to the user and wait for their answer.

Finish when every branch has been explored and no unresolved decisions, investigations, or silent assumptions remain. An empty frontier alone is not enough if prerequisites are still unresolved. Do not act on the resulting plan until the user confirms the shared understanding.
