---
name: 'track-detection-algorithm'
version: '1.0'
purpose: 'Auto-detect idea complexity and recommend processing track (Quick/Standard/Deep)'
consumedBy:
  - step-01-collect-ideas.md
  - step-02-roles-discovery.md
  - step-04-consilium.md
  - step-07-calendar-sync.md
---

# Track Detection Algorithm

## Problem Statement

Currently, all ideas pass through the same 9-step pipeline regardless of complexity.
A simple Telegram bot idea (VK Recipes) and a complex enterprise SaaS platform (Sales QA)
both require 100+ minutes. This is inefficient: simple ideas need 15-20 minutes, not 100+.

The 3-track system routes ideas to the appropriate depth of analysis,
reducing processing time by 60-70% for simple ideas while preserving
full rigor for complex ones.

---

## Track Definitions

### Quick Track (15-20 min)
**Purpose:** Rapid validation for simple, low-stakes ideas.
**Steps:** 1 (Collect) -> 4lite (Consilium Lite: 2-3 specialists, no Six Hats) -> 5 (Scoring) -> 9 (Complete)
**When:** The idea is well-understood, low risk, and the user just needs a quick go/no-go.

### Standard Track (45-60 min)
**Steps:** 1 (Collect) -> 2 (Roles) -> 3 (Specialist Match) -> 4 (Consilium) -> 5 (Scoring) -> 6 (Integration) -> 9 (Complete)
**When:** The idea has moderate complexity, some unknowns, and warrants structured specialist input.

### Deep Track (2-4 hours)
**Steps:** 0 (Goals) -> 1 (Collect) -> 2 (Roles) -> 3 (Specialist Match) -> 4 (Consilium Deep) -> 4.5 (TRIZ) -> 5 (Scoring) -> 6 (Integration) -> 7 (Calendar) -> 8 (Deep Plan L1-L6) -> 8.5 (Final Polish) -> 9 (Complete)
**When:** High-stakes project requiring full analysis, deep planning, and resource allocation.

---

## Algorithm

### Input Parameters

The algorithm uses 6 input signals collected during or immediately after Step 01 (Collect Ideas).
Each parameter is observable from the user's description of the idea without requiring extra questions.

| Parameter | Type | Values | Source |
|-----------|------|--------|--------|
| `domain` | enum | personal, hobby, freelance, small-business, software, saas, ai-ml, franchise, enterprise | Inferred from Step 01 domain field |
| `complexity_signal` | enum | quick-evaluation, standard-analysis, deep-analysis | User's explicit request OR inferred from language |
| `resource_level` | enum | solo-spare-time, solo-focused, small-team, funded-team | Inferred from Step 01 resources + timeline |
| `budget_range` | enum | zero, low (<100K RUB), medium (100K-1M), high (1M+), investment-round | Inferred from description |
| `stakeholder_count` | integer | 1, 2-3, 4+ | Number of people affected or involved |
| `novelty` | enum | proven-model, adaptation, new-in-domain, breakthrough | How novel is this idea relative to existing patterns |

### Signal Detection Rules

**Domain inference** (from Step 01 `domain` field + description keywords):

| Keywords / Signals | Detected Domain |
|-------------------|-----------------|
| pet project, hobby, recipe, personal blog, side thing | personal, hobby |
| freelance, gig, consulting, one-person | freelance |
| small shop, local business, service, cafe | small-business |
| app, SaaS, platform, API, microservice | software, saas |
| ML model, neural network, AI agent, LLM | ai-ml |
| franchise, multi-location, licensing | franchise |
| B2B, enterprise, 50+ employees, compliance, SOC2 | enterprise |

**Complexity signal inference** (from user language):

| User Language Patterns | Detected Signal |
|-----------------------|-----------------|
| "quick look", "just evaluate", "worth it?", "simple idea", "fast check" | quick-evaluation |
| "analyze this", "need specialists", "want to understand", "evaluate properly" | standard-analysis |
| "full analysis", "serious project", "need a plan", "deep dive", "strategic decision" | deep-analysis |
| (no explicit signal given) | determined by scoring matrix below |

