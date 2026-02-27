---
name: 'step-v-06-portfolio-view'
description: 'Display portfolio overview with capacity, health checks, and portfolio metrics'
nextStepFile: './step-v-07-decision-queue.md'
portfolioFile: '{bmb_creations_output_folder}/life-os/portfolio.md'
workflowPlanFile: '{bmb_creations_output_folder}/life-os/workflow-plan-life-os.md'
metricsFile: '{bmb_creations_output_folder}/life-os/metrics/metrics.md'
estimatedDuration: '3-5 minutes'
---

# Validation Step V-06: Portfolio Dashboard View

## STEP GOAL

Display a comprehensive portfolio overview showing current capacity utilization, active project health, portfolio balance, and risk indicators in a structured markdown report.

## WHEN TO USE

- **Daily/Weekly review:** Quick portfolio health check
- **Before planning session:** Assess capacity before adding new ideas
- **On-demand:** Any time user requests portfolio status
- **After milestone completion:** Review overall portfolio impact

## MANDATORY EXECUTION RULES (READ FIRST)

### Universal Rules
- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`

### Step-Specific Rules
- 🎯 Load portfolio and workflow plan data
- 🎯 Use subprocess for portfolio analysis (Pattern 2: LLM Operations)
- 💬 Return structured portfolio dashboard, not raw data files
- 📊 Display capacity metrics (X/5 slots used)
- 🚦 Show health indicators (on-track, at-risk, blocked)
- ⚖️ Calculate portfolio balance (business/personal/health)
- 🚨 Highlight risks and recommendations
- 🚫 FORBIDDEN to modify portfolio or projects here (view-only)

## EXECUTION PROTOCOLS

### Proactive Advice & Best Practices
- If user asks for advice about capacity management, use Search Orchestrator to retrieve best practices
- Summarize findings concisely and cite sources when possible

### Search Orchestrator Protocol (Optional)
- Follow data/search-decision-protocol.md
- Execute: CLI memory search → local MD (rg) → web/MCP
- Use for: portfolio management best practices, capacity planning patterns

## CONTEXT BOUNDARIES

- Available context: {portfolioFile}, {workflowPlanFile}, {metricsFile}
- Focus: portfolio overview and health assessment
- Read-only mode: no modifications to portfolio or projects

## MANDATORY SEQUENCE

### 1. Load Portfolio Data (Subprocess)

**Launch a subprocess that:**
1. Loads {portfolioFile} (if exists)
2. Loads {workflowPlanFile} (all ideas with status and scores)
3. Loads {metricsFile} (if exists) for trend data
4. Calculates portfolio metrics
5. Returns structured portfolio dashboard data

**Subprocess calculates:**
- **Capacity:** Active projects count / 5 (max capacity)
- **Status breakdown:** IN_PROGRESS, PLANNED, BLOCKED counts
- **Health indicators:** On-track, at-risk, blocked percentages
- **Portfolio balance:** Business/Personal/Health/Learning distribution
- **Score distribution:** Average score, top 3 projects
- **Timeline overview:** Near-term milestones (next 2 weeks)

**Subprocess returns:**
```json
{
  "capacity": {
    "current": 3,
    "max": 5,
    "available": 2,
    "utilization_percent": 60
  },
  "status_breakdown": {
    "in_progress": 3,
    "planned": 5,
    "blocked": 1,
    "completed": 12,
    "killed": 2
  },
  "health_indicators": {
    "on_track": 2,
    "at_risk": 1,
    "blocked": 0,
    "health_score": 85
  },
  "portfolio_balance": {
    "business": 40,
    "personal": 30,
    "health": 20,
    "learning": 10
  },
  "active_projects": [
    {
      "id": "idea-001",
      "name": "Project Alpha",
      "status": "IN_PROGRESS",
      "score": 8.5,
      "health": "on-track",
      "next_milestone": "MVP Launch",
      "milestone_date": "2026-02-15"
    }
  ],
  "risks": [
    {
      "severity": "medium",
      "project": "idea-002",
      "issue": "Timeline slippage detected",
      "recommendation": "Review scope or extend deadline"
    }
  ],
  "recommendations": [
    "2 capacity slots available - consider activating top planned idea",
    "1 project at-risk - schedule check-in this week"
  ]
}
```

**Context savings:** ~1,500 lines (portfolio + workflow plan + metrics) → ~300 lines (structured dashboard)

**Graceful fallback:** If subprocess unavailable, load files in main context and generate dashboard manually.

---

### 2. Generate Portfolio Dashboard Report

**Display formatted markdown report:**

```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 **PORTFOLIO DASHBOARD**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Generated: {timestamp}

