# BMAD Methodology Reference Guide
**Purpose:** Explain the BMAD workflow steps used to validate the 7 Life OS ideas

---

## What is BMAD?

**BMAD = Business Model Analysis & Design**

A structured decision-making framework used in the Life OS workflow to evaluate ideas through 8 sequential steps. Each step builds on the previous, ensuring ideas are thoroughly analyzed before execution.

### Key Principle
**Transform vague ideas → Actionable execution plans** by applying diverse perspectives, expert analysis, and systematic decomposition.

---

## The 8 BMAD Steps (Complete Workflow)

### **Step 0: Foundation** ✅
Captures raw idea input and establishes baseline context.

**Inputs:**
- User's initial idea description
- Problem statement
- Motivation and stakeholders

**Outputs:**
- Idea card with metadata
- Clear problem statement
- Success criteria sketch

**Example (Idea-001):**
> "Input: Katana-VectorBT — trading platform for autonomous strategies"
> "Output: SMART goal (≥3 Scaled-Live strategies in 90 days), stakeholder map, resource estimate"

**Tools Used:** None (human input)

---

### **Step 1: Ideation** ✅
Ensures the idea is clearly articulated (not detailed execution planning yet).

**Note:** For this validation, Step 1 is implicit — all 7 ideas already captured clearly.

---

### **Step 2: Roles Discovery** ✅
Identifies ALL stakeholder roles and specialist types needed for the idea to succeed.

**Process:**
1. Map idea to **5 Life OS domains** (Business, Finance, Tech, Creative, Personal)
2. For each domain, identify 2-3 specialist roles needed
3. Score roles by priority (High/Medium/Low)
4. Select 4-6 high-priority roles for Consilium

**Example (Idea-001: Katana-VectorBT):**
| Role | Domain | Priority |
|------|--------|----------|
| Portfolio Manager | Finance | **HIGH** |
| Risk Advisor | Finance | **HIGH** |
| Product Strategist | Business | **HIGH** |
| Quant Developer | Tech | **HIGH** |
| Finance Analyst | Finance | **MEDIUM** |
| Data Engineer | Tech | **MEDIUM** |

**Key Insight:** More roles = more perspectives = better decisions.

---

### **Step 3: Specialist Match** ✅
Maps discovered roles to actual subject matter experts (specialists).

**Process:**
1. For each high-priority role, identify a specialist (real person or archetype)
2. Match expertise to role requirements
3. Document why this specialist is qualified

**Example (Idea-001):**
- **Portfolio Manager role** → matched to real portfolio manager archetype (understands risk, diversification, returns)
- **Risk Advisor role** → matched to risk management expert (understands drawdown, slippage, overfitting)

**Output:** List of 4-6 specialists to consult in Step 4.

---

### **Step 4: Consilium (Expert Panel Analysis)** ✅
**Most critical step.** Gathers multi-disciplinary expert opinions on the idea.

**Format Options:**
- **Quick Mode** (1-2 hours): 3 specialists, brief opinions, rapid synthesis
- **Deep Mode** (4-8 hours): 5-6 specialists, detailed analysis, Six Thinking Hats framework

#### **Six Thinking Hats Method (Deep Mode)**

6 perspectives, each addressing different cognitive style:

| Hat | Perspective | Questions | Expert |
|-----|-------------|-----------|--------|
| **⚪ White Hat** | **Facts & Data** | What data exists? What are the metrics? | Finance/Data specialist |
| **🔴 Red Hat** | **Intuition & Emotion** | Does this *feel* right? What's my gut say? | Founder/Product specialist |
| **⚫ Black Hat** | **Critical (Risks)** | What could go wrong? What's risky? | Risk/Security specialist |
| **🟡 Yellow Hat** | **Optimistic (Benefits)** | What's the upside? Why this works? | Growth/Finance specialist |
| **🟢 Green Hat** | **Creative (Innovation)** | How could we make this better? New ideas? | Innovation/Design specialist |
| **🔵 Blue Hat** | **Process (Control)** | How do we organize this? What's the plan? | Product/Operations specialist |

**Output:**
- 6-page consilium report (one page per hat)
- Consensus recommendation (PROCEED / CONDITIONAL / REJECT)
- Key decisions to make before execution

