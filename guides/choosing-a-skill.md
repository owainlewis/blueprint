# Choosing the right Blueprint skill

Most features start straight with `/spec`, then `/task-to-pr`. Root `ARCHITECTURE.md` and `REQUIREMENTS.md` are optional project-level documents—use them when a system benefits from a living architecture map or a separate product PRD. Choose additional skills when they improve decisions or proof.

| Result | Skill | Output |
|---|---|---|
| One feature or major change | [`/spec`](../skills/spec/SKILL.md) | `docs/<feature-slug>/spec.md`, or the supplied ticket |
| Project-level system design *(optional)* | [`/architecture`](../skills/architecture/SKILL.md) | Root `ARCHITECTURE.md` |
| Product-wide PRD *(optional)* | [`/requirements`](../skills/requirements/SKILL.md) | Root `REQUIREMENTS.md` |
| Independent technical proposal review | [`/architecture-review`](../skills/architecture-review/SKILL.md) | Findings and verdict |
| Several ready delivery tasks | [`/plan`](../skills/plan/SKILL.md) | Ordered slices in chat, or GitHub, Linear, or Jira tickets |
| High-quality pull request | [`/pr`](../skills/pr/SKILL.md) | PR with change shape, proof, and merge risk |
| Passing open pull requests | [`/task-to-pr`](../skills/task-to-pr/SKILL.md) | PRs with tests, `/pr`, independent review, CI, and repairs complete |
| Large GitHub issue batch in Codex | [`/codex-issue-coordinator`](../skills/codex-issue-coordinator/SKILL.md) | Visible workers and checked PRs |
| Acceptance proof | [`/test`](../skills/test/SKILL.md) | Pass, fail, or unverified evidence |
| Independent implementation review | [`/review`](../skills/review/SKILL.md) | Spec, correctness, and design findings plus verdict |
| Simpler code with the same behavior | [`/improve`](../skills/improve/SKILL.md) | Focused change and preservation proof |
| HTML reading view | [`/html-doc`](../skills/html-doc/SKILL.md) | Verified static HTML |

Blueprint workflows are opt-in. See [invocation and client support](../README.md#opt-in-by-design).

## System documents and feature specs

A feature spec stands on its own: it defines both what the feature must do and how to build and prove it. `ARCHITECTURE.md` is an optional project-level map of boundaries, data models, and invariants. `REQUIREMENTS.md` is an optional product-wide PRD when a team separates product requirements from feature specs. When those root documents exist, link to them from specs instead of repeating their rules.

A spec is the ticket, whether it is Markdown or a GitHub issue. Do not create a
second product spec, technical spec, or tracker item for the same definition.
One spec may produce several tasks and PRs. Small, decided work can use a task
description and checks without formal system documents or a feature spec.

## Delivery authority

`/task-to-pr` includes the full test, independent review, CI, and repair loop.
It leaves passing PRs open unless the user grants merge authority.

Ask `/task-to-pr` to merge ("and merge it") and it merges after all gates and
required approvals pass, with the same quality standard. Explicit
`/codex-issue-coordinator` use grants the same scoped authority for its supplied
batch. Automatic skill selection grants neither.

Neither merge workflow authorizes deployment or release publication. Report
missing decisions, approvals, or checks as blockers.
