---
name: creating-skills
description: Creates, replaces, refactors, or improves skills. Use when the user asks to build a new skill, rewrite an existing skill, replace a weaker skill, optimize skill triggering, split oversized SKILL.md files, add references, scripts, or assets, or review a skill against skill best practices.
---

# Creating Skills

Create skills that are easy to trigger, cheap to load, and reliable in real work.

Read [references/examples.md](references/examples.md) when drafting metadata or structure.
Read [references/interface-metadata.md](references/interface-metadata.md) when adding optional platform-specific interface metadata such as `agents/openai.yaml`.
Read [references/checklist.md](references/checklist.md) before finishing, replacing, or reviewing a skill.

## Follow This Workflow

1. Decide whether a skill is warranted.
   Create a skill only when the capability will be reused, needs procedural guidance, bundles reusable artifacts, or benefits from deterministic helpers. For a one-off task, solve the task directly instead of manufacturing a skill.

2. Ground the skill in realistic requests.
   Collect or infer 3 to 5 example user asks that should trigger the skill. Include the actual artifacts or constraints when relevant. Use these examples to decide what belongs in metadata, `SKILL.md`, and optional resources.

3. If replacing an existing skill, preserve what already works.
   Read the current skill first. Keep its useful triggers, workflows, and resources. Remove duplication, stale assumptions, and environment-specific instructions that do not generalize. Tighten wording instead of expanding it.

4. Design the smallest useful package.
   Start with `SKILL.md`. Add `references/`, `scripts/`, `assets/`, or optional interface metadata only when they materially improve reuse, reliability, or discoverability.

5. Write metadata before body content.
   The YAML frontmatter is the trigger surface. Make it specific enough that the right requests activate the skill, but broad enough to cover the main variations. Use only:
   - `name`
   - `description`

6. Write a lean `SKILL.md`.
   Keep only the core workflow, decision rules, and navigation to bundled resources in the main file. Move bulky examples, schemas, and edge-case detail into `references/`.

7. Add deterministic resources selectively.
   Add scripts when the same code would otherwise be rewritten or when correctness depends on a fixed procedure. Add references when the model needs documentation on demand. Add assets when output should reuse files rather than recreate them.

8. Validate with real tasks.
   Run any local validation or scaffold scripts if they exist. If they do not exist, validate manually. Then forward-test the skill on realistic prompts and revise whatever caused confusion, drift, or unnecessary context loading.

## Name the Skill Well

- Use lowercase letters, digits, and hyphens only.
- Keep the folder name identical to the skill `name`.
- Prefer short action-oriented names such as `creating-skills`, `addressing-pr-comments`, or `analyzing-stock-data`.
- Keep names under 64 characters.

## Write Strong Trigger Metadata

Treat `description` as the primary routing mechanism.

- State what the skill does.
- State when to use it.
- Write in third person.
- Include concrete request patterns, adjacent synonyms, and important variants.
- Mention replacement or review scenarios if the skill supports them.
- Do not move trigger guidance into a "When to use" section in the body and assume it will help routing.

Good descriptions usually combine capability plus request context in one paragraph.

## Keep the Main File Lean

Prefer this split:

- `SKILL.md`: workflow, decision rules, failure handling, and links to resources
- `references/`: examples, schemas, detailed playbooks, large docs
- `scripts/`: deterministic helpers
- `assets/`: templates and files used in outputs
- `agents/openai.yaml`: optional interface metadata when the environment supports it

Do not create extra docs such as `README.md`, `CHANGELOG.md`, or process notes unless the skill genuinely needs them as runtime resources.

## Write the Body for Action, Not Commentary

- Use imperative phrasing.
- Tell the reader what to do, what to read, and what to avoid.
- Explain only the non-obvious decisions.
- Prefer short rules and checklists over long essays.
- Link directly from `SKILL.md` to every reference file the reader may need.
- Keep references one hop away from `SKILL.md`; avoid deep reference chains.

## Handle Environment Differences Cleanly

- If the environment already provides a scaffold or validation script, use it.
- If no helper exists, create the skill structure manually.
- Do not hardcode one local script path as if every environment has it.
- Prefer forward slashes in paths inside the skill content.
- When a step is environment-dependent, say how to detect the condition and what fallback to use.

## Validate the Skill

Validate at two levels:

1. Structural validation
   Check folder naming, frontmatter shape, broken links, and whether each resource folder is actually used.

2. Behavioral validation
   Test with realistic prompts. Confirm the skill triggers for the right requests, stays concise, reads only the needed references, and produces useful work without hidden context.

For difficult skills, forward-test with a fresh run using only the skill path and a realistic user-style prompt. Do not leak the expected answer or your diagnosis unless the test requires it.

## Tighten After Failures

When a test goes poorly, identify the failure mode before editing:

- wrong trigger
- too much context
- missing example
- weak decision rule
- hidden dependency on local environment
- step order ambiguity
- a task that should have been a script instead of prose

Then patch the smallest part that resolves the failure. Prefer surgical edits over broad expansion.

## Deliverables

When finishing skill work:

1. Create or update the skill files.
2. Summarize the main design decisions and assumptions.
3. State what you validated and what remains untested.
