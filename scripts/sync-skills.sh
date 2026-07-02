#!/bin/sh

set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname "$0")" && pwd)
REPO_ROOT=$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)
TARGET_ROOT=${AGENTS_SKILLS_DIR:-"$HOME/.agents/skills"}
BACKUP_ROOT="$TARGET_ROOT/.backup"
TIMESTAMP=$(date +"%Y%m%d-%H%M%S")
CHANGED=0
SKIPPED=0
CREATED=0

mkdir -p "$TARGET_ROOT"

echo "Syncing skills to: $TARGET_ROOT"

for skill_dir in "$REPO_ROOT"/*; do
  [ -d "$skill_dir" ] || continue

  skill_name=$(basename "$skill_dir")
  case "$skill_name" in
    .*|scripts)
      continue
      ;;
  esac
  [ -f "$skill_dir/SKILL.md" ] || continue

  target_dir="$TARGET_ROOT/$skill_name"

  if [ ! -e "$target_dir" ]; then
    mkdir -p "$target_dir"
    rsync -a "$skill_dir/" "$target_dir/"
    echo "[create] $skill_name"
    CREATED=$((CREATED + 1))
    continue
  fi

  if diff -qr "$skill_dir" "$target_dir" >/dev/null 2>&1; then
    echo "[skip]   $skill_name (already up to date)"
    SKIPPED=$((SKIPPED + 1))
    continue
  fi

  backup_dir="$BACKUP_ROOT/$TIMESTAMP/$skill_name"
  mkdir -p "$(dirname "$backup_dir")"
  mv "$target_dir" "$backup_dir"
  mkdir -p "$target_dir"
  rsync -a "$skill_dir/" "$target_dir/"
  echo "[update] $skill_name (backup: $backup_dir)"
  CHANGED=$((CHANGED + 1))
done

echo
echo "Done. created=$CREATED updated=$CHANGED skipped=$SKIPPED"
