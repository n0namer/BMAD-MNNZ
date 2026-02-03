# Unit Economics Calculator

**Purpose**: Calculate and validate the fundamental economic viability of a product idea through Customer Lifetime Value (CLV), Customer Acquisition Cost (CAC), and key ratios.

**When to Use**: Step 02 (Evaluation) - Economic Viability Assessment

---

## Overview

Unit economics determine whether a business model is fundamentally profitable at the individual customer level. This calculator provides formulas and validation thresholds for:

1. **Customer Lifetime Value (CLV)** - Total revenue expected from a customer
2. **Customer Acquisition Cost (CAC)** - Cost to acquire one customer
3. **CLV/CAC Ratio** - Efficiency of customer acquisition
4. **Payback Period** - Time to recover acquisition costs

---

## 1. Customer Lifetime Value (CLV)

### Formula

```
CLV = (ARPU × Gross Margin %) × (1 / Churn Rate)
```

**Where**:
- **ARPU** = Average Revenue Per User (monthly or annual)
- **Gross Margin %** = (Revenue - COGS) / Revenue
- **Churn Rate** = % of customers lost per period (monthly or annual)

### Alternative Formula (Finite Horizon)

```
CLV = (ARPU × Gross Margin %) × Average Customer Lifespan
```

**Average Customer Lifespan** = 1 / Churn Rate (in months or years)

### Example Calculation

**Scenario**: SaaS product with monthly subscription

```
ARPU = $50/month
Gross Margin = 80% (after hosting, support, payment processing)
Monthly Churn Rate = 5% (annual churn ~60%)

CLV = ($50 × 0.80) × (1 / 0.05)
CLV = $40 × 20 months
CLV = $800
```

### Validation Thresholds

| Metric | Minimum | Good | Excellent |
|--------|---------|------|-----------|
| **Gross Margin** | 60% | 75%+ | 85%+ |
| **Monthly Churn** | <10% | <5% | <3% |
| **Average Lifespan** | 10+ months | 20+ months | 36+ months |

---

## 2. Customer Acquisition Cost (CAC)

### Formula

```
CAC = (Total Sales & Marketing Costs) / (Number of New Customers Acquired)
```

**Total Sales & Marketing Costs Include**:
- Advertising spend (Google Ads, Facebook, LinkedIn, etc.)
- Content marketing costs (blog, SEO, videos)
- Sales team salaries and commissions
- Marketing tools and software (CRM, email, analytics)
- Events, partnerships, PR
- Overhead allocated to S&M

### Time Period

Calculate CAC over a consistent period (monthly, quarterly, or annually) matching your CLV calculation.

### Example Calculation

**Scenario**: Early-stage SaaS startup (monthly)

```
Total S&M Costs = $10,000/month
  - Ad spend: $5,000
  - Content marketing: $2,000
  - Marketing tools: $1,500
  - Sales salaries (allocated): $1,500

New Customers Acquired = 50

CAC = $10,000 / 50
CAC = $200
```

### Validation Thresholds

| Stage | CAC Target | Notes |
|-------|------------|-------|
| **MVP/Early** | <$100 | Mostly organic, low-cost channels |
| **Growth** | $100-$500 | Scaling paid channels, optimizing |
| **Mature** | $200-$1,000+ | Established channels, brand awareness |

**Critical**: CAC should be ≤ 1/3 of CLV (CLV/CAC ratio ≥ 3)

---

## 3. CLV/CAC Ratio

### Formula

```
CLV/CAC Ratio = CLV / CAC
```

### Interpretation

| Ratio | Meaning | Action |
|-------|---------|--------|
| **<1** | Losing money on every customer | 🔴 STOP - Business model broken |
| **1-3** | Marginal unit economics | 🟡 OPTIMIZE - Reduce CAC or increase CLV |
| **3-5** | Healthy business model | 🟢 SCALE - Good to proceed |
| **>5** | Excellent unit economics | 🟢 AGGRESSIVE SCALE - Rare, invest heavily |

### Example Validation

Using previous examples:
```
CLV = $800
CAC = $200

CLV/CAC = $800 / $200 = 4.0
```

**Result**: 🟢 **HEALTHY** - Meets 3x threshold, good to scale

### Industry Benchmarks

| Business Type | Target Ratio | Notes |
|---------------|--------------|-------|
| **SaaS (B2B)** | 3-5x | Higher is better, 5x+ is exceptional |
| **SaaS (B2C)** | 3-4x | Lower margins, higher churn |
| **E-commerce** | 2-4x | Depends on repeat purchase rate |
| **Marketplace** | 4-6x | Network effects improve over time |
| **Enterprise** | 5-10x+ | Long sales cycles, high retention |

---

## 4. Payback Period

### Formula

```
Payback Period (months) = CAC / (ARPU × Gross Margin %)
```

### Interpretation

The number of months required to recover the cost of acquiring a customer through their monthly gross profit contribution.

### Example Calculation

```
CAC = $200
ARPU = $50/month
Gross Margin = 80%

Payback Period = $200 / ($50 × 0.80)
Payback Period = $200 / $40
Payback Period = 5 months
```

### Validation Thresholds

