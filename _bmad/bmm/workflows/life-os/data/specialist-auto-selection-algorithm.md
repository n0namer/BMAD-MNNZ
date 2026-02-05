# Specialist Auto-Selection Algorithm

**Used in:** Step 04-consilium-lite (Quick Track) and Step 03 (Specialist Match)
**Goal:** Deterministically select the most relevant specialists for a given idea

---

## ALGORITHM OVERVIEW

**Input:** Idea context + available specialists database
**Output:** 1-2 specialists (Quick Track) or 4-8 specialists (Deep Track)

### Selection Logic

**Step 1: Domain Detection**
```
Parse idea description for primary domain:
- Business (revenue, product, customer, growth)
- Finance (budget, investment, ROI, money)
- Health (fitness, wellness, disease, nutrition)
- Personal Dev (learning, skill, habits, mindset)

Primary Domain = highest keyword match %
```

**Step 2: Specialist Scoring**

For each available specialist, calculate score:
```
Score = (domain_match × 0.6) + (availability × 0.3) + (usage_frequency × 0.1)

Where:
- domain_match: [0-1] how well matches primary domain
- availability: [0-1] current WIP as fraction of max (1 - current/max)
- usage_frequency: [0-1] recent usage pattern (normalized)
```

**Step 3: Ranking**
```
Sort specialists by score (descending)

For Quick Track: Select top 1-2
For Standard Track: Select top 4-6
For Deep Track: Select top 6-8
```

**Step 4: Diversity Check (Deep Track Only)**
```
If multiple specialists selected:
- Ensure at least 2 different expertise areas
- If all same domain, replace lowest-scoring with next domain

Example:
- Selected: [Founder, Product Manager, Marketer] → All Business domain
- Replacement: [Founder, Product Manager, Financial Analyst] → Business + Finance
```

---

## SCORING FORMULA DETAILS

### Domain Match Score

```
domain_match = sum(keyword_weight × keyword_found) / total_keywords

Keywords by domain:

Business:
- high weight (0.3): revenue, product, customer, market, growth, strategy
- medium weight (0.2): launch, launch, acquisition, partnership
- low weight (0.1): budget, team, process

Finance:
- high weight: budget, investment, ROI, cash flow, valuation, funding
- medium weight: cost, expense, revenue, price, margin
- low weight: time, risk, resource

Health:
- high weight: fitness, wellness, disease, nutrition, exercise, sleep
- medium weight: habit, behavior, goal, improvement, tracking
- low weight: time, motivation, commitment

Personal Dev:
- high weight: learning, skill, habit, mindset, improvement, growth
- medium weight: motivation, goal, challenge, development, discipline
- low weight: time, progress, commitment
```

### Availability Score

```
availability = 1 - (current_wip / max_wip)

Example:
- Specialist max capacity: 3 projects
- Current WIP: 2 projects
- Availability = 1 - (2/3) = 0.33

Interpretation:
- availability = 1.0 → Completely free
- availability = 0.5 → Half capacity
- availability = 0.0 → At max capacity
- availability < 0 → Overallocated (penalize)
```

### Usage Frequency Score

```
usage_frequency = (times_selected_past_90_days / avg_selection_rate) / 10

Interpretation:
- Frequently used specialist: higher score (visibility)
- Rarely used specialist: lower score (give opportunity)
- Balances consistency with diversity

Example:
- Specialist A used 8 times in 90 days
- Specialist B used 2 times in 90 days
- Average selection rate: 4 per 90 days
- Usage_frequency_A = (8/4) / 10 = 0.2
- Usage_frequency_B = (2/4) / 10 = 0.05
```

---

## SPECIAL CASES

### Case 1: No Specialists in Primary Domain
```
If no specialists available in detected domain:
1. Expand search to secondary domain (if detected)
2. Select from generalist specialists (cross-domain expertise)
3. Fall back to most recent active specialist
```

### Case 2: All Specialists at Capacity
```
If all specialists have availability ≤ 0:
1. Select anyway (system flags overallocation)
2. Display warning: "All specialists at capacity"
3. Recommend: "Reduce WIP or add new specialist"
```

### Case 3: Very Few Specialists (<3)
```
If total specialists < 3:
1. Reuse same specialist if necessary
2. Display warning: "Portfolio understaffed"
3. Recommend: "Add specialists in {missing_domain}"
```

### Case 4: Contradictory Expertise
```
If idea requires specialists from 2+ conflicting domains:
- Business idea that's also Health-focused
- Finance idea that's also Personal Dev-focused

Solution: Select top 1-2 from each domain
Example: [Business Expert, Health Expert] instead of [Business, Business]
```

---

## IMPLEMENTATION EXAMPLES

### Example 1: Quick Track - Health Project

**Idea:** "Create a 12-week fitness transformation program"

