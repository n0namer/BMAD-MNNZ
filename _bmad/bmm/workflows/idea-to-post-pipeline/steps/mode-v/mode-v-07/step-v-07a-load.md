---
description: Load raw ideas from ideas_inbox for pre-research validation
name: step-v-07a-load
nextStepFile: ./step-v-07b-checks.md
type: data-loading
---

# VALIDATE V-07A: Load Ideas for Validation

## STEP GOAL:

Load raw ideas from ideas_inbox.csv for pre-research validation to identify viable ideas before investing research time.

## EXECUTION:
### EXECUTION RULES - HALT AND WAIT

**ALWAYS halt and wait for user input after presenting menu or asking for selection.**
**ONLY proceed to next step when user provides explicit input/selection.**


### 1. Display Loading Status

```
═══════════════════════════════════════════════════════════════

  💡 VALIDATE V-07: VALIDATE IDEAS

  Loading raw ideas from inbox...

═══════════════════════════════════════════════════════════════
```

### 2. Load Ideas from Inbox

Query `ideas_inbox.csv`:
- Status: `active` (not archived)
- Focus: Raw ideas (not yet researched)
- Quantity: all unvalidated ideas

Example output:
```
Loaded 47 active ideas:

Idea #1: "The future of AI in education" [2024-01-25]
Idea #2: "How to build better habits" [2024-01-24]
Idea #3: "Common mistakes in learning React" [2024-01-23]
Idea #4: "Why remote work is failing" [2024-01-22]
...
Idea #47: "The psychology of productivity" [2024-01-01]

Ready for validation.
```

### 3. Display Scope

```
IDEA VALIDATION SCOPE:
  Total active ideas: 47
  Status: New/unvalidated
  Validation focus: Viability for research and writing
  Criteria: Specificity, researchability, audience clarity, uniqueness

Ready to validate ideas before research phase.
```

### 4. Confirmation

```
Proceed with idea validation?

[Y] YES — Начать валидацию идей
[F] FILTER — Выбрать диапазон идей
[?] BACK — Вернуться в меню

═══════════════════════════════════════════════════════════════
```

**[Y] YES:**
Load, read entire file, then execute `./step-v-07b-checks.md`

**[F] FILTER:**
Return to step 2 (user selects date range, categories, etc.)

**[?] BACK:**
Load `../mode-v-00-menu.md`


### Menu Handling Logic

**IF [Y]: YES:**
Load, read entire file, then execute `./step-v-07b-checks.md`

**IF [F]: FILTER:**
Return to step 2 (user selects date range, categories, etc.)

**EXECUTION RULE:**
ALWAYS halt and wait for user input after presenting menu. ONLY proceed when user makes a selection.
---

## SAVED DATA

Store loaded ideas for validation:
```json
{
  "validation_session_id": "v-07-[timestamp]",
  "loaded_ideas": 47,
  "ideas": [
    {"id": 1, "title": "The future of AI in education", "description": "...", "date_added": "2024-01-25"},
    ...
  ]
}
```

---

## NEXT STEP

Validate ideas: specificity, researchability, audience clarity, uniqueness

