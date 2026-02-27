# Resource Assessment Examples & Templates

## Speed Multiplier Detailed Examples

### Example 1: Solo LLM Development (10x-20x)

**Setup:**
- Developer: 1 solo founder
- Tools: Claude Code
- Codebase: Greenfield (0% reuse)
- No-code: None

**Calculation:**
- Base: LLM-assisted solo = 10x
- Adjustments: None
- Penalties: None
- **Final: 10x**

**Real-world:**
- Traditional task: 2 weeks manual coding
- With Claude: 1.4 days (14-16 hours)
- Time saved: 12.6 days

---

### Example 2: Team + LLM Hybrid (20x-50x)

**Setup:**
- Team: 2 developers (full-time)
- Tools: Claude Code + GitHub Copilot
- Codebase: 30% reusable
- No-code: Supabase (backend), Vercel (hosting)

**Calculation:**
- Base: LLM-assisted team = 20x
- Adjustments:
  - Existing code (30%): +2x
  - No-code (Supabase): +5x
  - Team size (2): +3x
- Penalties: None
- **Subtotal: 20 + 2 + 5 + 3 = 30x**
- **Final: 30x**

**Real-world (Автоответчик):**
- Traditional: 12 weeks (manual Python + React + backend)
- With setup above: 0.4 weeks = **2-3 DAYS**
- Time saved: 11.6 weeks

---

### Example 3: Optimal Setup (50x-100x)

**Setup:**
- Team: 3 developers (full-time) + 1 designer
- Tools: Claude Code + Cursor AI + v0.dev (UI generation)
- Codebase: 60% reusable (existing base)
- No-code: Supabase + Vercel + Zapier + existing CI/CD

**Calculation:**
- Base: LLM-assisted team = 20x
- Adjustments:
  - Existing code (60%): +5x
  - No-code stack: +10x
  - Team size (3): +5x
  - Infrastructure ready: +10x
- Penalties: None
- **Subtotal: 20 + 5 + 10 + 5 + 10 = 50x**
- **Final: 50x**

**Real-world (Katana Epic L):**
- Traditional: 12 weeks (manual Python + backtesting framework)
- With setup above: 0.24 weeks = **1.5-2 DAYS**
- Time saved: 11.75+ weeks

---

### Example 4: Constrained Setup (5x with penalties)

**Setup:**
- Developer: 1 solo (part-time, 10 hours/week)
- Tools: GitHub Copilot (no full LLM coding assistant)
- Codebase: Greenfield
- No-code: None
- Budget: Minimal ($0)

**Calculation:**
- Base: Traditional with Copilot = 2x
- Adjustments: None
- Penalties:
  - Time limited (part-time): -1x
  - Budget limited: -1x
  - Skill gaps (no DevOps): -1x
- **Subtotal: 2 - 1 - 1 - 1 = -1x (floor to 1x)**
- **Final: 1x** (traditional speed)

**Real-world:**
- Traditional: 12 weeks
- With constraints: 12 weeks (no acceleration)
- Time saved: 0 weeks

**Recommendation:** Invest in LLM tools (Claude Code) to unlock 10x+ multiplier.

---

## Constraint Analysis Details

### Budget Constraints

| Budget Level | Impact | Mitigation |
|--------------|--------|------------|
| **Unlimited** | No penalty | Full stack available |
| **Medium ($500-2000)** | -0.5x | Use free tiers, prioritize key tools |
| **Minimal ($0-100)** | -1x to -2x | Free tools only, slower iteration |

**Mitigation strategies:**
- Use free tier of Supabase, Vercel, Railway
- Claude Code with API key ($20/month) = 10x ROI
- Open-source alternatives to paid tools

---

### Time Constraints

| Availability | Impact | Mitigation |
|--------------|--------|------------|
| **Full-time (40+ hrs/week)** | No penalty | Optimal velocity |
| **Part-time (20-30 hrs/week)** | -0.5x | Batch tasks, async workflows |
| **Weekends only (10-15 hrs/week)** | -1x | Longer timeline, smaller scope |

