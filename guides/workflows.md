# Common Blueprint workflows

Blueprint is not a fixed sequence. Use the shortest path that gives the work enough thought and proof.

## A small, decided change

When the outcome is clear and one task can deliver it:

```text
task → /task-to-pr → tested and reviewed pull request
```

Example: add one validation rule with a known error message and acceptance test.

Do not write a design or plan just to create more process.

## A feature with important choices

When behavior, interfaces, data, security, or operations still need decisions:

```text
idea → /design → /architecture-review → /task-to-pr
```

If the reviewed design needs several independent agent runs, insert `/plan` before delivery.

The design owns the shared decisions. Each planned task owns one working result and its proof.

## Document an existing system

When a repository needs a durable, verified architecture document:

```text
existing code → /architecture → ARCHITECTURE.md
```

If that understanding leads to a proposed change, continue with `/design`, review, and delivery. Architecture records what the system does now. Design decides what should change. Keeping those documents separate prevents proposals from being mistaken for implemented behavior.

## A behavior-preserving cleanup

When the code works but is harder to understand than it needs to be:

```text
existing code → /improve → focused tests
```

Use `/task-to-pr` instead when the cleanup also changes behavior. Separate a large refactor when mixing it with product work would hide the real change.

## A large issue batch in Codex

When several GitHub issues have dependencies and need isolated coding sessions:

```text
issue batch → /codex-issue-coordinator → one Codex task and pull request per issue
```

The coordinator keeps the dependency view. Workers keep implementation details. Independent issues may run together. Dependent issues wait for their prerequisites.

Explicitly naming `/codex-issue-coordinator` grants its documented merge authority for that batch after every required gate passes. An implicit match does not.

## Testing or review on its own

`/test` and `/review` are useful outside the delivery workflow.

Use `/test` when you need acceptance criteria mapped to evidence for an existing branch, pull request, URL, or user flow. Use `/review` when you need a fresh agent to inspect a completed change without editing it.

## When to stop

Every Blueprint skill has a stopping point. Architecture stops with root `ARCHITECTURE.md`. Design stops with a proposal for review. Planning stops with tasks. Testing stops with explicit pass, fail, or unverified results. Delivery stops with checked pull requests unless merge authority was given.

That boundary matters. It keeps one skill from silently making decisions owned by another phase or by a person.
