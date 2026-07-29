---
name: design
description: "Writes a proposed specification for a feature or part of a system, including its executive summary, context, system fit, behavior, boundaries, decisions, invariants, requirements, interfaces, data, failures, constraints, risks, acceptance criteria, and proof. Use when the user asks to design or architect a change, write a spec or design doc, define requirements, or resolve important product or technical decisions before implementation. Do not use to document the current architecture of an implemented system; use the architecture skill instead."
user-invocable: true
argument-hint: "<feature, problem, or brief>"
---

# Design

## Workflow

1. Read the request, repository instructions, relevant code, and linked material.
2. Resolve choices that would change behavior, interfaces, data, errors, security, operations, or tests. Ask only questions whose answers materially change the design. Recommend an answer when asking.
3. Write `docs/<feature-slug>/design.md` using the numbered shape below. Keep it short, preserve the logical order, and omit only sections that genuinely do not apply.
4. Run the review pass. Fix what you can. List the rest under Open questions.
5. Stop for human review. Do not plan or implement.

## Document shape

```markdown
# <Title>

> **Status:** Proposed for review

## 1. Executive summary
In two or three short paragraphs, explain the problem, who it affects, the outcome, the proposed approach, and the most important tradeoff. A reviewer should understand the decision before reading the detail.

## 2. Context and scope
Describe the current behavior, why it is insufficient, what changes once this ships, and the boundary of this design.

## 3. System context
Show where the change fits in the existing architecture, which components and external systems it touches, and which boundaries it must preserve. Include a small diagram when the relationships are easier to understand visually.

## 4. Proposed design

### How it works
Walk one real case from start to finish. Name the thing that arrives, what handles it, what gets written down, and what the user sees.

### Components and responsibilities
For each changed component, state what it owns, what it depends on, and what it deliberately does not own.

### Decisions
For each choice that could reasonably have gone another way: what you chose, what you rejected, and what it costs. One short paragraph each. Skip choices nobody would argue about.

## 5. Invariants and requirements

### Invariants
Numbered statements that must hold at all times. These are what a reviewer checks a diff against, so keep them short and testable.

### Requirements
- Observable behavior and constraints.

## 6. Interfaces and data
APIs, commands, events, schemas, config, compatibility, or migration.

### Naming and identity
How every durable name or ID is derived, what happens when derivation fails, and what happens if the source of the name changes after state exists.

## 7. Failure behavior and lifecycle
What can fail, what state it moves to, whether it retries and how, and how it recovers. Cover startup, config or state changes, work in flight, shutdown, and what happens when everything fails at once.

## 8. Security, privacy, and operations
State the trust boundary, authorization checks, sensitive data handling, and operational impact. Cover anything shared and finite such as rate limits, connections, disk, memory, or cost, and say what happens when it runs out.

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

- Prose is the default. Use bullets only for content that is genuinely a list, such as config fields, acceptance criteria, risks, and out of scope.
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

1. **Executive summary.** Does it state the problem, outcome, approach, and decisive tradeoff without requiring the rest of the document?
2. **Architecture fit.** Does the design show the current system boundary, the boundary being changed, and the owner of each new responsibility?
3. **Names and identity.** Where does every durable identifier come from? What happens when it is missing, ambiguous, or changes after state exists?
4. **Failure and recovery.** What creates a bad state? Does the system retry, with what backoff, and can it recover without a restart? What happens when everything is bad at startup?
5. **Security and privacy.** Where is identity established, authorization enforced, untrusted input validated, and sensitive data exposed or retained?
6. **Shared resources.** What finite resource does the feature consume? State the budget and the behavior at the limit.
7. **Timing and fairness.** Replace words such as "eventually" and "will not starve" with a bound someone can test.
8. **Lifecycle.** Cover config reload, enable and disable behavior, work already in flight, and shutdown.
9. **Undefined terms.** Define words that carry a specific meaning in the design.
10. **Either/or acceptance criteria.** Do not allow both sides of "recovers or retains" to pass. Choose one observable behavior.

Put anything you cannot resolve under Open questions and state whether it blocks task breakdown.
