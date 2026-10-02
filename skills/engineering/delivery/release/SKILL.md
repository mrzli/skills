---
name: release
description: Prepare and execute a software release using the project's delivery procedure, then verify the result. Use for deploying a verified change or publishing a version to a specified environment or audience.
---

Deliver a known revision or artifact to the intended target and record evidence of its state. Use the project's release procedure and available tools; release preparation and an actual release are distinct outcomes.

## Establish the release boundary

Read the request, project instructions, release documentation, CI configuration, and relevant change and verification records. Identify the revision or artifact, target environment or registry, version where applicable, and the authorized actions. Resolve ambiguous targets before an external mutation.

Inspect the working tree, branch, and release state. Ensure the artifact being released corresponds to the verified change; account for any subsequent edits or rebuilds. Check required tests, review findings, dependencies, configuration, migrations, and compatibility with the running system. If evidence is missing, complete the available preparation and report what blocks release.

## Prepare the operation

Use established automation and versioning conventions. Identify the release steps, post-release checks, and relevant failure signals. For changes to persistent data or public contracts, establish deployment ordering, backward compatibility, and the recovery procedure. Check whether rollback is actually safe; restoring an old binary may not reverse a data migration.

Prepare required release notes or artifacts using the project convention. Keep secrets in the configured credential mechanism. Verify access with read-only checks where possible. Avoid inventing infrastructure, deployment commands, or credentials when the project has not established them.

If existing authorization covers the concrete operation, proceed. Otherwise finish preparation first, then request only the missing approval with the target, revision, and consequences clearly stated. A request to prepare a release is not permission to publish it.

## Execute and verify

Run the authorized release steps and record their results. Inspect remote or deployment state after an ambiguous tool outcome before retrying, especially for version publication or migrations that cannot safely repeat. Stop dependent steps when a prerequisite fails.

Verify the deployed revision or published artifact and exercise the critical behavior through the target environment or consumer interface. Check migration state and available health signals where relevant. A successful build or deployment command alone does not establish that the release works.

If verification fails, use the established recovery procedure within the authorized scope. Confirm the resulting state and report unresolved impact. Where recovery needs a new consequential decision, preserve evidence and present the concrete options rather than guessing.

## Record the result

Update the existing release record or use the project's convention; if absent, save a concise record to `docs/releases/<version-or-descriptive-slug>.md`. Include revision and artifact identifiers, target, actions taken, verification evidence, and any recovery or remaining limitations. Record unsuccessful attempts too when they changed external state.

Finish with an explicit status: prepared but not released, released and verified, or incomplete with the known target state. Do not equate a created pull request or local tag with a completed deployment or publication.
