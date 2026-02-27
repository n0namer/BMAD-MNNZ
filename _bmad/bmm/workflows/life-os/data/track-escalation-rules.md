# Track Escalation Rules

**Purpose:** Detect when a project requires deeper analysis than initially selected track provides, and guide upgrade decision.

**Version:** 1.0
**Last Updated:** 2026-02-06

---

## Overview

Life OS uses three processing tracks (Quick, Standard, Deep) based on complexity. During workflow execution, new information may emerge that suggests upgrading to a more comprehensive track. This document defines the complete escalation algorithm.

---

## Complexity Scoring Algorithm

**Scale:** 0-20 points (calculated at Step 01 and recalculated at Step 04/05)

### Variables and Weights

| Variable | Weight | Scoring Guide |
|----------|--------|---------------|
| **Stakeholder Count** | 4 pts | 1 stakeholder = 0pts, 2-3 = 2pts, 4-6 = 3pts, 7+ = 4pts |
| **Budget Range** | 4 pts | <$1K = 0pts, $1K-$10K = 1pt, $10K-$100K = 2pts, $100K-$1M = 3pts, >$1M = 4pts |
| **Risk Level** | 3 pts | Low = 0pts, Medium = 1pt, High = 2pts, Critical = 3pts |
| **Domain Complexity** | 3 pts | Single domain = 0pts, 2 domains = 1pt, 3+ domains = 2pts, Interdisciplinary = 3pts |
| **Technical Unknowns** | 3 pts | All known = 0pts, Some unknowns = 1pt, Many unknowns = 2pts, Research required = 3pts |
| **Timeline Pressure** | 2 pts | Flexible = 0pts, Weeks/Months = 1pt, Days/Weeks = 2pts |
| **Regulatory/Compliance** | 1 pt | None = 0pts, Some = 0.5pts, Strict = 1pt |

**Total:** Sum all variables (max 20 points)

### Track Assignment

```
Complexity Score → Recommended Track
─────────────────────────────────────
0-7   → Quick Track   (Simple, low-stakes)
8-15  → Standard Track (Moderate complexity)
16-20 → Deep Track    (Complex, high-stakes)
```

**Initial Calculation:** At Step 01 (Collect Ideas), calculate based on user's initial description

**Recalculation Triggers:**
- After Step 04 (Consilium) - new insights from specialists
- After Step 05 (Scoring) - contradictions or high-score variance detected
- User reveals new information mid-workflow

---

## Six Escalation Triggers

### Trigger 1: Consilium Divergence

**Condition:** Consilium Lite reveals >50% disagreement among specialists

**Example:**
- Specialist 1 (Product Manager): "This is a quick win, 2 weeks max"
- Specialist 2 (CTO): "This requires 6 months and complete architecture redesign"
- Disagreement: 24 weeks vs 2 weeks = 92% variance

**Detection:**
```
If (max_estimate - min_estimate) / max_estimate > 0.5:
    TRIGGER = "Consilium Divergence"
    RECOMMENDATION = "Upgrade Quick → Standard (full Six Hats analysis needed)"
```

**Why:** Deep disagreement indicates hidden complexity that Quick Track cannot uncover.

---

### Trigger 2: Scoring Contradiction

**Condition:** Two or more criteria score ≥4 on opposing dimensions

**Example:**
- Impact Score: 5/5 (Very High) ← Positive signal
- Feasibility Score: 1/5 (Very Low) ← Negative signal
- Alignment Score: 5/5 (Perfect fit)
- Resources Required: 1/5 (Massive investment needed)

**Opposing pairs:** Impact vs Feasibility, Alignment vs Resources, Urgency vs Complexity

**Detection:**
```
For each opposing pair:
    If (score_A >= 4 AND score_B <= 2) OR (score_A <= 2 AND score_B >= 4):
        CONTRADICTION_COUNT += 1

If CONTRADICTION_COUNT >= 2:
    TRIGGER = "Scoring Contradiction"
    If CURRENT_TRACK == "Quick":
        RECOMMENDATION = "Upgrade Quick → Standard (deeper analysis needed)"
    If CURRENT_TRACK == "Standard":
        RECOMMENDATION = "Upgrade Standard → Deep (TRIZ analysis suggested)"
```

