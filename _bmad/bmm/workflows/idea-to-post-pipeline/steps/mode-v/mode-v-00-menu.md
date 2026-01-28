---
name: mode-v-00-menu
type: mode-menu
description: VALIDATE Mode submenu with 8 operational options
nextStepFile: ./mode-v-01/step-v-01a-load.md

### Menu Handling Logic

**IF [A]: Advanced Elicitation:**
Execute Advanced Elicitation workflow, then return to this menu

**IF [P]: Party Mode:**
Execute Party Mode workflow, then return to this menu

**IF [M]: Back to MENU:**
Load `../step-00-menu.md` (back to 4-mode selection)

---

## VALIDATE MODE OVERVIEW

### What VALIDATE Does

VALIDATE is automated quality assurance mode - 90% of the work is done automatically, you review results and take action.

**EXECUTION RULE:**
ALWAYS halt and wait for user input after presenting menu. ONLY proceed when user makes a selection.

---

# VALIDATE MODE: Automated Quality Assurance Hub

## STEP GOAL:

Present VALIDATE Mode options and route user to selected operation.

## EXECUTION:

### 1. Display Mode Welcome

```
═══════════════════════════════════════════════════════════════

           ✅ VALIDATE MODE: Automated Quality Assurance

═══════════════════════════════════════════════════════════════

Здесь ты проверяешь качество контента, я помогаю:
  ✅ Проверяю качество постов (hook, CTA, tone)
  ✅ Анализирую производительность метрик
  ✅ Проверяю консистентность постов между собой
  ✅ Аудирую качество копирайтинга
  ✅ Прогнозирую потенциал взаимодействия
  ✅ Валидирую идеи перед исследованием
  ✅ Создаю полные отчёты валидации
  ✅ Автоматизирую все проверки качества

Взаимодействие: 90% автоматизировано (ты смотришь результаты)
Время цикла: 5-30 минут (зависит от объёма)
Качество: 95%+ (автоматизированная валидация)

═══════════════════════════════════════════════════════════════
```

### 2. Present Sub-Mode Menu

```
ВЫБЕРИ ЧТО ПРОВЕРИТЬ:

[1] 🔍 QUALITY CHECKLIST — Проверить качество постов
    Hook strength, problem clarity, solution relevance,
    CTA clarity, tone consistency → Pass/Fail report

[2] 📊 PERFORMANCE AUDIT — Анализ метрик вовлечения
    CTR, engagement rate, comments, shares →
    Top/bottom performers + trends

[3] 🎯 CONSISTENCY CHECK — Проверить консистентность
    Tone, brand voice, messaging, style alignment →
    Consistency report with issues

[4] ✏️  COPY AUDIT — Аудит качества копирайтинга
    Action verbs, specific data, benefits, language, CTA →
    Copy score report with improvements

[5] ⚡ ENGAGEMENT CHECK — Прогноз потенциала взаимодействия
    Urgency, curiosity, specificity, emotion, social proof →
    1-5 star engagement prediction

[6] 🚀 BATCH VALIDATE — Валидировать ВСЕ сразу
    Запуск всех проверок (V-01 to V-05) в параллель →
    Comprehensive batch report

[7] 💡 VALIDATE IDEAS — Проверить жизнеспособность идей
    Specificity, researchability, audience, uniqueness →
    Proceed/Revise/Skip recommendations

[8] 📈 VALIDATION REPORT — Полный отчёт валидации
    Компилировать данные + генерировать отчёт →
    Comprehensive quality dashboard

[?] HELP — Показать справку
[A] Advanced Elicitation — Глубокое изучение
[P] Party Mode — Мультиперспективное обсуждение
[M] Back to MENU — Вернуться в главное меню

═══════════════════════════════════════════════════════════════
```

### 3. Handle User Selection

**[1] QUALITY CHECKLIST:**
```
Проверяю качество постов...
```
Load, read entire file, then execute `./mode-v-01/step-v-01a-load.md`

**[2] PERFORMANCE AUDIT:**
```
Анализирую метрики производительности...
```
Load, read entire file, then execute `./mode-v-02/step-v-02a-load.md`

**[3] CONSISTENCY CHECK:**
```
Проверяю консистентность постов...
```
Load, read entire file, then execute `./mode-v-03/step-v-03a-load.md`

