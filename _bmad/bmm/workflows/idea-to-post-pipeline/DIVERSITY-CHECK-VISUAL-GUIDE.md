# DIVERSITY CHECK - VISUAL GUIDE
## Illustrated Examples and Decision Trees

---

## VISUAL 1: SIMILARITY SCORING BREAKDOWN

```
CANDIDATE POST:
┌─────────────────────────────────────────────────────────┐
│ Routine: ClaudeFlow parallel processing                │
│ Primary Pain: Slow document processing                 │
│ Secondary: [team_dependency, high_costs]               │
│ Offer: Templates                                       │
│ Persona: Marketing teams                               │
│ Angle: Time-saving                                     │
└─────────────────────────────────────────────────────────┘
                        ↓
          COMPARE TO EXISTING POSTS
                        ↓
┌─────────────────────────────────────────────────────────┐
│ POST 1 (from 3 days ago)                               │
├─────────────────────────────────────────────────────────┤
│ Routine: ClaudeFlow parallel    ← SAME = 100%          │
│ Pain: Slow documents            ← SAME = 100%          │
│ Secondary: [team_dependency]    ← OVERLAP = 50%        │
│ Offer: Done-for-you             ← DIFFERENT = 0%       │
│ Persona: Legal teams            ← DIFFERENT = 0%       │
│ Angle: Time-saving              ← SAME = 100%          │
├─────────────────────────────────────────────────────────┤
│ WEIGHTED SCORE:                                        │
│ = (100×0.20 + 100×0.25 + 50×0.15 + 0×0.20 + 0×0.10 + 100×0.10) / 100
│ = (20 + 25 + 7.5 + 0 + 0 + 10) / 100                   │
│ = 62.5%  →  ⚠️ SIMILAR (55-75%)                        │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ POST 2 (from 5 days ago)                               │
├─────────────────────────────────────────────────────────┤
│ Routine: BMAD generation        ← DIFFERENT = 0%       │
│ Pain: No documentation          ← DIFFERENT = 0%       │
│ Secondary: [scaling]            ← DIFFERENT = 0%       │
│ Offer: Training                 ← DIFFERENT = 30%      │
│ Persona: Small business         ← DIFFERENT = 0%       │
│ Angle: Empowerment              ← DIFFERENT = 15%      │
├─────────────────────────────────────────────────────────┤
│ WEIGHTED SCORE:                                        │
│ = (0 + 0 + 0 + 30×0.20 + 0 + 15×0.10) / 100            │
│ = 7.5%  →  ✅ UNIQUE (0-30%)                           │
└─────────────────────────────────────────────────────────┘
```

---

## VISUAL 2: DECISION FLOW TREE

```
                    START: Generate Post
                            ↓
                ┌───────────────────────┐
                │ Enter Post Parameters │
                │ (routine, pain, etc.) │
                └───────────┬───────────┘
                            ↓
                ┌───────────────────────┐
                │ Load last 30 posts    │
                │ from database         │
                └───────────┬───────────┘
                            ↓
                ┌───────────────────────┐
                │ Calculate similarity  │
                │ score to each         │
                └───────────┬───────────┘
                            ↓
                    ┌─── Is max >75%? ───┐
                    │                    │
                   YES                   NO
                    ↓                    ↓
            ┌────────────────┐  ┌──────────────────┐
            │ ❌ BLOCK       │  │ Is max >55%?     │
            │ Duplicate      │  └────────┬─────────┘
            │ detected       │          /        \
            └────────────────┘       YES          NO
                    ↓               ↓              ↓
              REJECT POST      ┌────────────────┐ ┌────────────────┐
                               │ ⚠️  WARN       │ │ ✅ APPROVE     │
                               │ Similar post   │ │ Unique post    │
                               │ detected       │ └────────┬───────┘
                               │ Check Rules    │         │
                               │ 1-6            │         ↓
                               └────────┬───────┘   ┌─────────────┐
                                        ↓          │ Check Rules │
                               ┌──────────────────┐│ 1-6 anyway  │
                               │ Any rules fail?  │└──────┬──────┘
                               └────────┬─────────┘      ↓
                                      /  \          All pass?
                                    YES  NO            /    \
                                     ↓    ↓         YES      NO
                                   WARN  APPROVE    ↓        ↓
                                                 APPROVE   WARN
                                        ↓
                                  POST TO TELEGRAM
```

