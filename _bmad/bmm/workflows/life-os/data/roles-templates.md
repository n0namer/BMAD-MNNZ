# Role Profile Templates

## Standard Role Profile Structure

```markdown
---
name: {role}
status: ACTIVE
created: {today}
---

# {role}

## Scope
{1-2 sentences describing the responsibility boundary}

## Typical Contributions
- {contribution 1}
- {contribution 2}
- {contribution 3}

## Signals This Role Is Needed
- {signal 1}
- {signal 2}
```

## Template Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{role}` | Role name from roles-base.csv | "Financial Planner" |
| `{today}` | Current date in ISO format | "2026-02-05" |
| `{responsibility boundary}` | Brief scope definition | "Manages budget allocation and investment strategy" |
| `{contribution N}` | Typical deliverables | "Monthly budget reports" |
| `{signal N}` | Indicators this role is needed | "Project involves financial planning" |

## Usage

1. Check if role exists in `{specialistsFolder}`
2. If missing, create new file: `{specialistsFolder}/{role-slug}.md`
3. Fill template with role-specific details from roles-base.csv
4. Save with status: ACTIVE
