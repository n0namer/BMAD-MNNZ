# Real Options Analysis Guide

**Status:** GAP 7 - Medium Priority
**Domain:** Strategic Decision-Making
**Integration:** Life-OS Decision Framework

---

## 1. Real Options Theory Overview

### What Are Real Options?

Real options are **the right, but not the obligation, to take action in the future**. They provide a systematic framework for managing uncertainty by deferring commitments until better information becomes available.

**Core Insight (Dixit & Pindyck):**
Instead of deciding "now or never," real options let you decide "now, later, or conditional on new information." This framework explicitly values waiting and learning.

### Financial Analogy

| Concept | Financial Option | Real Option |
|---------|-----------------|-----------|
| **Strike Price** | Price to buy stock | Cost to execute action |
| **Underlying Asset** | Stock value | Project cash flows |
| **Expiration** | Fixed date | Condition/deadline |
| **Holder's Right** | Buy/sell stock | Expand/defer/abandon |
| **Value** | Option premium | Strategic flexibility value |

**Key Difference:** Real options often have **no expiration** (perpetual), making them MORE valuable than finite financial options.

### Why Real Options Matter

**Traditional NPV Problem:**
- Net Present Value assumes "now or never"
- Ignores value of waiting for information
- Treats decision as binary (yes/no)
- Undervalues strategic flexibility

**Real Options Solution:**
- ✅ Captures value of waiting
- ✅ Handles irreversible investments properly
- ✅ Values sequence of decisions
- ✅ Incorporates uncertainty as advantage

---

## 2. Types of Real Options

### Option to Defer

**Definition:** Right to postpone action until uncertainty resolves.

**When Valuable:**
- High initial investment with declining irreversibility
- New information coming soon (market test, technology update)
- Waiting cost < deferral benefit
- No first-mover advantage needed

**Example - Product Launch:**
```
Scenario A (No Option):
- Invest $100K immediately in full product
- Market could reject → sunk loss

Scenario B (Defer Option):
- Spend $2K on landing page test (2 weeks)
- Get 100+ signups? → Proceed with full development
- Get <10 signups? → Abandon, lose only $2K
```

**Calculation:**
```
Deferral Value = NPV(information received) - NPV(without information)
                + Cost of Waiting (lost revenue, opportunity cost)
```

### Option to Expand

**Definition:** Right to increase scale/scope if project succeeds.

**When Valuable:**
- Success provides pathway to larger opportunity
- Limited capacity initially (test market)
- Expansion cost lower if foundation exists
- Success probability updatable with initial data

**Example - Geographic Expansion:**
```
Phase 1: Launch in single city ($100K)
  → Success signals strong market fit

Phase 2 Option: Expand to 10 cities ($500K)
  → Only viable if Phase 1 succeeds
  → Expansion cost < start-from-scratch in new market
```

**Calculation:**
```
Expansion Option Value = PV(scale-up payoff | success) × P(success)
                        - PV(expansion cost)
```

### Option to Contract

**Definition:** Right to reduce scale if project underperforms.

**When Valuable:**
- High initial investment but flexible cost structure
- Market slower to develop than expected
- Can scale back incrementally
- Salvage value available for underutilized assets

**Example - Capacity Investment:**
```
Build production line with 40% excess capacity ($500K total)

Scenario A (High demand):
- Utilize full capacity
- High margin per unit

Scenario B (Low demand):
- Contract to 60% capacity
- Reduce operating costs
- Only 20% excess dies as sunk cost
```

**Calculation:**
```
Contraction Option Value = Savings from scaling back
                          - Penalty from underutilization
```

### Option to Abandon

**Definition:** Right to exit and salvage value if project fails.

**When Valuable:**
- Large sunk costs with some salvage value
- High failure probability
- Early signals available
- Time-limited opportunity (deadline)

**Example - R&D Project:**
```
Full R&D Program: $10M over 3 years
Key Milestones:
  Month 6: Technical feasibility test → $500K salvage if abandoned
  Month 12: Market validation → $2M salvage if abandoned
  Month 24: Final decision → Full commitment or abandon

If milestone fails → Exit, salvage remaining assets
If milestone succeeds → Continue
```

**Calculation:**
```
Abandonment Option Value = Salvage Value × P(need to exit)
                          + Cost saved by exiting early
```

### Option to Switch

**Definition:** Right to pivot between alternative approaches.

**When Valuable:**
- Multiple viable paths exist
- Uncertainty about which path succeeds
- Can gather information on multiple paths
- Switching cost manageable

**Example - Platform Choice:**
```
Strategy A: Build on AWS
  - Higher upfront cost
  - Better for scale

Strategy B: Build on Heroku
  - Lower upfront cost
  - Easier to learn

Option: Start on Heroku
