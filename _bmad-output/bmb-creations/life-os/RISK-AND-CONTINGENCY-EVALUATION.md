# LIFE OS: COMPREHENSIVE RISK & CONTINGENCY EVALUATION
## All 7 Ideas - Risk Assessment & Mitigation Readiness

**Report Date:** 2026-02-05
**Evaluation Scope:** Top 3 risks per idea, contingency preparedness, overall risk level
**Assessment Methodology:** Multi-source analysis (consilium reports, risk analyses, execution plans)

---

## EXECUTIVE SUMMARY TABLE

| Idea | Title | Risk 1 | Risk 2 | Risk 3 | Overall Risk Level | Contingencies Ready? | Status |
|------|-------|--------|--------|--------|-------------------|----------------------|--------|
| **001** | Katana-VectorBT | Overfitting on historical data | Live trading execution failures | Insufficient capital for diversification | **HIGH** | ⚠️ PARTIAL | Paper Trading gate required |
| **002** | Auto-Reply Бот | API deprecation/changes | Platform ban (Google/Zoon ToS) | High churn rate (>10%/мес) | **HIGH** | ✅ PREPARED | Comprehensive mitigation documented |
| **003** | ВК Паблик Рецепты | Engagement drop if monetization heavy | Algo platform changes | Bot complexity/maintenance burden | **MEDIUM** | ✅ PREPARED | Phased approach, risk contingencies identified |
| **004** | ВК Бот (Salebot аналог) | Tight marketplace with strong competitors | API stability (ВК платформа) | High customer acquisition cost | **HIGH** | ⚠️ PARTIAL | Basic planning only, detailed risk analysis missing |
| **005** | QA для продаж | Privacy/compliance (152-ФЗ) - CRITICAL | Real-time latency requirements | Adoption resistance from sales team | **CRITICAL** | ⚠️ PARTIAL | Risk identified but incomplete mitigation plans |
| **006** | SaaS Consilium | "Universal mediocrity" positioning trap | Complex feature scope creep | High API costs (OpenAI, transcription) | **MEDIUM** | ✅ PREPARED | Detailed MVP scope + financial modeling |
| **007** | Beauty Franchise Scaling | Nikita partnership conditions unclear by Feb 7 | Mobile CRM adoption (Galina requirement) | Saxap competitive escalation | **CRITICAL** | ⚠️ CONDITIONAL | Gates require Feb 7 decisions; execution-ready IF gates pass |

---

## DETAILED RISK ANALYSIS BY IDEA

---

## IDEA 001: Katana-VectorBT - Торговая платформа автономных стратегий

### Status: PROCESSING STAGE (Consilium Complete)

**Risk Level: HIGH** (3/5 - Manageable with strict risk controls)

### Top 3 Risks

#### Risk 1: Overfitting on Historical Data
**Category:** Technical / Validation
**Probability:** HIGH (70%)
**Impact:** CRITICAL (renders strategies unprofitable in live trading)

**Description:**
- 33,280 strategies from Epic J create massive opportunity for curve-fitting
- Backtest results may not translate to live performance (slippage, latency, market changes)
- Insufficient historical data or unrealistic assumptions compound the problem

**Contingency Status:** ⚠️ PARTIAL
- **What's prepared:** Walk-forward optimization mentioned, Monte Carlo simulations recommended
- **What's missing:** Explicit out-of-sample validation protocol, real-time monitoring for parameter drift

**Mitigation Readiness (1-5):** 3/5
- Walk-forward validation documented in Consilium
- Paper Trading phase (1 month) required before Live
- Monte Carlo 95th percentile Max DD <20% gate specified
- **Gap:** Need automated drift detection system, not yet designed

**Contingency Plan:**
```
IF backtest performance ≠ live performance (>20% deviation) THEN
  1. Pause new strategy deployment
  2. Increase Paper Trading period (+1 month)
  3. Reduce position sizing by 50% on Live debut
  4. Add manual override for anomalous market conditions
```

---

#### Risk 2: Live Trading Execution Failures
**Category:** Operational / Market
**Probability:** MEDIUM-HIGH (60%)
**Impact:** CRITICAL (capital loss)

**Description:**
- Slippage (проскальзывание) - difference between expected and actual execution price
- Execution latency - delays in order placement/cancellation
- Broker outages - loss of position control
- Market conditions change between backtest period and live execution

**Contingency Status:** ⚠️ PARTIAL
- **What's prepared:** Slippage simulation (0.02-0.05%) in backtests mentioned
- **What's missing:** Live broker selection criteria, failover mechanism, position evacuation protocol

**Mitigation Readiness (1-5):** 2/5
- Risk-adjusted backtesting framework identified
- Paper Trading validates slippage assumptions
- **Critical gaps:**
  - No broker redundancy plan
  - No emergency liquidation protocol
  - Execution latency not modeled in backtests

**Contingency Plan:**
```
IF Paper Trading shows slippage >2x expected THEN
  1. Revise execution strategy (reduce position sizes)
  2. Switch to more liquid instruments
  3. Extend Paper Trading +2 weeks

IF broker outage occurs THEN
  1. Immediately contact backup broker
  2. Manual position reconciliation
  3. Pause new trades until system confirmed
  4. Review: Did we lose capital? If yes → insurance claim
```

---

#### Risk 3: Insufficient Capital for Diversification
**Category:** Financial
**Probability:** MEDIUM (50%)
**Impact:** HIGH (single drawdown kills entire portfolio)

**Description:**
- <$10K capital insufficient for diversifying across 3+ strategies
- Portfolio variance too high with concentrated bets
- One bad strategy drawdown can wipe out gains from others

**Contingency Status:** ✅ PREPARED
- **What's prepared:** Financial plan clearly states $10K-20K test, $50K+ for serious portfolio
- Conservative 20-40% ROI expectations set
- Break-even timeline 12-18 months realistic

**Mitigation Readiness (1-5):** 4/5
- Capital requirements clearly documented
- Phased investment approach outlined (test → serious)
- Risk scaling strategy present

**Contingency Plan:**
```
IF available capital <$10K THEN
  1. Start with single strategy on $5K
  2. Paper Trade other strategies for 3 months
  3. Add live capital only after profitable month
  4. Scale gradually (never exceed 25% portfolio in new strategy)

IF portfolio drawdown >15% on any month THEN
  1. Investigate which strategies underperformed
  2. Pause underperforming strategy
  3. Revert to live conservative allocation
  4. Paper Test improvements 1 month before reintroduction
```

---

### Consilium Recommendations (Key Changes)

| What | Change | Reason |
|------|--------|--------|
| **Timeline** | 90 → 120 days | Paper Trading + validation required |
| **Goal** | 3 → 2 Scaled-Live | Quality over quantity; higher success probability |
| **Priority** | Epic J first → Epic L first | Data quality critical; bad data = bad strategies |
| **Required Phase** | Add Paper Trading (1 month) | Risk mitigation: validate execution, slippage, latency |
| **Innovation** | Add Innovation Sprint (1 week) | Ensemble strategies + AutoML optimization |