**Mitigation strategies:**
- Use background workers (CI/CD, automated tests)
- Async communication (GitHub Issues, PRs)
- Pre-commit hooks to reduce manual checks

---

### Skill Gap Constraints

| Gap Type | Impact | Mitigation |
|----------|--------|------------|
| **None (full-stack)** | No penalty | Independent execution |
| **Minor (missing 1-2 skills)** | -0.5x | LLM fills gaps (e.g., Claude writes SQL) |
| **Major (missing 3+ skills)** | -1x to -2x | Hire freelancer or use no-code |

**Mitigation strategies:**
- LLM as co-developer (writes missing code)
- No-code tools for non-core features
- Pre-built templates and starter kits

---

## Asset Inventory Templates

### Template 1: Code & Infrastructure

```markdown
## Code & Infrastructure

### Existing Codebase
- **Reusability:** X% (estimate how much can be reused)
- **Languages:** {list: Python, TypeScript, etc.}
- **Frameworks:** {list: React, FastAPI, etc.}
- **Quality:** {good/needs refactor/legacy}

### API Integrations (Ready to Use)
- Authentication: {OAuth, JWT, etc.}
- Payment: {Stripe, PayPal, etc.}
- External APIs: {OpenAI, Twilio, etc.}

### Database Schemas
- **Existing schemas:** {yes/no}
- **Reusable:** {X% or "start from scratch"}
- **Migrations ready:** {yes/no}

### CI/CD Pipeline
- **Status:** {working/needs setup/none}
- **Tools:** {GitHub Actions, CircleCI, etc.}
- **Coverage:** {X% automated}
```

---

### Template 2: Design & Assets

```markdown
## Design & Assets

### Design System
- **Exists:** {yes/no}
- **Components:** {button, input, modal, etc.}
- **Accessibility:** {WCAG compliant/needs work}

### UI Components Library
- **Framework:** {Shadcn, MUI, Tailwind, custom}
- **Coverage:** {X% of needed components ready}
- **Customization:** {easy/medium/hard}

### Brand Assets
- **Logo:** {ready/needs design}
- **Color palette:** {defined/needs work}
- **Typography:** {defined/needs work}
- **Tone of voice:** {defined/needs work}
```

---

### Template 3: Data & Content

```markdown
## Data & Content

### Test Data
- **Exists:** {yes/no}
- **Realistic:** {production-like/synthetic/minimal}
- **Volume:** {X records or "needs generation"}

### User Research
- **Surveys:** {completed/in progress/none}
- **Interviews:** {X interviews completed}
- **Analytics:** {existing data/needs setup}

### Documentation
- **API docs:** {complete/partial/none}
- **User guides:** {complete/partial/none}
- **Internal docs:** {complete/partial/none}
```

---

### Template 4: Team & Skills

```markdown
## Team & Skills

### Current Team
- **Developers:** {X full-time, Y part-time}
- **Designers:** {X}
- **DevOps:** {X}
- **Product:** {X}

### Skill Matrix
| Skill | Level | Gap |
|-------|-------|-----|
| Frontend (React) | {expert/intermediate/beginner/none} | {yes/no} |
| Backend (Node/Python) | {expert/intermediate/beginner/none} | {yes/no} |
| Database (SQL/NoSQL) | {expert/intermediate/beginner/none} | {yes/no} |
| DevOps (CI/CD) | {expert/intermediate/beginner/none} | {yes/no} |
| Mobile (iOS/Android) | {expert/intermediate/beginner/none} | {yes/no} |

### Availability
- **Full-time hours:** {X hrs/week total}
- **Peak availability:** {when?}
- **Coordination:** {timezone, async/sync}
```

---

## Speed Multiplier Formula (Complete)

