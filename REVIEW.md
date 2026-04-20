# Review Concerns

This repo contains agent skills. When reviewing changes, prefer the simplest wording that still improves outcomes.

- Clear trigger: it should be obvious when a skill applies
- Clear boundary: it should be obvious when a skill does not apply
- Minimal instruction count: nothing should be included "just in case"
- Portable wording: avoid tying skills to one vendor, agent, or tool unless it is essential
- Real verification: checks should confirm outcomes, not ceremony
- No hidden assumptions: avoid requiring specific repo history, global tools, platforms, or unsupported features
- Simple language: assume agents are already smart and getting smarter
- Make the smallest safe change that fully solves the problem
- Preserve contracts or call out the migration clearly
- Handle failure paths explicitly instead of leaving them implicit