**Resource level inference** (from timeline + resources in Step 01):

| Signals | Detected Level |
|---------|----------------|
| "spare time", "evenings", "weekend project", no budget mentioned | solo-spare-time |
| "full-time on this", "main project", "dedicated", small budget | solo-focused |
| "small team", "2-3 people", "co-founder", moderate budget | small-team |
| "hiring team", "investors", "seed round", "significant budget" | funded-team |

**Novelty inference** (from description + domain knowledge):

| Signals | Detected Novelty |
|---------|------------------|
| "like X but for Y", "clone", "standard approach", "well-known model" | proven-model |
| "improve existing", "add feature", "optimize", "better version" | adaptation |
| "no one does this in [market]", "new approach for [domain]" | new-in-domain |
| "never been done", "research-stage", "paradigm shift" | breakthrough |

---

### Scoring Matrix

Each parameter contributes a weighted score. The total determines the recommended track.

| Parameter | Quick (0 pts) | Standard (1 pt) | Deep (2 pts) | Weight |
|-----------|---------------|-----------------|--------------|--------|
| `domain` | personal, hobby | freelance, small-business, software | saas, ai-ml, franchise, enterprise | 2.0 |
| `complexity_signal` | quick-evaluation | standard-analysis | deep-analysis | 3.0 |
| `resource_level` | solo-spare-time | solo-focused | small-team, funded-team | 1.5 |
| `budget_range` | zero, low | medium | high, investment-round | 1.5 |
| `stakeholder_count` | 1 | 2-3 | 4+ | 1.0 |
| `novelty` | proven-model | adaptation | new-in-domain, breakthrough | 1.0 |

**Total possible:** 0 to 20 points (sum of value * weight for each parameter).

### Decision Thresholds

| Score Range | Recommended Track | Confidence Modifier |
|-------------|-------------------|---------------------|
| 0.0 - 5.0 | **Quick** | High if score <= 3.0, Medium if 3.1-5.0 |
| 5.1 - 12.0 | **Standard** | High if 7.0-10.0, Medium if 5.1-6.9 or 10.1-12.0 |
| 12.1 - 20.0 | **Deep** | High if score >= 15.0, Medium if 12.1-14.9 |

### Decision Tree (Deterministic Shortcut)

Before applying the scoring matrix, apply these deterministic rules.
If a rule matches, skip the scoring matrix and use the rule's recommendation.

```
RULE 1: User explicitly said "quick evaluation" or "fast check"
  => Quick Track (confidence: 90%)
  UNLESS domain is enterprise OR budget is investment-round
    => Standard Track (confidence: 75%, override note: "User asked for quick
       but project complexity suggests Standard")

RULE 2: User explicitly said "deep analysis" or "full plan"
  => Deep Track (confidence: 95%)

RULE 3: Domain is enterprise AND budget is high or investment-round
  => Deep Track (confidence: 90%)

RULE 4: Domain is personal or hobby AND resource is solo-spare-time AND budget is zero
  => Quick Track (confidence: 95%)

RULE 5: Domain is saas or ai-ml AND resource is funded-team
  => Deep Track (confidence: 85%)

RULE 6: Stakeholder count >= 4 AND novelty is breakthrough
  => Deep Track (confidence: 90%)

OTHERWISE:
  => Apply Scoring Matrix
```

---

### Confidence Calculation

Confidence reflects how certain the algorithm is in its recommendation.
It accounts for signal clarity (did we have to infer or did the user state explicitly?)
and boundary proximity (is the score near a threshold boundary?).

