---
name: requirements
description: "Defines system product requirements: users, outcomes, capabilities, business rules, scope, and acceptance. Use for a new service or system, or a change to its product expectations."
user-invocable: true
argument-hint: "<system, brief, or REQUIREMENTS.md>"
disable-model-invocation: true
---

# Requirements

Use this skill only when the user explicitly selects it, or when an already selected Blueprint workflow requires its instructions. Do not select it from a general task match. For a required dependency, read its linked `SKILL.md` directly as part of the selected workflow; do not use a model-invoked skill command that the client blocks.

Create or update root `REQUIREMENTS.md`. Describe the product, what it does, and its key features. Keep this as a long-running product document.
Use `/spec` for one feature and `/architecture` for system technical decisions.

## Process

1. Read the request, repository instructions, existing requirements, and relevant evidence. Reuse decisions already made.
2. Identify the users, problem, desired outcome, scope, and constraints. Separate stated needs from assumptions. Inspect the repo for facts; ask the user for missing product decisions that could change the result.
3. Write the requirements using the shape below. Give each requirement a stable `REQ-n` ID. Never reuse or renumber existing IDs.
4. Check that the requirements agree, cover relevant failure behavior, and can be tested. Record unresolved decisions and whether they block architecture or delivery.
5. Stop with the document ready for human review. Do not design the implementation, plan tasks, or write code.

## Document shape

- **Purpose and users:** the problem, who has it, and the outcome they need.
- **User journey:** when several capabilities need connecting, show one realistic path from the problem to the desired result.
- **Evidence and assumptions:** link supplied research, feedback, or existing behavior that supports the problem. Label consequential assumptions and how to validate them. Do not invent evidence.
- **Key features and scope:** the main capabilities, their value, and explicit non-goals.
- **Requirements:** observable behavior, business rules, permissions, and user-visible failure and recovery. Define domain concepts when needed.
- **Constraints:** required compatibility, security, privacy, operational, and performance limits. Use measurable thresholds when known; mark unknown targets as open decisions.
- **Acceptance:** observable conditions for the system capabilities. Leave detailed feature scenarios and checks to its spec.
- **Success measures:** how to judge value after delivery, when evidence supports a measure. Keep these separate from implementation acceptance.
- **Open decisions:** each missing answer, recommended default when justified, and its effect on further work.

Use only sections that help define this product. Combine related points and omit sections that add no useful information.

Update this document when the product, key features, scope, or business rules change. Keep it current; preserve feature decision history in specs. Keep feature implementation detail in specs.

Keep implementation choices out of requirements. Include an imposed technology only as a stated constraint. Do not invent user research, targets, or business rules.

## Return

Report the path, decisions made, and any blocking question.
