---
name: 'step-07-calendar-sync'
description: 'Translate the approved project into a timeline and calendar plan'
nextStepFile: './step-08-deep-plan.md'
completeStepFile: './step-09-complete.md'
workflowPlanFile: '{bmb_creations_output_folder}/life-os/workflow-plan-life-os.md'
outputProjectFile: '{bmb_creations_output_folder}/life-os/projects/{project_id}.md'
snapshotsFolder: '{bmb_creations_output_folder}/life-os/snapshots'
journalFolder: '{bmb_creations_output_folder}/life-os/journal'
snapshotTemplate: '../templates/project-snapshot.template.md'
journalTemplate: '../templates/project-journal.template.md'
plansFolder: '{bmb_creations_output_folder}/life-os/plans'
planTemplate: '../templates/project-plan.template.md'
decisionsFolder: '{bmb_creations_output_folder}/life-os/decisions'
decisionsTemplate: '../templates/project-decisions.template.md'
calendarIntegrationMethodsRef: '../data/calendar-integration-methods.md'
calendarSyncProtocolsRef: '../data/calendar-sync-protocols.md'
calendarEventTemplatesRef: '../data/calendar-event-templates.md'
---

# Step 7: Calendar Sync

## STEP GOAL

Translate the approved project into a realistic timeline and capture it in a project file.

## MANDATORY EXECUTION RULES

### Universal Rules
- 🛑 NEVER generate content without user input
- 📖 Read the complete step file before taking any action
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ Communicate in your Agent style using `{communication_language}`

### Step-Specific Rules
- 🤝 Proactive guidance: highlight risks, opportunities, next best actions
- 🧭 Surface WIP/kill criteria or portfolio risks early with brief recommendation
- ✅ Ask user confirmation before changing scope or priorities
- 🎯 Focus ONLY on timeline and calendar alignment
- 🚫 FORBIDDEN to add new scope
- 💬 Confirm dates and capacity with user
- 💬 Ask 1-2 questions at a time, adapt to responses
- 🎯 Use subprocess for calendar event generation (Pattern 3: Data Operations)
- 💬 Return structured calendar events only

## EXECUTION PROTOCOLS

### Proactive Advice & Best Practices (MCP)
If user requests advice or recommendations:
1. Use MCP search (if available) to retrieve current guidance
2. Summarize findings concisely with sources
3. If MCP unavailable, provide best-effort guidance and note limitation

### Search Orchestrator Protocol (Required)
1. Follow `data/mcp_search_system_prompt_xml.md`
2. Execute: CLI memory search → local MD (rg) → web/MCP
3. Convene consilium to rank 2-4 options with pros/cons
4. Ask user to choose before proceeding

### Semantic Decision Support
If decision or prioritization unclear, use Search Orchestrator to rank 2-3 options.

### Core Deliverables
- 🎯 Confirm project readiness and start date
- 💾 Write project file to `{outputProjectFile}`
- 📖 Append timeline summary to `{workflowPlanFile}`
- 🧾 Record evidence snapshot in journal or workflow plan

## CONTEXT BOUNDARIES

- **Available context:** workflow plan (idea, consilium, scoring)
- **Focus:** scheduling and calendar alignment
- **Dependencies:** step-06 integration must be complete

## MANDATORY SEQUENCE

### 1. Confirm Schedule Inputs

Ask progressively (1-2 at a time):
- Target start date
- Target end date or duration
- Weekly capacity (hours/week)
- Milestones (if any)

**JIT Reference (if trade-offs unclear):** See `{calendarIntegrationMethodsRef}` for integration approaches.

**Validation:**
- End date before start date? → Ask to correct dates
- Capacity 0 or unrealistic? → Ask to clarify acceptable load

**Decision Support:** If unclear, use Search Orchestrator for 2-3 scheduling strategies.

### 2. Propose Timeline

Draft simple timeline with 3-6 milestones and confirm with user.

**JIT Reference (for sync methods):** See `{calendarSyncProtocolsRef}` for weekly sync, iCal export, or API integration protocols.

### 3. Generate Calendar Events (Subprocess)