```
Base Multiplier = Development Method (A/B/C/D)
  - A (LLM solo): 10-20x
  - B (Traditional): 1x
  - C (No-code): 5-20x
  - D (Hybrid): 20-100x

Adjustments (Additive):
  + Existing Codebase:
      0-20% reuse → +0x
     20-50% reuse → +2x
     50-80% reuse → +5x
     80%+ reuse   → +10x

  + No-Code Tools:
      None → +0x
      1-2 tools → +2x
      3-5 tools → +5x
      Full stack → +10x

  + Team Size:
      Solo → +0x
      2-3 → +3x
      4-6 → +5x
      7+ → +10x

  + Infrastructure Ready:
      None → +0x
      Partial → +2x
      Full (CI/CD + hosting + monitoring) → +10x

Penalties (Subtractive):
  - Budget Limited:
      Unlimited → -0x
      Medium → -0.5x
      Minimal → -1x to -2x

  - Time Limited:
      Full-time → -0x
      Part-time → -0.5x
      Weekends only → -1x

  - Skill Gaps:
      None → -0x
      Minor (1-2) → -0.5x
      Major (3+) → -1x to -2x

Final Multiplier = Base + Sum(Adjustments) - Sum(Penalties)
                  (floor at 1x minimum)
```

---

## Realistic Timeline Examples

### Project: Simple CRUD App (Traditional: 4 weeks)

| Setup | Multiplier | Timeline | Time Saved |
|-------|-----------|----------|------------|
| Traditional (manual) | 1x | 4 weeks | 0 weeks |
| Solo + Claude Code | 10x | 0.4 weeks (2-3 days) | 3.6 weeks |
| Team + LLM + Supabase | 30x | 0.13 weeks (1 day) | 3.87 weeks |
| Optimal hybrid | 50x | 0.08 weeks (6-8 hours) | 3.92 weeks |

---

### Project: E-commerce MVP (Traditional: 12 weeks)

| Setup | Multiplier | Timeline | Time Saved |
|-------|-----------|----------|------------|
| Traditional | 1x | 12 weeks | 0 weeks |
| Solo + Claude + Shopify | 15x | 0.8 weeks (4-5 days) | 11.2 weeks |
| Team + LLM + existing base | 40x | 0.3 weeks (1.5-2 days) | 11.7 weeks |
| Full stack + 60% reuse | 80x | 0.15 weeks (1 day) | 11.85 weeks |

---

### Project: AI SaaS Platform (Traditional: 24 weeks)

| Setup | Multiplier | Timeline | Time Saved |
|-------|-----------|----------|------------|
| Traditional | 1x | 24 weeks | 0 weeks |
| Solo + Claude + Supabase | 12x | 2 weeks | 22 weeks |
| Team + LLM + existing AI base | 50x | 0.48 weeks (2-3 days) | 23.5+ weeks |
| Optimal (existing base 70%) | 100x | 0.24 weeks (1-2 days) | 23.75+ weeks |

---

## Real-World Case Studies

### Case Study 1: Автоответчик (Auto-Responder)

**Project:** Telegram bot with AI auto-responses

**Traditional Approach:**
- Manual Python backend + Telegram API integration
- Manual database setup + ORM
- Manual testing + deployment
- **Timeline:** 8-12 weeks

**Actual Approach:**
- Claude Code (generates 90% of code)
- Supabase (backend + database)
- Vercel (hosting)
- **Timeline:** 3-4 DAYS (20x faster)

**Multiplier Breakdown:**
- Base (LLM solo): 10x
- No-code (Supabase): +5x
- Infrastructure (Vercel): +5x
- **Total: 20x**

---

### Case Study 2: Katana (Trading System, Epic L)

**Project:** Multi-strategy trading system with backtesting

**Traditional Approach:**
- Manual Python + backtesting framework
- Manual data pipeline
- Manual optimization
- **Timeline:** 12 weeks

**Actual Approach:**
- Claude Code + existing base (40%)
- Reuse existing data pipeline
- LLM-generated strategies
- **Timeline:** 3-4 weeks (4x faster)

