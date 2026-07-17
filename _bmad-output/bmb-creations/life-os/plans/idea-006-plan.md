# Project Plan: Consilium SaaS Assistant

**Project ID:** idea-006
**Status:** PLANNED
**Score:** 3.65/5.0 (73%)
**Strategic Bucket:** Growth / New Revenue Streams

---

## Idea Summary

**Title:** Универсальный SaaS ассистент-консилиум

**Domain:** бизнес/софт/личное/AI

**Description:** Multi-modal AI assistant with structured consilium methodology (Six Hats, TRIZ, MCDA) for meetings, task management, and life advisory. Positioned as "Personal Board of Advisors" vs generic AI assistants.

**MVP Scope (2 modes):**
1. **Meeting Moderator** - Live transcription + real-time framework suggestions
2. **Task Distributor** - Six Hats + TRIZ for project planning

**Business Model:**
- Freemium: 10 requests/day, basic modes (free)
- Pro tier: $15/month (unlimited, all modes, priority support)
- Team tier: $10/month/user (min 5 seats)

---

## Consilium Summary (Six Hats)

**Specialists Consulted:** Market Analyst, Finance Analyst, Creative Director, Product Strategist, Growth / GTM

**Key Insights:**
- ⚪ **Facts:** TAM $15.7B, competitors at $10-34/month, LTV:CAC 5.6:1 healthy
- 🔴 **Intuition:** Strong concept but must avoid "mediocre everywhere" trap
- ⚫ **Risks:** API cost spiral ($50-150k/month at 10k users), PMF uncertainty
- 🟡 **Benefits:** All-in-one value, consilium effect, premium positioning $15-30/month
- 🟢 **Creativity:** Specialist personas UI, workflow templates marketplace, modular modes
- 🔵 **Process:** 18-week plan (MVP 12w, Beta 4w, Launch 2w), metrics: Week 1 retention >40%

**Consensus:** GO with conditions (narrow MVP, beta validation required)

---

## Scoring Summary

**MCDA Criteria (weighted 1.0):**
- Impact: 4/5 (0.15) = 0.60
- Confidence: 3/5 (0.10) = 0.30
- Effort: 4/5 (0.10) = 0.40
- Strategic Alignment: 5/5 (0.10) = 0.50
- Risk: 3/5 (0.10) = 0.30
- Market Opportunity: 4/5 (0.10) = 0.40
- Competitive Advantage: 3/5 (0.10) = 0.30
- Expected Value: 3/5 (0.15) = 0.45
- Option Value: 4/5 (0.10) = 0.40

**Overall Score:** 3.65/5.0 (73%)

**Decision Rationale:** High strategic alignment (5/5) + strong impact (4/5) compensate for moderate confidence (3/5). PROCEED with beta validation condition.

---

## Integration Summary

**Strategic Bucket:** Growth / New Revenue Streams (new SaaS product, recurring revenue potential)

**Integration Pattern:** Standalone (minimal dependencies, potential Platform Extension future)

**Portfolio Health:** Moderate imbalance (57% Business/Tech projects), but unique (SaaS = long-term asset)

**BMAD Workflow:** Product Brief → Dev Story → TestArch (start now before development)

**WIP Decision:** CONDITIONAL ALLOW (must verify WIP < 2)

---

## Calendar Sync

**Start Date:** 2026-03-01 (conditional on WIP check)
**End Date:** 2026-07-15
**Duration:** 18 weeks (~4.5 months)
**Capacity:** 15-20 hours/week (part-time baseline, full-time Weeks 5-12)

**Milestones:**
1. **Product Brief Complete** - 2026-03-08 (Week 1)
2. **Infrastructure Ready** - 2026-03-22 (Week 3-4)
3. **Mode 1 (Meeting Moderator) Live** - 2026-04-26 (Week 8)
4. **Mode 2 (Task Distributor) Live** - 2026-05-24 (Week 12)
5. **Beta Testing Complete** - 2026-06-21 (Week 16)
6. **Public Launch** - 2026-07-05 (Week 18)

---

## Deep Plan (L1-L6)

### L1: Mission/Role
```
Launch Consilium SaaS MVP as Product Owner & Technical Lead
```

**Success Criteria:**
- MVP live with 2 modes by Week 12
- 50-100 beta users acquired
- >40% Week 1 retention achieved

---

### L2: Contribution Areas (5 phases)

```
L2.1: Product Definition & Strategy (Weeks 1-2)
  RACI: R=Self, A=Self, C=Product Strategist, I=Market Analyst

L2.2: Technical Foundation (Weeks 3-4)
  RACI: R=Self, A=Self, C=Production Lead, I=Operations Lead

L2.3: Core Features Build (Weeks 5-12)
  RACI: R=Self, A=Self, C=Creative Director, I=Finance Analyst

L2.4: Beta Launch & Validation (Weeks 13-16)
  RACI: R=Self, A=Self, C=Growth/GTM, I=Market Analyst

L2.5: Public Launch & Scale (Weeks 17-18)
  RACI: R=Self, A=Self, C=Growth/GTM, I=All stakeholders
```

---

### L3: Work Streams

**L2.1: Product Definition & Strategy**
- L3.1.1: MVP Scope & Feature Definition
- L3.1.2: Competitive Positioning & Differentiation
- L3.1.3: Pricing & Business Model Validation

**L2.2: Technical Foundation**
- L3.2.1: Infrastructure Setup (AWS/Vercel)
- L3.2.2: Auth & User Management
- L3.2.3: AI API Integration (OpenAI/Anthropic)

**L2.3: Core Features Build**
- L3.3.1: Mode 1 - Meeting Moderator (Weeks 5-8)
- L3.3.2: Mode 2 - Task Distributor (Weeks 9-12)
- L3.3.3: Dashboard & Billing

