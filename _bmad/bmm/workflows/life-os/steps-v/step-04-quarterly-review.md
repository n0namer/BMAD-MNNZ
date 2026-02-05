---
name: 'step-04-quarterly-review'
description: 'Run comprehensive quarterly OKR review and goal adjustment (PDCA Check-Act phase)'
nextStepFile: './step-00-return-to-plan.md'
goalsFile: '{bmb_creations_output_folder}/life-os/goals.yaml'
portfolioFile: '{bmb_creations_output_folder}/life-os/portfolio.md'
metricsFile: '{bmb_creations_output_folder}/life-os/metrics/metrics.md'
quarterlyReviewsFolder: '{bmb_creations_output_folder}/life-os/reviews/quarterly'
---

# Validation Step 4: Quarterly Review (Квартальный Обзор)

## STEP GOAL

Провести комплексный обзор квартала по методологии PDCA (Check-Act фазы): проанализировать достижение OKR, оценить прогресс по целям, скорректировать стратегию на следующий квартал.

## MANDATORY EXECUTION RULES

### Universal Rules
- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read complete step before action
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Step-Specific Rules
- 🤝 Proactive guidance: highlight risks, opportunities, strategic shifts
- 🧭 Surface portfolio-level insights and alignment gaps
- ✅ Ask for user confirmation before making goal adjustments
- 🎯 Focus on OKR completion, goal progress, and strategic realignment
- 🎯 Analyze quarterly review in subprocess (Pattern 2)
- 💬 Return structured quarterly findings and OKR results, not 3-month raw data
- 🚫 FORBIDDEN to micromanage tactics (that's for daily/weekly reviews)

## EXECUTION PROTOCOLS

### Search Orchestrator Protocol
- Follow data/mcp_search_system_prompt_xml.md
- Execute: CLI memory search → local MD (rg) → web/MCP
- Convene consilium for strategic decisions
- Record evidence snapshot and confidence level

### Semantic Decision Support
If quarterly priorities unclear, use Search Orchestrator to rank 2-3 strategic options.

## PDCA INTEGRATION

This step covers **CHECK** and **ACT** phases of PDCA cycle:

### CHECK Phase
- Review quarterly OKRs and key results
- Analyze actual vs. planned progress
- Identify what worked and what didn't

### ACT Phase
- Adjust goals based on learnings
- Reallocate resources for next quarter
- Update strategy and tactics

## MANDATORY SEQUENCE

### 1. Context Loading (Subprocess Pattern)

**Launch a subprocess that:**
1. Loads data/quarterly-review-okr-protocol.md
2. Loads data/quarterly-metrics-calc.md
3. Loads data/quarterly-review-swot.md
4. Loads 3 months of data from {metricsFile}
5. Loads {goalsFile} and {portfolioFile}
6. Performs OKR analysis, metrics calculation, SWOT analysis
7. Returns structured quarterly findings

Display: Quarter info, goals file, portfolio, metrics file.

**Subprocess analyzes:**
- Active goals and Key Results with Q{N} deadlines
- Milestones and portfolio projects
- 3-month trends and patterns
- OKR completion rates
- Goal alignment percentages

### 2-6. Quarterly Analysis (Subprocess Execution)

**Subprocess returns:**
```json
{
  "quarter": "Q{N} {YEAR}",
  "okr_results": [
    {
      "goal_id": "...",
      "goal_name": "...",
      "key_results": [
        {"kr": "...", "target": 100, "actual": 85, "status": "achieved/partial/missed"}
      ],
      "completion_pct": 85
    }
  ],
  "milestones": [
    {"milestone": "...", "completed": true, "on_time": false, "delay_reason": "..."}
  ],
  "portfolio_alignment": {
    "active_projects": 5,
    "completed": 2,
    "paused_killed": 1,
    "alignment_score": 78,
    "distractions": [...]
  },
  "quarterly_metrics": {
    "velocity": "...",
    "wip_avg": 3.2,
    "blocker_resolution_time": "5 days",
    "goal_progress": "..."
  },
  "swot": {
    "strengths": [...],
    "weaknesses": [...],
    "opportunities": [...],
    "threats": [...]
  }
}
```

**Context savings:** ~1,600 lines (3-month data + protocols) → ~120 lines (structured findings)

**Graceful fallback:** If subprocess unavailable, load protocols and data in main context.

📖 **Subprocess executes:**
- OKR Review (data/quarterly-review-okr-protocol.md)
- Milestones Review
- Portfolio Alignment Check
- Metrics Analysis (data/quarterly-metrics-calc.md)
- SWOT Analysis (data/quarterly-review-swot.md)

### 7. Goal Adjustment Protocol (ACT Phase)

For each goal, recommend one of: Keep as is, Adjust targets, Extend deadline, Pause, or Abandon.

Ask: "Что делаем с этой целью в Q{N+1}?"

Apply changes to goals.yaml.

### 8. Planning for Next Quarter (Q{N+1})

Ask: Theme, 3 main priorities, required resources.

Update goals.yaml with Q{N+1} configuration (theme, goals, focus_areas, milestones, status).

### 9. Save Quarterly Review Report

Create file: `{quarterlyReviewsFolder}/Q{N}-2026-review.md`

Include sections: Executive Summary (completion rates, top 3 wins, top 2 challenges), OKR Results, Portfolio Alignment, Metrics table, SWOT Analysis, Decisions & Adjustments, Q{N+1} Plan.

Use standard quarterly review markdown format.

### 10. Update Memory

Save to Claude Flow memory:

```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "life-os:reviews:quarterly:Q{N}-2026" \
  --value "{review_summary}"
```

### 11. Append to Metrics File

Append quarterly summary to {metricsFile}: Goal completion, KR achievement, rating, adjustments count, link to report.

### 12. Pattern Mining from Archive

Load pattern mining protocol:
📖 Reference: data/quarterly-pattern-mining.md

Execute pattern discovery process per loaded protocol:
- Success pattern detection
- Failure pattern detection
- Domain insights update
- Pattern application to future ideas

### 13. Calibration Review

Load calibration protocol:
📖 Reference: data/quarterly-calibration-protocol.md

Execute calibration review per loaded protocol:
- Estimate accuracy analysis
- Speed multiplier adjustments
- Common patterns identified
- Calibration summary

### 14. Completion Message

Show: OKR/Goals completion percentages, report saved, adjustments applied, memory updated.

PDCA status: CHECK done, ACT done, proceed to PLAN phase.

Ask: Continue with planning or return to work?

---

## VALIDATION & SUCCESS CRITERIA

### ✅ SUCCESS

- All quarterly OKRs reviewed
- Goal progress updated in goals.yaml
- Quarterly report saved
- Metrics calculated and recorded
- Next quarter planned (theme, focus, milestones)
- Calibration review completed (if ideas completed)
- Memory updated
- User confident in adjustments

### ❌ SYSTEM FAILURE

- Generating fake progress data
- Not reviewing all active goals
- Skipping goal adjustment decisions
- Not saving quarterly report
- Missing calibration review (if ideas completed)
- Missing memory update

---

## INTEGRATION WITH PDCA CYCLE

### Connection to Other Steps

**Backward:**
- Daily Review (v-01): Aggregated daily data
- Weekly Review (v-02): Aggregated weekly insights
- Monthly Review (v-03): Aggregated monthly patterns

**Forward:**
- Step-00 (Goals Discovery): May trigger goal redefinition
- Step e-01 (Update Project): Apply adjustments to portfolio
- Step e-02 (Rescoring): Re-evaluate project priorities

**PDCA Loop:**
```
PLAN (Step-00) → DO (Steps 1-8) → CHECK (This Step) → ACT (Adjustments) → PLAN (Q{N+1})
```

---

## BEST PRACTICES

### Timing

- Schedule quarterly review in last week of quarter
- Allow 2-3 hours for comprehensive review
- Do NOT rush — this is strategic planning

### Frequency

- Mandatory every quarter (4 times/year)
- Optional mid-quarter check-in (6 weeks)

### Mindset

- Be honest about progress (no sandbagging)
- Focus on learnings, not blame
- Celebrate wins, analyze failures objectively
- Think strategically (not tactically)

---

**End of Step 04: Quarterly Review**
