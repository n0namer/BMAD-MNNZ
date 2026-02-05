# Validation Examples: WRONG vs RIGHT Execution

## Purpose
Show concrete examples of poor vs excellent execution for critical workflow steps to prevent quality issues.

---

## Step 04: Consilium

### ❌ WRONG: Minimal, Rushed Consilium (Like Idea 007)

```markdown
## Consilium Analysis

**Specialists:** General Advisor, Tech Lead

### General Advisor
Looks good. Should work. Go for it.

### Tech Lead
Technically feasible. No major issues.

## Consensus
UNANIMOUS GO. Proceed.
```

**Problems:**
- Only 2 specialists (should be 4-6 for Standard, 6-8 for Deep)
- No Six Thinking Hats (no White/Red/Black/Yellow/Green/Blue)
- No depth (3 sentences total, should be 2-3 paragraphs per specialist)
- No specific analysis (no risks, assumptions, or tradeoffs identified)
- Too generic ("looks good" = no value)

### ✅ RIGHT: Quality Consilium Analysis

```markdown
## Consilium Analysis

**Specialists:** Tech Architect, Product Strategist, Risk Analyst, UX Lead

### 🤍 White Hat (Facts) - Tech Architect
**Current State:** Building SaaS platform for freelancers. Target market: 50K+ freelancers in CIS region. Existing competition: 3 major players (Xero, QuickBooks, Tinkoff Business).

**Technical Requirements:**
- Frontend: React dashboard with invoice tracking
- Backend: Node.js API + PostgreSQL
- Integrations: Banking APIs (Tinkoff, Sber), Tax APIs
- Scale: Start with 100 users, plan for 10K within 6 months

**Resources Available:** Solo developer, LLM-assisted, 20h/week capacity.

### 🔴 Red Hat (Intuition/Gut Feel) - Product Strategist
**Initial Reaction:** Strong market need but saturated space. Success depends on differentiation.

**Concerns:**
- Market dominated by established players with 5-10 year head start
- Freelancers price-sensitive (may not pay for new tool)
- Banking integrations complex (3-6 months each)

**Confidence:** 6/10 (viable if differentiated, but high risk)

### ⚫ Black Hat (Risks) - Risk Analyst
**Critical Risks:**
1. **Market Risk (HIGH):** Competing with Xero/QuickBooks who have massive budgets
   - Mitigation: Focus on niche (CIS freelancers, local tax compliance)
2. **Technical Risk (MEDIUM):** Banking API integrations complex
   - Mitigation: Start with manual CSV upload, add APIs later
3. **Resource Risk (MEDIUM):** Solo dev, 20h/week may be insufficient
   - Mitigation: Use LLM extensively, focus on MVP scope

**Assumptions to Validate:**
- Freelancers will pay $10/month (validate with 10 interviews)
- Banking APIs accessible (check documentation)
- Can build MVP in 2-3 months (verify scope)

### 🟡 Yellow Hat (Benefits) - UX Lead
**Key Benefits:**
1. **Local Focus:** CIS tax compliance built-in (competitors don't have this)
2. **Modern UX:** Better mobile experience than legacy tools
3. **Affordable:** $10/mo vs $30+ for Xero
4. **Quick Setup:** Onboarding in 5 minutes vs hours

**Competitive Advantage:** Only tool with CIS tax compliance + modern UX.

### 🟢 Green Hat (Creative Ideas) - Product Strategist
**Alternative Approaches:**
1. **Freemium Model:** Free for <$1K/mo freelancers, paid for above
2. **AI Tax Assistant:** Auto-categorize expenses, suggest deductions
3. **Telegram Bot:** Full functionality via bot (no web dashboard)
4. **B2B Pivot:** Sell to agencies managing multiple freelancers

**Recommendation:** Start with Telegram bot (faster MVP, easier adoption).

### 🔵 Blue Hat (Meta) - Tech Architect
**Process Check:**
- All key perspectives covered ✓
- Risks identified and mitigated ✓
- Creative alternatives explored ✓

**Consensus Needed On:**
1. MVP Scope: Web dashboard vs Telegram bot?
2. Banking Integration: Manual CSV vs API first?
3. Pricing: Freemium vs paid-only?

## Synthesis & Consensus

**Recommendation:** CONDITIONAL GO

**Conditions:**
1. Validate market: 10 user interviews + landing page test (100 signups)
2. Choose MVP approach: Telegram bot recommended (faster, easier)
3. Defer banking APIs: Start with manual CSV upload
4. Define success metrics: 100 paying users in 3 months

**If conditions met:** Strong GO (7/10 confidence)
**If not met:** PAUSE for more validation

**Timeline:** 2 weeks validation → 6-8 weeks MVP → 2 weeks beta

**Next Steps:**
1. Run 10 user interviews (Week 1-2)
2. Build landing page (Week 1)
3. If validated → Proceed to scoring (Step 05)
4. If not → Pivot or defer
```

