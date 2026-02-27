# Resource Assessment Examples & Templates

This document contains detailed examples, case studies, and templates for Step 0.6 (Resource Assessment).

## Complete Speed Multiplier Examples

### Example 1: Solo Developer + LLM (10x-20x)

**Scenario:** Solo developer using Claude Code for auto-responder service

**Resources:**
- Developer: 1 full-time (40 hrs/week)
- AI: Claude Code (80% code generation)
- No-code: Supabase (backend), Vercel (hosting)
- Existing: 0% (greenfield)

**Speed Calculation:**
```
Base Multiplier: 10x (LLM-assisted solo)
+ No-code tools (Supabase + Vercel): +5x
+ Infrastructure ready (CI/CD): +2x
- Budget constraint (minimal): -1x
= FINAL: 16x

Traditional: 8-12 weeks → Actual: 0.5-0.75 weeks (3-5 DAYS)
```

**Outcome:** Auto-responder completed in 3-5 days vs 2-4 months traditional

---

### Example 2: Team + LLM + Existing Codebase (30x-50x)

**Scenario:** Team of 3 devs building Katana consulting matching platform

**Resources:**
- Team: 3 full-time devs
- AI: Claude Code + Cursor AI
- No-code: Airtable (data), Webflow (landing)
- Existing: 40% codebase reusable (auth, UI components)

**Speed Calculation:**
```
Base Multiplier: 30x (team + LLM)
+ Existing code (40% reusable): +8x
+ No-code tools: +5x
+ Design system ready: +3x
- Coordination overhead (3 people): -4x
= FINAL: 42x

Traditional: 12 weeks → Actual: 0.29 weeks (2-3 DAYS)
```

**Outcome:** Katana completed in 3-4 weeks vs 12 weeks traditional

---

### Example 3: Hybrid (LLM + No-Code + Existing) (50x-100x)

**Scenario:** Enterprise integration with existing infrastructure

**Resources:**
- Team: 2 devs + 1 architect
- AI: GPT-4 + GitHub Copilot
- No-code: Zapier (integrations), Notion (docs), Airtable (CRM)
- Existing: 70% infrastructure (APIs, auth, DB, CI/CD)

**Speed Calculation:**
```
Base Multiplier: 40x (team + LLM + no-code)
+ Existing infrastructure (70%): +20x
+ API integrations ready: +10x
+ DevOps automation: +5x
- Legacy integration complexity: -8x
- Compliance constraints (GDPR): -5x
= FINAL: 62x

Traditional: 24 weeks → Actual: 0.39 weeks (3 DAYS)
```

---

## Speed Multiplier Matrix

| Development Method | Base | +Existing | +No-Code | +Team | -Constraints | Final Range |
|-------------------|------|-----------|----------|-------|--------------|-------------|
| **A: LLM Solo** | 10x | +2-5x | +2-5x | - | -1-3x | 8-17x |
| **B: Traditional** | 1x | +0-1x | - | +0-2x | -0-1x | 1-3x |
| **C: No-Code Only** | 5x | +1-3x | - | +1-2x | -1-2x | 4-9x |
| **D: Hybrid (All)** | 20x | +10-30x | +5-15x | +5-10x | -5-10x | 35-75x |

---

## Constraint Examples & Mitigation

### Budget Constraints

**Limited Budget (<$1000)**
- Impact: -1x to -3x (fewer tools, slower iteration)
- Mitigation:
  - Use free tiers (Supabase, Vercel, Railway)
  - Focus on open-source tools
  - Leverage LLM for faster development (saves time = saves money)

**Medium Budget ($1000-$10,000)**
- Impact: Neutral (0x)
- Access: Paid APIs, premium no-code tools, monitoring

**High Budget (>$10,000)**
- Impact: +2x to +5x (parallel experimentation, premium tools)
- Access: Enterprise tools, multiple developers, DevOps automation

---

### Time Constraints

**Critical Deadline (<2 weeks)**
- Impact: -2x to -5x (quality trade-offs, technical debt)
- Mitigation:
  - Reduce scope to MVP
  - Use pre-built templates
  - Accept technical debt (plan refactor later)

**Important (2-8 weeks)**
- Impact: -1x (some pressure but manageable)
- Sweet spot for quality + speed

**Flexible (>8 weeks)**
- Impact: +1x to +2x (time for optimization, refactoring)

