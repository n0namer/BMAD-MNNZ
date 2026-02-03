
---

#### Finance Projects (ROI-Focused)
| Dimension | Weight | Rationale |
|-----------|--------|-----------|
| Desirability (D) | 0.25 | Alpha opportunity, but risk-adjusted |
| Feasibility (F) | 0.20 | Quant complexity manageable |
| Viability (V) | 0.35 | Returns and risk metrics dominate |
| Competition (C) | 0.20 | Edge vs. market critical |

**When to use**: Trading systems, investment strategies, portfolio optimization, quantitative research

---

#### Personal Projects (Joy-Focused)
| Dimension | Weight | Rationale |
|-----------|--------|-----------|
| Desirability (D) | 0.40 | Joy, fulfillment, intrinsic motivation |
| Feasibility (F) | 0.25 | Learning tolerance higher |
| Viability (V) | 0.15 | Sustainability (prevent burnout), not profit |
| Competition (C) | 0.20 | Uniqueness matters (not market share) |

**When to use**: Hobbies, skill development, side projects for learning, personal passion projects

---

#### Product Projects (Standard Weights)
| Dimension | Weight | Rationale |
|-----------|--------|-----------|
| Desirability (D) | 0.35 | Customer-centric, problem-solution fit |
| Feasibility (F) | 0.25 | Execution capability key |
| Viability (V) | 0.25 | Economics and sustainability |
| Competition (C) | 0.15 | Differentiation important |

**When to use**: New product launches, feature prioritization, MVP planning

---

#### Health Projects (Impact-Focused)
| Dimension | Weight | Rationale |
|-----------|--------|-----------|
| Desirability (D) | 0.40 | Impact on well-being dominates |
| Feasibility (F) | 0.20 | Execution often constrained by regulations |
| Viability (V) | 0.25 | Sustainability without burnout |
| Competition (C) | 0.15 | Alternatives matter (holistic approach) |

**When to use**: Wellness apps, fitness programs, mental health solutions, nutrition tracking

---

#### Creative Projects (Uniqueness-Focused)
| Dimension | Weight | Rationale |
|-----------|--------|-----------|
| Desirability (D) | 0.30 | Artistic merit and personal fulfillment |
| Feasibility (F) | 0.25 | Skill mastery and learning |
| Viability (V) | 0.20 | Passive income potential |
| Competition (C) | 0.25 | Uniqueness and originality |

**When to use**: Content creation, art projects, music production, creative tools

---

#### Social Impact Projects (Scale + Depth)
| Dimension | Weight | Rationale |
|-----------|--------|-----------|
| Desirability (D) | 0.40 | Depth of need and scale of reach |
| Feasibility (F) | 0.20 | Resource constraints common |
| Viability (V) | 0.25 | Cost efficiency for sustainability |
| Competition (C) | 0.15 | Collaboration often preferred over competition |

**When to use**: Non-profit initiatives, community programs, open-source projects, education platforms

---

## 6. Worked Examples

### Example 1: Business Project - VK Bot for Online Stores

**Context**: Chatbot for VK (VKontakte) to automate customer support for small online stores in Russia. Targets 500K small e-commerce businesses on VK.

---

#### Desirability (D) Scoring

| Sub-Criterion | Score | Justification |
|---------------|-------|---------------|
| **Market Size** | 7 | TAM = 500K stores × $30/month = $15M/month = $180M/year (large market) |
| **Need Intensity** | 6 | Daily pain (customer inquiries), but not business-critical (Score 6: significant pain, daily) |
| **Willingness to Pay** | 6 | $30/month feasible for small stores (moderate WTP, Score 5-6 range) |
| **Competitive Advantage** | 5 | 2x faster response time vs. manual chat, but similar to 3 competitors (marginal advantage) |

**Calculation**:
```
D_score (Business weights) = (7 × 0.25) + (6 × 0.35) + (6 × 0.30) + (5 × 0.10)
                            = 1.75 + 2.10 + 1.80 + 0.50
                            = 6.15 / 10
```

---

#### Feasibility (F) Scoring

| Sub-Criterion | Score | Justification |
|---------------|-------|---------------|
| **Technical Complexity** | 7 | Familiar stack (Python, VK API, OpenAI), 4-week learning curve for VK specifics |
| **Time to MVP** | 8 | 2 months to working chatbot (fast iteration) |
| **Resource Availability** | 6 | 1 developer available 70%, $5K budget (most resources ready, minor gaps) |
| **Dependencies** | 7 | VK API stable (public), minor dependency on OpenAI API (clear mitigation) |

**Calculation**:
```
F_score (Business weights) = (7 × 0.25) + (8 × 0.30) + (6 × 0.30) + (7 × 0.15)
                            = 1.75 + 2.40 + 1.80 + 1.05
                            = 7.00 / 10
```

---

#### Viability (V) Scoring

| Sub-Criterion | Score | Justification |
|---------------|-------|---------------|
| **Unit Economics** | 6 | CLV = $30/month × 18 months retention = $540; CAC = $200 (ads); CLV/CAC = 2.7 (viable) |
| **Gross Margin** | 8 | $30 revenue - $3 hosting - $2 API costs = $25 margin (83% margin, SaaS-like) |
| **Payback Period** | 7 | $200 CAC / $25 monthly margin = 8 months (fast, healthy) |
| **Operational Leverage** | 7 | Mostly automated (80% incremental margin), some customer support needed |

**Calculation**:
```
V_score (Business weights) = (6 × 0.30) + (8 × 0.25) + (7 × 0.25) + (7 × 0.20)
                            = 1.80 + 2.00 + 1.75 + 1.40
                            = 6.95 / 10
```

---

#### Competition (C) Scoring

| Sub-Criterion | Score | Justification |
|---------------|-------|---------------|
| **Five Forces** | 5 | Growing market but 3-5 competitors; moderate barriers (VK integration complexity) |
| **Barriers to Entry** | 4 | Weak moat (VK API public, easy to replicate); minor brand advantage for early movers |
| **Threat of Substitutes** | 5 | Manual chat, generic chatbots, email support (viable substitutes, but less efficient) |
| **Market Timing** | 7 | Good timing (VK introducing business tools, AI chatbots trending in Russia) |

**Calculation**:
```
C_score (Business weights) = (5 × 0.25) + (4 × 0.30) + (5 × 0.25) + (7 × 0.20)
                            = 1.25 + 1.20 + 1.25 + 1.40
                            = 5.10 / 10
```

---

#### Total Score (Business Weights)

```
Total_Score = (D × 0.35) + (F × 0.20) + (V × 0.30) + (C × 0.15)
            = (6.15 × 0.35) + (7.00 × 0.20) + (6.95 × 0.30) + (5.10 × 0.15)
            = 2.15 + 1.40 + 2.09 + 0.77
            = 6.41 / 10
```

**Interpretation**: **GOOD PROJECT** - Strong feasibility and viability, moderate desirability and competition. Recommend: Proceed with MVP, focus on differentiation (unique integrations or industry-specific templates).

---

### Example 2: Finance Project - Crypto Arbitrage Trading Bot

**Context**: Automated trading bot exploiting price differences across 5 crypto exchanges (Binance, Coinbase, Kraken, Bitfinex, Huobi). Targets 0.2-0.5% profit per trade, 20-50 trades/day.

---

#### Desirability (D) Scoring (Finance Weights)

| Sub-Criterion | Score | Justification |
|---------------|-------|---------------|
| **Market Size** | 6 | Addressable: $500M daily volume on targeted pairs (medium-large market) |
| **Need Intensity** | 7 | High pain (manual arbitrage slow, misses opportunities); happens constantly |
