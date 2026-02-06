---
description: Load ideas_inbox and display available ideas for research
name: step-c-02a-load-ideas
nextStepFile: ./c-02b-select-idea.md
type: data-loading
---

# CREATE C-02: Research - Load Ideas

## STEP GOAL:

Load ideas_inbox.csv and display available ideas that need research.

## EXECUTION:
### EXECUTION RULES - HALT AND WAIT

**ALWAYS halt and wait for user input after presenting menu or asking for selection.**
**ONLY proceed to next step when user provides explicit input/selection.**


### 1. Display Loading

```
═══════════════════════════════════════════════════════════════

  🔍 RESEARCH: Loading ideas...

═══════════════════════════════════════════════════════════════
```

### 2. Load Ideas Inbox

Load from ideas_inbox.csv, filter for:
- Status = "active" or "pending"
- Not yet researched (no entry in ideas_research.csv)

### 3. Display Available Ideas

```
Available ideas for research:

[1] "ИИ контент за 3 часа"
    Source: brainstorm | Category: automation | Added: 2026-01-27

[2] "Speech-to-text для постов"
    Source: conversation | Category: tech | Added: 2026-01-27

[3] "Масштабирование личного бренда"
    Source: research | Category: market | Added: 2026-01-27

[4] "A/B тестирование hooks"
    Source: internal | Category: methodology | Added: 2026-01-26

─────────────────────────────────────────────────────────────

Or:
[+] ADD NEW — Добавить новую идею сначала
[?] HELP — Показать справку
[M] Back to MENU — Вернуться в меню

═════════════════════════════════════════════════════════════
```

### 4. Wait for User Selection

User selects [1-N] to research that idea.

---

## NEXT STEP

Load, read entire file, then execute `./step-c-02b-select-idea.md`