```
base_confidence = 70%

# Bonus: explicit signals
IF complexity_signal was stated by user (not inferred): +15%
IF domain was stated by user (not inferred): +5%

# Bonus: score distance from boundary
distance_from_nearest_boundary = min(
  abs(score - 5.0),
  abs(score - 12.0)
)
IF distance_from_nearest_boundary > 3.0: +10%
IF distance_from_nearest_boundary > 5.0: +5% (additional)

# Penalty: contradictory signals
IF domain suggests Deep BUT complexity_signal is quick-evaluation: -15%
IF domain suggests Quick BUT resource_level is funded-team: -10%
IF novelty is breakthrough BUT complexity_signal is quick-evaluation: -10%

confidence = clamp(base_confidence + bonuses - penalties, 50%, 99%)
```

### Confidence Levels

| Confidence | Label | Meaning |
|------------|-------|---------|
| 90-99% | HIGH | Very clear recommendation, proceed without hesitation |
| 75-89% | MEDIUM | Good recommendation, worth confirming with user |
| 50-74% | LOW | Ambiguous signals, must ask user to choose |

---

## User Override Protocol

The track recommendation is NEVER forced. The user always has final say.

### Presentation Format

After Step 01 completes (idea collected), present the track recommendation:

```
---------------------------------------------------
TRACK RECOMMENDATION

Based on your idea "{title}":

  Recommended track: {QUICK / STANDARD / DEEP}
  Confidence: {percentage}% ({HIGH / MEDIUM / LOW})
  Estimated time: {15-20 min / 45-60 min / 2-4 hours}

  Key factors:
  - {factor 1}: {value} (contributes to {track})
  - {factor 2}: {value} (contributes to {track})
  - {factor 3}: {value} (contributes to {track})

  Steps included: {step list}

  [Q] Quick Track (15-20 min)
  [S] Standard Track (45-60 min)
  [D] Deep Track (2-4 hours)
  [R] Accept recommendation ({track})

  Your choice: [Q/S/D/R]
---------------------------------------------------
```

### Override Rules

- If user chooses a LIGHTER track than recommended:
  Show a brief risk notice (one line), then proceed with user's choice.
  Example: "Note: Quick track skips specialist consilium and portfolio integration."

- If user chooses a HEAVIER track than recommended:
  Proceed immediately. No warning needed (more analysis is never harmful).

- If confidence is LOW (<75%):
  Do NOT auto-recommend. Present all three tracks equally and ask user to choose.

---

## Step Modifications Per Track

### Quick Track Step Adjustments

| Step | Modification |
|------|-------------|
| Step 01 | Unchanged. Full idea collection. |
| Step 02 | SKIPPED. No roles discovery needed. |
| Step 03 | SKIPPED. No specialist matching needed. |
| Step 04 (Lite) | Consilium Lite: 2-3 auto-selected specialists based on domain. No Six Hats. Single-round recommendations. No TRIZ. 5-10 min. |
| Step 04.5 | SKIPPED. No TRIZ. |
| Step 05 | Simplified scoring: 3 criteria only (Impact, Effort, Alignment). No domain-specific criteria. 5 min. |
| Step 06 | SKIPPED. No portfolio integration. |
| Step 07 | SKIPPED. No calendar sync. |
| Step 08 | SKIPPED. No deep plan. |
| Step 09 | Unchanged. Completion with quick summary. |

### Standard Track Step Adjustments

| Step | Modification |
|------|-------------|
| Step 00 | SKIPPED. Goals not required for standard evaluation. |
| Step 01 | Unchanged. |
| Step 02 | Unchanged. |
| Step 03 | Unchanged. |
| Step 04 | Full consilium with Six Hats. TRIZ optional but not prompted. |
| Step 05 | Full scoring with all criteria. Domain-specific criteria auto-added. |
| Step 06 | Full integration with portfolio health, WIP check. |
| Step 07 | SKIPPED. Calendar sync deferred (user can request later). |
| Step 08 | SKIPPED. Deep plan deferred (user can request later). |
| Step 09 | Unchanged. Completion with standard summary. |

### Deep Track Step Adjustments

