---
description: Load posts to validate for quality checklist
name: step-v-01a-load
nextStepFile: ./step-v-01b-checks.md
type: data-loading
---

# VALIDATE V-01A: Load Posts for Quality Validation

## STEP GOAL:

Load generated posts from database for quality checklist validation (structure, tone, formatting).

## EXECUTION:
### EXECUTION RULES - HALT AND WAIT

**ALWAYS halt and wait for user input after presenting menu or asking for selection.**
**ONLY proceed to next step when user provides explicit input/selection.**


### 1. Display Loading Status

```
═══════════════════════════════════════════════════════════════

  📋 VALIDATE V-01: QUALITY CHECKLIST

  Loading posts for quality validation...

═══════════════════════════════════════════════════════════════
```

### 2. Load Posts from Database

Query `posts.csv` with filters:
- Status: `published` or `draft`
- Date range: last 30 days (or user-specified)
- Limit: all available or user-specified range

Example output:
```
Loaded 24 posts (last 30 days):
├─ Post #1: "5 Ways to..." [2024-01-15]
├─ Post #2: "Common Mistake..." [2024-01-14]
├─ Post #3: "Why Most People..." [2024-01-13]
...
└─ Post #24: "The Truth About..." [2024-01-02]

Ready to validate.
```

### 3. Display Summary

```
VALIDATION SCOPE:
  Total posts: 24
  Date range: Jan 2 - Jan 15, 2024
  Status: draft/published

Next: Run quality checks on each post
```

### 4. Confirmation

```
Proceed with quality checks?

[Y] YES — Начать проверку качества
[M] MODIFY — Изменить диапазон постов
[?] BACK — Вернуться в меню

═══════════════════════════════════════════════════════════════
```

**[Y] YES:**
Load, read entire file, then execute `./step-v-01b-checks.md`

**[M] MODIFY:**
Return to step 2 (let user select date range, statuses, etc.)

**[?] BACK:**
Load `../mode-v-00-menu.md` (back to VALIDATE menu)


### Menu Handling Logic

**IF [Y]: YES:**
Load, read entire file, then execute `./step-v-01b-checks.md`

**IF [M]: MODIFY:**
Return to step 2 (let user select date range, statuses, etc.)

**EXECUTION RULE:**
ALWAYS halt and wait for user input after presenting menu. ONLY proceed when user makes a selection.
---

## SAVED DATA

Store loaded posts in temporary validation session:
```json
{
  "validation_session_id": "v-01-[timestamp]",
  "loaded_posts": 24,
  "date_range": "2024-01-02 to 2024-01-15",
  "status": ["draft", "published"],
  "posts": [
    {"id": 1, "title": "...", "content": "...", "created_at": "..."},
    ...
  ]
}
```

---

## NEXT STEP

Handle user confirmation and proceed to quality checks or modify selection

