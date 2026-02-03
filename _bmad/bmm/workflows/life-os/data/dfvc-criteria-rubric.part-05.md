| **Willingness to Pay** | 8 | Traders willing to pay 20% profit share (high WTP for proven alpha) |
| **Competitive Advantage** | 6 | 3x faster execution vs. manual, but HFT firms have 10x+ advantage (noticeable, not transformative) |

**Calculation**:
```
D_score (Finance weights) = (6 × 0.15) + (7 × 0.30) + (8 × 0.40) + (6 × 0.15)
                           = 0.90 + 2.10 + 3.20 + 0.90
                           = 7.10 / 10
```

---

#### Feasibility (F) Scoring (Finance Weights)

| Sub-Criterion | Score | Justification |
|---------------|-------|---------------|
| **Technical Complexity** | 4 | Complex (async programming, WebSocket APIs, risk management algorithms, 3-4 months learning) |
| **Time to MVP** | 6 | 4 months to working bot with paper trading validation (moderate timeline) |
| **Resource Availability** | 5 | Solo developer, $10K budget for exchange fees and hosting (adequate but tight) |
| **Dependencies** | 6 | Depends on 5 exchange APIs (some downtime risk), KYC/compliance in some regions |

**Calculation**:
```
F_score (Finance weights) = (4 × 0.35) + (6 × 0.20) + (5 × 0.25) + (6 × 0.20)
                           = 1.40 + 1.20 + 1.25 + 1.20
                           = 5.05 / 10
```

---

#### Viability (V) Scoring (Finance Weights)

| Sub-Criterion | Score | Justification |
|---------------|-------|---------------|
| **Unit Economics** | 9 | CLV = $5K/month profit × 24 months = $120K; CAC = $2K (time investment); CLV/CAC = 60 (exceptional) |
| **Gross Margin** | 7 | Profit per trade: 0.3% × $10K volume = $30; Costs: $2 exchange fees = 93% margin (high, but not 80%+ SaaS) |
| **Payback Period** | 9 | $2K investment / $5K monthly profit = 0.4 months (~2 weeks, exceptional) |
| **Operational Leverage** | 8 | Highly automated (once built, marginal cost near zero), but requires monitoring |

**Calculation**:
```
V_score (Finance weights) = (9 × 0.40) + (7 × 0.30) + (9 × 0.20) + (8 × 0.10)
                           = 3.60 + 2.10 + 1.80 + 0.80
                           = 8.30 / 10
```

---

#### Competition (C) Scoring (Finance Weights)

| Sub-Criterion | Score | Justification |
|---------------|-------|---------------|
| **Five Forces** | 4 | Crowded (many bots), low barriers (APIs public), high rivalry, substitute strategies exist |
| **Barriers to Entry** | 3 | Weak moat (code can be replicated, no IP); speed advantage requires capital (HFT) |
| **Threat of Substitutes** | 4 | Many alternatives (other arbitrage bots, market making, directional trading) |
| **Market Timing** | 6 | Moderate timing (crypto volatility creates opportunities, but arbitrage margins compressing) |

**Calculation**:
```
C_score (Finance weights) = (4 × 0.30) + (3 × 0.25) + (4 × 0.25) + (6 × 0.20)
                           = 1.20 + 0.75 + 1.00 + 1.20
                           = 4.15 / 10
```

---

#### Total Score (Finance Weights)

```
Total_Score = (D × 0.25) + (F × 0.20) + (V × 0.35) + (C × 0.20)
            = (7.10 × 0.25) + (5.05 × 0.20) + (8.30 × 0.35) + (4.15 × 0.20)
            = 1.78 + 1.01 + 2.91 + 0.83
            = 6.53 / 10
```

**Interpretation**: **SOLID PROJECT with RISKS** - Excellent viability (high ROI), good desirability (proven alpha), but moderate feasibility (technical complexity) and weak competition (many players). Recommend: Proceed if technical skills exist, focus on niche pairs or geographic arbitrage to differentiate.

---

### Example 3: Personal Project - Learning Piano

**Context**: Adult learner wants to achieve Grade 5 piano proficiency (ABRSM) in 18 months. No prior musical training. Goals: play favorite classical pieces, personal fulfillment.

---

#### Desirability (D) Scoring (Personal Weights)

