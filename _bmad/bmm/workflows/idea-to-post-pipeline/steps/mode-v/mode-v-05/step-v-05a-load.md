---
description: Load posts for engagement potential prediction
name: step-v-05a-load
nextStepFile: ./step-v-05b-predict.md
type: data-loading
---

# VALIDATE V-05A: Load Posts for Engagement Check

## STEP GOAL:

Load posts to predict engagement potential based on factors: urgency, curiosity, specificity, emotional appeal, social proof.

## EXECUTION:
### EXECUTION RULES - HALT AND WAIT

**ALWAYS halt and wait for user input after presenting menu or asking for selection.**
**ONLY proceed to next step when user provides explicit input/selection.**


### 1. Display Loading Status

```
═══════════════════════════════════════════════════════════════

  ⚡ VALIDATE V-05: ENGAGEMENT CHECK

  Loading posts for engagement prediction...

═══════════════════════════════════════════════════════════════
```

### 2. Load Posts from Database

Query `posts.csv`:
- Status: `draft` (pre-publication) or `published`
- Focus: Posts that need engagement validation
- Quantity: 15-20 posts for meaningful analysis

Example output:
```
Loaded 18 posts:

Post #1: "5 Ways to Transform Your Productivity" [draft]
Post #2: "The Hidden Cost of Procrastination" [published]
Post #3: "Why Most People Fail at Fitness" [draft]
...
Post #18: "Complete Guide to React Hooks" [published]

Ready for engagement prediction.
```

### 3. Display Analysis Scope

```
ENGAGEMENT PREDICTION SCOPE:
  Total posts: 18
  Analysis focus: Engagement potential (predict 1-5 stars)
  Factors: Urgency, curiosity, specificity, emotional appeal, social proof
  Threshold: ≥3 stars = acceptable engagement potential

Ready to predict engagement potential.
```

### 4. Confirmation

```
Proceed with engagement check?

[Y] YES — Начать проверку потенциала взаимодействия
[M] MODIFY — Изменить диапазон постов
[?] BACK — Вернуться в меню

═══════════════════════════════════════════════════════════════
```

**[Y] YES:**
Load, read entire file, then execute `./step-v-05b-predict.md`

**[M] MODIFY:**
Return to step 2 (user selects posts/status, etc.)

**[?] BACK:**
Load `../mode-v-00-menu.md`


### Menu Handling Logic

**IF [Y]: YES:**
Load, read entire file, then execute `./step-v-05b-predict.md`

**IF [M]: MODIFY:**
Return to step 2 (user selects posts/status, etc.)

**EXECUTION RULE:**
ALWAYS halt and wait for user input after presenting menu. ONLY proceed when user makes a selection.
---

## SAVED DATA

Store loaded posts for engagement check:
```json
{
  "validation_session_id": "v-05-[timestamp]",
  "loaded_posts": 18,
  "posts": [
    {"id": 1, "title": "...", "content": "...", "status": "draft"},
    ...
  ]
}
```

---

## NEXT STEP

Predict engagement potential based on content factors

