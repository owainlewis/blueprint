---
name: design
description: "Writes a clear spec for a proposed feature or system change. Use when important product or technical choices must be settled before coding. Covers behavior, interfaces, failures, risks, acceptance criteria, and tests. Use architecture to explain the current system."
user-invocable: true
argument-hint: "<feature, problem, or brief>"
---

# Design

## Workflow

1. Read the request, repository instructions, relevant code, and linked material.
2. Resolve choices that would change behavior, interfaces, data, errors, security, operations, or tests.
3. Ask only questions whose answers would change the design. Recommend an answer when asking.
4. Write `docs/<feature-slug>/design.md` using the numbered shape below. Keep it short and in order. Omit only sections that do not apply.
5. Run the review pass. Fix what you can. List the rest under Open questions.
6. Stop with the proposed design ready for review. Do not plan or implement it.

## Document shape

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
- Question, and whether it blocks starting work.

## 13. Out of scope
- Related work this design does not include.
```

## Writing rules

- Start with the simplest useful explanation. Write for a new teammate, not someone who already knows the project.
- Prose is the default. Use bullets only for real lists, such as config fields, acceptance criteria, risks, and out of scope.
- A bullet cannot carry a decision by itself. Write the reason next to it in a sentence.
- Use plain words. Say "the process crashed" instead of "an availability event occurred". Prefer short sentences.
- Define a term the first time you use it, or do not use it.
- Keep current architecture and proposed behavior distinct. Link to `ARCHITECTURE.md` when it exists and say exactly which current boundary changes.
- Give each changed component a positive and negative boundary: what it owns and what it does not own.
- Use numbered top-level sections so reviewers can refer to stable parts of the specification.
- Use diagrams only when they make system context, dependency direction, data flow, or lifecycle materially clearer.
- Prefer one clear recommendation over a list of options.
- Record rejected options only when the tradeoff matters later.
- Do not repeat the same fact in several sections with different wording.
- Do not use em dashes.

## Review pass

Reread the draft once and check each category. Fix any gap you can resolve from the available evidence.

1. **Executive summary.** Can a new teammate understand the problem, outcome, approach, and main downside without reading the rest of the document?
2. **Architecture fit.** Does the design show the current system boundary, the boundary being changed, and the owner of each new responsibility?
3. **Names and identity.** Where does every stored identifier come from? What happens when it is missing, unclear, or changes after data exists?
4. **Failure and recovery.** What creates a bad state? Does the system retry, how long does it wait between attempts, and can it recover without a restart? What happens when everything is bad at startup?
5. **Security and privacy.** Where is identity established, authorization enforced, untrusted input validated, and sensitive data exposed or retained?
6. **Shared resources.** What limited resource does the feature use? State the budget and what happens at the limit.
7. **Timing and fairness.** Replace words such as "eventually" and "will not starve" with a bound someone can test.
8. **Lifecycle.** Cover config reload, enable and disable behavior, work already in flight, and shutdown.
9. **Undefined terms.** Define words that carry a specific meaning in the design.
10. **Either/or acceptance criteria.** Do not allow both sides of "recovers or retains" to pass. Choose one observable behavior.

Put anything you cannot resolve under Open questions and state whether it blocks task breakdown.
