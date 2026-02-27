# Decision Queue Management

## Queue Data Structure

### Queue Summary
```json
{
  "total_planned_ideas": <count>,
  "ready_to_activate": <count>,
  "blocked_by_dependencies": <count>,
  "needs_replanning": <count>
}
```

### Capacity Context
```json
{
  "current_active": <count>,
  "max_capacity": <count>,
  "available_slots": <count>
}
```

### Decision Queue Entry
```json
{
  "id": "idea-XXX",
  "name": "Idea Name",
  "score": 8.7,
  "rank": 1,
  "activation_readiness": 95,
  "capacity_fit": "FITS|TIGHT|OVER|BLOCKED",
  "dependencies": ["idea-YYY"],
  "risk_level": "LOW|MEDIUM|HIGH",
  "estimated_duration_weeks": 6,
  "strategic_alignment": "HIGH|MEDIUM|LOW",
  "recommendation": "ACTIVATE_NOW|WAIT|RECONSIDER|KILL",
  "reasoning": "Explanation for recommendation"
}
```

## Filter Criteria

### Status Filter
- **Include:** PLANNED, PLANNED_EVALUATED
- **Exclude:** IDEA, IN_PROGRESS, COMPLETED, KILLED, PLANNED_PAUSED

### Completion Filter
- **Require:** Deep Plan (step-08) completed
- **Check:** `deep_plan_file` exists and non-empty
- **Exclude:** Ideas without scoring or planning data

## Display Formatting

### Readiness Indicators
- 🟢 **90-100%:** Ready to go
- 🟡 **70-89%:** Mostly ready, minor gaps
- 🔴 **<70%:** Not ready, significant gaps

### Risk Emojis
- 🟢 **LOW:** Low risk
- 🟡 **MEDIUM:** Moderate risk
- 🔴 **HIGH:** High risk

### Capacity Indicators
- ✅ **FITS:** Capacity available
- ⚠️ **TIGHT:** At capacity limit
- 🚫 **OVER:** Would exceed capacity
- ⏸️ **BLOCKED:** Dependencies not met

## Queue Actions

### Activate Idea
1. Validate capacity (available_slots > 0)
2. Check dependencies (all must be complete)
3. Confirm with user
4. Execute step-x-01-kickoff.md
5. Update status to IN_PROGRESS
6. Create execution tracker
7. Refresh queue

### Kill Idea
1. Confirm with user (irreversible)
2. Request reason
3. Update status to KILLED
4. Archive to `_archive/killed/{idea_id}.md`
5. Store decision in memory
6. Refresh queue

### Postpone Idea
1. Request reason
2. Update status to PLANNED_PAUSED
3. Store reason in workflow plan
4. Refresh queue

### View Details
1. Load Deep Plan (step-08 output)
2. Display L1-L6 structure
3. Show full scoring breakdown
4. Return to queue menu

## Graceful Fallback

**If subprocess unavailable:**
1. Load workflow plan and portfolio in main context
2. Filter manually for PLANNED ideas
3. Calculate decision factors inline
4. Generate simplified queue
5. Warn user about context limitations
