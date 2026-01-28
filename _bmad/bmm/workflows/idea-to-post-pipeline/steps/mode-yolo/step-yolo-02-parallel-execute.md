---
description: Execute all operations in parallel (add ideas, research, write posts, validate)
name: step-yolo-02-parallel-execute
nextStepFile: ./step-yolo-03-self-check.md
type: parallel-execution
yoloParameters: (passed from step-yolo-01-input)
---

# YOLO Step 2: Parallel Execution Engine

## STEP GOAL:

Execute all requested operations (add ideas, research, write posts) in parallel using sub-agents and subprocesses for maximum speed.

## MANDATORY EXECUTION RULES:

### Universal Rules:
- 🛑 NEVER wait for sequential completion
- 📖 CRITICAL: Read entire step file before execution
- 🔄 Execute all independent tasks simultaneously
- 📋 Track progress for all parallel tasks

### Role Reinforcement:
- ✅ You are a Parallel Execution Coordinator
- ✅ Spawn sub-agents for research and writing
- ✅ Monitor all tasks simultaneously
- ✅ Collect results as they complete

### Step-Specific Rules:
- 🎯 Focus ONLY on parallel execution
- 🚫 FORBIDDEN to execute sequentially (unless user specified)
- 💬 Show real-time progress updates
- 📋 Aggregate results into structured format

## EXECUTION PROTOCOLS:

### HALT AND WAIT RULES

**ALWAYS halt and wait for user input after presenting menu or asking for selection.**
**ONLY proceed to next step when user provides explicit input/selection.**

- 🎯 Display execution start
- 💾 Spawn parallel sub-agents/processes
- 📖 Track completion of all tasks
- 🚫 Do NOT wait for one task before starting next

---

## MANDATORY SEQUENCE

### 1. Display Execution Start

```
═══════════════════════════════════════════════════════════════

  🚀 STARTING PARALLEL EXECUTION

═══════════════════════════════════════════════════════════════

Параллельно запускаю все операции...

Это займёт 3-5 минут вместо 6-8 часов! ⚡

═══════════════════════════════════════════════════════════════
```

### 2. Spawn Parallel Sub-Agents

**IF add_ideas = true:**
```
┌─────────────────────────────────────────┐
│ SUB-TASK 1: Add Ideas (Parallel)         │
├─────────────────────────────────────────┤
│ Adding [ideas_count] ideas to inbox...   │
│                                          │
│ ✅ Idea #1: [title]                     │
│ ✅ Idea #2: [title]                     │
│ ... (all in parallel, not sequential)    │
│                                          │
│ Status: COMPLETED (5 sec)                │
└─────────────────────────────────────────┘
```

**IF research = true:**
```
┌─────────────────────────────────────────┐
│ SUB-TASK 2: Research Ideas (Parallel)    │
├─────────────────────────────────────────┤
│ Researching [ideas_count] ideas...       │
│                                          │
│ Sub-Agent 1: Web search Idea #1          │
│  └─ Found 7 sources                      │
│  └─ Extracted 8 angles (relevance 78-92%)│
│  └─ Status: DONE (45 sec)                │
│                                          │
│ Sub-Agent 2: Web search Idea #2          │
│  └─ Found 6 sources                      │
│  └─ Extracted 7 angles (relevance 75-87%)│
│  └─ Status: DONE (42 sec)                │
│                                          │
│ Sub-Agent 3: Web search Idea #3          │
│  └─ Found 8 sources                      │
│  └─ Extracted 9 angles (relevance 81-94%)│
│  └─ Status: DONE (48 sec)                │
│                                          │
│ Status: ALL DONE (45 sec total, not 2+ hours!) ⚡
└─────────────────────────────────────────┘
```

**IF write_posts = true:**
```
┌─────────────────────────────────────────┐
│ SUB-TASK 3: Write Posts (Parallel)       │
├─────────────────────────────────────────┤
│ Writing [total_posts] posts in parallel..│
│                                          │
│ Process Group 1: Idea #1 - 3 angles      │
│  ├─ Sub-Process 1a: Write angle_1 (500) │
│  ├─ Sub-Process 1b: Write angle_2 (500) │
│  └─ Sub-Process 1c: Write angle_3 (500) │
│  Status: ALL 3 DONE (30 sec)             │
│                                          │
│ Process Group 2: Idea #2 - 3 angles      │
│  ├─ Sub-Process 2a: Write angle_1 (500) │
│  ├─ Sub-Process 2b: Write angle_2 (500) │
│  └─ Sub-Process 2c: Write angle_3 (500) │
│  Status: ALL 3 DONE (32 sec)             │
│                                          │
│ Process Group 3: Idea #3 - 3 angles      │
│  ├─ Sub-Process 3a: Write angle_1 (500) │
│  ├─ Sub-Process 3b: Write angle_2 (500) │
│  └─ Sub-Process 3c: Write angle_3 (500) │
│  Status: ALL 3 DONE (28 sec)             │
│                                          │
│ Status: ALL POSTS DONE (32 sec, not 2+ hours!) ⚡
└─────────────────────────────────────────┘
```

### 3. Aggregate Results

Collect all results into structured format:

```json
{
  "execution_id": "yolo-run-2026-01-27-21-45",
  "execution_time_seconds": 125,

  "ideas_added": [
    {"id": 1, "title": "ИИ контент", "category": "automation"},
    {"id": 2, "title": "Speech-to-text", "category": "tech"},
    {"id": 3, "title": "Масштабирование", "category": "market"}
  ],

  "research_results": [
    {
      "idea_id": 1,
      "angles_found": 8,
      "sources_count": 7,
      "angles": [
        {"id": "a1", "title": "Экономия времени", "relevance": 92},
        {"id": "a2", "title": "Масштабирование", "relevance": 88},
        ...
      ]
    },
    ...
  ],

  "posts_written": [
    {
      "idea_id": 1,
      "angle_id": "a1",
      "post_id": "post_001",
      "version": 1,
      "content_500": "...",
      "content_250": "...",
      "content_100": "..."
    },
    ...
  ]
}
```

### 4. Display Execution Summary

```
═══════════════════════════════════════════════════════════════

  ✅ PARALLEL EXECUTION COMPLETE!

═══════════════════════════════════════════════════════════════

Результаты:

  📋 Добавлено идей: [ideas_count]
  🔍 Найдено углов: [total_angles]
  📝 Написано постов: [total_posts]

  Время выполнения: 2 мин 5 сек ⚡
  (вместо 6-8 часов вручную!)

═══════════════════════════════════════════════════════════════

Переходим к автоматической проверке качества...
```

---

## SUCCESS CRITERIA

- ✅ All parallel tasks started simultaneously
- ✅ No sequential waiting between independent tasks
- ✅ Results collected and aggregated
- ✅ Ready for validation step

---

## NEXT STEP

Load, read entire file, then execute `./step-yolo-03-self-check.md`