**Example (Idea-002: Maps Bot):**
- ⚪ White: TAM 2.5M businesses, 80% don't reply, could save 20h/month each
- 🔴 Red: Strong intuition, but fear of API bans is real blocker
- ⚫ Black: API ToS risk (ban potential), moderation complexity, onboarding friction
- 🟡 Yellow: Unit economics great (98% margin), strong GTM fit
- 🟢 Green: Personality AI, smart escalation, browser extension for Zoon
- 🔵 Blue: MVP scope (Yandex + Google only), human review layer

**Consensus:** CONDITIONAL PROCEED (requires human review, MVP scope locked)

---

### **Step 4.5: TRIZ Analysis** (Optional Enhancement) ✅
Resolves contradictions and unlocks breakthrough innovations.

**TRIZ = Theory of Inventive Problem Solving (Russian methodology)**

**Process:**
1. Identify core contradiction in the idea
2. Map to TRIZ contradiction matrix (39 parameters)
3. Apply suggested inventive principles
4. Generate breakthrough solutions

**Example (Idea-002: Maps Bot):**
| Contradiction | Problem | Solution |
|---|---|---|
| Need moderation (quality) vs. need speed (volume) | Manual 100% review = slow; no review = bad quality | Smart Confidence Layer: Auto-approve confident replies (30%), manual-review low-confidence (70%) |
| Need LLM intelligence vs. need low cost | LLM expensive ($0.02-0.10 per reply) | Hybrid LLM Routing: Use regex/templates 94% of time, LLM only for complex cases |
| Need custom Zoon integration vs. API unavailable | Zoon API blocked by ToS | Browser Extension: Extension auto-posts replies without API |

**Output:** 3-5 breakthrough solutions that improve cost/quality/speed.

---

### **Step 5: Scoring & MCDA** ✅
Quantifies idea quality using Multi-Criteria Decision Analysis.

**Process:**
1. Define 8-10 evaluation criteria (domain-specific)
2. Weight criteria by importance (sum to 100%)
3. Score idea on each criteria (1-5 scale)
4. Calculate weighted score: **SUM(score × weight)**

**Example Criteria Matrix:**

| Criteria | Score | Weight | Weighted |
|----------|-------|--------|----------|
| **Impact** (user value, market size) | 5/5 | 25% | 1.25 |
| **Confidence** (feasibility, team skill) | 4/5 | 20% | 0.80 |
| **Effort** (time, resources, complexity) | 2/5 (inverted) | 15% | 0.30 |
| **Strategic Alignment** (Life OS fit) | 5/5 | 20% | 1.00 |
| **Risk** (mitigatable, acceptable) | 3/5 (inverted) | 20% | 0.60 |
| **TOTAL** | — | 100% | **4.0/5.0** |

**Output:**
- Overall score (e.g., 4.2/5.0)
- Priority rating (HIGH / MEDIUM / LOW)
- Decision: PROCEED / CONDITIONAL / REJECT

---

### **Step 6: Integration (Portfolio Fit)** ✅
Assesses how the idea fits into the overall portfolio and resource constraints.

**Checks:**
1. **Strategic Bucket:** Which Life OS domain? (Growth, Revenue, Internal, Learning, Relationships, Health, Wealth)
2. **Portfolio Balance:** Will adding this idea create imbalance?
3. **WIP Management:** Current WIP projects vs. capacity available?
4. **Dependencies:** Does this idea depend on other projects?
5. **BMAD Workflow Selection:** Which workflow to use? (Dev Story, Quick Dev, Product Brief, etc.)

**Example (Idea-001):**
- **Strategic Bucket:** Growth / Innovation (primary), Wealth / Investment (secondary)
- **Portfolio Balance:** ✅ HEALTHY — adds growth without losing other domains
- **WIP Check:** Current WIP = 2 projects, capacity 40% available → ✅ ALLOW
- **BMAD Workflow:** Dev Story (12+ week project with clear phases)

**Example (Idea-006):**
- **Strategic Bucket:** Growth / Revenue Streams
- **Portfolio Balance:** ⚠️ MODERATE RISK — already 57% tech/business projects
- **WIP Check:** Current WIP = 2, but this adds 18 weeks → ⚠️ CONDITIONAL (verify WIP <2 at start)
- **BMAD Workflow:** Product Brief (validate MVP scope) → Dev Story

