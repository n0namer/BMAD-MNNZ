# D/F/V/C Criteria Rubric - Project Prioritization Framework

## Overview

The D/F/V/C framework provides a systematic approach to evaluate and prioritize projects across four critical dimensions:
- **D**esirability - Market pull and customer need
- **F**easibility - Technical and execution capability
- **V**iability - Financial sustainability and economics
- **C**ompetition - Market positioning and competitive advantage

Each dimension contains multiple sub-criteria scored 1-10, with sphere-specific weights to reflect different priorities across Business, Finance, Personal, and other project domains.

---

## 1. Desirability (D) - Market Pull

### Definition
Measures the strength of market demand, customer need intensity, and willingness to pay for the solution.

### Sub-Criteria

#### 1.1 Market Size (TAM/SAM/SOM)
**What it measures**: Total addressable market and reachable customer base

**Scoring Scale (1-10):**
- **1-2**: Niche market <$100K TAM, <100 potential customers
- **3-4**: Small market $100K-$1M TAM, 100-1K customers
- **5-6**: Medium market $1M-$10M TAM, 1K-10K customers
- **7-8**: Large market $10M-$100M TAM, 10K-100K customers
- **9-10**: Massive market >$100M TAM, >100K customers

**Evidence Required**:
- Market research data (Gartner, IDC, industry reports)
- Customer surveys or interviews
- Competitor customer base analysis

**Example Anchors**:
- Score 3: Local coffee shop loyalty app (500 customers)
- Score 7: Regional B2B SaaS for logistics (15K potential companies)
- Score 10: Global consumer fintech app (500M potential users)

---

#### 1.2 Customer Need Intensity (Pain × Frequency)
**What it measures**: How painful the problem is and how often customers experience it

**Scoring Scale (1-10):**
- **1-3**: Nice-to-have (low pain, infrequent)
  - Score 1: Mild annoyance, yearly occurrence
  - Score 3: Minor inconvenience, monthly occurrence
- **4-7**: Important (moderate pain, regular)
  - Score 4: Noticeable problem, weekly occurrence
  - Score 6: Significant pain, daily occurrence
- **8-10**: Critical (severe pain, constant)
  - Score 8: Major blocker, multiple times daily
  - Score 10: Business-critical, continuous pain

**Evidence Required**:
- Customer problem interviews (quantify pain: 1-10 scale)
- Support ticket volume and severity
- Current workaround complexity

**Example Anchors**:
- Score 2: Email signature generator (nice-to-have, set once)
- Score 6: Expense tracking for freelancers (important, daily task)
- Score 9: Hospital ICU patient monitoring (critical, 24/7 need)

---

#### 1.3 Willingness to Pay (WTP)
**What it measures**: Price sensitivity and perceived value by customers

**Scoring Scale (1-10):**
- **1-2**: Won't pay, expects free solution
- **3-4**: Low WTP, <$10/month or <$50 one-time
- **5-6**: Moderate WTP, $10-$50/month or $50-$500 one-time
- **7-8**: High WTP, $50-$200/month or $500-$5K one-time
- **9-10**: Premium WTP, >$200/month or >$5K one-time, price insensitive

**Evidence Required**:
- Price sensitivity surveys (Van Westendorp analysis)
- Competitor pricing benchmarks
- Customer budget allocation data

**Example Anchors**:
- Score 2: Ad-supported mobile game (free, ad tolerance)
- Score 6: Project management SaaS ($30/user/month)
- Score 10: Enterprise compliance software ($100K/year contracts)

---

#### 1.4 Competitive Advantage (Differentiation)
**What it measures**: How much better the solution is vs. alternatives (10x rule)

**Scoring Scale (1-10):**
- **1-2**: Commodity, no differentiation, parity with alternatives
- **3-4**: Marginal improvement, 1.2x-1.5x better on key dimension
- **5-6**: Noticeable advantage, 2x-3x better on core feature
- **7-8**: Strong differentiation, 5x-10x better on critical metric
- **9-10**: Transformative, 10x+ better, creates new category

**Evidence Required**:
- Feature comparison matrix vs. top 3 competitors
- Customer satisfaction delta (NPS/CSAT vs. alternatives)
- Unique value proposition validation

**Example Anchors**:
- Score 2: Generic CRM with standard features
- Score 6: Accounting software 3x faster data entry via AI OCR
- Score 10: First-to-market blockchain solution for supply chain (new category)

---

### Desirability Aggregation Formula

```
D_score = (Market_Size × 0.20) + (Need_Intensity × 0.40) + (WTP × 0.25) + (Competitive_Advantage × 0.15)
```

**Rationale for Weights**:
- **Need Intensity (40%)**: Highest weight - customers must actually care about the problem
- **WTP (25%)**: Strong signal of value perception
- **Market Size (20%)**: Important but not sufficient alone (large market of disinterested users = bad)
- **Competitive Advantage (15%)**: Differentiation matters, but solving real pain matters more

**Sphere-Specific Weight Adjustments**:

| Sphere | Market Size | Need Intensity | WTP | Competitive Advantage | Rationale |
|--------|-------------|----------------|-----|-----------------------|-----------|
| **Business** | 0.25 | 0.35 | 0.30 | 0.10 | Market size and monetization critical |
| **Finance** | 0.15 | 0.30 | 0.40 | 0.15 | ROI and pricing power key |
| **Personal** | 0.05 | 0.50 | 0.10 | 0.35 | Joy and uniqueness matter most (market size irrelevant) |
| **Product** | 0.20 | 0.40 | 0.25 | 0.15 | Standard business weights |
| **Health** | 0.10 | 0.60 | 0.20 | 0.10 | Impact on well-being dominates |
| **Creative** | 0.05 | 0.40 | 0.15 | 0.40 | Uniqueness and personal fulfillment key |
| **Social Impact** | 0.30 | 0.50 | 0.05 | 0.15 | Scale of reach and depth of need |

---

## 2. Feasibility (F) - Can We Build It?

### Definition
Assesses technical capability, resource availability, and execution risk.

### Sub-Criteria

#### 2.1 Technical Complexity
**What it measures**: Skills, tools, and technology stack difficulty

**Scoring Scale (1-10):**
- **1-2**: Moonshot - Unknown technologies, R&D required, high technical risk
- **3-4**: Complex - Multiple new technologies, steep learning curve (6+ months)
- **5-6**: Moderate - Some new skills needed, manageable learning (2-3 months)
- **7-8**: Familiar - Mostly known stack, minor new components (2-4 weeks)
- **9-10**: Trivial - Fully understood stack, repetitive work, no new learning

**Evidence Required**:
- Technology stack audit (known vs. unknown)
- Team skills matrix (current vs. required)
- Proof-of-concept results (if applicable)

**Example Anchors**:
- Score 2: Custom blockchain consensus algorithm (R&D phase)
- Score 6: React SPA with new state management library (moderate learning)
- Score 9: CRUD app with familiar Django + PostgreSQL stack

---

#### 2.2 Time to MVP
**What it measures**: Weeks/months to first working version with core features

**Scoring Scale (1-10):**
- **1-2**: >1 year to MVP (long runway, high uncertainty)
- **3-4**: 6-12 months to MVP (multi-quarter project)
- **5-6**: 3-6 months to MVP (single quarter)
- **7-8**: 1-3 months to MVP (fast iteration)
- **9-10**: <1 month to MVP (rapid prototyping)

**Evidence Required**:
- Project plan with milestone breakdown
