---
name: investigate
description: Answer a concrete engineering question through code inspection, primary-source research, or a focused experiment. Use when an unknown needs evidence before a decision or implementation can proceed.
---

Produce a supported answer to the question, including the limits of the evidence. Investigation may recommend a change. It does not imply production implementation.

## Define the question

Identify the unknown, the decision it affects, and what evidence would answer it. Use the request and available context to bound the work. Ask for clarification only when different interpretations would lead to materially different investigations.

Read relevant project instructions and existing findings. Record important versions, configuration, and environmental assumptions. Prefer the smallest useful investigation. Broaden it when the evidence exposes a necessary dependency or contradicts the initial explanation.

## Gather evidence

Choose the method that can resolve the uncertainty:

- Trace code, callers, tests, configuration, and history to establish how the system behaves.
- Consult primary sources for external contracts and capabilities, checking that they apply to the version and environment in use.
- Run a focused experiment or prototype when inspection cannot settle behavior, feasibility, or performance.

Use [prototype](../prototype/SKILL.md) when the question needs an interactive demonstration of UI or logic for the user to explore. Keep benchmarks and other technical experiments here, and interpret prototype observations against the original question.

For experiments, state the question and expected distinguishing observation before running them. Use representative inputs and a comparison or baseline where needed. Keep experimental code and data isolated in the project's scratch area or a temporary directory. Document how to reproduce the result and distinguish observed behavior from simulation or mocks.

Test competing explanations when the first plausible answer lacks support. Track failed approaches only when they prevent repeated work or explain the conclusion. If further access or a consequential external action is needed, gather what is available first and identify the exact missing evidence. Do not change live systems merely to obtain an answer.

## Report the answer

Lead with the conclusion or the unresolved question. Support it with file locations, source links, commands, or experimental results. Separate observations, inferences, and assumptions. Explain confidence, relevant limitations, and what the answer means for the decision that prompted the work.

For substantial investigations or later handoff, save findings using the existing project convention or `.scratch/investigations/<descriptive-slug>.md`. Include enough setup and artifact references to reproduce important results. A short answer with evidence is sufficient for a small question.

Stop when the question is answered well enough for its decision, or when a specific evidence gap prevents further useful progress. Return the result to the caller. Production fixes, design commitments, and discarded experimental artifacts should remain distinguishable from findings.