**Output:**
- Portfolio impact assessment
- WIP decision (ALLOW / CONDITIONAL / DEFER)
- BMAD workflow to use
- Start date

---

### **Step 7: Calendar Sync (Timeline & Capacity)** ✅
Creates realistic timeline, milestones, and capacity allocation.

**Process:**
1. Define start date and end date
2. Break into 3-5 major phases
3. Identify key milestones (gates, deliverables, go/no-go points)
4. Allocate hours per week
5. Map to calendar

**Example (Idea-001: Katana-VectorBT):**

| Phase | Duration | End Date | Milestone | Capacity |
|-------|----------|----------|-----------|----------|
| **1. Data Foundation** | 2 weeks | Feb 20 | Epic L complete (APIs integrated) | 10h/w |
| **2. Innovation Sprint** | 2 weeks | Mar 6 | Ensemble + AutoML evaluated | 10h/w |
| **3. Strategy Validation** | 8 weeks | May 1 | Walk-forward + Monte Carlo complete | 10h/w |
| **4. Paper Trading Gate** | 4 weeks | Jun 5 | Performance ≥80% backtest | 10h/w |
| **5. Live Launch** | 2 weeks | Jun 19 | 2 Scaled-Live strategies ACTIVE | 10h/w |
| **TOTAL** | **120 days** | Jun 19 | **Goal achieved** | **10h/w avg** |

**Output:**
- Calendar with milestone dates
- Weekly capacity allocation
- Dependency chain
- Go/no-go gates

---

### **Step 8: Deep Plan (L1-L6 Decomposition)** ✅
Creates hierarchical breakdown from high-level mission to atomic actions.

**The 6 Levels:**

| Level | Example | Detail |
|-------|---------|--------|
| **L1: Mission** | "Launch 2 profitable Scaled-Live trading strategies in 120 days" | 1 statement, 1 role |
| **L2: Phases** | Data Integration → Innovation → Validation → Paper Trading → Launch | 3-5 major phases |
| **L3: Work Streams** | Price Data Integration, News Calendar API, AutoML Framework, Ensemble Strategy, Walk-Forward Optimization, Paper Trading, Live Launch | 10-15 work streams |
| **L4: Stages** | Research → Design → Development → Testing → Deployment | Typical software stages |
| **L5: Tasks** | "Integrate Alpha Vantage API", "Setup IAM for AWS", "Write Whisper wrapper" | 30-50 tasks |
| **L6: Actions** | "Click API key button", "Copy to .env file", "Test connection" | 100+ atomic steps |

**Quality Gates (Step 8 Validation):**
- ✅ **Depth:** All 6 levels specified?
- ✅ **Breadth:** All L2 nodes have at least 2-3 L3 children?
- ✅ **RACI:** Clear owner (Responsible), approver, consulted, informed?
- ✅ **If-Then:** Contingency plans for 3+ risk scenarios?

**Example (Idea-001 Paper Trading Gate):**
| If | Then | Owner |
|---|---|---|
| IF Paper Trading performance <80% backtest | THEN re-optimize OR extend 2 weeks | Quant Dev |
| IF Data quality issues >5% missing | THEN halt, fix pipeline first | Data Engineer |
| IF Live first month Max DD >15% | THEN pause, investigate, reduce position size | Risk Advisor |
| IF Innovation Sprint Sharpe <1.2x original | THEN rollback to standard approach | Quant Dev |

---

## BMAD Compliance Checklist

For each idea, verify:

- ✅ **Step 0:** Foundation documented (goals, user input, stakeholders)
- ✅ **Step 1:** Idea clearly stated (not vague)
- ✅ **Step 2:** Roles discovered (4+ roles from 2+ domains)
- ✅ **Step 3:** Specialists matched (4+ specialists selected)
- ✅ **Step 4:** Consilium completed (expert panel analysis OR Six Hats)
- ✅ **Step 4.5:** TRIZ applied (contradiction resolution, breakthrough solutions)
- ✅ **Step 5:** MCDA scoring (8+ criteria, weighted, clear score)
- ✅ **Step 6:** Integration assessed (portfolio fit, WIP check, BMAD workflow)
- ✅ **Step 7:** Calendar synced (start date, phases, milestones, capacity)
- ✅ **Step 8:** Deep Plan complete (L1-L6, RACI, if-then gates)