| Step | Modification |
|------|-------------|
| All steps | Full pipeline, no modifications. Every step runs completely. |
| Step 00 | Goals Discovery (if not already done in this session). |
| Step 04 | Deep consilium mode forced. TRIZ prompted if contradictions detected. |
| Step 08 | Full L1-L6 deep plan with auto-intelligence and scenario mapping. |

---

## Track Escalation (Mid-Pipeline Upgrade)

During any track, the system monitors for signals that the idea is more complex than initially detected.
If escalation triggers fire, the system offers to upgrade to a higher track.

### Escalation Triggers

| Trigger | From | To | Condition |
|---------|------|----|-----------|
| Consilium divergence | Quick | Standard | Consilium Lite reveals >50% disagreement among specialists |
| Scoring contradiction | Quick/Standard | Standard/Deep | Two criteria score >=4 on opposing dimensions (e.g., Impact=5, Risk=5) |
| User requests depth | Any | Next track up | User says "I need more analysis", "let's go deeper", "this is more complex" |
| Stakeholder discovery | Quick | Standard | During consilium, a new stakeholder group is identified |
| Budget revelation | Standard | Deep | User reveals budget is >1M or involves investment round |

### Escalation Presentation

```
---------------------------------------------------
TRACK ESCALATION NOTICE

During {current step}, I detected that this idea may need
deeper analysis than the {current track} track provides.

  Trigger: {trigger description}
  Current track: {track}
  Suggested upgrade: {new track}

  What changes:
  + {added step 1}
  + {added step 2}
  + Additional {X} minutes estimated

  [U] Upgrade to {new track}
  [K] Keep {current track} (I understand the limits)

  Your choice: [U/K]
---------------------------------------------------
```

---

## Examples

### Example 1: VK Recipes Bot (Quick Track)

**Idea:** "Want to make a Telegram bot that sends daily recipes from VK communities."

**Signal Detection:**
- domain: personal/hobby (Telegram bot, recipes, personal project)
- complexity_signal: (not stated, inferred from simplicity) -> quick-evaluation
- resource_level: solo-spare-time (no team or budget mentioned)
- budget_range: zero (no budget mentioned)
- stakeholder_count: 1 (just the user)
- novelty: proven-model (recipe bots exist)

**Scoring:**
- domain: 0 * 2.0 = 0.0
- complexity_signal: 0 * 3.0 = 0.0
- resource_level: 0 * 1.5 = 0.0
- budget_range: 0 * 1.5 = 0.0
- stakeholder_count: 0 * 1.0 = 0.0
- novelty: 0 * 1.0 = 0.0
- **Total: 0.0**

**Deterministic Rule 4 also matches:** domain=hobby, resource=solo-spare-time, budget=zero

**Result:** Quick Track, confidence 95%
**Time:** 15-20 minutes (vs 100+ minutes in current pipeline)

---

### Example 2: Freelance Design Portfolio Site (Standard Track)

**Idea:** "I want to build a portfolio website for my freelance design business. Need to attract enterprise clients. Budget around 200K RUB."

**Signal Detection:**
- domain: freelance (freelance business, portfolio)
- complexity_signal: standard-analysis (wants to "attract enterprise clients" suggests thoughtfulness)
- resource_level: solo-focused ("my freelance business" = dedicated effort)
- budget_range: medium (200K RUB)
- stakeholder_count: 2-3 (freelancer + target clients)
- novelty: proven-model (portfolio sites are common)

**Scoring:**
- domain: 1 * 2.0 = 2.0
- complexity_signal: 1 * 3.0 = 3.0
- resource_level: 1 * 1.5 = 1.5
- budget_range: 1 * 1.5 = 1.5
- stakeholder_count: 1 * 1.0 = 1.0
- novelty: 0 * 1.0 = 0.0
- **Total: 9.0**

**Result:** Standard Track, confidence 87% (HIGH, score is in 7.0-10.0 sweet spot)
**Time:** 45-60 minutes

---

### Example 3: Sales QA Platform (Deep Track)

