---
name: planning-app
description: Manage the Ghost Team Planning App database via Neon MCP and connect to Supabase MCP for product data. Use when creating, updating, or querying goals, objectives, stories, KPIs, sprints, or any planning data. Triggers on requests to add tasks, update progress, create goals, manage sprints, track KPIs, query planning data, or check project status.
---

# Planning App Database Management

Manage goals, objectives, stories, KPIs, and sprints via Neon MCP `run_sql` tool. Optionally connect to Supabase MCP for cross-referencing product analytics data.

## Data Sources

### 1. Neon MCP — Planning Database (Primary)

Sprint planning, goals, stories, KPIs, and activity tracking.

| Property | Value |
|----------|-------|
| Neon Project ID | `weathered-waterfall-03263467` |
| Database | `neondb` |
| MCP Tool | `run_sql(projectId, sql, databaseName)` |

#### mcporter Setup

Add to your `mcporter.json`:

```json
{
  "ghost-team-planning-app": {
    "command": "npx",
    "args": ["-y", "@neondatabase/mcp-server-neon"],
    "env": {
      "NEON_API_KEY": "<your-neon-api-token>"
    },
    "transportType": "stdio"
  }
}
```

Then call via:
```bash
mcporter call ghost-team-planning-app run_sql "<SQL>" "weathered-waterfall-03263467"
```

**Important:** When SQL contains single quotes, use `--args` JSON syntax:
```bash
mcporter call ghost-team-planning-app run_sql --args '["SELECT * FROM stories WHERE status = '\''in_progress'\''", "weathered-waterfall-03263467"]'
```

### 2. Supabase MCP — Product Data (Secondary)

App discoverability data: tools, apps, search results, auth scans.

| Property | Value |
|----------|-------|
| Supabase Project Ref | `bfdtklwpgjkpivxzabqd` |
| Auth | Personal Access Token (PAT) |

#### mcporter Setup

Add to your `mcporter.json`:

```json
{
  "supabase": {
    "command": "npx",
    "args": ["-y", "@anthropic-ai/supabase-mcp-server"],
    "env": {
      "SUPABASE_ACCESS_TOKEN": "<your-supabase-pat>"
    },
    "transportType": "stdio"
  }
}
```

#### Key Supabase Tables

| Table | Records | Description |
|-------|---------|-------------|
| `apps` | 163+ | App profiles (name, slug, description, images) |
| `tool_versions` | 120+ | MCP tool metadata snapshots |
| `auth_scans` | 162+ | Auth type breakdown per app |
| `search_results` | 69k+ | Intent-to-app search result mappings |
| `intents` | 638+ | Search intents/queries |
| `appstore_versions` | 1.7k+ | App Store listing snapshots |
| `subscribers` | 29+ | Email subscribers |

#### Materialized Views (pre-aggregated for dashboards)

| View | Description |
|------|-------------|
| `mv_track_stats` | Summary stats (total apps, tools, etc.) |
| `mv_track_apps` | App listing with tool counts |
| `mv_track_timeline` | Timeline of app/tool additions |
| `mv_track_categories` | Category breakdown |
| `mv_track_tools_summary` | Tool-level summary |
| `mv_track_auth_breakdown` | Auth type distribution |
| `mv_competitive_ranks` | Search ranking data |

Refresh views: `SELECT refresh_track_views();`

## Users

Always use the correct UUID for `created_by`, `assignee_id`, `accountable_id`, `recorded_by`.

| Name | UUID | Email |
|------|------|-------|
| **Vincent McLeese** | `2549f386-e526-4f9e-9626-e4feee96ca6d` | vincent@ghostteam.ai |
| **Elliot Garreffa** | `e586df16-a268-4736-b71a-e19cf1bf398c` | elliot@ghostteam.ai |

Default `created_by`: Vincent's UUID (unless specified otherwise).

## Hierarchy

```
goals → objectives → stories
              ↳ → kpis → kpi_updates
sprints ↔ stories (via story_sprints join table)
```