**Why:** Contradictions indicate fundamental trade-offs requiring structured problem-solving (TRIZ).

---

### Trigger 3: User Request

**Condition:** User explicitly asks for more depth

**Examples:**
- "I need more detailed analysis"
- "Can we explore this more thoroughly?"
- "This feels rushed, can we slow down?"

**Detection:**
```
If USER_INPUT contains ["more analysis", "deeper", "thorough", "detailed", "not enough"]:
    TRIGGER = "User Request"
    RECOMMENDATION = "Upgrade to next track level (user-driven decision)"
```

**Why:** User knows context best; always honor depth requests.

---

### Trigger 4: Stakeholder Discovery

**Condition:** New stakeholder group identified during consilium (Quick Track only)

**Example:**
- Initial: "Just a personal project, only affects me"
- During Consilium: Specialist reveals "This will need legal approval, marketing input, and finance sign-off"
- Stakeholders: 1 → 4+ groups

**Detection:**
```
INITIAL_STAKEHOLDERS = parsed_from_step_01
CONSILIUM_STAKEHOLDERS = parsed_from_step_04

If CONSILIUM_STAKEHOLDERS > INITIAL_STAKEHOLDERS * 2:
    TRIGGER = "Stakeholder Discovery"
    RECOMMENDATION = "Upgrade Quick → Standard (multi-party coordination needed)"
```

**Why:** Multi-stakeholder projects require Six Hats analysis to capture all perspectives.

---

### Trigger 5: Budget Revelation

**Condition:** User reveals budget >$1M or investment round involvement (Standard Track only)

**Example:**
- Initial: "We have some budget for this"
- During Scoring: "Actually, this is a $2M Series A initiative"

**Detection:**
```
If BUDGET_REVEALED > $1,000,000 AND CURRENT_TRACK != "Deep":
    TRIGGER = "Budget Revelation"
    RECOMMENDATION = "Upgrade to Deep Track (financial planning + NPV required)"

If INVESTMENT_ROUND_MENTIONED AND CURRENT_TRACK != "Deep":
    TRIGGER = "Budget Revelation (Investor Involvement)"
    RECOMMENDATION = "Upgrade to Deep Track (investor analysis + scenarios needed)"
```

**Why:** High-stakes financial decisions require comprehensive planning (NPV, Monte Carlo, scenario analysis).

---

### Trigger 6: Contradiction Detection

**Condition:** ≥2 fundamental contradictions detected during Standard Track

**Example:**
- Contradiction 1: "Need fast time-to-market" vs "Requires thorough QA and compliance testing"
- Contradiction 2: "Low budget constraint" vs "Needs enterprise-grade infrastructure"

**Detection:**
```
CONTRADICTIONS = []

# Check for common contradiction patterns
If ("fast" OR "quick" OR "urgent") AND ("thorough" OR "comprehensive" OR "compliance"):
    CONTRADICTIONS.append("Speed vs Quality")

If ("low budget" OR "minimal cost") AND ("enterprise" OR "scalable" OR "robust"):
    CONTRADICTIONS.append("Cost vs Quality")

If ("simple" OR "MVP") AND ("feature-rich" OR "complete"):
    CONTRADICTIONS.append("Scope vs Simplicity")

If len(CONTRADICTIONS) >= 2 AND CURRENT_TRACK == "Standard":
    TRIGGER = "Contradiction Detection"
    RECOMMENDATION = "Upgrade Standard → Deep (TRIZ analysis strongly recommended)"
```

**Why:** Multiple contradictions signal need for TRIZ (Theory of Inventive Problem Solving).

---

## Escalation Presentation Template

When escalation trigger fires, present to user:

