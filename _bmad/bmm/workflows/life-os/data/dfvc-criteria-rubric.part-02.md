- Historical velocity data (if team has prior projects)
- Critical path analysis

**Example Anchors**:
- Score 3: Enterprise ERP system (12+ months)
- Score 6: Mobile app with backend API (4 months)
- Score 9: Landing page + email signup (2 weeks)

---

#### 2.3 Resource Availability
**What it measures**: Team, budget, tools, and infrastructure readiness

**Scoring Scale (1-10):**
- **1-2**: Missing critical resources, no budget, need to hire/acquire
- **3-4**: Partial resources, tight budget, some gaps (50-70% ready)
- **5-6**: Most resources available, adequate budget, minor gaps (70-85% ready)
- **7-8**: Full team available, good budget, all tools ready (85-95% ready)
- **9-10**: Abundant resources, flexible budget, no blockers (95-100% ready)

**Evidence Required**:
- Team availability calendar (% allocation)
- Budget breakdown (actual vs. required)
- Tooling and infrastructure audit

**Example Anchors**:
- Score 2: Need to hire 3 specialized engineers, $0 budget
- Score 6: Team available 60%, $20K budget (need $30K), cloud infra ready
- Score 10: Dedicated team 100%, $100K budget approved, full stack ready

---

#### 2.4 Dependencies
**What it measures**: External blockers (APIs, partnerships, approvals, regulations)

**Scoring Scale (1-10):**
- **1-2**: Many hard dependencies with unknown timelines (high blocker risk)
- **3-4**: Several dependencies, some controllable, some external
- **5-6**: Few dependencies, mostly internal control
- **7-8**: Minor dependencies, clear mitigation paths
- **9-10**: No external dependencies, full autonomy

**Evidence Required**:
- Dependency map (internal vs. external, critical vs. optional)
- Risk assessment for each dependency (probability of delay)
- Contingency plans

**Example Anchors**:
- Score 2: Requires FDA approval + partnership with 3 hospitals (18+ months)
- Score 6: Depends on public API (stable) + 1 internal team approval (2 weeks)
- Score 10: Standalone project, no external integrations

---

### Feasibility Aggregation Formula

```
F_score = (Technical_Complexity × 0.30) + (Time_to_MVP × 0.25) + (Resource_Availability × 0.30) + (Dependencies × 0.15)
```

**Rationale for Weights**:
- **Technical Complexity (30%)**: Can we actually build this with our skills?
- **Resource Availability (30%)**: Do we have people, money, tools?
- **Time to MVP (25%)**: Speed matters for learning and iteration
- **Dependencies (15%)**: External blockers are painful but often mitigable

**Sphere-Specific Weight Adjustments**:

| Sphere | Technical Complexity | Time to MVP | Resource Availability | Dependencies | Rationale |
|--------|----------------------|-------------|-----------------------|--------------|-----------|
| **Business** | 0.25 | 0.30 | 0.30 | 0.15 | Speed to market critical |
| **Finance** | 0.35 | 0.20 | 0.25 | 0.20 | Quant complexity higher, regulatory dependencies |
| **Personal** | 0.30 | 0.35 | 0.25 | 0.10 | Learning tolerance higher, time constraints matter |
| **Product** | 0.30 | 0.25 | 0.30 | 0.15 | Standard weights |
| **Health** | 0.25 | 0.20 | 0.30 | 0.25 | Regulatory dependencies significant |
| **Creative** | 0.40 | 0.30 | 0.20 | 0.10 | Skill mastery matters most |
| **Social Impact** | 0.20 | 0.25 | 0.40 | 0.15 | Resource scarcity common |

---

## 3. Viability (V) - Can We Sustain It?

### Definition
Evaluates financial sustainability, unit economics, and long-term profitability.

### Sub-Criteria

#### 3.1 Unit Economics (CLV/CAC Ratio)
**What it measures**: Customer lifetime value vs. customer acquisition cost

