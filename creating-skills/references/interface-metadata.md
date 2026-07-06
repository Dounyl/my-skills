# Interface Metadata Notes

Some environments support optional interface metadata files in addition to `SKILL.md`.

For example, this repository may include `agents/openai.yaml` as a platform-specific metadata file. Treat that file as optional integration metadata, not as part of Anthropic's documented core Skill structure.

Use the minimal shape:

```yaml
interface:
  display_name: "Creating Skills"
  short_description: "Create, replace, or improve skills."
  default_prompt: "Use this skill to create, replace, or refine a skill."
```

Guidelines:

- Keep interface metadata clearly separated from core Skill instructions.
- Keep `display_name` human-readable.
- Keep `short_description` concrete and under one sentence.
- Make `default_prompt` describe the primary action clearly.
- Keep platform-specific metadata aligned with `SKILL.md`; update both together.
- If the target platform does not use this file, omit it instead of forcing it into every Skill.
