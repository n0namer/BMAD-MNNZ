# Auto-Linking Engine

**Purpose:** Automatically populate template fields from workflow plan and other templates to reduce redundant data entry and maintain consistency across project artifacts.

**Version:** 1.0
**Last Updated:** 2026-02-04
**Status:** Active

---

## Overview

The Auto-Linking Engine detects relationships between templates and workflow plans, then automatically populates fields based on predefined linking rules. This reduces manual effort by 40-60% and ensures consistency across all project documentation.

**Key Benefits:**
- Eliminate redundant data entry across templates
- Maintain consistency between related frameworks
- Reduce errors from manual transcription
- Speed up template initialization by 40-60%
- Preserve data lineage and traceability

---

## Linking Rules Database

### Business → Finance Links

```yaml
# Lean Canvas → NPV Analysis
lean_canvas.revenue_streams → npv.cash_inflows
  transform: currencyToNPV
  confidence: 0.95

lean_canvas.cost_structure → npv.cash_outflows
  transform: currencyToNPV
  confidence: 0.95

lean_canvas.customer_segments → dcf.market_size
  transform: segmentsToMarketSize
  confidence: 0.85

# Business Model Canvas → NPV Analysis
bmc.revenue_streams → npv.cash_inflows
  transform: currencyToNPV
  confidence: 0.90

bmc.cost_structure → npv.cash_outflows
  transform: currencyToNPV
  confidence: 0.90

bmc.key_resources → npv.capital_expenditures
  transform: resourcesToCapEx
  confidence: 0.80

# OKRs → DCF Analysis
okrs.objectives → dcf.business_objectives
  transform: directCopy
  confidence: 0.95

okrs.key_results → dcf.growth_rate_assumptions
  transform: metricsToGrowthRate
  confidence: 0.85

okrs.quarterly_targets → dcf.revenue_projections
  transform: targetsToProjections
  confidence: 0.80

# Value Proposition Canvas → Real Options
vpc.customer_jobs → real_options.value_drivers
  transform: jobsToDrivers
  confidence: 0.85

vpc.gains → real_options.upside_scenarios
  transform: gainsToScenarios
  confidence: 0.80

vpc.pains → real_options.risks
  transform: painsToRisks
  confidence: 0.80
```

### Business → Personal Links

```yaml
# OKRs → Deep Plan
okrs.objectives → deep_plan.l1_mission
  transform: objectiveToMission
  confidence: 0.95

okrs.key_results → deep_plan.l2_phases
  transform: keyResultsToPhases
  confidence: 0.90

okrs.initiatives → deep_plan.l3_milestones
  transform: initiativesToMilestones
  confidence: 0.85

# Business Model Canvas → GTD
bmc.key_activities → gtd.projects
  transform: activitiesToProjects
  confidence: 0.85

bmc.key_partners → gtd.waiting_for
  transform: partnersToWaitingFor
  confidence: 0.75

# Lean Canvas → TRIZ
lean_canvas.problem → triz.contradiction_statement
  transform: problemToContradiction
  confidence: 0.90

lean_canvas.solution → triz.ideal_final_result
  transform: solutionToIFR
  confidence: 0.85

lean_canvas.unfair_advantage → triz.resources
  transform: advantageToResources
  confidence: 0.80

# Value Proposition Canvas → Pomodoro
vpc.customer_tasks → pomodoro.task_list
  transform: tasksToPomodoro
  confidence: 0.85

vpc.gains → pomodoro.outcomes
  transform: gainsToOutcomes
  confidence: 0.75
```

### Health → Personal Links

```yaml
# SMART Goals → Atomic Habits
smart_goals.specific_target → atomic_habits.identity_statement
  transform: goalToIdentity
  confidence: 0.90

smart_goals.measurable_metrics → atomic_habits.tracking_method
  transform: metricsToTracking
  confidence: 0.85

smart_goals.action_steps → atomic_habits.habit_stack
  transform: stepsToStack
  confidence: 0.80

# Progressive Overload → Pomodoro
progressive_overload.weekly_plan → pomodoro.weekly_schedule
  transform: workoutsToPomodoro
  confidence: 0.90

progressive_overload.session_duration → pomodoro.time_blocks
  transform: durationToBlocks
  confidence: 0.85

# Habit Loop → Deep Plan
habit_loop.cue → deep_plan.l5_daily_tasks
  transform: cueToDailyTasks
  confidence: 0.85

habit_loop.routine → deep_plan.l4_weekly_tasks
  transform: routineToWeeklyTasks
  confidence: 0.80

habit_loop.reward → deep_plan.checkpoints
  transform: rewardToCheckpoints
  confidence: 0.75

# Recovery Protocols → Atomic Habits
recovery_protocols.sleep_target → atomic_habits.environment_design
  transform: sleepToEnvironment
  confidence: 0.85

recovery_protocols.nutrition_plan → atomic_habits.cue_design
  transform: nutritionToCues
  confidence: 0.80

recovery_protocols.rest_days → atomic_habits.habit_tracking
  transform: restDaysToTracking
  confidence: 0.75
```

### Finance → Personal Links

```yaml
# NPV → Deep Plan
npv.project_timeline → deep_plan.l2_phases
  transform: timelineToPhases
  confidence: 0.90

npv.milestones → deep_plan.l3_milestones
  transform: directCopy
  confidence: 0.95

npv.decision_points → deep_plan.checkpoints
  transform: decisionsToCheckpoints
  confidence: 0.85

# Monte Carlo → Deep Plan
monte_carlo.scenarios → deep_plan.scenario_branches
  transform: monteCarloToScenarios
  confidence: 0.90

monte_carlo.probability_distributions → deep_plan.risk_assessments
  transform: probabilityToRisk
  confidence: 0.85

# Real Options → Deep Plan
real_options.decision_points → deep_plan.l3_milestones
  transform: optionsToMilestones
  confidence: 0.85

real_options.timing_flexibility → deep_plan.l2_phases
  transform: timingToPhases
  confidence: 0.80

real_options.scenarios → deep_plan.scenario_branches
  transform: optionsToScenarios
  confidence: 0.85

# DCF → Atomic Habits
dcf.growth_projections → atomic_habits.progress_tracking
  transform: projectionsToProgress
  confidence: 0.75

dcf.terminal_value → atomic_habits.long_term_identity
  transform: terminalToIdentity
  confidence: 0.70
```

### Workflow Plan → All Templates

