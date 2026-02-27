---
name: 'step-x-01c-today-view'
description: 'Display today\'s TODOs with progress tracking for active projects'
nextStepFile: './step-x-02-weekly-pulse.md'
workflowPlanFile: '{bmb_creations_output_folder}/life-os/workflow-plan-life-os.md'
portfolioFile: '{bmb_creations_output_folder}/life-os/portfolio.md'
metricsFile: '{bmb_creations_output_folder}/life-os/metrics/metrics.md'
estimatedDuration: '2-5 minutes'
dataFiles:
  templates: '../data/today-view-templates.md'
  filters: '../data/task-filtering-rules.md'
  balancing: '../data/energy-level-balancing.md'
  calendar: '../data/calendar-integration-guide.md'
---

# Execution Step X-01c: Today View

## STEP GOAL

Display today's focused TODO list with progress tracking for all active projects. Show what needs to be done TODAY, current progress, blockers, and recommended next actions.

## WHEN TO USE

- **Morning standup:** Start of day - what's the focus?
- **Mid-day check-in:** Progress review and adjustment
- **End of day:** Completion status and tomorrow prep
- **On-demand:** Any time user needs to see today's work

## MANDATORY EXECUTION RULES (READ FIRST)

### Universal Rules
- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`

### Step-Specific Rules
- 🎯 Load today's tasks from execution trackers
- 🎯 Use subprocess for today view generation (Pattern 2: LLM Operations)
- 💬 Return structured today view, not raw tracker files
- 📊 Show progress metrics (X/Y tasks done)
- 🚦 Highlight blockers and at-risk items
- 💡 Recommend priority order for remaining tasks
- ✅ Allow task completion marking
- ⏱️  Keep view focused on TODAY only (not future tasks)

## EXECUTION PROTOCOLS

### Proactive Advice & Best Practices
- If user asks for productivity advice, use Search Orchestrator to retrieve best practices
- Provide time management recommendations based on task load

### Search Orchestrator Protocol (Optional)
- Follow data/search-decision-protocol.md
- Execute: CLI memory search → local MD (rg) → web/MCP
- Use for: daily productivity patterns, time management strategies

## CONTEXT BOUNDARIES

- Available context: execution trackers for active projects, {portfolioFile}, {metricsFile}
- Focus: TODAY's tasks only (current date)
- Time horizon: Current day (00:00 - 23:59)
- Action: Can mark tasks complete, update blockers

## DATA FILE REFERENCES

📖 **Report templates:** `{dataFiles.templates}` - View structure, emoji reference, subprocess schema
📖 **Filtering rules:** `{dataFiles.filters}` - Task/project filters, sort order, calculations
📖 **Energy balancing:** `{dataFiles.balancing}` - Time block allocation, capacity rules
📖 **Calendar integration:** `{dataFiles.calendar}` - Sync patterns, event templates (future)

## MANDATORY SEQUENCE

### 1. Load Today's Tasks (Subprocess)

**Launch a subprocess that:**
1. Loads {portfolioFile} (active projects list)
2. Loads execution tracker files for all IN_PROGRESS projects
3. Loads {metricsFile} (today's logged progress if any)
4. Filters tasks using rules from `{dataFiles.filters}`
5. Applies energy-level balancing from `{dataFiles.balancing}`
6. Returns structured today view (schema in `{dataFiles.templates}`)

**Context savings:** ~2,500 lines (all execution trackers + portfolio) → ~500 lines (today's tasks)

**Graceful fallback:** If subprocess unavailable, load execution tracker files and filter manually using `{dataFiles.filters}`.

---

### 2. Generate Today View Report

**Render report using template from `{dataFiles.templates}`**

Include:
- Progress summary with metrics
- Focus recommendation (from subprocess)
- Time block allocations (morning/afternoon/evening)
- Tasks grouped by priority (overdue → high → medium → low)
- Blocker summary with severity and recommendations
- Productivity tips

**Visual formatting:**
- Status emoji: ✅ 🔄 ⏸️ 🔴 (see `{dataFiles.templates}`)
- Keep report to 1-2 screen lengths

---

### 3. Display Menu Options

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

What would you like to do?

[✓] Mark task complete     - Update task status to done
[+] Add task               - Quick-add task for today
[B] Report blocker         - Flag blocker for task
[U] Update progress        - Log time spent or notes
[R] Refresh                - Reload today view
[D] Details                - View full project tracker
[E] End of day             - Day summary and tomorrow prep
[C] Continue               - Proceed to weekly pulse

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### 4. Menu Handling Logic

**[✓] Mark task complete:**
1. Ask task ID → Validate → Confirm
2. Update execution tracker: status=COMPLETED, completion_date=today
3. Calculate actual time spent if not logged
4. Check if milestone completed (all milestone tasks done)
5. Store completion in memory
6. Refresh today view

**[+] Add task:**
1. Ask: project, title, priority, estimated hours
2. Add task to execution tracker
3. Refresh today view

**[B] Report blocker:**
1. Ask: task ID, blocker description, severity
2. Update execution tracker + store in memory
3. Refresh today view

**[U] Update progress:**
1. Ask: task ID, time spent, progress note
2. Update execution tracker
3. Refresh today view

**[R] Refresh:**
- Re-execute Section 1 (reload data)
- Re-display today view

**[D] Details:**
- Ask: project ID/name
- Load full execution tracker for selected project
- Display all tasks, milestones, timeline
- Return to today view menu

**[E] End of day:**
- Calculate completion rate
- Ask: reflection + tomorrow's priority
- Save daily summary to {metricsFile} + memory
- Display: "Great work today! Tomorrow's focus: {priority}"
- Exit to main menu

**[C] Continue:**
- Load, read entire file, then execute {nextStepFile}

---

### 5. Save Daily Progress

**After any task completion or end-of-day:**

```bash
# Append to metrics file
cat >> "{metricsFile}" << EOF

