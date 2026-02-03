  → If growth exceeds Heroku limits → Migrate to AWS (switching cost)
  → If slow growth continues → Stick with Heroku
```

**Calculation:**
```
Switching Option Value = PV(correct path if switch) - Switching cost
                        - Cost of initial "wrong" path
```

---

## 3. When to Use Real Options vs Full Commitment

### Decision Matrix

| Factor | Use Real Options | Use Full Commitment |
|--------|-----------------|-------------------|
| **Uncertainty Level** | High | Low |
| **Information Timing** | Available soon | Unlikely to change |
| **Irreversibility** | High investment, hard to reverse | Low sunk costs |
| **Flexibility Cost** | Low option/deferral cost | High flexibility cost |
| **Competition** | Weak (no first-mover advantage) | Strong (winner-take-all) |
| **Early Signals** | Cheap experiments available | Hard to test early |

### Real Options Framework - Decision Tree

```
START: Facing decision with uncertainty

├─ Is uncertainty SIGNIFICANT?
│  ├─ NO → Use traditional NPV analysis (full commit or no commit)
│  └─ YES → Continue
│
├─ Can we learn/test CHEAPLY before committing?
│  ├─ NO → Evaluate full commitment now vs never
│  └─ YES → Continue
│
├─ Is information arriving SOON?
│  ├─ NO (>5 years) → Commit now or never
│  └─ YES (<2 years) → Continue
│
├─ What's the ASYMMETRY?
│  ├─ Large downside (sunk cost), small upside → Use options (defer)
│  └─ Large upside potential, manageable downside → Commit or expand option
│
└─ RECOMMENDATION:
   - Design sequence of cheap experiments → Gather info → Expand/contract → Scale/abandon
   - Use option value to price deferral benefit
   - Commit when value of waiting < cost of waiting
```

### Commitment Scenarios

**Use FULL COMMITMENT When:**
1. **Proven business model** - Market demand validated, unit economics work
2. **First-mover advantage critical** - "Move fast or lose market" (e.g., network effects)
3. **Low uncertainty** - Clear path, few unknowns
4. **Waiting cost > option value** - Cost of deferral exceeds value of learning
5. **Competitive pressure** - Winner-take-all market

**Use REAL OPTIONS When:**
1. **Unproven assumptions** - Core hypotheses not yet validated
2. **High investment** - Large capital required, hard to reverse
3. **Information pending** - Market data, tech maturity, regulatory clarity due soon
4. **Sequential decisions** - Can break into stages with go/kill gates
5. **Cheap experiments** - Can test cheaply before full commitment

---

## 4. Cheap Experiments Methodology

### Design Philosophy

**Core Principle:** Identify your riskiest assumption, design the cheapest test to validate/invalidate it, execute quickly, and update probability.

**Cost Multiplier Framework:**

| Experiment Level | Cost Multiplier | Timeline | Decision |
|-----------------|-----------------|----------|----------|
| **Assumption test** | 1x | 1 week | Kill if false |
| **Prototype** | 5x | 2-4 weeks | Kill if bad UX |
| **Concierge MVP** | 25x | 4-8 weeks | Kill if wrong market |
| **Pilot** | 100x | 2-3 months | Scale or abandon |
| **Full product** | 500x | 6-12 months | Scale or sunset |

**Example: SaaS Product Development**

```
Riskiest Assumption: "People will pay $50/month for this solution"

Experiment Level 1 - Landing Page Test ($500, 1 week)
├─ Create landing page describing solution
├─ Drive traffic (ads, organic)
├─ Measure: Conversion to email signup
└─ Pass: >20% conversion, 100+ signups
   Fail: Abandon project

Experiment Level 2 - Manual Service Test ($2K, 2 weeks)
├─ Offer manual service (you do work, charge $50/month)
├─ Get 3-5 paying customers
├─ Measure: Retention after month 1, willingness to pay
└─ Pass: >60% retention, no churn
   Fail: Wrong market, abort

Experiment Level 3 - Concierge MVP ($15K, 4 weeks)
├─ Semi-automated product (some manual, some automated)
├─ Validate core workflow with 10 customers
├─ Measure: Onboarding success, feature usage, NPS
└─ Pass: >8 NPS, <20% onboarding drop-off
   Fail: Wrong solution, pivot

Experiment Level 4 - Pilot Product ($75K, 3 months)
├─ Fully automated product
├─ Release to 50 customers
├─ Measure: Churn, expansion revenue, unit economics (CAC < 12mo LTV)
└─ Pass: Unit economics positive, <5% monthly churn
   Fail: Not defensible, abort

Experiment Level 5 - Scale ($500K+, 12 months)
├─ Full go-to-market
├─ Enterprise features, sales team
└─ Growth phase
```

### Cheap Experiments Design Template

**For ANY decision, follow this structure:**

```markdown
### Riskiest Assumption
What assumption, if wrong, kills the project?

### Experiment Design
- **Input:** What will you do? (Be specific, time-boxed)
- **Success Criteria:** What counts as "pass"? (Quantified)
- **Failure Criteria:** What counts as "fail"? (Quantified)
- **Cost:** Money and time to run this experiment
- **Timeline:** How long until you have results?

### Probability Update
- **Prior:** What did you think before the experiment?
- **Posterior:** What do you think after?
- **Evidence:** What changed your mind?

### Go/Kill Decision
- If pass → Which option next?
- If fail → Abandon, pivot, or double-down?
```

### Rapid Iteration Loop (2-Week Sprints)

```
Sprint 1-2 (Weeks 1-2):
├─ Riskiest assumption: Do people want this category?
├─ Experiment: Landing page + ads → Track signup rate
├─ Investment: $500-1K time + $500 ads
├─ Decision: Kill, continue, or pivot market

Sprint 3-4 (Weeks 3-4):
├─ Riskiest assumption: Will people actually pay?
├─ Experiment: Manual service delivery to 3 customers
├─ Investment: $2-5K (time + customer acquisition)
├─ Decision: Expand customer base, pivot offer, or kill

Sprint 5-8 (Weeks 5-8):
├─ Riskiest assumption: Can we build sustainable product?
├─ Experiment: Concierge MVP with 5-10 customers
├─ Investment: $10-20K (dev + ops)
├─ Decision: Scale to pilot or kill

Sprint 9-16 (Weeks 9-16):
├─ Riskiest assumption: Can we monetize at scale?
├─ Experiment: Pilot release, 50-100 customers
├─ Investment: $50-100K (team + ops)
├─ Decision: Full commit to growth or sunset
```

---

