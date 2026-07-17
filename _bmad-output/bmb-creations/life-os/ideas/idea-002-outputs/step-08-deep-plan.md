---
idea_id: idea-002
step: 08
step_name: Deep Plan
workflow: Life OS
created: 2026-02-05
status: COMPLETED
---

# Step 08: Deep Plan - Автоответчик для карт

## Детальный execution plan для запуска

### 🎯 Executive Summary

**Продукт:** Автоответчик для отзывов на Яндекс/Google Картах
**Goal:** $50k MRR (1000 клиентов) за 12 месяцев
**Investment:** $36.5k (bootstrap-friendly)
**Team:** 2 founders + 2 developers (outsource)
**Timeline:** 12 месяцев от start до scale

**Key Milestones:**
- ✅ Month 2: MVP + 10 beta clients
- ✅ Month 4: 100 paying clients, $5k MRR
- ✅ Month 8: Break-even, 500 clients, $25k MRR
- ✅ Month 12: 1000 clients, $50k MRR

---

## 📅 Детальный Timeline

### 🚀 PHASE 1: PRE-LAUNCH (Month 0 - Weeks 1-4)

#### Week 1-2: Foundation & Planning

**Day 1-3: Legal Setup**
- [ ] Регистрация ООО или ИП
- [ ] Открытие расчётного счёта
- [ ] Подготовка User Agreement (template адаптация)
- [ ] Подготовка DPA для GDPR/152-ФЗ
- [ ] Privacy Policy draft

**Deliverable:** Legal docs готовы для клиентов
**Owner:** Founder 1 (legal background)
**Cost:** $1.5k (юрист-консультант)

---

**Day 4-7: Technical Architecture**
- [ ] Architecture document (component diagram)
- [ ] Technology stack finalization
- [ ] Database schema design (PostgreSQL)
- [ ] API abstraction layer design (для легкой смены провайдеров)
- [ ] Infrastructure plan (Railway vs AWS)

**Deliverable:** Technical spec document (15-20 стр)
**Owner:** Founder 2 (CTO)
**Cost:** $0 (founder time)

---

**Day 8-14: Team & Vendor Setup**
- [ ] Наём 2 developers (Upwork/remote.com)
  - Backend developer (Node.js + NestJS)
  - Frontend developer (React + TypeScript)
- [ ] Настройка dev environment (GitHub, CI/CD)
- [ ] OpenAI API account setup (credits $100)
- [ ] Railway/AWS account setup
- [ ] Figma setup для UI design

**Deliverable:** Team assembled, tools configured
**Owner:** Founder 2 (CTO)
**Cost:** $0 (setup), $8k/месяц developers

---

#### Week 3-4: MVP Scoping & Beta Recruitment

**Day 15-18: Feature Prioritization**
- [ ] MVP feature list finalization (MoSCoW method)
- [ ] User stories написание (20-30 stories)
- [ ] Sprint planning (4 sprints × 2 weeks)
- [ ] Acceptance criteria для каждой фичи

**Deliverable:** Product backlog (Jira/Linear)
**Owner:** Founder 1 (Product)
**Cost:** $0

---

**Day 19-25: Beta Tester Recruitment**
- [ ] Outreach к 50 локальным бизнесам (рестораны/салоны)
  - LinkedIn personal messages
  - Email campaigns (холодные письма)
  - Посты в профильных Facebook группах
- [ ] Screening calls (15-20 заинтересованных)
- [ ] Selection: 10 beta testers
- [ ] Beta agreement подписание (бесплатно в обмен на feedback)

**Deliverable:** 10 committed beta testers
**Owner:** Founder 1 (Sales/Marketing)
**Cost:** $0 (founder time)

---

**Day 26-28: Design & Branding**
- [ ] Logo design (Fiverr/99designs)
- [ ] Brand colors & typography
- [ ] Landing page design (Figma)
- [ ] Dashboard mockups (5-7 screens)
- [ ] Onboarding flow wireframes

**Deliverable:** Design system + mockups
**Owner:** Freelance designer
**Cost:** $500

