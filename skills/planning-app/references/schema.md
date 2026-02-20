# Planning App Database Schema

## goals
| Column | Type | Nullable | Default |
|--------|------|----------|---------|
| id | uuid | NO | gen_random_uuid() |
| title | varchar | NO | |
| description | text | YES | |
| year | integer | NO | |
| quarter_start | integer | NO | |
| quarter_end | integer | NO | |
| status | goal_status | NO | 'draft' |
| created_by | uuid | NO | |
| created_at | timestamptz | NO | now() |
| updated_at | timestamptz | NO | now() |
| priority | priority | NO | 'nice_to_have' |
| position | integer | NO | 0 |

## objectives
| Column | Type | Nullable | Default |
|--------|------|----------|---------|
| id | uuid | NO | gen_random_uuid() |
| goal_id | uuid (FK→goals) | NO | |
| title | varchar | NO | |
| description | text | YES | |
| status | objective_status | NO | 'not_started' |
| created_by | uuid | NO | |
| created_at | timestamptz | NO | now() |
| updated_at | timestamptz | NO | now() |
| priority | priority | NO | 'nice_to_have' |
| position | integer | NO | 0 |
| accountable_id | uuid (FK→users) | YES | |

## stories
| Column | Type | Nullable | Default |
|--------|------|----------|---------|
| id | uuid | NO | gen_random_uuid() |
| objective_id | uuid (FK→objectives) | NO | |
| title | varchar | NO | |
| description | text | YES | |
| acceptance_criteria | text | YES | |
| status | story_status | NO | 'backlog' |
| priority | priority | NO | 'nice_to_have' |
| estimated_hours | numeric | YES | |
| actual_hours | numeric | YES | |
| assignee_id | uuid (FK→users) | YES | |
| created_by | uuid | NO | |
| created_at | timestamptz | NO | now() |
| updated_at | timestamptz | NO | now() |

## sprints
| Column | Type | Nullable | Default |
|--------|------|----------|---------|
| id | uuid | NO | gen_random_uuid() |
| sprint_number | integer | NO | |
| year | integer | NO | |
| start_date | date | NO | |
| end_date | date | NO | |
| created_at | timestamptz | NO | now() |
| description | text | YES | |
| updated_at | timestamptz | YES | now() |

## story_sprints (join table)
| Column | Type | Nullable | Default |
|--------|------|----------|---------|
| story_id | uuid (FK→stories) | NO | |
| sprint_id | uuid (FK→sprints) | NO | |
| carried_over | boolean | NO | false |
| added_at | timestamptz | NO | now() |
| completed_in_sprint | boolean | NO | false |
| is_unplanned | boolean | NO | false |
| unplanned_reason | varchar | YES | |
| dashboard_position | integer | YES | |
| dashboard_section | varchar | YES | 'rest' |

## kpis
| Column | Type | Nullable | Default |
|--------|------|----------|---------|
| id | uuid | NO | gen_random_uuid() |
| objective_id | uuid (FK→objectives) | NO | |
| name | varchar | NO | |
| target_value | numeric | NO | |
| current_value | numeric | NO | 0 |
| unit | varchar | NO | |
| measurement_frequency | varchar | YES | 'weekly' |
| created_by | uuid | NO | |
| created_at | timestamptz | NO | now() |
| updated_at | timestamptz | NO | now() |
| data_source | kpi_data_source | NO | 'manual' |
| data_source_config | jsonb | YES | |

## kpi_updates
| Column | Type | Nullable | Default |
|--------|------|----------|---------|
| id | uuid | NO | gen_random_uuid() |
| kpi_id | uuid (FK→kpis) | NO | |
| value | numeric | NO | |
| note | text | YES | |
| recorded_at | timestamptz | NO | now() |
| recorded_by | uuid | NO | |
| is_system_generated | boolean | NO | false |
| metadata | jsonb | YES | |

## users
| Column | Type | Nullable | Default |
|--------|------|----------|---------|
| id | uuid | NO | |
| email | varchar | NO | |
| name | varchar | NO | |
| avatar_url | text | YES | |
| created_at | timestamptz | NO | now() |
| updated_at | timestamptz | NO | now() |
| hourly_rate | numeric | YES | |