**Domain Detection:**
```
Keywords: fitness (3x), exercise (2x), wellness, transformation, health
Primary domain = Health (60% match)
Secondary domain = Personal Dev (25% match)
```

**Available Specialists:**
```
1. Health Coach (domain_match=0.9, availability=0.5, usage=0.15) → Score = 0.54 + 0.15 + 0.015 = 0.705
2. Nutritionist (domain_match=0.8, availability=0.3, usage=0.12) → Score = 0.48 + 0.09 + 0.012 = 0.582
3. Entrepreneur (domain_match=0.2, availability=1.0, usage=0.20) → Score = 0.12 + 0.3 + 0.02 = 0.44
4. Habit Coach (domain_match=0.7, availability=0.7, usage=0.10) → Score = 0.42 + 0.21 + 0.01 = 0.64
```

**Selection (Quick Track = top 1-2):**
```
Ranked:
1. Health Coach (0.705) ← Selected
2. Habit Coach (0.64) ← Selected
3. Nutritionist (0.582)
4. Entrepreneur (0.44)

Result: [Health Coach, Habit Coach]
```

---

### Example 2: Deep Track - Complex Business Project

**Idea:** "Launch AI SaaS product targeting healthcare market with $2M funding"

**Domain Detection:**
```
Keywords:
- Business: launch (2x), product, market, growth, strategy
- Finance: funding, $2M, investment
- Health: healthcare

Primary: Business (50%)
Secondary: Finance (30%)
Tertiary: Health (20%)
```

**Available Specialists:**
```
1. Founder (B domain, avail=0.4, usage=0.18) → 0.54 + 0.12 + 0.018 = 0.678
2. CTO (B domain, avail=0.6, usage=0.14) → 0.42 + 0.18 + 0.014 = 0.614
3. Product Manager (B domain, avail=0.5, usage=0.16) → 0.48 + 0.15 + 0.016 = 0.646
4. CFO (F domain, avail=0.7, usage=0.12) → 0.42 + 0.21 + 0.012 = 0.642
5. Venture Capitalist (F domain, avail=0.8, usage=0.10) → 0.48 + 0.24 + 0.010 = 0.73
6. Healthcare Consultant (H domain, avail=0.6, usage=0.08) → 0.54 + 0.18 + 0.008 = 0.728
7. Marketer (B domain, avail=0.3, usage=0.15) → 0.30 + 0.09 + 0.015 = 0.405
8. Legal Counsel (B domain, avail=0.9, usage=0.09) → 0.54 + 0.27 + 0.009 = 0.819
```

**Ranked:**
```
1. Legal Counsel (0.819) ← Business domain
2. Venture Capitalist (0.73) ← Finance domain
3. Healthcare Consultant (0.728) ← Health domain
4. Founder (0.678) ← Business domain (repeat)
5. Product Manager (0.646)
6. CFO (0.642)
7. CTO (0.614)
8. Marketer (0.405)
```

**Selection (Deep Track = top 6-8, with diversity check):**
```
Initial: [Legal Counsel, Venture Capitalist, Healthcare Consultant, Founder, Product Manager, CFO]

Diversity check: 3 Business, 1 Finance, 1 Health, 1 Finance → Balanced ✓

Result: [Legal Counsel, Venture Capitalist, Healthcare Consultant, Founder, Product Manager, CFO]
(6 specialists, 3 domains represented)
```

---

## ALGORITHM PERFORMANCE

**Expected Accuracy:**
- Domain match: 85-90% (manual review sometimes needed)
- Availability prediction: 95%+ (objective metric)
- User satisfaction: 80%+ (specialists feel relevant)

**Edge Cases Handled:**
- Single specialist available
- All specialists overallocated
- Cross-domain projects
- New projects (no historical usage data)

**Fallback Strategy:**
- If algorithm produces poor selection → User can manually override
- Feedback loop: Poor selections inform future weightings
- Learning: System improves with more project history

---

## CONFIGURATION

These parameters can be adjusted per workflow or user preference:

```yaml
specialist_selection:
  weights:
    domain_match: 0.6
    availability: 0.3
    usage_frequency: 0.1

  selection_counts:
    quick_track: 1-2
    standard_track: 4-6
    deep_track: 6-8

  diversity_threshold: 2  # Minimum different domains

  overallocation_threshold: 1.2  # Warn if > 120% capacity
```

---

## AUDIT & LOGGING

Every specialist selection is logged:
```
timestamp: 2025-02-05T10:30:00Z
idea_id: idea-2025-02-05-fitness
domain_detected: Health
specialists_selected: [Health Coach, Habit Coach]
scores: [0.705, 0.64]
selection_method: auto-algorithm-quick-track
user_override: false
```

This enables:
- Audit trail for selection transparency
- Performance analysis
- Algorithm improvement over time