---

### 🛠️ PHASE 2: MVP DEVELOPMENT (Month 1-2, Weeks 5-12)

#### Sprint 1 (Weeks 5-6): Backend Core + API Integration

**Week 5: Backend Foundation**
- [ ] NestJS project setup (auth, database, API structure)
- [ ] PostgreSQL schema creation (users, reviews, responses, settings)
- [ ] Redis setup (job queue, caching)
- [ ] BullMQ job queue configuration
- [ ] Authentication (JWT tokens)
- [ ] User CRUD operations

**Deliverable:** Backend skeleton running
**Owner:** Backend Developer
**Metrics:** 100% test coverage core modules

---

**Week 6: Platform API Integration**
- [ ] Yandex Maps API integration
  - OAuth flow
  - Fetch reviews endpoint
  - Publish response endpoint
- [ ] Google My Business API integration
  - OAuth flow (multi-step)
  - Fetch reviews
  - Publish response
- [ ] Webhook receivers (для real-time review notifications)
- [ ] API error handling + retry logic

**Deliverable:** Review fetching working для 2 платформ
**Owner:** Backend Developer
**Metrics:** Successfully fetch+publish 10 test reviews

---

#### Sprint 2 (Weeks 7-8): AI Engine + Moderation

**Week 7: LLM Integration**
- [ ] OpenAI API integration (GPT-3.5 + GPT-4)
- [ ] Hybrid routing logic
  - Sentiment analysis (simple=GPT-3.5, complex=GPT-4)
  - Star-based routing (5-star → GPT-3.5)
- [ ] Prompt engineering
  - Template prompts для разных типов отзывов
  - Few-shot learning integration (клиент примеры)
- [ ] Response generation pipeline
- [ ] Token usage tracking (cost monitoring)

**Deliverable:** AI генерирует ответы на тестовые отзывы
**Owner:** Backend Developer + Founder 2
**Metrics:** 70%+ approval rate на manual test set (50 отзывов)

---

**Week 8: Confidence & Moderation**
- [ ] Confidence scoring implementation
  - Perplexity calculation
  - Rule-based adjustments (keywords)
- [ ] Fact-checking filters
  - Blacklist: "возврат денег", "скидка", "бесплатно"
  - Whitelist: safe phrases
- [ ] Toxicity detection (Perspective API integration)
- [ ] Review queue (low-confidence → manual review)
- [ ] One-click approve/edit/reject flow

**Deliverable:** Moderation system functional
**Owner:** Backend Developer
**Metrics:** <5% false positives (safe content flagged), <1% false negatives (toxic content missed)

---

#### Sprint 3 (Weeks 9-10): Frontend Dashboard

**Week 9: Core UI**
- [ ] React + TypeScript + Tailwind setup
- [ ] Authentication pages (login/signup)
- [ ] Dashboard layout (sidebar, header)
- [ ] Review list view (pending, approved, published)
- [ ] Response editor (edit AI generated text)
- [ ] Platform connection status indicators

**Deliverable:** Functional dashboard (basic)
**Owner:** Frontend Developer
**Metrics:** <2s page load time, mobile responsive

---

**Week 10: Onboarding Wizard**
- [ ] Multi-step wizard UI
  - Step 1: Platform selection
  - Step 2: OAuth authorization
  - Step 3: Business info (tone, keywords)
  - Step 4: Template selection
  - Step 5: Review and launch
- [ ] Progress bar & gamification
- [ ] Demo mode (generate responses before auth)
- [ ] Personality training (upload примеры или choose presets)

**Deliverable:** Onboarding flow <10 минут
**Owner:** Frontend Developer + Founder 1 (UX)
**Metrics:** 80%+ completion rate (test with 10 users)

---

#### Sprint 4 (Weeks 11-12): Analytics & Polish

**Week 11: Analytics Dashboard**
- [ ] Metrics cards (ответов сгенерировано, published, pending)
- [ ] Rating change chart (Yandex/Google trends)
- [ ] Sentiment distribution chart (positive/neutral/negative)
- [ ] Response time average
- [ ] Top keywords в отзывах (word cloud)