**Why this is RIGHT:**
- 4-6 specialists (appropriate for Standard/Deep track)
- Six Thinking Hats applied (6 perspectives)
- 2-3 paragraphs per specialist (depth and specificity)
- Specific risks identified with mitigations
- Assumptions stated explicitly
- Creative alternatives explored
- Clear decision: CONDITIONAL GO (not just "go for it")
- Next steps defined

**Output Length:**
- WRONG: 50-80 words
- RIGHT: 500-800 words (10x more value)

---

## Step 05: Scoring

### ❌ WRONG: Rushed Scoring

```markdown
## Scoring Results

| Criterion | Score |
|-----------|-------|
| Impact | 4/5 |
| Feasibility | 4/5 |
| Alignment | 4/5 |

**Total: 4.0/5.0** → HIGH PRIORITY
```

**Problems:**
- No justification (why 4/5?)
- No evidence or reasoning
- All scores identical (suspicious)
- No weighted calculation
- Too generic

### ✅ RIGHT: Detailed Scoring

```markdown
## Scoring Results (MCDA Methodology)

### Criterion 1: Impact (Weight: 0.25)
**Score: 4/5**

**Justification:**
- Revenue potential: $10/mo × 1000 users = $10K/mo (target met)
- Time savings: 5h/week per freelancer (significant value)
- Market size: 50K+ potential users in CIS

**Evidence:**
- Competitor analysis: Xero has 3M users globally → 50K in CIS realistic
- User interviews (3/10 done): All willing to pay $10/mo for time savings

**Why not 5/5:** Market saturated, need differentiation to capture users

### Criterion 2: Feasibility (Weight: 0.20)
**Score: 3.5/5**

**Justification:**
- Technical: Feasible with React + Node.js (known stack)
- Resource: 20h/week sufficient for MVP (8-10 weeks)
- Complexity: Medium (banking APIs complex, but deferrable)

**Evidence:**
- Similar projects: Built invoice app in 6 weeks (Idea 002)
- LLM acceleration: 10x multiplier validated on API work
- Banking APIs: Can defer (start with CSV, add APIs later)

**Why not 4-5/5:** Banking API integration adds risk, resource constraints

### Criterion 3: Strategic Alignment (Weight: 0.25)
**Score: 4.5/5**

**Justification:**
- Finance goal: ₽50K/mo passive income → $10K/mo from 1K users contributes
- Business goal: Product launch → This is a product
- Skill goal: Learn SaaS business → Directly relevant

**Evidence:**
- Goals.yaml: Finance #1 goal is passive income
- This idea generates recurring revenue (SaaS model)
- Aligns with 3-year business goal (own product)

**Why not 5/5:** Slight misalignment with immediate focus (other ideas higher priority)

### Criterion 4: Effort Required (Weight: 0.15)
**Score: 3/5**

**Justification:**
- Time: 8-10 weeks for MVP (moderate)
- Complexity: Medium (banking APIs complex)
- Resources: Solo dev with LLM (manageable but not trivial)

**Scoring:**
- Low effort (1-2 weeks): 5/5
- Medium effort (2-3 months): 3/5 ← This idea
- High effort (6+ months): 1/5

### Criterion 5: Risk Level (Weight: 0.15)
**Score: 2.5/5** (lower is riskier)

**Justification:**
- Market risk: HIGH (competition from Xero, QuickBooks)
- Technical risk: MEDIUM (banking APIs complex)
- Resource risk: MEDIUM (solo dev, 20h/week constraint)

**Mitigation:**
- Market: Focus on niche (CIS compliance)
- Technical: Defer APIs (start with CSV)
- Resource: Use LLM extensively (10x multiplier)

**Why 2.5/5:** High market risk, but technical/resource risks mitigated

---

## Weighted Calculation

```
Total Score = Σ (Criterion Score × Weight)

