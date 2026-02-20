# Contributing Skills

## Creating a New Skill

1. Create a directory under `skills/` with a kebab-case name
2. Add `SKILL.md` with YAML frontmatter (`name` and `description` required)
3. Add `manifest.json` with version, requirements, and compatibility
4. Add `scripts/`, `references/`, `assets/` as needed
5. Update `registry.json` with the new skill entry
6. Update the skills table in `README.md`

## SKILL.md Guidelines

- Keep under 500 lines — move details to `references/`
- Use imperative voice
- Include concrete examples
- Description in frontmatter is the trigger — be specific about when to use it

## manifest.json Schema

```json
{
  "name": "skill-name",
  "version": "1.0.0",
  "description": "What this skill does",
  "category": "finance|product|growth|planning|ops|client|browsing",
  "tags": ["tag1", "tag2"],
  "requires": {
    "secrets": ["api_key_name"],
    "tools": ["exec", "web_fetch"]
  },
  "compatibility": {
    "openclaw": ">=2026.2.0"
  }
}
```

## Versioning

- Use semver (major.minor.patch)
- Bump patch for fixes, minor for new features, major for breaking changes
- Git tags: `<skill-name>/v1.0.0`