**Deliverable:** Analytics dashboard v1
**Owner:** Frontend Developer
**Metrics:** All charts render <1s

---

**Week 12: Integration & Testing**
- [ ] End-to-end testing (Playwright/Cypress)
- [ ] Load testing (100 concurrent reviews processing)
- [ ] Security audit (basic: SQL injection, XSS, CSRF)
- [ ] Bug fixing sprint
- [ ] Documentation (API docs, admin guide)
- [ ] Deployment to production (Railway/AWS)

**Deliverable:** MVP ready for beta launch
**Owner:** Full team
**Metrics:** <10 critical bugs, 99% uptime в staging

---

### 🧪 PHASE 3: BETA LAUNCH (Month 3, Weeks 13-16)

#### Week 13-14: Beta Onboarding

**Day 85-90: First Wave (5 beta clients)**
- [ ] Personal onboarding calls (30 мин each)
- [ ] Platform authorization assistance
- [ ] Personality training setup
- [ ] Monitor first 20 reviews per client
- [ ] Daily check-ins (bugs, confusion points)

**Deliverable:** 5 beta clients active
**Owner:** Founder 1 (Customer Success)
**Metrics:** 100% activation (first response generated)

---

**Day 91-98: Second Wave (5 beta clients)**
- [ ] Onboarding remaining 5 clients
- [ ] Collect feedback (survey + interviews)
- [ ] Identify top 3 issues
- [ ] Hot-fix critical bugs (<24h response)

**Deliverable:** 10 beta clients active
**Owner:** Full team
**Metrics:** <5 critical bugs reported, NPS >40

---

#### Week 15-16: Iteration & PMF Validation

**Day 99-105: Feature Improvements**
- [ ] Address top 3 feedback items
- [ ] Onboarding simplification (based на observations)
- [ ] UI polish (confusing elements)
- [ ] Performance optimization (if needed)

**Deliverable:** MVP v1.1 deployed
**Owner:** Developers
**Metrics:** Onboarding time reduced to <8 minutes

---

**Day 106-112: PMF Assessment**
- [ ] Sean Ellis test (40%+ "very disappointed" = PMF)
- [ ] Usage metrics analysis (DAU, retention)
- [ ] Churn reasons (if any cancellations)
- [ ] Prepare case study (best client results)
- [ ] Pricing validation survey

**Deliverable:** PMF report + go/no-go decision
**Owner:** Founder 1 (Product)
**Metrics:** PMF score >40%, Week 1 retention >70%

**GO/NO-GO GATE:**
```
IF PMF score >40% AND retention >70% THEN
  → Proceed to Phase 4 (Paid Launch)
ELSE
  → Iterate for 4 more weeks (repeat Phase 3)
END IF
```

---

### 💰 PHASE 4: PAID LAUNCH (Month 4-6, Weeks 17-28)

#### Month 4 (Weeks 17-20): Launch Preparation

**Week 17: Marketing Assets**
- [ ] Landing page (conversion-optimized)
  - Hero: Clear value prop
  - Social proof: Beta testimonials
  - ROI calculator
  - Pricing table
  - FAQ
- [ ] Case study (best beta client)
- [ ] Blog setup (Ghost/WordPress)
- [ ] SEO optimization (target keywords research)

**Deliverable:** Marketing website live
**Owner:** Founder 1 + Freelance copywriter
**Cost:** $1k (copywriter + design polish)

---

**Week 18: Content Marketing**
- [ ] Write 5 SEO blog posts
  - "Как поднять рейтинг на Яндекс Картах"
  - "Автоматизация ответов на отзывы"
  - "Почему важно отвечать на отзывы"
  - "Google My Business best practices"
  - "Case study: Ресторан поднял рейтинг с 4.1 до 4.6"
- [ ] LinkedIn founder posts (5 posts)
- [ ] Guest post outreach (3 sites)

**Deliverable:** Content published
**Owner:** Founder 1 + Content writer
**Cost:** $500 (content writer)

---

