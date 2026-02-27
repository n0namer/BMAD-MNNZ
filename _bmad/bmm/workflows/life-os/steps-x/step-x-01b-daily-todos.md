---
name: 'step-x-01b-daily-todos'
description: 'Auto-generate daily task list from week plan, respecting capacity and energy levels'
nextStepFile: './step-x-02-weekly-pulse.md'
workflowPlanFile: '{bmb_creations_output_folder}/life-os/workflow-plan-life-os.md'
weekPlanFile: '{bmb_creations_output_folder}/life-os/projects/{project-id}/week-plan.md'
resourceAssessmentFile: '{bmb_creations_output_folder}/life-os/foundation/resource-assessment.md'
dailyTodosOutputFolder: '{bmb_creations_output_folder}/life-os/daily-todos/'
taskExtractionProtocol: '../data/task-extraction-protocol.md'
priorityAlgorithm: '../data/priority-calculation-algorithm.md'
capacityGuide: '../data/capacity-calculation-guide.md'
energyPatterns: '../data/energy-level-patterns.md'
---

# Step X-01b: Generate Daily TODOs

## STEP GOAL:

Generate a balanced daily task list from the week plan and active tasks, filtering by capacity (4-6 hours/day) and balancing by energy levels (morning/afternoon/evening).

## WHEN TO USE:

- **After Step X-01 (Kickoff):** Immediately after project transitions to IN_PROGRESS
- **Daily trigger:** Auto-generate at 8am for new day
- **Manual trigger:** User requests `/daily-todos` or "generate today's tasks"
- **Weekly review:** Regenerate for upcoming week during Step V-02 (Weekly Review)

## MANDATORY EXECUTION RULES (READ FIRST):

**Universal:** 🛑 Facilitator not generator | 📖 Read step first | 🔄 Read next step file completely | ✅ Use {communication_language}

**Step-Specific:** 🎯 Focus on daily TODO only | 📊 Respect capacity limits (4-6h) | ⚡ Balance energy (high→medium→low) | 🚫 No task creation/editing | 📅 Only today's date | 💬 Show balanced list | 🔄 Update completion tracking

## EXECUTION PROTOCOLS:

- 🎯 Load week plan for active projects
- 📊 Fetch active tasks (status=todo, project.status=ACTIVE) → See {taskExtractionProtocol}
- 🔢 Sort by priority + due_date + energy_level → See {priorityAlgorithm}
- ⚖️ Filter by capacity (sum ≤ 4-6 hours/day) → See {capacityGuide}
- ⚡ Balance by energy (Morning high, Afternoon medium, Evening low) → See {energyPatterns}
- 💾 Output to daily-todos/YYYY-MM-DD.md
- 📘 Save generation log to memory

### Search Orchestrator Protocol (Optional)
- If user needs task prioritization guidance, use Search Orchestrator
- Retrieve successful daily planning patterns from similar projects

## CONTEXT BOUNDARIES:

