---
ideaId: idea-004
title: "Бот для ВК (аналог Salebot)"
status: IN_PROGRESS
created: 2026-02-05
stepsCompleted: [step-02-roles-discovery, step-03-specialist-match, step-04-consilium, step-05-scoring, step-06-integration, step-07-calendar-sync, step-08-deep-plan]
---

# Life OS Workflow Plan: Бот для ВК (аналог Salebot)

## Idea Summary
**ID:** idea-004
**Title:** Бот для ВК (аналог Salebot)
**Domain:** бизнес/софт
**Motivation:** Salebot платный и с ограничениями. Своё решение: полный контроль, кастомизация, экономия на подписке.

**Функционал:** авто-ответы, воронки продаж, сбор заявок, интеграция с CRM
**Timeline:** MVP 1-2 месяца, полный продукт 3-4 месяца
**Resources:** 80-120 часов разработки, хостинг, БД

## Roles

**Spheres:** business, career, creative

**Required Roles:**
- Product Strategist — priority: high
  * Позиционирование против Salebot
  * Value proposition и дифференциация
  * Roadmap развития функций

- Market Analyst — priority: medium
  * Конкурентный анализ (Salebot, аналоги)
  * Анализ целевой аудитории (SMM, бизнес в ВК)
  * Оценка рыночного потенциала

- Operations Lead — priority: medium
  * Планирование инфраструктуры (хостинг, БД, webhook)
  * Процессы CI/CD
  * Масштабирование и надёжность

- Skill Development — priority: medium
  * Изучение API ВК, webhook
  * Освоение визуального конструктора flow
  * План обучения для разработки

- Creative Director — priority: medium
  * UX визуального конструктора сценариев
  * Дизайн интерфейса админки
  * Пользовательские flow и experience

**Notes:**
- Ключевая роль: Product Strategist (позиционирование против Salebot)
- Техническая роль добавится на этапе Deep Plan (backend, frontend)
- Focus на дифференциацию: что будет лучше, чем у Salebot?

## Specialist Matching

**Idea ID:** idea-004
**Idea Title:** Бот для ВК (аналог Salebot)

**Selected Specialists:**
- **Product Strategist** (product-strategist) — Определит позиционирование против Salebot, value proposition, roadmap развития (priority: high)
- **Market Analyst** (market-analyst) — Проведёт конкурентный анализ Salebot и аналогов, оценит целевую аудиторию (SMM, бизнес в ВК) и рыночный потенциал (priority: medium)
- **Operations Lead** (operations-lead) — Спланирует инфраструктуру (хостинг, БД, webhook), процессы CI/CD и масштабирование (priority: medium)
- **Creative Director** (creative-director) — Разработает UX визуального конструктора сценариев, дизайн админки и пользовательские flow (priority: medium)
- **Backend Architect** (backend-architect) — Спроектирует архитектуру интеграции с API ВК, webhook систему, обеспечит масштабируемость (priority: high)

**Notes:**
- Две high-priority роли: Product Strategist (стратегия) и Backend Architect (техническая реализация)
- Operations Lead критичен для продакшен-готовности (хостинг, БД)
- Creative Director важен для конкурентного UX визуального конструктора (преимущество над Salebot)
- Объединены Skill Development + Backend в Backend Architect (избежание дублирования)

## Consilium Recommendations (Six Hats)

**Mode:** Deep

**Specialists Consulted:**
- **Market Analyst** (⚪ White Hat - Facts): Salebot ~15K users, тариф от 990₽/мес. Альтернативы: Senler (500₽), MessageBot (1200₽). Целевая аудитория: 500K+ сообществ ВК >5K подписчиков. Pain: дороговизна (12K₽/год), ограничения, vendor lock-in. Потенциал: 5-10% рынка (25-50K пользователей за 2 года) при цене на 30-50% ниже + больше кастомизации.

- **Creative Director** (🔴 Red Hat - Intuition): Интуиция: пользователи хотят "как в Figma" - drag-and-drop без кода. Первое впечатление критично. Эмоционально важно: "я сам создал бота за 10 минут" (эффект мгновенной победы). Визуальная метафора: flow как flowchart.

- **Operations Lead** (⚫ Black Hat - Risks): Риски: (1) API ВК меняется → постоянная поддержка, (2) Rate limits ВК 20 req/sec → нужна очередь, (3) Хостинг для 1000+ users = 50-100K₽/мес → unit-economics под вопросом, (4) Salebot может снизить цены, (5) GDPR/персональные данные → legal compliance.

- **Product Strategist** (🟡 Yellow Hat - Benefits): Возможности: (1) Open-source → community + lower costs, (2) Self-hosted → privacy-first для enterprise (нет у Salebot), (3) API-first → интеграции с любыми CRM, (4) White-label → франшизы digital-агентствам (B2B2C), (5) Marketplace плагинов → community monetization.