### Current Status

**Completion:** 70% (Phases 3-4 complete)
**Next Gates:** Epic L data integration (2 weeks) → Innovation Sprint (1 week) → Paper Trading setup
**Go/No-Go Decision:** ✅ PROCEED (with timeline extension + risk controls)

---

---

## IDEA 002: Автоответчик для карт (Auto-Reply Bot)

### Status: PROCESSED (Risk Analysis Complete - Step 07)

**Risk Level: HIGH** (3/5 - Manageable with prepared mitigations)

### Top 3 Risks

#### Risk 1: API Deprecation/Changes by Google/Yandex
**Category:** Technical / Dependency
**Probability:** HIGH (60-70%)
**Impact:** CRITICAL (platform functionality loss)

**Description:**
- Google My Business API changes every 12-18 months
- Yandex could introduce restrictions unpredictably
- Twitter API became paid in 2023; similar precedents exist
- Loss of API access = entire product becomes inoperable

**Contingency Status:** ✅ FULLY PREPARED
- **What's prepared:**
  - API abstraction layer (decouples product from provider)
  - Version management (support 2-3 API versions simultaneously)
  - Fallback modes (browser extension as backup)
  - 2-week sprint migration plan documented
  - Customer communication protocol (pre-notify 30 days before breaking changes)

**Mitigation Readiness (1-5):** 4/5
- Comprehensive monitoring plan (subscribe to developer changelogs)
- Adapter pattern implemented for easy provider switching
- Quick migration plan (7-30 days depending on API change severity)

**Mitigation Details:**
```
BEFORE LAUNCH:
  ✅ Monitor official changelogs (Google Cloud, Yandex)
  ✅ Subscribe to developer mailing lists
  ✅ Build abstraction layer

POST-LAUNCH:
  ✅ API versioning system (2-3 versions simultaneously)
  ✅ Quick migration sprint (2 weeks max)
  ✅ Fallback mode: browser extension
  ✅ Customer pre-notification (30 days notice)
```

**Contingency Plan:**
```
IF Google API deprecated THEN
  [Day 0-7]   Assess new API requirements
  [Day 7-14]  Develop migration adapter
  [Day 14-21] Beta test with 10 clients
  [Day 21-30] Roll out to all customers
  Fallback: Browser extension mode for 30 days
```

**Cost of Mitigation:** $5k (development time)
**Residual Risk:** MEDIUM (cannot prevent, but quick adaptation possible)

---

#### Risk 2: Platform Ban (Google/Zoon ToS Violation)
**Category:** Legal / Compliance
**Probability:** MEDIUM (30-40%)
**Impact:** CRITICAL (reputation + legal liability)

**Description:**
- Google bans accounts for "bulk automated responses without human oversight"
- Zoon explicitly forbids scraping in ToS (no public API)
- Clients lose access to their business profiles
- Potential legal claims for damages

**Contingency Status:** ✅ FULLY PREPARED
- **What's prepared:**
  - Human review queue (mandatory 30% moderation)
  - Confidence threshold (>80% for auto-publish)
  - Rate limiting (10 responses/hour per location - looks human)
  - User Agreement liability disclaimer
  - Toxic content filtering (Perspective API)
  - Fallback: Manual mode for banned accounts

**Mitigation Readiness (1-5):** 4/5
- Legal docs prepared with liability caps
- Technical controls (rate limiting, human review)
- Diversification strategy (Yandex as primary, Google secondary)

**Mitigation Details:**
```
GOOGLE:
  ✅ Human review queue (30% of responses)
  ✅ Confidence threshold >80%
  ✅ Rate limiting (10/hour per location)
  ✅ User Agreement disclaimer
  ✅ Diversify to Yandex

ZOON:
  ✅ Exclude from MVP (too risky)
  ✅ Add in v2.0 after validation

LEGAL:
  ✅ User Agreement §Disclaimer
  ✅ Liability cap: subscription refund only
```

**Contingency Plan:**
```
IF single client Google ban THEN
  1. Pause auto-publish for that account
  2. Investigate root cause
  3. Update filters
  4. Offer manual mode + partial refund

IF mass bans (>5% clients) THEN
  1. Emergency: Switch all to manual review
  2. Appeal to Google support
  3. Communicate transparently
  4. Consider pivot to pure analytics
```

**Cost of Mitigation:** $3k (legal docs + rate limiting)
**Residual Risk:** MEDIUM-LOW (managed by human review)

---

#### Risk 3: High Churn Rate (>10%/месяц)
**Category:** Business / Retention
**Probability:** MEDIUM (40-50%)
**Impact:** HIGH (breaks unit economics)

**Description:**
- Clients cancel after 1-3 months (goal achieved or dissatisfaction)
- LTV drops from $450 to $150 (3 months vs 10 months lifetime)
- LTV/CAC ratio breaks below 3x threshold
- Unit economics become non-viable

**Contingency Status:** ✅ FULLY PREPARED
- **What's prepared:**
  - Week 1 critical onboarding (aha moment acceleration)
  - Progress tracking + gamification
  - Weekly value reports
  - Win alerts ("Your rating improved 0.2 stars!")
  - Advanced feature drip campaigns
  - Analytics addiction (switching cost)
  - Community/template marketplace (network effects)
  - Win-back campaigns (50% discount offers)
  - Cancellation surveys to identify churn reasons
  - Exit interviews for high-value clients

**Mitigation Readiness (1-5):** 5/5
- Comprehensive retention strategy documented
- Cohort-based churn targets (Month 1: <15%, Month 2-3: <10%, Month 4+: <5%)
- Multiple engagement hooks identified

**Mitigation Details:**
```
PREVENT CHURN:
  ✅ Week 1: Aha moment + onboarding checklist
  ✅ Month 1-3: Weekly reports + win alerts
  ✅ Month 4+: Analytics addiction + data lock-in
  ✅ Community: Template marketplace + network effects

REACT TO CHURN:
  ✅ Cancellation surveys
  ✅ Win-back offers (50% 2 months)
  ✅ Exit interviews (high-value clients)
```

**Churn Cohort Targets:**
```
Month 1:  <15% (onboarding friction)
Month 2-3: <10% (value not demonstrated)
Month 4+:  <5% (sticky customers)
Acceptable LTV: 10 months avg = $450 (still >3x CAC)
```

**Cost of Mitigation:** $8k (onboarding + retention features)
**Residual Risk:** MEDIUM (5-7% realistic churn achievable)

---

### Overall Assessment

**Consilium Verdict:** ✅ **STRONG GO WITH CAUTIONS**

**Confidence:** 8/10 (improved after risk analysis)

