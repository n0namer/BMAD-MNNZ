# Decision Prioritization Algorithm

## Subprocess Calculates Per Idea

### Activation Readiness (0-100%)
- **Plan completeness:** Has Deep Plan (step-08) been completed? (40%)
- **Dependencies met:** Are prerequisite ideas completed? (30%)
- **Resource availability:** Are required resources available? (20%)
- **Risk assessment:** Low risk = higher readiness (10%)

**Formula:**
```
activation_readiness = (plan_complete * 0.4) + (deps_met * 0.3) + (resources * 0.2) + (risk_factor * 0.1)
```

### Capacity Fit Analysis
- **FITS:** Current active projects < max capacity
- **TIGHT:** At max capacity but can accommodate
- **OVER:** Would exceed max capacity
- **BLOCKED:** Dependencies not met

### Dependencies Check
- **None:** No prerequisites
- **MET:** All prerequisite ideas completed
- **PENDING:** Some prerequisites in progress
- **BLOCKED:** Prerequisites not started

### Risk Level (Low/Medium/High)
- **LOW:** Clear requirements, proven approach, <8 weeks, low complexity
- **MEDIUM:** Some unknowns, moderate complexity, 8-16 weeks
- **HIGH:** Significant unknowns, high complexity, >16 weeks, new domain

### Strategic Alignment
- **HIGH:** Directly supports 2+ portfolio goals
- **MEDIUM:** Supports 1 portfolio goal
- **LOW:** Tangential or exploratory

## Recommendation Logic

### ACTIVATE_NOW
**Conditions (ALL must be true):**
- Activation readiness ≥ 90%
- Capacity fit = FITS
- Dependencies = None or MET
- Risk level = LOW or MEDIUM
- Strategic alignment = HIGH

### WAIT
**Conditions (ANY):**
- Dependencies = PENDING
- Capacity fit = TIGHT or OVER
- Risk level = HIGH and strategic alignment < HIGH

### RECONSIDER
**Conditions (ANY):**
- Activation readiness < 70%
- Strategic alignment = LOW
- Plan incomplete or outdated

### KILL (if applicable)
**Conditions (ANY):**
- Activation readiness < 50%
- Strategic alignment = LOW and risk = HIGH
- Duplicate of existing project

## Ranking Formula

**Primary sort:** Score (descending)

**Tie-breaker priorities:**
1. Activation readiness (higher first)
2. Risk level (lower first)
3. Estimated duration (shorter first)

## Portfolio Recommendations Generation

**Analyze:**
1. Available capacity slots vs ready ideas
2. Portfolio balance (goal coverage, risk distribution)
3. Dependency chains and sequencing
4. Resource constraints

**Generate recommendations:**
- "X capacity slots available - recommend activating top Y ideas"
- "Consider delaying idea-{id} until dependency completes"
- "Portfolio balance: activating {type} idea would maintain {ratio} split"
- "Warning: Activating {id} would exceed capacity by {n} slots"
