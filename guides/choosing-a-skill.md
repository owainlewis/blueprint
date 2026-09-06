# Choosing the right Blueprint skill

Blueprint has ten skills. You rarely need all of them for one change. Start with the result you need now.

## Document an implemented system

Use [`/architecture`](../skills/architecture/SKILL.md) to create or update root `ARCHITECTURE.md`. It checks claims against code, configuration, schemas, infrastructure, and tests. It documents what exists and does not propose new behavior.

Good requests:

- "Create ARCHITECTURE.md for this repository."
- "Update ARCHITECTURE.md after the new event pipeline shipped."
- "Bring the architecture document back in line with the current code."

If you only need a quick explanation, ask the agent directly. If you are deciding how a new system or feature should work, use `/design` instead.

## Decide what to build

Use [`/design`](../skills/design/SKILL.md) when a meaningful product or technical choice must be settled before coding. It produces a compact proposal with five parts:

1. Requirements: what to build, why it matters, and the scope.
2. User experience: actions, inputs, results, and failure or recovery from the user or caller's point of view.
3. Technical design and choices: how it works, which technologies it uses, and the reasons and tradeoffs.
4. Acceptance and proof: testable conditions paired with checks.
5. Open questions: unresolved decisions and whether they block work.

Routine features aim for 500 to 800 words. Larger or riskier changes get the detail needed to settle their decisions. Existing stack choices and conventions are referenced; additions and changes are explained. The skill stops with the proposed design ready for review.

Use [`/architecture-review`](../skills/architecture-review/SKILL.md) to challenge that proposal before implementation. This is useful when a wrong choice could affect data, security, compatibility, scale, performance, cost, or operations.

Use [`/plan`](../skills/plan/SKILL.md) after the important choices are settled and the work needs more than one agent run. It creates ordered, self-contained tasks. It does not write code.

Small, decided work does not need a design or plan. Send it directly to `/task-to-pr`.

## Deliver work

Use [`/task-to-pr`](../skills/task-to-pr/SKILL.md) for one or more tasks, tickets, pull requests, or a milestone. Each task gets its own branch, tests, independent review, and pull request. Pull requests remain open unless the user asks to merge them.

Use [`/codex-issue-coordinator`](../skills/codex-issue-coordinator/SKILL.md) for a large GitHub issue batch that needs visible Codex worker tasks. The coordinator orders dependencies and gives each active issue its own task, worktree, branch, and pull request.

The coordinator is intentionally Codex-specific. The other skills are portable instructions.

## Check and improve work

Use [`/test`](../skills/test/SKILL.md) to prove acceptance criteria and affected failure paths. Browser-facing changes must be checked in a real browser.

Use [`/review`](../skills/review/SKILL.md) for an independent implementation review by a fresh agent. It reports defects, meaningful risks, missing proof, and a verdict. It does not edit the change.

Use [`/improve`](../skills/improve/SKILL.md) to simplify existing code without changing its intended behavior. Tests must prove the behavior was preserved.

These skills can be called on their own. `/task-to-pr` also uses testing and review as part of delivery.

## Present a document

Use [`/html-doc`](../skills/html-doc/SKILL.md) to turn a complete Markdown product requirements document or technical design into a static HTML reading view. The Markdown stays authoritative. The skill changes presentation, not meaning.

## A quick rule

Ask what result you need next:

- A current root `ARCHITECTURE.md`: `/architecture`
- A decision about future behavior: `/design`
- A challenge to a proposal: `/architecture-review`
- Several ready tasks: `/plan`
- A pull request: `/task-to-pr`
- Proof: `/test`
- An independent verdict: `/review`
- Simpler code with the same behavior: `/improve`
- A readable HTML document: `/html-doc`
- Coordinated GitHub issue delivery in Codex: `/codex-issue-coordinator`
