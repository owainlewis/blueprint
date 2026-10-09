# Choosing the right Blueprint skill

Blueprint has twelve skills. New projects start with `/requirements` and `/architecture`, maintained as long-running documents. New features start with `/spec`, then `/task-to-pr` or `/factory`. Choose additional skills when they improve decisions or proof.

| Result | Skill | Output |
|---|---|---|
| System product needs | [`/requirements`](../skills/requirements/SKILL.md) | Root `REQUIREMENTS.md` |
| Intended system design and data model | [`/architecture`](../skills/architecture/SKILL.md) | Root `ARCHITECTURE.md` |
| One feature or major change | [`/spec`](../skills/spec/SKILL.md) | `docs/<feature-slug>/spec.md`, or the supplied source |
| Independent technical proposal review | [`/architecture-review`](../skills/architecture-review/SKILL.md) | Findings and verdict |
| Several ready delivery tasks | [`/plan`](../skills/plan/SKILL.md) | Tasks in chat; tracker tickets only when asked |
| Passing open pull requests | [`/task-to-pr`](../skills/task-to-pr/SKILL.md) | PRs with tests, independent review, CI, and repairs complete |
| Delivery through merge | [`/factory`](../skills/factory/SKILL.md) | Verified merges, or explicit blockers |
| Large GitHub issue batch in Codex | [`/codex-issue-coordinator`](../skills/codex-issue-coordinator/SKILL.md) | Visible workers and checked PRs |
| Acceptance proof | [`/test`](../skills/test/SKILL.md) | Pass, fail, or unverified evidence |
| Independent implementation review | [`/review`](../skills/review/SKILL.md) | Findings and verdict |
| Simpler code with the same behavior | [`/improve`](../skills/improve/SKILL.md) | Focused change and preservation proof |
| HTML reading view | [`/html-doc`](../skills/html-doc/SKILL.md) | Verified static HTML |

## Opt-in workflows

All twelve Blueprint skills require explicit selection. Name the skill in your request or use its command. An ordinary request such as “fix this bug” follows the agent's normal abilities and repository policy without automatically loading Blueprint.

Once selected, a workflow can load its required skills. For example, `/factory` uses `/task-to-pr`, which uses `/test` and `/review`. You do not need to invoke each step. The agent reads required dependencies directly from their linked `SKILL.md` files as workflow instructions, rather than invoking a blocked skill command. Reading dependencies does not expand scope or merge authority.

Codex uses `agents/openai.yaml` with `allow_implicit_invocation: false`. Claude Code uses `disable-model-invocation: true` in skill frontmatter. Other clients may not enforce these settings; the skill instructions also state the opt-in rule.

## System documents and feature specs

Requirements define what users need. Architecture defines how the whole system
should work. A feature spec defines one coherent change and its proof. Keep
shared rules in the root documents and link to them from specs.

A spec is the ticket, whether it is Markdown or a GitHub issue. Do not create a
second product spec, technical spec, or tracker item for the same definition.
One spec may produce several tasks and PRs. Small, decided work can use a task
description and checks without formal system documents or a feature spec.

## Delivery authority

`/task-to-pr` includes the full test, independent review, CI, and repair loop.
It leaves passing PRs open unless the user grants merge authority.

Explicit `/factory` use grants authority to merge its supplied work after all
gates and required approvals pass. It reuses `/task-to-pr`; it does not lower the
quality standard. Explicit `/codex-issue-coordinator` use grants the same scoped
authority for its supplied batch. Automatic skill selection grants neither.

Neither merge workflow authorizes deployment or release publication. Report
missing decisions, approvals, or checks as blockers.
