# Common Blueprint workflows

Use the shortest path that gives the work enough decisions and proof.

## Opt-in workflows

All twelve Blueprint skills require explicit selection. Name the skill in your request or use its command. An ordinary request such as “fix this bug” follows the agent's normal abilities and repository policy without automatically loading Blueprint.

Once selected, a workflow can load its required skills. For example, `/factory` uses `/task-to-pr`, which uses `/test` and `/review`. You do not need to invoke each step. The agent reads required dependencies directly from their linked `SKILL.md` files as workflow instructions, rather than invoking a blocked skill command. Reading dependencies does not expand scope or merge authority.

Codex uses `agents/openai.yaml` with `allow_implicit_invocation: false`. Claude Code uses `disable-model-invocation: true` in skill frontmatter. Other clients may not enforce these settings; the skill instructions also state the opt-in rule.

## A new project

```text
/requirements + /architecture → long-running system documents
```

`REQUIREMENTS.md` describes the product, what it does at a high level, and its key
features. `ARCHITECTURE.md` describes the intended technical design and data
model. Refine them together and maintain them as the project changes. State
which parts of the intended architecture are implemented. Include relevant user
journeys, supporting evidence, alternatives, operating expectations, and migration
constraints. Omit sections that add no useful information.

Use `/architecture-review` before implementation when a wrong technical choice
could materially affect users, data, security, compatibility, operations, or
proof. The review does not replace product approval.

## A new feature or major change

```text
/spec → /task-to-pr or /factory
```

The spec is the ticket. It references the long-running system documents,
defines the feature's behavior and technical design, and pairs acceptance with
checks. `/task-to-pr` makes the code changes and leaves a passing PR open.
Explicit `/factory` use makes the code changes through the same quality loop,
then merges after all gates pass.

Use `/architecture-review` for consequential technical choices. Use `/plan` if
the spec needs several delivery tasks. Neither is a mandatory step for every
feature. One spec can produce several PRs. Update shared documents when the
feature changes their rules; do not repeat them in each spec. After delivery,
retain the spec as decision history with its delivery status, PR links, and proof.
Requirements and architecture stay current.

## A small, decided change

```text
task and checks → /task-to-pr → passing open PR
```

Do not write a spec or plan just to add process.

## Delivery through merge

```text
spec or decided task → explicit /factory → /task-to-pr quality loop → gated merge
```

Both delivery paths implement, test, independently review, pass CI, and repair
valid findings. `/factory` adds merging after required approvals and merge gates
pass. If a gate needs human action, leave the PR open and report the blocker.

## A large issue batch in Codex

```text
issue batch → /codex-issue-coordinator → visible workers and checked PRs
```

Independent issues may run together. Dependent issues wait for prerequisite
merges. Explicit invocation grants merge authority only for the supplied batch;
an implicit match leaves passing PRs open.

## Improvement, testing, and review

Use `/improve` for a behavior-preserving cleanup. Use `/test` to prove acceptance
and failure paths, including real-browser checks for browser behavior. Use
`/review` for a fresh agent's read-only implementation review.

## Stop conditions

Requirements, architecture, and spec stop with documents ready for review.
Planning stops with tasks. Testing reports evidence. Review reports findings
and a verdict. Delivery stops with passing open PRs or verified merges according
to the user's authority. Return to the source when implementation reveals a
wrong requirement or design.
