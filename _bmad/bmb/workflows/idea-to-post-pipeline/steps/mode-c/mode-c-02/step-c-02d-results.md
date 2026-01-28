---
description: Display detailed research results (all angles with sources)
name: step-c-02d-results
nextStepFile: ../../mode-c/mode-c-03/step-c-03a-select-idea.md
type: results-display
---

## DATA REFERENCE

All angles accessible from ideas_research.csv for future use.

---

## NEXT STEP

Handle user selection and route to writing step

**EXECUTION RULE:**
ALWAYS halt and wait for user input after presenting menu. ONLY proceed when user makes a selection.

---

# CREATE C-02: Research - Results

## STEP GOAL:

Display detailed research results with all angles, sources, and facts.

## EXECUTION:

### 1. Display Results Header

```
═══════════════════════════════════════════════════════════════

  📊 RESEARCH RESULTS: "ИИ контент за 3 часа"

═══════════════════════════════════════════════════════════════

Total angles found: 8
Average relevance: 86%
Total sources: 32
Research time: 18 minutes
```

### 2. Show All Angles in Detail

```
ANGLE 1: Time Saving ⏱️  [Relevance: 92%] ⭐⭐⭐⭐⭐
─────────────────────────────────────────────────
Insight: "Saves 70% of content creation time"

Key Facts:
  • Traditional copywriter: 2-3 hours per post
  • With ИИ assistance: 20-30 minutes per post
  • Productivity gain: 70-75% time savings

Sources (7 found):
  1. "The State of AI in Content Creation 2025" - TechCrunch
  2. Case study: "How Company X Scaled with ИИ" - LinkedIn
  3. Research: "Productivity gains with generative ИИ" - McKinsey
  ... (4 more sources)

Best for: Founders, busy professionals, agencies
Post angle: "3 часа вместо недели..."

─────────────────────────────────────────────────

ANGLE 2: Quality Control 🎯  [Relevance: 88%] ⭐⭐⭐⭐
─────────────────────────────────────────────────
Insight: "ИИ content can be higher quality with proper editing"

Key Facts:
  • Quality depends heavily on prompts
  • Human editing adds personal voice
  • Hybrid approach: ИИ + editing yields best results

Sources (5 found):
  1. "Best practices for ИИ-assisted writing" - Copyblogger
  2. Study: "Quality assessment of AI-generated content" - Harvard
  ... (3 more sources)

Best for: Quality-focused brands, perfectionists
Post angle: "ИИ контент не значит плохой контент..."

─────────────────────────────────────────────────

[Continue for all 8 angles...]

═════════════════════════════════════════════════════════════════
```

### 3. Present Choices

```
Что дальше?

[1-8] SELECT ANGLE — Выбери угол для написания поста
[W] WRITE ANY — Напиши пост (я выберу лучший угол)
[M] Back to MENU — Вернуться в меню

═════════════════════════════════════════════════════════════════
```

**[1-8] SELECT ANGLE:**
User selects which angle to use for writing. Load, read entire file, then execute `../mode-c-03/step-c-03b-select-angle.md` with selected angle

**[W] WRITE ANY:**
Auto-select best angle (highest relevance) and proceed to writing. Load `../mode-c-03/step-c-03b-select-angle.md`

**[M] Back to MENU:**
Load `../mode-c-00-menu.md`

---

## DATA REFERENCE

All angles accessible from ideas_research.csv for future use.

---

## NEXT STEP

Handle user selection and route to writing step
