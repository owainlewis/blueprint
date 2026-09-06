---
name: design
description: "Writes a proposed design covering requirements, user experience, technical choices, and proof. Use when important product or technical choices must be settled before coding. Use architecture to document an implemented system."
user-invocable: true
argument-hint: "<feature, problem, or brief>"
---

# Design

Decide what to build, why it matters, what the user experiences, and how it will work. Settle consequential choices so the implementing agent does not have to invent them.

## Process

1. Read the request, repository instructions, relevant code, and linked material. Reuse settled requirements and repository conventions.
2. Identify missing decisions that would change behavior, interfaces, data, security, operations, or proof. Ask blocking questions before drafting, with a recommended answer. Record non-blocking questions with a recommended default.
3. Write `docs/<feature-slug>/design.md` using the compact shape below. For a routine feature, aim for 500 to 800 words. Expand when a material decision or risk needs more explanation; completeness matters more than the word target.
4. Run the review pass once. Fix gaps supported by the available evidence and record unresolved decisions under Open questions.
5. Stop with a proposed design ready for review. Do not plan or implement it.

## Document shape

```markdown
# <Title>

> **Status:** Proposed for review

## 1. Requirements: what and why
Explain the problem, who has it, and the outcome they need. State the required capabilities, constraints, and what is out of scope. Make the value clear before introducing implementation details.

## 2. User experience
Describe the system as a black box: what the user does or supplies, what they see or receive, and what happens next. Walk through the main flow and relevant empty, invalid, denied, and failed outcomes, including recovery. For a CLI, API, or library, the user can be an operator or caller. Keep internal components and algorithms in the technical design.

## 3. Technical design and choices
Explain how the proposed change fits the existing system. Name the changed responsibilities, interfaces, and data. Record consequential technology choices with a reason and their main tradeoff. Add the relevant detail described below.

## 4. Acceptance and proof
Pair each testable condition with how it will be checked. Include affected failure paths and rules that must always hold. Reference earlier decisions instead of repeating their full definitions.

| ID | Done when | How to check |
|---|---|---|
| AC-1 | Observable condition | Exact command, automated scenario, or manual check |

## 5. Open questions
List unresolved decisions, the recommended answer, and whether they block planning or implementation. Write None when the design is settled.
```

## Technical detail

Include only the topics that require a decision for this change. Use short subsections when needed.

- **Technology choices:** language, framework, major dependencies, storage, and deployment. For a new project, choose the core stack. For an existing project, reference established choices and explain additions or changes. Pin versions when compatibility depends on them.
- **Structure and contracts:** changed component responsibilities and boundaries, APIs, commands, events, schemas, configuration, and migrations. Explain identifier creation and compatibility when stored names or IDs change.
- **Failure and recovery:** what can fail, resulting state, retries and their limits, and recovery. Cover startup, changes while work is running, and shutdown when they affect the outcome.
- **Security and operations:** trust boundaries, authorization, sensitive data, and relevant limits on scale, latency, connections, disk, memory, or cost. State what happens when an applicable limit is reached.

For each meaningful choice, state the decision, why it fits the requirements, and its main cost or limitation. Mention a rejected alternative only when the comparison explains the choice. Leave easily reversible local mechanics to the implementing agent.

## Writing rules

- Use plain words and define necessary terms. Do not use em dashes.
- Give each fact one home. Requirements explain the need; user experience describes observable behavior; technical design explains implementation. Acceptance checks reference these rather than creating another copy.
- Use prose for explanations, lists for parallel facts, and diagrams only when they clarify a relationship or flow.
- Keep current architecture distinct from proposed behavior. Link to `ARCHITECTURE.md` when it exists and reference shared conventions instead of restating them.
- Use `INV-n` for rules that need stable references across planning, implementation, and review. Map every invariant to proof in Acceptance and proof.
- Keep cited `AC-n` and `INV-n` IDs attached to the same rules. Never renumber or reuse them; assign additions the next unused ID.
- When updating an existing design, preserve linked section anchors. Do not restructure it merely to match this template.

## Review pass

Check four things before returning the design:

1. Can a new teammate explain what is changing, why, and the user experience without reading the technical design?
2. Could an implementing agent proceed without inventing a consequential product or technical decision? Are technology choices justified and compatible with the repository?
3. Are relevant failures, data changes, trust boundaries, and operational limits explicit, with enough detail to prevent an unsafe or incompatible implementation?
4. Does each acceptance criterion and invariant have concrete proof? Replace vague timing or alternative outcomes with one testable rule. Remove repeated background and sections that add no decisions.

## Return

Report the design path, main technical decision and tradeoff, any blocking question, and the review result. Keep the response short; the design contains the detail.
