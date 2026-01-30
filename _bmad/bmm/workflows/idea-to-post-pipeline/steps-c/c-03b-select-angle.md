---
description: User selects which angle (from research) to use for the post
name: step-c-03b-select-angle
nextStepFile: ./c-03b1-offer-check.md (for demo) OR ./c-03c-draft.md (for normal)
type: selection
---

# CREATE C-03: Write Post - Select Angle

## STEP GOAL:

User selects which research angle to develop into a post.

## EXECUTION:
### EXECUTION RULES - HALT AND WAIT

**ALWAYS halt and wait for user input after presenting menu or asking for selection.**
**ONLY proceed to next step when user provides explicit input/selection.**


### 1. Display Angles from Research

Load angles from ideas_research.csv for selected idea.

### 2. Show Angle Options

```
═══════════════════════════════════════════════════════════════

  💡 WRITE POST: Select Angle

  Идея: "ИИ контент за 3 часа"
  Найдено углов: 8

═════════════════════════════════════════════════════════════════

Какой угол развить в пост?

[1] Time Saving ⏱️  [Relevance: 92%] ⭐ BEST
    "Saves 70% of content creation time"

[2] Quality Control 🎯  [Relevance: 88%]
    "ИИ content can be higher quality with proper editing"

[3] Scalability 📈  [Relevance: 85%]
    "Create unlimited variations without hiring"

[4] Learning Tool 📚  [Relevance: 78%]
    "Using ИИ teaches you better copywriting"

[5] Cost Savings 💰  [Relevance: 82%]
    "ИИ subscription is 100x cheaper than hiring"

[6] Personal Touch 🎨  [Relevance: 76%]
    "ИИ handles bulk work, you add creativity"

[7] Competitive Advantage 🏆  [Relevance: 84%]
    "Early adopters get huge head start"

[8] Emotional Appeal 💪  [Relevance: 79%]
    "Freedom from burnout of manual content"

─────────────────────────────────────────────────────────────

[A] AUTO-SELECT — Выбрать лучший угол (#1)
[?] DETAILS — Показать детали каждого угла
[M] Back to MENU

═════════════════════════════════════════════════════════════════
```

### 3. Handle Selection

**[1-8] Select angle:**
```
Выбрал угол: Time Saving ⏱️

Переходим дальше...
```

**CONDITIONAL ROUTING (Content Machine Integration):**

```
IF content_type == "demo":
  Сейчас перейдём к настройке профиля офферов!
  Load, read entire file, then execute `./c-03b1-offer-check.md`
  (Stage 4: FILTER — настройка профиля офферов)

ELSE (content_type != "demo"):
  Сейчас начнём писать варианты!
  Load, read entire file, then execute `./c-03c-draft.md`
  (Stage 5: OUTPUT — написание 3 вариантов)
```

**[A] AUTO-SELECT:**
Auto-select angle [1] (best relevance) and proceed with same conditional routing

**[?] DETAILS:**
Display more info about each angle (sources, key facts)

**[M] Back to MENU:**
Load `./c-00-menu.md`

---

## NEXT STEP

**Conditional Next Step (Content Machine Aware):**

When angle selected:

**IF content_type == "demo":**
  - Load, read entire file, then execute `./c-03b1-offer-check.md`
  - Flow: angle selection → offer filter → offer generation → draft writing

**IF content_type != "demo":**
  - Load, read entire file, then execute `./c-03c-draft.md`
  - Flow: angle selection → draft writing (3 variants)

---

**EXECUTION RULE:**
ALWAYS halt and wait for user input after presenting menu. ONLY proceed when user makes a selection.