**Idea:** "Building an AI-powered sales quality assurance platform. Enterprise SaaS. We have a team of 5 and pre-seed funding of $200K. Need to plan the full architecture and go-to-market."

**Signal Detection:**
- domain: enterprise/saas (enterprise SaaS, B2B)
- complexity_signal: deep-analysis ("plan the full architecture and go-to-market")
- resource_level: funded-team (team of 5, $200K pre-seed)
- budget_range: investment-round ($200K funding)
- stakeholder_count: 4+ (5 team members + investors + enterprise customers)
- novelty: new-in-domain (AI-powered QA is emerging)

**Deterministic Rule 2 matches:** user said "full plan" -> Deep Track (95%)
**Deterministic Rule 3 also matches:** enterprise + investment-round
**Deterministic Rule 5 also matches:** saas + funded-team

**Scoring (for reference):**
- domain: 2 * 2.0 = 4.0
- complexity_signal: 2 * 3.0 = 6.0
- resource_level: 2 * 1.5 = 3.0
- budget_range: 2 * 1.5 = 3.0
- stakeholder_count: 2 * 1.0 = 2.0
- novelty: 2 * 1.0 = 2.0
- **Total: 20.0** (maximum)

**Result:** Deep Track, confidence 99%
**Time:** 2-4 hours (full pipeline justified)

---

### Example 4: Online Course on Cooking (Boundary Case)

**Idea:** "I want to create an online course teaching Russian cuisine. I'm a professional chef. Thinking about Udemy or my own platform. Maybe a small team of 2."

**Signal Detection:**
- domain: small-business (online course, professional, potential platform)
- complexity_signal: (not stated) -> inferred as standard-analysis
- resource_level: small-team (team of 2)
- budget_range: low (no budget explicitly stated but professional = some investment)
- stakeholder_count: 2-3 (chef + assistant + students)
- novelty: adaptation (online courses exist, niche is Russian cuisine)

**Scoring:**
- domain: 1 * 2.0 = 2.0
- complexity_signal: 1 * 3.0 = 3.0
- resource_level: 2 * 1.5 = 3.0
- budget_range: 0 * 1.5 = 0.0
- stakeholder_count: 1 * 1.0 = 1.0
- novelty: 1 * 1.0 = 1.0
- **Total: 10.0**

**Result:** Standard Track, confidence 82% (MEDIUM-HIGH, close to center of Standard range)
**Time:** 45-60 minutes

**Note:** If user later reveals they want to build their own platform (not Udemy),
escalation trigger fires (budget/scope revelation) and system offers upgrade to Deep Track.

---

### Example 5: Personal Fitness Tracking Habit (Quick Track, Edge Case)

**Idea:** "I just want to start tracking my workouts. Nothing fancy, just a habit."

**Signal Detection:**
- domain: personal (personal habit, fitness)
- complexity_signal: quick-evaluation ("nothing fancy", "just a habit")
- resource_level: solo-spare-time (personal habit)
- budget_range: zero (no budget implied)
- stakeholder_count: 1 (just the user)
- novelty: proven-model (workout tracking is well-established)

**Deterministic Rule 4 matches:** personal, solo-spare-time, zero budget

**Result:** Quick Track, confidence 97%
**Time:** 15 minutes

**Edge case note:** This idea is arguably not even a "project" but the user brought it to Life OS.
Quick Track handles it gracefully without wasting time on consilium deep analysis.

---

## Integration Points

### Where the Algorithm Runs

The track detection algorithm runs **immediately after Step 01 completes** (idea captured and saved).
It does NOT require a separate step file; it is embedded in the transition logic between Step 01 and Step 02.

### Implementation in Step 01

After Step 01 saves the idea (section 7: "Save to Claude Flow Memory"), the following sequence executes:

1. Extract the 6 input parameters from the idea record just saved
2. Apply deterministic rules (decision tree)
3. If no rule matched, apply scoring matrix
4. Calculate confidence
5. Present track recommendation to user
6. Route to appropriate next step based on user's choice

