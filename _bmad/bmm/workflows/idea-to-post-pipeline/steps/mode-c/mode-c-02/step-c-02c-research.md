---
description: Execute research - find 5-8 angles with sources and facts
name: step-c-02c-research
nextStepFile: ./step-c-02d-results.md
type: research-execution
---

## SAVED DATA

Results saved to ideas_research.csv:
```csv
id,original_idea_id,research_date,main_angle,sub_angles_count,best_angle_id,angles_list,sources_count,avg_relevance
1,1,[today],"Time Saving via ИИ",8,"angle_1",[list of angles],32,86
```

---

## NEXT STEP

Handle user selection from step 4

**EXECUTION RULE:**
ALWAYS halt and wait for user input after presenting menu. ONLY proceed when user makes a selection.

---

# CREATE C-02: Research - Execute

## STEP GOAL:

Research the selected idea and find 5-8 different angles with supporting sources.

## EXECUTION:

### 1. Display Research Start

```
═══════════════════════════════════════════════════════════════

  🔍 RESEARCHING: "ИИ контент за 3 часа"

  Поиск углов, источников и фактов...

═══════════════════════════════════════════════════════════════
```

### 2. Research Process

Using web search + analysis, find angles like:

```
ANGLE 1: Time Saving ⏱️
├─ Main insight: "Saves 70% of content creation time"
├─ Sources found: 7 (news articles, blogs, studies)
├─ Key facts:
│  • Average copywriter: 2-3 hours per post
│  • With ИИ: 20-30 minutes per post
│  • Relevance: 92% (highly relevant)
└─ Best for: Founders, agencies, busy entrepreneurs

ANGLE 2: Quality Control 🎯
├─ Main insight: "ИИ content can be higher quality if well-guided"
├─ Sources found: 5 (studies, case studies)
├─ Key facts:
│  • Quality depends on prompts and editing
│  • Best practice: ИИ write → human edit
│  • Relevance: 88% (relevant)
└─ Best for: Perfectionists, detail-oriented teams

ANGLE 3: Scalability 📈
├─ Main insight: "Create unlimited variations without hiring"
├─ Sources found: 6 (business blogs, research)
├─ Key facts:
│  • Hiring writer: $2000-5000/month
│  • ИИ subscription: $20-40/month
│  • Relevance: 85% (relevant)
└─ Best for: Growth-focused businesses

ANGLE 4: Learning Tool 📚
├─ Main insight: "Using ИИ teaches you better copywriting"
├─ Sources found: 4 (opinion pieces, educational)
├─ Key facts:
│  • ИИ shows different writing styles
│  • Forces you to refine your prompts
│  • Relevance: 78% (relevant)
└─ Best for: Aspiring copywriters, learners

...and so on (up to 8-10 angles)
```

### 3. Aggregate Results

```
═══════════════════════════════════════════════════════════════

  ✅ RESEARCH COMPLETE

  Found: 8 different angles
  Sources: 32 total (average 4 per angle)
  Avg relevance: 86% (GOOD)
  Time: 18 minutes

═════════════════════════════════════════════════════════════════

Результаты сохранены в ideas_research.csv
```

### 4. Offer Next Steps

```
Что дальше?

[W] WRITE — Написать пост из одного из этих углов
[A] ANGLES — Посмотреть все углы в деталях
[M] Back to MENU — Вернуться в меню

═════════════════════════════════════════════════════════════════
```

**[W] WRITE:**
Load, read entire file, then execute `../mode-c-03/step-c-03a-select-idea.md`

**[A] ANGLES:**
Load, read entire file, then execute `./step-c-02d-results.md`

**[M] Back to MENU:**
Load `../mode-c-00-menu.md`

---

## SAVED DATA

Results saved to ideas_research.csv:
```csv
id,original_idea_id,research_date,main_angle,sub_angles_count,best_angle_id,angles_list,sources_count,avg_relevance
1,1,[today],"Time Saving via ИИ",8,"angle_1",[list of angles],32,86
```

---

## NEXT STEP

Handle user selection from step 4
