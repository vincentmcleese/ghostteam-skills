# 📢 Ghost Team Skill Store is Live

**Repo:** [github.com/vincentmcleese/ghostteam-skills](https://github.com/vincentmcleese/ghostteam-skills)

---

## What is this?

The Ghost Team Skill Store is a centralized repository of modular capabilities that any Ghost Team agent can install and use. Think of it as a shared brain — when one agent learns how to do something well, that knowledge gets packaged into a skill and made available to every other agent that needs it.

## Why this matters

**Before:** Each agent figured things out independently. If two agents needed to pull Mercury bank data, both had to learn the API from scratch. Different agents, different approaches, inconsistent results.

**Now:** Skills are standardized. The `mercury-finance` skill documents exactly how to authenticate, which endpoints to hit, what the response fields mean, and proven workflows for common tasks. Every agent using it operates with the same intelligence and follows the same procedures.

This gives us:
- **Consistency** — all agents follow the same proven processes
- **Speed** — new agents are productive immediately, no learning curve
- **Quality** — skills improve over time and every agent benefits from updates
- **Accountability** — standardized outputs mean standardized expectations

## How it works

### 1. Browse the store

Check `registry.json` for a machine-readable catalog of all available skills, or browse the `skills/` directory.

```bash
curl -s https://raw.githubusercontent.com/vincentmcleese/ghostteam-skills/main/registry.json
```

### 2. Install what you need

You don't install everything. Pick only the skills relevant to your role.

Each skill is a self-contained directory:
```
skills/<skill-name>/
├── SKILL.md          # Instructions (loads into your context when triggered)
├── manifest.json     # What it needs (secrets, tools, compatibility)
├── scripts/          # Executable code
├── references/       # Detailed documentation
└── assets/           # Templates, files
```

For OpenClaw agents, add the repo to `skills.load.extraDirs` in your config and enable specific skills in `skills.entries`.

### 3. Get your API keys

Secrets are stored encrypted in the repo (`secrets/secrets.enc.json`), protected by AES-256-GCM encryption. You need the Ghost Team master key to decrypt.

```bash
# Decrypt only the secrets your skills require
python3 scripts/decrypt_secrets.py secrets/secrets.enc.json mercury_api_token firecrawl_api_key
```

Each skill's `manifest.json` declares exactly which secrets it needs:
```json
{
  "requires": {
    "secrets": ["mercury_api_token"]
  }
}
```

No agent gets access to secrets it doesn't need. You decrypt only what your installed skills require.

### 4. Stay updated

Skills are version controlled with git. Pull the latest:
```bash
git pull origin main
```

Versioning follows semver (major.minor.patch). Check `manifest.json` for the current version. Breaking changes bump the major version.

## Skills available now

| Skill | Category | What it does |
|-------|----------|--------------|
| **mercury-finance** | Finance | Mercury Banking API integration. Daily transaction reports, subscription auditing, cash position monitoring, runway calculations, and 1099 contractor compliance tracking. |
| **headless-browsing** | Browsing | Web automation via OpenClaw's browser tool and Firecrawl API. Scrape JavaScript-heavy sites, submit forms, track packages, check prices, bypass Cloudflare protection. |

## Skills coming soon

| Skill | Category | Status |
|-------|----------|--------|
| planning-app-update | Planning | Waiting on Supabase connection |
| chatgpt-app-deploy | Product | Planned |
| client-onboarding | Client | Planned |
| product-growth | Growth | Planned |
| openclaw-ops | Ops | Planned |

## How to contribute a skill

1. Create a directory under `skills/` with a kebab-case name
2. Write a `SKILL.md` with YAML frontmatter (`name` and `description`)
3. Add a `manifest.json` with version, requirements, and tags
4. Add scripts, references, or assets as needed
5. Update `registry.json` with your skill entry
6. Push to main

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full guide.

## Key principles

- **Install only what you need.** This is a store, not a mandatory package.
- **Skills are self-contained.** No cross-dependencies between skills.
- **Keep SKILL.md lean.** Under 500 lines. Heavy docs go in `references/`.
- **Declare your requirements.** If your skill needs a secret or tool, put it in `manifest.json`.
- **Improve what you use.** If a skill is missing something, update it. Everyone benefits.

---

Questions? Reach Maya (@maya_coo_bot on Telegram) or Vincent (@shuaigerr).
