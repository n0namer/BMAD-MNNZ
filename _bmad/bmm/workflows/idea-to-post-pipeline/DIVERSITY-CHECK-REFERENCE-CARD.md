# DIVERSITY CHECK - REFERENCE CARD
## One-Page Cheat Sheet

---

## SIMILARITY SCORE FORMULA

```
OVERALL_SIMILARITY = (
    routine_match × 0.20 +
    pain_match × 0.25 +
    secondary_pain_overlap × 0.15 +
    offer_match × 0.20 +
    persona_match × 0.10 +
    angle_match × 0.10
) / 100
```

---

## DECISION TABLE

| Score | Status | Action | Example |
|-------|--------|--------|---------|
| 0-30% | ✅ Unique | POST IT | Different routine, persona, pain, offer |
| 30-55% | ⚠️ Similar | MODIFY | Same pain+offer, different routine+persona |
| 55-75% | ❌ Very Similar | REQUEST CHANGES | Same routine+pain+persona, different offer |
| 75%+ | ❌ DUPLICATE | REJECT | Nearly identical post already exists |

---

## PAIN CATEGORIES (GROUPS)

Use these to calculate `pain_match`:

### SPEED/EFFICIENCY GROUP
- "slow document processing"
- "lengthy decision-making"
- "inefficient workflows"
- "manual bottlenecks"

**Match within group: 85-100%**

### EXPERTISE/KNOWLEDGE GROUP
- "lack team expertise"
- "dependency on key people"
- "knowledge not documented"
- "skill gaps"

**Match within group: 80-95%**

### SCALING GROUP
- "hiring costs too high"
- "can't scale without more people"
- "difficult to add team members"
- "growth constraints"

**Match within group: 85-100%**

### QUALITY/ACCURACY GROUP
- "inconsistent quality"
- "human errors in processing"
- "poor standardization"
- "unreliable results"

**Match within group: 80-90%**

### COST GROUP
- "expensive experts"
- "high payroll costs"
- "budget constraints"
- "fee-based solutions"

**Match within group: 75-85%**

### Between groups: 20-40% match

---

## OFFER TYPES

Pick one per post:

| Offer Type | Description | Price Point | Lead Time | Best For |
|-----------|-------------|------------|-----------|----------|
| **training** | Course, webinar, educational | $99-999 | Low conversion, high volume | Authority building |
| **done-for-you** | Full service delivery | $2,000-10,000 | High conversion, low volume | Revenue growth |
| **templates** | Self-serve tools, frameworks | $29-299 | Med conversion, med volume | Passive income |
| **consulting** | Advisory, 1:1 guidance | $100-500/hr | Med conversion, selective | Brand premium |
| **setup-only** | Partial service, they maintain | $1,000-5,000 | Med conversion, recurring | Hybrid model |

**Monthly requirement: Use at least 3 different types**

---

## NARRATIVE ANGLES (GROUPS)

### SPEED/EFFICIENCY
- "Do it faster"
- "Rapid deployment"
- "Quick turnaround"
- "Time-saving"

### COST
- "Do it cheaper"
- "Budget optimization"
- "ROI improvement"
- "Cost reduction"

### QUALITY
- "Do it better"
- "Accuracy improvement"
- "Consistency"
- "Risk reduction"

### EMPOWERMENT
- "Do it yourself"
- "Self-service"
- "Independence from experts"
- "Democratization"

### SCALING
- "Do it at scale"
- "Parallel processing"
- "Infinite capacity"
- "Growth without hiring"

### SAFETY/RISK
- "Do it safer"
- "Compliance"
- "Risk mitigation"
- "Audit trail"

**Rotation rule: Max 2x per 14 days for same angle**

---

## PERSONAS

Pick one per post:

```
Legal Teams          HR Teams              Small Business Owners
├─ Pain focus:      ├─ Pain focus:       ├─ Pain focus:
│  contracts        │  hiring            │  resource constraints
│  compliance       │  compliance        │  cost + speed
│  risk             │  documentation     │  scalability
│                   │                    │
├─ Offer fit:       ├─ Offer fit:        ├─ Offer fit:
│  document         │  automation        │  templates
│  automation       │  systems           │  training
│  review tools     │  workflows         │  consulting
│                   │                    │
└─ Last posted:     └─ Last posted:      └─ Last posted:
   [DATE]              [DATE]               [DATE]

Entrepreneurs         Marketing Teams      Finance Teams
├─ Pain focus:       ├─ Pain focus:      ├─ Pain focus:
│  growth            │  campaign speed   │  accuracy
│  hiring            │  scaling reach    │  compliance
│  scaling           │  efficiency       │  reporting
│                    │                   │
├─ Offer fit:        ├─ Offer fit:       ├─ Offer fit:
│  done-for-you      │  templates        │  automation
│  consulting        │  training         │  systems
│  setup             │  done-for-you     │  consulting
│                    │                   │
└─ Last posted:      └─ Last posted:     └─ Last posted:
   [DATE]               [DATE]              [DATE]
```