- **Backend Architect** (🟢 Green Hat - Creativity): Идеи: (1) No-code editor с AI-подсказками (GPT для сценариев), (2) Serverless (AWS Lambda) → scale to zero, низкая стоимость, (3) Multi-tenant SaaS + self-hosted гибрид, (4) Real-time analytics dashboard, (5) Template marketplace (готовые сценарии по индустриям).

- **Product Strategist** (🔵 Blue Hat - Process): Структура: Phase 1 (MVP, 1-2 мес) - webhook + simple flow builder + 5 templates; Phase 2 (Beta, 2-3 мес) - drag-and-drop + 3-5 CRM интеграций + analytics; Phase 3 (Launch, 3-4 мес) - marketplace + white-label + enterprise. KPI: 100 beta-users за 2 мес, 1000 users за 6 мес, $10K MRR за 12 мес. GTM: Product Hunt + ВК dev community + кейсы.

**Consensus View (Balanced):**
1. **Стратегия**: Self-hosted + privacy-first + API-first подход. Target: enterprise (GDPR) + digital-агентства (white-label). Дифференциация: не дешевле, а гибче и безопаснее.
2. **Технический подход**: Serverless (AWS Lambda) для low cost, multi-tenant SaaS + self-hosted hybrid. MVP: webhook + visual builder + 5 templates (2 мес).
3. **UX приоритет**: Drag-and-drop как в Figma. Метрика: "10 минут до первого бота". Template marketplace в Phase 3.
4. **Риски**: API monitoring + fallback, rate limiting + queue с 1-го дня, unit-economics <5K₽/мес на 1000 users (serverless помогает), GDPR consultant в Phase 2.


## Scoring Summary

**Criteria Scores (1-5):**
- **Impact: 4/5** — Потенциал 25-50K пользователей за 2 года (5-10% рынка), $10K MRR за 12 месяцев. Решает pain: дороговизна Salebot и vendor lock-in. НЕ 5/5: ниша ВК, не массовый рынок.

- **Confidence: 3/5** — Средняя уверенность: API ВК известен, примеры есть (Salebot работает). Риски: API changes, конкуренция. Техническая сложность умеренная. Неясность: достижим ли "10 минут до первого бота" UX.

- **Effort: 3/5** — MVP 1-2 месяца = 80-120 часов. Total Phase 1-3: 200-300 часов. Средняя сложность: webhook + visual builder + integrations. Serverless снижает инфраструктурную сложность.

- **Strategic Alignment: 4/5** — Хорошее соответствие: развитие навыков (API, serverless, UX), потенциал B2B2C (white-label), portfolio SaaS продукт. НЕ 5/5: отвлекает от других проектов (WIP risk).

- **Risk: 3/5** — Средний риск: API changes (ВК стабилен, но бывают breaking), unit-economics неизвестен (serverless помогает), конкуренция может снизить цены, GDPR управляем через consultant.

- **Market Opportunity: 4/5** — Рынок существует: Salebot 15K users, потенциал 500K+ сообществ ВК. Pain: 12K₽/год и ограничения. Тренд: автоматизация коммуникаций растёт. НЕ 5/5: ниша ВК (не Telegram/WhatsApp).

- **Competitive Advantage: 4/5** — Strong: self-hosted + privacy-first (нет у Salebot), API-first + white-label (unique), template marketplace. НЕ 5/5: Salebot имеет brand recognition и first-mover advantage.

**Overall Score:** 3.90 / 5.00 (78%)

**Weights Used:**
- Impact: 0.25, Confidence: 0.20, Effort: 0.15, Strategic Alignment: 0.15, Risk: 0.15, Market Opportunity: 0.10, Competitive Advantage: 0.10

**Decision Rationale:**
- Strong project (>70% threshold): высокий impact и market opportunity компенсируют умеренные confidence и effort
- Proceed с фокусом на risk mitigation: API monitoring, unit-economics validation в MVP
- Key success factors: достижение "10 минут до первого бота" UX, serverless cost optimization, early GDPR compliance

## Stage Gate: Scoring

**Gate Decision:** Proceed
**DoD Checklist:** Met
- ✅ Scores complete and justified
- ✅ Key risks acknowledged (API changes, competition, unit-economics)
- ✅ Strategic alignment acceptable (4/5)
- ✅ Overall score 3.90/5.00 exceeds 70% threshold

**Notes:** Proceed to Integration with focus on risk mitigation plan and unit-economics validation in MVP phase.


## Integration Summary