```yaml
# Universal Links (apply to all templates)
workflow_plan.project_name → all_templates.project_name
  transform: directCopy
  confidence: 1.0

workflow_plan.start_date → all_templates.start_date
  transform: directCopy
  confidence: 1.0

workflow_plan.owner → all_templates.created_by
  transform: directCopy
  confidence: 1.0

# Design Thinking Phase → Templates
workflow_plan.design_thinking.who_benefits → all_templates.stakeholders
  transform: beneficiariesToStakeholders
  confidence: 0.95

workflow_plan.design_thinking.problem_statement → all_templates.context
  transform: problemToContext
  confidence: 0.90

workflow_plan.design_thinking.constraints → all_templates.constraints
  transform: directCopy
  confidence: 0.95

# Consilium Phase → Templates
workflow_plan.consilium.specialists → template.recommended_roles
  transform: specialistsToRoles
  confidence: 0.90

workflow_plan.consilium.insights → template.key_considerations
  transform: insightsToConsiderations
  confidence: 0.85

workflow_plan.consilium.frameworks_recommended → template.related_frameworks
  transform: directCopy
  confidence: 0.95

# Scoring Phase → Templates
workflow_plan.scoring.impact → template.priority_score
  transform: impactToPriority
  confidence: 0.90

workflow_plan.scoring.strategic_alignment → template.alignment_check
  transform: directCopy
  confidence: 0.95

workflow_plan.scoring.urgency → template.deadline_priority
  transform: urgencyToDeadline
  confidence: 0.85

# TRIZ Analysis → Templates
workflow_plan.triz.contradictions → triz_template.contradiction_statement
  transform: directCopy
  confidence: 0.95

workflow_plan.triz.ideal_final_result → all_templates.success_criteria
  transform: ifrToSuccess
  confidence: 0.90

workflow_plan.triz.inventive_principles → template.approaches
  transform: principlesToApproaches
  confidence: 0.85
```

---

## Auto-Population Algorithm

### Step 1: Detect Source Data

```javascript
/**
 * Scans for available source data to populate template fields
 * @param {Object} template - Target template to populate
 * @returns {Array} Array of available source data objects
 */
function detectSources(template) {
  const sources = []

  // Check workflow plan
  if (workflowPlan.exists) {
    sources.push({
      type: 'workflow_plan',
      priority: 1, // Highest priority
      fields: extractRelevantFields(workflowPlan, template.domain),
      timestamp: workflowPlan.lastModified
    })
  }

  // Check other templates in current project
  const existingTemplates = findTemplates(currentProject)
  existingTemplates.forEach(t => {
    const links = findLinks(t.framework, template.framework)
    if (links.length > 0) {
      sources.push({
        type: 'template',
        priority: 2, // Lower than workflow plan
        template: t.framework,
        domain: t.domain,
        fields: links,
        timestamp: t.lastModified
      })
    }
  })

  // Check global memory for similar projects
  const memorySources = searchMemory(
    `domain:${template.domain} framework:${template.framework}`
  )
  if (memorySources.length > 0) {
    sources.push({
      type: 'memory',
      priority: 3, // Lowest priority
      patterns: memorySources,
      confidence: 0.7 // Default lower confidence for memory
    })
  }

  // Sort by priority and recency
  return sources.sort((a, b) => {
    if (a.priority !== b.priority) return a.priority - b.priority
    return b.timestamp - a.timestamp
  })
}
```

### Step 2: Apply Linking Rules

```javascript
/**
 * Applies linking rules to populate template fields from sources
 * @param {Object} template - Target template
 * @param {Array} sources - Available source data
 * @returns {Object} Populated fields with metadata
 */
function autoPopulate(template, sources) {
  const populated = {}
  const conflicts = {}

  sources.forEach(source => {
    // Get linking rules for this source type and template
    const rules = LINKING_RULES[source.type]?.[template.framework] || []

    rules.forEach(rule => {
      // Check if source has the required field
      if (source.hasField(rule.sourceField)) {
        const rawValue = source.getField(rule.sourceField)

        // Apply transformation function if specified
        const transformedValue = rule.transform
          ? TRANSFORMS[rule.transform](rawValue, rule.options)
          : rawValue

        // Calculate final confidence score
        const confidence = calculateConfidence(
          rule.confidence || 0.8,
          source.priority,
          source.timestamp
        )

        // Check for conflicts (multiple sources for same field)
        if (populated[rule.targetField]) {
          if (!conflicts[rule.targetField]) {
            conflicts[rule.targetField] = [populated[rule.targetField]]
          }
          conflicts[rule.targetField].push({
            value: transformedValue,
            source: `${source.type}:${rule.sourceField}`,
            confidence: confidence,
            timestamp: source.timestamp
          })
        } else {
          populated[rule.targetField] = {
            value: transformedValue,
            source: `${source.type}:${rule.sourceField}`,
            sourceType: source.type,
            confidence: confidence,
            timestamp: source.timestamp,
            rule: rule.name || `${rule.sourceField}→${rule.targetField}`
          }
        }
      }
    })
  })

  // Resolve conflicts
  if (Object.keys(conflicts).length > 0) {
    Object.entries(conflicts).forEach(([field, options]) => {
      populated[field] = resolveConflict(field, options)
      populated[field].hasConflict = true
      populated[field].alternatives = options
    })
  }

  return populated
}

/**
 * Calculates confidence score based on multiple factors
 */
function calculateConfidence(baseConfidence, priority, timestamp) {
  let confidence = baseConfidence

  // Boost confidence for higher priority sources
  if (priority === 1) confidence *= 1.1
  if (priority === 2) confidence *= 1.0
  if (priority === 3) confidence *= 0.9

  // Reduce confidence for older data (decay over 30 days)
  const ageInDays = (Date.now() - timestamp) / (1000 * 60 * 60 * 24)
  if (ageInDays > 30) {
    confidence *= Math.max(0.7, 1 - (ageInDays - 30) / 365)
  }

  // Clamp to [0, 1]
  return Math.min(1.0, Math.max(0.0, confidence))
}
```

### Step 3: User Confirmation