| Sub-Criterion | Score | Justification |
|---------------|-------|---------------|
| **Market Size** | 1 | Irrelevant (personal project, no market) |
| **Need Intensity** | 9 | High intrinsic motivation (childhood dream, deep joy from music); daily desire |
| **Willingness to Pay** | 6 | $50/month lessons + $2K piano (moderate WTP, manageable) |
| **Competitive Advantage** | 8 | Unique personal achievement (no "competitors", just self vs. prior self); 5x+ skill gain |

**Calculation**:
```
D_score (Personal weights) = (1 × 0.05) + (9 × 0.50) + (6 × 0.10) + (8 × 0.35)
                            = 0.05 + 4.50 + 0.60 + 2.80
                            = 7.95 / 10
```

---

#### Feasibility (F) Scoring (Personal Weights)

| Sub-Criterion | Score | Justification |
|---------------|-------|---------------|
| **Technical Complexity** | 5 | Moderate (requires muscle memory, sight-reading, coordination; 6-12 months to Grade 5) |
| **Time to MVP** | 7 | 3 months to play first simple piece (fast initial progress, long mastery curve) |
| **Resource Availability** | 8 | Teacher available, piano purchased, 1 hour/day practice time allocated (most resources ready) |
| **Dependencies** | 9 | No external dependencies (teacher optional, self-paced) |

**Calculation**:
```
F_score (Personal weights) = (5 × 0.30) + (7 × 0.35) + (8 × 0.25) + (9 × 0.10)
                            = 1.50 + 2.45 + 2.00 + 0.90
                            = 6.85 / 10
```

---

#### Viability (V) Scoring (Personal Weights)

| Sub-Criterion | Score | Justification |
|---------------|-------|---------------|
| **Unit Economics** | 7 | "CLV" = lifetime joy; "CAC" = time investment; sustainable if 1 hour/day manageable |
| **Gross Margin** | 6 | "Margin" = time ROI (joy per hour); moderate (practice can feel tedious initially) |
| **Payback Period** | 8 | "Payback" = 3 months to first rewarding piece (fast emotional ROI) |
| **Operational Leverage** | 9 | High leverage (skills compound; Grade 5 unlocks 80% of classical repertoire) |

**Calculation**:
```
V_score (Personal weights) = (7 × 0.20) + (6 × 0.15) + (8 × 0.30) + (9 × 0.35)
                            = 1.40 + 0.90 + 2.40 + 3.15
                            = 7.85 / 10
```

---

#### Competition (C) Scoring (Personal Weights)

| Sub-Criterion | Score | Justification |
|---------------|-------|---------------|
| **Five Forces** | 9 | No competition (personal journey, not marketplace) |
| **Barriers to Entry** | 7 | Moderate "moat" (once learned, skill retained; switching cost = starting over) |
| **Threat of Substitutes** | 6 | Some substitutes (guitar, digital music production), but piano uniquely satisfying |
| **Market Timing** | 8 | Good timing (online lessons abundant, affordable digital pianos, AI practice tools emerging) |

**Calculation**:
```
C_score (Personal weights) = (9 × 0.10) + (7 × 0.15) + (6 × 0.35) + (8 × 0.40)
                            = 0.90 + 1.05 + 2.10 + 3.20
                            = 7.25 / 10
```

---

#### Total Score (Personal Weights)

```
Total_Score = (D × 0.40) + (F × 0.25) + (V × 0.15) + (C × 0.20)
            = (7.95 × 0.40) + (6.85 × 0.25) + (7.85 × 0.15) + (7.25 × 0.20)
            = 3.18 + 1.71 + 1.18 + 1.45
            = 7.52 / 10
```

**Interpretation**: **EXCELLENT PERSONAL PROJECT** - Very high desirability (intrinsic joy), good feasibility (resources available), strong viability (sustainable practice), and favorable "competition" (unique achievement). Recommend: Proceed with structured practice plan, track milestones (Grade 1 → 2 → 3 → 5), celebrate progress.

---

## 7. Decision Matrix & Thresholds

### Priority Bands (0-10 Scale)

| Score Range | Priority | Action | Typical Characteristics |
|-------------|----------|--------|-------------------------|
| **8.0-10.0** | **Critical** | Execute immediately | High desirability + viability, manageable feasibility, favorable competition |
| **6.5-7.9** | **High** | Plan execution within 1-2 months | Solid across dimensions, some risks identified |
| **5.0-6.4** | **Medium** | Further analysis needed | Mixed signals (e.g., high D/V but low F/C) |
| **3.0-4.9** | **Low** | Deprioritize or pivot | Significant gaps in 2+ dimensions |