**Rotation rule: Switch every 2-3 posts**

---

## 6 DIVERSITY RULES - QUICK CHECK

```
RULE 1: Routine Frequency
├─ Max 1 per 7 days
├─ Violation: BLOCK
└─ Example: ClaudeFlow on day 1, next ClaudeFlow allowed day 8+

RULE 2: Pain Category Frequency
├─ Max 2 per 30 days per category
├─ Violation: WARN at 2, BLOCK at 3
└─ Example: "Speed" on day 1 & 15, next "speed" blocked until day 31

RULE 3: Offer Type Distribution
├─ Min 3 types per 30 days
├─ Violation: SUGGEST alternatives
└─ Example: After 10 posts, must have used at least 3 offer types

RULE 4: Persona Rotation
├─ Switch every 2-3 posts
├─ Violation: WARN
└─ Example: Legal (1), HR (2), Legal (3) → switch at next post

RULE 5: Angle Freshness
├─ Max 2 per 14 days
├─ Violation: SUGGEST alternatives
└─ Example: "Speed" on day 1 & 7, next "speed" blocked until day 15

RULE 6: Secondary Pain Diversity
├─ New pain every 3 posts
├─ Violation: INFO (can override)
└─ Example: First 3 posts mention "team_dependency", post 4 should mention different pain
```

---

## SIMILARITY CALCULATION - QUICK EXAMPLES

### Example 1: Same Routine, Different Everything Else

```
Candidate:
  routine: ClaudeFlow parallel
  pain: slow documents (SPEED group)
  secondary: [cost_savings]
  offer: templates
  persona: marketing teams
  angle: time-saving

Existing Post:
  routine: ClaudeFlow parallel
  pain: lengthy decisions (SPEED group)
  secondary: [efficiency]
  offer: done-for-you
  persona: legal teams
  angle: speed improvement

SCORES:
  routine: 100% (identical)
  pain: 95% (same group: SPEED)
  secondary: 50% (1/2 match)
  offer: 0% (templates vs done-for-you)
  persona: 0% (marketing vs legal)
  angle: 95% (same group: SPEED)

WEIGHTED = (100×.20 + 95×.25 + 50×.15 + 0×.20 + 0×.10 + 95×.10) / 100
         = (20 + 23.75 + 7.5 + 0 + 0 + 9.5) / 100
         = 60.75%

RESULT: ❌ VERY SIMILAR (55-75%)
ACTION: Request modifications
SUGGESTION: Change persona to "HR teams" or pain to "cost" category
```

### Example 2: Different Routine, Similar Pain

```
Candidate:
  routine: BMAD documentation
  pain: no_documentation
  secondary: [team_dependency]
  offer: training
  persona: small_business
  angle: empowerment

Existing Post:
  routine: ClaudeFlow parallel
  pain: no_standardization
  secondary: [team_dependency]
  offer: training
  persona: small_business
  angle: empowerment

SCORES:
  routine: 0% (completely different)
  pain: 40% (different categories - SPEED vs EXPERTISE)
  secondary: 100% (same secondary pain)
  offer: 100% (both training)
  persona: 100% (both small_business)
  angle: 100% (both empowerment)

WEIGHTED = (0×.20 + 40×.25 + 100×.15 + 100×.20 + 100×.10 + 100×.10) / 100
         = (0 + 10 + 15 + 20 + 10 + 10) / 100
         = 65%

RESULT: ❌ VERY SIMILAR (55-75%)
ACTION: Request modifications
SUGGESTION: Change offer to "templates" or angle to "quality" or persona to "HR teams"
```

### Example 3: Completely Different

```
Candidate:
  routine: Agent role selection
  pain: high_costs
  secondary: [hiring, time_waste]
  offer: templates
  persona: entrepreneurs
  angle: cost reduction

Existing Post:
  routine: ClaudeFlow parallel
  pain: slow_documents
  secondary: [team_dependency]
  offer: done-for-you
  persona: legal_teams
  angle: time-saving

SCORES:
  routine: 0% (different)
  pain: 25% (different categories - COST vs SPEED)
  secondary: 0% (completely different)
  offer: 30% (templates vs done-for-you)
  persona: 0% (entrepreneurs vs legal)
  angle: 15% (cost vs speed)

WEIGHTED = (0×.20 + 25×.25 + 0×.15 + 30×.20 + 0×.10 + 15×.10) / 100
         = (0 + 6.25 + 0 + 6 + 0 + 1.5) / 100
         = 13.75%

RESULT: ✅ UNIQUE (0-30%)
ACTION: APPROVE
```