**L2.4: Beta Launch & Validation**
- L3.4.1: Beta User Recruitment (50-100 users)
- L3.4.2: Metrics Tracking & Feedback Loop
- L3.4.3: Iteration & Refinement

**L2.5: Public Launch & Scale**
- L3.5.1: Product Hunt Launch Campaign
- L3.5.2: Content Marketing (Twitter/LinkedIn)
- L3.5.3: Monitoring & Optimization

---

### L4: Stages (Example: L3.3.1 Mode 1)

**L3.3.1: Mode 1 - Meeting Moderator**
```
L4.1: Design (Week 5)
  - User flows for live meeting capture
  - UI mockups for transcription display
  - Framework suggestion UI (Six Hats indicators)

L4.2: Backend Dev (Weeks 6-7)
  - Real-time audio transcription (Whisper API)
  - Framework detection logic (keyword matching)
  - Meeting session storage

L4.3: Frontend Dev (Week 7)
  - Live transcript UI component
  - Framework suggestion cards
  - Export meeting notes

L4.4: Testing (Week 8)
  - Unit tests (backend logic)
  - Integration tests (API calls)
  - User acceptance testing (5 beta users)

L4.5: Deploy (Week 8)
  - Staging environment deploy
  - Production deploy with feature flag
```

---

### L5: Tasks (Example: L4.1 Design)

**L4.1: Design (Mode 1)**
```
L5.1: Sketch user flows (Day 1)
L5.2: Create UI mockups in Figma (Days 2-3)
L5.3: Define framework suggestion triggers (Day 4)
L5.4: Design export templates (Day 5)
L5.5: User testing prototype (5 users, Day 5)
```

---

### L6: Atomic Actions (Example: L5.2 Figma)

**L5.2: Create UI mockups in Figma**
```
L6.1: Create new Figma project "Consilium - Mode 1"
L6.2: Design main canvas component (transcript stream)
L6.3: Design framework suggestion card component
L6.4: Design meeting controls toolbar
L6.5: Create mobile responsive variants
L6.6: Export assets for dev handoff
```

---

### Plan Quality Metrics

**Depth Covered:** 6/6 (100%) ✅
- L1: Mission defined
- L2: 5 phases with RACI
- L3: 13 work streams
- L4: 5 stages per critical stream (example shown)
- L5: 5 tasks per stage (example shown)
- L6: 6 atomic actions per task (example shown)

**Nodes Count:** ~150+ nodes (full expansion)
- L1: 1 node
- L2: 5 nodes
- L3: 13 nodes
- L4: ~30 nodes (5 stages × 6 streams estimated)
- L5: ~100 nodes (5 tasks × 20 stages estimated)
- L6: ~500+ actions (not all expanded here)

**RACI Coverage:** 5/5 = 100% ✅
- All L2 phases have R (Self) and A (Self) defined
- Consulted (C) and Informed (I) roles mapped to consilium specialists

**If-Then Coverage:** 4 scenarios defined ✅

### If-Then Actions (Contingencies)

**IF-THEN 1: API Cost Spike**
- **Trigger:** Weekly API spend >$5k for 2 consecutive weeks
- **Action:**
  1. Analyze high-cost operations (which mode, which users)
  2. Implement cheaper model fallback (GPT-3.5 for non-critical)
  3. Add usage caps per user (Pro tier: 1000 requests/month)
  4. Re-evaluate pricing ($15 → $20/month if needed)

**IF-THEN 2: Low Beta Retention (<40% Week 1)**
- **Trigger:** Beta Week 1 retention below 40% threshold
- **Action:**
  1. User interviews with churned users (why they stopped)
  2. Identify top 3 friction points
  3. Sprint to fix critical issues (1-2 weeks)
  4. Re-launch beta with fixes before public launch

**IF-THEN 3: Feature Creep Request**
- **Trigger:** Stakeholder/user requests 3rd mode during MVP
- **Action:**
  1. Politely defer: "Great idea, we'll consider for v1.1"
  2. Document request in backlog
  3. Stay focused on 2-mode MVP
  4. Re-evaluate after launch based on metrics

**IF-THEN 4: Technical Blocker (AI API Down)**
- **Trigger:** OpenAI/Anthropic API unavailable for >1 hour
- **Action:**
  1. Switch to backup provider (if down is provider-specific)
  2. Display graceful error to users ("Service temporarily unavailable")
  3. Queue requests for retry when API back online
  4. Communicate proactively to beta users

---

### Quality Gate: Deep Plan Completeness

**Gate Criteria:**
- ✅ L1-L4 present (100% depth covered)
- ✅ RACI Coverage ≥70% (achieved 100%)
- ✅ If-Then Coverage ≥2 (achieved 4)

**Gate Decision:** ✅ PASS - Plan is execution-ready

---

## Critical Success Metrics

**Beta Phase:**
- Week 1 retention: >40%
- Month 1 retention: >20%
- Beta users: 50-100

**Launch Phase:**
- Target: 100 paying users by Month 3
- MRR: $1,500 by Month 3
- LTV:CAC ratio: >3:1

**Financial Guardrails:**
- Max API spend: $5k/month in MVP phase
- Break-even target: Month 12 ($15k MRR)
- Track API costs weekly (alert if >$5k/month)

---

## Next Steps

1. **IMMEDIATE:** Verify current WIP count
   - If WIP < 2: Proceed to Deep Plan (optional) or Complete
   - If WIP ≥ 2: Defer project
2. **WHEN READY TO START:**
   - Run Product Brief workflow (2-3 hours)
   - Generate Deep Plan L1-L6 (optional, ~1 hour)
   - Set up weekly API cost tracking
3. **Week 1:** Complete Product Brief, begin infrastructure setup