---

## VISUAL 3: PAIN CATEGORY SIMILARITY MATRIX

```
                  SPEED    EXPERTISE  SCALING  QUALITY   COST
                  ────────────────────────────────────────────
        SPEED     100%      20%       25%      30%      35%
                  ▓▓▓▓▓▓▓▓▓▓
    EXPERTISE      20%      85%       15%      20%      25%
                           ▓▓▓▓▓▓▓▓▓
    SCALING        25%      15%       90%      20%      30%
                                     ▓▓▓▓▓▓▓▓▓
    QUALITY        30%      20%       20%      85%      25%
                                              ▓▓▓▓▓▓▓▓▓
    COST           35%      25%       30%      25%      80%
                                                       ▓▓▓▓▓▓▓▓

KEY:
  Same category (dark): 80-100% match
  Different category: 15-40% match
  Close categories: 40-50% match

IMPLICATION:
  If you use "slow documents" (SPEED) and existing post used
  "inconsistent quality" (QUALITY), they're different angles.
  Similarity = ~30% on pain dimension
```

---

## VISUAL 4: OFFER TYPE VARIETY TRACKING

```
MONTH OF JANUARY (10 posts)

Offer Type Distribution:
┌──────────────────┬───────┬───────────┐
│ Offer Type       │Count │ Percentage│
├──────────────────┼───────┼───────────┤
│ Training         │  6    │ 60%  ▓▓▓▓▓▓│
│ Done-for-you     │  3    │ 30%  ▓▓▓  │
│ Templates        │  1    │ 10%  ▓    │
│ Consulting       │  0    │  0%       │
│ Setup-only       │  0    │  0%       │
└──────────────────┴───────┴───────────┘

VERDICT: ❌ POOR VARIETY (only 2 types used)
         Need minimum 3 types

ACTION FOR FEBRUARY:
  Posts 1: Training ✓ (continue)
  Posts 2-4: Templates (build up)
  Posts 5-7: Done-for-you (maintain)
  Posts 8-9: Consulting (add new)
  Post 10: Training or new type

TARGET DISTRIBUTION:
┌──────────────────┬───────┬───────────┐
│ Training         │  3    │ 30%  ▓▓▓  │
│ Done-for-you     │  3    │ 30%  ▓▓▓  │
│ Templates        │  2    │ 20%  ▓▓   │
│ Consulting       │  1    │ 10%  ▓    │
│ Setup-only       │  1    │ 10%  ▓    │
└──────────────────┴───────┴───────────┘
```

---

## VISUAL 5: PERSONA ROTATION PATTERN

```
GOOD ROTATION:
┌────────────────────────────────────────────────────────┐
│ Post 1: Legal    Post 2: HR       Post 3: Marketing   │
│ ├────┤           ├────┤            ├────┤             │
│ Day 1           Day 3            Day 5               │
│                                                       │
│ Post 4: Legal    Post 5: Finance  Post 6: Entrepreneurs
│ ├────┤           ├────┤            ├────┤            │
│ Day 8           Day 10           Day 12              │
└────────────────────────────────────────────────────────┘
✅ Different persona every 2-3 days
✅ Reaching different decision-makers
✅ Each persona gets fresh angle


BAD ROTATION:
┌────────────────────────────────────────────────────────┐
│ Post 1: Legal    Post 2: Legal    Post 3: Legal      │
│ ├────┤           ├────┤            ├────┤            │
│ Day 1           Day 2            Day 3              │
│                                                       │
│ Post 4: Legal    Post 5: Legal    Post 6: Marketing  │
│ ├────┤           ├────┤            ├────┤            │
│ Day 4           Day 5            Day 6              │
└────────────────────────────────────────────────────────┘
❌ Same persona 5 posts in a row
❌ Audience fatigue (same message)
❌ Other personas never see your content
```

