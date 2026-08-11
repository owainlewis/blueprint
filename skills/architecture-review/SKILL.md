---
name: architecture-review
description: "Reviews a technical proposal before implementation. Use for designs, RFCs, ADRs, architecture proposals, and issues that define how a system change should work. Finds material ambiguity and flaws in correctness, scalability, performance, security, operations, and proof."
user-invocable: true
argument-hint: "[technical proposal, design, RFC, ADR, or issue]"
---

# Architecture Review

Review a technical proposal before implementation. It may describe a large
system change or a small implementation-level design. Review the proposed
choices, not the document type or size.

Use one fresh subagent that did not write the proposal. Give it the complete
review context and tell it to review directly without delegating. If you are
that reviewer, review directly. Stay read-only.

If fresh subagents are unavailable, stop and report that independent review is blocked unless the user explicitly accepts a documented self-review.

## Workflow

1. Read the goal, proposal, repository instructions, relevant current code,
   tests, schemas, configuration, and linked material. Treat claims about the
   current system as unverified until code, tests, schemas, configuration,
   infrastructure, or relevant runtime evidence supports them.
2. State the problem, affected user, intended outcome, success measure, scope,
   constraints, and main tradeoff. Report any that the proposal leaves unclear.
3. Trace one real case from input to observable outcome. Include ownership,
   validation, state changes, side effects, response timing, failure, retry,
   cleanup, and what the user sees where they matter.
4. Challenge the chosen design with the review focus below. Look for a simpler
   choice that reaches the same outcome and proof with less state, coupling,
   duplication, or operational work.
5. Surface material open questions. Recommend an answer when evidence supports
   one. Do not invent questions that cannot change the design.
6. Return findings, open questions, a short assessment, and one verdict. Do not
   rewrite the proposal, plan the work, review implementation code, or implement
   changes.

## Review focus

- Check fit with the current system, ownership, boundaries, interfaces, data,
  compatibility, migration, rollout, and rollback.
- Trace partial failure, retry, cancellation, concurrency, startup, shutdown,
  and recovery where they affect the proposal.
- Check claimed scale, limited resources, latency, throughput, storage, cost,
  dependency failure, and operator recovery only where they can change the choice.
- Check identity, authorization, untrusted input, credentials, destructive
  authority, and sensitive data handling.
- Require observable acceptance criteria and proof for important rules and
  failure paths. Do not let implementation invent user-visible behavior,
  interfaces, data rules, security policy, or failure behavior.

## Material questions

Report an open question only when two capable implementations could answer it
differently in a way that affects users, data, interfaces, security, scale,
performance, operations, cost, compatibility, or proof.

- **Blocking:** implementation should not start without the answer.
- **Important:** the proposal should record the answer, but the reviewer can
  recommend a safe default from available evidence.

Omit questions that are stylistic, safely local to implementation, outside the
stated scope, or speculative beyond the scale the proposal claims to support.

## Findings

Report only flaws that can change the design or its safety:

- **Blocker:** the choice is unsafe, contradicts the goal or current system, or
  cannot recover from an important failure.
- **Important:** the proposal permits materially different implementations or
  leaves a meaningful risk in behavior, scale, performance, security,
  operations, compatibility, or proof.

For each finding or open question include its location, concrete failure or
ambiguity, impact, evidence, and the smallest correction or recommended answer.
Report unclear wording when it prevents a new teammate from explaining,
evaluating, or implementing the design. Omit other writing preferences.

## Verdict

- `Approve`: no blocker or important findings or open questions remain.
- `Request changes`: the proposal has a fixable blocker or important finding or
  open question.
- `Blocked`: the review lacks required context, repository evidence, specialist
  coverage, or an independent reviewer.

State what remains unverified. Do not approve because the document is detailed
or because every template section exists.
