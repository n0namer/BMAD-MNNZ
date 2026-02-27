---
name: 'step-06.5-portfolio-dashboard'
description: 'View and manage portfolio capacity, active projects, synergies'
stepType: Execute
estimatedMinutes: 15
trackApplicable: [Deep]
prerequisites: [step-06]
outputs: [portfolio-overview.md]
nextStepFile: './step-07-calendar-sync.md'
completeStepFile: './step-09-complete.md'
workflowPlanFile: '{bmb_creations_output_folder}/life-os/workflow-plan-life-os.md'
portfolioOutputFile: '{bmb_creations_output_folder}/life-os/portfolio-overview.md'
projectsFolder: '{bmb_creations_output_folder}/life-os/projects'
goalsFile: '../data/goals.yaml'
---

# Step 6.5: Portfolio Dashboard

## STEP GOAL

Display portfolio overview showing capacity utilization, active projects, health status, and synergies between projects while tying each active project back to the goals cascade (IDEAL 1.5) and calling out PDCA checkpoints (daily/weekly review links).

## MANDATORY EXECUTION RULES

### Universal Rules
- 🛑 NEVER generate content without user input
- 📖 Read the complete step file before taking any action
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ Communicate in your Agent style using `{communication_language}`

### Step-Specific Rules
- 🤝 Proactive guidance: highlight capacity risks, synergies, and bottlenecks
- 🧭 Surface WIP limits or portfolio risks early with brief recommendation
- ✅ Ask user confirmation before suggesting project changes
- 🎯 Focus ONLY on portfolio analysis and capacity management
- 🚫 FORBIDDEN to modify existing projects without user approval
- 💬 Ask 1-2 questions at a time, adapt to responses
- 🎯 Use subprocess for portfolio data aggregation (Pattern 3: Data Operations)

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
If portfolio decisions unclear, use Search Orchestrator to rank 2-3 portfolio strategies.

### Core Deliverables
- 🎯 Generate portfolio dashboard with capacity metrics
- 💾 Write portfolio overview to `{portfolioOutputFile}`
- 📖 Append portfolio summary to `{workflowPlanFile}`
- 🧾 Record portfolio health snapshot

## CONTEXT BOUNDARIES

- **Available context:** all project files, goals, workflow plan
- **Focus:** capacity, health status, synergies
- **Dependencies:** step-06 integration must be complete

## MANDATORY SEQUENCE

### 1. Load Portfolio State

**Load all active projects from `{projectsFolder}`:**

```bash
# Scan for projects with status: PLANNED, IN_PROGRESS, ACTIVE
# Count total active projects
# Extract key fields: projectId, title, status, startDate, endDate, capacityPerWeek
```

**Validation:**
- No projects folder? → Create folder and inform user (0/5 capacity)
- No active projects? → Inform user (0/5 capacity, green status)

**Decision Support:** If multiple competing projects, use Search Orchestrator to rank prioritization strategies.

### 2. Calculate Capacity Metrics

**Aggregate capacity data:**

1. **Active Projects Count:**
   - Count projects with status: PLANNED, IN_PROGRESS, ACTIVE
   - Display as: `X/5 projects active`

2. **Capacity Utilization:**
   - Sum `capacityPerWeek` from all active projects
   - Calculate percentage: `(total_capacity / available_capacity) * 100%`
   - Available capacity typically: 40 hours/week (or user-defined)

3. **Health Status Per Project:**
   - GREEN: On track, no blockers, capacity within limits
   - YELLOW: Minor delays, approaching capacity limits, dependencies at risk
   - RED: Blocked, overdue, capacity exceeded, critical risks

4. **Portfolio Health Score:**
   - GREEN: 0-3 active projects, <80% capacity
   - YELLOW: 4 active projects, 80-100% capacity
   - RED: 5+ active projects, >100% capacity

**JIT Reference (for capacity calculation):** If calculation unclear, refer to developer profile (step-0.6) for base capacity.

### 3. Identify Synergies

**Scan for synergies between projects:**

1. **Shared Goals:** Load `{goalsFile}` and match project goals
   - Projects aligned to same L1/L2 goal = synergy

2. **Shared Domains:** Compare project domains (Life/Goal/Project spheres)
   - Projects in same domain = potential resource sharing

3. **Shared Technologies:** Extract tech stack from project plans
   - Projects using same tools/frameworks = knowledge transfer opportunity

4. **Temporal Overlap:** Check start/end dates
   - Projects running simultaneously = coordination opportunity