**Key Requirements:**
1. ❌ Remove Zoon from MVP (legal + technical risks too high)
2. ✅ Add human review queue (Google compliance)
3. ✅ Implement confidence scoring (only >80% auto-publish)
4. ✅ Prepare User Agreement with liability disclaimer

**Financial Health:** ✅ EXCELLENT
- Gross margin: 90%
- CAC: $100
- LTV: $450 (with churn mitigation)
- LTV/CAC: 4.5x
- Payback: 2.2 months
- Break-even: 45 clients (month 4-5)
- ROI: 13.7x in year 1

**Timeline:** MVP 2 months → Beta 3-4 weeks → Paid launch month 3

---

---

## IDEA 003: Паблик ВК с рецептами (10K subscribers)

### Status: PROCESSED (Consilium Complete)

**Risk Level: MEDIUM** (2.5/5 - Manageable with phased approach)

### Top 3 Risks

#### Risk 1: Engagement Drop Due to Heavy Monetization
**Category:** Community / Content
**Probability:** MEDIUM (40-50%)
**Impact:** HIGH (kills growth + monetization strategy)

**Description:**
- Pushing ads too hard → followers see it as spam
- Switching to paid content too early → audi ence resentment
- If engagement falls <3%, reclama partners won't buy
- Vicious cycle: engagement down → ad rates down → revenue down

**Contingency Status:** ✅ PREPARED
- **What's prepared:**
  - Phased approach (Months 1-2: ads only, Month 3+: growth focus, Month 5+: paid content)
  - Balance rule: 1 ad post per 5-7 regular posts (avoid spam perception)
  - Content calendar + automation (frees time for quality)
  - A/B testing of ad formats
  - Diversification across 3+ revenue sources (not dependent on one partner)

**Mitigation Readiness (1-5):** 4/5
- Clear monetization phases mapped
- Engagement rate targets (5%+ maintain)
- Quality-first positioning established

**Mitigation Details:**
```
PHASE 1 (Months 1-2): Ads only
  • Find 5-10 partners for reklama integratsii
  • Test different ad formats
  • Monitor engagement

PHASE 2 (Months 3-4): Growth acceleration
  • Viral formats (video-retsepti, contests)
  • Refera program
  • Growth target: +30-50% subscribers

PHASE 3 (Months 5+): Paid content
  • Only if engagement ≥5% AND audience ≥13K
  • Exclusive recipes, master-classes
  • Diversified income (rekkama + partners + paid)
```

**Contingency Plan:**
```
IF engagement drops <5% THEN
  1. Pause new ads (use existing partners only)
  2. Shift to content-heavy strategy
  3. Run contests/UGC campaigns (no monetization focus)
  4. Wait 2 weeks for recovery
  5. Resume ads only if engagement >4%

IF partnership exclusive clause conflicts THEN
  1. Negotiate: 1 exclusive post per week max
  2. Diversify: Never >50% revenue from single partner
```

**Cost of Mitigation:** Minimal (strategy adjustment)
**Residual Risk:** LOW (with phasing discipline)

---

#### Risk 2: VK Platform Algorithm Changes
**Category:** Technical / Platform Dependency
**Probability:** MEDIUM (40%)
**Impact:** MEDIUM (growth slowdown, not catastrophic)

**Description:**
- VK algorithms change (happened 3x in 2024)
- Organic reach drops (dependency on platform, not owned audience)
- Growth velocity slows without paid ads
- Potential migration to other platforms needed

**Contingency Status:** ✅ PREPARED
- **What's prepared:**
  - Multi-platform strategy (ВК + Telegram + Zen)
  - Own audience building (email list, Telegram community)
  - Telegram as owned channel (less algorithm-dependent)
  - Content repurposing across platforms

**Mitigation Readiness (1-5):** 3/5
- Multi-platform mentioned, but timeline not specified
- Telegram community not yet launched
- Email list strategy not detailed

**Mitigation Details:**
```
PRIMARY: ВК (current focus)
SECONDARY: Telegram (low algorithm risk)
  → Duplicate audience from ВК
  → Less dependent on algorithm
TERTIARY: Яндекс.Дзен (content distribution)
```

**Contingency Plan:**
```
IF VK organic reach drops >30% THEN
  1. Activate Telegram as primary community
  2. Start email newsletter (owned audience)
  3. Migrate high-engagement followers to Telegram
  4. Continue content production for both platforms
  5. Evaluate: VK still worth investment?
```

**Cost of Mitigation:** $2-3k (Telegram bot, email platform)
**Residual Risk:** MEDIUM (platform risk inherent, mitigated by diversification)

---

#### Risk 3: Bot Complexity & Maintenance Burden
**Category:** Technical / Ops
**Probability:** MEDIUM (45%)
**Impact:** MEDIUM (distraction from core business)

**Description:**
- Phase 3 bot adds complexity
- API changes require maintenance
- Support burden grows with automation
- Time spent on bot = time lost from content
- Small bugs can break automation, frustrate audience

**Contingency Status:** ⚠️ PARTIAL
- **What's prepared:** Phased approach (bot in Phase 3, not MVP)
- **What's missing:** Detailed bot requirements, support escalation plan, rollback procedures

**Mitigation Readiness (1-5):** 2/5
- Decision to delay bot to Month 5+ reduces risk significantly
- No detailed bot specs documented
- No rollback plan if bot fails

**Mitigation Details:**
```
BOT LIFECYCLE:
  Phase 3 (Month 5+): MVP Bot
    • Minimum viable functions (auto-post, FAQ)
    • Test with small subset of followers
    • Measure: <5% failure rate before full rollout

  Budget: 40-60 hours (consultant or dev)
  Cost: 60K₽ (outbound developer)
```

**Contingency Plan:**
```
IF bot reliability <95% THEN
  1. Pause bot deployment
  2. Hire dev to fix issues
  3. Extend testing period
  4. Option: Abandon bot, focus on content

IF bot breaks during peak usage THEN
  1. Immediate: Manual override (disabler switch)
  2. Rollback to pre-bot state
  3. Investigate root cause
  4. Test fix in staging (3 days min)
  5. Redeploy only if 100% confidence
```

**Cost of Mitigation:** $5-8k (dev support, testing)
**Residual Risk:** LOW (with cautious rollout approach)

---

### Overall Assessment

**Consilium Verdict:** ✅ **PROCEED WITH PHASED STRATEGY**

**Confidence:** 4/5 (HIGH for Phase 1-2, MEDIUM for bot in Phase 3)

**Key Success Factors:**
1. ✅ Engagement ≥5% (500+ active from 10K)
2. ✅ ARPU ≥250₽ for 3 months
3. ✅ Minimum 3 revenue sources (diversification)

**Financial Health:** ✅ SOLID
- Income: 25-50K₽/месяц (Phase 1-2)
- Payback: 2-3 months
- ROI: 150-250% in 6 months

