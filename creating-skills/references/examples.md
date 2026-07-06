# Examples

Use these examples as patterns, not copy-paste law.

## Better Skill Name

Prefer:

- `creating-skills`
- `reviewing-prs`
- `drafting-prds`

Avoid:

- `skill`
- `helper`
- `tooling-for-various-things`

## Better Description

Weak:

```yaml
description: Help create skills.
```

Stronger:

```yaml
description: Creates, replaces, and improves skills. Use when the user asks to build a new skill, rewrite an existing skill, optimize triggering metadata, split a large SKILL.md into references, add reusable scripts or assets, or review a skill against skill best practices.
```

## Lean Main File Pattern

```text
SKILL.md
references/
  checklist.md
  examples.md
  interface-metadata.md
agents/
  openai.yaml
```

Use this pattern when the skill needs a short core workflow plus supporting material and optional interface metadata.

## Resource Decision Examples

- Add a script when the same parsing, conversion, or validation logic would be rewritten repeatedly.
- Add a reference when the model needs a schema, policy, or provider-specific guide on demand.
- Add an asset when outputs should reuse a template, icon, or boilerplate project.
- Skip extra folders when the skill works well with a single `SKILL.md`.

## Replacement Pattern

When replacing an older skill:

1. Read the current skill fully.
2. Keep successful triggers and useful examples.
3. Remove duplicated explanations.
4. Move bulky detail into `references/`.
5. Replace hardcoded local assumptions with conditional instructions.
6. Re-test with realistic prompts that the old skill was supposed to handle.
