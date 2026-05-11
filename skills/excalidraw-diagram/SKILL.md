---
name: excalidraw-diagram
description: "Create an editable Excalidraw diagram from a repo, spec, architecture, workflow, concept, PR, or source material. Use when the user says \"make a diagram\", \"diagram this\", \"visualize this architecture\", or \"turn this into Excalidraw\"."
user-invocable: true
argument-hint: "<repo, spec, architecture, workflow, concept, PR, or source material>"
---

# Excalidraw Diagram

Create an editable Excalidraw diagram that helps a human understand an idea. A good diagram makes a claim; it does not merely list parts.

## Workflow

### 1. Understand

- Read the source material.
- Identify the audience, core claim, entities, relationships, flow, and what the reader should remember.
- For repo, PR, or architecture diagrams, inspect the relevant files before drawing.
- Ask one clarifying question with your recommended answer only if the missing answer would change the diagram.

### 2. Choose Shape

Pick the smallest visual shape that teaches the idea:

- before/after for change
- flow for sequence
- system map for components
- lifecycle for repeated stages
- dependency map for relationships
- concept model for mental models
- layered architecture for stacks

Split into multiple diagrams if one diagram would need unrelated ideas.

### 3. Draw

Use the official Excalidraw MCP when the client exposes it. Create or update an editable Excalidraw canvas there, then export or save a `.excalidraw` file if the tool supports it.

If the MCP is unavailable, write an editable `.excalidraw` file directly. Use the requested path; otherwise write `docs/<slug>.excalidraw` when `docs/` exists, or `<slug>.excalidraw` in the current directory.

Use clear hierarchy, aligned shapes, readable labels, and generous spacing. Keep the Excalidraw hand-drawn feel: few colors, consistent shape language, and no decorative clutter.

### 4. Verify

- Parse the `.excalidraw` file as JSON.
- Run a fast geometry pass before opening a browser:
  - text has visible top, bottom, and side padding inside every shape
  - labels do not touch borders, overflow shapes, or drift toward one edge
  - repeated cards use consistent dimensions, line heights, and internal spacing
  - elements do not overlap unless the overlap is intentional
- Use one visual pass at the end. Open the canvas, zoom out to inspect the whole diagram, then zoom into dense areas only if needed.
- Fix clipped labels, ambiguous arrows, unreadable scale, missing relationships, dense walls of nodes, and sloppy spacing before reporting success.

### 5. Report

Report the output path, Excalidraw MCP status, chosen diagram shape, core claim, and verification performed. Include a preview or share URL when available.

## Rules

- Explain, do not decorate.
- One diagram teaches one main idea.
- Use simple nouns and verbs in labels.
- Prefer fewer nodes with clearer relationships.
- Use grouping, arrows, and spatial position to carry meaning.
- Ground claims in the source material.
- Default to editable Excalidraw; use another format only when requested.
- Prefer the official Excalidraw MCP over unofficial CLIs when both are available.
- Keep verification fast: use JSON geometry for mechanical layout issues, then one browser pass for taste and readability.
- If validation fails, fix the file before reporting success.