**Launch a subprocess that:**
1. Loads Deep Plan L5 tasks from project plan
2. Extracts all tasks with timeline dependencies
3. Loads event templates from `{calendarEventTemplatesRef}`
4. Generates calendar events for:
   - Milestones (with reminder 7 days prior)
   - Capacity blocks (recurring work sessions)
   - Deadlines (with color-coding by priority)
   - Review points (weekly/bi-weekly checkpoints)
5. Returns structured event list with iCal format

**Subprocess returns:** Formatted event list (50-100 lines) instead of loading full calendar-event-templates.md (800+ lines).

**Graceful fallback:** If subprocess unavailable, load `{calendarEventTemplatesRef}` and manually select 3-5 template types relevant to timeline.

### 4. Create Project File

Write to `{outputProjectFile}`:

```markdown
---
projectId: {project_id}
title: {project_title}
status: PLANNED
startDate: {start_date}
endDate: {end_date}
capacityPerWeek: {hours}
---

# {project_title}

## Timeline
- {milestone}: {date}
- {milestone}: {date}

## Calendar Events
{subprocess_generated_events}

## Notes
- {constraints}
```

### 5. Append to Workflow Plan

Append to `{workflowPlanFile}`:

```markdown
## Calendar Sync

**Start Date:** {start_date}
**End Date:** {end_date}
**Capacity:** {hours}/week

**Milestones:**
- {milestone}: {date}
- {milestone}: {date}
```

### 6. Create Artifacts

**Ensure folders exist:**
- `{snapshotsFolder}`
- `{journalFolder}`
- `{plansFolder}`
- `{decisionsFolder}`

**Create files:**
1. **Snapshot** in `{snapshotsFolder}` (use `{snapshotTemplate}`):
   - Goal
   - Current status (PLANNED)
   - Next actions
   - Last decision (Calendar Sync approved)

2. **Journal** in `{journalFolder}` (use `{journalTemplate}`):
   - Append initial entry with scheduling decision

3. **Project Plan** in `{plansFolder}` (use `{planTemplate}`):
   - Idea summary
   - Consilium summary
   - Scoring summary
   - Integration summary
   - Calendar summary

4. **Decisions** in `{decisionsFolder}` (use `{decisionsTemplate}`):
   - Document scheduling trade-offs and rationale

**JIT Reference (for event templates):** See `{calendarEventTemplatesRef}` for milestone, deadline, and work block templates.

### 7. Present MENU OPTIONS

Display: **"Select: [D] Deep Plan [C] Complete"**

**Menu Handling:**
- **D** → Load and read `{nextStepFile}`, then execute
- **C** → Save content to `{workflowPlanFile}`, update frontmatter, load and read `{completeStepFile}`, then execute
- **Other** → Help user respond, redisplay menu

**Execution Rules:**
- ALWAYS halt and wait for user input after menu
- ONLY proceed to next step when user selects 'D'
- If 'C' selected, ensure all outputs saved before completion

## JIT REFERENCE SUMMARY

**Integration Methods:** `{calendarIntegrationMethodsRef}`
- Manual entry, iCal export, API integration, capacity blocking
- Best practices, compatibility matrix, common pitfalls

**Sync Protocols:** `{calendarSyncProtocolsRef}`
- Weekly manual sync, iCal import/export, API-based sync, capacity blocking
- Validation checklists, conflict resolution, troubleshooting

**Event Templates:** `{calendarEventTemplatesRef}`
- Milestone events, capacity blocks, deadlines, reviews, buffer time
- Color-coding, reminder strategy, naming conventions

## SUCCESS/FAILURE METRICS

### ✅ SUCCESS
- Timeline confirmed by user
- Project file created at `{outputProjectFile}`
- Plan updated with schedule in `{workflowPlanFile}`
- Snapshot, journal, plan, decisions artifacts created

### ❌ SYSTEM FAILURE
- Timeline proposed without user confirmation
- Project file not written to correct location
- Missing schedule in workflow plan
- Artifacts missing or incomplete

**Master Rule:** Scheduling must be confirmed by user and saved to project file before proceeding.




