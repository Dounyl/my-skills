# Skill Review Checklist

Use this checklist before considering a skill complete.

## Trigger Quality

- Does `description` explain both what the skill does and when to use it?
- Is `description` written in third person?
- Would 3 to 5 realistic user requests clearly match this metadata?
- Are important synonyms or variants present?
- Does the metadata avoid vague phrases like "helps with tasks"?

## Main File Quality

- Does `SKILL.md` contain only core workflow and decision rules?
- Is bulky detail moved into `references/`?
- Are all optional resources linked directly from `SKILL.md`?
- Is the writing imperative and action-oriented?
- Is there any repeated content that should live in one place only?

## Resource Quality

- Does every `scripts/` file remove repeated or fragile manual work?
- Does every `references/` file contain material worth loading on demand?
- Does every `assets/` file support outputs rather than explanation?
- Are there any empty or unused folders that should be removed?

## Portability

- Does the skill avoid assuming one machine, one repo, or one hardcoded path?
- Are in-skill paths written with forward slashes?
- Are environment-specific steps paired with a detection rule or fallback?
- If replacing an existing skill, are the good triggers and useful resources preserved?

## Validation

- Did you run any available validators or scaffold checks?
- Did you test at least one realistic prompt end to end?
- If the skill is intended for multiple models or runtimes, did you test the important ones?
- For complex skills, did you forward-test with minimal leaked context?
- Do the observed failures map to concrete edits in the skill?
