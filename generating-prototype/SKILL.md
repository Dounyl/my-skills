---
name: generating-prototype
description: Generates offline-first React visual prototypes from PRDs, Markdown requirements, plain-text product descriptions, or reference examples. Use when users ask for mobile or desktop page mockups, editable HTML prototypes, multi-page business flows, Dagre flow overviews, linked prototype pages, or review-note-enabled prototype deliverables.
---

# Generating Prototype

Generate visual prototype files, not a prose specification.

## Workflow

1. Inspect the PRD, description, and every supplied reference before drafting.
2. Reuse reference content, visual language, platform, and flow assumptions when they are clear. If no usable reference exists, ask only for missing information that materially changes pages, platform, flow, or visual direction; wait for the answers before generating.
3. Split the requirement into named businesses. Give every business its own `overview.html` and `pages/` directory.
4. Model each business as pages and directed transitions. Preserve decision branches, failure states, loops, and edge labels from the PRD.
5. Read [references/specification.md](references/specification.md), create the JSON input, and run `scripts/generate_prototype.py` rather than rebuilding the shell, editor, notes, or graph code.
   Use [examples/sample.json](examples/sample.json) only as a schema and component-pattern example; replace its product content and styling.
6. If local vendor files are unavailable, run `scripts/prepare_vendor.py` once. Generated output must use local React, ReactDOM, and Dagre files and remain usable without a network connection.
7. Open every generated overview and representative mobile and desktop pages. Verify layout, links, text editing, notes, save fallback, and reset behavior.
8. Apply [references/review-checklist.md](references/review-checklist.md) before delivery.

## Output Rules

- Render only the business selector when multiple businesses exist, each Dagre flow overview, the prototype pages, external product callouts when needed, and the compact editing toolbar.
- Do not add PRD summaries, page-purpose explanations, implementation notes, rule lists, or labels such as “this is an overview page.”
- Use phone frames for mobile pages and browser-window frames for desktop pages.
- Keep each business self-contained and portable. Link overview nodes to their page HTML and link page controls when the PRD defines navigation.
- Make visible prototype text editable, but do not expose visual-style editing.
- Support draggable editable notes. Persist drafts locally and embed text edits and notes into saved HTML so recipients can see them.
- Provide `保存` and `重置` actions with adjacent `!` controls. Show the detailed behavior only after the matching `!` is clicked.
- Save through the File System Access API when available. Otherwise download an updated HTML file; never claim silent self-overwrite is universally supported.
- Prefer close visual fidelity over generic dashboards. Derive colors, density, typography, and components from references or the requested product context.

## Commands

Prepare fixed local browser dependencies:

```bash
python3 scripts/prepare_vendor.py
```

Generate the prototype:

```bash
python3 scripts/generate_prototype.py requirements.json --output prototype-output
```

Validate without writing output:

```bash
python3 scripts/generate_prototype.py requirements.json --check
```

Use `--vendor-dir <path>` when dependencies are stored outside this skill.