**Timeline:**
- Phase 1-2: Months 1-4 (monetization + growth)
- Phase 3: Months 5+ (bot automation)

---

---

## IDEA 004: Бот для ВК (Salebot аналог)

### Status: INBOX (Minimal Analysis Available)

**Risk Level: HIGH** (3/5 - High competition, complex feature set)

### Top 3 Risks

#### Risk 1: Intense Competitive Pressure
**Category:** Market / Competition
**Probability:** HIGH (70%)
**Impact:** CRITICAL (CAC too high, pricing pressure)

**Description:**
- Salebot dominates market with premium features
- 2GIS, Битрикс24 have integrated bots
- Race to the bottom on pricing (commoditization)
- Difficult to differentiate on core features alone

**Contingency Status:** ⚠️ PARTIAL
- **What's prepared:** None documented in current materials
- **What's missing:** Competitive differentiation strategy, market positioning, pricing model

**Mitigation Readiness (1-5):** 1/5
- No market analysis beyond "self-made vs Salebot"
- No identified killer features
- No pricing strategy documented

**Mitigation Options:**
```
Option 1: Vertical Focus (not horizontal)
  → Focus on one industry (restaurants, salons, e-commerce)
  → Deep customization for that vertical
  → Avoid head-to-head with Salebot

Option 2: Price/Value Trap
  → Much cheaper than Salebot
  → Risk: Undercut on features, hard to scale margins

Option 3: Technical Moat
  → Better AI quality (custom fine-tuned models)
  → Unique integrations (proprietary CRM connectivity)
  → Risk: Salebot copies features within 6 months
```

---

#### Risk 2: ВК API Stability & Changes
**Category:** Technical / Dependency
**Probability:** MEDIUM (50%)
**Impact:** HIGH (product breaks if API changes)