```javascript
/**
 * Presents auto-links to user for confirmation
 * @param {Object} populated - Auto-populated fields
 * @param {Object} template - Target template
 * @returns {Object} Confirmed auto-links
 */
function confirmAutoLinks(populated, template) {
  console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
  console.log("🔗 Auto-Linking Found:")
  console.log(`   Template: ${template.framework}`)
  console.log(`   ${Object.keys(populated).length} fields can be auto-populated\n`)

  // Group by confidence level
  const highConfidence = []
  const mediumConfidence = []
  const lowConfidence = []

  Object.entries(populated).forEach(([field, data]) => {
    if (data.confidence >= 0.9) highConfidence.push([field, data])
    else if (data.confidence >= 0.7) mediumConfidence.push([field, data])
    else lowConfidence.push([field, data])
  })

  // Display high confidence links
  if (highConfidence.length > 0) {
    console.log("✅ High Confidence (≥90%):")
    highConfidence.forEach(([field, data]) => {
      console.log(`   • ${field}`)
      console.log(`     Value: "${truncate(data.value, 60)}"`)
      console.log(`     Source: ${data.source}`)
      console.log(`     Confidence: ${(data.confidence * 100).toFixed(0)}%`)
      if (data.hasConflict) console.log(`     ⚠️  Multiple sources available`)
      console.log()
    })
  }

  // Display medium confidence links
  if (mediumConfidence.length > 0) {
    console.log("⚠️  Medium Confidence (70-89%):")
    mediumConfidence.forEach(([field, data]) => {
      console.log(`   • ${field}`)
      console.log(`     Value: "${truncate(data.value, 60)}"`)
      console.log(`     Source: ${data.source}`)
      console.log(`     Confidence: ${(data.confidence * 100).toFixed(0)}%`)
      console.log()
    })
  }

  // Display low confidence links
  if (lowConfidence.length > 0) {
    console.log("❓ Low Confidence (<70%):")
    lowConfidence.forEach(([field, data]) => {
      console.log(`   • ${field}`)
      console.log(`     Value: "${truncate(data.value, 60)}"`)
      console.log(`     Source: ${data.source}`)
      console.log(`     Confidence: ${(data.confidence * 100).toFixed(0)}%`)
      console.log()
    })
  }

  console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")

  // Ask for confirmation
  const response = askUser(
    "Options:\n" +
    "  [A] Accept all auto-links\n" +
    "  [H] Accept high confidence only (≥90%)\n" +
    "  [S] Select individually\n" +
    "  [N] Skip auto-linking\n" +
    "Choice: "
  )

  switch (response.toUpperCase()) {
    case 'A':
      return populated

    case 'H':
      const confirmed = {}
      highConfidence.forEach(([field, data]) => {
        confirmed[field] = data
      })
      return confirmed

    case 'S':
      return selectiveConfirm(populated)

    case 'N':
    default:
      return {}
  }
}

/**
 * Allows user to select individual auto-links
 */
function selectiveConfirm(populated) {
  const confirmed = {}

  Object.entries(populated).forEach(([field, data]) => {
    console.log(`\n📌 Field: ${field}`)
    console.log(`   Value: "${truncate(data.value, 80)}"`)
    console.log(`   Source: ${data.source}`)
    console.log(`   Confidence: ${(data.confidence * 100).toFixed(0)}%`)

    if (data.hasConflict) {
      console.log(`\n   ⚠️  Multiple sources available:`)
      data.alternatives.forEach((alt, idx) => {
        console.log(`   [${idx + 1}] "${truncate(alt.value, 60)}"`)
        console.log(`       Source: ${alt.source} (${(alt.confidence * 100).toFixed(0)}%)`)
      })

      const choice = askUser("   Select option (1-" + data.alternatives.length + ") or [N] to skip: ")

      if (choice.toUpperCase() !== 'N' && !isNaN(choice)) {
        const selectedIdx = parseInt(choice) - 1
        if (selectedIdx >= 0 && selectedIdx < data.alternatives.length) {
          confirmed[field] = data.alternatives[selectedIdx]
        }
      }
    } else {
      const accept = askUser("   Accept? [Y/n]: ")
      if (accept.toUpperCase() !== 'N') {
        confirmed[field] = data
      }
    }
  })

  return confirmed
}

/**
 * Truncates string for display
 */
function truncate(str, maxLength) {
  if (typeof str !== 'string') str = JSON.stringify(str)
  if (str.length <= maxLength) return str
  return str.substring(0, maxLength - 3) + '...'
}
```

---

## Transformation Functions

### Currency Conversion

```javascript
TRANSFORMS.currencyToNPV = (leanCanvasRevenue, options = {}) => {
  /**
   * Transforms Lean Canvas revenue format to NPV cash flow format
   * Input: "Subscription: $50/mo × 1000 users"
   * Output: { monthly: 50000, annual: 600000, growth_rate: 0.1 }
   */

  const result = {
    monthly: 0,
    annual: 0,
    growth_rate: options.defaultGrowthRate || 0.1,
    years: options.projectionYears || 5
  }

  // Parse subscription format: $X/mo × Y users
  const subscriptionMatch = leanCanvasRevenue.match(/\$(\d+(?:,\d{3})*(?:\.\d{2})?)\/mo\s*[×x]\s*(\d+(?:,\d{3})*)/)
  if (subscriptionMatch) {
    const pricePerMonth = parseFloat(subscriptionMatch[1].replace(/,/g, ''))
    const users = parseInt(subscriptionMatch[2].replace(/,/g, ''))
    result.monthly = pricePerMonth * users
    result.annual = result.monthly * 12
  }

  // Parse one-time revenue: $X/unit × Y units
  const oneTimeMatch = leanCanvasRevenue.match(/\$(\d+(?:,\d{3})*(?:\.\d{2})?)\/unit\s*[×x]\s*(\d+(?:,\d{3})*)/)
  if (oneTimeMatch) {
    const pricePerUnit = parseFloat(oneTimeMatch[1].replace(/,/g, ''))
    const units = parseInt(oneTimeMatch[2].replace(/,/g, ''))
    result.annual = pricePerUnit * units
    result.monthly = result.annual / 12
  }

  // Parse annual format: $X/year
  const annualMatch = leanCanvasRevenue.match(/\$(\d+(?:,\d{3})*(?:\.\d{2})?)\/year/)
  if (annualMatch) {
    result.annual = parseFloat(annualMatch[1].replace(/,/g, ''))
    result.monthly = result.annual / 12
  }

  // Project over multiple years with growth
  result.projections = []
  for (let year = 1; year <= result.years; year++) {
    result.projections.push({
      year: year,
      revenue: result.annual * Math.pow(1 + result.growth_rate, year - 1)
    })
  }

  return result
}
```

### Time Conversion