**Output synergies as:**
```
Synergy between Project A and Project B:
- Shared goal: [Goal Name]
- Shared domain: [Domain]
- Recommendation: [Share learnings / Coordinate sprints / Merge resources]
```

**Decision Support:** If synergy strategy unclear, use Search Orchestrator to rank 2-3 coordination approaches.

### 4. Generate Dashboard View

**Create portfolio dashboard markdown:**

```markdown
---
generatedDate: {YYYY-MM-DD}
portfolioStatus: {GREEN|YELLOW|RED}
activeProjectsCount: {X}
capacityUtilization: {Y%}
---

# Portfolio Dashboard

## Capacity Overview

**Active Projects:** {X}/5
**Capacity Utilization:** {Y}% ({total_hours}/week of {available_hours}/week)
**Portfolio Health:** {GREEN|YELLOW|RED}

## Active Projects

### Project 1: {title}
- **Status:** {status}
- **Start:** {startDate} | **End:** {endDate}
- **Capacity:** {hours}/week
- **Health:** {GREEN|YELLOW|RED}
- **Next Milestone:** {milestone} on {date}
- **Blockers:** {blocker_list or "None"}

### Project 2: {title}
...

## Synergies

### Synergy Group 1
- **Projects:** Project A, Project B
- **Type:** Shared Goal ({goal_name})
- **Recommendation:** Coordinate sprint planning

### Synergy Group 2
...

## Capacity Warnings

{IF capacity > 80%:}
⚠️ **Capacity Warning:** You are at {Y}% capacity. Consider:
- Defer new projects until current projects complete
- Reduce capacity allocation on lower-priority projects
- Extend timelines to reduce weekly load

{IF capacity > 100%:}
🚨 **Capacity Overload:** You are at {Y}% capacity (overcommitted). Action required:
- Pause or kill lowest-priority project
- Renegotiate deadlines
- Reduce weekly commitments

## Portfolio Recommendations

{Based on analysis, suggest 2-3 actionable recommendations}
```

**Write to `{portfolioOutputFile}`**

### 5. Append to Workflow Plan

Append to `{workflowPlanFile}`:

```markdown
## Portfolio Dashboard

**Active Projects:** {X}/5
**Capacity Utilization:** {Y}%
**Portfolio Health:** {GREEN|YELLOW|RED}

**Key Synergies:**
- {Synergy 1}
- {Synergy 2}

**Recommendations:**
- {Recommendation 1}
- {Recommendation 2}
```

### 6. Prompt for Action

**Ask user:**

```
Portfolio Dashboard Generated!

Current Status:
- {X}/5 active projects
- {Y}% capacity utilization
- Portfolio health: {GREEN|YELLOW|RED}

Would you like to:
1. View detailed dashboard ({portfolioOutputFile})
2. Modify portfolio (pause/kill project, adjust capacity)
3. Continue to Calendar Sync
4. Export dashboard for review

Select option [1-4]:
```

**Wait for user response before proceeding.**

### 7. Present MENU OPTIONS

Display: **"Select: [C] Calendar Sync [M] Modify Portfolio [E] Export Dashboard [X] Complete"**

**Menu Handling:**
- **C** → Load and read `{nextStepFile}`, then execute
- **M** → Ask user which project to modify, then guide through changes
- **E** → Export dashboard to specified format (PDF, CSV, etc.)
- **X** → Save content to `{workflowPlanFile}`, update frontmatter, load and read `{completeStepFile}`, then execute
- **Other** → Help user respond, redisplay menu

**Execution Rules:**
- ALWAYS halt and wait for user input after menu
- ONLY proceed to next step when user selects option
- If modifications requested, update project files before continuing

## JIT REFERENCE SUMMARY

**Capacity Calculation:** Developer profile in step-0.6 (base capacity, speed multipliers)
**Project Health Metrics:** Refer to project status definitions in workflow.md
**Synergy Identification:** Use sphere registry (data/sphere-registry.md) for domain matching

## SUCCESS/FAILURE METRICS

### ✅ SUCCESS
- Portfolio dashboard generated with accurate metrics
- Capacity utilization calculated correctly
- Synergies identified between projects
- Health status assigned per project
- Portfolio overview written to `{portfolioOutputFile}`
- Plan updated with portfolio summary in `{workflowPlanFile}`

### ❌ SYSTEM FAILURE
- Dashboard generated without loading actual project data
- Capacity metrics inaccurate or missing
- No synergy analysis performed
- Portfolio overview not written to correct location
- Missing portfolio summary in workflow plan

**Master Rule:** Portfolio dashboard must be based on actual project data and confirmed by user before proceeding to Calendar Sync.