## 📈 CAPACITY OVERVIEW

┌─────────────────────────────────────┐
│ Active Projects: {current} / {max}  │
│ Utilization: {percent}%             │
│ Available Slots: {available}        │
└─────────────────────────────────────┘

**Status Breakdown:**
- ✅ In Progress: {in_progress}
- 📋 Planned: {planned}
- 🚫 Blocked: {blocked}
- ✔️  Completed (all-time): {completed}

---

## 🚦 HEALTH INDICATORS

Overall Health Score: {health_score}/100

- 🟢 On Track: {on_track} projects
- 🟡 At Risk: {at_risk} projects
- 🔴 Blocked: {blocked} projects

---

## ⚖️  PORTFOLIO BALANCE

Distribution by Category:
- 💼 Business: {business}%
- 👤 Personal: {personal}%
- 🏃 Health: {health}%
- 📚 Learning: {learning}%

{IF imbalanced: "⚠️  Portfolio imbalance detected: {category} overweighted"}

---

## 🎯 ACTIVE PROJECTS

{FOR EACH active project:}
**{project_name}** (Score: {score}/10)
- Status: {status_emoji} {status}
- Health: {health_emoji} {health}
- Next Milestone: {milestone_name} ({milestone_date})
- {IF at_risk: "⚠️  {risk_description}"}

---

## 🚨 RISKS & ALERTS

{IF risks exist:}
{FOR EACH risk:}
- **{severity_emoji} {project_name}:** {issue}
  💡 Recommendation: {recommendation}

{ELSE:}
✅ No active risks detected

---

## 💡 RECOMMENDATIONS

{FOR EACH recommendation:}
- {recommendation}

---

## 📅 UPCOMING MILESTONES (Next 2 Weeks)

{FOR EACH upcoming milestone:}
- **{date}:** {project_name} - {milestone_name}

---
```

**Visual formatting notes:**
- Use emoji consistently for quick scanning
- Box borders for key metrics
- Color indicators: 🟢 🟡 🔴
- Keep report to 1-2 screen lengths max

---

### 3. Display Menu Options

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

What would you like to do?

[V]iew Decision Queue       - See ideas awaiting activation
[D]etails on project        - Deep dive into specific project
[M]etrics                   - View detailed metrics/trends
[R]efresh                   - Reload portfolio dashboard
[B]ack                      - Return to previous step
[C]ontinue                  - Proceed to decision queue

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### 4. Menu Handling Logic

**[V] View Decision Queue:**
- Load, read entire file, then execute {nextStepFile} (step-v-07-decision-queue.md)

**[D] Details on project:**
- Ask: "Which project? (Enter ID or name)"
- Load project execution tracker or deep plan
- Display detailed status
- Return to dashboard menu

**[M] Metrics:**
- Load {metricsFile}
- Display trend charts/metrics
- Return to dashboard menu

**[R] Refresh:**
- Re-execute Section 1 (reload data)
- Re-display dashboard

**[B] Back:**
- Return to calling step (typically validation flow)

**[C] Continue:**
- Load, read entire file, then execute {nextStepFile}

---

### 5. Save Dashboard Snapshot (Optional)

**If user requests:**
```bash
# Save dashboard to output for historical tracking
DASHBOARD_FILE="{bmb_creations_output_folder}/life-os/output/portfolio-dashboard-{date}.md"
# Write dashboard markdown to file
echo "✅ Dashboard snapshot saved: {DASHBOARD_FILE}"
```

**Store in memory:**
```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "portfolio:dashboard:{date}" \
  --content "{dashboard_json}"
```

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS
- Portfolio data loaded and analyzed in subprocess
- Dashboard report generated with all 5 sections
- Capacity, health, balance, risks clearly displayed
- Recommendations provided based on current state
- User can quickly assess portfolio health (<3 min)
- View-only mode enforced (no accidental modifications)

### ❌ SYSTEM FAILURE
- Loading full portfolio/workflow files in main context (context waste)
- Missing key metrics (capacity, health, balance)
- No risk detection or recommendations
- Allowing modifications from view-only step
- Dashboard too verbose (>3 screens)
- Not using subprocess for analysis

---

## RELATED FILES

📖 Portfolio data: `{portfolioFile}`
📖 Workflow plan: `{workflowPlanFile}`
📖 Metrics: `{metricsFile}`
📖 Next step: `{nextStepFile}` (Decision Queue)

---

**Master Rule:** This is a READ-ONLY view step. Display comprehensive portfolio overview efficiently using subprocess analysis. Help user make informed decisions about capacity and priorities.