```javascript
TRANSFORMS.weeklyToPomodoro = (progressiveOverloadPlan, options = {}) => {
  /**
   * Transforms Progressive Overload weekly plan to Pomodoro schedule
   * Input: "3x per week, 60 min each"
   * Output: { weekly_pomodoros: 9, schedule: [...], pomodoros_per_day: 3 }
   */

  // Parse frequency: "Nx per week"
  const freqMatch = progressiveOverloadPlan.match(/(\d+)x?\s*per\s*week/i)
  const sessionsPerWeek = freqMatch ? parseInt(freqMatch[1]) : 3

  // Parse duration: "X min each"
  const durationMatch = progressiveOverloadPlan.match(/(\d+)\s*min(?:utes?)?\s*each/i)
  const minutesPerSession = durationMatch ? parseInt(durationMatch[1]) : 60

  // Calculate pomodoros (25 min per pomodoro, 5 min break)
  const pomodorosPerSession = Math.ceil(minutesPerSession / 25)
  const totalWeeklyPomodoros = sessionsPerWeek * pomodorosPerSession

  // Generate default schedule (Mon/Wed/Fri or similar)
  const defaultDays = sessionsPerWeek === 3
    ? ['Monday', 'Wednesday', 'Friday']
    : sessionsPerWeek === 4
    ? ['Monday', 'Tuesday', 'Thursday', 'Friday']
    : Array(sessionsPerWeek).fill(null).map((_, i) =>
        ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][i]
      )

  const schedule = defaultDays.map((day, idx) => ({
    day: day,
    time: options.preferredTime || '07:00',
    duration_minutes: minutesPerSession,
    pomodoros: pomodorosPerSession,
    breaks: pomodorosPerSession - 1
  }))

  return {
    weekly_pomodoros: totalWeeklyPomodoros,
    sessions_per_week: sessionsPerWeek,
    pomodoros_per_session: pomodorosPerSession,
    schedule: schedule,
    total_weekly_minutes: sessionsPerWeek * minutesPerSession,
    estimated_weekly_hours: (sessionsPerWeek * minutesPerSession) / 60
  }
}
```

### Goal Decomposition

```javascript
TRANSFORMS.okrToL2 = (okrKeyResults, options = {}) => {
  /**
   * Transforms OKR Key Results into Deep Plan L2 Phases
   * Input: Array of key results with targets and deadlines
   * Output: Array of L2 phases with milestones
   */

  if (!Array.isArray(okrKeyResults)) {
    okrKeyResults = [okrKeyResults]
  }

  return okrKeyResults.map((kr, index) => {
    // Extract target value if present
    const targetMatch = kr.description?.match(/(\d+(?:,\d{3})*(?:\.\d+)?)\s*(%|users|customers|revenue)?/)
    const targetValue = targetMatch ? targetMatch[1] : kr.target_value || 'TBD'
    const targetUnit = targetMatch ? targetMatch[2] || '' : ''

    // Parse deadline
    const deadline = kr.deadline || calculateDeadline(index, okrKeyResults.length)

    // Generate phase name
    const phaseName = kr.name || kr.description || `Phase ${index + 1}`

    return {
      phase: `L2.${index + 1}`,
      name: phaseName,
      description: kr.description || phaseName,
      target: {
        value: targetValue,
        unit: targetUnit,
        metric: kr.metric || 'Progress'
      },
      deadline: deadline,
      milestone: `Achieve ${kr.description || phaseName}`,
      success_criteria: kr.success_criteria || [
        `${targetValue}${targetUnit} achieved`,
        'Quality standards met',
        'Stakeholder approval obtained'
      ],
      dependencies: kr.dependencies || [],
      estimated_effort: kr.estimated_effort || estimateEffort(kr.description)
    }
  })
}

function calculateDeadline(index, total) {
  const today = new Date()
  const weeksPerPhase = 12 / total // Distribute over a quarter
  const deadline = new Date(today.getTime() + (index + 1) * weeksPerPhase * 7 * 24 * 60 * 60 * 1000)
  return deadline.toISOString().split('T')[0]
}

function estimateEffort(description) {
  // Simple heuristic based on keywords
  const highEffortKeywords = ['launch', 'build', 'develop', 'create', 'implement']
  const mediumEffortKeywords = ['improve', 'optimize', 'enhance', 'update']
  const lowEffortKeywords = ['document', 'review', 'analyze', 'plan']

  const lowerDesc = (description || '').toLowerCase()

  if (highEffortKeywords.some(kw => lowerDesc.includes(kw))) return 'High (8-12 weeks)'
  if (mediumEffortKeywords.some(kw => lowerDesc.includes(kw))) return 'Medium (4-8 weeks)'
  if (lowEffortKeywords.some(kw => lowerDesc.includes(kw))) return 'Low (1-4 weeks)'

  return 'Medium (4-8 weeks)' // Default
}
```

### Additional Transform Functions

```javascript
TRANSFORMS.problemToContradiction = (leanCanvasProblem, options = {}) => {
  /**
   * Converts Lean Canvas problem statement to TRIZ contradiction format
   */

  const problems = Array.isArray(leanCanvasProblem)
    ? leanCanvasProblem
    : [leanCanvasProblem]

  return problems.map(problem => ({
    improving_parameter: options.improving || 'User satisfaction',
    worsening_parameter: options.worsening || 'Cost/Complexity',
    current_state: problem,
    desired_state: `${problem} solved without increasing ${options.worsening || 'cost'}`,
    contradiction_type: 'Technical' // vs. Physical
  }))
}

TRANSFORMS.goalToIdentity = (smartGoal, options = {}) => {
  /**
   * Converts SMART goal to Atomic Habits identity statement
   * Input: "Lose 20 pounds in 6 months"
   * Output: "I am a healthy person who makes nutritious choices"
   */

  // Extract goal type from keywords
  const goalLower = smartGoal.toLowerCase()

  const identityMap = {
    'lose weight|fitness|exercise|workout': 'I am a healthy person who prioritizes fitness',
    'learn|study|read|course': 'I am a lifelong learner who constantly improves',
    'save money|invest|budget': 'I am a financially responsible person who plans ahead',
    'write|author|publish': 'I am a writer who creates valuable content',
    'build|create|develop': 'I am a builder who brings ideas to life',
    'lead|manage|coordinate': 'I am a leader who inspires others'
  }

  for (const [pattern, identity] of Object.entries(identityMap)) {
    const regex = new RegExp(pattern, 'i')
    if (regex.test(goalLower)) {
      return identity
    }
  }

  // Fallback: Generic identity
  return `I am someone who achieves: ${smartGoal}`
}

TRANSFORMS.directCopy = (value, options = {}) => {
  /**
   * Simple pass-through transformation with optional formatting
   */
  return value
}
```

