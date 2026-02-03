### Step 05: Integration (Portfolio Decision)
- Use CLV/CAC ratio to prioritize among multiple ideas
- Allocate resources based on unit economics strength

---

## 9. Common Pitfalls

### 1. Ignoring Churn
**Mistake**: Assuming 0% churn or using revenue without accounting for retention
**Fix**: Use realistic churn estimates (5-10% monthly for early SaaS)

### 2. Underestimating CAC
**Mistake**: Only counting ad spend, ignoring salaries, tools, overhead
**Fix**: Include ALL sales & marketing costs in CAC calculation

### 3. Overestimating CLV
**Mistake**: Using infinite horizon without discounting or using too-low churn
**Fix**: Use conservative churn estimates, finite horizon calculations

### 4. Not Segmenting
**Mistake**: One CLV/CAC for all customer types
**Fix**: Calculate separately for SMB vs Enterprise, organic vs paid

### 5. Using Gross Revenue Instead of Gross Margin
**Mistake**: CLV = ARPU × Lifespan (forgetting to subtract COGS)
**Fix**: Always multiply by gross margin % first

---

## 10. Excel/Sheets Template

```
| Input Variables              | Value    | Units        |
|------------------------------|----------|--------------|
| ARPU                         | $50      | per month    |
| Gross Margin %               | 80%      |              |
| Monthly Churn Rate           | 5%       |              |
| Total S&M Costs (monthly)    | $10,000  |              |
| New Customers (monthly)      | 50       |              |

| Calculated Metrics           | Formula                          | Result   |
|------------------------------|----------------------------------|----------|
| Average Lifespan (months)    | = 1 / Churn Rate                 | 20       |
| CLV                          | = ARPU × Margin × Lifespan       | $800     |
| CAC                          | = S&M Costs / New Customers      | $200     |
| CLV/CAC Ratio                | = CLV / CAC                      | 4.0      |
| Monthly Gross Profit         | = ARPU × Margin                  | $40      |
| Payback Period (months)      | = CAC / Monthly Gross Profit     | 5        |

| Validation Checks            | Threshold    | Status       |
|------------------------------|--------------|--------------|
| Gross Margin ≥ 60%           | 60%          | ✅ PASS (80%) |
| Monthly Churn ≤ 10%          | 10%          | ✅ PASS (5%)  |
| CLV/CAC Ratio ≥ 3.0          | 3.0          | ✅ PASS (4.0) |
| Payback Period ≤ 12 months   | 12 months    | ✅ PASS (5)   |
| CLV > $500                   | $500         | ✅ PASS ($800)|

| Decision                     | Result       |
|------------------------------|--------------|
| All checks passed            | ✅ PROCEED   |
```

---

## 11. References & Resources

### Books
- "The SaaS Metrics Bible" - David Skok (Bessemer Venture Partners)
- "Scaling Lean" - Ash Maurya

### Articles
- [SaaS Metrics 2.0](https://www.forentrepreneurs.com/saas-metrics-2/) - David Skok
- [Unit Economics](https://a16z.com/2015/09/23/unit-economics/) - Andreessen Horowitz

### Tools
- [SaaS Calculator](https://www.forentrepreneurs.com/saas-metrics-2-saas-calculator/) - Free Excel template
- ProfitWell - Automated metrics tracking
- ChartMogul - MRR and churn analytics

---

## Summary

**Unit economics are the foundation of business viability**. Before proceeding past Step 02 (Evaluation), you MUST validate:

1. ✅ **CLV/CAC Ratio ≥ 3.0** (ideally 4-5x)
2. ✅ **Payback Period ≤ 12 months** (ideally <6 months)
3. ✅ **Gross Margin ≥ 60%** (ideally 75%+)
4. ✅ **Monthly Churn ≤ 10%** (ideally <5%)

If these checks fail, iterate on pricing, positioning, or business model before building the product.

**Next Step**: MCDA Methodology (data/mcda-methodology.md) for multi-criteria scoring and prioritization.
