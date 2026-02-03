## 5. Option Value Calculation (Simplified)

### Black-Scholes for Real Options (Simplified)

**Traditional Black-Scholes Formula:**
```
C = S × N(d1) - K × e^(-rT) × N(d2)

Where:
- C = Option value
- S = Current spot price (present value of payoff)
- K = Strike price (cost to exercise)
- r = Risk-free rate
- T = Time to expiration
- N(d1), N(d2) = Normal distribution functions
```

**In Real Options Language:**
```
Option Value = PV(Payoff if Succeed) × N(d1)
             - Cost to Execute × e^(-rT) × N(d2)

Where:
- PV(Payoff) = Expected cash flows if project succeeds
- Cost = Investment required to execute option
- r = Discount rate (opportunity cost of capital)
- T = Time until decision point
- N(d1), N(d2) ≈ Probability of exercise + time value
```

### Simplified Practical Calculation

**Step 1: Define Payoff Tree**

```
Project: Launch new product

Best Case (20% probability):
  Revenue Year 1: $500K
  Revenue Year 2: $1.5M
  Revenue Year 3: $2.5M
  Total NPV: $3M

Base Case (60% probability):
  Revenue Year 1: $200K
  Revenue Year 2: $600K
  Revenue Year 3: $900K
  Total NPV: $1M

Worst Case (20% probability):
  Revenue Year 1: $50K
  Revenue Year 2: $50K
  Revenue Year 3: $0K
  Total NPV: $0 (kill project, salvage equipment for $50K)
```

**Step 2: Calculate Expected NPV**

```
E[NPV] = 0.2 × $3M + 0.6 × $1M + 0.2 × $50K
       = $600K + $600K + $10K
       = $1.21M

Traditional Decision:
- If cost < $1.21M → Commit now
- If cost > $1.21M → Don't commit
```

**Step 3: Calculate Option Value (Deferral)**

Defer 6 months, run experiment (cost $50K):
```
After Experiment Probability Update:
- If success signal → High case now 60% likely
- If failure signal → Low case now 80% likely

E[NPV | success signal] = 0.6 × $3M + 0.4 × $1M = $2.2M
E[NPV | failure signal] = 0.2 × $3M + 0.8 × $0 = $0.6M

Expected Update Value:
= 0.4 × $2.2M + 0.6 × $0.6M  [Example: 40% chance success]
= $0.88M + $0.36M
= $1.24M

Deferral Value:
= E[NPV | after info] - E[NPV | now] + Cost Paid
= $1.24M - $1.21M + $50K
= $0.04M (marginal, close call)
```

**Step 4: Decision Rule**

```
Deferral Value > 0?
  → Wait for information ($50K investment)
  → Kill/expand based on results

Deferral Value < 0?
  → Commit now (cost of waiting > value of info)
  → Accept current risk
```

### Real Options Value Framework

| Option Type | Value Formula | When Largest |
|------------|---------------|--------------|
| **Deferral** | E[NPV\|info] - E[NPV\|now] | High uncertainty, long timeline |
| **Expansion** | E[Upside\|success] - Expand Cost | Sequential payoff, asymmetric |
| **Contraction** | Cost Savings from exit | High fixed costs, variable demand |
| **Abandonment** | Salvage Value × P(fail) | High sunk cost, salvage available |
| **Switching** | PV(correct path) - Switch cost | Multiple viable paths |

---

## 6. Workflow Integration Points

### Life-OS Decision Framework Integration

**Stage 0 - Opportunity Identification:**
- ✅ Assess: "Is this high-uncertainty opportunity?"
- ✅ Decision: Real options framework? Or traditional analysis?
- ✅ Output: Decision type (deferral, expand, contract, abandon, switch)

**Stage 1 - Cheap Experiments Phase:**
- ✅ Design experiments to test riskiest assumptions
- ✅ Execute Level 1 experiments (validation tests)
- ✅ Update probability based on results
- ✅ Gate: Pass-fail to continue

**Stage 2 - Progressive Commitment:**
- ✅ Execute Level 2-3 experiments (prototypes, MVPs)
- ✅ Refine option value calculation
- ✅ Decide: Expand option, pivot, or kill
- ✅ Gate: Major investment decision

**Stage 3 - Scaling/Full Commitment:**
- ✅ Execute Level 4-5 (pilot, full scale)
- ✅ Optimize unit economics
- ✅ Scale or sunset based on performance
- ✅ Gate: Growth/profitability verification

### Decision Gates Template

```markdown
## Gate Criteria

### Pre-Gate 1 (Assumption Validation)
- [ ] 3+ landing page tests with >15% conversion
- [ ] 10+ interviews confirming problem
- [ ] Competitive analysis completed
- [ ] GO/KILL decision made

### Pre-Gate 2 (Solution Validation)
- [ ] Manual service test with 3 paying customers
- [ ] >60% retention after 30 days
- [ ] NPS >5 on small sample
- [ ] Pivot or proceed decision made

### Gate 3 (Pilot Readiness)
- [ ] Concierge MVP tested with 5-10 customers
- [ ] Core workflow validated
- [ ] Onboarding success >80%
- [ ] Unit economics target: CAC < 12-month LTV
- [ ] Ready for 50-100 customer pilot

### Gate 4 (Scale Readiness)
- [ ] Pilot with 50+ customers, 3+ months
- [ ] Churn <5% monthly
- [ ] NPS >40 (B2B) or >50 (B2C)
- [ ] Unit economics positive and repeatable
- [ ] Ready for full go-to-market
```

---

## 7. Detailed Examples

### Example 1: SaaS Product Launch

**Scenario:** Build a project management tool for freelancers