---

## Integration with Life OS Steps

### Step 5: Auto-Link Before Scoring

When user reaches Step 5 (scoring), the system should automatically check for auto-linking opportunities:

```markdown
### After Consilium, Before Scoring:

**Auto-Linking Check:**

```bash
# Detect available auto-links
echo "🔍 Scanning for auto-linkable fields..."

AUTO_LINKS=$(node -e "
  const { detectSources, autoPopulate } = require('./auto-linking-engine')
  const template = loadCurrentTemplate()
  const sources = detectSources(template)
  const populated = autoPopulate(template, sources)
  console.log(JSON.stringify(populated))
")

if [ -n "$AUTO_LINKS" ] && [ "$AUTO_LINKS" != "{}" ]; then
  LINK_COUNT=$(echo "$AUTO_LINKS" | jq 'length')
  echo "✅ Found $LINK_COUNT auto-linkable fields"

  # Show preview
  node -e "
    const { confirmAutoLinks } = require('./auto-linking-engine')
    const populated = $AUTO_LINKS
    const confirmed = confirmAutoLinks(populated, loadCurrentTemplate())
    saveAutoLinks(confirmed)
  "
else
  echo "ℹ️  No auto-links available (workflow plan or other templates not found)"
fi
```

**Manual Override:**
If auto-linking suggests a value but you want to change it:
1. Accept the auto-link to populate the field
2. Edit the field manually in the template
3. Manual edits always take precedence over auto-links
```

### Step 8: Auto-Link to Deep Plan

When generating Deep Plan in Step 8, maximum auto-population should occur:

```markdown
### Deep Plan Auto-Population Strategy:

**L1 (Mission):**
- Source Priority: OKRs.objectives > Workflow Plan.project_name > Lean Canvas.value_proposition
- Confidence Threshold: 0.90

**L2 (Phases):**
- Source Priority: NPV.project_timeline > OKRs.key_results > Progressive Overload.training_blocks
- Transformation: Timeline/results decomposed into 3-5 phases
- Confidence Threshold: 0.85

**L3 (Milestones):**
- Source Priority: Real Options.decision_points > OKRs.initiatives > NPV.milestones
- Confidence Threshold: 0.85

**L4 (Weekly Tasks):**
- Source Priority: Habit Loop.routine > Pomodoro.weekly_schedule > GTD.projects
- Confidence Threshold: 0.80

**L5 (Daily Tasks):**
- Source Priority: Habit Loop.cue > Pomodoro.task_list > Atomic Habits.habit_stack
- Confidence Threshold: 0.80

**Auto-Population Execution:**

```bash
# Initialize Deep Plan with auto-linking
echo "📋 Generating Deep Plan with auto-population..."

node -e "
  const { generateDeepPlan } = require('./auto-linking-engine')

  // Load all available sources
  const sources = {
    workflowPlan: loadWorkflowPlan(),
    okrs: findTemplate('okrs'),
    npv: findTemplate('npv'),
    leanCanvas: findTemplate('lean-canvas'),
    pomodoro: findTemplate('pomodoro'),
    habitLoop: findTemplate('habit-loop'),
    atomicHabits: findTemplate('atomic-habits'),
    gtd: findTemplate('gtd')
  }

  // Generate Deep Plan with maximum auto-population
  const deepPlan = generateDeepPlan(sources, {
    confidenceThreshold: 0.75,
    preferRecent: true,
    includeAlternatives: true
  })

  // Save with metadata
  saveDeepPlan(deepPlan, {
    autoPopulated: true,
    sources: Object.keys(sources).filter(k => sources[k]),
    timestamp: new Date().toISOString()
  })

  // Show summary
  console.log('✅ Deep Plan generated:')
  console.log(\`   L1: \${deepPlan.l1.name}\`)
  console.log(\`   L2: \${deepPlan.l2.length} phases\`)
  console.log(\`   L3: \${deepPlan.l3.length} milestones\`)
  console.log(\`   L4: \${deepPlan.l4.length} weekly tasks\`)
  console.log(\`   L5: \${deepPlan.l5.length} daily tasks\`)
  console.log()
  console.log(\`   Auto-populated: \${deepPlan.metadata.autoPopulatedFields} / \${deepPlan.metadata.totalFields} fields\`)
"
```

**User Review Required:**
Even with high confidence auto-population, user MUST review and approve Deep Plan before finalizing.
```

---

## Conflict Resolution

### When Multiple Sources Populate Same Field

**Resolution Strategy:**

1. **Highest Confidence Wins (Default)**
   - Workflow plan: 1.0 (always authoritative)
   - Same-domain template: 0.9
   - Cross-domain template: 0.7
   - Global memory pattern: 0.6

2. **Recency Tiebreaker**
   - If confidence scores within 0.05, use most recently modified source
   - Example: NPV (0.88, updated yesterday) beats Lean Canvas (0.85, updated last week)

3. **User Override**
   - User can manually select which source to use
   - System presents all options with confidence scores
   - User selection is remembered for future similar conflicts

4. **Merge Strategy (for compatible data types)**
   - **Lists**: Combine and deduplicate
     ```javascript
     // OKRs suggests: ["User growth", "Revenue growth"]
     // Lean Canvas suggests: ["Revenue growth", "Market share"]
     // Merged result: ["User growth", "Revenue growth", "Market share"]
     ```

   - **Numbers**: Present both, ask user which to use or average
     ```javascript
     // NPV suggests growth_rate: 0.15
     // DCF suggests growth_rate: 0.12
     // Options: [Use 0.15] [Use 0.12] [Average: 0.135] [Custom: ___]
     ```

   - **Text**: Show both side-by-side, ask user to choose or combine
     ```javascript
     // Source A: "Increase user engagement through gamification"
     // Source B: "Improve user retention via reward system"
     // Options: [A] [B] [Combine] [Custom]
     ```

### Conflict Resolution UI

```javascript
function resolveConflict(fieldName, options) {
  console.log(`\n⚠️  Conflict detected for field: ${fieldName}`)
  console.log(`   Multiple sources provide different values:\n`)

  // Sort options by confidence (descending)
  const sortedOptions = options.sort((a, b) => b.confidence - a.confidence)

  // Display options
  sortedOptions.forEach((opt, idx) => {
    console.log(`   [${idx + 1}] ${truncate(opt.value, 70)}`)
    console.log(`       Source: ${opt.source}`)
    console.log(`       Confidence: ${(opt.confidence * 100).toFixed(0)}%`)
    console.log(`       Updated: ${formatTimestamp(opt.timestamp)}`)
    console.log()
  })

  // Check if values can be merged
  const canMerge = checkMergeable(sortedOptions.map(o => o.value))
  if (canMerge) {
    console.log(`   [M] Merge all values`)
    console.log()
  }

  console.log(`   [C] Custom value`)
  console.log(`   [S] Skip this field`)

  const choice = askUser(`\n   Select option (1-${sortedOptions.length}${canMerge ? '/M' : ''}/C/S): `)

  if (choice.toUpperCase() === 'M' && canMerge) {
    return {
      value: mergeValues(sortedOptions.map(o => o.value)),
      source: 'merged',
      confidence: Math.max(...sortedOptions.map(o => o.confidence)) * 0.9, // Slightly reduce confidence for merged
      mergedFrom: sortedOptions.map(o => o.source)
    }
  } else if (choice.toUpperCase() === 'C') {
    const customValue = askUser('   Enter custom value: ')
    return {
      value: customValue,
      source: 'user-override',
      confidence: 1.0,
      overrode: sortedOptions.map(o => o.source)
    }
  } else if (choice.toUpperCase() === 'S') {
    return null
  } else if (!isNaN(choice)) {
    const selectedIdx = parseInt(choice) - 1
    if (selectedIdx >= 0 && selectedIdx < sortedOptions.length) {
      return {
        ...sortedOptions[selectedIdx],
        userSelected: true,
        alternatives: sortedOptions.filter((_, i) => i !== selectedIdx)
      }
    }
  }

  // Default to highest confidence if invalid input
  return sortedOptions[0]
}

function checkMergeable(values) {
  // Check if all values are arrays (can concatenate)
  if (values.every(v => Array.isArray(v))) return true

  // Check if all values are numbers (can average)
  if (values.every(v => typeof v === 'number')) return true

  // Check if all values are short strings (can concatenate)
  if (values.every(v => typeof v === 'string' && v.length < 200)) return true

  return false
}

function mergeValues(values) {
  // Merge arrays
  if (values.every(v => Array.isArray(v))) {
    const merged = []
    values.forEach(arr => {
      arr.forEach(item => {
        if (!merged.includes(item)) merged.push(item)
      })
    })
    return merged
  }

  // Average numbers
  if (values.every(v => typeof v === 'number')) {
    return values.reduce((sum, v) => sum + v, 0) / values.length
  }

  // Concatenate strings
  if (values.every(v => typeof v === 'string')) {
    return values.join(' | ')
  }

  return values[0] // Fallback
}
```

---

## Memory Integration

### Store Successful Links

After successful auto-linking, store the outcome in global memory for future optimization:

```bash
# Store successful auto-link
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "auto-linking:lean-canvas→npv:revenue-success" \
  --content "$(cat <<EOF
{
  "source_framework": "lean-canvas",
  "target_framework": "npv",
  "field_mapping": "revenue_streams → cash_inflows",
  "transform_function": "currencyToNPV",
  "confidence": 0.95,
  "user_feedback": "accepted",
  "project_type": "saas-startup",
  "timestamp": "$(date -Iseconds)",
  "outcome": "success"
}
EOF
)"
```

### Learn from Rejections

If user rejects an auto-link, store the rejection to improve future suggestions:

```bash
# Store rejected auto-link
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "auto-linking:okrs→deep-plan:l2-rejected-$(date +%s)" \
  --content "$(cat <<EOF
{
  "source_framework": "okrs",
  "target_framework": "deep-plan",
  "field_mapping": "key_results → l2_phases",
  "transform_function": "okrToL2",
  "confidence": 0.85,
  "user_feedback": "rejected",
  "rejection_reason": "Phases don't align with actual project timeline",
  "project_type": "product-launch",
  "timestamp": "$(date -Iseconds)",
  "outcome": "rejected"
}
EOF
)"

