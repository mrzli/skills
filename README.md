# Agent Skills

These are the skills I use every day with Claude Code and Codex. Most of them cover software engineering, from shaping a feature through design, implementation, review, and release. The rest help with conversations, documentation, and learning.

The skills are written to work together. Each one does one job and names the skill to use next when the work calls for it.

## Installation

To install the skills, clone the repository and run the sync script with `--user`. It links each skill into the directories the agents read, `~/.claude/skills` for Claude Code and `~/.agents/skills` for Codex:

```bash
git clone https://github.com/mrzli/skills.git
cd skills
bash scripts/sync-skills.sh --user
```

To update, run `git pull` and the script again. The script links new skills, removes links to skills that were deleted, and leaves other skills in those directories alone. It stops without changing anything if a skill of the same name is already installed from elsewhere.

Without `--user`, the script links the skills only into this repository's own `.claude/skills` and `.agents/skills`. An agent started in this repository then finds them without a user-wide installation, which is a way to try them out.

## Getting started

You don't need to name a skill. The agent loads one on its own when a request matches it, such as "find out why the chart stutters and fix it" for [fix-bug](skills/engineering/delivery/fix-bug/SKILL.md). When you're not sure what to do next, ask, and [guide](skills/engineering/workflow/guide/SKILL.md) suggests the next skill.

Eight skills load only when you call them by name, such as `/spawn` in Claude Code: collect, create-verification, explore, restate, spawn, teach, warmup, and yield.

## How I use them

I talk to the agent in one main session, mostly by voice dictation. My global agent instructions give every question, option, and work item an ID, such as F2 or B7d2, so I can answer or approve each one briefly.

- **Discussion and implementation run side by side.** Once I agree to an item, [queue-work](skills/engineering/workflow/queue-work/SKILL.md) hands it to a background agent, and the discussion moves on to the next item.
- **A point that needs a longer discussion gets its own tab.** `/spawn F2` opens a fork of the session in a new terminal tab, started from a short brief or from a full copy of the conversation. Forks only discuss and never change the checkout. A fork can open forks of its own.
- **Results come back without copying.** spawn records which tab each fork came from, so the tabs form a tree. In a fork, `/yield` writes a note of what was decided and which changes I agreed to. In any tab above it, `/collect` takes in the new notes from the forks below, at any depth. In the main tab, it also queues the agreed changes, so all changes to the checkout happen in one tab.
- **After a break,** `/warmup` says where the work stopped and suggests a few small steps to get back into it.
- **When a session ends or work moves to another repository,** [handoff](skills/conversation/handoff/SKILL.md) writes what the next session needs.

[spawn](skills/conversation/spawn/SKILL.md) needs Claude Code running in herdr or tmux, and [yield](skills/conversation/yield/SKILL.md) and [collect](skills/conversation/collect/SKILL.md) rely on the tree it records. They work only in the tabs spawn opened and in the tabs above them. [warmup](skills/conversation/warmup/SKILL.md) reads Claude Code and Codex session files from their default locations.

## How the skills improve

Most changes come from my own work with the agents. Two of the skills review that work:

- [improve-workflow](skills/engineering/workflow/improve-workflow/SKILL.md) goes through my past sessions, such as the places where I corrected the agent or repeated a step by hand, and proposes the smallest change to a skill, the project's instructions, or its tooling that would have prevented the problem.
- [maintain-skills](skills/engineering/workflow/maintain-skills/SKILL.md) reviews the collection as a whole. It counts how often I use each skill in my session history, checks that each name and description matches what I actually ask for, and keeps the skills consistent with my global agent instructions. It runs routing tests, realistic requests that check a fresh agent loads the right skill.