**Description:**
- ВК API is known to be unstable
- Rate limits could kill bulk operations
- Scope of API access (what's allowed) can change
- ВК could launch built-in bot features (cannibalizes product)

**Contingency Status:** ❌ UNPREPARED
- **What's prepared:** None documented
- **What's missing:** API abstraction layer, fallback modes, deprecation monitoring

**Mitigation Readiness (1-5):** 0/5
- No risk analysis or contingency plan
- Would require rebuilding from ВК API dependency

---

#### Risk 3: Customer Acquisition Cost Too High
**Category:** Business / Economics
**Probability:** MEDIUM (50%)
**Impact:** HIGH (breaks unit economics)

**Description:**
- Small ВК businesses don't have large marketing budgets
- Must acquire customers via paid ads (expensive)
- Target audience (SMBs) price-sensitive
- CAC could exceed LTV if not careful

**Contingency Status:** ❌ UNPREPARED
- **What's prepared:** None documented
- **What's missing:** Unit economics model, CAC targets, pricing strategy

**Mitigation Readiness (1-5):** 0/5
- No financial model or GTM strategy documented

---

### Overall Assessment

**Status:** ⚠️ **NEEDS DEEPER ANALYSIS BEFORE PROCEEDING**

**Risks:** HIGH - competitive pressure, technical dependencies, poor unit economics potential

**Recommendation:**
- Conduct market analysis first (is there a gap Salebot doesn't fill?)
- Define killer feature or vertical focus
- Model unit economics (CAC, LTV, payback period)
- Reassess after answering: "Why would someone choose us over Salebot?"

**Current Contingency Readiness:** Very Low (1/5)

---

---

## IDEA 005: Софт для контроля качества отдела продаж (Sales QA)

### Status: PROCESSED (Consilium Complete)

**Risk Level: CRITICAL** (4/5 - Multiple critical risks, high complexity)

### Top 3 Risks

#### Risk 1: Privacy/Compliance (152-ФЗ) - CRITICAL
**Category:** Legal / Compliance
**Probability:** HIGH (70%)
**Impact:** CRITICAL (shutdown, fines, legal liability)

**Description:**
- Recording conversations without explicit consent = violation of 152-ФЗ
- Potential fines: up to 2 million rubles
- Client data (personal info in conversations) subject to GDPR
- Menagers могут claim "workplace surveillance" violations

**Contingency Status:** ⚠️ PARTIAL
- **What's prepared:**
  - Auto-consent in IVR (beginning of call)
  - Opt-out option for customers
  - Data retention: 30 days max
  - Legal docs template recommended
- **What's missing:**
  - Explicit legal consultation BEFORE launch
  - Compliance verification by lawyer
  - Data privacy officer assignment

**Mitigation Readiness (1-5):** 2/5
- Legal framework mentioned but NOT reviewed by lawyer
- Compliance measures identified but untested
- HIGH RISK: Proceeding without legal sign-off could destroy the project

**Critical Actions:**
```
BEFORE MVP LAUNCH (non-negotiable):
  1. Legal consultation with Russian data protection lawyer
     ✅ Verify 152-ФЗ compliance
     ✅ Verify consent mechanisms are sufficient
     ✅ Verify GDPR compliance (if international)
     ✅ Review liability caps in User Agreement

  2. Draft compliance checklist:
     ✅ IVR consent script
     ✅ Opt-out mechanism
     ✅ Data retention policy
     ✅ User Agreement with clear liability limitations
     ✅ Privacy policy
     ✅ Data Processing Agreement template

  3. HR coordination (internal):
     ✅ Ensure management approval for recording
     ✅ Employee consent forms
     ✅ Works council notification (if applicable)
```

**Contingency Plan:**
```
IF Роспотребнадзор investigation opens THEN
  1. Immediately pause transcription for affected customers
  2. Delete all conversation recordings for that customer
  3. Notify customer of issue
  4. Engage lawyer to respond to investigation
  5. Assess fine amount + remediation costs

IF legal analysis shows 152-ФЗ violation THEN
  1. Halt MVP launch immediately
  2. Pivot to "enterprise-only" model (businesses can self-consent)
  3. Or pivot to "text transcription" instead of live (gray area)
  4. Redesign with lawyer oversight before relaunch
```

**Cost of Mitigation:** $10-20k (legal consultation + compliance framework)
**Residual Risk:** HIGH even with mitigation (regulatory enforcement unpredictable)

---

#### Risk 2: Real-Time Latency Requirement
**Category:** Technical / Product
**Probability:** HIGH (80%)
**Impact:** CRITICAL (Module 3 feature doesn't work)

**Description:**
- Module 3 (real-time assistant) requires <500ms latency
- GPT-4 inference: 2-3 seconds typical
- Menagers won't wait 2 seconds for AI suggestion during live call
- Practical usability threshold: <1 second
- Current LLM tech cannot achieve this without expensive optimization

**Contingency Status:** ⚠️ PARTIAL
- **What's prepared:**
  - Hybrid caching approach (80% cached, 20% GPT)
  - Predictive loading during call setup
  - Streaming responses (show suggestion as it's generated)
- **What's missing:**
  - Actual latency benchmarking (is <500ms achievable?)
  - Fallback if latency can't be met
  - Option to delay Module 3 to v2.0

**Mitigation Readiness (1-5):** 2/5
- Strategies identified but NOT tested with real infrastructure
- Risk of Module 3 being killed due to latency

**Mitigation Strategy:**
```
PHASE 1 (MVP): Modules 1 + 2 only (NO real-time)
  • Module 1: Transcription + analysis (async, 24-hour turn-around OK)
  • Module 2: Sales script generation (async, overnight OK)
  • Timeline: 2-3 months

PHASE 2 (v1.0): Test Module 3 (real-time)
  • Build latency test infrastructure (benchmark GPT inference time)
  • Test with 10 beta clients
  • Success criteria: <1s latency achievable 90% of the time
  • If fails: Move to v2.0 roadmap

PHASE 3 (v2.0): Full real-time OR admit it's not viable
  • Option A: Invest in edge deployment + model quantization
  • Option B: Pivot to asynchronous suggestions (within 5 min after call)
```

**Contingency Plan:**
```
IF latency tests show >2 seconds THEN
  1. Accept: Real-time module is not viable for v1.0
  2. Pivot: Position as "rapid response" (1-5 min after call)
  3. Timeline: Delay Module 3 to v2.0 (6+ months later)
  4. Resource: Invest in model optimization research
```

**Cost of Mitigation:** $15-25k (benchmark testing, optimization R&D)
**Residual Risk:** HIGH (latency may be physical impossibility for current tech)

---

#### Risk 3: Sales Team Adoption Resistance
**Category:** Organizational / Change Management
**Probability:** MEDIUM (50%)
**Impact:** MEDIUM-HIGH (product unused, project fails)

**Description:**
- Menagers fear "Big Brother surveillance"
- Concern that system used against them (bonus docking, firing)
- Distrust of AI suggestions ("I know better")
- Change resistance from those who built processes manually

**Contingency Status:** ⚠️ PARTIAL
- **What's prepared:**
  - Positioning: "AI Coach, not Big Brother"
  - Gamification (ratings, achievements)
  - Show ROI (higher KPIs = more commission)
  - Internal change management training
- **What's missing:**
  - Detailed adoption playbook
  - Incentive alignment strategy
  - Rollback plan if adoption <30%

**Mitigation Readiness (1-5):** 3/5
- Strategy identified but execution details missing
- Success depends on proper internal positioning

**Mitigation Strategy:**
```
LAUNCH STRATEGY (adoption-focused):
  1. Position as "Your AI Coach" (not surveillance)
  2. Pilot with 3-5 willing champions first
  3. Share wins: "Champion A improved close rate +20%"
  4. Address fears: "Data used ONLY for coaching, not punishment"
  5. Incentive: Coaches (ROPs) bonus if menagers improve KPIs

METRICS:
  Week 1: >50% of target audience activated
  Week 4: >70% daily active rate
  Month 3: >60% using AI suggestions in calls
```

**Contingency Plan:**
```
IF adoption <30% at Month 1 THEN
  1. Conduct interviews: "What's not working?"
  2. Identify top blockers (surveillance fear? complexity? relevance?)
  3. Redesign positioning/features based on feedback
  4. Relaunch with new approach
  5. If still <30%, pivot to "pure analytics" (no suggestions)
```

**Cost of Mitigation:** $5-10k (change management, incentive design)
**Residual Risk:** MEDIUM (depends on culture fit)

---

### Overall Assessment

**Consilium Verdict:** ✅ **SRONGLY RECOMMEND GO, BUT WITH CRITICAL GATES**

**Confidence:** 5/5 (for the concept), 2/5 (for viability without legal clarity)

**NON-NEGOTIABLE REQUIREMENTS:**
1. 🚨 **LEGAL CLEARANCE FIRST** - Cannot proceed without 152-ФЗ compliance verified by lawyer
2. 🚨 **LATENCY TESTING** - Must prove Module 3 <500ms before including in scope
3. ✅ **MVP SCOPE** - Start with Modules 1+2 (transcription + analysis), delay Module 3

**Financial Health:** ✅ EXCEPTIONAL
- Unit economics: ROI 75,000% for customers
- Gross margin: 60-86%
- TAM: $50M+ (B2B sales software market)

**Timeline (REVISED):**
- Phase 1 (MVP): 2-3 months (Modules 1+2)
- Phase 2 (v1.0): 2 months (features, beta)
- Phase 3 (v2.0): 3-4 months (Module 3, if latency solved)
- Full product: 6-9 months

**Critical Path:**
1. Week 1: Legal consultation (non-negotiable gate)
2. Week 2-3: Latency benchmarking
3. Week 4+: Development IF gates cleared

---

---

## IDEA 006: SaaS Consilium Assistant

### Status: PROCESSED (Life OS Steps 2-8 Complete)

**Risk Level: MEDIUM** (2/5 - Manageable with focused MVP)

### Top 3 Risks

#### Risk 1: "Universal Mediocrity" Positioning Trap
**Category:** Product / Strategy
**Probability:** HIGH (70%)
**Impact:** HIGH (product too broad, users see no value)

**Description:**
- Original idea: "Do everything for everyone" (meetings, projects, personal advice)
- Risk: Watered-down product with weak value prop
- Competitors excel in specific domains (Slack for meetings, Notion for projects, etc.)
- Users try, see "meh, does all things but nothing great"

**Contingency Status:** ✅ FULLY PREPARED
- **What's prepared:**
  - **Decision: Narrow MVP to 2 killer modes only**
    - Mode 1: Meeting Moderator (real-time solution generation)
    - Mode 2: Task Distributor (intelligent task assignment)
  - Avoid "universal mediocrity" trap
  - Build deep functionality in 2 areas before expanding
  - Positioning: "Personal Board of Advisors" (not generic AI)

**Mitigation Readiness (1-5):** 5/5
- Consilium explicitly identified trap and proposed solution
- MVP scope narrowed + documented
- Phase 2 expansion roadmap (add personal advisor mode)

**MVP Strategy:**
```
PHASE 1 (MVP - 12 weeks): 2 modes only
  ✅ Meeting Moderator (killer feature #1)
  ✅ Task Distributor (killer feature #2)
  ❌ NOT: Personal consultant, project management, health tracking

PHASE 2 (v1.0 - +8 weeks): Expand to 3-4 modes
  ✅ Personal Consultant (finances, career, wellness)
  ✅ Project Dashboard (light - not competing with Notion)

PHASE 3+ (v2.0): Full "Life OS" ambition
```

**Success Criteria for MVP:**
```
Week 1 retention: >40% (validation gate)
  → If <40%: The 2 modes aren't compelling, pivot
  → If >40%: Proceed to Phase 2
```

---

#### Risk 2: Scope Creep & Feature Bloat
**Category:** Execution / Discipline
**Probability:** MEDIUM (50%)
**Impact:** MEDIUM (timeline slip, launch delay)

**Description:**
- Temptation to add "just one more mode" during development
- Customer requests for features outside 2 core modes
- "Life OS" brand suggests "do everything" → pressure to deliver
- 12-week timeline becomes 20 weeks with scope creep

**Contingency Status:** ✅ PREPARED
- **What's prepared:**
  - Explicit scope gates: "Only 2 modes in MVP"
  - User story prioritization framework (MoSCoW)
  - Weekly scope review gates
  - **Role:** Product Manager enforces scope discipline

**Mitigation Readiness (1-5):** 4/5
- Governance structure defined
- WIP limit mentioned (WIP <2 before start)
- Needs: Detailed feature prioritization doc

**Scope Discipline Process:**
```
WEEKLY SCOPE GATE:
  1. Feature request arrives
  2. Owner asks: "Is this in the 2 killer modes?"
  3. If NO: Add to Phase 2 backlog, not MVP
  4. If YES: Evaluate against timeline impact
  5. Decision: Build now (if <1 day) or Phase 2 (if >1 day)
```

**Contingency Plan:**
```
IF scope creep detected (timeline risk +5 days) THEN
  1. Emergency: Cut lowest-priority features
  2. Reassess Phase 2 backlog
  3. Option: Delay non-critical features to v1.1
  4. No exceptions: Launch 2-mode MVP on schedule
```

---

#### Risk 3: High API Costs (OpenAI, Transcription)
**Category:** Financial / Operations
**Probability:** MEDIUM (40%)
**Impact:** MEDIUM (margins get crushed)

**Description:**
- Transcription (Whisper): $0.006/min
- GPT-4 inference: $0.03-0.06 per 1K tokens
- Consilium analysis: 50K tokens/session × $0.06 = $3 per session
- 1000 users × 5 sessions/month = 5K sessions = $15K/month (too high)
- Pricing: $15/month per user
- Gross margin: $15 - $15 = $0 (BREAK-EVEN or negative)

**Contingency Status:** ✅ PREPARED
- **What's prepared:**
  - Freemium model (basic free, Pro $15/month)
  - Cost cap: API costs <$5k/month in MVP phase
  - Usage limits: Free tier limited to 50 sessions/month (manageable cost)
  - Pro tier: 500 sessions/month (margin positive if retention >70%)
  - Alternative: Self-hosted LLM option (Llama 3) for enterprise

**Mitigation Readiness (1-5):** 4/5
- Cost structure modeled
- Freemium strategy addresses cost issue
- Needs: Real usage forecasting (is 50 sessions/user reasonable?)

**Cost Management Strategy:**
```
TIER 1 (Free): 50 sessions/month
  • Cost to platform: ~$15
  • Price to user: $0
  • Conversion target: 10% → $15 revenue (Pro tier)

TIER 2 (Pro): $15/month, 500 sessions/month
  • Cost to platform: ~$150
  • Gross margin: $0 (break-even on LLM costs)
  • Covered by: Infrastructure, support, profit margin

TIER 3 (Enterprise): Custom pricing
  • Dedicated support + custom LLM fine-tuning
  • Margin: 40-50%
  • Target: 1-2 enterprise customers by Month 6
```

**Cost Reduction Tactics:**
```
Tactic 1: API optimization
  → Use GPT-3.5 Turbo (cheaper than GPT-4)
  → Cache repeated queries (same industry patterns)
  → Batch non-urgent analyses

Tactic 2: Usage management
  → Free tier: 50 sessions (manageable cost)
  → Set hard limits (no unlimited usage)

Tactic 3: Hybrid models
  → Migrate to self-hosted Llama 3 for enterprise (save 70% costs)
  → Keep OpenAI only for free tier (quality > cost)

Tactic 4: Revenue diversification
  → White-label to Notion, Slack (B2B2C revenue share)
  → API access for integrations
```

**Contingency Plan:**
```
IF API costs >$5k/month in Month 3 THEN
  1. Reduce free tier to 30 sessions (not 50)
  2. Increase Pro pricing to $25/month (test demand)
  3. Accelerate Llama 3 self-hosted integration
  4. If margin still negative: Raise seed round or reduce scope
```

**Cost of Mitigation:** $5k (optimization development)
**Residual Risk:** LOW (multiple cost reduction options available)

---

### Overall Assessment

**Status:** ✅ **GO WITH FOCUS & DISCIPLINE**

**Consilium Verdict:** ✅ **PROCEED WITH CONDITIONS**

**Confidence:** 3.65/5.0 (73%) - "Strong potential with moderate confidence"

**Key Success Factors:**
1. **Narrow MVP to 2 killer modes only** (don't try to be "Life OS" in v1)
2. **Enforce scope discipline** (weekly gates, no creep)
3. **Monitor API costs monthly** (don't let them spiral)
4. **Hit Week 1 retention >40%** (validation gate)
5. **Reach 100 paying users by Month 3** ($1.5k MRR target)

**Financial Health:** ✅ VIABLE
- LTV:CAC 5.6:1 (excellent)
- Payback: <2 months
- Gross margin: 70%+ (after API costs controlled)
- Break-even: $5k revenue/month (~300 Pro users)

**Timeline (REVISED):**
- MVP: 12 weeks (2 modes only)
- Beta: 4 weeks (validation)
- Launch: 2 weeks
- **Total: 18 weeks**

**Critical Gates:**
```
Week 1:  >40% retention (validation gate)
Month 2: 50 beta users with >60% NPS
Month 3: 100 paying users ($1.5k MRR)
```

---

---

## IDEA 007: Beauty Franchise Scaling (DepylBrazil)

### Status: ACTIVE (Planning Phase - CRITICAL GATES)

**Risk Level: CRITICAL** (4/5 - Multiple blockages, tight timeline, execution-dependent)

### Top 3 Risks

#### Risk 1: Nikita Partnership Conditions NOT Formalized by Feb 7
**Category:** Legal / Partnership
**Probability:** MEDIUM (40%) of conditions NOT being clear by deadline
**Impact:** CRITICAL (project stalls or loses expert guidance)

**Description:**
- Nikita's entry depends on "paid pilot" terms (фикс? %, KPI, bonus?)
- Ambiguous terms = dispute risk later
- Feb 7 decision deadline approaches (72-hour план-разведка window closes)
- Without clear terms, Nikita may withdraw during execution
- Loss of expert guidance downgrades project confidence from 8/10 to 6/10

**Contingency Status:** ⚠️ CONDITIONAL
- **What's prepared:**
  - Feb 7 decision gate explicitly documented
  - Template for conditions memo (2-page framework)
  - Options: фикс+bonus, %, pilot→partnership
  - Written agreement (email OK for now)
- **What's missing:**
  - Actual negotiation with Nikita
  - Legal review of partnership terms
  - Formal contract (not just email)

**Mitigation Readiness (1-5):** 2/5 (HIGH dependency on Feb 7 decision-making)
- Template exists but not yet filled
- Timeline extremely tight (2 days to finalize)
- Risk: Nikita says "need more time" → project slips

**Critical Path:**
```
TODAY (Feb 5):
  1. Nikita starts план-разведка (72-hour window)
  2. Galina + Nikita: Draft conditions memo (2 hours)

FEB 6:
  1. Complete conditions memo
  2. Nikita preliminary decision (yes/no/negotiate)

FEB 7 (DECISION DAY):
  ⭐ 9:00 AM: Nikita final meeting (1 hour)
     Q: "Partner with us? Yes/No/What terms?"
  ⭐ 10:00 AM: Signatures on conditions memo (30 min)

GATE OUTCOME:
  ✅ IF Nikita says YES + memo signed → PROCEED
  ❌ IF Nikita says NO or "need more time" → RESCOPE to March
```

**Contingency Plan:**
```
SCENARIO A: Nikita says YES by Feb 7
  → Proceed immediately with 3-stream parallel execution
  → Nikita as paid consultant + potential equity partner

SCENARIO B: Nikita says "YES but negotiate terms"
  → Negotiate final 2 days (Feb 7-8)
  → Delay kickoff by 3 days (Feb 8 → Feb 11)
  → 3-4 day slip manageable if Nikita aligned

SCENARIO C: Nikita says NO or "need time"
  → Project RESCOPED to March timeline (+2 weeks)
  → Evaluate: Can team execute without Nikita?
  → May downgrade success probability to 65%

SCENARIO D: Nikita says YES but on expensive terms
  → Evaluate ROI: Does his % payoff vs. cost?
  → If >$50k equity ask: May not be worth it
  → Option: Partial engagement (4 weeks instead of 8)
```

**Cost of Mitigation:** Negotiation effort (minimal $)
**Residual Risk:** HIGH (Nikita's decision is outside team's control)

---

#### Risk 2: Galina Mobile CRM Adoption by Feb 10
**Category:** Organizational / Technical
**Probability:** MEDIUM (50%) of adoption delay
**Impact:** CRITICAL (blocks training, timeline cascades)

**Description:**
- Galina requires "mobile-first" access ("Редко за ПК" - rarely at desk)
- Standard Bitrix24 setup = desktop-heavy
- If not mobile-accessible by Feb 10 → Galina won't use it
- Adoption failure → training delays → opening delays → full project slip

**Contingency Status:** ✅ PREPARED (Creative solution)
- **What's prepared:**
  - MVP-first mobile rollout (identified as creative tactic)
  - Phase 1 (Feb 8-10): Push notifications + checklist (2 hours setup)
  - Phase 2 (Feb 11-15): Заявки workflow on phone (8 hours)
  - Phase 3 (Feb 16-20): Full dashboard (20 hours)
- This approach proven: Behavioral adoption → Feature addition (not feature → adoption)

**Mitigation Readiness (1-5):** 4/5
- Clear phased rollout documented
- Timeline realistic (2 hours MVP very achievable)
- Risk: CRM specialist must understand priority (mobile > desktop initially)

**Mobile Rollout Strategy:**
```
WEEK 1 PHASE 1 (Feb 8-10): MVP 10% scope
  Build: Push notifications + simple checklist
  Deploy: To Galina's phone
  Success: Galina sees notification + clicks checklist
  Effort: 2 hours total

WEEK 2 PHASE 2 (Feb 11-15): Enhanced 30% scope
  Add: Заявки (approvals) workflow on phone
  Galina now: Gets notifications + approves leads + checks tasks
  Effort: 8 hours
  Success: Galina using system daily by Feb 12

WEEK 3 PHASE 3 (Feb 16-20): Full 100% scope
  Add: CRM dashboard + analytics (on phone)
  Galina: Full system operational
  Effort: 20 hours
```

**Contingency Plan:**
```
IF MVP not ready by Feb 10 THEN
  1. Emergency: Deploy basic version (notifications only, no checklist)
  2. Manual workaround: Galina gets daily SMS summary
  3. Extend Phase 1 deadline to Feb 12
  4. Risk: Training delayed 2 days, but manageable

IF Galina still not engaged by Feb 12 THEN
  1. Issue: Mobile approach not solving her problem
  2. Investigation: What IS blocking her? Complexity? Notification fatigue?
  3. Option A: Simplify (fewer notifications, clearer actions)
  4. Option B: Hybrid (phone app + assistant to help)
  5. Option C: Admit: CRM not right for Galina, find alternative
  6. Timeline impact: +1 week if pivot needed
```

**Cost of Mitigation:** $3-5k (CRM specialist for priority setup)
**Residual Risk:** MEDIUM (depends on CRM platform capabilities)

---

#### Risk 3: Saxap Competitive Escalation During Feb-Mar Execution
**Category:** Market / Competitive
**Probability:** MEDIUM (40%)
**Impact:** MEDIUM-HIGH (market share stolen, positioning challenged)

**Description:**
- Saxap is known competitor (mentioned in Data Room)
- If Saxap launches similar offering during Feb-Mar → market window closes
- DepylBrazil won't differentiate (new brand vs established)
- Franchisee interest diverted to Saxap

**Contingency Status:** ⚠️ PARTIAL
- **What's prepared:**
  - Speed as advantage (Feb-Mar execution fast-tracked)
  - Weekly competitive intelligence monitoring
  - Case study preparation during Feb-Mar (build defensibility)
- **What's missing:**
  - Differentiation strategy vs Saxap
  - "Defensibility" if Saxap matches on speed/features
  - Marketing strategy during Feb-Mar window

**Mitigation Readiness (1-5):** 2/5
- Awareness of competitive threat exists
- Speed is only tactic; need substantive differentiation

**Competitive Defense Strategy:**
```
TACTIC 1: Speed (defensibility: First-mover, case study)
  → Open Sochi salon by Mar 7 (before Saxap can react)
  → Create case study: "DepylBrazil Opens Salon in 30 Days"
  → Franchisee narrative: Proven model from day 1

TACTIC 2: Quality differentiation
  → Saxap may be quick but fragmented
  → DepylBrazil: Fully packaged system (CRM + training + standards)
  → Marketing: "Complete package vs DIY"

TACTIC 3: Founder story
  → Galina + Vivioletta + Maria = authentic founders
  → Saxap = corporate entity
  → Positioning: "Built by practitioners, for franchisees"

TACTIC 4: Network effects
  → First 3-5 franchisees → community of practice
  → Shared templates, case studies, success stories
  → Network becomes defensible moat
```

**Contingency Plan:**
```
IF Saxap announces competing offering during Feb-Mar THEN
  1. Assess: How similar is it? What's different?
  2. Speed play: Accelerate Sochi opening (if possible)
  3. Messaging: "DepylBrazil is founded BY salon owners, FOR salon owners"
  4. Timeline: Have case study ready within 2 weeks of Sochi opening
  5. Sales: If Saxap undercuts on price, double down on quality differentiation

IF Saxap opens salon in Sochi before DepylBrazil THEN
  1. Shift: Focus on other cities (Moscow, St. Pete, Kazan)
  2. Positioning: "The original, most experienced" vs Saxap
  3. Case studies: Vladim ir location established + profitable = proof
```

**Cost of Mitigation:** $3-5k (marketing materials, case study production)
**Residual Risk:** MEDIUM (competitive threat uncontrollable, but mitigation options exist)

---

### Overall Assessment

**Status:** ✅ **GO-CONDITIONAL** (Feb 7 gates are BLOCKER)

**Consilium Verdict:** ✅ **PROCEED IF GATES PASS**

**Confidence:** 80%+ (IF Feb 7 gates met), 20% (IF gates fail)

**CRITICAL SUCCESS FACTORS (Non-Negotiable):**

1. **🚨 FEB 7 DECISION GATE (BLOCKER)**
   - Nikita: Formal written agreement on terms by 23:59 Feb 7
   - Orgstructure: Functional roles matrix signed by all 4 by 23:59 Feb 7
   - **If either fails: RESCOPE entire project to March (+2 weeks)**

2. **📱 MOBILE CRM ADOPTION (ENABLER)**
   - Push notifications + checklist MVP live on Galina's phone by Feb 10
   - Galina using system daily by Feb 12
   - **If delayed: Training blocked, timeline +2 weeks**

3. **⚡ PARALLEL EXECUTION (ACCELERATOR)**
   - All 3 streams start Feb 8 simultaneously (not sequential)
   - CRM + Помещение + Docs all in progress simultaneously
   - **If serialized: Adds 2+ weeks to timeline**

4. **📊 WEEKLY GATE REVIEWS (ASSURANCE)**
   - Feb 7, Feb 19, Feb 28, Mar 5: Mandatory checkpoints
   - If gates slip: Immediate escalation + rescope
   - **Consistent monitoring prevents cascade failures**

**Financial Health:** ✅ EXCEPTIONAL
- Revenue increase: 150-250% in 6 months ($600k → $1.5-2.5M)
- ROI: 150-250% (per Consilium Yellow Hat analysis)
- Participant satisfaction: Exceptional (all 4 stakeholders have positive ROI)

**Timeline (AGGRESSIVE):**
- Week 1 (Feb 5-7): GATES & DECISIONS
- Week 2-3 (Feb 8-19): Parallel execution (CRM, помещение, docs)
- Week 4 (Feb 22-28): Integration & finalization
- Week 5 (Mar 1-7): LAUNCH
- **Total: 30 days as planned**

**Contingency Plan (If Feb 7 Gates Fail):**
```
If EITHER gate fails:
  → Entire timeline slips +2-3 weeks (rescope to March 21)
  → Success probability drops from 80% to 60%
  → Project becomes "Nice to have" vs "Must do"
```

---

---

## SUMMARY TABLE: RISK & CONTINGENCY EVALUATION

| Idea | Risk Level | Top 3 Risks | Contingencies Ready | Mitigation Readiness | Status | Recommendation |
|------|------------|-------------|---------------------|-----------------------|--------|-----------------|
| **001 Katana** | HIGH | Overfitting, Execution failures, Low capital | ⚠️ PARTIAL | 3/5 | Paper Trading required | ✅ GO (extend timeline) |
| **002 Auto-Reply** | HIGH | API deprecation, Platform ban, Churn | ✅ PREPARED | 4/5 | Remove Zoon, add human review | ✅ STRONG GO |
| **003 ВК Recipes** | MEDIUM | Monetization engagement drop, Platform algo, Bot complexity | ✅ PREPARED | 4/5 | Phased approach | ✅ PROCEED |
| **004 ВК Bot** | HIGH | Competition, API stability, CAC too high | ❌ UNPREPARED | 1/5 | Deep market analysis needed | ⚠️ NEEDS ANALYSIS |
| **005 Sales QA** | **CRITICAL** | Privacy/compliance, Real-time latency, Adoption resistance | ⚠️ PARTIAL | 2/5 | Legal gate + latency testing | ⚠️ GO w/LEGAL GATE |
| **006 SaaS Consilium** | MEDIUM | Universal mediocrity trap, Scope creep, API costs | ✅ PREPARED | 4/5 | Narrow MVP to 2 modes | ✅ GO w/FOCUS |
| **007 Beauty Franchise** | **CRITICAL** | Nikita terms unclear, Mobile CRM adoption, Saxap competition | ⚠️ CONDITIONAL | 2/5 | Feb 7 gates BLOCKER | ⚠️ GO-IF-GATES-PASS |

---

## RED FLAGS: CRITICAL RISKS LACKING CONTINGENCIES

| Idea | Critical Risk | Issue | Recommendation |
|------|---------------|-------|-----------------|
| **005** | Privacy/Compliance (152-ФЗ) | No legal sign-off, could destroy project | **LEGAL CONSULTATION REQUIRED BEFORE LAUNCH** |
| **005** | Real-time Latency | May be technically impossible, kills Module 3 | **LATENCY TESTING BEFORE MODULE 3 COMMITMENT** |
| **007** | Nikita Partnership | Feb 7 deadline, unclear terms | **WRITTEN AGREEMENT REQUIRED BY FEB 7** |
| **007** | Mobile CRM Adoption | Galina requirement, Feb 10 gate | **MVP DEPLOYMENT REQUIRED BY FEB 10** |

---

## TOKEN SAVINGS INSIGHTS

- **Idea 002** (Auto-Reply): Comprehensive risk analysis documented - can be reused for all review-automation products
- **Idea 003** (ВК Recipes): Low-risk phased approach = template for future content monetization
- **Idea 006** (SaaS): Consilium identified "universal mediocrity trap" = valuable pattern for all AI assistants
- **Idea 007** (Franchise): Detailed gate structure = project management template

---

## NEXT STEPS

1. **Idea 001:** Approve timeline extension (120 → 90 days), setup Paper Trading phase
2. **Idea 002:** Proceed immediately, remove Zoon from MVP scope
3. **Idea 003:** Proceed with phased strategy (Months 1-4: monetization + growth, Month 5+: bot)
4. **Idea 004:** Conduct competitive analysis + market sizing before proceeding
5. **Idea 005:** LEGAL CONSULTATION REQUIRED (non-negotiable)
6. **Idea 006:** Approve MVP scope (2 modes only), enforce weekly scope gates
7. **Idea 007:** Execute Feb 5-7 decision gates immediately, weekly checkpoints Mar 1-7

**Report Compiled:** 2026-02-05
**Assessment Confidence:** HIGH (based on consilium reports, risk analyses, execution plans)

