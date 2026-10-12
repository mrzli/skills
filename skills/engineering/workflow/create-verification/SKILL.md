---
name: create-verification
description: Create a project-local verification skill and tool that let agents launch the real application, drive it as a user would, and capture evidence. Use when a project has no scripted way to prove UI, CLI, or service behavior, or when results keep being checked by hand.
disable-model-invocation: true
---

Give the project a reusable, tested way for any agent to prove that a change works in the real application. Write the result for an agent that reads it mid-task without knowing the application.

## Inspect the project

Answer these from the repository, and ask the user only what cannot be observed:

- **Surface:** what a user actually touches, such as a desktop or web UI, a CLI, a service, or setup scripts. Pick the primary surface and note the others.
- **Run:** how the application starts locally, using the project's documented commands, with its ports, environment, data, and authentication.
- **Drive:** how an agent can operate it. Prefer existing harnesses and test drivers. Otherwise choose a generic method, such as browser automation, a virtual display like Xvfb for desktop applications, a terminal multiplexer for interactive CLIs, or HTTP requests for services.
- **Observe:** what evidence is available, such as screenshots, accessibility snapshots, terminal output, responses, logs, exit codes, and files or state written.
- **Isolate:** whether two instances can run side by side with separate ports, data, and profiles. If not, the skill must refuse to drive an instance it did not start.

If the project does not build or start as is, fix that first or report the exact blocker. A skill written against a broken base teaches wrong steps.

## Write the tool and the skill

Create a small command-line tool for the project, following its conventions. Give it subcommands for launch, doctor, drive actions, evidence capture, and cleanup. A tool keeps every agent on the same interface, uses less context than ad hoc scripts, and lets the user rerun a check.

Write `verify-<app>/SKILL.md` where the project keeps agent skills. If it keeps none, use `.agents/skills/verify-<app>/` and link `.claude/skills/verify-<app>` to it. Include frontmatter with a description that names the application, the surface, and when to use the skill. Cover each part with real commands from this project:

- **Launch:** the command that starts the application and how to tell it is ready. Ready means usable from empty data, including migrations and seed data, not merely a process that answers. Include teardown.
- **Doctor:** one read-only check that the instance is worth driving, such as the right process, build, port, and authentication. Run it first whenever something looks wrong.
- **Drive:** recipes using stable handles, such as accessible names, command names, or routes, rather than coordinates or tab order.
- **Evidence:** what to capture and where it is saved. Exercise the real user path, not internal setters or test-only endpoints. Capture the action and the resulting state, and check side effects as well as what is visible. For visual output, capture each relevant variant, such as light and dark themes or window sizes. When the safe path is a dry run, observe what it actually skips.
- **Cleanup:** stop only what the run started, never by process name, and keep the evidence.

Add a short feature map when the application has several user-facing features. Follow [feature-map.md](references/feature-map.md).

## Prove it before handing it over

Run the new skill end to end once: launch, doctor, drive one mapped feature, capture evidence, and clean up. Confirm that the evidence survived cleanup. Fix whatever fails, cleaning up after each failed attempt. A verification skill that was never run is a draft.

If the proof ran in a stand-in for the real target, such as a container instead of a fresh machine, list the steps the stand-in performed that the target will not. Those steps remain unverified.

Report the skill and tool paths, the feature proved, the evidence location, and any unverified parts. Tell the user that [implement](../../delivery/implement/SKILL.md), [fix-bug](../../delivery/fix-bug/SKILL.md), and [deliver](../deliver/SKILL.md) use the skill when it exists, and that the feature map should be updated when user-facing features change.