= (4.0 × 0.25)   [Impact]
+ (3.5 × 0.20)   [Feasibility]
+ (4.5 × 0.25)   [Alignment]
+ (3.0 × 0.15)   [Effort]
+ (2.5 × 0.15)   [Risk]

= 1.00 + 0.70 + 1.125 + 0.45 + 0.375
= 3.65/5.0
```

**Priority Band:** HIGH PRIORITY (3.5-4.0 range)

**Decision:** PROCEED to portfolio integration (Step 06)

**Sensitivity Analysis:**
- If market risk eliminated (niche focus works): Score → 4.0/5.0 (CRITICAL)
- If effort doubles (banking APIs required): Score → 3.3/5.0 (MEDIUM)
```

**Why this is RIGHT:**
- Every score justified with reasoning
- Evidence provided (competitor analysis, user interviews)
- "Why not higher?" explains ceiling
- Weighted calculation shown
- Sensitivity analysis (what-if scenarios)
- Clear decision with rationale

**Output Length:**
- WRONG: 100 words
- RIGHT: 600-800 words (6-8x more value)

---

## Step 08: Deep Plan

### ❌ WRONG: Minimal Deep Plan (Like Idea 007)

```markdown
# Deep Plan

## L1: Overview
Build SaaS platform for freelancers.

## L2: Phases
1. Design
2. Development
3. Testing
4. Launch

Done.
```

**Problems:**
- Only L1-L2 (Deep Track should be L1-L6)
- No detail (4 sentences for entire plan)
- Generic phases (no specifics)
- No timeline, milestones, or dependencies
- No risk analysis
- No acceptance criteria

### ✅ RIGHT: Comprehensive Deep Plan (L1-L6)

