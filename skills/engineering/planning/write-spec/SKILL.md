---
name: write-spec
description: Turn agreed intent into a durable specification with scope, behavior, and verifiable acceptance criteria. Use when requirements from a conversation, brief, or existing document need to guide implementation or review.
---

Write a specification that another agent or developer can use without reconstructing the conversation. Synthesize established requirements and decisions, with detail proportional to the change.

## Establish the source of truth

Read the request, relevant conversation, referenced artifacts, and applicable project instructions. Inspect enough of the codebase to distinguish current behavior from the proposed change and to identify relevant interfaces and constraints. Follow established terminology and architectural decisions.

Separate agreed requirements from suggestions, assumptions, and unresolved decisions. Resolve factual questions from available evidence. Ask focused questions only when missing information materially changes the specification. Draft the settled parts while questions remain open. Mark the document as a draft if unresolved decisions block implementation. Keep routine implementation choices open unless they are actual constraints.

## Describe the change

Use the project's specification format if one exists. Otherwise, organize the document around the following content, combining sections when the change is small:

- **Purpose and scope:** the problem, intended outcome, and boundaries, including relevant exclusions.
- **Required behavior:** observable behavior, important examples, and failure cases. Cover compatibility, permissions, data changes, or operational constraints where they affect the requested outcome.
- **Agreed design:** technical decisions and constraints already established, with reasons where they help implementation. Link to existing decisions rather than duplicating them. Label proposed approaches as proposals.
- **Acceptance and verification:** observable conditions that distinguish a working change from an incomplete one, and how they can be checked.
- **Open questions:** unresolved decisions and assumptions, their consequences, and which ones block implementation.

Make acceptance criteria specific enough for an implementer and reviewer to reach the same conclusion. Replace vague requirements such as "handles errors gracefully" with the expected response to concrete failure cases. Cover the important behaviors and constraints without inventing requirements to fill a template.

Choose verification appropriate to each criterion, such as automated tests, application interaction, or operational checks. Prefer existing test boundaries and tools. Identify verification gaps. Code inspection or a passing unit test may not prove an end-to-end outcome. Leave test implementation details to implementation unless already agreed.

Include paths, interfaces, or small examples when they materially clarify a requirement or decision. Distinguish references to the current implementation from required future structure. Keep task breakdown and scheduling for planning.

## Save and check

Update the existing specification when it covers the same change. Otherwise use the requested destination or project convention. Absent either, save it where the user's rules put work in progress. Without such rules, save to `.scratch/specs/<descriptive-slug>.md`. Read the target before editing, preserve unrelated content, and consolidate superseded statements so the specification expresses the current agreement.

Publish to an external tracker only when authorized by the request or established workflow. Otherwise report the saved local path.

Check the document against its sources for omissions, contradictions, and unapproved additions. Ensure each important requirement has a verification route and that another implementer can identify what is settled and what remains open.

Finish by linking the specification and stating any decisions that still block implementation. Writing the specification alone does not authorize implementing it.
