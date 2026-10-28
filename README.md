# Agent Skills

These are the skills I use every day with Claude Code and Codex. Most of them cover software engineering, from shaping a feature through design, implementation, review, and release. The rest help with conversations, documentation, and learning.

The skills are written to work together. Each one does one job and names the skill to use next when the work calls for it. I maintain them with [maintain-skills](skills/engineering/workflow/maintain-skills/SKILL.md), which compares them with other skill collections and runs routing tests, realistic requests that check a fresh agent loads the right skill.

## Installation

I don't install the skills by hand. [Archon](https://github.com/mrzli/archon), my workstation setup, clones this repository and links the skills for both agents every time its setup script runs.

To install them manually, clone the repository and run the sync script with `--user`. It links each skill into the directories the agents read, `~/.claude/skills` for Claude Code and `~/.agents/skills` for Codex:

```bash
git clone https://github.com/mrzli/skills.git
cd skills
bash scripts/sync-skills.sh --user
```

To update, run `git pull` and the script again. The script links new skills, removes links to skills that were deleted, and leaves other skills in those directories alone. It stops without changing anything if a skill of the same name is already installed from elsewhere.

Without `--user`, the script links the skills only into this repository's own `.claude/skills` and `.agents/skills`. An agent started in this repository then finds them without a user-wide installation, which is a way to try them out.

## Getting started

Ask the agent what to do next, and [guide](skills/engineering/workflow/guide/SKILL.md) picks the engineering skill that fits. The agent loads the other skills on its own when a request matches them.

[spawn](skills/conversation/spawn/SKILL.md) opens a fork of the conversation in a new tab and needs Claude Code running in herdr or tmux. [yield](skills/conversation/yield/SKILL.md) and [collect](skills/conversation/collect/SKILL.md) pass notes between those forks. [warmup](skills/conversation/warmup/SKILL.md) reads Claude Code and Codex session files from their default locations.

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