maintain-skills also looks through [Matt Pocock's skills](https://github.com/mattpocock/skills) and [pstack](https://github.com/cursor/plugins/tree/main/pstack) for new ideas. It adopts one only when it fits how I work and solves a problem I actually have.

The reviews and their results are kept in [.scratch/skills](.scratch/skills) and [.scratch/workflow](.scratch/workflow).

## Skills

### [Docs](skills/docs)

| Skill | Description |
| --- | --- |
| [glossary](skills/docs/glossary/SKILL.md) | Keep a project's agreed terms and short definitions current. |
| [tidy-docs](skills/docs/tidy-docs/SKILL.md) | Review and clean up documentation in a repository. |
| [writing-agents](skills/docs/writing-agents/SKILL.md) | Guide the writing of `AGENTS.md` files. |
| [writing-skills](skills/docs/writing-skills/SKILL.md) | Guide the writing of agent skills. |
| [writing-text](skills/docs/writing-text/SKILL.md) | Make text concise, clear, and direct. |

### [Conversation](skills/conversation)

| Skill | Description |
| --- | --- |
| [clarify](skills/conversation/clarify/SKILL.md) | Explain a topic, how something works, or part of the conversation more clearly, or check the user's understanding, splitting longer explanations into manageable parts. Defaults to the last response. |
| [collect](skills/conversation/collect/SKILL.md) | Take in the notes of forks below this tab, at any depth, and queue the changes agreed in them to implement now. |
| [explore](skills/conversation/explore/SKILL.md) | Clarify a vague interest or problem through questions and small next steps. |
| [handoff](skills/conversation/handoff/SKILL.md) | Summarize a session so another agent can continue the work. |
| [interrogate](skills/conversation/interrogate/SKILL.md) | Stress-test a plan or idea through structured rounds of questions. |
| [recap](skills/conversation/recap/SKILL.md) | Summarize where the work or discussion stands, including decisions, open questions, and status. |
| [restate](skills/conversation/restate/SKILL.md) | Restate the user's goals and problem in clear words, including long or dictated requests. |
| [spawn](skills/conversation/spawn/SKILL.md) | Open a fork in a new terminal tab to discuss one point, from a short brief or a full copy of the conversation. |
| [warmup](skills/conversation/warmup/SKILL.md) | Get back into a project after a break, with a very short summary and a few small steps. |
| [yield](skills/conversation/yield/SKILL.md) | Write a short note of what a fork has resolved, for the tabs above it to collect. |

### [Learning](skills/learning)

| Skill | Description |
| --- | --- |
| [teach](skills/learning/teach/SKILL.md) | Teach a topic through lessons that track the user's progress across sessions. |

### [Engineering](skills/engineering)

#### [Planning](skills/engineering/planning)

| Skill | Description |
| --- | --- |
| [write-spec](skills/engineering/planning/write-spec/SKILL.md) | Capture agreed requirements, scope, and verifiable acceptance criteria in a durable specification. |
| [plan](skills/engineering/planning/plan/SKILL.md) | Break agreed work into verifiable tasks with explicit dependencies. |
| [shape-feature](skills/engineering/planning/shape-feature/SKILL.md) | Clarify a feature's user problem, behavior, and useful scope. |
| [design](skills/engineering/planning/design/SKILL.md) | Choose a technical approach and record the important tradeoffs. |
| [start-project](skills/engineering/planning/start-project/SKILL.md) | Define project purpose, users, first useful scope, and success criteria. |

#### [Delivery](skills/engineering/delivery)

| Skill | Description |
| --- | --- |
| [implement](skills/engineering/delivery/implement/SKILL.md) | Build a scoped code change, verify it, and resolve review findings. |
| [review-code](skills/engineering/delivery/review-code/SKILL.md) | Review a change against intended behavior and project conventions, with actionable findings. |
| [fix-bug](skills/engineering/delivery/fix-bug/SKILL.md) | Diagnose a failure, repair its cause, and verify the fix. |
| [optimize](skills/engineering/delivery/optimize/SKILL.md) | Improve a measured performance metric through keep-or-revert attempts. |
| [refactor](skills/engineering/delivery/refactor/SKILL.md) | Improve code structure while preserving required behavior. |
| [release](skills/engineering/delivery/release/SKILL.md) | Prepare, execute, and verify an authorized release. |

#### [Investigation](skills/engineering/investigation)

| Skill | Description |
| --- | --- |
| [investigate](skills/engineering/investigation/investigate/SKILL.md) | Resolve a concrete unknown through inspection, research, or experiments. |
| [prototype](skills/engineering/investigation/prototype/SKILL.md) | Build an interactive demonstration to explore UI alternatives or logic before implementation. |
| [review-architecture](skills/engineering/investigation/review-architecture/SKILL.md) | Check code structure against the project's rules, summarize its modules, and prioritize evidence-backed improvements. |
| [review-product](skills/engineering/investigation/review-product/SKILL.md) | Evaluate product usefulness and recommend the next improvement or experiment. |

#### [Workflow](skills/engineering/workflow)

| Skill | Description |
| --- | --- |
| [deliver](skills/engineering/workflow/deliver/SKILL.md) | Coordinate a feature or backlog across tasks through its authorized delivery endpoint. |
| [queue-work](skills/engineering/workflow/queue-work/SKILL.md) | Keep discussing upcoming work items while background agents implement the agreed ones in parallel, in dependency order. |
| [create-verification](skills/engineering/workflow/create-verification/SKILL.md) | Create a tested, project-local skill and tool for driving the real application and capturing evidence. |
| [guide](skills/engineering/workflow/guide/SKILL.md) | Choose the next engineering activity or skill, with a concrete example invocation. |
| [improve-workflow](skills/engineering/workflow/improve-workflow/SKILL.md) | Improve the development process using evidence from completed work. |
| [maintain-skills](skills/engineering/workflow/maintain-skills/SKILL.md) | Review the skill collection and external sources for useful additions, improvements, consolidation, or retirement. |

## Credits and license

Some skills are based on [Matt Pocock's skills](https://github.com/mattpocock/skills) and [pstack](https://github.com/cursor/plugins/tree/main/pstack). [LICENSES.md](LICENSES.md) lists them with their licenses.

The skills are under the [MIT License](LICENSE).
