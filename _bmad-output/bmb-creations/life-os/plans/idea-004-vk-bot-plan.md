---
projectId: idea-004
planVersion: 1.0
created: 2026-02-05
status: READY
---

# Project Plan: Бот для ВК (аналог Salebot)

## Idea Summary
Self-hosted + privacy-first альтернатива Salebot для автоматизации коммуникации ВКонтакте. Serverless архитектура, visual flow builder, template marketplace.

**Motivation:** Salebot платный (12K₽/год) с ограничениями и vendor lock-in. Собственное решение: полный контроль, кастомизация, экономия.

**Target Market:** 500K+ сообществ ВК >5K подписчиков. Focus: enterprise (GDPR compliance) + digital-агентства (white-label B2B2C).

## Consilium Summary

**Six Hats Applied (Deep Mode):**
- ⚪ **Facts:** Salebot 15K users, рынок 500K+ сообществ, pain: 12K₽/год + ограничения
- 🔴 **Intuition:** "Как в Figma" drag-and-drop критично, "10 минут до первого бота"
- ⚫ **Risks:** API changes, rate limits (20 req/sec), unit-economics (50-100K₽/мес на 1000 users), GDPR
- 🟡 **Benefits:** Self-hosted (privacy), API-first (интеграции), white-label (B2B2C), marketplace
- 🟢 **Creativity:** Serverless (scale to zero), AI-подсказки GPT, template marketplace
- 🔵 **Process:** 3 phases (MVP → Beta → Launch), KPI: 100 beta users за 2 мес, $10K MRR за 12 мес

**Consensus:**
1. Positioning: Self-hosted + privacy-first + API-first (vs Salebot cloud-only)
2. Tech: Serverless (AWS Lambda), multi-tenant + self-hosted hybrid
3. UX: Drag-and-drop like Figma, "10 min to first bot" метрика
4. Risks: API monitoring, rate limiting day 1, unit-economics <5K₽/мес per 1000 users

## Scoring Summary

**Score:** 3.90 / 5.00 (78%)

- Impact: 4/5 - Потенциал 25-50K пользователей, $10K MRR
- Confidence: 3/5 - API ВК известен, UX uncertainty
- Effort: 3/5 - 200-300 часов (4 месяца)
- Strategic Alignment: 4/5 - Развитие навыков, portfolio SaaS
- Risk: 3/5 - API changes, competition, unit-economics
- Market Opportunity: 4/5 - Рынок существует, pain confirmed
- Competitive Advantage: 4/5 - Self-hosted unique, white-label B2B2C

**Gate Decision:** Proceed (>70%)

## Integration Summary

**Bucket:** Growth / Innovation
**Pattern:** Standalone Product (с Platform Extension потенциалом)
**WIP Decision:** Conditional allow (verify WIP <3 before start)

**Timeline:**
- Start: 2026-03-01
- MVP: 2026-04-30 (2 months)
- Launch: 2026-06-30 (4 months)

**Capacity:** 10-12 hours/week (Phase 1), 200-300 hours total

## Calendar Summary

**Start Date:** 2026-03-01
**End Date (MVP):** 2026-04-30
**End Date (Launch):** 2026-06-30
**Capacity:** 10-12 hours/week

**Milestones:**
1. **2026-03-01** - Kickoff: Infrastructure, ВК API research
2. **2026-03-15** - Webhook system + flow engine prototype
3. **2026-04-01** - Visual flow builder MVP (5 templates)
4. **2026-04-15** - Beta testing start (10-20 users)
5. **2026-04-30** - Phase 1 Complete: 100 beta signups target
6. **2026-05-31** - Phase 2: Drag-and-drop UI + 3 CRM integrations
7. **2026-06-30** - Phase 3: Marketplace + white-label + Product Hunt

## Deep Plan (L1-L6)

**Status:** TO BE COMPLETED (Step 8)

Deep plan will structure:
- L1: Role/Mission
- L2: Contribution areas (Product, Tech, GTM)
- L3: Work streams per area
- L4: Stages per stream
- L5: Tasks per stage
- L6: Atomic actions

**Scenario Template:** Tech Product Development (serverless SaaS)

**RACI Coverage Target:** ≥70%
**If-Then Actions Target:** ≥2

## Next Steps

1. **Complete Deep Plan (Step 8)** - L1-L6 structure with RACI
2. **Verify WIP** - Check portfolio WIP <3 before 2026-03-01
3. **Start BMAD Workflow** - BMB-002 (Product Development)
4. **Infrastructure Setup** - AWS Lambda, ВК API credentials
5. **Beta Recruitment** - 5-10 early testers from ВК dev community

## Deep Plan (L1-L6)

**Planning Mode:** Tech Product Development (Serverless SaaS)
**Status:** COMPLETE (2026-02-05)

### L1: Role/Mission
**Solo Founder & Full-Stack Developer** - создание и запуск self-hosted альтернативы Salebot для ВК автоматизации

### L2: Contribution Areas

**L2.1: Product Strategy & UX** (Priority: High)
- RACI: R/A: Solo Founder, C: Beta testers, I: ВК dev community
- Positioning, feature prioritization, UX design

**L2.2: Technical Development** (Priority: High)
- RACI: R/A: Solo Founder, C: DevOps consultant (optional), I: ВК API docs
- Backend API, webhook system, visual flow builder

