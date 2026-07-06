# Personal Skills Repository

This repository contains personal Codex/agent skills, along with sync scripts for installing them into a local global skills directory.

## Included Skills

- `a-stock-data`
- `agnes-ai-generation`
- `ai-evals`
- `competitive-analysis`
- `conducting-user-interviews`
- `conventional-commits`
- `creating-skills`
- `find-skills`
- `prioritizing-roadmap`
- `problem-definition`
- `scoping-cutting`
- `writing-prds`

## Structure

Each skill is preserved in its original directory layout, including supporting `references/`, `agents/`, and `scripts/` folders where present.

The sync scripts detect any top-level directory that contains a `SKILL.md` file, so newly added skills can be picked up without editing the script for each addition.

## Sync To Local Skills

This repository includes quick sync scripts for copying the skills in this repo into the local global skills directory.

### macOS

Run:

```bash
./sync-skills.sh
```

Default target:

```text
~/.agents/skills
```

You can also override the target path:

```bash
AGENTS_SKILLS_DIR=/custom/path ./sync-skills.sh
```

### Windows

Run in Command Prompt:

```bat
sync-skills.cmd
```

Default target:

```text
%USERPROFILE%\.agents\skills
```

You can also override the target path:

```bat
set AGENTS_SKILLS_DIR=D:\custom\skills
sync-skills.cmd
```

### Existing Skills Behavior

- If a skill does not exist in the target directory, it is copied directly.
- If a skill already exists and the content is unchanged, it is skipped.
- If a skill already exists and the content is different, the existing version is moved into a timestamped `.backup` folder and then replaced with the repository version.

## Source

Maintained as the working repository for local personal skills on this machine.
