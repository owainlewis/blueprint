---
name: spec
description: "Defines one feature or major change: required behavior, technical design, failure handling, and acceptance checks. Use when consequential decisions must be settled before delivery. The spec is the ticket."
user-invocable: true
argument-hint: "<feature, change, issue, or brief>"
---

# Spec

Write one implementation-ready specification for one coherent change.
The spec is the ticket: its source may be `docs/<feature-slug>/spec.md`, a GitHub
issue, or another user-supplied document. Update the supplied source; do not
create a duplicate ticket or document. Without a supplied source, use the
Markdown path above. Publish to a tracker only when asked.

## Process

1. Read the request, repository instructions, requirements, architecture, and relevant implementation. Reuse settled decisions and verify claims about current behavior.
2. Define the outcome and scope. Ask about unresolved choices that could change behavior, data, interfaces, security, compatibility, operations, cost, or proof. Leave reversible local mechanics to implementation.
3. Write the spec using the shape below. Explain the change from current behavior; link shared requirements and architecture instead of restating them.
4. Check that a fresh agent could implement it without inventing a consequential decision. Trace success, denial, invalid input, and partial failure where relevant.
5. Stop with the spec ready for review. Do not plan tasks or implement it.

## Spec shape

### Outcome and scope

State the problem, affected user or caller, desired result, constraints, and non-goals.

### Required behavior

Describe inputs, actions, observable results, permissions, business rules, and failure recovery. Reference applicable `REQ-n` IDs. Settle feature-specific product details here.

### Technical design

Explain changed responsibilities, interfaces, data, and execution order. Use concrete types, payloads, state tables, or diagrams when they remove ambiguity.

Cover schema changes, indexes, migrations, transaction boundaries, concurrency, retries, cancellation, security, compatibility, observability, rollout, and rollback only where they affect the change. State important choices, their reasons, and their costs.

Name any required change to system architecture. Do not silently override an accepted rule. Record the proposed architecture change for review before delivery.

### Acceptance and proof

Pair each observable condition and affected architectural rule with a check.

| ID | Done when | How to check |
|---|---|---|
| AC-1 | Concrete result | Command, automated scenario, or manual check |

Preserve existing `AC-n`, `REQ-n`, and `INV-n` references. Never reuse or renumber IDs. Do not invent executable commands for code that does not exist; define the scenario and expected result instead.

### Open decisions

State missing answers, recommended defaults when justified, and whether they block delivery. Write None when settled. Do not hide unknowns behind placeholders.

## Boundaries

One spec may lead to several tasks and pull requests. Use `/plan` when splitting helps delivery. Small, decided fixes can use their task description and checks without a formal spec. Do not require root documents for a local change that does not need them.

## Return

Report the source, main decision and tradeoff, and any blocking question.