**Multiplier Breakdown:**
- Base (LLM solo): 10x
- Existing code (40%): +2x
- Penalties (complexity): -8x
- **Total: 4x**

**Note:** Complex domain knowledge limits LLM effectiveness.

---

### Case Study 3: Internal Tool (CRUD Dashboard)

**Project:** Admin dashboard for data management

**Traditional Approach:**
- Manual React + REST API
- Manual authentication
- Manual deployment
- **Timeline:** 6 weeks

**Actual Approach:**
- v0.dev (UI generation)
- Supabase (backend + auth)
- Claude Code (custom logic)
- **Timeline:** 2-3 DAYS (15x faster)

**Multiplier Breakdown:**
- Base (LLM + no-code): 15x
- No-code (v0 + Supabase): +10x
- Penalties (UI customization): -10x
- **Total: 15x**

---

## When Speed Multiplier is Lower

### Scenario 1: Highly Regulated Domain (Healthcare, Finance)

**Constraints:**
- Compliance (HIPAA, SOC2, PCI-DSS)
- Manual audits required
- Limited automation

**Typical Multiplier:** 2x-5x (vs. 10x-50x in standard projects)

**Why:**
- LLM cannot auto-generate compliant code
- Manual security reviews required
- Slower iteration due to risk

---

### Scenario 2: Legacy System Integration

**Constraints:**
- Undocumented legacy APIs
- No existing integration examples
- LLM has no training data on proprietary systems

**Typical Multiplier:** 1x-3x

**Why:**
- LLM cannot infer legacy behavior
- Manual reverse-engineering required
- Trial-and-error integration

---

### Scenario 3: Novel AI Research

**Constraints:**
- Cutting-edge algorithms (no training data)
- Experimental domain
- No existing patterns

**Typical Multiplier:** 1x-2x

**Why:**
- LLM trained on existing knowledge only
- Cannot invent new algorithms
- Human expertise required

---

## Optimization Tips

### Tip 1: Maximize LLM Coverage

**Strategy:** Use LLM for 80-90% of code generation

**How:**
- Clear prompts (describe desired behavior)
- Iterative refinement (provide feedback)
- Leverage existing examples (show LLM similar code)

**Impact:** 10x-20x multiplier

---

### Tip 2: Stack No-Code Tools

**Strategy:** Use multiple no-code tools for different layers

**Examples:**
- Backend: Supabase, Firebase, Railway
- Frontend: v0.dev, Webflow, Framer
- Automation: Zapier, Make, n8n
- Hosting: Vercel, Netlify, Cloudflare Pages

**Impact:** +5x-10x additional multiplier

---

### Tip 3: Reuse Existing Code Aggressively

**Strategy:** Start from existing codebase (even 20% reuse = big win)

**How:**
- Clone similar project as starter
- Use boilerplates and templates
- Extract reusable components

**Impact:** +2x-10x additional multiplier

---

### Tip 4: Invest in Infrastructure Early

**Strategy:** Set up CI/CD, hosting, monitoring BEFORE coding

**How:**
- Use managed services (GitHub Actions, Vercel)
- Automate testing and deployment
- Pre-configure monitoring (Sentry, LogRocket)

**Impact:** +10x multiplier (eliminates manual deployment time)

---

## Summary Table

| Resource Type | Impact Range | When to Use |
|---------------|--------------|-------------|
| **LLM (Claude Code)** | 10x-50x | Always (highest ROI) |
| **No-Code Tools** | 5x-20x | Non-core features, rapid MVP |
| **Existing Code** | 2x-10x | When available (even 20% helps) |
| **Team** | 3x-10x | Parallel work, faster iteration |
| **Infrastructure** | 2x-10x | Eliminates manual ops |
| **Traditional** | 1x (baseline) | Never choose (always use LLM) |

**Golden Rule:** ALWAYS use LLM. Minimum 10x multiplier. Anything less = leaving 90% time savings on the table.