- Available context: week-plan.md, tasks/*, resource-assessment.md, workflow plan
- Focus: daily task allocation and energy balancing
- Dependencies: step-x-01 kickoff complete, at least one IN_PROGRESS project

## ALGORITHM (IDEAL v2.1)

```
1. Parse week plan → extract active projects and planned tasks
2. Fetch active tasks → {taskExtractionProtocol}
3. Sort tasks → {priorityAlgorithm}
4. Filter by capacity → {capacityGuide}
5. Balance energy levels → {energyPatterns}
6. Output to daily-todos/YYYY-MM-DD.md → structured markdown with energy blocks
7. Notify user → show summary + completion tracking
```

## MANDATORY SEQUENCE

### 1. Determine Target Date

**Default:** Today (YYYY-MM-DD format)
**Alternative:** User specifies date (e.g., "tomorrow", "2026-02-10")
**Format:** `TARGET_DATE=$(date +%Y-%m-%d)` or user-provided date

**Present:** "Generating daily TODOs for {TARGET_DATE}..."

### 2. Load Resource Capacity

**Read:** {resourceAssessmentFile} → extract `daily_capacity_hours` (typical: 4-6 hours)
**Fallback:** If file not found, default to 5 hours/day
**Present:** "Daily capacity: {X} hours (from resource assessment)"

### 3. Load Week Plan

**Read:** {weekPlanFile} for all IN_PROGRESS projects
**Extract:** Project ID, name, planned tasks for current week, tasks marked for {TARGET_DATE}
**Fallback:** If week plan not found, skip to Section 4 (fetch all active tasks)

### 4. Fetch Active Tasks

**Protocol:** Use {taskExtractionProtocol} for query logic and data structure
**Present:** "Found {N} active tasks across {M} projects"

### 5. Sort Tasks

**Algorithm:** Use {priorityAlgorithm} for 3-level priority sort
**Present:** "Sorted {N} tasks by priority, due date, and energy level"

### 6. Filter by Capacity

**Logic:** Use {capacityGuide} for capacity filtering algorithm
**Present:** "Selected {N} tasks totaling {X} hours (target: {capacity} hours)"

### 7. Balance by Energy Levels

**Algorithm:** Use {energyPatterns} for energy block definitions and balancing
**Present:** "Balanced: {X}h morning | {Y}h afternoon | {Z}h evening"

### 8. Generate Daily TODO File

**Filename:** `{dailyTodosOutputFolder}/YYYY-MM-DD.md`
**Format:**

```markdown
---
date: YYYY-MM-DD
total_tasks: N
total_hours: X.X
capacity_hours: Y
balance: "X%/Y%/Z% (morning/afternoon/evening)"
generated_at: "YYYY-MM-DD HH:MM:SS"
projects: [proj-1, proj-2, ...]
---

# Daily TODO - {Day of Week}, {Month} {Day}, {Year}

**Total:** {N} tasks | **Estimated:** {X} hours | **Capacity:** {Y} hours

---

## Morning (High Energy) - {N} tasks, {X} hours

**Focus time: 8am - 12pm**
**Energy:** Deep work, creativity, strategic thinking

- [ ] **[Project Name]** Task title (Est: Xh) [Priority: critical/high]
  - Due: YYYY-MM-DD | Energy: high
  - Context: Brief description or link

---

## Afternoon (Medium Energy) - {M} tasks, {Y} hours

**Focus time: 12pm - 5pm**
**Energy:** Collaboration, meetings, reviews

- [ ] **[Project Name]** Task title (Est: Xh) [Priority: medium]
  - Due: YYYY-MM-DD | Energy: medium
  - Context: Brief description or link

---

## Evening (Low Energy) - {K} tasks, {Z} hours

**Focus time: 5pm - 9pm**
**Energy:** Admin, cleanup, light tasks

- [ ] **[Project Name]** Task title (Est: Xh) [Priority: low]
  - Due: YYYY-MM-DD | Energy: low
  - Context: Brief description or link

---

## Completed Today: 0/{N}

**Progress:** ░░░░░░░░░░ 0%

### Completion Log
<!-- Mark tasks as complete with timestamp -->

---

## Notes & Blockers

<!-- Add notes, blockers, or adjustments during the day -->

---

## Tomorrow's Preview

**Pending tasks:** {X} tasks from other projects
**Upcoming deadlines:** {list tasks due tomorrow or soon}

---

_Generated by Life OS Step X-01b at {timestamp}_
```

**Validation:** File created successfully, all tasks rendered correctly, energy balance displayed
**Present:** "✅ Daily TODO file created: {filename}"

### 9. Save Generation Log to Memory

**Save:** `npx claude-flow@v3alpha memory store --namespace "shared-knowledge" --key "daily-todos:{TARGET_DATE}:generation-log" --content "{target_date, total_tasks, total_hours, capacity_hours, balance, projects, generated_at}"`

**Present:** "✅ Generation log saved to memory"

### 10. Present Summary

**Show:**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📅 DAILY TODO GENERATED - {Day}, {Month} {Day}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 **Summary:**
- Total Tasks: {N}
- Estimated Time: {X} hours (Capacity: {Y} hours)
- Balance: {X%} Morning | {Y%} Afternoon | {Z%} Evening

⚡ **Energy Distribution:**
- 🌅 Morning ({X}h): {list task titles}
- ☀️ Afternoon ({Y}h): {list task titles}
- 🌙 Evening ({Z}h): {list task titles}

📁 **Projects:**
- {Project 1}: {N} tasks
- {Project 2}: {M} tasks

✅ **File created:** daily-todos/{YYYY-MM-DD}.md

🚀 **Next Steps:**
- Review your daily TODO
- Start with morning high-energy tasks
- Track progress throughout the day
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 11. Quick Feedback & MENU OPTIONS

**Ask:** 👍 Helpful | 😐 OK | 👎 Frustrating [Type feedback or skip]
**Save:** `npx claude-flow@v3alpha memory store --namespace "user-context" --key "feedback:step-x-01b-daily-todos:{timestamp}" --content "{step, rating, comment, timestamp}"`

**Menu:** [V] View TODO file | [R] Regenerate (adjust tasks) | [N] Tomorrow's TODO | [T] Track Progress (X-02) | [D] Dashboard

**Logic:**
- V: Display full daily TODO file content
- R: Rerun algorithm with adjustments (add/remove tasks, rebalance)
- N: Generate tomorrow's TODO (TARGET_DATE = tomorrow)
- T: Save state, read entire `./step-x-02-weekly-pulse.md`, execute
- D: Show all IN_PROGRESS projects with today's tasks

**Rules:** Wait for input after menu | Only proceed when user selects action | Save before navigating

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- Daily TODO file created for target date
- Tasks filtered correctly (status=todo, project.status=ACTIVE)
- Tasks sorted by {priorityAlgorithm}
- Capacity respected per {capacityGuide}
- Energy balanced per {energyPatterns}
- Generation log saved to memory
- Summary presented to user

### ❌ SYSTEM FAILURE:
- Exceeding daily capacity (total_hours > capacity_hours)
- Unbalanced energy distribution (e.g., all high-energy tasks)
- Including completed or blocked tasks
- Missing task metadata (priority, estimate_hours, energy_level)
- Not saving generation log to memory
- Tasks from paused or archived projects included

**Master Rule:** Daily TODO must respect capacity, balance energy, and only include actionable tasks from active projects.

## INTEGRATION WITH OTHER STEPS

**Step X-01 (Kickoff):** After project kickoff, immediately call Step X-01b to generate first daily TODO
**Step X-02 (Tracking):** Reference daily TODO for progress updates
**Step V-02 (Weekly Review):** Regenerate daily TODOs for upcoming week during review
**Step V-01 (Daily Review):** Check today's TODO completion status

**Workflow routing:** Step X-01 (Kickoff) → Step X-01b (Generate Daily TODO) → Step X-02 (Tracking)