```markdown
# Deep Plan: Katana (Finance SaaS)

## L1: High-Level Overview (The 30,000-foot view)

**What:** SaaS platform enabling CIS freelancers to track income/expenses and generate tax-compliant reports.

**Why:**
- Market need: 50K+ freelancers lack affordable, compliant tool
- Competitive advantage: Only tool with CIS tax compliance + modern UX
- Revenue potential: $10/mo × 1K users = $10K/mo passive income

**How:**
- MVP: Telegram bot (faster than web dashboard)
- Tech: Node.js backend + PostgreSQL + Telegram Bot API
- Timeline: 8-10 weeks MVP, 2 weeks beta, launch Q1 2026

**Key Decision:** Telegram bot over web dashboard (60% faster MVP)

## L2: Major Phases (5 phases, 10 weeks total)

### Phase 1: Foundation (Week 1-2)
**Goal:** Architecture designed, core APIs defined, DB schema finalized

**Key Activities:**
- Design system architecture (bot + API + DB)
- Define API endpoints (10-12 endpoints)
- Create DB schema (users, transactions, reports)
- Set up development environment

**Deliverables:**
- Architecture diagram
- API specification (OpenAPI)
- DB migration scripts
- Dev environment configured

**Risks:** None critical, standard setup phase

### Phase 2: Core Features (Week 3-5)
**Goal:** MVP feature set implemented (income tracking, expense categorization)

**Key Activities:**
- Implement Telegram bot commands (/start, /income, /expense)
- Build transaction API (CRUD)
- Implement auto-categorization (LLM-based)
- Create basic reports (monthly summary)

**Deliverables:**
- Working bot with 5 core commands
- Transaction API (10 endpoints)
- Auto-categorization (80% accuracy)
- Monthly report generator

**Risks:**
- LLM categorization may need fine-tuning (2-3 days)
- Telegram API rate limits (mitigate with queuing)

### Phase 3: Tax Compliance (Week 6-7)
**Goal:** CIS tax reports generated correctly

**Key Activities:**
- Implement tax calculation logic (Patent, USN, General)
- Generate tax reports (quarterly, annual)
- Validate against tax code (consultant review)
- Add export formats (PDF, Excel)

**Deliverables:**
- Tax calculator (3 regimes)
- Report templates (2 formats)
- Validation passed (external consultant)

**Risks:**
- Tax code changes (mitigate: consultant review)
- Compliance errors (critical, allocate extra time)

### Phase 4: Polish & Testing (Week 8-9)
**Goal:** Bug-free, user-friendly bot ready for beta

**Key Activities:**
- User testing (10 beta users)
- Bug fixes and refinements
- Performance optimization
- Documentation (user guide)

**Deliverables:**
- Zero critical bugs
- User guide (Notion)
- Beta feedback report
- Performance: <1s response time

**Risks:**
- User feedback may require scope changes (allocate buffer)

### Phase 5: Launch (Week 10)
**Goal:** Public launch, first 100 users onboarded

**Key Activities:**
- Deploy to production (Render/Railway)
- Launch marketing (Telegram channels, habr.com)
- Onboard first 100 users
- Monitor for issues

**Deliverables:**
- Production deployment
- 100 paying users
- Monitoring dashboard
- Support process established

**Risks:**
- Launch day traffic spike (mitigate: load testing)

## L3: Key Milestones (8 milestones)

### M1: Architecture Complete (Week 2, Feb 19)
**Success Criteria:**
- ✓ Architecture diagram reviewed and approved
- ✓ API spec finalized (12 endpoints)
- ✓ DB schema supports all features
- ✓ No critical design flaws identified

**Deliverable:** Architecture doc + API spec

### M2: MVP Core Features (Week 5, Mar 12)
**Success Criteria:**
- ✓ Bot responds to 5 core commands
- ✓ Transactions stored and retrieved
- ✓ Auto-categorization 80%+ accurate
- ✓ Monthly report generates correctly

**Deliverable:** Working MVP (internal use)

### M3: Tax Compliance Validated (Week 7, Mar 26)
**Success Criteria:**
- ✓ Tax calculations validated by consultant
- ✓ Reports match official formats
- ✓ All 3 tax regimes supported
- ✓ Export formats work (PDF, Excel)

**Deliverable:** Compliant tax module

### M4: Beta Launch (Week 9, Apr 9)
**Success Criteria:**
- ✓ 10 beta users onboarded
- ✓ Zero critical bugs reported
- ✓ User satisfaction 7+/10
- ✓ Performance meets targets (<1s)

**Deliverable:** Beta-ready product

### M5: Public Launch (Week 10, Apr 16)
**Success Criteria:**
- ✓ Production deployment stable
- ✓ 100 users onboarded
- ✓ Payment processing working
- ✓ Monitoring active

**Deliverable:** Live product, 100 users

### M6: Product-Market Fit (Month 2, May 16)
**Success Criteria:**
- ✓ 500 active users
- ✓ 20%+ monthly retention
- ✓ NPS score 40+
- ✓ $5K MRR

**Deliverable:** PMF validation report

### M7: Scale Milestone (Month 4, July 16)
**Success Criteria:**
- ✓ 2000 active users
- ✓ $20K MRR
- ✓ <2% churn rate
- ✓ Infrastructure scales smoothly

**Deliverable:** Growth metrics dashboard

### M8: Profitability (Month 6, Sep 16)
**Success Criteria:**
- ✓ Revenue > costs
- ✓ 5000+ users
- ✓ $50K MRR
- ✓ Sustainable growth rate

**Deliverable:** Financial sustainability report

## L4: Detailed Tasks (100+ tasks, organized by phase)

### Phase 1: Foundation Tasks (20 tasks)

#### 1.1 System Architecture
- [ ] 1.1.1 Design high-level architecture (bot-API-DB)
- [ ] 1.1.2 Choose hosting platform (Render vs Railway)
- [ ] 1.1.3 Define API authentication (JWT)
- [ ] 1.1.4 Plan database structure (users, transactions, reports)
- [ ] 1.1.5 Review architecture with Tech Architect specialist

#### 1.2 API Specification
- [ ] 1.2.1 Define endpoint structure (/api/v1/...)
- [ ] 1.2.2 Document 12 core endpoints (OpenAPI)
- [ ] 1.2.3 Define request/response schemas
- [ ] 1.2.4 Plan error handling
- [ ] 1.2.5 API versioning strategy

#### 1.3 Database Schema
- [ ] 1.3.1 Design users table (id, telegram_id, subscription)
- [ ] 1.3.2 Design transactions table (amount, category, date)
- [ ] 1.3.3 Design reports table (period, type, data)
- [ ] 1.3.4 Create migration scripts (Prisma)
- [ ] 1.3.5 Add indexes for performance

#### 1.4 Development Environment
- [ ] 1.4.1 Set up Node.js project (TypeScript)
- [ ] 1.4.2 Configure PostgreSQL locally
- [ ] 1.4.3 Install dependencies (Express, Prisma, Telegraf)
- [ ] 1.4.4 Set up linting and formatting (ESLint, Prettier)
- [ ] 1.4.5 Configure testing framework (Jest)

### Phase 2: Core Features Tasks (30 tasks)

#### 2.1 Telegram Bot
- [ ] 2.1.1 Initialize Telegraf bot
- [ ] 2.1.2 Implement /start command (user registration)
- [ ] 2.1.3 Implement /income command (add income)
- [ ] 2.1.4 Implement /expense command (add expense)
- [ ] 2.1.5 Implement /report command (monthly summary)
- [ ] 2.1.6 Add error handling and user feedback
- [ ] 2.1.7 Implement conversation flows (multi-step)
- [ ] 2.1.8 Add inline keyboards for navigation

#### 2.2 Transaction API
- [ ] 2.2.1 POST /api/v1/transactions (create)
- [ ] 2.2.2 GET /api/v1/transactions (list with filters)
- [ ] 2.2.3 GET /api/v1/transactions/:id (retrieve)
- [ ] 2.2.4 PATCH /api/v1/transactions/:id (update)
- [ ] 2.2.5 DELETE /api/v1/transactions/:id (soft delete)
- [ ] 2.2.6 Add pagination and sorting
- [ ] 2.2.7 Implement filtering (date range, category)
- [ ] 2.2.8 Add validation middleware

#### 2.3 Auto-Categorization
- [ ] 2.3.1 Integrate LLM API (OpenAI/Claude)
- [ ] 2.3.2 Design categorization prompt
- [ ] 2.3.3 Implement category prediction
- [ ] 2.3.4 Add confidence scores
- [ ] 2.3.5 Allow manual override
- [ ] 2.3.6 Store user corrections for learning
- [ ] 2.3.7 Test accuracy (target 80%+)

#### 2.4 Reporting
- [ ] 2.4.1 Calculate monthly income/expense totals
- [ ] 2.4.2 Generate category breakdowns
- [ ] 2.4.3 Format report for Telegram (Markdown)
- [ ] 2.4.4 Add charts/visualizations (optional)
- [ ] 2.4.5 Implement date range selection

### Phase 3: Tax Compliance Tasks (25 tasks)

#### 3.1 Tax Calculators
- [ ] 3.1.1 Research CIS tax regimes (Patent, USN, General)
- [ ] 3.1.2 Implement Patent tax calculator (6% revenue)
- [ ] 3.1.3 Implement USN calculator (6% revenue or 15% profit)
- [ ] 3.1.4 Implement General regime calculator
- [ ] 3.1.5 Add regime selection in user settings
- [ ] 3.1.6 Validate calculations with tax consultant

#### 3.2 Tax Reports
- [ ] 3.2.1 Design quarterly tax report template
- [ ] 3.2.2 Design annual tax report template
- [ ] 3.2.3 Generate reports in PDF format
- [ ] 3.2.4 Generate reports in Excel format
- [ ] 3.2.5 Match official tax form layouts
- [ ] 3.2.6 Add digital signatures (optional)

#### 3.3 Compliance Validation
- [ ] 3.3.1 Hire tax consultant for review
- [ ] 3.3.2 Test all 3 tax regimes with sample data
- [ ] 3.3.3 Validate against official guidelines
- [ ] 3.3.4 Fix any calculation errors
- [ ] 3.3.5 Add compliance disclaimer

### Phase 4: Testing & Polish Tasks (15 tasks)

#### 4.1 User Testing
- [ ] 4.1.1 Recruit 10 beta users
- [ ] 4.1.2 Onboard beta users
- [ ] 4.1.3 Collect feedback (survey + interviews)
- [ ] 4.1.4 Analyze pain points
- [ ] 4.1.5 Prioritize fixes and improvements

#### 4.2 Bug Fixes
- [ ] 4.2.1 Fix critical bugs (P0)
- [ ] 4.2.2 Fix high-priority bugs (P1)
- [ ] 4.2.3 Fix medium-priority bugs (P2)
- [ ] 4.2.4 Regression testing

#### 4.3 Performance Optimization
- [ ] 4.3.1 Profile API response times
- [ ] 4.3.2 Optimize slow queries (add indexes)
- [ ] 4.3.3 Implement caching (Redis optional)
- [ ] 4.3.4 Load testing (target 1000 concurrent users)
- [ ] 4.3.5 Validate <1s response time target

#### 4.4 Documentation
- [ ] 4.4.1 Write user guide (Notion/Markdown)
- [ ] 4.4.2 Create video tutorials (optional)
- [ ] 4.4.3 Document API for developers
- [ ] 4.4.4 Write troubleshooting FAQ

### Phase 5: Launch Tasks (10 tasks)

#### 5.1 Deployment
- [ ] 5.1.1 Set up production environment (Render/Railway)
- [ ] 5.1.2 Configure environment variables
- [ ] 5.1.3 Set up PostgreSQL production database
- [ ] 5.1.4 Deploy backend API
- [ ] 5.1.5 Configure SSL certificates
- [ ] 5.1.6 Set up monitoring (Sentry, LogRocket)

#### 5.2 Marketing
- [ ] 5.2.1 Create landing page
- [ ] 5.2.2 Post on Telegram channels (freelancer communities)
- [ ] 5.2.3 Post on habr.com (article)
- [ ] 5.2.4 Reach out to influencers

#### 5.3 User Onboarding
- [ ] 5.3.1 Monitor first 100 user signups
- [ ] 5.3.2 Respond to support questions
- [ ] 5.3.3 Fix any launch issues
- [ ] 5.3.4 Collect feedback and iterate

## L5: Dependencies & Critical Path

### Dependency Map
```
Architecture (M1) → Core Features (M2) → Tax Module (M3) → Beta (M4) → Launch (M5)
     ↓                    ↓                   ↓                ↓
   API Spec         Telegram Bot       Tax Calculator    User Testing
     ↓                    ↓                   ↓                ↓
  DB Schema      Auto-categorization    Report Export   Bug Fixes