## Enum Values

| Type | Values |
|------|--------|
| goal_status | `draft`, `in_progress`, `done`, `archived` |
| objective_status | `not_started`, `in_progress`, `completed`, `maintaining` |
| story_status | `backlog`, `ready`, `in_progress`, `in_review`, `done`, `blocked`, `deprioritized`, `archived` |
| priority | `critical`, `must_have`, `nice_to_have` |
| kpi_data_source | `manual`, `sprint_accuracy`, `sprint_velocity`, `external_api` |

## Workflow Rules

1. **Always query first** when updating — never assume a record ID exists
2. **Use RETURNING clause** on INSERT/UPDATE to confirm changes
3. **Verify parent exists** before creating child records (e.g., goal before objective)
4. **Include `created_by`** on all inserts — use the correct user UUID

## Quick Reference SQL

For full table schemas, see [references/schema.md](references/schema.md).

### Create Goal
```sql
INSERT INTO goals (title, description, year, quarter_start, quarter_end, status, priority, position, created_by)
VALUES ('Title', 'Desc', 2026, 1, 4, 'draft', 'must_have', 0, '2549f386-e526-4f9e-9626-e4feee96ca6d')
RETURNING id, title, status;
```

### Create Objective
```sql
INSERT INTO objectives (goal_id, title, description, status, priority, created_by, accountable_id)
VALUES ('<goal_uuid>', 'Title', 'Desc', 'not_started', 'must_have', '2549f386-e526-4f9e-9626-e4feee96ca6d', '2549f386-e526-4f9e-9626-e4feee96ca6d')
RETURNING id, title, status;
```

### Create Story
```sql
INSERT INTO stories (objective_id, title, description, acceptance_criteria, status, priority, estimated_hours, assignee_id, created_by)
VALUES ('<obj_uuid>', 'Title', 'Desc', 'AC', 'backlog', 'must_have', 4.0, '2549f386-e526-4f9e-9626-e4feee96ca6d', '2549f386-e526-4f9e-9626-e4feee96ca6d')
RETURNING id, title, status;
```

### Assign Story to Sprint
```sql
INSERT INTO story_sprints (story_id, sprint_id) VALUES ('<story_uuid>', '<sprint_uuid>');
```

### Update Status
```sql
UPDATE stories SET status = 'in_progress', updated_at = NOW() WHERE id = '<uuid>' RETURNING *;
```

### Log Activity (story_updates)
```sql
INSERT INTO story_updates (story_id, field_name, old_value, new_value, changed_by, note)
VALUES ('<story_uuid>', 'status', 'in_progress', 'done', '2549f386-e526-4f9e-9626-e4feee96ca6d', 'Completed review')
RETURNING id, created_at;
```

### Record KPI Update
```sql
INSERT INTO kpi_updates (kpi_id, value, note, recorded_by)
VALUES ('<kpi_uuid>', 50, 'Note', '2549f386-e526-4f9e-9626-e4feee96ca6d')
RETURNING id, value, recorded_at;
```

### Sprint Status Summary
```sql
SELECT s.status, COUNT(*) as count, COALESCE(SUM(s.estimated_hours), 0) as est_hours, COALESCE(SUM(s.actual_hours), 0) as actual_hours
FROM stories s
JOIN story_sprints ss ON ss.story_id = s.id
WHERE ss.sprint_id = '<sprint_uuid>'
GROUP BY s.status ORDER BY count DESC;
```

## Safety Rules

- ❌ Never delete users or modify `neon_auth.*` tables
- ❌ Never insert without verifying foreign keys exist
- ✅ Always set `created_by` on goals, objectives, stories, KPIs
- ✅ Always set `recorded_by` on KPI updates
- ✅ Always use `RETURNING` to confirm operations
- ✅ Always set `updated_at = NOW()` on updates

## Detailed Reference

For complete schema details, see [references/schema.md](references/schema.md).