**Scoring Scale (1-10):**
- **1-2**: CLV/CAC <1.5 (unprofitable, unsustainable)
- **3-4**: CLV/CAC 1.5-2.0 (marginal, high risk)
- **5-6**: CLV/CAC 2.0-3.0 (viable, industry standard)
- **7-8**: CLV/CAC 3.0-5.0 (healthy, good economics)
- **9-10**: CLV/CAC >5.0 (exceptional, highly profitable)

**Evidence Required**:
- CLV calculation (revenue per customer × retention period)
- CAC calculation (marketing + sales costs / new customers)
- Cohort analysis (retention curves by acquisition channel)

**Example Anchors**:
- Score 2: SaaS with $30 MRR, 6-month retention, $40 CAC → CLV/CAC = 1.5
- Score 6: E-commerce with $200 avg order, 3 purchases/year, $30 CAC → CLV/CAC = 2.5
- Score 10: B2B software $10K ACV, 5-year retention, $5K CAC → CLV/CAC = 10

---

#### 3.2 Gross Margin
**What it measures**: Revenue minus cost of goods sold (COGS) as percentage

**Scoring Scale (1-10):**
- **1-2**: <20% margin (commoditized, low profitability)
- **3-4**: 20-40% margin (competitive pressure)
- **5-6**: 40-60% margin (healthy, sustainable)
- **7-8**: 60-80% margin (strong, scalable)
- **9-10**: >80% margin (software-like economics)

**Evidence Required**:
- COGS breakdown (direct costs per unit/customer)
- Revenue per unit/customer
- Margin trend analysis (improving vs. declining)

**Example Anchors**:
- Score 2: Hardware retail (15% margin after shipping, inventory)
- Score 6: Managed services (50% margin, labor-intensive)
- Score 10: SaaS product (90% margin, mostly fixed costs)

---

#### 3.3 Payback Period
**What it measures**: Months to recover customer acquisition cost

**Scoring Scale (1-10):**
- **1-2**: >36 months (very long, high risk)
- **3-4**: 24-36 months (long, requires patient capital)
- **5-6**: 12-24 months (industry standard)
- **7-8**: 6-12 months (fast, healthy)
- **9-10**: <6 months (exceptional, capital efficient)

**Evidence Required**:
- CAC calculation (per channel if applicable)
- Monthly gross margin per customer
- Payback period = CAC / (Monthly Gross Margin)

**Example Anchors**:
- Score 3: Enterprise sales, $50K CAC, $1.5K/month margin → 33 months
- Score 6: SMB SaaS, $500 CAC, $30/month margin → 17 months
- Score 9: Self-serve product, $20 CAC, $5/month margin → 4 months

---

#### 3.4 Operational Leverage (Scalability)
**What it measures**: How costs scale with growth (linear vs. exponential revenue)

**Scoring Scale (1-10):**
- **1-2**: Linear scaling (add 1 customer = add 1 unit cost, no leverage)
- **3-4**: Sub-linear (some efficiencies, but costs grow significantly)
- **5-6**: Moderate leverage (costs grow slower than revenue, 60-70% incremental margin)
- **7-8**: High leverage (costs nearly flat, 80-90% incremental margin)
- **9-10**: Exponential leverage (network effects, marginal cost near zero)

**Evidence Required**:
- Cost structure analysis (fixed vs. variable)
- Unit economics at scale (current vs. 10x customers)
- Bottleneck identification (where does linear scaling break?)

**Example Anchors**:
- Score 2: Consulting (revenue scales linearly with headcount)
- Score 6: SaaS with customer success team (some variable costs)
- Score 10: Marketplace with network effects (each user attracts more users)

---

### Viability Aggregation Formula

```
V_score = (Unit_Economics × 0.35) + (Gross_Margin × 0.25) + (Payback_Period × 0.20) + (Operational_Leverage × 0.20)
```
