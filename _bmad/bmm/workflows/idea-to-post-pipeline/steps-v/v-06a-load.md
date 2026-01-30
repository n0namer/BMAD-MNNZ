---
description: Load all posts and ideas for batch validation
name: step-v-06a-load
nextStepFile: ./v-06b-batch-checks.md
type: data-loading
---

# VALIDATE V-06A: Load All Content for Batch Validation

## STEP GOAL:

Load all posts and ideas for comprehensive batch validation across all quality checks (V-01 through V-05).

## EXECUTION:
### EXECUTION RULES - HALT AND WAIT

**ALWAYS halt and wait for user input after presenting menu or asking for selection.**
**ONLY proceed to next step when user provides explicit input/selection.**


### 1. Display Loading Status

```
═══════════════════════════════════════════════════════════════

  🚀 VALIDATE V-06: BATCH VALIDATE ALL

  Loading all posts and ideas for comprehensive validation...

═══════════════════════════════════════════════════════════════
```

### 2. Load Content from Database

Query both databases:
- Posts: from `posts.csv` (all statuses, all dates)
- Ideas: from `ideas_inbox.csv` (active ideas)

Example output:
```
LOADING CONTENT:

Posts database: 156 total posts
├─ Published: 124 posts
├─ Draft: 28 posts
└─ Archived: 4 posts

Ideas database: 47 active ideas
├─ New: 12 ideas (pending research)
├─ Researched: 18 ideas (ready to write)
├─ Used: 17 ideas (already published)

Total content items: 203
Loading complete.
```

### 3. Display Loading Summary

```
BATCH VALIDATION SCOPE:
  Total posts: 156
  Total ideas: 47
  Combined items: 203

  Validation will include:
    ✓ Quality Checklist (V-01)
    ✓ Performance Audit (V-02)
    ✓ Consistency Check (V-03)
    ✓ Copy Audit (V-04)
    ✓ Engagement Check (V-05)

  Estimated time: 10-15 minutes
  Results: Comprehensive quality report

Ready for batch validation.
```

### 4. Confirmation

```
This will validate ALL content in parallel.

[Y] YES — Запустить полную проверку (10-15 мин)
[F] FILTER — Выбрать диапазон постов/идей
[?] BACK — Вернуться в меню

═══════════════════════════════════════════════════════════════
```

**[Y] YES:**
Load, read entire file, then execute `./step-v-06b-batch-checks.md`

**[F] FILTER:**
Return to step 2 (user selects posts/ideas, date range, etc.)

**[?] BACK:**
Load `./v-00-menu.md`


### Menu Handling Logic

**IF [Y]: YES:**
Load, read entire file, then execute `./step-v-06b-batch-checks.md`

**IF [F]: FILTER:**
Return to step 2 (user selects posts/ideas, date range, etc.)

**EXECUTION RULE:**
ALWAYS halt and wait for user input after presenting menu. ONLY proceed when user makes a selection.
---

## SAVED DATA

Store loaded content for batch validation:
```json
{
  "validation_session_id": "v-06-[timestamp]",
  "loaded_posts": 156,
  "loaded_ideas": 47,
  "total_items": 203,
  "batch_type": "comprehensive",
  "content": {
    "posts": [ ... ],
    "ideas": [ ... ]
  }
}
```

---

## NEXT STEP

Run all quality checks on all content in parallel

