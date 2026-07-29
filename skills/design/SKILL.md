---
name: design
description: "Writes a clear spec for a proposed feature or system change. Use when important product or technical choices must be settled before coding. Covers behavior, interfaces, failures, risks, acceptance criteria, and tests. Use architecture to explain the current system."
user-invocable: true
argument-hint: "<feature, problem, or brief>"
---

# Design

Write a spec for a proposed feature or system change.

## Workflow

1. **Read**
   - Read the request, repository instructions, relevant code, current architecture, and linked material.

2. **Decide**
   - Resolve choices that change behavior, interfaces, data, errors, security, operations, or tests.
   - Ask only questions whose answers would change the design.
   - Recommend one answer when asking.

3. **Write**
   - Write `docs/<feature-slug>/design.md` using the template below.
   - Keep sections short and in order.
   - Omit only sections that do not apply.

4. **Review**
   - Check that a new teammate can understand the problem, outcome, approach, and main downside from the executive summary.
   - Check the current boundary, the boundary being changed, and the owner of each new responsibility.
   - Check where every stored name and identifier comes from, and what happens when it is missing or later changes.
   - Check failure, retry timing, recovery without restart, config and enable or disable changes, work in flight, and shutdown.
   - Check what happens when every dependency is unavailable at startup.
   - Check identity, authorization, untrusted input, sensitive data, limited resources, and behavior at each limit.
   - Replace words such as "eventually" and "will not starve" with a bound that can be tested.
   - Make every acceptance criterion choose one observable result.
   - Fix gaps supported by current evidence. Put the rest under Open questions and say whether each one blocks task breakdown.

5. **Stop**
   - Return the design for human review.
   - Do not plan or implement.

## Document template

```markdown
# <Title>

> **Status:** Proposed for review

## 1. Executive summary
Say what is wrong today, who feels the problem, what will change, how we plan to fix it, and the main downside. Use simple words. Do not list sections or implementation details.

## 2. Context and scope
Describe the current behavior, why it is insufficient, what changes once this ships, and the boundary of this design.

## 3. System context
Show where the change fits in the current system. Name the parts and outside systems it touches and the boundaries it must preserve. Include a small diagram when it makes those relationships clearer.

## 4. Proposed design

### How it works
Walk one real case from start to finish. Name the thing that arrives, what handles it, what gets written down, and what the user sees.

### Components and responsibilities
For each changed part, state what it owns, what it depends on, and what it does not own.

### Decisions
For each real choice, say what you chose, what you rejected, and what the choice costs. Use one short paragraph. Skip choices nobody would question.

## 5. Invariants and requirements

### Invariants
List numbered rules that must always hold. A reviewer checks the code against these rules, so keep them short and testable.

### Requirements
- Observable behavior and constraints.

## 6. Interfaces and data
APIs, commands, events, schemas, config, compatibility, or migration.

### Naming and identity
How every stored name or ID is created, what happens when that fails, and what happens if its source changes after data exists.

## 7. Failure behavior and lifecycle
Say what can fail, what state follows, whether the system retries, and how it recovers. Cover startup, config or state changes, work in flight, shutdown, and what happens when several things fail together.

## 8. Security, privacy, and operations
State the trust boundary, authorization checks, sensitive data handling, and operational impact. Name shared limits such as rate limits, connections, disk, memory, or cost. Say what happens at each limit.

## 9. Acceptance criteria
- Testable conditions that prove the work is complete.

## 10. Test approach
How each invariant and each important requirement will be proved.

## 11. Risks and tradeoffs
- Risk and mitigation.

## 12. Open questions
- Question, and whether it blocks task breakdown.

## 13. Out of scope
- Related work this design does not include.
```

## Rules

- Write for a new teammate. Start with the simplest useful explanation.
- Prose is the default. Use bullets only for real lists, such as config fields, acceptance criteria, risks, and out of scope.
- Put the reason for a decision in a sentence, not a bare bullet.
- Use plain words and short sentences. Say "the process crashed" instead of "an availability event occurred".
- Define a term the first time you use it, or do not use it.
- Keep current architecture and proposed behavior distinct. Link to `ARCHITECTURE.md` when it exists and say exactly which current boundary changes.
- Give each changed component a positive and negative boundary: what it owns and what it does not own.
- Use numbered top-level sections so reviewers can refer to stable parts of the specification.
- Use diagrams only when they make system context, dependency direction, data flow, or lifecycle materially clearer.
- Prefer one clear recommendation over a list of options.
- Record rejected options only when the tradeoff matters later.
- Do not repeat the same fact in several sections with different wording.
- Do not use em dashes.
