# Review Concerns

This repository contains agent skills. Prefer the fewest instructions that reliably improve outcomes.

- **Clear trigger:** It is obvious when the skill applies.
- **Clear boundary:** It is obvious when the skill stops and what it does not do.
- **One transformation:** The input and output are clear. `build` may coordinate many tickets because it owns the full delivery phase.
- **Self-contained:** Runtime instructions, defaults, templates, checks, and stop rules live in the owning `SKILL.md`.
- **No hidden dependency:** A skill does not require root docs, another skill, a custom agent definition, or an unsupported tool.
- **Useful defaults:** Common work can proceed without repeating branch, commit, PR, test, or review policy.
- **Real verification:** Checks prove observable outcomes and important failure paths.
- **Portable wording:** Vendor or tool details appear only when the workflow requires them.
- **Simple language:** Remove ceremony, repetition, vague advice, and rules that do not change behavior.
- **Complete failure paths:** State when to stop, resume, or ask for a human decision.
- **Smallest complete change:** Preserve existing behavior and interfaces unless migration is explicit.

Review the five skills as a set. Look for gaps, overlap, contradictory defaults, and stale references to removed workflows.