---

## VISUAL 6: ANGLE FRESHNESS CHECK

```
LAST 14 DAYS OF POSTS:

Day 1:  Angle: Time-saving      ⏱️
Day 2:  Angle: Cost-reduction   💰
Day 3:  Angle: Quality          ✓
Day 4:  Angle: Empowerment      🦸
Day 5:  Angle: Time-saving      ⏱️  ← Second use of Time-saving
Day 6:  Angle: Scaling          📈
Day 7:  Angle: Risk-mitigation  🛡️
Day 8:  Angle: Time-saving      ⏱️  ← THIRD USE - ❌ BLOCKED
        └─ Violates Rule 5: Max 2x per 14 days

SOLUTION FOR DAY 8:
├─ Use different angle:
│  ├─ Cost-reduction? ✓ OK (last used day 2, >5 days)
│  ├─ Quality? ❌ (just used day 3)
│  ├─ Independence? ✓ OK (new angle)
│  └─ Scaling? ❌ (just used day 6)
│
└─ Current day 8 post: Change to Cost-reduction or Independence

NEW 14-DAY DISTRIBUTION:
  Time-saving: 2x ✓ (meets rule)
  Cost-reduction: 2x ✓
  Quality: 1x ✓
  Empowerment: 1x ✓
  Scaling: 1x ✓
  Risk-mitigation: 1x ✓
  Independence: 1x ✓
  ───────────────
  Total: 9 posts, 7 unique angles (88% diversity)
```

---

## VISUAL 7: SECONDARY PAIN DIVERSITY

```
LAST 5 POSTS:

Post 1: Primary pain = Slow documents
        Secondary = [team_dependency, high_costs]

Post 2: Primary pain = No documentation
        Secondary = [team_dependency, scaling_issues]

Post 3: Primary pain = Lack expertise
        Secondary = [team_dependency, quality_issues]

Post 4: Primary pain = High costs
        Secondary = [team_dependency, hiring_issues]

Post 5: Primary pain = Scaling bottleneck
        Secondary = [team_dependency, time_waste]

PATTERN DETECTED:
  ❌ "team_dependency" appears in ALL 5 posts
  ❌ Low diversity in secondary pains

UNIQUE SECONDARY PAINS USED:
  team_dependency: 5/5 posts (100%) - OVERUSED
  high_costs: 1/5 posts
  scaling_issues: 1/5 posts
  quality_issues: 1/5 posts
  hiring_issues: 1/5 posts
  time_waste: 1/5 posts

RECOMMENDATION:
  For Post 6+, introduce NEW secondary pains:
  ├─ Process bottlenecks
  ├─ Regulatory compliance
  ├─ Knowledge silos
  ├─ Audit trail gaps
  └─ Vendor management issues

POST 6 EXAMPLE:
  Primary: Inconsistent quality
  Secondary: [knowledge_silos, audit_gaps] ← NEW pains
  ✅ This increases diversity
```

---

## VISUAL 8: MONTHLY DIVERSITY SCORE CALCULATION