**Bucket:** Growth / Innovation
- Новый SaaS продукт с коммерческим потенциалом ($10K MRR target)
- Innovation: serverless + self-hosted hybrid, AI-подсказки, template marketplace
- Развитие навыков: API integration, UX design, product development

**Portfolio Health:** Moderate (conditional proceed)
- ⚠️ Adding another innovation project может перегрузить WIP
- ✅ Score 3.90/5.00 оправдывает приоритизацию
- Recommendation: Limit WIP to 2-3 projects max, defer lower-priority если WIP=3

**Integration Pattern:** Standalone Product (с Platform Extension потенциалом)
- Собственный codebase, инфраструктура, GTM
- API-first подход позволит будущие интеграции с CRM/analytics платформами
- Не Bundle, не Enabler

**Dependencies:**
- External: ВК API (stable)
- Infrastructure: AWS Lambda / Cloud Functions
- Optional (Phase 2): CRM integration APIs

**Shared Components:**
- None initially (greenfield)
- Future potential: reusable webhook framework, visual flow builder library

**BMAD Workflow:** Product Development (BMB-002) — Defer to post-planning
- Workflow включает: Discovery → Design → MVP → Beta → Launch
- Соответствует 3 phases из консилиума
- Start: After Deep Plan (Step 8)

**Timeline (High-Level):**
- Start: 2026-03-01 (через 3-4 недели)
- Phase 1 MVP End: 2026-04-30 (2 месяца)
- Phase 3 Launch End: 2026-06-30 (4 месяца total)

**Capacity:** 
- Phase 1: 10-12 часов/неделю (MVP focus)
- Phase 2: 8-10 часов/неделю (beta feedback)
- Phase 3: 12-15 часов/неделю (GTM push)
- Total: 200-300 часов

**WIP Decision:** Allow with condition
- If current WIP = 2 → Allow (станет 3-й)
- If current WIP = 3 → Defer one existing project (score <3.5) before start
- Action: Verify WIP before 2026-03-01 start date

## Stage Gate: Plan Readiness

**Gate Decision:** Proceed (conditional on WIP)
**DoD Checklist:** Met
- ✅ Integration summary complete
- ✅ WIP decision confirmed (conditional allow)
- ✅ Resources and timeline agreed
- ✅ Dependencies identified

**Notes:** Proceed to Calendar Sync and Deep Plan. Verify WIP status before 2026-03-01 start date. If WIP=3, defer lower-priority project first.


## Calendar Sync

**Start Date:** 2026-03-01
**End Date (MVP):** 2026-04-30
**End Date (Launch):** 2026-06-30
**Capacity:** 10-12 hours/week (Phase 1), 8-10h/week (Phase 2), 12-15h/week (Phase 3)

**Milestones:**
1. **2026-03-01** - Project Kickoff: Infrastructure setup, ВК API research
2. **2026-03-15** - Week 2: Webhook system + basic flow engine prototype
3. **2026-04-01** - Month 1: Visual flow builder MVP (5 templates)
4. **2026-04-15** - Week 6: Beta testing start (10-20 users)
5. **2026-04-30** - Phase 1 Complete: MVP ready (100 beta signups target)
6. **2026-05-31** - Phase 2: Drag-and-drop UI + 3 CRM integrations + analytics
7. **2026-06-30** - Phase 3 Launch: Marketplace + white-label + Product Hunt

**Files Created:**
- Project: `projects/idea-004-vk-bot.md`
- Snapshot: `snapshots/idea-004-vk-bot.md`
- Journal: `journal/idea-004-vk-bot.md`
- Plan: `plans/idea-004-vk-bot-plan.md`
- Decisions: `decisions/idea-004-decisions.md`


## Deep Plan (L1-L6)

**Status:** COMPLETE (2026-02-05)
**Planning Mode:** Tech Product Development (Serverless SaaS)

### Summary
- **L1:** Solo Founder & Full-Stack Developer - создание self-hosted Salebot альтернативы
- **L2:** 3 contribution areas (Product Strategy & UX, Technical Development, GTM & Growth)
- **L3:** 9 work streams across 3 areas
- **L4-L6:** Full depth structure with atomic actions

**Quality Metrics:**
- Depth: 6/6 levels = 100% ✅
- RACI Coverage: 3/3 L2 nodes = 100% ✅
- If-Then Actions: 4 (target ≥2) ✅
- Quality Gate: **PASS**

**Full Plan:** See `plans/idea-004-vk-bot-plan.md` for complete L1-L6 structure

**Key If-Then Actions:**
1. API ВК changes → monitoring alert + fallback + 24h notification
2. Rate limit exceeded → queue system (BullMQ) + exponential backoff
3. Unit-economics >5K₽/1000 users → optimize Lambda config + hybrid cloud
4. "10 min to first bot" not achieved → simplify onboarding + interactive tutorial