**[4] COPY AUDIT:**
```
Аудирую качество копирайтинга...
```
Load, read entire file, then execute `./mode-v-04/step-v-04a-load.md`

**[5] ENGAGEMENT CHECK:**
```
Прогнозирую потенциал взаимодействия...
```
Load, read entire file, then execute `./mode-v-05/step-v-05a-load.md`

**[6] BATCH VALIDATE:**
```
Запускаю полную валидацию всего контента...
```
Load, read entire file, then execute `./mode-v-06/step-v-06a-load.md`

**[7] VALIDATE IDEAS:**
```
Валидирую идеи перед исследованием...
```
Load, read entire file, then execute `./mode-v-07/step-v-07a-load.md`

**[8] VALIDATION REPORT:**
```
Компилирую данные и генерирую отчёт...
```
Load, read entire file, then execute `./mode-v-08/step-v-08a-compile.md`

**[?] HELP:**
Return to step 1 (redisplay this menu with explanations)

**[A] Advanced Elicitation:**
Execute Advanced Elicitation workflow, then return to this menu

**[P] Party Mode:**
Execute Party Mode workflow, then return to this menu

**[M] Back to MENU:**
Load `../step-00-menu.md` (back to 4-mode selection)

---

## VALIDATE MODE OVERVIEW

### What VALIDATE Does

VALIDATE is automated quality assurance mode - 90% of the work is done automatically, you review results and take action.

**Core Operations:**
1. **Load content** - Fetch posts/ideas from database
2. **Run automated checks** - AI analyzes against criteria
3. **Generate report** - Comprehensive results with scores
4. **Review & decide** - You choose which posts to fix
5. **Auto-archive data** - Results saved for future reference

### Sub-Mode Details

| # | Mode | What It Checks | Output | Time |
|---|------|---|---|---|
| 1 | Quality Checklist | Hook, problem, solution, CTA, tone | Pass/fail by criterion | 5-10 min |
| 2 | Performance Audit | CTR, engagement, comments, shares | Top/bottom performers | 5-10 min |
| 3 | Consistency Check | Tone, voice, messaging, style | Consistency score + issues | 5-10 min |
| 4 | Copy Audit | Action verbs, data, benefits, language | Copy score + improvements | 5-10 min |
| 5 | Engagement Check | Urgency, curiosity, emotion, proof | 1-5 star prediction | 5-10 min |
| 6 | Batch Validate | All of above (V-01 to V-05) | Comprehensive batch report | 10-15 min |
| 7 | Validate Ideas | Specificity, viability, uniqueness | Proceed/revise/skip | 5-10 min |
| 8 | Validation Report | All dimensions + compilation | 90-day action plan | 10-15 min |

### Typical Workflow

**Option A: Single Dimension Check**
- Run 1 sub-mode (V-01 through V-05)
- Review results (5-10 min)
- Take action on flagged items

**Option B: Batch Everything**
- Run batch validate (V-06)
- Get comprehensive overview (10-15 min)
- Decide what to fix

**Option C: Complete Assessment**
- Run validate ideas (V-07)
- Run batch validate (V-06)
- Run validation report (V-08)
- 90-day action plan complete (30 min)

### Key Features

**Autonomous:** 90% automated analysis, 10% human review
**Fast:** Most checks complete in 5-15 minutes
**Comprehensive:** Multiple quality dimensions analyzed
**Actionable:** Clear recommendations and priorities
**Archived:** All results saved for future reference

---

## CRITICAL RULES

- 🛑 ALWAYS halt and wait for user input
- 📋 ONLY proceed when user selects [1-8]
- 💬 If user selects [A] or [P], return to menu after completion
- 🚫 NEVER force user into a sub-mode
- ✅ ALWAYS explain what each sub-mode checks

---

## SUCCESS CRITERIA

- ✅ All 8 VALIDATE sub-modes clearly explained
- ✅ User understands which sub-mode fits their need
- ✅ Selection handled correctly and routed properly
- ✅ Can return to main menu anytime
- ✅ Results are clear, actionable, and archived

---

## NEXT STEP

When user selects [1-8]:
- Display confirmation
- Load, read entire file, then execute appropriate sub-mode file
- Maintain current session state
