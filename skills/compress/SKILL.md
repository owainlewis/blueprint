---
name: compress
description: "Compress agent-facing instructions to the fewest words that preserve behavior, constraints, and clarity."
user-invocable: true
argument-hint: "<file path or pasted instruction>"
---

# Compress

## When to use

- Compressing specs, plans, tickets, prompts, `AGENTS.md`, or skill files
- Removing redundancy from instructions before giving them to an agent
- Tightening a document that has grown through repeated edits

## Process

1. Choose the target from `$ARGUMENTS`, a pasted instruction, or the named file.
2. Preserve the target's behavior exactly. Compression is not permission to weaken rules.
3. Cut:
   - restated rules
   - overlapping instructions
   - padding phrases
   - obvious preamble
   - hedging that does not change behavior
   - examples that restate a rule without adding format or edge-case value
4. Keep:
   - actual rules and constraints
   - concrete examples that show a required format or edge case
   - file paths, exact names, identifiers, commands, and schemas
   - instructions that came from previous failures
5. If asked to update a file, replace it with the compressed version. Otherwise return only the compressed instruction.

## Verification

- Meaning and behavioral constraints are preserved
- Redundant wording is removed
- Specific names, paths, commands, schemas, and examples still exist where needed
- The result is easier for an agent to follow

## Rules

- Return the compressed version only unless the user asks for commentary.
- Prefer bullets for lists of rules.
- Prefer prose for a single connected idea.
- Merge overlapping sections.
- State a general rule and its exception together.
- Do not drop a rule to hit a word count.
- If compression changes likely agent behavior, restore the load-bearing instruction.