# Update confidence score for this rule
node -e "
  const { updateLinkingRule } = require('./auto-linking-engine')
  updateLinkingRule('okrs', 'deep-plan', 'key_results → l2_phases', {
    confidenceAdjustment: -0.1,
    reason: 'User rejected: Phases don\'t align with timeline'
  })
"
```

### Adaptive Learning

Over time, the system learns which auto-links work well for specific project types:

```javascript
/**
 * Updates linking rule confidence based on historical feedback
 */
function updateLinkingRule(sourceFramework, targetFramework, mapping, adjustment) {
  // Retrieve historical data
  const history = memory.search({
    namespace: 'shared-knowledge',
    pattern: `auto-linking:${sourceFramework}→${targetFramework}:*`
  })

  // Calculate success rate
  const total = history.length
  const successful = history.filter(h => h.outcome === 'success').length
  const successRate = successful / total

  // Find the rule
  const rule = LINKING_RULES[sourceFramework][targetFramework].find(
    r => `${r.sourceField} → ${r.targetField}` === mapping
  )

  if (rule) {
    // Adjust confidence based on success rate
    const newConfidence = (rule.confidence * 0.7) + (successRate * 0.3)

    rule.confidence = Math.max(0.5, Math.min(1.0, newConfidence + (adjustment.confidenceAdjustment || 0)))

    // Store update
    memory.store({
      namespace: 'shared-knowledge',
      key: `auto-linking:${sourceFramework}→${targetFramework}:rule-update`,
      value: {
        mapping: mapping,
        old_confidence: rule.confidence,
        new_confidence: rule.confidence,
        success_rate: successRate,
        sample_size: total,
        reason: adjustment.reason,
        timestamp: new Date().toISOString()
      }
    })

    console.log(`✅ Updated linking rule confidence: ${(rule.confidence * 100).toFixed(0)}%`)
  }
}
```

---

## Examples

### Example 1: Lean Canvas → NPV

**Source (Lean Canvas):**

```yaml
framework: lean-canvas
project_name: "SaaS Analytics Platform"

revenue_streams:
  - "Subscription: $50/mo × 1000 users"
  - "Enterprise: $500/mo × 50 companies"
  - "Professional Services: $10,000 per implementation"

cost_structure:
  - "Cloud Infrastructure: $2000/mo"
  - "Salaries (5 engineers): $20,000/mo"
  - "Marketing: $5,000/mo"
  - "Office & Operations: $3,000/mo"
