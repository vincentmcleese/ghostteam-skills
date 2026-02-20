#!/usr/bin/env bash
set -euo pipefail

AGENT_NAME="${1:-maya}"
HOSTNAME_SHORT="$(hostname -s)"
BRANCH="${AGENT_NAME}-${HOSTNAME_SHORT}"
BACKUP_ROOT="${HOME}/.openclaw-backup-tmp"
SRC_OC="${HOME}/.openclaw"
REPO_URL="${BACKUP_REPO_URL:-}"
GH_PAT="${GITHUB_PAT:-}"

if [[ -z "$REPO_URL" ]]; then
  echo "Set BACKUP_REPO_URL env var" >&2
  exit 1
fi

if [[ -z "$GH_PAT" ]]; then
  echo "Set GITHUB_PAT env var" >&2
  exit 1
fi

rm -rf "$BACKUP_ROOT"
mkdir -p "$BACKUP_ROOT"

# Copy safe paths
mkdir -p "$BACKUP_ROOT/.openclaw"
rsync -a --delete "$SRC_OC/workspace/" "$BACKUP_ROOT/.openclaw/workspace/"
[[ -f "$SRC_OC/openclaw.json" ]] && cp "$SRC_OC/openclaw.json" "$BACKUP_ROOT/.openclaw/openclaw.json"
[[ -f "$SRC_OC/cron/jobs.json" ]] && mkdir -p "$BACKUP_ROOT/.openclaw/cron" && cp "$SRC_OC/cron/jobs.json" "$BACKUP_ROOT/.openclaw/cron/jobs.json"
[[ -d "$SRC_OC/custom-skills" ]] && rsync -a "$SRC_OC/custom-skills/" "$BACKUP_ROOT/.openclaw/custom-skills/"

# Remove sensitive paths/files
rm -rf "$BACKUP_ROOT/.openclaw/workspace/.secrets"
find "$BACKUP_ROOT" -type f \( -name "*.pem" -o -name "*.key" -o -name "*.p12" \) -delete

# Git push
cd "$BACKUP_ROOT"
git init -q
git config user.name "OpenClaw Backup Bot"
git config user.email "backup-bot@ghostteam.ai"
git remote add origin "https://x-access-token:${GH_PAT}@${REPO_URL#https://}"

git checkout -b "$BRANCH" >/dev/null 2>&1 || git checkout "$BRANCH"
git add -A
if git diff --cached --quiet; then
  echo "No changes to back up"
  exit 0
fi

git commit -m "backup(${AGENT_NAME}): $(date -u +%Y-%m-%dT%H:%M:%SZ)"
git push -u origin "$BRANCH" --force

echo "Backup complete: $BRANCH"