```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ TRACK ESCALATION NOTICE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

During **{current_step}**, I detected that this idea may need
deeper analysis than the **{current_track} Track** provides.

  **Trigger:** {trigger_description}

  **Current track:** {current_track}
  **Suggested upgrade:** {new_track}

  **What changes if you upgrade:**
  {changes_list}

  **Additional time estimate:** +{X} minutes

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  [U] Upgrade to {new_track} Track
  [K] Keep {current_track} Track (I understand the limitations)

  **Your choice:** [U/K]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Changes List by Upgrade Path

**Quick → Standard:**
```
+ Step 02: Roles Discovery (identify all stakeholders)
+ Step 03: Specialist Match (5-7 specialists instead of 2-3)
+ Step 04: Full Six Hats consilium (multi-perspective analysis)
+ Step 05: Full MCDA scoring (9 criteria instead of 3)
+ Step 06: Portfolio Integration (WIP limits, synergy check)
+ Step 08: Deep Plan L1-L3 (high-level implementation plan)

Additional time: +40-60 minutes
```

**Standard → Deep:**
```
+ Step 00: Goals Discovery (align with long-term objectives)
+ Step 04.5: TRIZ Analysis (structured contradiction resolution)
+ Step 06.5: Portfolio Dashboard (capacity utilization analysis)
+ Step 07: Calendar Sync (milestone scheduling)
+ Step 08: Upgraded to L1-L6 Deep Plan (comprehensive scenarios)
+ Step 08b: Milestone Planning (dependencies + critical path)
+ Step 08c: Gantt Generation (visual timeline)

Additional time: +90-150 minutes
```

**Quick → Deep (rare, but possible):**
```
All Standard additions PLUS:
+ Multi-round consilium (2-3 rounds with synthesis)
+ Extended TRIZ (ARIZ algorithm option)
+ Advanced portfolio analytics
+ Risk scenario modeling

Additional time: +120-180 minutes
```

---

## Implementation Checkpoints

### At Step 04 (Post-Consilium)

```bash
# Recalculate complexity score
NEW_COMPLEXITY = calculate_complexity(
    stakeholders = COUNT_FROM_CONSILIUM,
    budget = REVEALED_BUDGET,
    risks = IDENTIFIED_RISKS,
    domains = CONSILIUM_DOMAINS,
    unknowns = CONSILIUM_UNKNOWNS,
    timeline = TIMELINE_ESTIMATE,
    regulatory = COMPLIANCE_FLAGS
)

# Check for triggers
if TRIGGER_1_CONSILIUM_DIVERGENCE:
    present_escalation_notice("Consilium Divergence", "Standard")

if TRIGGER_4_STAKEHOLDER_DISCOVERY:
    present_escalation_notice("Stakeholder Discovery", "Standard")

# Check if complexity drifted
if NEW_COMPLEXITY > INITIAL_COMPLEXITY + 5:
    present_escalation_notice("Complexity Drift", auto_recommend_track(NEW_COMPLEXITY))
```

### At Step 05 (Post-Scoring)

```bash
# Check for contradictions
CONTRADICTION_COUNT = detect_opposing_scores()

if CONTRADICTION_COUNT >= 2 AND CURRENT_TRACK == "Quick":
    present_escalation_notice("Scoring Contradiction", "Standard")

if CONTRADICTION_COUNT >= 2 AND CURRENT_TRACK == "Standard":
    present_escalation_notice("Scoring Contradiction (TRIZ suggested)", "Deep")

# Check for budget revelation
if BUDGET_REVEALED > 1000000 AND CURRENT_TRACK != "Deep":
    present_escalation_notice("Budget Revelation", "Deep")

# Fundamental contradictions detected
if detect_fundamental_contradictions() >= 2 AND CURRENT_TRACK == "Standard":
    present_escalation_notice("Contradiction Detection (TRIZ recommended)", "Deep")
```

---

## User Override Rules

**User can always:**
- ✅ Decline escalation (system records decision + rationale)
- ✅ Request escalation manually at any step (via `/upgrade` command)
- ✅ Downgrade after escalation (if complexity decreases)

**System behavior on decline:**
```markdown
Understood. Continuing with {current_track} Track.

⚠️ **Limitations acknowledged:**
- {limitation_1}
- {limitation_2}
- {limitation_3}