**Week 19: Sales Channels Setup**
- [ ] Yandex.Direct campaign setup
  - Keywords: "автоответчик яндекс карты"
  - Budget: $500/мес
- [ ] VK Реклама setup (таргет: владельцы бизнеса)
- [ ] Partnership outreach
  - Zoon (proposal draft)
  - Restoclub (proposal draft)
  - 2GIS (proposal draft)
- [ ] Referral program implementation (код в продукте)

**Deliverable:** 3 acquisition channels active
**Owner:** Founder 1 (Growth)
**Cost:** $1k (ads setup + first month budget)

---

**Week 20: Launch Week**
- [ ] Public launch announcement
  - Product Hunt submission
  - VC.ru post
  - LinkedIn/Facebook posts
  - Email blast к 500 cold leads
- [ ] Monitor signup flow (funnel metrics)
- [ ] Support readiness (FAQ, chat)
- [ ] First 10 paying customers target

**Deliverable:** Launch executed, first revenue
**Owner:** Full team
**Metrics:** 10 paying customers, $390 MRR

---

#### Month 5-6 (Weeks 21-28): Growth Sprint

**Goal:** 100 paying customers, $5k MRR

**Weekly Cadence:**
- Monday: Review week metrics (signups, churn, CAC)
- Tuesday: Growth experiment planning (1-2 tests)
- Wednesday-Friday: Execution
- Weekend: Founder customer calls (5-10 per week)

**Growth Experiments (8 weeks = 16 experiments):**

**Week 21:**
- Experiment 1: A/B test landing page hero
- Experiment 2: Increase Yandex.Direct budget 2x

**Week 22:**
- Experiment 3: Referral program promo (email blast)
- Experiment 4: Cold outreach LinkedIn (100 messages)

**Week 23:**
- Experiment 5: Guest post on VC.ru
- Experiment 6: Free trial extension (10 → 20 ответов)

**Week 24:**
- Experiment 7: Partnership: Zoon meeting
- Experiment 8: VK community posts (рестораны/салоны groups)

**Week 25:**
- Experiment 9: Webinar "Управление репутацией" (100 attendees target)
- Experiment 10: Case study #2 published

**Week 26:**
- Experiment 11: Outbound sales (cold calls 50 businesses)
- Experiment 12: Pricing test (Starter $39 → $49)

**Week 27:**
- Experiment 13: Referral incentive increase (1 month → 2 months free)
- Experiment 14: Content: comparison post "vs competitors"

**Week 28:**
- Experiment 15: Partnership: 2GIS follow-up
- Experiment 16: Facebook ads test ($500 budget)

**Metrics Tracking:**

| Week | Customers | MRR | CAC | Experiments Run | Top Channel |
|------|-----------|-----|-----|-----------------|-------------|
| 20 | 10 | $390 | $100 | - | Launch buzz |
| 21 | 15 | $585 | $120 | 2 | Yandex.Direct |
| 22 | 22 | $858 | $110 | 2 | Referrals |
| 23 | 30 | $1,170 | $105 | 2 | SEO organic |
| 24 | 40 | $1,560 | $115 | 2 | Zoon partnership |
| 25 | 52 | $2,028 | $108 | 2 | Webinar |
| 26 | 67 | $2,613 | $125 | 2 | Outbound sales |
| 27 | 82 | $3,198 | $112 | 2 | Referrals spike |
| 28 | 100 | $5,000 | $118 | 2 | Mix (stable) |

**Success Criteria Month 6:**
- ✅ 100 paying customers
- ✅ $5k MRR
- ✅ CAC <$150
- ✅ Churn <7%/мес
- ✅ 2+ successful channels (repeatable)

---

### 📈 PHASE 5: SCALE (Month 7-12, Weeks 29-52)

#### Quarter 3 (Month 7-9, Weeks 29-40)

**Goal:** 500 customers, $25k MRR, break-even

**Focus Areas:**

**1. Product Enhancement (v1.5)**
- [ ] Few-shot personality learning (better AI quality)
- [ ] Advanced analytics (competitor comparison)
- [ ] Template marketplace (community templates)
- [ ] Mobile app (basic, React Native)
- [ ] API для third-party integrations