**L2.3: Go-to-Market & Growth** (Priority: Medium)
- RACI: R/A: Solo Founder, C: Digital agencies, I: Product Hunt community
- Beta testing, Product Hunt launch, community building

### L3: Work Streams

**L2.1: Product Strategy & UX**
- **L3.1.1:** Competitive Analysis & Positioning
- **L3.1.2:** Visual Flow Builder UX Design
- **L3.1.3:** Template Library Design

**L2.2: Technical Development**
- **L3.2.1:** Serverless Infrastructure Setup
- **L3.2.2:** ВК API Integration & Webhook System
- **L3.2.3:** Visual Flow Builder Backend
- **L3.2.4:** Frontend Drag-and-Drop UI

**L2.3: Go-to-Market & Growth**
- **L3.3.1:** Beta Testing Program
- **L3.3.2:** Product Hunt Launch Campaign
- **L3.3.3:** Community Engagement (ВК Dev Community)

### L4: Stages (Selected Streams)

**L3.1.1: Competitive Analysis & Positioning**
- **L4.1.1.1:** Research Salebot features & pricing
- **L4.1.1.2:** Define differentiation (self-hosted, privacy-first)
- **L4.1.1.3:** Create value proposition document

**L3.1.2: Visual Flow Builder UX Design**
- **L4.1.2.1:** Wireframe flow builder interface
- **L4.1.2.2:** Design drag-and-drop components
- **L4.1.2.3:** Prototype "10 min to first bot" onboarding

**L3.2.1: Serverless Infrastructure Setup**
- **L4.2.1.1:** AWS Lambda / Cloud Functions setup
- **L4.2.1.2:** Database selection & configuration (PostgreSQL/MongoDB)
- **L4.2.1.3:** CI/CD pipeline setup (GitHub Actions)

**L3.2.2: ВК API Integration & Webhook System**
- **L4.2.2.1:** ВК API authentication setup
- **L4.2.2.2:** Webhook receiver implementation
- **L4.2.2.3:** Rate limiting & queue system (Bull/BullMQ)

**L3.3.1: Beta Testing Program**
- **L4.3.1.1:** Recruit 10-20 beta testers
- **L4.3.1.2:** Collect feedback & iterate
- **L4.3.1.3:** Achieve 100 beta signups by MVP launch

### L5: Tasks (Selected Stages)

**L4.1.1.1: Research Salebot features & pricing**
- **L5.1.1.1.1:** Sign up for Salebot trial
- **L5.1.1.1.2:** Document feature matrix (flows, integrations, analytics)
- **L5.1.1.1.3:** Analyze pricing tiers & limitations

**L4.2.2.2: Webhook receiver implementation**
- **L5.2.2.2.1:** Create webhook endpoint (Express.js/Fastify)
- **L5.2.2.2.2:** Parse ВК callback events (message_new, message_reply)
- **L5.2.2.2.3:** Implement signature validation (secret key)
- **L5.2.2.2.4:** Store events in database with retry logic

**L4.3.1.1: Recruit 10-20 beta testers**
- **L5.3.1.1.1:** Post in ВК dev community groups (10+ groups)
- **L5.3.1.1.2:** Reach out to 5 digital agencies via LinkedIn/email
- **L5.3.1.1.3:** Create beta signup landing page with waitlist

### L6: Atomic Actions (Selected Tasks)

**L5.1.1.1.1: Sign up for Salebot trial**
- **L6.1.1.1.1.1:** Visit salebot.pro
- **L6.1.1.1.1.2:** Create account with email
- **L6.1.1.1.1.3:** Set up test ВК community (create if needed)
- **L6.1.1.1.1.4:** Connect Salebot to test community via OAuth

**L5.2.2.2.1: Create webhook endpoint**
- **L6.2.2.2.1.1:** `npm init` new Node.js project (package.json)
- **L6.2.2.2.1.2:** Install Express.js, body-parser, dotenv
- **L6.2.2.2.1.3:** Create POST `/webhook` route with req.body parsing
- **L6.2.2.2.1.4:** Deploy to AWS Lambda via Serverless Framework (serverless.yml)

### If-Then Actions

1. **If** API ВК changes break integration **Then** activate API monitoring alert → implement fallback mechanism → notify users within 24h → update docs

2. **If** rate limit (20 req/sec) exceeded **Then** activate queue system (BullMQ) → throttle requests → exponential backoff (2^n seconds) → alert admin

3. **If** unit-economics exceed 5K₽/month per 1000 users **Then** optimize Lambda memory config (512MB→256MB) → consider hybrid cloud/self-hosted → pause scaling until optimized

4. **If** "10 min to first bot" UX not achieved in beta feedback (<70% complete in 10min) **Then** simplify onboarding flow → add interactive tutorial (5 steps max) → reduce default template complexity → A/B test

### Plan Quality Metrics

**Depth Covered:** 6/6 levels (L1-L6) = **100%** ✅
**Nodes Count:** ~55 nodes total
**RACI Coverage:** 3/3 L2 nodes = **100%** (target ≥70%) ✅
**If-Then Coverage:** 4 actions (target ≥2) ✅

**Quality Gate:** **PASS** - All criteria met

### Scenario Template Used
**Tech Product Development (Serverless SaaS)** - для продуктов с API integration, visual builder, и GTM focus

