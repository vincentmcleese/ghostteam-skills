#!/usr/bin/env bash
set -euo pipefail

REPO_URL="${1:?usage: restore_backup.sh <repo_url> <branch> [target_dir]}"
BRANCH="${2:?usage: restore_backup.sh <repo_url> <branch> [target_dir]}"
TARGET_DIR="${3:-$HOME}"
TMP_DIR="$(mktemp -d)"
GH_PAT="${GITHUB_PAT:-}"

if [[ -z "$GH_PAT" ]]; then
  echo "Set GITHUB_PAT env var" >&2
  exit 1
fi

AUTH_URL="https://x-access-token:${GH_PAT}@${REPO_URL#https://}"

git clone --depth 1 --branch "$BRANCH" "$AUTH_URL" "$TMP_DIR/repo"

rsync -a "$TMP_DIR/repo/.openclaw/" "$TARGET_DIR/.openclaw/"

echo "Restore complete to $TARGET_DIR/.openclaw"
