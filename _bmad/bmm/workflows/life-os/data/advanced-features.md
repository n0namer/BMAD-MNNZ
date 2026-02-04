# Life OS Advanced Features

**Purpose:** Advanced capabilities for power users and complex projects.

**Version:** 1.0
**Last Updated:** 2026-02-04
**Target Users:** Power users managing multiple projects, complex portfolios, and cross-domain initiatives

---

## Table of Contents

1. [Multi-Project Portfolio Management](#feature-1-multi-project-portfolio-management)
2. [Stage-Gate Decision Framework](#feature-2-stage-gate-decision-framework)
3. [Adaptive Framework Suggestions](#feature-3-adaptive-framework-suggestions)
4. [Batch Processing Mode](#feature-4-batch-processing-mode)
5. [Template Versioning & History](#feature-5-template-versioning--history)
6. [Smart Calendar Integration](#feature-6-smart-calendar-integration)
7. [Consilium Save & Replay](#feature-7-consilium-save--replay)
8. [Framework Performance Analytics](#feature-8-framework-performance-analytics)
9. [Cross-Project Learning](#feature-9-cross-project-learning)
10. [Export & Sharing](#feature-10-export--sharing)
11. [Advanced Scoring Algorithms](#feature-11-advanced-scoring-algorithms)
12. [Risk Management Dashboard](#feature-12-risk-management-dashboard)
13. [AI-Powered Pattern Detection](#feature-13-ai-powered-pattern-detection)
14. [Custom Framework Builder](#feature-14-custom-framework-builder)

---

## Feature 1: Multi-Project Portfolio Management

**Use Case:** Managing 5-10 projects simultaneously with resource constraints, strategic alignment, and capacity limits.

### Strategic Buckets

Life OS organizes projects into strategic buckets based on your life domains:

```yaml
strategic_buckets:
  business_career:
    max_active: 3
    resource_allocation: 35%
    priority_weight: 0.30

  finance_investments:
    max_active: 2
    resource_allocation: 20%
    priority_weight: 0.20

  health_wellness:
    max_active: 2
    resource_allocation: 20%
    priority_weight: 0.25

  personal_development:
    max_active: 3
    resource_allocation: 15%
    priority_weight: 0.15

  relationships_social:
    max_active: 2
    resource_allocation: 10%
    priority_weight: 0.10
```

### Implementation

**Portfolio View Command:**
```bash
# View entire portfolio
life-os portfolio view

# Output:
# ┌─────────────────────────────┬────────┬────────┬──────────┐
# │ Bucket                      │ Active │ Limit  │ Capacity │
# ├─────────────────────────────┼────────┼────────┼──────────┤
# │ Business & Career           │ 2/3    │ OK     │ 67%      │
# │ Finance & Investments       │ 2/2    │ AT MAX │ 100%     │
# │ Health & Wellness           │ 1/2    │ OK     │ 50%      │
# │ Personal Development        │ 3/3    │ AT MAX │ 100%     │
# │ Relationships & Social      │ 0/2    │ OK     │ 0%       │
# └─────────────────────────────┴────────┴────────┴──────────┘
#
# Overall Portfolio Health: 72% (GOOD)
# Recommendations:
# - ⚠️ Finance bucket at capacity - defer new financial projects
# - ⚠️ Personal Dev at capacity - consider killing lowest priority
# - 💡 Relationships bucket underutilized - opportunity for new project
```

**Check Capacity:**
```bash
# Check if capacity exists for new project
life-os portfolio capacity --bucket "Health & Wellness"

# Output:
# ✅ CAPACITY AVAILABLE
# Bucket: Health & Wellness
# Current: 1/2 active projects
# Available slots: 1
# Resource allocation: 20% (10% currently used, 10% available)
```

**Add Project to Portfolio:**
```bash
# Add new project with bucket assignment
life-os portfolio add "Marathon Training Program" \
  --bucket "Health & Wellness" \
  --priority high \
  --estimated-duration "6 months"

# Output:
# ✅ Project added to portfolio
# Bucket: Health & Wellness (1/2 → 2/2)
# Portfolio health updated: 72% → 78%
# Next step: Run Step 1 (Collect Ideas) for this project
```

### Portfolio Scoring

Projects are scored across multiple dimensions for portfolio prioritization:

```yaml
portfolio_scoring:
  strategic_alignment: 0.30    # Does it fit strategic buckets?
  resource_availability: 0.25  # Can we staff/fund it?
  risk_adjusted_impact: 0.25   # Expected value / risk
  synergy_with_existing: 0.20  # Does it complement other projects?
```

**Scoring Algorithm:**
```javascript
function calculatePortfolioScore(project, portfolio) {
  // Strategic Alignment (0-10)
  const alignment = calculateStrategicAlignment(
    project.bucket,
    portfolio.strategic_priorities
  )

  // Resource Availability (0-10)
  const resources = calculateResourceAvailability(
    project.estimated_effort,
    portfolio.current_utilization,
    portfolio.bucket_limits[project.bucket]
  )

  // Risk-Adjusted Impact (0-10)
  const impact = project.expected_impact * (1 - project.risk_score / 10)

  // Synergy (0-10)
  const synergy = calculateSynergy(
    project,
    portfolio.active_projects
  )

  // Weighted score
  const score = (
    alignment * 0.30 +
    resources * 0.25 +
    impact * 0.25 +
    synergy * 0.20
  )

  return {
    total: score,
    breakdown: { alignment, resources, impact, synergy },
    recommendation: score >= 7.0 ? "APPROVE" :
                   score >= 5.5 ? "CONDITIONAL" :
                   "DEFER"
  }
}
```

### WIP Limits by Bucket

**Default WIP Limits:**
- **Business & Career:** max 3 projects (strategic focus)
- **Finance & Investments:** max 2 projects (high attention required)
- **Health & Wellness:** max 2 projects (consistency over quantity)
- **Personal Development:** max 3 projects (learning can parallel)
- **Relationships & Social:** max 2 projects (quality connections)
- **Total Portfolio:** max 10 active projects across all buckets

**Enforcement:**
```bash
# Try to add project when bucket is full
life-os portfolio add "Side Business Launch" --bucket "Business & Career"

# Output:
# ❌ BUCKET AT CAPACITY
# Bucket: Business & Career (3/3 active)
#
# Active projects in this bucket:
# 1. Product Launch Q2 (Priority: High, Score: 8.2)
# 2. Team Expansion (Priority: Medium, Score: 7.5)
# 3. Process Optimization (Priority: Low, Score: 6.8)
#
# Options:
# 1. Kill lowest priority project (#3 - Process Optimization)
# 2. Defer new project until capacity opens
# 3. Override WIP limit (not recommended)
#
# [Kill #3] [Defer new] [Override] [Cancel]
```

### Portfolio Health Dashboard

**Real-Time Health Metrics:**
```bash
life-os portfolio health

# Output:
# 📊 PORTFOLIO HEALTH DASHBOARD
#
# Overall Score: 78/100 (GOOD)
# ├─ Strategic Alignment: 85/100 ✅
# ├─ Resource Utilization: 72/100 ⚠️
# ├─ Risk Balance: 68/100 ⚠️
# └─ Progress Velocity: 82/100 ✅
#
# Active Projects: 8/10
# At Risk: 1 (Process Optimization - behind schedule)
# On Track: 6
# Ahead: 1 (Marathon Training - ahead 2 weeks)
#
# Bucket Balance:
# ┌──────────────────────┬────────┬──────────┬────────┐
# │ Bucket               │ Active │ Health   │ Trend  │
# ├──────────────────────┼────────┼──────────┼────────┤
# │ Business & Career    │ 3/3    │ 82/100   │ ↑      │
# │ Finance & Invest.    │ 2/2    │ 75/100   │ →      │
# │ Health & Wellness    │ 2/2    │ 90/100   │ ↑↑     │
# │ Personal Dev.        │ 1/3    │ 65/100   │ ↓      │
# │ Relationships        │ 0/2    │ N/A      │ -      │
# └──────────────────────┴────────┴──────────┴────────┘
#
# Recommendations:
# 💡 Personal Development underutilized - start new learning project
# ⚠️ Process Optimization 3 weeks behind - escalate or kill
# 🎯 Overall velocity strong - maintain current pace
```

---

## Feature 2: Stage-Gate Decision Framework

**Use Case:** Multi-phase projects with go/no-go decision points at critical milestones.

### Gate Structure

Life OS implements 4 decision gates aligned with workflow steps:

```yaml
gates:
  gate_1_idea:
    location: "After Step 4 (Consilium)"
    criteria:
      - consilium_consensus: ">80%"
      - initial_feasibility: "PASS"
      - role_clarity: "ALL roles identified"
    decision_options:
      - "PROCEED to scoring"
      - "KILL idea"
      - "RETURN for more consilium"

  gate_2_scoring:
    location: "After Step 5 (Scoring)"
    criteria:
      - mcda_score: "≥6.5"
      - strategic_alignment: "≥7.0"
      - risk_assessment: "≤7.0"
    decision_options:
      - "PROCEED to integration"
      - "RE-SCORE with new data"
      - "KILL idea"

  gate_3_integration:
    location: "After Step 6 (Integration)"
    criteria:
      - portfolio_fit: "true"
      - resource_availability: "true"
      - conflicts_resolved: "true"
    decision_options:
      - "PROCEED to planning"
      - "DEFER until capacity"
      - "KILL idea"

  gate_4_planning:
    location: "After Step 8 (Deep Plan)"
    criteria:
      - quality_gate: "PASS"
      - timeline_realistic: "true"
      - dependencies_mapped: "true"
    decision_options:
      - "EXECUTE project"
      - "RE-PLAN with adjustments"
      - "KILL idea"
```

### Gate 1: Idea Gate

**Location:** After Step 4 (Consilium)

**Purpose:** Validate idea viability before investing in detailed scoring.

**Criteria:**
```yaml
idea_gate_criteria:
  consilium_consensus:
    threshold: ">80%"
    measure: "% of specialists agreeing on core approach"
    weight: 0.40

  initial_feasibility:
    checks:
      - "Technical feasibility assessment"
      - "Resource availability check"
      - "Timeline realism"
    all_must_pass: true
    weight: 0.35

  role_clarity:
    requirement: "ALL required roles identified"
    measure: "Count of specialists vs required"
    weight: 0.25
```

**Decision Matrix:**
```javascript
function evaluateIdeaGate(project) {
  const consensus = calculateConsiliumConsensus(project.consilium)
  const feasibility = assessInitialFeasibility(project)
  const roles = validateRolesCoverage(project.consilium.specialists)

  const score = (
    consensus.percentage * 0.40 +
    feasibility.score * 0.35 +
    roles.coverage * 0.25
  ) * 10

  if (score >= 8.0 && consensus.percentage >= 80) {
    return {
      decision: "PROCEED",
      confidence: "HIGH",
      next: "Move to Step 5 (Scoring)"
    }
  } else if (score >= 6.5) {
    return {
      decision: "CONDITIONAL",
      confidence: "MEDIUM",
      required_actions: identifyGaps(consensus, feasibility, roles),
      next: "Address gaps, then re-evaluate"
    }
  } else {
    return {
      decision: "KILL",
      confidence: "HIGH",
      reasons: identifyKillReasons(consensus, feasibility, roles)
    }
  }
}
```

**Gate 1 Review Screen:**
```bash
life-os gate review 1

# Output:
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🚦 GATE 1: IDEA VALIDATION
# Project: Marathon Training Program
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#
# Criteria Assessment:
# ✅ Consilium Consensus: 92% (threshold: >80%)
#    - 11/12 specialists agreed on approach
#    - Only Green Hat suggested alternative (noted)
#
# ✅ Initial Feasibility: PASS
#    - Technical: ✅ Training plan available
#    - Resources: ✅ 6 months available
#    - Timeline: ✅ Realistic for beginner
#
# ✅ Role Clarity: ALL ROLES IDENTIFIED
#    - Coach (Red Hat): Motivation & commitment
#    - Trainer (White Hat): Training science
#    - Nutritionist (Yellow Hat): Fueling strategy
#    - Physio (Black Hat): Injury prevention
#
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Gate Score: 8.7/10
#
# 🟢 RECOMMENDATION: PROCEED
# Confidence: HIGH
#
# Next Steps:
# 1. Move to Step 5 (Scoring)
# 2. Use MCDA framework for detailed evaluation
# 3. Target score: ≥6.5 to pass Gate 2
#
# [✅ Approve & Proceed] [⏸️ Pause for Review] [❌ Kill Idea]
```

### Gate 2: Scoring Gate

**Location:** After Step 5 (Scoring)

**Purpose:** Validate project value before portfolio integration.

**Criteria:**
```yaml
scoring_gate_criteria:
  mcda_score:
    threshold: "≥6.5"
    measure: "Weighted MCDA score (0-10)"
    weight: 0.40

  strategic_alignment:
    threshold: "≥7.0"
    measure: "Fit with strategic buckets & priorities"
    weight: 0.35

  risk_assessment:
    threshold: "≤7.0"
    measure: "Overall risk score (0-10, lower better)"
    weight: 0.25
```

**Auto-Kill Rules:**
```yaml
auto_kill_conditions:
  mcda_score_critical: "<5.0"
  strategic_misalignment: "<5.0"
  unacceptable_risk: ">8.0"
  resource_conflict: "true"
  consilium_divergence: ">60%"
```

**Gate 2 Evaluation:**
```javascript
function evaluateScoringGate(project) {
  const mcda = project.scoring.mcda_final_score
  const alignment = project.scoring.strategic_alignment
  const risk = project.scoring.risk_score

  // Check auto-kill conditions first
  if (mcda < 5.0) {
    return {
      decision: "AUTO-KILL",
      reason: "MCDA score below minimum threshold",
      score: mcda
    }
  }

  if (alignment < 5.0) {
    return {
      decision: "AUTO-KILL",
      reason: "Strategic misalignment - does not fit portfolio",
      score: alignment
    }
  }

  if (risk > 8.0) {
    return {
      decision: "AUTO-KILL",
      reason: "Unacceptable risk level",
      score: risk
    }
  }

  // Gate criteria evaluation
  const passed_mcda = mcda >= 6.5
  const passed_alignment = alignment >= 7.0
  const passed_risk = risk <= 7.0

  if (passed_mcda && passed_alignment && passed_risk) {
    return {
      decision: "PROCEED",
      confidence: "HIGH",
      next: "Move to Step 6 (Integration)"
    }
  } else if (passed_mcda && passed_alignment) {
    return {
      decision: "CONDITIONAL",
      confidence: "MEDIUM",
      concern: "Risk score borderline",
      required_action: "Develop risk mitigation plan",
      next: "Re-score after mitigation identified"
    }
  } else {
    return {
      decision: "RE-SCORE",
      reasons: identifyGaps({ mcda, alignment, risk }),
      next: "Gather additional data and re-run Step 5"
    }
  }
}
```

### Gate 3: Integration Gate

**Location:** After Step 6 (Integration)

**Purpose:** Confirm portfolio fit and resource availability.

**Criteria:**
```yaml
integration_gate_criteria:
  portfolio_fit:
    checks:
      - "Bucket has capacity"
      - "No strategic conflicts"
      - "Complements existing projects"
    weight: 0.40

  resource_availability:
    checks:
      - "Time available matches estimate"
      - "Budget available (if applicable)"
      - "Dependencies resolvable"
    weight: 0.35

  conflicts_resolved:
    checks:
      - "Calendar conflicts resolved"
      - "Priority conflicts resolved"
      - "Resource conflicts resolved"
    weight: 0.25
```

### Gate 4: Planning Gate

**Location:** After Step 8 (Deep Plan)

**Purpose:** Final quality check before execution commitment.

**Criteria:**
```yaml
planning_gate_criteria:
  quality_gate:
    checks:
      - completeness: "All 6 layers present (L1-L6)"
      - depth: "L5 has daily/weekly breakdown"
      - frameworks: "≥2 frameworks applied"
      - metrics: "Success criteria defined"
    weight: 0.40

  timeline_realistic:
    checks:
      - "Milestones spaced appropriately"
      - "Buffer time included (15-20%)"
      - "Dependencies sequenced correctly"
    weight: 0.35

  dependencies_mapped:
    checks:
      - "All dependencies identified"
      - "Critical path calculated"
      - "Blockers have mitigation plans"
    weight: 0.25
```

**Gate 4 Quality Checklist:**
```markdown
## Planning Gate Quality Checklist

### Completeness (Weight: 0.40)
- [ ] L1: Purpose & Vision defined
- [ ] L2: Phases & Milestones mapped
- [ ] L3: Success Criteria & Metrics clear
- [ ] L4: Frameworks applied (min 2)
- [ ] L5: Daily/Weekly tasks broken down
- [ ] L6: Micro-Habits & Routines defined

### Timeline Realism (Weight: 0.35)
- [ ] Total duration matches capacity
- [ ] Milestones have 2-4 week spacing
- [ ] Buffer time: 15-20% of total
- [ ] Dependencies sequenced (no circular)
- [ ] Critical path identified

### Dependencies & Risks (Weight: 0.25)
- [ ] All dependencies listed
- [ ] External blockers identified
- [ ] Mitigation plans for top 3 risks
- [ ] Escalation paths defined
- [ ] Fallback plans for critical tasks

**Scoring:**
- ALL items checked: PASS (proceed to execution)
- 1-2 items missing: CONDITIONAL (fix gaps first)
- 3+ items missing: FAIL (re-do Deep Plan)
```

---

## Feature 3: Adaptive Framework Suggestions

**Use Case:** System learns which frameworks work best for which project types and suggests optimal combinations.

### Learning Algorithm

```javascript
function suggestFrameworks(project) {
  // 1. Detect project attributes
  const attributes = {
    domain: detectDomain(project.description),
    complexity: estimateComplexity(project),
    timeAvailable: project.deadline ?
      calculateDaysUntil(project.deadline) : null,
    userExperience: getUserExperienceLevel(),
    keywords: extractKeywords(project.description)
  }

  // 2. Search memory for similar projects
  const similar = memorySearch({
    query: project.description,
    limit: 20,
    namespace: "shared-knowledge:framework-usage",
    filters: {
      domain: attributes.domain,
      status: "completed"
    }
  })

  // 3. Rank frameworks by success rate
  const rankings = {}

  similar.forEach(past => {
    // Each past project used 2-4 frameworks
    past.frameworks_used.forEach(fw => {
      if (!rankings[fw.name]) {
        rankings[fw.name] = {
          uses: 0,
          successes: 0,
          total_rating: 0,
          avg_time_minutes: 0,
          domains: {}
        }
      }

      rankings[fw.name].uses++

      if (past.outcome === "success") {
        rankings[fw.name].successes++
      }

      rankings[fw.name].total_rating +=
        past.framework_ratings[fw.name] || 0

      rankings[fw.name].avg_time_minutes +=
        past.framework_time[fw.name] || 0

      // Track domain-specific performance
      const domain = past.domain
      if (!rankings[fw.name].domains[domain]) {
        rankings[fw.name].domains[domain] = {
          uses: 0,
          successes: 0
        }
      }
      rankings[fw.name].domains[domain].uses++
      if (past.outcome === "success") {
        rankings[fw.name].domains[domain].successes++
      }
    })
  })

  // 4. Calculate confidence scores
  const suggestions = Object.entries(rankings)
    .map(([name, stats]) => {
      const overall_success_rate =
        (stats.successes / stats.uses) * 100

      const domain_success_rate =
        stats.domains[attributes.domain] ?
        (stats.domains[attributes.domain].successes /
         stats.domains[attributes.domain].uses) * 100 : 0

      const avg_rating = stats.total_rating / stats.uses
      const avg_time = stats.avg_time_minutes / stats.uses

      // Confidence score combines:
      // - Overall success rate (40%)
      // - Domain-specific success rate (30%)
      // - User rating (20%)
      // - Sample size reliability (10%)
      const confidence = (
        overall_success_rate * 0.40 +
        domain_success_rate * 0.30 +
        (avg_rating / 5) * 100 * 0.20 +
        Math.min(stats.uses / 10, 1) * 100 * 0.10
      )

      return {
        framework: name,
        confidence: confidence,
        success_rate: overall_success_rate,
        domain_success_rate: domain_success_rate,
        avg_rating: avg_rating,
        avg_time_minutes: Math.round(avg_time),
        sample_size: stats.uses,
        domain_sample: stats.domains[attributes.domain]?.uses || 0
      }
    })
    .filter(s => s.sample_size >= 3) // Minimum 3 past uses
    .sort((a, b) => b.confidence - a.confidence)

  return suggestions.slice(0, 5) // Top 5
}
```

### Framework Synergy Detection

```javascript
function detectSynergies(frameworks) {
  // Frameworks often used together successfully
  const synergy_matrix = {
    "Lean Canvas": ["OKRs", "NPV", "SWOT"],
    "OKRs": ["Lean Canvas", "SMART Goals", "Pomodoro"],
    "Pomodoro": ["OKRs", "Atomic Habits", "GTD"],
    "TRIZ": ["SWOT", "Six Thinking Hats", "Design Thinking"],
    "NPV": ["Lean Canvas", "Break-Even Analysis", "ROIC"]
  }

  const suggestions = []

  frameworks.forEach(fw => {
    const synergistic = synergy_matrix[fw.framework] || []
    synergistic.forEach(partner => {
      // Check if partner is also in top suggestions
      const partner_fw = frameworks.find(f => f.framework === partner)
      if (partner_fw) {
        suggestions.push({
          pair: [fw.framework, partner],
          combined_confidence: (fw.confidence + partner_fw.confidence) / 2,
          synergy_reason: getSynergyReason(fw.framework, partner)
        })
      }
    })
  })

  return suggestions
    .sort((a, b) => b.combined_confidence - a.combined_confidence)
    .slice(0, 3) // Top 3 pairs
}

function getSynergyReason(fw1, fw2) {
  const reasons = {
    "Lean Canvas + OKRs": "Canvas defines business model, OKRs set execution goals",
    "Lean Canvas + NPV": "Canvas qualitative, NPV quantitative validation",
    "Pomodoro + Atomic Habits": "Pomodoro structures time, Habits ensure consistency",
    "TRIZ + SWOT": "TRIZ solves contradictions identified by SWOT",
    "OKRs + SMART Goals": "OKRs set direction, SMART makes goals actionable"
  }

  const key = `${fw1} + ${fw2}`
  return reasons[key] || "Commonly used together with success"
}
```

### Suggestion Display

```bash
life-os frameworks suggest "Launch online course on productivity"

# Output:
# 💡 **Framework Suggestions**
#
# Based on 23 similar projects in memory (18 in "Personal Development" domain):
#
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 1. ⭐⭐⭐⭐⭐ Lean Canvas
#    Confidence: 94/100
#    Success Rate: 92% overall (89% in Personal Development)
#    Average Rating: 4.6/5 (based on 12 uses)
#    Typical Time: 45 minutes
#
#    Why recommended:
#    - Used 12 times for projects with "launch" + "online" keywords
#    - High success rate for course/product launches
#    - Helps validate business model before building
#
#    💡 Works well with: OKRs, NPV
#
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 2. ⭐⭐⭐⭐⭐ OKRs (Objectives & Key Results)
#    Confidence: 91/100
#    Success Rate: 87% overall (91% in Personal Development)
#    Average Rating: 4.3/5 (based on 15 uses)
#    Typical Time: 35 minutes
#
#    Why recommended:
#    - Used 15 times for "goals" + "measurement" keywords
#    - Excellent for tracking course launch metrics
#    - Pairs well with Lean Canvas for execution
#
#    💡 Works well with: Lean Canvas, SMART Goals
#
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 3. ⭐⭐⭐⭐ Atomic Habits Framework
#    Confidence: 87/100
#    Success Rate: 93% overall (95% in Personal Development)
#    Average Rating: 4.7/5 (based on 18 uses)
#    Typical Time: 30 minutes
#
#    Why recommended:
#    - Highest rating in Personal Development domain
#    - Excellent for building course creation routine
#    - Used successfully for "consistency" projects
#
#    💡 Works well with: Pomodoro, Habit Loop
#
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 4. ⭐⭐⭐⭐ SWOT Analysis
#    Confidence: 83/100
#    Success Rate: 83% overall (80% in Personal Development)
#    Average Rating: 4.1/5 (based on 18 uses)
#    Typical Time: 25 minutes
#
#    Why recommended:
#    - Used for "analysis" + "decision" keywords
#    - Good for assessing course market fit
#    - Quick framework (25 min average)
#
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 5. ⭐⭐⭐⭐ Pomodoro Technique
#    Confidence: 81/100
#    Success Rate: 95% overall (96% in Personal Development)
#    Average Rating: 4.8/5 (based on 22 uses)
#    Typical Time: 15 minutes (setup)
#
#    Why recommended:
#    - Highest overall success rate
#    - Perfect for "productivity" + "time management"
#    - Essential for course content creation sessions
#
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔗 **Recommended Combinations:**
#
# 1. Lean Canvas + OKRs (Confidence: 92/100)
#    → Canvas defines business model, OKRs set execution goals
#    → Used together in 8/23 similar projects (all successful)
#
# 2. Atomic Habits + Pomodoro (Confidence: 89/100)
#    → Habits ensure consistency, Pomodoro structures time
#    → Used together in 12/23 similar projects (92% success rate)
#
# 3. Lean Canvas + NPV (Confidence: 85/100)
#    → Canvas qualitative, NPV quantitative validation
#    → Used together in 6/23 similar projects (100% success rate)
#
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#
# Select frameworks: [1,2,3] [1,2] [Custom selection] [Skip suggestions]
```

---

## Feature 4: Batch Processing Mode

**Use Case:** Process multiple similar ideas efficiently in parallel.

### Batch Collection

```bash
# Start batch collection mode
life-os batch collect --count 10 --timeout 30min

# Output:
# 🎯 BATCH COLLECTION MODE
# Target: 10 ideas
# Timeout: 30 minutes
#
# Idea 1/10: ___________________________________________
# [Enter idea, press Enter for next]
#
# Idea 2/10: ___________________________________________
#
# ...
#
# ✅ 10 ideas collected in 18 minutes
#
# Ideas:
# 1. Launch online course on productivity
# 2. Start morning workout routine
# 3. Learn Python for data analysis
# 4. Build side project: Budget tracker app
# 5. Read 12 books this year
# 6. Improve public speaking skills
# 7. Launch podcast on tech trends
# 8. Meal prep system for healthy eating
# 9. Learn guitar (30 min/day)
# 10. Build investment portfolio
#
# Next: [Process all] [Remove some] [Add more]
```

### Batch Processing Steps

```bash
# Process Steps 1-4 for all ideas at once
life-os batch process --steps 1-4 --ideas all

# What happens:
# 1. Step 1 (Collect) - DONE (already collected)
# 2. Step 2 (Roles Discovery) - Run for each idea in parallel
# 3. Step 3 (Specialist Match) - Run for each idea
# 4. Step 4 (Consilium) - Run for each idea (lite mode for speed)
#
# Processing:
# ┌────────────────────────────────────────┬──────────┬──────────┐
# │ Idea                                   │ Status   │ Progress │
# ├────────────────────────────────────────┼──────────┼──────────┤
# │ 1. Online course on productivity       │ Running  │ Step 3/4 │
# │ 2. Morning workout routine             │ Running  │ Step 4/4 │
# │ 3. Learn Python                        │ Running  │ Step 2/4 │
# │ 4. Budget tracker app                  │ Running  │ Step 3/4 │
# │ 5. Read 12 books                       │ Running  │ Step 4/4 │
# │ 6. Public speaking                     │ Running  │ Step 2/4 │
# │ 7. Launch podcast                      │ Queued   │ Step 1/4 │
# │ 8. Meal prep system                    │ Queued   │ Step 1/4 │
# │ 9. Learn guitar                        │ Queued   │ Step 1/4 │
# │ 10. Investment portfolio               │ Queued   │ Step 1/4 │
# └────────────────────────────────────────┴──────────┴──────────┘
#
# Estimated completion: 22 minutes (parallel execution)
```

### Batch Scoring

```bash
# Score all ideas with consistent criteria
life-os batch score --threshold 6.5

# Output:
# 📊 BATCH SCORING RESULTS
#
# Scored 10 ideas using MCDA framework:
#
# ┌────┬───────────────────────────────┬───────┬────────┬──────┬────────┐
# │ #  │ Idea                          │ Score │ Impact │ Risk │ Status │
# ├────┼───────────────────────────────┼───────┼────────┼──────┼────────┤
# │ 1  │ Online course (productivity)  │ 8.2   │ 9/10   │ 4/10 │ ✅ PASS│
# │ 4  │ Budget tracker app            │ 7.8   │ 8/10   │ 3/10 │ ✅ PASS│
# │ 2  │ Morning workout routine       │ 7.5   │ 7/10   │ 2/10 │ ✅ PASS│
# │ 7  │ Launch podcast                │ 7.1   │ 8/10   │ 5/10 │ ✅ PASS│
# │ 10 │ Investment portfolio          │ 6.9   │ 9/10   │ 6/10 │ ✅ PASS│
# │ 3  │ Learn Python                  │ 6.5   │ 7/10   │ 4/10 │ ⚠️ EDGE│
# │ 8  │ Meal prep system              │ 6.3   │ 6/10   │ 3/10 │ ❌ FAIL│
# │ 5  │ Read 12 books                 │ 6.0   │ 6/10   │ 2/10 │ ❌ FAIL│
# │ 6  │ Public speaking               │ 5.8   │ 7/10   │ 5/10 │ ❌ FAIL│
# │ 9  │ Learn guitar                  │ 5.2   │ 5/10   │ 3/10 │ ❌ FAIL│
# └────┴───────────────────────────────┴───────┴────────┴──────┴────────┘
#
# Summary:
# ✅ Passed (≥6.5): 5 ideas
# ⚠️ Borderline: 1 idea
# ❌ Failed (<6.5): 4 ideas
#
# Recommendations:
# - AUTO-KEEP: Top 5 (scores 6.9-8.2)
# - REVIEW: #3 Learn Python (borderline at 6.5)
# - AUTO-KILL: Bottom 4 (scores 5.2-6.3)
#
# [Accept recommendations] [Manual selection] [Adjust threshold]
```

### Batch Filtering

```bash
# Keep only top 5 projects
life-os batch filter --keep 5 --criteria score

# Output:
# 🎯 BATCH FILTERING
#
# Strategy: Keep top 5 by score
#
# ✅ KEPT (5 projects):
# 1. Online course on productivity (8.2)
# 2. Budget tracker app (7.8)
# 3. Morning workout routine (7.5)
# 4. Launch podcast (7.1)
# 5. Investment portfolio (6.9)
#
# ❌ KILLED (5 projects):
# 6. Learn Python (6.5) - Below top 5
# 7. Meal prep system (6.3)
# 8. Read 12 books (6.0)
# 9. Public speaking (5.8)
# 10. Learn guitar (5.2)
#
# Next steps:
# - Kept projects: Move to Step 6 (Integration)
# - Killed projects: Archived to _archive/batch-2026-02-04/
#
# [Confirm] [Adjust selection] [Cancel]
```

### Time Savings

**Sequential Processing:**
```
10 ideas × (Step 1: 5min + Step 2: 8min + Step 3: 10min + Step 4: 30min)
= 10 × 53 min = 530 minutes (8.8 hours)
```

**Batch Processing:**
```
Step 1: 20min (collect all at once)
Steps 2-4: 120min (parallel processing with shared consilium)
= 140 minutes (2.3 hours)
```

**Savings: 73% time reduction (8.8h → 2.3h)**

---

## Feature 5: Template Versioning & History

**Use Case:** Track changes to project plans over time, compare versions, and understand evolution.

### Auto-Snapshot System

**Snapshot Triggers:**
```yaml
auto_snapshot_triggers:
  step_completion:
    - step: 4  # After Consilium
      label: "consilium_baseline"
    - step: 5  # After Scoring
      label: "scoring_baseline"
    - step: 8  # After Deep Plan
      label: "deep_plan_v1"

  time_based:
    - frequency: "weekly"
      condition: "if project status = ACTIVE"
      label: "weekly_checkpoint"
    - frequency: "monthly"
      condition: "if project status = ACTIVE"
      label: "monthly_review"

  milestone_based:
    - trigger: "milestone_completed"
      label: "milestone_{milestone_name}"
    - trigger: "phase_completed"
      label: "phase_{phase_number}_complete"

  manual:
    - command: "life-os snapshot create"
      label: "manual_{timestamp}"
```

### Version Storage

**Directory Structure:**
```
_bmad/projects/{project-slug}/
├── current/
│   ├── workflow-plan.md
│   ├── project-plan.md
│   ├── project-journal.md
│   └── templates/
│       ├── lean-canvas.md
│       ├── okrs.md
│       └── ...
└── versions/
    ├── v1-consilium-baseline-20260204-1430/
    │   ├── workflow-plan.md
    │   ├── metadata.json
    │   └── templates/
    ├── v2-scoring-baseline-20260204-1615/
    ├── v3-deep-plan-v1-20260205-0920/
    ├── v4-weekly-checkpoint-20260211-1800/
    └── v5-milestone-mvp-launch-20260218-1400/
```

### Version Metadata

```json
{
  "version": "v3",
  "label": "deep_plan_v1",
  "timestamp": "2026-02-05T09:20:15Z",
  "trigger": "step_completion",
  "step": 8,
  "project": {
    "name": "Online Course Launch",
    "slug": "online-course-launch",
    "status": "PLANNING"
  },
  "changes_since_last": {
    "files_modified": 3,
    "lines_added": 247,
    "lines_deleted": 12,
    "key_changes": [
      "Added 6-layer Deep Plan (L1-L6)",
      "Applied Lean Canvas + OKRs frameworks",
      "Defined 12 milestones over 3 phases"
    ]
  },
  "metrics": {
    "deep_plan_layers": 6,
    "frameworks_applied": 2,
    "milestones_count": 12,
    "estimated_duration_days": 90
  }
}
```

### Version Comparison

```bash
# Compare two versions
life-os version diff v2 v3

# Output:
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# VERSION COMPARISON
# Project: Online Course Launch
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#
# v2: scoring_baseline (2026-02-04 16:15)
#  ↓
# v3: deep_plan_v1 (2026-02-05 09:20)
#
# Changes: 247 lines added, 12 lines deleted, 3 files modified
#
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📊 SCORING CHANGES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#
# MCDA Score: 7.8 → 8.2 (+0.4)
# - Impact: 8/10 → 9/10 (increased after market research)
# - Feasibility: 7/10 → 7/10 (unchanged)
# - Strategic Fit: 8/10 → 9/10 (aligned with Q2 goals)
#
# Risk Score: 4/10 → 7/10 (+3) ⚠️ INCREASED
# Reason: Discovered compliance requirements for course platform
#
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📅 DEEP PLAN ADDED
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#
# + L1: Purpose & Vision
#   - Vision: "Become go-to resource for productivity in tech"
#   - Success: 1000 students, 4.5+ rating, $50K revenue
#
# + L2: Phases & Milestones (3 phases, 12 milestones)
#   - Phase 1: Content Creation (Weeks 1-4)
#     * M1: Course outline complete
#     * M2: First 3 modules recorded
#     * M3: All content recorded
#     * M4: Content edited & polished
#   - Phase 2: Platform Setup (Weeks 5-6)
#     * M5: Platform selected & configured
#     * M6: Payment integration tested
#     * M7: Email automation set up
#     * M8: Landing page live
#   - Phase 3: Launch & Marketing (Weeks 7-12)
#     * M9: Beta launch (50 students)
#     * M10: Feedback incorporated
#     * M11: Public launch
#     * M12: First 1000 students milestone
#
# + L3: Success Criteria
#   - 1000 students enrolled within 6 months
#   - 4.5+ average rating
#   - $50K revenue in Year 1
#   - 30% completion rate
#
# + L4: Frameworks Applied
#   - Lean Canvas: Business model validation
#   - OKRs: Goal tracking (O1: Launch successfully)
#
# + L5: Daily/Weekly Breakdown
#   - Week 1-4: 2 hours/day content creation
#   - Week 5-6: 1 hour/day platform setup
#   - Week 7-12: 3 hours/week marketing
#
# + L6: Micro-Habits & Routines
#   - Daily: 7:00 AM - 30min course work (Pomodoro)
#   - Weekly: Sunday - Review progress & adjust plan
#
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📈 TIMELINE CHANGES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#
# Estimated Duration: 4 weeks → 12 weeks (+8 weeks)
# Reason: Added platform setup and marketing phases
#
# Start Date: 2026-02-10 → 2026-02-10 (unchanged)
# End Date: 2026-03-10 → 2026-05-05 (+8 weeks)
#
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔍 KEY INSIGHTS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#
# 1. Scope expanded significantly (4w → 12w)
#    - Originally: Just content creation
#    - Now: Full launch including platform & marketing
#
# 2. Risk increased due to compliance requirements
#    - Action: Added "Legal review" milestone (M6.5)
#
# 3. Success metrics more concrete
#    - Before: "Launch successful course"
#    - Now: "1000 students, 4.5+ rating, $50K revenue"
#
# [View full diff] [Revert to v2] [Export comparison]
```

### Rollback Feature

```bash
# Revert to previous version
life-os version revert v2

# Output:
# ⚠️ REVERT CONFIRMATION
#
# You are about to revert from:
# v3 (deep_plan_v1, 2026-02-05 09:20)
#
# Back to:
# v2 (scoring_baseline, 2026-02-04 16:15)
#
# This will:
# ❌ Remove Deep Plan (L1-L6)
# ❌ Remove 2 framework templates (Lean Canvas, OKRs)
# ❌ Reset timeline from 12 weeks to 4 weeks
# ❌ Reset risk score from 7/10 to 4/10
#
# Current state will be saved as:
# v4-manual-backup-20260205-1045
#
# Are you sure? [Yes] [No] [View diff first]
```

### History Timeline

```bash
# View version history
life-os version history

# Output:
# 📚 VERSION HISTORY
# Project: Online Course Launch
#
# v5 ● milestone_mvp_launch (2026-02-18 14:00) [CURRENT]
#    │ Trigger: Milestone completed - MVP Launch
#    │ Changes: Launch completed, first 50 beta users onboarded
#    │ Metrics: 50 students, 4.8/5 rating, $2.5K revenue
#    │
# v4 ● weekly_checkpoint (2026-02-11 18:00)
#    │ Trigger: Weekly snapshot
#    │ Changes: Content creation 80% complete, on track
#    │ Metrics: 8/10 modules recorded
#    │
# v3 ● deep_plan_v1 (2026-02-05 09:20)
#    │ Trigger: Step 8 completion
#    │ Changes: +247 lines, Deep Plan added
#    │ Metrics: 6 layers, 2 frameworks, 12 milestones
#    │
# v2 ● scoring_baseline (2026-02-04 16:15)
#    │ Trigger: Step 5 completion
#    │ Changes: MCDA score 7.8, Risk 4/10
#    │ Metrics: Impact 8/10, Feasibility 7/10
#    │
# v1 ● consilium_baseline (2026-02-04 14:30)
#    │ Trigger: Step 4 completion
#    │ Changes: Initial project definition
#    │ Metrics: Consilium consensus 92%
#
# [Compare versions] [Export history] [View specific version]
```

---

## Feature 6: Smart Calendar Integration

**Use Case:** Auto-block time based on Deep Plan + Pomodoro estimates, sync with Google Calendar/Outlook.

### Configuration

```yaml
calendar:
  provider: "google_calendar"  # or "outlook", "apple_calendar"
  api_credentials: "~/.claude-flow/calendar-creds.json"

  auto_block: true

  settings:
    l5_to_events: true           # L5 daily tasks → Calendar events
    pomodoro_to_blocks: true     # Pomodoro sessions → Time blocks
    buffer_time: 15              # Minutes between blocks
    respect_existing: true       # Don't overwrite existing events
    work_hours_only: true        # Only schedule 9 AM - 6 PM

  sync:
    frequency: "hourly"          # Check for updates hourly
    bidirectional: true          # Calendar changes → Update plan
    conflict_resolution: "manual" # or "auto_reschedule"

  event_naming:
    format: "[{project}] {task_name}"
    color_by_bucket: true        # Different color per strategic bucket
    add_links: true              # Link to project files
```

### Auto-Generated Events

From Deep Plan L5 breakdown:

```markdown
## L5: Daily/Weekly Breakdown

### Week 1: Content Creation Phase
- **Mon-Fri 7:00-7:25 AM**: Record module content (Pomodoro 1)
- **Mon-Fri 7:30-7:55 AM**: Edit & polish (Pomodoro 2)
- **Mon-Wed-Fri 8:00-8:25 PM**: Research & outline next module
- **Sunday 9:00-9:30 AM**: Weekly review & planning
```

**Converts to Google Calendar:**

```
Mon 7:00-7:25 AM: [Online Course] Record module content (Pomodoro 1/2)
  📝 Description: Phase 1 - Content Creation
  🔗 Link: file:///.../online-course-launch/project-plan.md#L5
  🎨 Color: Blue (Personal Development bucket)

Mon 7:30-7:55 AM: [Online Course] Edit & polish (Pomodoro 2/2)
  (15 min buffer: 7:55-8:10 AM)

Mon 8:00-8:25 PM: [Online Course] Research & outline next module
  (15 min buffer: 8:25-8:40 PM)

Sun 9:00-9:30 AM: [Online Course] Weekly review & planning
```

### Habit Loop Integration

From L6 Micro-Habits:

```markdown
## L6: Micro-Habits & Routines

**Daily Morning Routine (Habit Loop)**:
1. **Cue**: Wake up at 6:45 AM (alarm)
2. **Routine**:
   - 6:45-7:00: Coffee + review day plan
   - 7:00-7:25: Course work (Pomodoro 1)
   - 7:30-7:55: Course work (Pomodoro 2)
3. **Reward**: Healthy breakfast + podcast (8:00-8:30)
```

**Calendar Blocks:**

```
6:45-7:00 AM: [Habit] Morning coffee + planning
7:00-7:25 AM: [Online Course] Pomodoro 1
7:30-7:55 AM: [Online Course] Pomodoro 2
8:00-8:30 AM: [Habit] Breakfast + podcast (reward)
```

### Bidirectional Sync

**Scenario: User reschedules in Google Calendar**

```
User action:
Moves "[Online Course] Record module" from Mon 7:00 AM → Mon 9:00 AM

Life OS detects change:
⚠️ CALENDAR CONFLICT DETECTED

Your calendar was updated:
- Event: "[Online Course] Record module content"
- Original time: Mon 7:00-7:25 AM
- New time: Mon 9:00-9:25 AM
- Changed by: You (via Google Calendar)

This affects your Deep Plan (L5).

Options:
1. Update Deep Plan to match calendar (recommended)
2. Revert calendar to original plan
3. Mark as one-time exception (don't update plan)

[Update plan] [Revert calendar] [One-time exception]
```

**If user chooses "Update plan":**

```markdown
## L5: Daily/Weekly Breakdown (UPDATED)

### Week 1: Content Creation Phase
- ~~**Mon-Fri 7:00-7:25 AM**: Record module content (Pomodoro 1)~~
- **Mon-Fri 9:00-9:25 AM**: Record module content (Pomodoro 1) ← UPDATED
- **Mon-Fri 7:30-7:55 AM**: Edit & polish (Pomodoro 2)
```

### Conflict Detection

```bash
life-os calendar conflicts

# Output:
# ⚠️ CALENDAR CONFLICTS DETECTED
#
# 3 conflicts found for this week:
#
# 1. Tuesday 10:00-10:30 AM
#    ❌ [Online Course] Platform research
#    🔴 Team meeting (existing calendar event)
#
#    Options:
#    - Reschedule course work to Tue 2:00 PM (available)
#    - Move to Wednesday 10:00 AM (available)
#    - Skip this session (not recommended)
#
# 2. Thursday 7:00-7:25 AM
#    ❌ [Online Course] Record module
#    🔴 Doctor appointment (existing calendar event)
#
#    Options:
#    - Reschedule to Thu 8:00 PM (available)
#    - Move to Friday 7:00 AM (available)
#
# 3. Sunday 9:00-9:30 AM
#    ❌ [Online Course] Weekly review
#    🔴 Family brunch (existing calendar event)
#
#    Options:
#    - Reschedule to Sun 7:00 PM (available)
#    - Move to Saturday 9:00 AM (available)
#
# [Auto-resolve conflicts] [Manual resolution] [View calendar]
```

### Time Blocking Dashboard

```bash
life-os calendar dashboard

# Output:
# 📅 TIME BLOCKING DASHBOARD
# Week of Feb 10-16, 2026
#
# ┌──────────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┐
# │ Time     │ Mon  │ Tue  │ Wed  │ Thu  │ Fri  │ Sat  │ Sun  │
# ├──────────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
# │ 7:00 AM  │ 🔵   │ 🔵   │ 🔵   │ 🔵   │ 🔵   │ ⚪   │ ⚪   │
# │ 8:00 AM  │ 🟢   │ 🟢   │ 🟢   │ 🟢   │ 🟢   │ ⚪   │ ⚪   │
# │ 9:00 AM  │ ⚪   │ 🔴   │ ⚪   │ ⚪   │ ⚪   │ ⚪   │ 🟡   │
# │ ...      │      │      │      │      │      │      │      │
# │ 8:00 PM  │ 🔵   │ ⚪   │ 🔵   │ ⚪   │ 🔵   │ ⚪   │ ⚪   │
# └──────────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┘
#
# Legend:
# 🔵 Online Course (Personal Development)
# 🟢 Morning routine (Habit)
# 🔴 Existing calendar event (conflict)
# 🟡 Weekly review
# ⚪ Available time
#
# Summary:
# - Total blocked: 12.5 hours this week
# - Available: 45 hours (work hours only)
# - Utilization: 28% (healthy)
# - Conflicts: 1 (Tuesday 10 AM)
#
# [Resolve conflicts] [Adjust schedule] [Export to calendar]
```

---

## Feature 7: Consilium Save & Replay

**Use Case:** Save expert consilium configurations for reuse across similar projects.

### Save Consilium Configuration

```bash
# After successful consilium
life-os consilium save "Product Launch Expert Panel"

# Output:
# ✅ CONSILIUM CONFIGURATION SAVED
#
# Name: "Product Launch Expert Panel"
# Created: 2026-02-04 16:30
#
# Configuration:
# ┌─────────────────────────┬──────────────────┬─────────────┐
# │ Specialist              │ Six Thinking Hat │ Focus Area  │
# ├─────────────────────────┼──────────────────┼─────────────┤
# │ Product Strategist      │ 🔵 Blue Hat      │ Coordination│
# │ Market Analyst          │ ⚪ White Hat     │ Data        │
# │ Risk Advisor            │ ⚫ Black Hat     │ Risks       │
# │ Growth Lead             │ 🟡 Yellow Hat    │ Opportunities│
# │ UX Designer             │ 🔴 Red Hat       │ User needs  │
# │ Innovation Expert       │ 🟢 Green Hat     │ Creativity  │
# └─────────────────────────┴──────────────────┴─────────────┘
#
# Mode: deep (45-60 minutes)
# Success rate: N/A (first use)
#
# Saved to: ~/.claude-flow/consilium-configs/product-launch-panel.yaml
```

### Consilium Library

```bash
# List saved consilium configurations
life-os consilium list

# Output:
# 📚 SAVED CONSILIUM CONFIGURATIONS
#
# 1. ⭐⭐⭐⭐⭐ Product Launch Expert Panel
#    Success rate: 94% (17/18 uses)
#    Avg consensus: 89%
#    Avg time: 45 min
#    Last used: 2026-02-03
#    Best for: Product launches, business ideas
#
# 2. ⭐⭐⭐⭐⭐ Health & Fitness Advisory Board
#    Success rate: 96% (24/25 uses)
#    Avg consensus: 92%
#    Avg time: 35 min
#    Last used: 2026-01-28
#    Best for: Health goals, fitness programs
#
# 3. ⭐⭐⭐⭐ Technical Architecture Panel
#    Success rate: 87% (13/15 uses)
#    Avg consensus: 84%
#    Avg time: 55 min
#    Last used: 2026-01-20
#    Best for: Software projects, technical decisions
#
# 4. ⭐⭐⭐⭐ Financial Planning Team
#    Success rate: 91% (10/11 uses)
#    Avg consensus: 88%
#    Avg time: 40 min
#    Last used: 2026-01-15
#    Best for: Investment decisions, financial goals
#
# 5. ⭐⭐⭐ Creative Projects Panel
#    Success rate: 78% (7/9 uses)
#    Avg consensus: 76%
#    Avg time: 50 min
#    Last used: 2025-12-10
#    Best for: Creative work, content creation
#
# [Use saved config] [Create new] [View details]
```

### Replay Consilium

```bash
# Use saved consilium for new project
life-os consilium replay "Product Launch Expert Panel" \
  --project "Online Course Launch"

# Output:
# 🔄 REPLAYING CONSILIUM CONFIGURATION
#
# Configuration: "Product Launch Expert Panel"
# Project: "Online Course Launch"
#
# Loading specialists:
# ✅ Product Strategist (🔵 Blue Hat)
# ✅ Market Analyst (⚪ White Hat)
# ✅ Risk Advisor (⚫ Black Hat)
# ✅ Growth Lead (🟡 Yellow Hat)
# ✅ UX Designer (🔴 Red Hat)
# ✅ Innovation Expert (🟢 Green Hat)
#
# Mode: deep (estimated 45 minutes)
#
# Starting consilium session...
#
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔵 BLUE HAT (Product Strategist) - Coordination
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#
# Let's structure this course launch discussion:
# 1. Market analysis (White Hat)
# 2. Risk assessment (Black Hat)
# 3. Growth opportunities (Yellow Hat)
# 4. User experience (Red Hat)
# 5. Creative approaches (Green Hat)
# 6. Final synthesis (Blue Hat)
#
# [Continue] [Customize order] [Add specialist]
```

### Auto-Suggest Consilium

```bash
# System suggests best consilium config for project
life-os consilium suggest --project "Learn Python for data analysis"

# Output:
# 💡 SUGGESTED CONSILIUM CONFIGURATIONS
#
# Based on project keywords: "learn", "python", "data analysis"
#
# 1. ⭐⭐⭐⭐⭐ Technical Learning Panel (Confidence: 92%)
#    Success rate: 95% for learning projects
#    Specialists:
#    - Learning Expert (🔵 Blue Hat)
#    - Technical Mentor (⚪ White Hat)
#    - Progress Tracker (⚫ Black Hat)
#    - Career Coach (🟡 Yellow Hat)
#    - Motivation Coach (🔴 Red Hat)
#    - Innovation Expert (🟢 Green Hat)
#
#    Why recommended:
#    - Used 20 times for "learn" + "technical" projects
#    - 95% success rate (19/20 completed goals)
#    - Avg time: 35 min (efficient)
#
# 2. ⭐⭐⭐⭐ Data Science Advisory Board (Confidence: 85%)
#    Success rate: 88% for data projects
#    Specialists:
#    - Data Scientist (🔵 Blue Hat)
#    - Python Expert (⚪ White Hat)
#    - ...
#
# 3. ⭐⭐⭐ General Learning Panel (Confidence: 78%)
#    ...
#
# [Use #1] [Use #2] [Custom consilium] [Skip suggestions]
```

### Consilium Analytics

```bash
# View performance metrics for consilium config
life-os consilium analyze "Product Launch Expert Panel"

# Output:
# 📊 CONSILIUM CONFIGURATION ANALYTICS
# Name: Product Launch Expert Panel
#
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Performance Metrics
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#
# Success Rate: 94% (17/18 uses)
# ├─ Completed projects: 16/17
# ├─ High consensus (>80%): 15/17
# └─ Led to Gate 1 PASS: 17/17
#
# Consensus Metrics:
# ├─ Average: 89%
# ├─ Median: 91%
# ├─ Range: 76% - 98%
# └─ Std Dev: 6.2%
#
# Time Metrics:
# ├─ Average: 45 minutes
# ├─ Median: 43 minutes
# ├─ Range: 35-58 minutes
# └─ Mode: deep (recommended)
#
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Specialist Performance
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#
# 🔵 Blue Hat (Product Strategist): ⭐⭐⭐⭐⭐
# - Contribution score: 9.2/10
# - Led to high consensus 94% of time
# - Best insight: "Focus on MVP first, then scale"
#
# ⚪ White Hat (Market Analyst): ⭐⭐⭐⭐⭐
# - Contribution score: 8.9/10
# - Provided critical data in 17/17 sessions
# - Best insight: "Identified underserved market segment"
#
# ⚫ Black Hat (Risk Advisor): ⭐⭐⭐⭐
# - Contribution score: 8.5/10
# - Identified risks that saved 3 projects from failure
# - Best insight: "Regulatory compliance often overlooked"
#
# ...
#
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Usage Patterns
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#
# Most used for:
# 1. Product launches (12 uses)
# 2. Business ideas (4 uses)
# 3. SaaS projects (2 uses)
#
# Success by domain:
# - Product launches: 100% (12/12)
# - Business ideas: 75% (3/4)
# - SaaS projects: 100% (2/2)
#
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Recommendations
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#
# ✅ This config is highly effective for product launches
# ✅ Deep mode recommended (better outcomes than lite)
# 💡 Consider adding "Customer Success Specialist" for SaaS
# ⚠️ Business ideas domain has lower success - may need tweaking
#
# [Use config] [Edit config] [View successful sessions] [Export data]
```

---

## Feature 8: Framework Performance Analytics

**Use Case:** Track which frameworks deliver best results, identify underperformers, optimize framework selection.

### Metrics Tracked

```yaml
framework_metrics:
  lean_canvas:
    total_uses: 47
    successful_uses: 42
    success_rate: 89.4%

    time:
      avg_minutes: 42
      median_minutes: 40
      range: [25, 68]

    ratings:
      avg: 4.6
      median: 5.0
      distribution:
        5_star: 28 (60%)
        4_star: 14 (30%)
        3_star: 4 (8%)
        2_star: 1 (2%)
        1_star: 0 (0%)

    domains:
      business:
        uses: 35
        success_rate: 91%
        avg_rating: 4.7
      personal:
        uses: 12
        success_rate: 83%
        avg_rating: 4.3

    synergies:
      okrs:
        combined_uses: 23
        combined_success: 22
        synergy_rating: 5.0
        boost: "+12% vs solo"
      npv:
        combined_uses: 18
        combined_success: 18
        synergy_rating: 4.8
        boost: "+8% vs solo"

    trending:
      last_30_days: 12 uses (+50% vs prior 30 days)
      momentum: "↑↑ Strong growth"
```

### Framework Dashboard

```bash
life-os frameworks dashboard

# Output:
# 📊 FRAMEWORK PERFORMANCE DASHBOARD
# Based on 487 framework applications across 156 projects
#
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⭐ TOP PERFORMERS (Last 90 Days)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#
# 1. Pomodoro Technique
#    Rating: ⭐⭐⭐⭐⭐ 4.8/5 (56 uses)
#    Success: 95% (53/56 projects completed)
#    Time: 15 min avg (setup only)
#    Trend: ↑↑ (+35% usage vs Q4)
#    Best for: Productivity, time management, focus
#
# 2. Atomic Habits Framework
#    Rating: ⭐⭐⭐⭐⭐ 4.7/5 (41 uses)
#    Success: 93% (38/41 habits established)
#    Time: 30 min avg
#    Trend: ↑↑ (+40% usage vs Q4)
#    Best for: Behavior change, consistency, routines
#
# 3. Lean Canvas
#    Rating: ⭐⭐⭐⭐⭐ 4.6/5 (47 uses)
#    Success: 89% (42/47 projects launched)
#    Time: 42 min avg
#    Trend: ↑ (+18% usage vs Q4)
#    Best for: Business validation, product-market fit
#
# 4. Net Present Value (NPV)
#    Rating: ⭐⭐⭐⭐⭐ 4.6/5 (29 uses)
#    Success: 90% (26/29 good investment decisions)
#    Time: 38 min avg
#    Trend: → (stable)
#    Best for: Financial decisions, ROI analysis
#
# 5. OKRs (Objectives & Key Results)
#    Rating: ⭐⭐⭐⭐ 4.3/5 (62 uses)
#    Success: 87% (54/62 objectives achieved)
#    Time: 35 min avg
#    Trend: ↑ (+22% usage vs Q4)
#    Best for: Goal setting, measurement, alignment
#
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⚠️ UNDERPERFORMERS (May need review)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#
# 1. SMART Goals
#    Rating: ⭐⭐⭐ 3.2/5 (12 uses)
#    Success: 58% (7/12 goals achieved)
#    Time: 28 min avg
#    Trend: ↓ (-40% usage vs Q4)
#    Issue: "Too rigid for creative projects" (common feedback)
#    Recommendation: Use FAST goals instead for creative work
#
# 2. Eisenhower Matrix
#    Rating: ⭐⭐⭐ 3.5/5 (18 uses)
#    Success: 67% (12/18 used consistently)
#    Time: 20 min avg
#    Trend: ↓ (-25% usage vs Q4)
#    Issue: "Hard to prioritize when everything feels urgent"
#    Recommendation: Combine with MoSCoW method
#
# 3. SWOT Analysis (standalone)
#    Rating: ⭐⭐⭐ 3.8/5 (22 uses)
#    Success: 73% (16/22 led to clear decision)
#    Time: 25 min avg
#    Trend: → (stable but low rating)
#    Issue: "Analysis without action" (common feedback)
#    Recommendation: Always pair with TRIZ or decision framework
#
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📈 TRENDING UP (Growing adoption)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#
# 1. TRIZ (40 Principles)
#    Rating: ⭐⭐⭐⭐ 4.4/5 (11 uses, up from 3 last quarter)
#    Growth: +267% usage
#    Why: Effective for solving contradictions in complex projects
#
# 2. Jobs to Be Done (JTBD)
#    Rating: ⭐⭐⭐⭐ 4.2/5 (9 uses, up from 2 last quarter)
#    Growth: +350% usage
#    Why: Better user insight than traditional persona methods
#
# 3. Value Proposition Canvas
#    Rating: ⭐⭐⭐⭐ 4.3/5 (14 uses, up from 6 last quarter)
#    Growth: +133% usage
#    Why: Complements Lean Canvas for product positioning
#
# [View framework details] [Compare frameworks] [Export data]
```

### Framework Comparison

```bash
# Compare two frameworks
life-os frameworks compare "SMART Goals" "FAST Goals"

# Output:
# ⚖️ FRAMEWORK COMPARISON
# SMART Goals vs FAST Goals
#
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Overall Performance
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#
#                        SMART Goals    FAST Goals    Winner
# ────────────────────────────────────────────────────────────
# Rating                 3.2/5          4.5/5         FAST ✅
# Success Rate           58%            91%           FAST ✅
# Uses                   12             8             SMART
# Avg Time               28 min         22 min        FAST ✅
# Trending               ↓ -40%         ↑↑ +150%      FAST ✅
#
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Domain Performance
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#
# Business & Career:
#   SMART: 3.8/5 (4 uses, 75% success)
#   FAST: 4.6/5 (3 uses, 100% success) ✅
#
# Personal Development:
#   SMART: 2.9/5 (6 uses, 50% success)
#   FAST: 4.5/5 (4 uses, 100% success) ✅
#
# Health & Wellness:
#   SMART: 3.0/5 (2 uses, 50% success)
#   FAST: 4.3/5 (1 use, 100% success) ✅
#
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Key Differences
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#
# SMART Goals:
# ✅ Pros:
#    - Well-known framework
#    - Comprehensive structure
#    - Works well for compliance/structured projects
#
# ❌ Cons:
#    - "Too rigid for creative projects" (8/12 feedback)
#    - "Hard to adapt when circumstances change" (6/12)
#    - Lower motivation - feels bureaucratic
#
# FAST Goals:
# ✅ Pros:
#    - Flexible and adaptable
#    - Higher engagement ("feels more dynamic")
#    - Better for fast-moving environments
#    - Transparent progress tracking
#
# ❌ Cons:
#    - Less structure (can be too loose)
#    - Newer framework - less familiar
#
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# User Feedback
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#
# SMART Goals:
# - "Felt too constraining for my creative project" (2026-01-15)
# - "Good for work goals, didn't work for personal" (2026-01-08)
# - "Abandoned after 2 weeks - too much overhead" (2025-12-20)
#
# FAST Goals:
# - "Much better for my startup - adapted as we learned" (2026-01-28)
# - "Loved the transparency aspect - kept team aligned" (2026-01-22)
# - "Easier to maintain momentum vs SMART" (2026-01-10)
#
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Recommendation
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#
# 🏆 WINNER: FAST Goals
#
# Use FAST Goals when:
# - Creative or innovative projects
# - Fast-changing environment
# - Need team alignment and transparency
# - Want higher engagement
#
# Use SMART Goals when:
# - Compliance-driven projects
# - Structured environments
# - Long-term planning (1+ years)
# - Stakeholder reporting required
#
# [View FAST template] [View SMART template] [Try both]
```

### Framework Synergy Matrix

```bash
life-os frameworks synergies

# Output:
# 🔗 FRAMEWORK SYNERGY MATRIX
# Frameworks that work better together
#
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 💎 HIGHEST SYNERGY PAIRS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#
# 1. Lean Canvas + OKRs
#    Synergy: ⭐⭐⭐⭐⭐ 5.0/5
#    Used together: 23 times
#    Success rate: 96% (22/23)
#    Boost vs solo: +12% success rate
#
#    Why it works:
#    - Lean Canvas: Defines business model (WHAT)
#    - OKRs: Sets execution goals (HOW)
#    - Together: Complete strategy + execution framework
#
#    User feedback:
#    "Canvas helped me validate, OKRs kept me on track" (2026-01-25)
#
# 2. Atomic Habits + Pomodoro
#    Synergy: ⭐⭐⭐⭐⭐ 4.9/5
#    Used together: 18 times
#    Success rate: 94% (17/18)
#    Boost vs solo: +8% success rate
#
#    Why it works:
#    - Atomic Habits: Builds consistency (WHY)
#    - Pomodoro: Structures time (HOW)
#    - Together: Motivation + execution system
#
# 3. Lean Canvas + NPV
#    Synergy: ⭐⭐⭐⭐⭐ 4.8/5
#    Used together: 18 times
#    Success rate: 100% (18/18)
#    Boost vs solo: +11% success rate
#
#    Why it works:
#    - Lean Canvas: Qualitative validation
#    - NPV: Quantitative validation
#    - Together: Holistic business case
#
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⚠️ WEAK SYNERGY PAIRS (Avoid combining)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#
# 1. SMART Goals + FAST Goals
#    Synergy: ⭐ 1.2/5
#    Used together: 3 times
#    Success rate: 33% (1/3)
#    Issue: "Conflicting philosophies - confusing" (2 feedbacks)
#
# 2. TRIZ + Lean Canvas
#    Synergy: ⭐⭐ 2.5/5
#    Used together: 4 times
#    Success rate: 50% (2/4)
#    Issue: "Overlap in problem-solving, felt redundant"
#
# [View all synergies] [Export matrix] [Get recommendations]
```

---

## Feature 9: Cross-Project Learning

**Use Case:** Apply lessons from completed projects to new initiatives, avoid repeating mistakes.

### Pattern Recognition Engine

```javascript
function suggestImprovements(currentProject) {
  // 1. Find similar completed projects
  const similar = findSimilarProjects(currentProject, {
    status: "completed",
    similarity_threshold: 0.70,
    max_results: 10,
    weight_factors: {
      domain: 0.30,        // Same strategic bucket
      keywords: 0.25,      // Similar description
      frameworks: 0.20,    // Used same frameworks
      complexity: 0.15,    // Similar scope
      duration: 0.10       // Similar timeline
    }
  })

  // 2. Extract lessons from similar projects
  const lessons = []

  similar.forEach(past => {
    // Challenges encountered
    if (past.challenges && past.challenges.length > 0) {
      past.challenges.forEach(challenge => {
        const applicability = calculateApplicability(
          challenge,
          currentProject
        )

        if (applicability > 0.6) {
          lessons.push({
            type: "challenge",
            challenge: challenge.description,
            solution: challenge.solution,
            outcome: challenge.outcome,
            project: past.name,
            applicability: applicability,
            prevented_by: challenge.could_have_prevented_by
          })
        }
      })
    }

    // Success factors
    if (past.success_factors) {
      past.success_factors.forEach(factor => {
        const relevance = calculateRelevance(factor, currentProject)

        if (relevance > 0.7) {
          lessons.push({
            type: "success_factor",
            factor: factor.description,
            impact: factor.impact_score,
            project: past.name,
            relevance: relevance,
            how_to_apply: factor.how_to_replicate
          })
        }
      })
    }

    // Framework effectiveness
    if (past.frameworks_used) {
      past.frameworks_used.forEach(fw => {
        lessons.push({
          type: "framework_lesson",
          framework: fw.name,
          rating: fw.rating,
          what_worked: fw.what_worked,
          what_didnt: fw.what_didnt,
          project: past.name
        })
      })
    }
  })

  // 3. Rank lessons by priority
  return lessons
    .sort((a, b) => {
      // Prioritize challenges (prevent failures)
      if (a.type === "challenge" && b.type !== "challenge") return -1
      if (b.type === "challenge" && a.type !== "challenge") return 1

      // Then sort by applicability/relevance
      const scoreA = a.applicability || a.relevance || 0
      const scoreB = b.applicability || b.relevance || 0
      return scoreB - scoreA
    })
    .slice(0, 10) // Top 10 lessons
}

function calculateApplicability(challenge, currentProject) {
  // How applicable is this past challenge to current project?
  let score = 0

  // Domain match
  if (challenge.domain === currentProject.domain) score += 0.30

  // Phase match
  if (challenge.phase === currentProject.current_phase) score += 0.25

  // Keywords overlap
  const keywordOverlap = calculateKeywordOverlap(
    challenge.keywords,
    currentProject.keywords
  )
  score += keywordOverlap * 0.25

  // Complexity similarity
  const complexityDiff = Math.abs(
    challenge.complexity - currentProject.estimated_complexity
  )
  score += (1 - complexityDiff / 10) * 0.20

  return Math.min(score, 1.0)
}
```

### Cross-Project Insights Display

```bash
life-os insights suggest

# Output:
# 💡 CROSS-PROJECT LEARNING INSIGHTS
# Project: Online Course Launch
#
# Based on 8 similar completed projects:
# - SaaS Product Launch (87% similar)
# - E-book Publishing (82% similar)
# - Podcast Launch (78% similar)
# - Online Workshop Series (75% similar)
# - Digital Product Launch (74% similar)
# - Membership Site Launch (72% similar)
# - Coaching Program Launch (71% similar)
# - YouTube Channel Monetization (70% similar)
#
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⚠️ CHALLENGES TO AVOID (Lessons from past projects)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#
# 1. ⚠️ Underestimated legal compliance (Applicability: 92%)
#    From: SaaS Product Launch (2025-Q4)
#
#    What happened:
#    - Launched MVP without reviewing GDPR requirements
#    - Had to halt sales for 3 weeks to add compliance
#    - Added unplanned 3 weeks + $5K legal fees
#
#    Solution that worked:
#    - Consulted privacy lawyer in Week 1
#    - Built compliance into MVP (not afterthought)
#    - Added "Legal review" milestone upfront
#
#    Outcome:
#    - No delays on relaunch
#    - Compliance became competitive advantage
#
#    How to apply to your project:
#    ✅ Add "Legal & Compliance Review" as L3 milestone
#    ✅ Budget $2K-5K for legal consultation
#    ✅ Complete before public launch (Phase 3, M11)
#
# 2. ⚠️ Content creation took 2x longer than estimated (Applicability: 89%)
#    From: E-book Publishing (2025-Q3)
#
#    What happened:
#    - Estimated 20 hours for writing
#    - Actually took 45 hours (2.25x over)
#    - Missed launch date by 4 weeks
#
#    Solution that worked:
#    - Added 50% buffer to all creative estimates
#    - Broke content into smaller chunks (easier to track)
#    - Used Pomodoro to track actual time spent
#
#    How to apply to your project:
#    ✅ Your Phase 1 estimate: 4 weeks → Add 2 weeks buffer (6 weeks total)
#    ✅ Use Pomodoro tracking from Day 1
#    ✅ Review actual vs estimated weekly
#
# 3. ⚠️ Email automation setup more complex than expected (Applicability: 85%)
#    From: Digital Product Launch (2025-Q2)
#
#    What happened:
#    - Thought email automation would take 2 hours
#    - Actually took 12 hours (6x over)
#    - Learning curve for new platform
#
#    Solution that worked:
#    - Started email setup in Phase 1 (not Phase 2)
#    - Hired freelancer for $200 (saved 8 hours)
#    - Used proven templates (not custom build)
#
#    How to apply to your project:
#    ✅ Move "Email automation setup" from M7 to M3 (earlier)
#    ✅ Budget $200-300 for freelance help
#    ✅ Or add 10 hours to timeline if DIY
#
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🏆 SUCCESS FACTORS (Replicate these wins)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#
# 1. 🏆 Beta launch with small group was critical (Relevance: 95%)
#    From: SaaS Product Launch (2025-Q4)
#
#    What worked:
#    - Launched to 50 beta users first
#    - Got 127 pieces of feedback
#    - Fixed 12 critical issues before public launch
#    - Beta users became advocates (word-of-mouth)
#
#    Impact: 9/10 (prevented disaster on public launch)
#
#    How to replicate:
#    ✅ You already have M9 "Beta launch (50 students)"
#    ✅ Set up feedback system (Google Form + weekly check-ins)
#    ✅ Plan 2-week feedback incorporation window (M9 → M10)
#    ✅ Incentivize feedback (beta discount or bonus content)
#
# 2. 🏆 Lean Canvas + NPV combination validated business case (Relevance: 91%)
#    From: Podcast Launch (2025-Q3)
#
#    What worked:
#    - Lean Canvas identified target audience clearly
#    - NPV proved sponsorship model was viable
#    - Saved from pursuing unprofitable niche
#
#    Impact: 10/10 (prevented wasted effort)
#
#    How to replicate:
#    ✅ You're already using Lean Canvas (good!)
#    ✅ Add NPV framework to Step 8 (Deep Plan)
#    ✅ Calculate: $50K revenue - ($10K costs) = $40K profit
#    ✅ Compare to time invested: $40K / 200 hours = $200/hour
#
# 3. 🏆 Daily Pomodoro routine created momentum (Relevance: 88%)
#    From: E-book Publishing (2025-Q3)
#
#    What worked:
#    - Committed to 2 Pomodoros every morning (7-8 AM)
#    - Consistency beat intensity (50 min/day × 30 days = 25 hours)
#    - Never missed more than 1 day in a row
#
#    Impact: 8/10 (finished on time despite challenges)
#
#    How to replicate:
#    ✅ You already have L6 habit: "7:00-7:55 AM daily" (great!)
#    ✅ Add accountability: Track streak in journal
#    ✅ Set minimum: 1 Pomodoro on busy days (don't break streak)
#
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📚 FRAMEWORK LESSONS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#
# Lean Canvas (from 3 similar projects):
# ✅ What worked:
#    - Forced clarity on value proposition early
#    - Customer segments section prevented scope creep
#    - Revenue streams helped prioritize features
#
# ⚠️ What didn't:
#    - "Unfair Advantage" section often left blank (hard to define)
#    - Recommendation: Skip or replace with "Key Differentiators"
#
# Pomodoro Technique (from 5 similar projects):
# ✅ What worked:
#    - 25-minute blocks perfect for course content creation
#    - Breaks prevented burnout
#    - Easy to track actual time spent
#
# ⚠️ What didn't:
#    - 5-minute breaks sometimes too short (felt rushed)
#    - Recommendation: Use 10-minute breaks for creative work
#
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📊 SUMMARY
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#
# Recommended adjustments to your plan:
#
# 🔴 HIGH PRIORITY (Do these):
# 1. Add 2-week buffer to Phase 1 (4w → 6w)
# 2. Add "Legal & Compliance Review" milestone
# 3. Move email automation earlier (M7 → M3)
#
# 🟡 MEDIUM PRIORITY (Should do):
# 4. Add NPV framework to validate business case
# 5. Set up beta feedback system upfront
# 6. Track Pomodoro streak in journal
#
# 🟢 LOW PRIORITY (Nice to have):
# 7. Adjust Pomodoro breaks to 10 minutes
# 8. Skip "Unfair Advantage" in Lean Canvas
#
# Estimated impact: +25% success probability if all applied
#
# [Apply all recommendations] [Select specific ones] [View more details]
```

### Automated Plan Adjustments

```bash
# Apply cross-project insights automatically
life-os insights apply --priority high,medium

# Output:
# ✅ APPLYING CROSS-PROJECT INSIGHTS
#
# Applying 6 recommendations (3 high, 3 medium priority)...
#
# 1. ✅ Extended Phase 1 duration: 4 weeks → 6 weeks
#    Updated: project-plan.md L2 timeline
#
# 2. ✅ Added milestone: "Legal & Compliance Review"
#    Location: Phase 2, between M7 and M8
#    Assigned: Week 6
#
# 3. ✅ Moved email automation setup earlier
#    From: M7 (Week 5) → M3 (Week 3)
#    Updated dependencies
#
# 4. ✅ Added NPV framework template
#    Location: templates/npv-analysis.md
#    Linked from Deep Plan L4
#
# 5. ✅ Created beta feedback system checklist
#    Location: templates/beta-feedback-system.md
#    Linked to M9 milestone
#
# 6. ✅ Added Pomodoro streak tracker
#    Location: project-journal.md
#    Daily entry template updated
#
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Summary of changes:
# - Files modified: 4
# - New milestones: 1
# - Timeline adjusted: +2 weeks
# - New templates: 2
#
# Estimated success probability: 72% → 85% (+13%)
#
# Review changes: [View diff] [Undo all] [Keep changes]
```

---

## Feature 10: Export & Sharing

**Use Case:** Share workflow plans with team members, clients, or stakeholders in various formats.

### Export Formats

```bash
# Export to PDF
life-os export pdf "Online Course Launch" \
  --include-templates \
  --include-journal \
  --output "./exports/project-plan.pdf"

# Output:
# 📄 EXPORTING TO PDF
#
# Project: Online Course Launch
#
# Including:
# ✅ Workflow Plan (9 steps)
# ✅ Project Plan (Deep Plan L1-L6)
# ✅ Framework Templates (2):
#    - Lean Canvas
#    - OKRs
# ✅ Project Journal (12 entries)
# ✅ Calendar Schedule (12 weeks)
# ✅ Metrics Dashboard
#
# Generating PDF... (estimated 15 seconds)
#
# ✅ PDF generated successfully
# Location: ./exports/project-plan.pdf
# Size: 2.4 MB
# Pages: 47
#
# [Open PDF] [Share via email] [Upload to cloud]
```

### Export to Notion

```bash
# Sync to Notion workspace
life-os export notion "Online Course Launch" \
  --workspace "Personal" \
  --sync-updates

# Output:
# 🌐 EXPORTING TO NOTION
#
# Connecting to Notion workspace: "Personal"
# ✅ Authenticated
#
# Creating pages:
# ✅ Created: "Online Course Launch" (parent page)
#    ├─ ✅ "Workflow Plan"
#    ├─ ✅ "Deep Plan (L1-L6)"
#    ├─ ✅ "Frameworks"
#    │   ├─ ✅ "Lean Canvas"
#    │   └─ ✅ "OKRs"
#    ├─ ✅ "Project Journal"
#    ├─ ✅ "Calendar Schedule"
#    └─ ✅ "Metrics & Progress"
#
# Setting up sync:
# ✅ Bidirectional sync enabled
#    - Changes in Notion → Update Life OS
#    - Changes in Life OS → Update Notion
#    - Sync frequency: Every 15 minutes
#
# ✅ Export complete
# Notion URL: https://notion.so/online-course-launch-abc123
#
# [Open in Notion] [Configure sync] [Disable sync]
```

### Export to Jira/Linear

```bash
# Create tickets/issues from milestones
life-os export jira "Online Course Launch" \
  --project "COURSE" \
  --create-tickets \
  --link-milestones

# Output:
# 🎫 EXPORTING TO JIRA
#
# Project: Online Course Launch
# Jira Project: COURSE
#
# Creating issues from 12 milestones:
#
# ✅ COURSE-101: Course outline complete
#    Type: Task
#    Priority: High
#    Due: 2026-02-17
#    Description: Complete detailed course outline with 10 modules
#    Labels: phase-1, content-creation
#
# ✅ COURSE-102: First 3 modules recorded
#    Type: Task
#    Priority: High
#    Due: 2026-02-24
#    Depends on: COURSE-101
#
# ✅ COURSE-103: All content recorded
#    Type: Task
#    Priority: High
#    Due: 2026-03-03
#    Depends on: COURSE-102
#
# [... 9 more issues ...]
#
# ✅ Created 12 Jira issues
# ✅ Linked dependencies (11 links)
# ✅ Set up board: "Online Course Launch"
#
# Jira Board: https://jira.company.com/projects/COURSE
#
# Sync options:
# - Manual sync: life-os export jira --sync
# - Auto sync: life-os config set jira.auto_sync true
#
# [Open board] [Configure sync] [View issues]
```

### Export to Markdown (GitHub)

```bash
# Export to Markdown for GitHub README
life-os export markdown "Online Course Launch" \
  --output "README.md" \
  --format github \
  --include-progress

# Generates README.md:
```

```markdown
# Online Course Launch

**Status:** 🟢 IN PROGRESS (Phase 1 - Content Creation)
**Progress:** 23% complete (2/12 milestones)
**Timeline:** Feb 10 - May 5, 2026 (12 weeks)

## 📊 Quick Stats

- **Strategic Bucket:** Personal Development
- **MCDA Score:** 8.2/10
- **Risk Level:** 7/10 (Medium-High)
- **Estimated Revenue:** $50K Year 1

## 🎯 Vision & Goals

**Vision:** Become the go-to resource for productivity in tech

**Success Criteria:**
- 1,000 students enrolled within 6 months
- 4.5+ average rating
- $50K revenue in Year 1
- 30% completion rate

## 📅 Timeline

### Phase 1: Content Creation (Weeks 1-6) - IN PROGRESS ✅

| Milestone | Status | Due Date | Progress |
|-----------|--------|----------|----------|
| M1: Course outline complete | ✅ DONE | Feb 17 | 100% |
| M2: First 3 modules recorded | ✅ DONE | Feb 24 | 100% |
| M3: All content recorded | 🔄 IN PROGRESS | Mar 10 | 40% |
| M4: Content edited & polished | ⏸️ PENDING | Mar 17 | 0% |

### Phase 2: Platform Setup (Weeks 7-8)

| Milestone | Status | Due Date |
|-----------|--------|----------|
| M5: Platform selected & configured | ⏸️ PENDING | Mar 24 |
| M6: Payment integration tested | ⏸️ PENDING | Mar 31 |
| M6.5: Legal & Compliance Review | ⏸️ PENDING | Apr 3 |
| M7: Email automation set up | ⏸️ PENDING | Apr 7 |
| M8: Landing page live | ⏸️ PENDING | Apr 14 |

### Phase 3: Launch & Marketing (Weeks 9-12)

| Milestone | Status | Due Date |
|-----------|--------|----------|
| M9: Beta launch (50 students) | ⏸️ PENDING | Apr 21 |
| M10: Feedback incorporated | ⏸️ PENDING | Apr 28 |
| M11: Public launch | ⏸️ PENDING | May 5 |
| M12: First 1000 students | ⏸️ PENDING | Nov 5 |

## 🛠️ Frameworks Applied

### Lean Canvas
- **Problem:** Tech professionals struggle with productivity
- **Solution:** Structured course with frameworks + community
- **Unique Value:** Combines proven frameworks (Pomodoro, Atomic Habits, GTD)
- **Revenue Streams:** Course sales ($97), coaching upsell ($297)

### OKRs
**Objective 1:** Launch course successfully by May 5
- KR1: 1000 students enrolled by Nov 5
- KR2: 4.5+ average rating
- KR3: 30%+ completion rate
- KR4: $50K revenue in Year 1

## 📈 Progress Tracking

**Overall Progress:** 23% (2/12 milestones completed)

```
█████░░░░░░░░░░░░░░░░░░░░░░░ 23%
```

**Phase Progress:**
- Phase 1 (Content): 50% (2/4 milestones)
- Phase 2 (Platform): 0% (0/5 milestones)
- Phase 3 (Launch): 0% (0/3 milestones)

## 🔗 Links

- [Full Project Plan](./project-plan.md)
- [Project Journal](./project-journal.md)
- [Lean Canvas](./templates/lean-canvas.md)
- [OKRs](./templates/okrs.md)

## 📝 Recent Updates

**2026-02-24:**
- ✅ Completed M2 - First 3 modules recorded
- 🎯 Module 1: "Introduction to Productivity" (25 min)
- 🎯 Module 2: "Pomodoro Technique Deep Dive" (32 min)
- 🎯 Module 3: "Atomic Habits for Developers" (28 min)
- 📊 Total content: 85 minutes (target: 180 minutes)

**2026-02-17:**
- ✅ Completed M1 - Course outline complete
- 📝 10 modules defined (180 minutes total)
- 🎯 Target audience validated: Junior/mid-level developers
- 💡 Added bonus module on AI-assisted productivity

---

*Generated by Life OS - Advanced Workflow Management System*
*Last updated: 2026-02-24 18:30*
```

### Shareable Links

```bash
# Generate shareable link (read-only)
life-os export link "Online Course Launch" \
  --permissions read-only \
  --expiry 30days

# Output:
# 🔗 SHAREABLE LINK GENERATED
#
# Project: Online Course Launch
# Permissions: Read-only
# Expiry: March 6, 2026 (30 days)
#
# Link: https://lifeOS.app/share/abc123def456
#
# What's included:
# ✅ Workflow Plan (current state)
# ✅ Project Plan (L1-L6)
# ✅ Frameworks (Lean Canvas, OKRs)
# ✅ Progress metrics
# ❌ Project Journal (private)
# ❌ Edit capabilities
#
# Share this link with:
# - Team members (for transparency)
# - Clients (for status updates)
# - Stakeholders (for progress tracking)
#
# [Copy link] [Send via email] [Generate QR code] [Revoke link]
```

---

## Feature 11: Advanced Scoring Algorithms

**Use Case:** More sophisticated project evaluation beyond basic MCDA.

### Risk-Adjusted Scoring

```yaml
risk_adjusted_mcda:
  base_score: 8.2          # Standard MCDA score
  risk_score: 7.0          # Risk level (0-10)
  risk_tolerance: 6.0      # User's risk tolerance

  # Risk adjustment formula
  # adjusted_score = base_score × (1 - risk_penalty)
  # risk_penalty = max(0, (risk_score - risk_tolerance) / 10) × 0.3

  calculation:
    risk_penalty: 0.03     # (7.0 - 6.0) / 10 × 0.3
    adjusted_score: 7.95   # 8.2 × (1 - 0.03)
```

### Expected Value Scoring

```yaml
expected_value:
  optimistic_outcome:
    score: 9.5
    probability: 0.20
    value: 1.90

  realistic_outcome:
    score: 7.5
    probability: 0.60
    value: 4.50

  pessimistic_outcome:
    score: 4.0
    probability: 0.20
    value: 0.80

  expected_score: 7.20    # Sum of values
  confidence: "MEDIUM"     # Based on probability distribution
```

---

## Feature 12: Risk Management Dashboard

**Use Case:** Comprehensive risk tracking and mitigation planning.

### Risk Categories

```yaml
risk_categories:
  technical:
    - Platform compatibility issues
    - Content quality concerns
    - Integration challenges

  market:
    - Competition from existing courses
    - Market saturation
    - Pricing pressure

  resource:
    - Time constraints
    - Budget limitations
    - Skill gaps

  external:
    - Regulatory changes
    - Platform policy changes
    - Economic conditions
```

---

## Feature 13: AI-Powered Pattern Detection

**Use Case:** System learns from user behavior and automatically suggests optimizations.

### Pattern Types

```yaml
detected_patterns:
  time_patterns:
    - "Most productive: 7-9 AM (89% task completion)"
    - "Low energy: 2-4 PM (42% task completion)"
    - "Recommended: Schedule creative work for mornings"

  workflow_patterns:
    - "Projects with beta phase: 95% success rate"
    - "Projects without beta: 67% success rate"
    - "Recommendation: Always include beta milestone"

  framework_patterns:
    - "Lean Canvas + NPV: 100% good decisions (18/18)"
    - "SWOT alone: 73% good decisions (16/22)"
    - "Recommendation: Always pair SWOT with action framework"
```

---

## Feature 14: Custom Framework Builder

**Use Case:** Create your own frameworks for domain-specific needs.

### Framework Template

```yaml
custom_framework:
  name: "Course Quality Framework"
  category: "Education"
  created: "2026-02-04"

  sections:
    - name: "Content Quality"
      questions:
        - "Are learning objectives clear?"
        - "Is content engaging and practical?"
        - "Are examples relevant to audience?"

    - name: "Production Quality"
      questions:
        - "Is audio clear and professional?"
        - "Are visuals consistent?"
        - "Is pacing appropriate?"

    - name: "Student Experience"
      questions:
        - "Is navigation intuitive?"
        - "Are resources easily accessible?"
        - "Is support available?"

  scoring:
    method: "weighted_average"
    weights:
      content_quality: 0.50
      production_quality: 0.30
      student_experience: 0.20

  usage_count: 5
  avg_rating: 4.8
  success_rate: 100%
```

---

## Implementation Notes

**Storage:** All advanced features store data in global memory (`~/.claude-flow/agentdb-global/`)

**Performance:** HNSW indexing enables sub-100ms searches even with 100K+ patterns

**CLI Integration:** All features accessible via `life-os` CLI commands

**MCP Integration:** Advanced features leverage MCP tools for intelligence and coordination

---

**Advanced Features Version:** 1.0
**Last Updated:** 2026-02-04
**Total Lines:** ~950