```
TARGET CALCULATION (last 30 days):

Step 1: Count UNIQUE ROUTINES
────────────────────────────────────────
  Used: ClaudeFlow (3x), BMAD (4x), Agents (2x), Manual (1x)
  Unique routines: 4
  Possible routines: 8
  Score: 4/8 = 50%

Step 2: Count UNIQUE PAIN CATEGORIES
────────────────────────────────────────
  Used: SPEED (4x), EXPERTISE (3x), QUALITY (2x), SCALING (1x)
  Unique categories: 4
  Possible categories: 7
  Score: 4/7 = 57%

Step 3: Count UNIQUE PERSONAS
────────────────────────────────────────
  Used: Legal (3x), HR (2x), Small business (2x), Marketing (2x), Finance (1x)
  Unique personas: 5
  Possible personas: 8
  Score: 5/8 = 63%

DIVERSITY SCORE = (50% + 57% + 63%) / 3 = 57%

TARGET: 70%

GAP: 13 points

HOW TO CLOSE THE GAP (next month):
├─ Routines: Need to use 6/8 (add 2 new routines)
├─ Pain categories: Need 5/7 (add 1 new pain category)
└─ Personas: Need 6/8 (add 1 new persona)

ACTION PLAN FOR NEXT MONTH:
  ✅ Introduce 2 new routines (Operations audit, Workflow mapping)
  ✅ Introduce 1 new pain (Regulatory compliance)
  ✅ Introduce 1 new persona (Operations managers)
  ✅ Keep using high-performing combinations
```

---

## VISUAL 9: RULE VIOLATION TIMELINE

```
RULE VIOLATION LOG (10 posts over 2 weeks)

Day 1: Post A (ClaudeFlow)
       ✅ All rules pass → POSTED

Day 2: Post B (ClaudeFlow)
       ⚠️  Rule 1 Warning: Same routine as day 1
           (only 1 day apart, need 7 days)
           But different angle + persona → Allow with warning
       → POSTED WITH WARNING

Day 3: Post C (BMAD)
       ✅ All rules pass (different routine)
       → POSTED

Day 4: Post D (ClaudeFlow again)
       ❌ Rule 1 BLOCKED: Third ClaudeFlow post
           Last ClaudeFlow was day 2 (only 2 days ago)
       ❌ Rule 2 WARNING: Speed pain 3x in 4 days
       → REJECTED

Day 5: Post D (modified - BMAD instead)
       ✅ All rules pass
       → POSTED

Day 6: Post E (Agent roles)
       ✅ All rules pass
       → POSTED

Day 7: Post F (ClaudeFlow)
       ⚠️  Rule 4 WARNING: Personas have been Legal, Legal, HR, Small bus, Marketing
           Next ClaudeFlow can target Finance or Entrepreneurs (underused)
       → POSTED (with persona swap to Finance)

STATISTICS:
  Posts submitted: 10
  Posts approved: 8 (80%)
  Posts with warnings: 1 (10%)
  Posts rejected: 1 (10%)
  Modifications requested: 1

VERDICT: ✅ Good system health
         - Few rejections (shows good planning)
         - Some warnings (shows awareness of limits)
         - High approval rate (flexible enough to work)
```

---

## VISUAL 10: ENGAGEMENT TRACKING BY DIMENSION

```
30 DAYS OF POSTS - WHAT PERFORMS BEST?

BY ROUTINE:
  ClaudeFlow: 4.2% avg engagement ⭐⭐⭐⭐
  BMAD: 3.8% avg engagement ⭐⭐⭐
  Agent roles: 4.5% avg engagement ⭐⭐⭐⭐⭐
  Manual process: 2.1% avg engagement ⭐⭐

BY PRIMARY PAIN:
  Speed: 3.2% avg engagement ⭐⭐⭐
  Expertise: 4.1% avg engagement ⭐⭐⭐⭐
  Scaling: 4.8% avg engagement ⭐⭐⭐⭐⭐
  Quality: 3.5% avg engagement ⭐⭐⭐
  Cost: 2.9% avg engagement ⭐⭐

BY OFFER TYPE:
  Training: 3.3% avg engagement ⭐⭐⭐
  Done-for-you: 4.6% avg engagement ⭐⭐⭐⭐⭐
  Templates: 2.8% avg engagement ⭐⭐
  Consulting: 4.2% avg engagement ⭐⭐⭐⭐

BY PERSONA:
  Legal: 3.4% avg engagement ⭐⭐⭐
  HR: 3.9% avg engagement ⭐⭐⭐⭐
  Small business: 4.7% avg engagement ⭐⭐⭐⭐⭐
  Entrepreneurs: 4.1% avg engagement ⭐⭐⭐⭐
  Marketing: 2.6% avg engagement ⭐⭐

BY ANGLE:
  Time-saving: 3.2% avg engagement ⭐⭐⭐
  Cost-reduction: 3.8% avg engagement ⭐⭐⭐⭐
  Quality: 4.1% avg engagement ⭐⭐⭐⭐
  Empowerment: 4.5% avg engagement ⭐⭐⭐⭐⭐
  Scaling: 4.9% avg engagement ⭐⭐⭐⭐⭐

INSIGHTS FOR NEXT MONTH:
  ✅ Keep using: Agent roles, Scaling pain, Done-for-you, Small business, Empowerment angle
  ⚠️  Reduce: Manual process, Cost pain, Templates, Marketing personas
  📈 Experiment more: Combine top performers (Agent roles + Scaling + Small business + Empowerment)
```