### Routing Table

| User Choice | Next Step Loaded |
|-------------|-----------------|
| Quick Track | step-04-consilium.md (with `track: quick` flag in workflow plan) |
| Standard Track | step-02-roles-discovery.md (normal flow) |
| Deep Track | step-00-goals-discovery.md (if goals not done) OR step-01 -> step-02 (if goals exist) |

### Workflow Plan Tracking

When a track is selected, append to workflow plan:

```markdown
## Track Selection (Auto-Detected)

**Recommended Track:** {track}
**Confidence:** {percentage}% ({level})
**Selected Track:** {user's choice}
**Override:** {yes/no}
**Scoring Breakdown:**
- domain: {value} ({points} pts)
- complexity_signal: {value} ({points} pts)
- resource_level: {value} ({points} pts)
- budget_range: {value} ({points} pts)
- stakeholder_count: {value} ({points} pts)
- novelty: {value} ({points} pts)
- **Total:** {total} / 20.0

**Steps Included:** {comma-separated step list}
**Estimated Time:** {range}
```

### Memory Storage

After track selection, save to Claude Flow memory for learning loop:

```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "life-os:track-selection:{IDEA_ID}" \
  --content "{track_data_json}"
```

This enables future analysis of:
- How often users override recommendations
- Which tracks are most used
- Whether confidence correlates with user agreement
- Domain-to-track patterns for improving the algorithm

---

## Appendix: Step-by-Step Time Estimates

| Step | Quick Track | Standard Track | Deep Track |
|------|-------------|----------------|------------|
| Step 00 (Goals) | - | - | 10-15 min |
| Step 01 (Collect) | 5 min | 5 min | 5 min |
| Track Detection | 1 min | 1 min | 1 min |
| Step 02 (Roles) | - | 5 min | 5 min |
| Step 03 (Specialists) | - | 5 min | 5 min |
| Step 04 (Consilium) | 5-10 min (Lite) | 15-20 min | 25-30 min (Deep) |
| Step 04.5 (TRIZ) | - | - (optional) | 10-60 min |
| Step 05 (Scoring) | 5 min (simplified) | 10 min | 10-15 min |
| Step 06 (Integration) | - | 10 min | 15 min |
| Step 07 (Calendar) | - | - | 10 min |
| Step 08 (Deep Plan) | - | - | 20-60 min |
| Step 08.5 (Polish) | - | - | 10 min |
| Step 09 (Complete) | 1 min | 1 min | 1 min |
| **TOTAL** | **17-22 min** | **52-67 min** | **132-242 min** |

---

## Appendix: Consilium Lite Specification (Quick Track Only)

When running the Quick Track, Step 04 operates in "Lite" mode:

**Consilium Lite Rules:**
1. Auto-select 2-3 specialists based on domain (no user confirmation needed)
2. No Six Thinking Hats assignment
3. Each specialist provides ONE recommendation (no multi-round discussion)
4. Consensus is 1-2 bullet points (not full synthesis)
5. No Auto-Suggest Engine trigger
6. No TRIZ offer
7. No Advanced Elicitation or Party Mode menu options
8. Menu options: [C] Continue only

**Domain-to-Specialist Quick Map:**

| Domain | Specialist 1 | Specialist 2 | Specialist 3 (if needed) |
|--------|-------------|-------------|-------------------------|
| personal, hobby | Life Coach | General Advisor | - |
| freelance | Business Advisor | Market Analyst | - |
| small-business | Business Advisor | Finance Analyst | Market Analyst |
| software | Tech Architect | Product Strategist | - |
| saas | Product Strategist | Growth Lead | Tech Architect |
| ai-ml | AI Specialist | Tech Architect | Data Scientist |
| franchise | Business Advisor | Legal Advisor | Finance Analyst |
| enterprise | Product Strategist | Risk Advisor | Finance Analyst |