**Timeline:** 8 weeks development
**Owner:** Developers + 1 additional hire
**Cost:** $16k (2 months × $8k)

---

**2. Marketing Scale**
- [ ] SEO: 20 blog posts total (5 new per month)
- [ ] Paid ads scale: $2k/мес budget (Yandex + VK + Facebook)
- [ ] Partnerships finalized: Zoon, 2GIS revenue share deals
- [ ] Webinars: 2 per month (200 attendees each)
- [ ] Case studies: 5 total (different industries)

**Owner:** Founder 1 + Marketing hire (part-time)
**Cost:** $8k (ads + content + part-time hire)

---

**3. Sales Process**
- [ ] Outbound sales playbook (scripts, templates)
- [ ] Enterprise tier launch ($299/мес for networks 10+ locations)
- [ ] Sales CRM setup (Pipedrive/HubSpot)
- [ ] Customer success process (onboarding, check-ins)

**Owner:** Founder 1
**Cost:** $1k (CRM subscription)

---

**Monthly Growth Trajectory:**

| Month | Customers | New | Churn | MRR | CAC | Notes |
|-------|-----------|-----|-------|-----|-----|-------|
| 7 | 140 | 40 | -5% | $7k | $130 | Product v1.5 launch |
| 8 | 200 | 60 | -5% | $10k | $125 | Zoon partnership live |
| 9 | 280 | 80 | -5% | $14k | $120 | Webinars scaling |
| **End Q3** | **~300** | **180 total** | **5% avg** | **$15k** | **$125 avg** | **Close to break-even** |

**Break-Even Analysis (Month 9):**
- Revenue: $15k MRR × 12 = $180k ARR
- COGS (LLM + infrastructure): $5/client × 300 = $1.5k/мес
- Fixed costs: $10k/мес (team salaries)
- **Profit:** $15k - $1.5k - $10k = $3.5k/мес ✅

---

#### Quarter 4 (Month 10-12, Weeks 41-52)

**Goal:** 1000 customers, $50k MRR, profitability

**Focus Areas:**

**1. Product v2.0**
- [ ] Zoon browser extension (unlock 3rd platform)
- [ ] Fine-tuned Llama 3 (reduce LLM costs 90%)
- [ ] CRM integrations (amoCRM, Bitrix24)
- [ ] White-label option (для Zoon, 2GIS)
- [ ] Advanced features (voice replies prototype)

**Timeline:** 12 weeks
**Owner:** Development team (2 devs + 1 ML engineer)
**Cost:** $30k (3 месяца × $10k)

---

**2. Enterprise Sales**
- [ ] Outbound campaign: 500 restaurant chains (10+ locations)
- [ ] Enterprise sales deck
- [ ] Custom pricing proposals
- [ ] Target: 10 enterprise deals @ $299/мес = $3k MRR

**Owner:** Founder 1 (Sales)
**Cost:** $2k (sales tools, prospecting)

---

**3. International Expansion (Prep)**
- [ ] Market research: Ukraine, Kazakhstan (русскоязычные)
- [ ] Legal setup для cross-border (если нужно)
- [ ] Localization (currency, language tweaks)
- [ ] Partnership outreach (local aggregators)

**Owner:** Founder 2
**Cost:** $3k (legal + research)

---

**Monthly Growth Trajectory:**

| Month | Customers | New | Churn | MRR | ARPU | Notes |
|-------|-----------|-----|-------|-----|------|-------|
| 10 | 400 | 100 | -5% | $20k | $50 | v2.0 launch, Zoon live |
| 11 | 600 | 200 | -5% | $30k | $50 | Enterprise deals start |
| 12 | 1000 | 400 | -4% | $50k | $50 | Target achieved! |

**Year-End Financials:**
- **MRR:** $50k
- **ARR:** $600k
- **Profit margin:** ~50% ($25k profit/мес)
- **Team size:** 6 (2 founders + 4 employees)
- **Runway:** Infinite (profitable)

