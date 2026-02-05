# Portfolio Alignment & Scoring

## Strategic Bucket Classification

Use {strategicBucketsRef} to classify project into one of:
- **Core Business** - Direct revenue/customer impact
- **Innovation** - Experimentation and new capabilities
- **Infrastructure** - Foundational systems and tooling
- **Operations** - Maintenance and optimization

## Portfolio Health Assessment

### Health Indicators

**🟢 Healthy Portfolio:**
- Balanced allocation across buckets
- WIP ≤ 3 projects
- Clear priorities and dependencies
- Adequate capacity per project

**🟡 Needs Attention:**
- Slight imbalance in allocation
- WIP = 3 (at limit)
- Some priority conflicts
- Tight capacity constraints

**🔴 Unhealthy Portfolio:**
- Heavy concentration in one bucket
- WIP > 3
- Many priority conflicts
- Insufficient capacity

### Allocation Targets

| Bucket | Target % | Min % | Max % |
|--------|----------|-------|-------|
| Core Business | 40-50% | 30% | 60% |
| Innovation | 20-30% | 10% | 40% |
| Infrastructure | 15-25% | 10% | 30% |
| Operations | 10-20% | 5% | 25% |

## Integration Pattern Selection Criteria

| Pattern | Use When | Avoid When |
|---------|----------|------------|
| **Standalone** | Independent goals, no dependencies | Duplicates existing capability |
| **Platform Extension** | Builds on proven foundation | Platform not stable |
| **Bundle** | Related projects, shared timeline | Projects can succeed independently |
| **Enabler** | Unblocks multiple initiatives | Single-use infrastructure |
