# Personal Skills Repository

This repository contains the personal Codex/agent skills extracted from the local global skills directory at `/Users/jonny/.agents/skills`.

## Included Skills

- `agnes-ai-generation`
- `ai-evals`
- `competitive-analysis`
- `conducting-user-interviews`
- `conventional-commits`
- `find-skills`
- `prioritizing-roadmap`
- `problem-definition`
- `scoping-cutting`
- `writing-prds`

## Structure

Each skill is preserved in its original directory layout, including supporting `references/`, `agents/`, and `scripts/` folders where present.

## Sync To Local Skills

This repository includes quick sync scripts for copying the skills in this repo into the local global skills directory.

### macOS

Run:

```bash
./scripts/sync-skills.sh
```

Default target:

```text
~/.agents/skills
```

You can also override the target path:

```bash
AGENTS_SKILLS_DIR=/custom/path ./scripts/sync-skills.sh
```

### Windows

Run in Command Prompt:

```bat
scripts\sync-skills.cmd
```

Default target:

```text
%USERPROFILE%\.agents\skills
```

You can also override the target path:

```bat
set AGENTS_SKILLS_DIR=D:\custom\skills
scripts\sync-skills.cmd
```

### Existing Skills Behavior

- If a skill does not exist in the target directory, it is copied directly.
- If a skill already exists and the content is unchanged, it is skipped.
- If a skill already exists and the content is different, the existing version is moved into a timestamped `.backup` folder and then replaced with the repository version.

## Source

Extracted on `2026-06-29` from the local personal skills path on this machine.
