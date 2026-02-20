---
name: agent-backup-github
description: Set up and operate daily OpenClaw agent backups to a private GitHub repository. Use when creating backup automation, disaster recovery workflows, or cross-agent backup standards. Includes safe include/exclude rules, cron scheduling, and restore procedures.
---

# Agent Backup to GitHub

Create daily, secret-safe backups for OpenClaw agents.

## Backup scope
Include:
- `~/.openclaw/workspace/`
- `~/.openclaw/openclaw.json`
- `~/.openclaw/cron/jobs.json`
- `~/.openclaw/custom-skills/` (if exists)

Exclude secrets:
- `~/.openclaw/.env`
- `~/.openclaw/identity/`
- `~/.openclaw/devices/`
- `workspace/.secrets/`
- any `*.pem`, `*.key`, `*token*` plaintext files

## Repo convention
- Private repo: `ghostteam-agent-backups`
- Branch per agent host: `<agent>-<hostname>`
- Example: `maya-vmi3090164`

## Setup
1. Ensure GitHub PAT with `repo` scope is available.
2. Create or use private backup repo.
3. Install scripts from `scripts/`.
4. Schedule daily cron at 03:00 local time.

## Runbook
- Daily: run backup script, commit only when changed.
- Weekly: verify last 7 backups exist.
- Monthly: test restore on a staging path.

## Restore
Use `scripts/restore_backup.sh` with:
- repo URL
- branch
- target path (default `~/.openclaw`)
Then restart gateway.

## Notes
- Keep secrets separate from backups.
- Store encrypted secrets in dedicated skill store repo (`secrets.enc.json`).
- Backup is for continuity, not for credential escrow.
