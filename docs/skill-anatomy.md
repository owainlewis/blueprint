# Skill Anatomy

Blueprint skills are workflows, not reference material. A skill should tell an agent how to do a repeatable piece of engineering work and when to stop.

## Density

Skills should be as short as they can be while remaining clear. The test for every line is: would removing this change agent behavior? If no, cut it.

Use `compress` whenever a skill starts to feel bloated. Compression preserves behavior, constraints, exact names, paths, commands, schemas, and examples that carry meaning.

## Frontmatter

Every skill has YAML frontmatter:

- `name`: the command and skill name.
- `description`: what the skill does and when it should be used.
- `user-invocable`: optional; defaults to true in most tools.
- `argument-hint`: optional; shows expected input.

## Sections

Use the smallest structure that makes the workflow clear.

- Role or intro: the stance the agent should take.
- Workflow: ordered actions that change behavior.
- Rules: constraints that apply throughout.

Avoid separate verification sections unless they add behavior not already covered by the workflow and rules.

## What Does Not Belong

- Anti-rationalization tables.
- Domain knowledge such as frontend, performance, or security references.
- Always-on rules; put those in `AGENTS.md` or tool-specific instructions.
- Decision trees the model can already handle.
- Multiple personas or per-stage agent swarms.
- Examples that restate the rule without teaching required format or edge-case behavior.

## Example

`skills/implement/SKILL.md` is the model: it has one role, a short ordered workflow, and a small rule set. It tells the agent to understand the task, make the smallest complete change, test it, verify it, and report.