---

## 💼 Team & Roles

### Founding Team

**Founder 1: CEO/Product** (Full-time)
- Product vision & roadmap
- Customer development & sales
- Marketing & growth experiments
- Fundraising (если потребуется)

**Founder 2: CTO** (Full-time)
- Technical architecture
- Developer management
- Infrastructure & DevOps
- AI/ML optimization

---

### Initial Team (Month 1-6)

**Backend Developer** (Contract, $4k/мес)
- NestJS, PostgreSQL, Redis
- API integrations (Yandex, Google)
- LLM pipeline development

**Frontend Developer** (Contract, $4k/мес)
- React, TypeScript, Tailwind
- Dashboard & analytics UI
- Onboarding wizard

---

### Growth Team (Month 7+)

**Marketing Manager** (Part-time → Full-time, $3k/мес)
- Content marketing
- SEO & paid ads management
- Partnership coordination

**Customer Success** (Part-time, $2k/мес)
- Onboarding support
- Churn reduction campaigns
- Customer feedback collection

**ML Engineer** (Contract, Month 10-12, $5k/мес)
- Fine-tuning Llama 3
- Confidence scoring improvements
- Performance optimization

---

## 💰 Financial Plan

### Investment Required

**Phase 1-2 (MVP):** $18.5k
- Development: $16k
- Legal: $1.5k
- Infrastructure: $0.5k
- Design: $0.5k

**Phase 3-4 (Beta + Launch):** $5k
- Marketing assets: $1k
- Content creation: $0.5k
- Ads budget: $2k
- Tools/software: $0.5k
- Contingency: $1k

**Phase 5 (Scale):** $13k
- Additional development: $6k
- Marketing scale: $5k
- Tools/infrastructure: $2k

**Total to Break-Even (Month 9):** $36.5k

---

### Revenue Projections

| Month | Customers | MRR | ARR | Cumulative Revenue |
|-------|-----------|-----|-----|--------------------|
| 2 | 10 (beta) | $0 | $0 | $0 |
| 4 | 10 | $390 | $4.7k | $390 |
| 6 | 100 | $5k | $60k | $5.4k |
| 9 | 300 | $15k | $180k | $35k |
| 12 | 1000 | $50k | $600k | $175k |

**Year 1 Total Revenue:** ~$200k

---

### Cost Structure (Steady State, Month 12)

**Fixed Costs:**
- Team salaries: $18k/мес (6 people)
- Infrastructure: $1k/мес (AWS + OpenAI)
- Tools/software: $0.5k/мес
- Office/misc: $0.5k/мес
- **Total Fixed:** $20k/мес

**Variable Costs:**
- LLM inference: $180/мес (1000 clients × $0.18 after Llama optimization)
- Support: $1k/мес (customer success time)
- Marketing: $5k/мес (ads + content)
- **Total Variable:** $6.2k/мес

**Total Costs:** $26.2k/мес
**Revenue (Month 12):** $50k/мес
**Net Profit:** $23.8k/мес (48% margin)

---

### Funding Strategy

**Bootstrap до PMF (Month 4):**
- Founders investment: $20k (savings)
- Friends & Family: $10k
- Pre-sales (beta clients): $2k
- **Total:** $32k (enough для MVP + launch)

**Profitable growth (Month 5-12):**
- Self-funded из revenue
- No external funding needed

**Optional Seed Round (Month 12+):**
- IF желание aggressive scale (international expansion)
- Raise: $300-500k
- Valuation: $3-5M (based на $600k ARR)
- Use: Hiring (10+ team), marketing scale ($50k/мес), international

---

## 📊 Success Metrics & KPIs

### North Star Metric
**MRR (Monthly Recurring Revenue)**

### Leading Indicators

**Acquisition:**
- Weekly signups (target: 25/week к Month 6)
- CAC (target: <$150)
- Conversion rate (landing → signup: >3%)

**Activation:**
- Onboarding completion rate (>80%)
- Time to first value (<10 мин)
- First week retention (>70%)