```

### Critical Path (Longest dependency chain)
1. Architecture → API Spec → Telegram Bot → Core Features → Tax Calc → Beta → Launch
   **Duration:** 10 weeks (cannot be shortened without parallel work)

### Parallelization Opportunities
- API development + Bot development (Weeks 3-5)
- Tax calculator + Report templates (Week 6)
- Testing + Documentation (Week 8)

### Bottlenecks
1. **Tax Compliance Validation (Week 7):**
   - Requires external consultant (2-day turnaround)
   - **Mitigation:** Book consultant in advance (Week 5)

2. **Beta User Recruitment (Week 8):**
   - Need 10 users for testing
   - **Mitigation:** Start outreach Week 6

## L6: Risk Analysis & Contingencies

### High-Priority Risks

#### Risk 1: Tax Code Compliance Errors (Severity: HIGH, Probability: MEDIUM)
**Impact:** Legal issues, user trust damage, potential fines
**Mitigation:**
- Hire tax consultant for validation (Week 7)
- Add disclaimer: "Not official tax advice"
- Implement manual review option

**Contingency:** If validation fails, delay launch 1-2 weeks for fixes

#### Risk 2: LLM Auto-Categorization Accuracy <80% (Severity: MEDIUM, Probability: LOW)
**Impact:** Poor UX, manual work for users
**Mitigation:**
- Fine-tune on CIS transaction data
- Allow manual override + learning

**Contingency:** If <70% accurate, make categorization manual (fallback)

#### Risk 3: Telegram API Rate Limits (Severity: MEDIUM, Probability: MEDIUM)
**Impact:** Bot slow or unresponsive under load
**Mitigation:**
- Implement job queue (BullMQ)
- Rate limit: 30 messages/second

**Contingency:** If hit limits, throttle less critical operations

#### Risk 4: User Adoption Below Target (Severity: HIGH, Probability: MEDIUM)
**Impact:** Failed to reach 100 users in launch month
**Mitigation:**
- Pre-launch marketing (2 weeks before)
- Referral program (invite friends for free month)
- Outreach to freelancer communities

**Contingency:** If <50 users after 2 weeks, pivot to B2B (sell to agencies)

#### Risk 5: Payment Processing Issues (Severity: HIGH, Probability: LOW)
**Impact:** Cannot collect revenue
**Mitigation:**
- Use established provider (Stripe, YooKassa)
- Test thoroughly before launch

**Contingency:** If payment fails, offer manual bank transfer as fallback

#### Risk 6: Security Vulnerability (Severity: CRITICAL, Probability: LOW)
**Impact:** Data breach, legal liability
**Mitigation:**
- Security audit before launch
- Use encryption for sensitive data
- Regular security updates

**Contingency:** If breach occurs, notify users immediately, fix within 24h

### Assumptions to Validate
1. ✓ Freelancers will pay $10/mo (validate: 10 interviews)
2. ✓ Telegram bot acceptable UX (validate: prototype test)
3. ⏳ Can build MVP in 8-10 weeks (validate: Sprint 1 velocity)
4. ⏳ LLM categorization 80%+ accurate (validate: POC)
5. ⏳ Banking APIs accessible (validate: API documentation review)

---

**Plan Confidence:** 75% (Medium-High)
**Last Updated:** 2026-02-05
**Next Review:** After Phase 1 (Week 2)
```