---

### Team Constraints

**Solo Developer**
- Impact: Neutral (baseline 10x with LLM)
- Pros: No coordination overhead, fast decisions
- Cons: Limited capacity, single point of failure

**Small Team (2-3 devs)**
- Impact: +5x to +10x (parallel work, code review)
- Optimal for most projects
- Coordination overhead minimal (<10% time)

**Large Team (4+ devs)**
- Impact: +10x to +20x BUT -5x to -10x coordination
- Net: +5x to +10x (diminishing returns)
- Only worth it for large, complex projects

---

### Technical Constraints

**Legacy Integration**
- Impact: -2x to -8x (reverse engineering, adapter code)
- Mitigation:
  - Use API wrappers
  - Isolate legacy in separate module
  - Consider gradual migration

**Compliance (GDPR, HIPAA, SOC2)**
- Impact: -3x to -10x (additional testing, documentation, audits)
- Mitigation:
  - Use compliant platforms (AWS, GCP)
  - Leverage compliance frameworks
  - Budget extra time for audit prep

**Platform-Specific (iOS, Android, Desktop)**
- Impact: -1x to -3x per additional platform
- Mitigation:
  - Use cross-platform frameworks (React Native, Flutter)
  - Web-first approach (PWA)
  - Prioritize single platform first

---

## Asset Inventory Templates

### Existing Codebase Assessment

**Completion Scale:**
- 0-20%: Greenfield (minimal reuse, -0x bonus)
- 20-40%: Early stage (+2x bonus from auth, DB, UI foundation)
- 40-60%: Mid-stage (+5x bonus from core features ready)
- 60-80%: Advanced (+10x bonus from most features complete)
- 80-100%: Near-complete (+20x bonus from minor additions only)

**Reusability Checklist:**
- [ ] Authentication & authorization
- [ ] Database schema & migrations
- [ ] UI component library / design system
- [ ] API integrations (payment, email, analytics)
- [ ] Test suite & CI/CD pipeline
- [ ] Documentation & setup scripts

---

### Design System Inventory

**Ready Assets:**
- [ ] Component library (buttons, forms, modals)
- [ ] Design tokens (colors, spacing, typography)
- [ ] Layout templates (dashboard, landing, auth)
- [ ] Icon set
- [ ] Brand guidelines

**Impact:**
- Full design system: +3x to +5x (no design work needed)
- Partial system: +1x to +2x (some design reuse)
- No system: -0x (start from scratch)

---

### API Integration Inventory

**Pre-Integrated Services:**
- [ ] Authentication (Auth0, Clerk, Supabase Auth)
- [ ] Payment (Stripe, PayPal)
- [ ] Email (SendGrid, Mailgun, Resend)
- [ ] Analytics (PostHog, Mixpanel, Google Analytics)
- [ ] Monitoring (Sentry, LogRocket)
- [ ] Storage (S3, Cloudinary)

**Impact per integration:**
- Each ready integration: +0.5x to +1x
- 5+ integrations: +3x to +5x

---

## Speed Multiplier Calculation Worksheet

**Step 1: Base Multiplier**
```
Development Method: [A / B / C / D]
Base Multiplier: ___x

A: LLM-assisted (10x-20x)
B: Traditional (1x)
C: No-code (5x-20x)
D: Hybrid (20x-100x)
```

**Step 2: Positive Adjustments**
```
+ Existing codebase (___% reusable): +___x
+ No-code tools (list: _______): +___x
+ Team size (___devs): +___x
+ Infrastructure ready (CI/CD, cloud, monitoring): +___x
+ Design system: +___x
+ API integrations (count: ___): +___x

TOTAL POSITIVE: +___x
```

**Step 3: Constraint Penalties**
```
- Budget limited: -___x
- Time limited: -___x
- Team coordination overhead: -___x
- Skill gaps: -___x
- Legacy integration: -___x
- Compliance requirements: -___x

TOTAL PENALTIES: -___x
```

**Step 4: Final Calculation**
```
Base: ___x
+ Positive Adjustments: +___x
- Constraint Penalties: -___x
= FINAL SPEED MULTIPLIER: ___x
```

**Step 5: Timeline Impact**
```
Traditional Estimate: ___ weeks
÷ Speed Multiplier: ___x
= Realistic Timeline: ___ weeks

Time Saved: ___ weeks
Acceleration Factor: ___x faster
```

