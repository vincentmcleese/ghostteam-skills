# 🛠️ Ghost Team Skill Store

Modular, self-contained capabilities for AI agents. Agents browse the registry, pick what they need, and install only the skills relevant to their role.

## How It Works

1. **Browse** — check `registry.json` or browse `skills/` by category
2. **Select** — read the skill's `manifest.json` for requirements and compatibility
3. **Install** — pull the skill's `SKILL.md` + resources into your agent's skill directory

## Categories

| Category | Description |
|----------|-------------|
| `finance` | Banking, expense tracking, compliance |
| `product` | App deployment, MCP integrations |
| `growth` | Outreach, newsletters, metrics |
| `planning` | Sprint planning, project tracking |
| `ops` | Infrastructure, monitoring, security |
| `client` | Client onboarding, reporting |
| `browsing` | Web scraping, form automation |

## Skills

| Skill | Category | Version | Description |
|-------|----------|---------|-------------|
| [mercury-finance](skills/mercury-finance/) | finance | 1.0.0 | Daily finance tracking, subscription auditing, cash monitoring via Mercury API |
| [headless-browsing](skills/headless-browsing/) | browsing | 1.0.0 | Web scraping, form submission, and interaction with JS-heavy sites |

## For Agents

```bash
# Discover skills
curl -s https://raw.githubusercontent.com/vincentmcleese/ghostteam-skills/main/registry.json

# Pull a skill
curl -s https://raw.githubusercontent.com/vincentmcleese/ghostteam-skills/main/skills/<skill-name>/SKILL.md
```

## Structure

```
skills/
├── <skill-name>/
│   ├── SKILL.md          # Instructions (loaded into agent context)
│   ├── manifest.json     # Requirements, version, compatibility
│   ├── scripts/          # Executable code
│   ├── references/       # Documentation for context
│   └── assets/           # Templates, files used in output
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to create or update skills.

---

Built by [Ghost Team](https://ghostteam.ai) 👻