---

## WORKFLOW GATE LOCATION

```
Your workflow:
┌──────────────────────┐
│ 1. Show routine      │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ 2. Find pain points  │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ 3. Match to offer    │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ 4. Generate variants │
└──────────┬───────────┘
           ↓
┌──────────────────────┐  ← INSERT HERE
│ ⭐ DIVERSITY CHECK   │
├──────────────────────┤
│ • Calc similarity    │
│ • Check 6 rules      │
│ • Get approval       │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ 5. Finalize text     │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ 6. Post to Telegram  │
└──────────────────────┘
```

---

## MONTHLY REVIEW CHECKLIST

```
Every 30 days, calculate:

[ ] Diversity Score
    = (unique_routines/8 + unique_pain_cats/7 + unique_personas/8) / 3
    Target: 70%+

[ ] Offer Type Distribution
    Count: training_posts | done-for-you_posts | template_posts
    Minimum each: 2+ posts
    If any missing: PLAN to add it next week

[ ] Persona Coverage
    List personas used last 30 days
    Unused personas: PLAN to reach next
    Max frequency: Any persona >3 posts? Flag as overused

[ ] Engagement by Dimension
    Top engagement by routine?
    Top engagement by pain?
    Top engagement by offer?
    Top engagement by persona?
    → Use this to guide next 10 posts

[ ] Rule Violations
    Count how many times you hit warnings/blocks
    Should be <5% of posts
    If higher: Review your template choices
```

---

## TROUBLESHOOTING

### "Score shows 72% - Similar but Not Blocked"

You're in the ⚠️ WARN zone (55-75%).

**What to change:**
1. **Easiest:** Switch `target_persona` (0% match → instant difference)
2. **Medium:** Change `primary_pain` to different category
3. **Medium:** Use different `offer_type`
4. **Hardest:** Use completely different `routine`

**Try #1 first - takes 5 seconds.**

---

### "I Keep Getting Blocked on Same Routine"

You're hitting Rule 1 (max 1x per 7 days).

**Options:**
1. **Wait** - Post different routine for 3 days, retry original
2. **Swap personas** - Same routine, different target_persona
3. **Swap angle** - Same routine, different angle

**Example:**
```
Day 1: ClaudeFlow → Legal → Speed
Day 2: ClaudeFlow → HR → Quality ← Different persona=different post
Day 3: BMAD demo → Legal → Speed
Day 4: ClaudeFlow → Marketing → Cost ← Different persona+pain
```

All are different targets, so ClaudeFlow can repeat.

---

### "My Offer Type is Imbalanced"

You posted 10 times: 6 training, 3 done-for-you, 0 templates.

**Fix for next 5 posts:**
```
Post 11: Use "templates" ✅
Post 12: Use "consulting" ✅
Post 13: Use "setup-only" ✅
Posts 14-15: Your choice
```

After this, you'll have 6+3+3 distribution (balanced).

---

## COPY-PASTE FORM

Before posting, fill this out:

```
DIVERSITY CHECK PRE-POST FORM

Date: _______________

[ ] Routine: __________________________
[ ] Primary Pain: __________________________
[ ] Secondary Pains: __________, __________, __________
[ ] Offer Type: __________________________
[ ] Target Persona: __________________________
[ ] Narrative Angle: __________________________

Last similar post in database:
  Routine match: ___% (Days ago: ___)
  Pain match: ___% (Days ago: ___)
  Persona match: ___% (Days ago: ___)

OVERALL SIMILARITY: ___% → Status: [ ] ✅ POST [ ] ⚠️ MODIFY [ ] ❌ REJECT

If modifying:
  Suggested change 1: ______________________________
  Suggested change 2: ______________________________
  Suggested change 3: ______________________________

User approval: [ ] APPROVED [ ] DENIED
```

---

## METRICS TO WATCH

```
Weekly:
  ✓ Avg similarity score (target: <40%)
  ✓ Rule violations (target: 0)
  ✓ Posts needing modifications (target: <20%)

Monthly:
  ✓ Diversity score (target: 70%+)
  ✓ Engagement by routine
  ✓ Conversion by offer type
  ✓ Click-through rate by persona
  ✓ Engagement by angle

Quarterly:
  ✓ Best-performing routine
  ✓ Best-performing pain point
  ✓ Best-performing offer type
  ✓ Best-performing persona
  ✓ Emerging patterns
```

---

**Print this and keep it next to your posting workflow.**