---

## Real-World Case Studies

### Case Study 1: SaaS Dashboard (Supabase + React)

**Project:** Admin dashboard for SaaS product

**Traditional Approach:**
- Manual backend API (Express + PostgreSQL): 4 weeks
- Manual frontend (React components): 3 weeks
- Auth implementation: 1 week
- Testing & deployment: 2 weeks
- **Total: 10 weeks**

**LLM-Assisted Approach:**
- Supabase backend (no-code): 2 days
- Claude Code generates React dashboard: 3 days
- Supabase Auth (pre-built): 1 day
- Vercel deployment: 1 hour
- **Total: 6 days (0.86 weeks)**

**Speed Multiplier: 11.6x**

**Resources Used:**
- Claude Code (LLM)
- Supabase (no-code backend)
- Vercel (no-code deployment)
- Existing: React boilerplate (10%)

---

### Case Study 2: E-commerce MVP (Shopify + Custom)

**Project:** Custom e-commerce with unique checkout flow

**Traditional Approach:**
- Custom backend: 6 weeks
- Frontend + checkout: 4 weeks
- Payment integration: 2 weeks
- Inventory system: 2 weeks
- **Total: 14 weeks**

**Hybrid Approach:**
- Shopify base (no-code): 1 day
- Custom checkout with LLM: 5 days
- Stripe integration (pre-built): 1 day
- Inventory via Airtable: 2 days
- **Total: 9 days (1.3 weeks)**

**Speed Multiplier: 10.8x**

**Resources Used:**
- Shopify (no-code platform)
- Claude Code (custom checkout)
- Airtable (no-code inventory)
- Stripe (API integration)

---

## Optimization Tips

### Maximizing Speed Multiplier

**1. Leverage No-Code for Non-Differentiating Features**
- Backend: Supabase, Firebase, Airtable
- Frontend: Webflow, Bubble (for simple sites)
- Integrations: Zapier, Make
- Hosting: Vercel, Netlify (zero-config)

**2. Use LLM for Custom Logic**
- Business logic unique to your product
- Complex algorithms
- Custom integrations
- Performance-critical code

**3. Reuse Everything Possible**
- Start with boilerplates (Next.js, T3 stack)
- Use component libraries (shadcn/ui, Material-UI)
- Leverage templates (Tailwind UI, Chakra)

**4. Parallel Work with Team**
- Split features across developers
- Use LLM to maintain consistency
- Daily syncs to avoid conflicts

**5. Accept Technical Debt for MVP**
- Ship fast, refactor later
- 80% good code > 100% perfect code delayed
- Use LLM to refactor incrementally

---

## Common Mistakes

### Mistake 1: Assuming Traditional Speed (1x)

**Problem:** Planning as if manually coding without LLM

**Fix:** Always calculate Speed Multiplier first

**Impact:** Timeline off by 10x-50x

---

### Mistake 2: Ignoring Existing Assets

**Problem:** Not assessing what's already done

**Fix:** Run Step 0.5 (Project Stage Discovery) first

**Impact:** Wasted time rebuilding existing code

---

### Mistake 3: Overestimating Team Coordination

**Problem:** Thinking 5 devs = 5x speed

**Fix:** Account for -20% to -40% coordination overhead

**Impact:** Delays, communication bottlenecks

---

### Mistake 4: Underestimating Constraints

**Problem:** Not factoring in compliance, legacy, deadlines

**Fix:** Document all constraints, apply realistic penalties

**Impact:** Missed deadlines, scope creep

---

## References

**Data Sources:**
- `../data/speed-multipliers.yaml` (detailed multiplier values)
- Step 0.5: Project Stage Discovery (completion % assessment)
- Step 0.7: Optimization Intelligence (optimal approaches)

**Related Steps:**
- Step 0.5: What exists and works (baseline completion)
- Step 0.6: Resource Assessment (this step)
- Step 0.7: Optimal tech stack suggestions
- Step 08: Timeline calculation (uses Speed Multiplier)

**External Resources:**
- Claude Code documentation: https://docs.anthropic.com
- Supabase speed case studies: https://supabase.com/case-studies
- No-code tool comparisons: Zapier, Make, Bubble, Webflow

---

**Last Updated:** 2026-02-06
**Version:** 1.0
**Purpose:** Support Step 0.6 Resource Assessment with detailed examples and templates