You can request upgrade anytime by typing `/upgrade`.
```

**System must record:**
- Escalation trigger detected: YES
- User decision: DECLINED
- Rationale provided: {user_explanation}
- Timestamp: {ISO_DATE}

---

## Example Scenarios

### Scenario 1: Quick → Standard (Stakeholder Discovery)

**Initial (Step 01):**
- User: "I want to build a personal habit tracker app"
- Stakeholders: 1 (self)
- Budget: $0 (personal project)
- Complexity Score: 4/20 → Quick Track

**During Consilium (Step 04):**
- Product Manager: "If this goes well, you'll want to share with your team"
- CTO: "Consider data privacy regulations if sharing data"
- UX Designer: "Multi-user mode needs different architecture"
- Stakeholders revealed: 4+ (self, team, legal, architecture)
- Complexity Score: 11/20 → Recalculated

**Trigger:** Stakeholder Discovery (1 → 4 stakeholders)
**Recommendation:** Upgrade Quick → Standard
**User Decision:** Upgrade (acknowledges team/legal involvement)

---

### Scenario 2: Standard → Deep (Budget Revelation)

**Initial (Step 01):**
- User: "We need a new CRM system"
- Budget: "Some budget available"
- Complexity Score: 12/20 → Standard Track

**During Scoring (Step 05):**
- User reveals: "This is a $2.5M Series A initiative with board oversight"
- Stakeholders: Board, investors, executive team
- Complexity Score: 19/20 → Recalculated

**Trigger:** Budget Revelation (>$1M + investor involvement)
**Recommendation:** Upgrade Standard → Deep
**User Decision:** Upgrade (investor analysis required)

---

### Scenario 3: Standard → Deep (Contradiction Detection)

**Initial (Step 01):**
- User: "Launch new product feature"
- Complexity Score: 10/20 → Standard Track

**During Scoring (Step 05):**
- Contradiction 1: Urgency=5 (ship in 2 weeks) vs Feasibility=2 (needs 3 months of testing)
- Contradiction 2: Impact=5 (critical for retention) vs Resources=1 (team fully allocated)
- Fundamental contradictions: 2 detected

**Trigger:** Contradiction Detection (≥2 contradictions)
**Recommendation:** Upgrade Standard → Deep (TRIZ analysis)
**User Decision:** Upgrade (TRIZ to resolve contradictions)

---

## Integration with workflow.md

**References to add:**

1. **Line 270 (Track Escalation Rules section):**
   - Add reference: `trackEscalationRules: './data/track-escalation-rules.md'`

2. **Step 04 (Post-Consilium check):**
   - Add: "See `track-escalation-rules.md` for escalation triggers"
   - Implement: Complexity recalculation + Trigger 1, 4 checks

3. **Step 05 (Post-Scoring check):**
   - Add: "See `track-escalation-rules.md` for contradiction detection"
   - Implement: Trigger 2, 3, 5, 6 checks

---

## Quality Gates

**Escalation decision must include:**
- ✅ Clear trigger identification
- ✅ Specific examples from user's project
- ✅ Quantified impact (time, quality, risk reduction)
- ✅ User acknowledgment of limitations if declined

**System validation:**
```bash
# Before allowing continuation after declined escalation
if ESCALATION_DECLINED:
    require USER_ACKNOWLEDGMENT of:
        - Limited depth of analysis
        - Potential blind spots
        - Reduced confidence in recommendations
```

---

## Metrics to Track

**Per session:**
- Escalation triggers fired: {count}
- Escalations accepted: {count}
- Escalations declined: {count}
- Final track vs initial track: {Quick→Standard, Standard→Deep, etc.}

**Cross-session learning:**
- Which triggers most accurate (user accepts)
- Which triggers over-fire (user always declines)
- Complexity drift patterns (initial vs final score)

**Store in memory:**
```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "life-os:escalation-metrics:{date}" \
  --content "{trigger_stats + acceptance_rate + drift_patterns}"
```

---

**End of Track Escalation Rules**

**Version:** 1.0
**Status:** Complete
**Integration Required:** workflow.md (frontmatter + Step 04/05 references)