**Retention:**
- Monthly churn rate (<5%)
- NPS (>50)
- DAU/MAU ratio (>30%)

**Revenue:**
- MRR growth rate (>15%/мес first 6 months)
- ARPU (target: $50)
- LTV/CAC (>3x)

---

### Monthly Tracking Dashboard

```
┌──────────────────────────────────────────────┐
│ MONTH 6 SCORECARD                            │
├──────────────────────────────────────────────┤
│ 🎯 MRR:              $5,000  ✅ (target $5k)  │
│ 👥 Customers:        100     ✅ (target 100)  │
│ 📈 Growth:           +30%    ✅ (target 15%)  │
│ 💰 CAC:              $118    ✅ (target $150) │
│ 😊 NPS:              55      ✅ (target 50)   │
│ 📉 Churn:            6%      ⚠️  (target 5%)  │
│ 🔄 Retention (W1):   72%     ✅ (target 70%)  │
│ ⏱️  Onboarding time: 8.5min  ✅ (target 10m)  │
└──────────────────────────────────────────────┘

Status: ON TRACK ✅
Action items: Focus on churn reduction (6% → 5%)
```

---

## 🚨 Risk Mitigation (Quick Reference)

| Risk | Probability | Impact | Mitigation | Cost |
|------|-------------|--------|------------|------|
| API Changes | High | High | Abstraction layer + monitoring | $5k |
| Platform Ban | Medium | High | Human review + legal docs | $3k |
| High Churn | Medium | High | Onboarding focus + retention features | $8k |
| LLM Quality | Medium | Medium | Fact-checking + confidence scoring | $5k |
| Cash Flow | Low | High | Bootstrap + pre-sales | $0 |

**Total Risk Budget:** $21k (включено в $36.5k total)

---

## 🎯 Go/No-Go Gates

### Gate 1: Post-MVP (Month 2)
**Criteria:**
- ✅ MVP deployed без critical bugs
- ✅ 10 beta clients onboarded
- ✅ >80% activation rate

**Decision:** Proceed to Beta Launch

---

### Gate 2: Post-Beta (Month 3)
**Criteria:**
- ✅ PMF score >40% (Sean Ellis test)
- ✅ Week 1 retention >70%
- ✅ NPS >40

**Decision:** Proceed to Paid Launch OR Iterate 4 more weeks

---

### Gate 3: Post-Launch (Month 6)
**Criteria:**
- ✅ 100 paying customers
- ✅ $5k MRR
- ✅ Churn <7%/мес
- ✅ LTV/CAC >3

**Decision:** Scale marketing OR Optimize product

---

### Gate 4: Pre-Scale (Month 9)
**Criteria:**
- ✅ Break-even achieved
- ✅ 300+ customers
- ✅ 2+ repeatable acquisition channels

**Decision:** Aggressive scale OR International expansion

---

## 📅 Critical Path

```
Month 0-2:  MVP Development
              ↓
Month 3:    Beta Launch (10 clients)
              ↓
         [GO/NO-GO GATE]
              ↓
Month 4-6:  Paid Launch → 100 clients
              ↓
         [GO/NO-GO GATE]
              ↓
Month 7-9:  Growth Sprint → 300 clients (break-even)
              ↓
         [GO/NO-GO GATE]
              ↓
Month 10-12: Scale → 1000 clients, $50k MRR
              ↓
         [SUCCESS OR PIVOT]
```

---

## 🎓 Key Learnings & Contingencies

### If PMF Not Achieved (Month 3)

**Signals:**
- PMF score <40%
- Retention <50%
- High churn in beta

**Actions:**
1. Customer interviews (all 10 beta clients)
2. Identify top 3 issues
3. 4-week iteration sprint
4. Re-test PMF

**Budget for iteration:** $8k (1 month development)

---

### If Growth Stalls (Month 6-9)

**Signals:**
- MRR growth <10%/мес
- CAC >$200
- No repeatable channels

**Actions:**
1. Pause scale, focus на retention
2. Deep dive user analytics (где drop-off?)
3. Pricing experiment (A/B test)
4. Consider pivot (pure analytics SaaS)

