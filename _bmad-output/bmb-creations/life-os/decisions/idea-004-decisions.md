---
projectId: idea-004
---

# Decision Log: Бот для ВК (аналог Salebot)

## 2026-02-05 — Calendar Sync Decision

**Context:** Portfolio Integration complete, timeline planning

**Decision:**
- Start Date: 2026-03-01 (conditional on WIP check)
- MVP: 2026-04-30 (2 months)
- Launch: 2026-06-30 (4 months total)
- Capacity: 10-12 hours/week (Phase 1)

**Rationale:**
- 2 months MVP realistic based on 80-120 hours estimate + serverless simplicity
- 4 months to launch aligns with 3-phase consilium plan (MVP → Beta → Launch)
- 10-12h/week sustainable capacity for Growth/Innovation project
- Start date allows 3-4 weeks for Deep Plan completion

**Alternatives Considered:**
- Shorter MVP (1 month): Rejected - too aggressive for quality UX
- Longer MVP (3 months): Rejected - market timing risk (Salebot may adapt)

---

## 2026-02-05 — Integration Decision

**Context:** Portfolio Integration, scoring 3.90/5.00 complete

**Decision:**
- Bucket: Growth / Innovation
- Pattern: Standalone Product
- WIP: Conditional allow (verify <3 before start)

**Rationale:**
- Score 3.90/5.00 justifies prioritization in Growth bucket
- Standalone pattern: greenfield product, own infrastructure/GTM
- WIP conditional: balance portfolio, avoid overload

**Alternatives Considered:**
- Platform Extension: Rejected - not extending existing platform
- Bundle: Rejected - standalone SaaS, not bundled with others
- Immediate start: Rejected - need WIP verification first

---

## 2026-02-05 — Scoring Decision

**Context:** Consilium complete, MCDA scoring needed

**Decision:** Score 3.90 / 5.00 (78%), Gate Decision: Proceed

**Rationale:**
- High impact (4/5) and market opportunity (4/5) compensate moderate confidence (3/5)
- Competitive advantage (4/5) strong: self-hosted + white-label unique
- Risk (3/5) manageable with mitigation plan
- Score >70% threshold for proceeding

**Alternatives Considered:**
- Defer: Rejected - score sufficient, market timing important
- Rescore with different weights: Rejected - current weights balanced

---

## 2026-02-05 — Consilium Decision

**Context:** Specialist matching complete, Deep consilium mode

**Decision:**
- Mode: Deep (4 specialists + Six Thinking Hats)
- Positioning: Self-hosted + privacy-first + API-first
- Architecture: Serverless (AWS Lambda), multi-tenant + self-hosted hybrid
- UX: "10 minutes to first bot", drag-and-drop like Figma
- Risk mitigation: API monitoring, rate limiting day 1, GDPR consultant Phase 2

**Rationale:**
- 2 high-priority roles (Product Strategist, Backend Architect) warrant Deep mode
- Six Hats balanced perspectives (facts, risks, benefits, creativity, process)
- Consensus alignment on self-hosted positioning (unique vs Salebot)
- Serverless reduces unit-economics risk (<5K₽/мес per 1000 users)

**Alternatives Considered:**
- Lite consilium: Rejected - complexity warrants Deep mode
- Cloud-only (like Salebot): Rejected - no differentiation
- On-premise only: Rejected - limits market (SaaS + self-hosted hybrid better)

---

## 2026-02-05 — Specialist Match Decision

**Context:** Roles discovery complete, need specialist mapping

**Decision:**
- Product Strategist (high)
- Backend Architect (high)
- Market Analyst (medium)
- Operations Lead (medium)
- Creative Director (medium)

**Rationale:**
- 2 high-priority: strategy (positioning vs Salebot) + tech (API integration)
- Market Analyst critical for competitive analysis (Salebot, Senler, MessageBot)
- Operations for production-readiness (хостинг, CI/CD)
- Creative for UX differentiation ("like Figma")

**Alternatives Considered:**
- Separate Skill Development role: Rejected - merged into Backend Architect (avoid duplication)
- Add Security role: Deferred to Deep Plan (GDPR handled by consultant Phase 2)

---

## 2026-02-05 — Roles Discovery Decision

**Context:** Idea captured (idea-004), need role identification

**Decision:**
- Spheres: business, career, creative
- Roles: Product Strategist (high), Market Analyst (medium), Operations Lead (medium), Skill Development (medium), Creative Director (medium)

**Rationale:**
- Business sphere: SaaS product needs strategy, market analysis, operations
- Career sphere: skill development (API ВК, webhook, visual builder)
- Creative sphere: UX design critical for "10 min to first bot" goal

**Alternatives Considered:**
- Add Finance sphere: Rejected - premature (unit-economics validation in MVP)
- Add Legal sphere: Deferred to Phase 2 (GDPR consultant)