## Daily Progress - $(date +%Y-%m-%d)

- **Completion Rate:** {completion_rate}%
- **Tasks Completed:** {completed}/{total}
- **Time Spent:** {actual_hours}h (Estimated: {estimated_hours}h)
- **Reflection:** {reflection_notes}
- **Tomorrow's Priority:** {tomorrow_priority}

EOF

# Store in memory
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "execution:daily:{date}" \
  --content "{date, completion_rate, tasks_completed, reflection, blockers}"
```

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS
- Today's tasks loaded and analyzed in subprocess
- Clear focus recommendation provided
- Tasks grouped by priority with time estimates
- Progress metrics visible at-a-glance
- Blockers highlighted and actionable
- User can complete daily work efficiently (<5 min to review)
- Task completion tracking integrated
- End-of-day reflection captured

### ❌ SYSTEM FAILURE
- Loading full execution trackers in main context (context waste)
- Not filtering for today's date (showing all tasks)
- Missing time estimates or priority levels
- No blocker detection or recommendations
- Allowing task completion without validation
- Not saving daily progress to memory
- Today view too verbose (>3 screens)

---

## INTEGRATION NOTES

**From Portfolio Dashboard (step-v-06):** User sees daily progress overview → clicks "View Today's Tasks" → lands here

**From Morning Routine:** User starts day → opens workflow → sees today's focused task list

**To Weekly Pulse (step-x-02):** User completes [C] Continue → proceeds to weekly review flow

---

## RELATED FILES

📖 Workflow plan: `{workflowPlanFile}`
📖 Portfolio: `{portfolioFile}`
📖 Metrics: `{metricsFile}`
📖 Execution trackers: `output/{idea-id}-execution-tracker.md`
📖 Next step: `{nextStepFile}` (Weekly Pulse)
📖 Data files: `{dataFiles.templates}`, `{dataFiles.filters}`, `{dataFiles.balancing}`, `{dataFiles.calendar}`

---

**Master Rule:** Keep user focused on TODAY only. Show clear priorities, progress metrics, and next actions. Make task completion seamless. Capture daily learnings for improvement.
