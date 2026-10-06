# Review Blueprint

Read the request, complete diff, relevant skills, and rendered public docs.
Use [AGENTS.md](AGENTS.md) for repository policy. Review the changed workflow
against its skill rather than copying every skill rule into this checklist.

## Check the instructions

- Can a new teammate tell when the skill applies, what it produces, and when it stops?
- Does it own one phase or delivery outcome without duplicating another skill?
- Are commands, paths, conditions, and effects concrete and consistent?
- Can the agent choose local mechanics without inventing product or technical decisions?
- Are authority, dependencies, failure handling, and required proof clear?

Walk representative requests through changed instructions, including a failure
or missing-input case. Report the exact conflicting steps or missing decision,
not a general claim that the skill is unclear.

## Check the documents

- Do requirements, architecture, and feature specs keep their agreed scopes?
- Do examples follow the current workflow and distinguish proposals from implemented behavior?
- Do guides and migration instructions agree with the skills?
- Does the rendered Markdown keep readable headings, lists, tables, and links?

## Check the proof

Run the relevant repository checks. Separate automated validation, instruction
walkthroughs, and real agent execution. None is a substitute for the others.

Follow the writing rules in `AGENTS.md`. Cut repetition and instructions that
add no decision or proof. Treat broken boundaries, duplicate workflows, and
unsupported claims as findings. Do not block on personal taste.
