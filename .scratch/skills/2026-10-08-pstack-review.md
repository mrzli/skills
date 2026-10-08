# pstack source review, 2026-10-08

First review of [pstack](https://github.com/cursor/plugins/tree/ccb5507cec1546dc88135c1139c811e6c59115ba/pstack) at `cursor/plugins` `ccb5507` (2026-10-07). pstack is MIT licensed, © 2026 Lauren Tan. Any adapted text needs her notice added to `LICENSES.md`. This review produced recommendations only. The only change is adding pstack to [sources.md](../../skills/engineering/workflow/maintain-skills/references/sources.md).

## Scope and method

The local baseline was `7f39dae`, with 29 skills. Three parallel read-only agents compared upstream clusters with their local counterparts. Each read both sides in full. The compared items were:

- **Routing and workflow:** `poteto-mode` and all 23 playbooks, `poteto-help`, `figure-it-out`, `show-me-your-work`, `recall`, `reflect`, `correct`, `automate-me`, `arena`, `swarm`, and `docs/guide`.
- **Principles and checks:** all 24 `principle-*` skills, `benchmark-checklist`, `blast-radius`, `tdd`, `no-comments`, `typescript-best-practices`, `create-verification-skill`, `maintain-verification-skill`, and `make-bot-ui`.
- **Explanation and writing:** `how`, `why`, `bro`, `teach`, `interrogate`, `architect`, `unslop`, `technical-writing`, and `poteto-agent`.

I verified the main local finding, the compatibility defaults in `refactor` and `plan`, directly. `automations/benny`, `setup-pstack`, and the scripts were not audited.

## Context that limits adoption

pstack targets Cursor with multi-model panels (Grok and Opus), cloud workers, stacked GitHub PRs, and a dispatcher. `poteto-mode` reads the principle index at the start of each task, and every principle has `disable-model-invocation: true`. Without that dispatcher, separate principle skills would go unused. This user works solo in Claude Code and Codex, on local branches with merges on request. The main recorded problem is agents skipping skills, so adding many skills would work against it.

## Recommendations

| # | Change | Evidence | Kind |
| --- | --- | --- | --- |
| 1 | **No legacy compatibility by default.** `refactor` and `plan` currently default to "introduce a compatible form, migrate consumers, and remove the old form". Change them, plus `implement` and `design`, so that when every consumer is in the repository, the agent migrates all callers and deletes the old form in the same change. Shims and fallbacks need external consumers, persisted data, or a user request, and the reason must be stated. | archon Codex 10-05: "don't have legacy compatibility". Upstream `principle-migrate-callers-then-delete-legacy-apis` and `playbooks/refactoring.md`. | Observed. The local wording causes it. |
| 2 | **Code-grounded `clarify`.** Read the code before explaining it, and cite the file and symbol for each step. Name links that could not be traced. When dictation may have garbled the question, restate the reading in one line first. Widen the description to "how code works" and plain-word "clarify". | qt Codex 10-05: "explain to me exactly how our code currently works so I can check it… you are not hallucinating". Upstream `how/references/explorer-prompt.md`. | Observed |
| 3 | **New `optimize` skill** for iterative performance work. Freeze a measurement that has been shown to detect the slow case. Make one change per attempt, then keep or revert it. Report the median of N runs with alternating sides. Confirm that GPU work finished inside the timed region, and measure release builds. Log each attempt. `fix-bug` links to it for performance regressions. | qt-market-chart frame-time and GPU line work. No local skill owns it. Upstream `perf-issue`, `hillclimb`, `trace-forensics`, `benchmark-checklist`, and `principle-explain-the-number`. | Relevant activity. No measurement failure observed yet. Trial. |
| 4 | **Close calls in `guide`.** An interface or data shape goes to `design`, user-visible behavior to `shape-feature`, and stress-testing a proposal to `interrogate`. Status goes to `recap` and continuation to `handoff`. | qt Codex 10-05: four skills in five minutes. Upstream `poteto-help`. | Observed once |
| 5 | **AI-tells checklist in `writing-text`,** used by the final check. It covers -ing tails, inflated vocabulary, "serves as", forced triplets, synonym cycling, bold label lines, chatbot openers and closers, framing labels, abstract metaphor nouns, and dropped articles. It also adds one name per thing and clear referents. | Past failures to apply writing guidance. Upstream `unslop` and `technical-writing`. | Hypothesis. Cheap. |
| 6 | **Routing tests in `maintain-skills`.** Give a fresh subagent a realistic prompt that does not name the skill. Grade which `SKILL.md` it actually read. | Agents skipping skills. Upstream `playbooks/eval.md`. | Measures a known problem |

## Smaller candidates

These are one sentence each. Apply them alongside a related change, or skip them.

- `fix-bug`: when evidence refutes a hypothesis, revert the changes it motivated. Source: `bug-fix.md`.
- `refactor`: spot-check renames for strings, prose, and back-references. Source: `refactoring.md`.
- `review-code`: name the fact a risky change's safety depends on and how it was established. A test that would pass if the code returned nothing verifies nothing. Source: `blast-radius` and `principle-test-behavior-not-implementation`.
- `design`: write two or three call sites before the types. Reject designs with two ways to do one task, hand-synced lists, importable internals, or state with more than one writer. `implement` reports deviations from the agreed design. Source: `architect`.
- `improve-workflow`: fix a recurring mistake at the highest workable level, in this order: architecture, types, lint, test, docs. Prove the check catches a real past case. Source: `correct`.
- `implement`: when verification setup fails, suspect the observation method first. Source: `principle-prove-it-works`.

## Outside this collection

- **qt-market-chart:** a project-local verification skill covering the Xvfb launch, a doctor check, screenshots, and teardown. Run it once end to end before keeping it. The idea comes from `create-verification-skill`.
- **archon:** take TypeScript conventions from `typescript-best-practices` into that project's AGENTS.md if wanted.

## Declined

- Multi-model, cloud, or PR-stack mechanics: babysit, shipping, opening-a-pr, autopilot-*, orchestrate, multi-phase-plan, worktree-cleanup, arena, swarm, reflect, upstream `interrogate`, and eval's blinded panels.
- Separate principle skills. The useful principles are folded in above, and the rest are already covered inline.
- Already covered: `figure-it-out` and autonomous-run (`deliver-feature`), session-pickup and pause-safely (`handoff`), `recall` (`recap`), `bro` (`clarify`), and `tdd` (an opt-in gate the user rejected before).
- `why` needs MCPs and adds little on solo projects. `show-me-your-work` and `automate-me` are covered by the progress record and AGENTS.md. `no-comments`, `make-bot-ui`, `poteto-agent`, and `maintain-verification-skill` were also declined.

## Next review

Start from `cursor/plugins` `ccb5507` and diff `pstack/` only.
