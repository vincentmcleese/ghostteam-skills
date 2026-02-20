# Cron Example

Daily backup at 03:00 Europe/Berlin:

```bash
export BACKUP_REPO_URL="https://github.com/vincentmcleese/ghostteam-agent-backups.git"
export GITHUB_PAT="<pat>"
/root/.openclaw/custom-skills/ghostteam-skills/skills/agent-backup-github/scripts/backup_agent.sh maya
```

Cron line:

```cron
0 3 * * * BACKUP_REPO_URL=https://github.com/vincentmcleese/ghostteam-agent-backups.git GITHUB_PAT=<pat> /root/.openclaw/custom-skills/ghostteam-skills/skills/agent-backup-github/scripts/backup_agent.sh maya >> /tmp/openclaw-backup.log 2>&1
```