**Passing Score:** ≥80% steps complete + <2 critical blockers

---

## BMAD Workflow Selection (Step 6 Output)

After passing BMAD validation, choose execution workflow:

| Workflow | Use When | Duration | Ideal For |
|----------|----------|----------|-----------|
| **Dev Story** | Clear scope, 6+ month timeline, complex product | 12-24 weeks | Idea-001 (Katana), Idea-005 (Sales QA) |
| **Quick Dev** | MVP clear, <4 weeks, simple product | 2-4 weeks | Idea-002 (Maps Bot) |
| **Product Brief** | Requires design phase, customer validation first | 4 weeks + dev | Idea-003 (VK Recipes), Idea-004 (VK Bot), Idea-006 (SaaS) |
| **TestArch Framework** | Quality/testing critical, architectural decisions needed | Integrated | Idea-005 (Sales QA — transcription accuracy critical) |

---

## Scoring Interpretation

| Score Range | Interpretation | Recommendation |
|-------------|-----------------|-----------------|
| **4.5-5.0** | Exceptional; clear winner | ✅ **START IMMEDIATELY** |
| **4.0-4.49** | Strong potential; high confidence | ✅ **APPROVE TO START** |
| **3.5-3.99** | Good idea, but needs pre-work | ⚠️ **CONDITIONAL: Do prep sprint first** |
| **3.0-3.49** | Viable, but moderate risk | ⚠️ **CONDITIONAL: Requires POC or validation** |
| **2.5-2.99** | High risk; needs major refinement | 🔴 **DEFER or REJECT; revisit later** |
| **<2.5** | Not recommended at this time | ❌ **REJECT** |

---

## Common Blockers & How BMAD Finds Them

| Blocker Type | BMAD Step | How Found | Example |
|---|---|---|---|
| **Undefined MVP scope** | Step 2-3 (Roles) | Roles needed for MVP unclear | Idea-005: "What modules in MVP?" |
| **Competitive threat unvalidated** | Step 4 (Consilium) | Competitors not analyzed by specialist | Idea-004: Salebot v2 not assessed |
| **Market assumption unproven** | Step 5 (Scoring) | Low confidence score reveals gap | Idea-006: 40% Week 1 retention unvalidated |
| **Timeline unrealistic** | Step 7 (Calendar) | Hours allocated don't match complexity | Idea-007: 30 days for 130-205 hours |
| **Execution risk unmitigated** | Step 8 (Deep Plan) | No if-then contingencies documented | Many ideas: "What if data is bad?" |
| **Portfolio imbalance** | Step 6 (Integration) | WIP overload or domain concentration | Current: 7 ideas queued, >3 recommended |

---

## BMAD Validation Outputs (What You Get)

Each validated idea produces:

1. **Summary document** (executive summary, 2-3 pages)
2. **Consilium report** (expert panel analysis, 5-10 pages)
3. **Scoring sheet** (weighted decision matrix)
4. **Deep Plan** (L1-L6 breakdown, 20+ pages)
5. **Timeline + milestones** (calendar with capacity allocation)
6. **Risk assessment** (contingency plans, go/no-go gates)
7. **Execution recommendation** (PROCEED, CONDITIONAL, DEFER)

**Total BMAD processing time:** 4-8 hours per idea (deep analysis)

---

## Key Takeaways

1. **BMAD removes guesswork** — Ideas are evaluated through 8 systematic steps, not gut feel
2. **Multiple perspectives matter** — Consilium (expert panel) catches blindspots that solo analysis misses
3. **Risk mitigation is explicit** — Step 8 deep plan identifies if-then gates before execution
4. **Timeline is realistic** — Capacity allocation in Step 7 prevents overcommitment
5. **Portfolio health is managed** — WIP caps and integration checks prevent chaos
6. **Execution is ready** — When BMAD is complete, team knows exactly what to do next

---

**BMAD Philosophy:** Better to spend 8 hours analyzing BEFORE execution than 80 hours fixing mistakes after.