```

**Auto-Populated (NPV):**

```yaml
framework: npv-analysis
project_name: "SaaS Analytics Platform"  # Auto-linked from workflow plan

cash_inflows:
  year_1:
    subscription_revenue: 600000      # $50 × 1000 × 12
    enterprise_revenue: 300000        # $500 × 50 × 12
    services_revenue: 100000          # $10,000 × 10 implementations (estimated)
    total_inflows: 1000000

  year_2:
    subscription_revenue: 900000      # 50% growth assumption
    enterprise_revenue: 450000        # 50% growth assumption
    services_revenue: 150000          # 50% growth assumption
    total_inflows: 1500000

  # Years 3-5 projected...

cash_outflows:
  year_1:
    infrastructure: 24000             # $2000 × 12
    salaries: 240000                  # $20000 × 12
    marketing: 60000                  # $5000 × 12
    operations: 36000                 # $3000 × 12
    total_outflows: 360000

  year_2:
    infrastructure: 28800             # 20% increase (scaling)
    salaries: 288000                  # 20% increase (new hires)
    marketing: 72000                  # 20% increase
    operations: 43200                 # 20% increase
    total_outflows: 432000

net_cash_flow:
  year_1: 640000    # 1000000 - 360000
  year_2: 1068000   # 1500000 - 432000

# Auto-populated metadata
auto_linking:
  sources:
    - "lean-canvas:revenue_streams → npv:cash_inflows (confidence: 0.95)"
    - "lean-canvas:cost_structure → npv:cash_outflows (confidence: 0.95)"
  transform: "currencyToNPV"
  user_confirmed: true
  timestamp: "2026-02-04T10:30:00Z"
```

### Example 2: OKRs → Deep Plan L2

**Source (OKRs):**

```yaml
framework: okrs
project_name: "Mobile App Launch"

objectives:
  - name: "Launch MVP and validate product-market fit"
    key_results:
      - description: "Sign 100 beta users by Q2 end"
        metric: "User count"
        target_value: 100
        deadline: "2026-06-30"

      - description: "Achieve 4.5/5 average NPS score"
        metric: "NPS"
        target_value: 4.5
        deadline: "2026-06-30"

      - description: "Process 10,000 transactions successfully"
        metric: "Transaction volume"
        target_value: 10000
        deadline: "2026-08-31"

      - description: "Reduce crash rate to <0.5%"
        metric: "Stability"
        target_value: 0.5
        deadline: "2026-07-31"
```

**Auto-Populated (Deep Plan L2):**

```markdown
## L1: Mission
Launch MVP and validate product-market fit for mobile app

## L2: Phases

### L2.1: User Acquisition Phase (Q1-Q2)
**Milestone:** Sign 100 beta users by Q2 end

**Target:**
- Metric: User count
- Goal: 100 users
- Deadline: 2026-06-30

**Success Criteria:**
- ✅ 100 users achieved
- ✅ Quality standards met (active users, not just signups)
- ✅ Stakeholder approval obtained

**Estimated Effort:** High (8-12 weeks)

**Dependencies:** None (can start immediately)

---

### L2.2: Quality & Satisfaction Phase (Q2)
**Milestone:** Achieve 4.5/5 average NPS score

**Target:**
- Metric: NPS
- Goal: 4.5/5
- Deadline: 2026-06-30

**Success Criteria:**
- ✅ 4.5/5 NPS achieved
- ✅ User feedback incorporated
- ✅ Quality standards met

**Estimated Effort:** Medium (4-8 weeks)

**Dependencies:** L2.1 (need users before measuring satisfaction)

---

### L2.3: Stability & Reliability Phase (Q2-Q3)
**Milestone:** Reduce crash rate to <0.5%

**Target:**
- Metric: Stability (crash rate)
- Goal: <0.5%
- Deadline: 2026-07-31

**Success Criteria:**
- ✅ Crash rate below 0.5%
- ✅ All critical bugs fixed
- ✅ Performance benchmarks met

**Estimated Effort:** Medium (4-8 weeks)

**Dependencies:** L2.1 (need user data to identify crashes)

---

### L2.4: Scale Operations Phase (Q3)
**Milestone:** Process 10,000 transactions successfully

**Target:**
- Metric: Transaction volume
- Goal: 10,000 transactions
- Deadline: 2026-08-31

**Success Criteria:**
- ✅ 10,000 transactions processed
- ✅ 99.9% transaction success rate
- ✅ Infrastructure scaled appropriately

**Estimated Effort:** High (8-12 weeks)

**Dependencies:** L2.2, L2.3 (need quality and stability before scaling)

---

**Auto-Linking Metadata:**
- Source: okrs:key_results
- Transform: okrToL2
- Confidence: 0.90
- Fields Auto-Populated: 4/4 L2 phases
- User Confirmed: Yes
- Timestamp: 2026-02-04T10:45:00Z
```

### Example 3: Progressive Overload → Pomodoro

**Source (Progressive Overload):**

```yaml
framework: progressive-overload
project_name: "12-Week Strength Program"

weekly_plan:
  frequency: "4x per week"
  session_duration: "90 min each"
  days: ["Monday", "Tuesday", "Thursday", "Friday"]

sessions:
  - name: "Upper Body Push"
    duration: 90
    exercises: 6

  - name: "Lower Body"
    duration: 90
    exercises: 5

  - name: "Upper Body Pull"
    duration: 90
    exercises: 6

  - name: "Full Body Accessories"
    duration: 90
    exercises: 8
```

**Auto-Populated (Pomodoro):**

```yaml
framework: pomodoro
project_name: "12-Week Strength Program"

weekly_schedule:
  total_pomodoros: 16              # 4 sessions × 4 pomodoros each
  sessions_per_week: 4
  pomodoros_per_session: 4         # 90 min ÷ 25 min ≈ 4 (with breaks)
  total_weekly_minutes: 360
  estimated_weekly_hours: 6.0

