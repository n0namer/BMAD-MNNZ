---
description: Execute all operations in parallel (add ideas, research, write posts, validate)
name: step-yolo-02-parallel-execute
nextStepFile: ./yolo-03-self-check.md
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
- 📖 Track completion of all tasks with real-time progress
- 🚫 Do NOT wait for one task before starting next
- 💡 Use result caching to avoid duplicate work
- ⚡ Batch similar operations for efficiency
- ♻️ Reuse agent pools instead of spawning new agents

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

### 2. Spawn Parallel Sub-Agents with Optimization

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

**IF research = true (OPTIMIZED):**
```
┌─────────────────────────────────────────┐
│ SUB-TASK 2: Research Ideas (Parallel)    │
├─────────────────────────────────────────┤
│ 💡 Checking cache for similar topics...  │
│  └─ Cache HIT: Idea #2 (87% similar)     │
│  └─ Reusing angles (save 42 sec) ⚡      │
│                                          │
│ 📦 Batching similar ideas:               │
│  └─ Batch 1: Tech-related (Ideas #1, #3)│
│  └─ Shared context (save 30% time)      │
│                                          │
│ ♻️ Agent Pool: 3 agents ready            │
│  └─ Reusing Agent 1 (no spawn delay)    │
│                                          │
│ Sub-Agent 1: Web search Idea #1          │
│  └─ Found 7 sources                      │
│  └─ Extracted 8 angles (relevance 78-92%)│
│  └─ Status: DONE (35 sec) ⚡ -22%        │
│                                          │
│ Sub-Agent 2: CACHE HIT Idea #2           │
│  └─ Loaded 6 cached angles               │
│  └─ Refreshed 2 new sources              │
│  └─ Status: DONE (8 sec) ⚡ -81%         │
│                                          │
│ Sub-Agent 1 (reused): Web search Idea #3│
│  └─ Shared batch context with Idea #1   │
│  └─ Found 8 sources                      │
│  └─ Extracted 9 angles (relevance 81-94%)│
│  └─ Status: DONE (30 sec) ⚡ -38%        │
│                                          │
│ 📊 Progress: [███████████████░░] 85%     │
│ Status: ALL DONE (35 sec, not 2+ hours!) ⚡
│ Optimization saved: 50 sec (58% faster)  │
└─────────────────────────────────────────┘
```

**IF write_posts = true (OPTIMIZED):**
```
┌─────────────────────────────────────────┐
│ SUB-TASK 3: Write Posts (Parallel)       │
├─────────────────────────────────────────┤
│ Writing [total_posts] posts in parallel..│
│                                          │
│ ♻️ Agent Pool: 6 pre-warmed agents       │
│  └─ No spawn delay (save 5 sec) ⚡       │
│                                          │
│ 📊 Real-time Progress Monitor:          │
│ [███████░░░░░░░░] 9/9 posts             │
│ Estimated completion: 18 sec remaining   │
│                                          │
│ Process Group 1: Idea #1 - 3 angles      │
│  ├─ Agent 1: Write angle_1 (500) [DONE 22s]│
│  ├─ Agent 2: Write angle_2 (500) [DONE 24s]│
│  └─ Agent 3: Write angle_3 (500) [DONE 20s]│
│  Status: ALL 3 DONE (24 sec) ⚡ -20%     │
│                                          │
│ Process Group 2: Idea #2 - 3 angles      │
│  ├─ Agent 4: Write angle_1 (500) [DONE 21s]│
│  ├─ Agent 5: Write angle_2 (500) [DONE 23s]│
│  └─ Agent 6: Write angle_3 (500) [DONE 19s]│
│  Status: ALL 3 DONE (23 sec) ⚡ -28%     │
│                                          │
│ Process Group 3: Idea #3 - 3 angles      │
│  ├─ Agent 1 (reused): Write angle_1 [DONE 18s]│
│  ├─ Agent 2 (reused): Write angle_2 [DONE 20s]│
│  └─ Agent 3 (reused): Write angle_3 [DONE 17s]│
│  Status: ALL 3 DONE (20 sec) ⚡ -29%     │
│                                          │
│ Status: ALL POSTS DONE (24 sec, not 2+ hours!) ⚡
│ Optimization saved: 8 sec (25% faster)   │
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

  Время выполнения: 1 мин 25 сек ⚡
  (вместо 6-8 часов вручную!)

  📈 Optimization Stats:
  • Cache hits: [N] results reused (save [X] sec)
  • Agent reuse: [N] agents recycled (save [Y] sec)
  • Batch processing: [N] grouped (save [Z] sec)
  • Total speedup: 40% faster than baseline ⚡

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
