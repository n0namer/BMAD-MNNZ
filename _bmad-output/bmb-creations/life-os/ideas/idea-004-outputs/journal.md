---
projectId: idea-004
---

# Project Journal: Бот для ВК (аналог Salebot)

## 2026-02-05 - Calendar Sync Complete

**Decision:** Approved timeline with 3 phases (MVP → Beta → Launch)

**Key Points:**
- Start: 2026-03-01 (conditional on WIP check)
- MVP: 2026-04-30 (2 months, 80-120 hours)
- Launch: 2026-06-30 (4 months total, 200-300 hours)
- Capacity: 10-12 hours/week initially

**Milestones Defined:**
1. 2026-03-01 - Kickoff
2. 2026-03-15 - Webhook prototype
3. 2026-04-01 - Visual builder MVP
4. 2026-04-15 - Beta testing start
5. 2026-04-30 - MVP complete (100 beta signups)
6. 2026-05-31 - Drag-and-drop UI + CRM integrations
7. 2026-06-30 - Marketplace + Product Hunt launch

**Next:** Deep Plan (Step 8) to structure L1-L6 execution plan

---

## 2026-02-05 - Integration Complete

**Decision:** Standalone Product in Growth/Innovation bucket, conditional WIP allow

**Rationale:**
- Score 3.90/5.00 justifies prioritization
- Self-hosted positioning differentiates from Salebot
- Serverless reduces infrastructure complexity and cost
- API-first enables future platform extensions

**Condition:** Verify WIP <3 before start. If WIP=3, defer lower-priority project.

**Dependencies Identified:**
- External: ВК API (stable)
- Infrastructure: AWS Lambda / Cloud Functions
- Optional: CRM APIs (Phase 2)

---

## 2026-02-05 - Scoring Complete

**Score:** 3.90 / 5.00 (78%)

**Breakdown:**
- Impact: 4/5 - Strong market potential (25-50K users)
- Confidence: 3/5 - Moderate (API known, UX uncertainty)
- Effort: 3/5 - Medium (200-300 hours)
- Strategic Alignment: 4/5 - Good fit (skills, portfolio)
- Risk: 3/5 - Moderate (API changes, competition)
- Market Opportunity: 4/5 - Existing market with pain
- Competitive Advantage: 4/5 - Strong (self-hosted, privacy)

**Gate Decision:** Proceed (score >70%)

---

## 2026-02-05 - Consilium Complete

**Mode:** Deep (4 specialists: Product Strategist, Market Analyst, Operations Lead, Creative Director, Backend Architect)

**Six Thinking Hats Applied:**
- ⚪ White (Facts): Market 500K+ сообществ ВК, Salebot 15K users, 990₽/мес
- 🔴 Red (Intuition): "Как в Figma" drag-and-drop критично для adoption
- ⚫ Black (Risks): API changes, rate limits, unit-economics, GDPR
- 🟡 Yellow (Benefits): Open-source, self-hosted, API-first, white-label
- 🟢 Green (Creativity): Serverless, AI-подсказки, template marketplace
- 🔵 Blue (Process): 3 phases (MVP → Beta → Launch), KPI defined

**Consensus:**
1. Positioning: Self-hosted + privacy-first + API-first
2. Architecture: Serverless (AWS Lambda), multi-tenant + self-hosted hybrid
3. UX: "10 minutes to first bot", drag-and-drop like Figma
4. Risk mitigation: API monitoring, rate limiting, GDPR consultant Phase 2

---

## 2026-02-05 - Specialist Match Complete

**Selected:**
- Product Strategist (high) - positioning vs Salebot
- Market Analyst (medium) - competitive analysis
- Operations Lead (medium) - infrastructure planning
- Creative Director (medium) - UX visual flow builder
- Backend Architect (high) - API integration, webhook system

**Rationale:** 2 high-priority roles (strategy + tech), Operations for production-readiness, Creative for competitive UX

---

## 2026-02-05 - Roles Discovery Complete

**Spheres:** business, career, creative

**Roles Identified:**
- Product Strategist (high)
- Market Analyst (medium)
- Operations Lead (medium)
- Skill Development (medium) → merged into Backend Architect
- Creative Director (medium)

**Focus:** Positioning against Salebot, technical feasibility, UX differentiation
