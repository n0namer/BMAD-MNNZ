---
description: Load multiple posts for consistency analysis
name: step-v-03a-load
nextStepFile: ./v-03b-analyze.md
type: data-loading
---

# VALIDATE V-03A: Load Posts for Consistency Check

## STEP GOAL:

Load multiple posts to analyze cross-post consistency: tone, brand voice, messaging, style.

## EXECUTION:
### EXECUTION RULES - HALT AND WAIT

**ALWAYS halt and wait for user input after presenting menu or asking for selection.**
**ONLY proceed to next step when user provides explicit input/selection.**


### 1. Display Loading Status

```
═══════════════════════════════════════════════════════════════

  🎯 VALIDATE V-03: CONSISTENCY CHECK

  Loading posts for consistency analysis...

═══════════════════════════════════════════════════════════════
```

### 2. Load Posts from Database

Query `posts.csv`:
- Status: `published` or `draft`
- Date range: last 30 days (or user-specified)
- Minimum: 8+ posts for meaningful consistency check

Example output:
```
Loaded 20 posts (last 30 days):

├─ Post #1: "5 Ways to Increase..." [2024-01-15] 450 words
├─ Post #2: "Common Mistake When..." [2024-01-14] 380 words
├─ Post #3: "Why Most People Fail..." [2024-01-13] 520 words
├─ Post #4: "The Hidden Cost of..." [2024-01-12] 410 words
...
└─ Post #20: "Complete Guide to..." [2024-01-01] 890 words

Ready for consistency analysis.
```

### 3. Display Analysis Scope

```
CONSISTENCY SCOPE:
  Total posts: 20
  Date range: Jan 1-15, 2024
  Analysis focus: Tone, brand voice, messaging, style
  Minimum sample: 20 posts ✅

Ready to analyze consistency across posts.
```

### 4. Confirmation

```
Proceed with consistency check?

[Y] YES — Начать проверку консистентности
[M] MODIFY — Изменить диапазон постов
[?] BACK — Вернуться в меню

═══════════════════════════════════════════════════════════════
```

**[Y] YES:**
Load, read entire file, then execute `./step-v-03b-analyze.md`

**[M] MODIFY:**
Return to step 2 (user selects date range, quantity, etc.)

**[?] BACK:**
Load `./v-00-menu.md`


### Menu Handling Logic

**IF [Y]: YES:**
Load, read entire file, then execute `./step-v-03b-analyze.md`

**IF [M]: MODIFY:**
Return to step 2 (user selects date range, quantity, etc.)

**EXECUTION RULE:**
ALWAYS halt and wait for user input after presenting menu. ONLY proceed when user makes a selection.
---

## SAVED DATA

Store loaded posts in validation session:
```json
{
  "validation_session_id": "v-03-[timestamp]",
  "loaded_posts": 20,
  "date_range": "2024-01-01 to 2024-01-15",
  "posts": [
    {"id": 1, "title": "...", "content": "...", "tone": "...", "word_count": 450},
    ...
  ]
}
```

---

## NEXT STEP

Analyze consistency: tone across posts, brand voice, messaging alignment, style