---

### If Competition Intensifies

**Signals:**
- New competitor с better product
- Price war (competitors drop <$30/мес)
- Large player enters (Яндекс/Google builds native solution)

**Actions:**
1. **Moat building:** Accelerate v2.0 (unique features)
2. **Niche focus:** Vertical specialization (только рестораны)
3. **M&A:** Acquisition by competitor (exit strategy)

---

## ✅ Launch Checklist (Final Week Before Public Launch)

**Legal:**
- [ ] User Agreement reviewed by lawyer
- [ ] DPA signed template ready
- [ ] Privacy Policy published
- [ ] Terms of Service published

**Technical:**
- [ ] Production infrastructure tested (load test 100 concurrent)
- [ ] Monitoring setup (Sentry, Datadog)
- [ ] Backup strategy tested (database recovery)
- [ ] Security audit completed (pen-test)

**Marketing:**
- [ ] Landing page live + conversion tracking
- [ ] 5 blog posts published (SEO)
- [ ] Case study (beta client) published
- [ ] Social media assets prepared

**Sales:**
- [ ] Pricing finalized
- [ ] Payment gateway tested (Stripe/CloudPayments)
- [ ] Onboarding flow tested with 5 users
- [ ] Support email/chat setup

**Team:**
- [ ] On-call rotation scheduled
- [ ] Launch day plan (roles, responsibilities)
- [ ] Crisis communication plan ready

---

## 🏆 Success Criteria (12-Month Vision)

**Quantitative:**
- ✅ 1000 paying customers
- ✅ $50k MRR ($600k ARR)
- ✅ 48% profit margin
- ✅ <5% monthly churn
- ✅ NPS >50
- ✅ LTV/CAC >4

**Qualitative:**
- ✅ Category leader в России (автоответчики для карт)
- ✅ 5+ case studies (разные индустрии)
- ✅ Partnership с Zoon или 2GIS (distribution)
- ✅ Team: 6 человек, culture defined
- ✅ International expansion ready (prep complete)

---

## 🚀 Beyond Year 1 (Vision)

**Year 2 Goals:**
- 5000 customers
- $250k MRR ($3M ARR)
- International expansion (Ukraine, Kazakhstan, Беларусь)
- Enterprise focus (сети 50+ локаций)
- Potential exit ($10-20M valuation)

**Potential Acquirers:**
- Яндекс (integrate в Яндекс.Справочник)
- 2GIS (add-on к их платформе)
- amoCRM/Битрикс24 (CRM integration native)
- International players (Podium, Grade.us)

---

## 📝 Final Notes

**This plan is:**
- ✅ Detailed enough для execution
- ✅ Flexible enough для pivots
- ✅ Realistic (bootstrap-friendly $36.5k)
- ✅ Data-driven (clear metrics & gates)

**Next Immediate Actions:**
1. [ ] Secure $36.5k funding (bootstrap/F&F)
2. [ ] Register legal entity
3. [ ] Hire 2 developers (by Month 0, Week 2)
4. [ ] Start MVP development (Sprint 1)

**Timeline to first revenue:** 4 months
**Timeline to break-even:** 9 months
**Timeline to $50k MRR:** 12 months

---

**READY TO EXECUTE!** 🚀

---

## Appendix: Tools & Resources

**Development:**
- Backend: NestJS, PostgreSQL, Redis, BullMQ
- Frontend: React, TypeScript, Tailwind CSS
- AI: OpenAI API, Llama 3 (later)
- Hosting: Railway (MVP) → AWS (scale)

**Marketing:**
- Landing page: Webflow/Framer
- Analytics: PostHog + Google Analytics
- SEO: Ahrefs/Semrush
- Email: Mailgun/SendGrid

**Sales:**
- CRM: Pipedrive (simple) or HubSpot (enterprise)
- Payments: Stripe (международные) + CloudPayments (РФ)
- Support: Intercom or Crisp

**Ops:**
- Project management: Linear or Jira
- Docs: Notion
- Communication: Slack
- Version control: GitHub
