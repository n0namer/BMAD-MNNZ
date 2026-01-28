---
description: Load posts for copywriting quality audit
name: step-v-04a-load
nextStepFile: ./step-v-04b-audit.md
type: data-loading
---

# VALIDATE V-04A: Load Posts for Copy Audit

## STEP GOAL:

Load posts for copywriting quality audit: action verbs, specific data, clear benefits, compelling language, CTA clarity.

## EXECUTION:
### EXECUTION RULES - HALT AND WAIT

**ALWAYS halt and wait for user input after presenting menu or asking for selection.**
**ONLY proceed to next step when user provides explicit input/selection.**


### 1. Display Loading Status

```
═══════════════════════════════════════════════════════════════

  ✏️  VALIDATE V-04: COPY AUDIT

  Loading posts for copywriting analysis...

═══════════════════════════════════════════════════════════════
```

### 2. Load Posts from Database

Query `posts.csv`:
- Status: `published` or `draft`
- Date range: last 30 days (or user-specified)
- Focus: Full post text for copywriting analysis

Example output:
```
Loaded 22 posts (last 30 days):

Post #1: "5 Ways to Increase Productivity" [450 words]
Post #2: "Common Mistake When Learning" [380 words]
Post #3: "Why Most People Fail at Fitness" [520 words]
...
Post #22: "Complete Guide to React Hooks" [850 words]

Ready for copy audit.
```

### 3. Display Analysis Scope

```
COPY AUDIT SCOPE:
  Total posts: 22
  Date range: Jan 1-28, 2024
  Analysis focus: Copywriting quality
  Criteria: action verbs, data specificity, benefits, language, CTAs

Ready to audit copywriting quality.
```

### 4. Confirmation

```
Proceed with copy audit?

[Y] YES — Начать аудит копирайтинга
[M] MODIFY — Изменить диапазон постов
[?] BACK — Вернуться в меню

═══════════════════════════════════════════════════════════════
```

**[Y] YES:**
Load, read entire file, then execute `./step-v-04b-audit.md`

**[M] MODIFY:**
Return to step 2 (user selects date range, etc.)

**[?] BACK:**
Load `../mode-v-00-menu.md`


### Menu Handling Logic

**IF [Y]: YES:**
Load, read entire file, then execute `./step-v-04b-audit.md`

**IF [M]: MODIFY:**
Return to step 2 (user selects date range, etc.)

**EXECUTION RULE:**
ALWAYS halt and wait for user input after presenting menu. ONLY proceed when user makes a selection.
---

## SAVED DATA

Store loaded posts for copy audit:
```json
{
  "validation_session_id": "v-04-[timestamp]",
  "loaded_posts": 22,
  "date_range": "2024-01-01 to 2024-01-28",
  "posts": [
    {"id": 1, "title": "...", "content": "...", "word_count": 450},
    ...
  ]
}
```

---

## NEXT STEP

Audit copywriting quality: action verbs, specificity, benefits, language, CTAs