time_blocks:
  monday:
    - session: "Upper Body Push"
      time: "07:00"
      duration_minutes: 90
      pomodoros: 4
      breaks: 3
      structure:
        - "Pomodoro 1 (25 min): Warm-up + Compound lifts"
        - "Break 1 (5 min)"
        - "Pomodoro 2 (25 min): Compound lifts continued"
        - "Break 2 (5 min)"
        - "Pomodoro 3 (25 min): Accessory work"
        - "Break 3 (5 min)"
        - "Pomodoro 4 (25 min): Accessory work + Cool-down"

  tuesday:
    - session: "Lower Body"
      time: "07:00"
      duration_minutes: 90
      pomodoros: 4
      breaks: 3
      structure:
        - "Pomodoro 1 (25 min): Warm-up + Squats"
        - "Break 1 (5 min)"
        - "Pomodoro 2 (25 min): Deadlifts"
        - "Break 2 (5 min)"
        - "Pomodoro 3 (25 min): Accessory work"
        - "Break 3 (5 min)"
        - "Pomodoro 4 (25 min): Accessory work + Cool-down"

  # Thursday and Friday similar structure...

outcomes:
  - "Complete 16 focused workout pomodoros per week"
  - "Maintain consistent 4x/week schedule"
  - "Progressive overload tracked each session"

# Auto-linking metadata
auto_linking:
  source: "progressive-overload:weekly_plan"
  transform: "weeklyToPomodoro"
  confidence: 0.90
  fields_populated: ["weekly_schedule", "time_blocks", "outcomes"]
  user_confirmed: true
  timestamp: "2026-02-04T11:00:00Z"
```

---

## Configuration

### Enable/Disable Auto-Linking

Configuration file: `.claude-flow/auto-linking-config.json`

```json
{
  "auto_linking": {
    "enabled": true,
    "confidence_threshold": 0.70,
    "auto_apply_threshold": 0.95,
    "ask_confirmation": true,

    "domains": {
      "business_to_finance": true,
      "business_to_personal": true,
      "health_to_personal": true,
      "finance_to_personal": true,
      "cross_domain": true
    },

    "transform_functions": {
      "currencyToNPV": true,
      "weeklyToPomodoro": true,
      "okrToL2": true,
      "problemToContradiction": true,
      "goalToIdentity": true
    },

    "memory_integration": {
      "store_successes": true,
      "learn_from_rejections": true,
      "adaptive_confidence": true,
      "min_sample_size": 5
    },

    "ui_preferences": {
      "show_confidence_scores": true,
      "show_sources": true,
      "show_alternatives": true,
      "group_by_confidence": true
    }
  }
}
```

### Per-Template Override

Individual templates can override global auto-linking settings:

```yaml
# In template frontmatter
---
framework: npv-analysis
auto_linking:
  enabled: true
  prefer_sources: ["lean-canvas", "bmc"]  # Priority order
  confidence_threshold: 0.80              # Higher than global
  fields:
    cash_inflows:
      auto_populate: true
      sources: ["lean-canvas:revenue_streams", "bmc:revenue_streams"]
    cash_outflows:
      auto_populate: true
      sources: ["lean-canvas:cost_structure", "bmc:cost_structure"]
---
```

### Command-Line Override

Users can enable/disable auto-linking per-session:

```bash
# Disable auto-linking for this template initialization
claude-flow template init npv-analysis --no-auto-link

# Enable with specific confidence threshold
claude-flow template init deep-plan --auto-link --confidence 0.85

# Auto-apply high-confidence links without confirmation
claude-flow template init pomodoro --auto-link --auto-apply
```

---

## Performance Considerations

### Optimization Strategies

1. **Lazy Loading**
   - Only load linking rules when needed
   - Cache frequently used transformations
   - Index templates by framework for fast lookup

2. **Parallel Source Detection**
   - Scan multiple templates concurrently
   - Use worker threads for large projects
   - Implement timeout for slow sources

3. **Incremental Updates**
   - Only re-check modified templates
   - Cache auto-link results until sources change
   - Track dependencies to invalidate cache

4. **Memory Caching**
   - Cache recent auto-link patterns in memory
   - Preload common transformations
   - Use LRU cache for transform results

### Performance Benchmarks

| Operation | Target | Typical | Notes |
|-----------|--------|---------|-------|
| Source detection | <100ms | 50ms | For 10 templates |
| Rule application | <50ms | 20ms | For 20 rules |
| Transform execution | <10ms | 5ms | Per field |
| User confirmation UI | N/A | 10-30s | User interaction |
| Total auto-link process | <500ms | 200ms | Excluding UI |

---

## Error Handling

### Common Errors and Recovery

**Error 1: Source Not Found**
```javascript
try {
  const leanCanvas = findTemplate('lean-canvas')
} catch (err) {
  console.log('ℹ️  Lean Canvas not found, skipping auto-link from that source')
  // Continue with other sources
}
```

**Error 2: Transform Function Fails**
```javascript
try {
  const transformed = TRANSFORMS[rule.transform](value, options)
} catch (err) {
  console.error(`⚠️  Transform failed for ${rule.transform}: ${err.message}`)
  console.log(`   Using raw value instead`)
  const transformed = value // Fallback to raw value
}
```

**Error 3: Circular Dependencies**
```javascript
function detectCircularDependency(source, target, visited = new Set()) {
  if (visited.has(source)) {
    throw new Error(`Circular dependency detected: ${Array.from(visited).join(' → ')} → ${source}`)
  }

  visited.add(source)

  // Check if target has links back to source
  const targetLinks = LINKING_RULES[target]
  if (targetLinks && targetLinks[source]) {
    detectCircularDependency(target, source, visited)
  }
}
```

**Error 4: Data Type Mismatch**
```javascript
function validateDataType(value, expectedType) {
  if (expectedType === 'number' && typeof value !== 'number') {
    console.warn(`⚠️  Expected number, got ${typeof value}. Attempting conversion...`)
    const converted = parseFloat(value)
    if (isNaN(converted)) {
      throw new Error(`Cannot convert "${value}" to number`)
    }
    return converted
  }

  return value
}
```

---

## Future Enhancements

### Planned Features

1. **AI-Powered Link Discovery**
   - Use LLM to discover new linking patterns
   - Suggest custom transform functions
   - Auto-generate linking rules from user behavior

2. **Visual Dependency Graph**
   - Show how templates are linked
   - Visualize data flow between frameworks
   - Highlight circular dependencies

3. **Version Control Integration**
   - Track auto-link history in git
   - Diff auto-populated vs. manual changes
   - Rollback to previous auto-link states

4. **Multi-Project Learning**
   - Share successful linking patterns across projects
   - Build global confidence scores
   - Recommend links based on similar projects

5. **Template Chaining**
   - Auto-suggest next template based on current
   - Pre-populate entire workflow from single source
   - Smart template sequences

---

**Auto-Linking Engine Version:** 1.0
**Last Updated:** 2026-02-04
**Status:** Active
**Documentation Complete:** Yes
