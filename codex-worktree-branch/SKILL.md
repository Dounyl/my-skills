---
name: codex-worktree-branch
description: Creates a Codex-managed worktree and a scoped branch only when the user explicitly requests a Codex worktree, such as "创建 Codex 工作树", "新建 Codex 工作树", or "切换到 Codex 工作树". Do not use for ordinary Git worktree requests, branch operations, independent development, Codex task creation, or carrying uncommitted changes unless the request explicitly names a Codex worktree.
---

# Codex Worktree Branch

Create a separate Codex task, then create and attach the new branch inside that task's worktree. Default to a clean `main` baseline and include source-worktree changes only when the user explicitly requests them.

## Confirm The Request

Use this skill only when the user explicitly asks to create, use, or switch to a Codex worktree. A request for a Git worktree, a separate/independent task, or development effort does not imply a Codex worktree.

If the request is for an ordinary Git worktree, to create, name, base, or switch a Git branch, create a Codex task, start independent development, or carry uncommitted changes without explicitly requesting a Codex worktree, do not create a Codex worktree or Codex task. Perform the requested operation in the current repository using the normal Git workflow. A `codex/...` branch prefix alone does not request a Codex worktree.

## Name The Branch

1. Extract the stated development scope.
2. Convert it to a short, specific English kebab-case name using lowercase ASCII letters, digits, and hyphens.
3. Prefix it with `codex/`.

Examples:

- "首页业务接入" -> `codex/home-business-integration`
- "Google Play 审核" -> `codex/google-play-review`
- "修复登录验证码" -> `codex/fix-login-otp`

Honor a user-provided valid `codex/...` name. Otherwise state the derived name before creating the task.

## Select The Starting State

Choose exactly one mode before creating the task:

| User request | Codex starting state | Branch creation in the new worktree |
| --- | --- | --- |
| No baseline or change-transfer request | `{ type: "branch", branchName: "main" }` | `git checkout -b <branch> main` |
| Specifies an existing baseline branch | `{ type: "branch", branchName: "<base>" }` | `git checkout -b <branch> <base>` |
| Explicitly asks to carry current uncommitted changes | `{ type: "working-tree" }` | `git checkout -b <branch>` |

For the default mode, confirm `main` exists with `git rev-parse main`. For a specified baseline, confirm that ref exists. For `working-tree`, record the source `HEAD` and `git status --short` before creating the task. Request Codex to carry the source checkout and its uncommitted changes, then treat the post-creation status comparison as authoritative, especially for untracked files.

If the request combines a baseline branch and uncommitted changes, require the current source worktree to already be on that baseline. `working-tree` uses the current checkout; do not silently transfer a diff from a different branch.

## Create The Worktree

1. Confirm the derived branch does not exist and is not attached to another worktree with `git show-ref --verify refs/heads/<branch>` and `git worktree list --porcelain`.
2. Do not create the branch in the source worktree. If the branch already exists, report its owner and request direction; never delete or reuse it implicitly.
3. Use `codex_app__list_projects`, then create a new Codex task with `codex_app__create_thread`, `environment.type: "worktree"`, and the selected starting state.
4. Wait for setup to finish and identify the new task's actual worktree path. The active task cannot move itself to a worktree; open the new task instead.

## Attach And Verify

1. In the new Codex worktree only, create the branch with the command selected above.
2. Verify the branch name and its worktree association with `git status --short --branch` and `git worktree list --porcelain`.
3. For clean or specified-baseline modes, verify `git status --short` is empty and `git rev-parse <branch>` equals the selected baseline ref.
4. For `working-tree` mode, verify the branch `HEAD` equals the recorded source `HEAD`, then compare the recorded and destination `git status --short` output. Report any difference, especially missing untracked files.
5. Open the new task with `codex_app__navigate_to_codex_page`.

## Report

State the Codex task, branch name, worktree path, selected baseline, and whether uncommitted files were excluded or carried over.