**Why this is RIGHT:**
- Full L1-L6 depth (not just L1-L2)
- Specific timelines (weeks, dates)
- 100+ detailed tasks broken down
- Dependencies mapped (critical path identified)
- Risk analysis with contingencies
- Assumptions stated and validation plan
- Milestones with clear success criteria

**Output Length:**
- WRONG: 50-100 words (barely a plan)
- RIGHT: 2000-3000 words (comprehensive plan)

---

## Quality Validation Checklist

### For Consilium (Step 04)
- [ ] 4-6 specialists for Standard Track (6-8 for Deep)
- [ ] All Six Thinking Hats covered (White/Red/Black/Yellow/Green/Blue)
- [ ] 2-3 paragraphs per specialist (not 1-2 sentences)
- [ ] Specific risks identified (not generic "might be hard")
- [ ] Mitigations proposed for each risk
- [ ] Assumptions stated explicitly
- [ ] Creative alternatives explored (Green Hat)
- [ ] Clear decision: GO / CONDITIONAL GO / NO GO (not "looks good")
- [ ] Output: 500-800 words minimum

### For Scoring (Step 05)
- [ ] Every score justified with reasoning (not just numbers)
- [ ] Evidence provided (data, competitor analysis, interviews)
- [ ] "Why not higher?" ceiling explained
- [ ] Weighted calculation shown (MCDA)
- [ ] Sensitivity analysis (what-if scenarios)
- [ ] Clear decision with rationale
- [ ] Output: 600-800 words minimum

### For Deep Plan (Step 08)
- [ ] L1-L6 depth for Deep Track (not just L1-L2)
- [ ] Specific timelines (weeks, dates, not "soon")
- [ ] 100+ tasks broken down by phase
- [ ] Dependencies mapped (critical path)
- [ ] Risk analysis (5-8 risks minimum)
- [ ] Contingencies for high-severity risks
- [ ] Assumptions validated
- [ ] Output: 2000-3000 words minimum (L1-L6)

---

**Last Updated:** 2026-02-05
**Purpose:** Prevent Idea 007-type quality issues
**Usage:** Reference before completing critical steps