---

## VISUAL 11: MODIFICATION DECISION TREE

```
                     Similarity > 55%?
                         YES ↓

            ┌──────────────────────────────┐
            │ What makes it similar?       │
            └──────────────┬───────────────┘
                           ↓
        ┌──────────────────┬──────────────────┐
        │                  │                  │
    Routine?          Pain point?          Persona?
        │                  │                  │
        ↓                  ↓                  ↓
   ┌────────┐      ┌────────────┐      ┌────────────┐
   │ Change │      │ Change to  │      │ Change to  │
   │ routine│      │ different  │      │ underused  │
   │        │      │ category   │      │ persona    │
   │ OR     │      │ (e.g.,     │      │ (e.g.,     │
   │ wait   │      │ Cost if    │      │ Finance if │
   │ 7 days │      │ Speed)     │      │ always     │
   └────────┘      │ OR modify  │      │ legal)     │
                   │ secondary  │      │ OR         │
                   │ pains      │      │ change     │
                   └────────────┘      │ angle      │
                                       └────────────┘

   ┌──────────────────────────────────────────────┐
   │ After modification, recalculate similarity   │
   └──────────────┬───────────────────────────────┘
                  ↓
        Is new score < 55%?
           /              \
         YES              NO
          ↓                ↓
    ✅ APPROVE      Try different modification
                     (e.g., if pain didn't help,
                      try offer type instead)
```

---

## VISUAL 12: QUICK SIMILARITY ESTIMATION

```
QUICK MENTAL MATH (Before running calculator):

SAME ROUTINE + SAME PAIN:
  ├─ Same persona? → 90%+ (almost duplicate)
  ├─ Different persona? → 70-80% (very similar)
  └─ Different offer? → 60-70% (similar)

SAME ROUTINE + DIFFERENT PAIN (different category):
  ├─ Same persona, same offer? → 60-70% (similar)
  ├─ Different persona? → 40-50% (moderately different)
  └─ Different offer + persona? → 30-40% (mostly different)

DIFFERENT ROUTINE + SAME PAIN:
  ├─ Same persona, same offer? → 65-75% (similar)
  ├─ Different persona OR offer? → 45-55% (borderline)
  └─ Different everything else? → 25-35% (mostly unique)

DIFFERENT ROUTINE + DIFFERENT PAIN + DIFFERENT PERSONA:
  ├─ Same offer type? → 30-40% (mostly different)
  ├─ Different offer? → 15-25% (quite unique)
  └─ Different angle too? → <15% (very unique)

QUICK RULE OF THUMB:
  Each different dimension:
    ├─ Routine: -20 points
    ├─ Pain: -25 points
    ├─ Persona: -10 points
    ├─ Offer: -20 points
    └─ Angle: -10 points

  Start at 100% similarity
  Subtract points for each difference
  Result = rough estimate
```

---

**These visuals help internalize the system. Print and reference them!**

