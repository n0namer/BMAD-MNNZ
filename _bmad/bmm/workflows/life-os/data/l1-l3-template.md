---
name: 'l1-l3-quick-plan-template'
version: '1.0'
purpose: 'Simplified 3-level planning template for Standard Track ideas'
target_time: '10-15 minutes'
use_cases:
  - Standard Track ideas (moderate complexity)
  - Ideas that need structure but not exhaustive detail
  - Projects with clear scope and proven approaches
when_to_use: 'Default for Standard Track, optional for Quick Track, skip for Deep Track (use L1-L6)'
consumedBy:
  - step-08-deep-plan.md
---

# L1-L3 Quick Plan Template

## Purpose

The L1-L3 template provides **sufficient planning detail for Standard Track ideas** without the time investment of full L1-L6 deep planning.

**Target time:** 10-15 minutes
**Output:** High-level roadmap with major phases, key milestones, and timeline estimate

---

## When to Use L1-L3

### ✅ Use L1-L3 When:
- Standard Track ideas (moderate complexity)
- Proven business models or approaches
- Solo or small team projects (1-3 people)
- Budget <1M RUB
- Timeline <6 months
- You need structure but not exhaustive task lists

### ❌ Don't Use L1-L3 When:
- Deep Track ideas (use full L1-L6)
- Breakthrough innovation (too many unknowns)
- Large teams (4+ people need detailed coordination)
- Multi-year projects (need detailed phasing)
- User explicitly requests L1-L6 depth

---

## Template Structure

### L1: High-Level Overview (2-3 paragraphs)

**Purpose:** Establish what we're building, why, and how at a strategic level.

**Content to include:**

**What (1 paragraph):**
- Brief description of the end result
- Core value proposition
- Who it's for

**Why (1 paragraph):**
- Key decisions that shape the approach
- Why this approach was chosen
- What alternatives were considered and rejected

**How (1 paragraph):**
- High-level technical/operational approach
- Major components or work areas
- Key dependencies or constraints

**Example (Freelance Portfolio Website):**

```markdown
## L1: High-Level Overview

### What
Building a professional portfolio website for freelance design business targeting enterprise clients. The site will showcase 8-10 case studies, client testimonials, service offerings, and contact/booking system. Primary goal: attract 2-3 enterprise clients per quarter.

### Why
Choosing custom WordPress + Elementor over pure custom code because: (1) faster time-to-market (2-3 weeks vs 2-3 months), (2) client can self-update content, (3) proven ecosystem for enterprise B2B sites. Rejected Webflow due to lack of CRM integration. Enterprise clients expect premium design + technical credibility.

### How
WordPress foundation + premium theme + Elementor Pro for design flexibility. Key components: Case study showcase (custom post type), testimonial slider, service pages, HubSpot form integration for lead capture, Google Analytics + Search Console for SEO tracking. Hosting on WP Engine for performance and security (enterprise requirement).
```

**Time allocation: 2-3 minutes**

---

### L2: Major Phases (3-5 phases)

**Purpose:** Break the work into sequential phases with clear goals.

**Content per phase:**
- **Phase name** (descriptive, action-oriented)
- **Duration estimate** (weeks or months)
- **Goal** (what's accomplished by end of phase)
- **Key activities** (3-5 bullet points)

**Template:**

```markdown
## L2: Major Phases

### Phase 1: {Phase Name} - {Duration estimate}
**Goal:** {What's accomplished by the end of this phase}

**Key activities:**
- {Activity 1}
- {Activity 2}
- {Activity 3}
- {Activity 4}
- {Activity 5}

### Phase 2: {Phase Name} - {Duration estimate}
**Goal:** {What's accomplished}

**Key activities:**
- {Activity 1}
- {Activity 2}
- {Activity 3}

{Repeat for 3-5 phases total}
```

**Example (Freelance Portfolio Website):**

```markdown
## L2: Major Phases

### Phase 1: Foundation & Setup - 1 week
**Goal:** WordPress environment ready with theme and core plugins installed

**Key activities:**
- Purchase domain, set up WP Engine hosting
- Install WordPress + premium theme (Astra Pro)
- Install essential plugins (Elementor Pro, SEO, security, caching)
- Set up staging environment for testing
- Create basic site structure (pages, menus)

### Phase 2: Content & Design - 2 weeks
**Goal:** All pages designed and content populated

**Key activities:**
- Write/edit 8-10 case studies (1-2 per day)
- Design homepage hero, services section, case study grid
- Design case study template with Elementor
- Gather and upload client testimonials
- Create service offering pages (3-5 services)
- Set up contact/booking forms with HubSpot integration

### Phase 3: SEO & Optimization - 3-5 days
**Goal:** Site optimized for search and performance

**Key activities:**
- Keyword research for services and case studies
- Optimize meta titles, descriptions, headings
- Set up Google Analytics and Search Console
- Image optimization and lazy loading
- Speed testing and caching configuration

### Phase 4: Launch & Monitoring - 2-3 days
**Goal:** Site live and monitored

**Key activities:**
- Final content review and QA testing
- DNS configuration and go-live
- Submit sitemap to Google
- Set up uptime monitoring
- Train client on content updates
```

**Time allocation: 5-7 minutes**

---

### L3: Key Milestones (5-8 milestones)

**Purpose:** Define checkpoints with measurable success criteria.

**Content per milestone:**
- **Milestone name** (concrete, measurable)
- **Target date** (relative or absolute)
- **Success criteria** (how you know it's done)
- **Deliverables** (what exists at this point)

**Template:**

```markdown
## L3: Key Milestones

### M1: {Milestone Name} - {Target date}
**Success criteria:**
- {Measurable criterion 1}
- {Measurable criterion 2}

**Deliverables:**
- {Artifact 1}
- {Artifact 2}

### M2: {Milestone Name} - {Target date}
**Success criteria:**
- {Criterion 1}
- {Criterion 2}

**Deliverables:**
- {Artifact 1}
- {Artifact 2}

{Repeat for 5-8 milestones total}
```

**Example (Freelance Portfolio Website):**

```markdown
## L3: Key Milestones

### M1: Environment Ready - Week 1, Day 3
**Success criteria:**
- WordPress accessible at staging URL
- Theme and plugins installed and activated
- Basic site structure created (10 pages minimum)

**Deliverables:**
- Live staging site
- Plugin configuration documentation

### M2: First Case Study Live - Week 2, Day 2
**Success criteria:**
- 1 complete case study published with images
- Case study template reusable for others
- Client testimonial integrated

**Deliverables:**
- Case study page (live)
- Elementor template saved

### M3: Content 50% Complete - Week 2, Day 5
**Success criteria:**
- 4+ case studies published
- All service pages drafted
- Homepage hero designed

**Deliverables:**
- 4 case study pages
- 3-5 service pages
- Homepage mockup

### M4: Content 100% Complete - Week 3, Day 3
**Success criteria:**
- 8-10 case studies published
- All testimonials added
- Contact forms tested and working

**Deliverables:**
- All content pages live
- HubSpot integration tested

### M5: SEO Optimized - Week 3, Day 5
**Success criteria:**
- All pages have optimized meta tags
- Google Analytics tracking confirmed
- Sitemap submitted to Google

**Deliverables:**
- SEO audit report
- Google Analytics dashboard

### M6: Performance Pass - Week 4, Day 2
**Success criteria:**
- PageSpeed score >85 (mobile and desktop)
- All images optimized
- Caching configured

**Deliverables:**
- Speed test reports
- Optimization checklist

### M7: Launch Ready - Week 4, Day 4
**Success criteria:**
- All QA issues resolved
- Client sign-off received
- DNS ready to point

**Deliverables:**
- QA checklist (100% pass)
- Client approval email

### M8: Live & Monitored - Week 4, Day 5
**Success criteria:**
- Site live on production domain
- Uptime monitoring active
- Analytics tracking live traffic

**Deliverables:**
- Live site URL
- Monitoring dashboard
```

**Time allocation: 3-5 minutes**

---

## Summary Section (Required)

**Add this at the end of every L1-L3 plan:**

```markdown
---

## Plan Summary

**Total estimated duration:** {X weeks/months}

**Critical path:**
{Phase 1} → {Phase 2} → {Phase 3} → Launch

**Top 3 risks:**
1. {Risk 1 and mitigation}
2. {Risk 2 and mitigation}
3. {Risk 3 and mitigation}

**Resource requirements:**
- Time commitment: {hours per week}
- Budget: {total budget estimate}
- Team: {who's involved}

**Success metrics:**
- {Metric 1}: {Target}
- {Metric 2}: {Target}
- {Metric 3}: {Target}
```

**Example:**

```markdown
---

## Plan Summary

**Total estimated duration:** 4 weeks (with 10-15 hours/week commitment)

**Critical path:**
Foundation & Setup → Content & Design → SEO & Optimization → Launch

**Top 3 risks:**
1. **Content delays** (case studies take longer to write) → Mitigation: Write 1-2 case studies before Phase 2 starts
2. **Client feedback cycles** (revisions slow progress) → Mitigation: Set expectation of 2 revision rounds max per phase
3. **HubSpot integration issues** (API complexity) → Mitigation: Use Zapier as backup if native integration fails

**Resource requirements:**
- Time commitment: 10-15 hours/week (solo work)
- Budget: 200K RUB (domain + hosting + premium theme + Elementor Pro + WP Engine)
- Team: Solo freelancer + occasional design feedback from peer

**Success metrics:**
- Site live and indexed by Google (Week 4)
- 2-3 enterprise leads within first month
- PageSpeed score >85 maintained
```

---

## Quality Checklist

Before finalizing L1-L3 plan, verify:

**L1 Completeness:**
- [ ] What is clearly described (1 paragraph, <100 words)
- [ ] Why explains key decisions (1 paragraph, rationale clear)
- [ ] How outlines approach (1 paragraph, major components listed)

**L2 Completeness:**
- [ ] 3-5 phases defined
- [ ] Each phase has clear goal
- [ ] Key activities are actionable (3-5 per phase)
- [ ] Duration estimates are realistic

**L3 Completeness:**
- [ ] 5-8 milestones defined
- [ ] Each milestone has measurable success criteria
- [ ] Deliverables are concrete
- [ ] Target dates align with phase durations

**Summary Completeness:**
- [ ] Total duration stated
- [ ] Critical path identified
- [ ] Top 3 risks with mitigations
- [ ] Resource requirements clear
- [ ] Success metrics defined

---

## Time Investment Guide

| Section | Minimum Time | Maximum Time | Average |
|---------|-------------|-------------|---------|
| L1 (Overview) | 2 min | 5 min | 3 min |
| L2 (Phases) | 4 min | 10 min | 6 min |
| L3 (Milestones) | 3 min | 8 min | 5 min |
| Summary | 1 min | 3 min | 2 min |
| **TOTAL** | **10 min** | **26 min** | **16 min** |

**Target:** 10-15 minutes for Standard Track
**Acceptable range:** 10-20 minutes (if user adds extra detail)

---

## When to Upgrade to L1-L6

**Upgrade to full L1-L6 deep plan if:**

1. **Complexity revealed during L1-L3**
   - Phase 2 or 3 reveals >20 distinct tasks
   - Critical dependencies discovered between phases
   - Multiple stakeholders need detailed coordination

2. **User requests more detail**
   - "I need task-level breakdown"
   - "How do I actually execute Phase 2?"
   - "What are the day-to-day actions?"

3. **Track escalation**
   - Standard Track idea escalates to Deep Track mid-pipeline
   - Budget increases >1M RUB
   - Team grows to 4+ people

**How to upgrade:**
- Preserve L1-L3 as foundation
- Expand L3 into L4 (stages per work stream)
- Add L5 (tasks per stage) and L6 (atomic actions)
- Typical upgrade time: +30-45 minutes

---

## Examples by Domain

### Example 1: Small Business CRM Implementation (Standard Track)

**L1: Overview**
```
What: Implementing HubSpot CRM for 10-person team to centralize customer data, automate follow-ups, and track sales pipeline. Goal: 50% reduction in manual data entry and 30% faster lead response time.

Why: Chose HubSpot over Salesforce because: (1) better for SMB (easier onboarding), (2) free tier sufficient for initial rollout, (3) strong email integration. Need automation to scale beyond current 50 leads/month capacity.

How: HubSpot free tier + Sales Hub Starter. Key components: Contact import from spreadsheets, email sync (Gmail), deal pipeline setup (3 stages), automated follow-up sequences, team training (2 sessions). Gradual rollout: Sales team first (week 1-2), then support team (week 3).
```

**L2: Phases (4 phases)**
1. **Setup & Configuration** (1 week) → HubSpot account ready, basic pipeline configured
2. **Data Migration** (1 week) → All contacts and deals imported, validated
3. **Team Training** (1 week) → All team members trained, actively using system
4. **Optimization** (2 weeks) → Automations configured, reports customized

**L3: Milestones (6 milestones)**
- M1: HubSpot configured (Day 3)
- M2: Contacts imported (Day 7)
- M3: Sales team trained (Day 10)
- M4: Full team onboarded (Day 14)
- M5: First automation live (Day 18)
- M6: 30-day usage review (Day 30)

**Duration:** 1 month
**Time saved vs L1-L6:** 40-50 minutes

---

### Example 2: Online Course Launch (Standard Track)

**L1: Overview**
```
What: Creating and launching "Russian Cuisine Fundamentals" online course on Udemy. 20 video lessons (30-45 min each), recipe PDFs, quizzes. Target: 100 students in first 3 months, 4.5+ star rating.

Why: Chose Udemy over own platform because: (1) built-in audience (10M+ students), (2) no tech maintenance, (3) payment processing handled. Trade-off: 50% revenue share but worth it for discoverability. Focus on quality over quantity (20 lessons vs competitors' 50+ rushed lessons).

How: Pre-record all content before launch (batch filming over 2 weeks), professional editing (outsourced), structured curriculum (beginner → intermediate → advanced). Udemy platform handles hosting, payments, student management. Marketing via Udemy search + targeted FB ads to cooking enthusiasts.
```

**L2: Phases (5 phases)**
1. **Content Planning** (1 week) → Full curriculum outlined, recipes selected
2. **Video Production** (2 weeks) → All 20 lessons filmed and edited
3. **Platform Setup** (3 days) → Udemy course created, materials uploaded
4. **Pre-Launch** (1 week) → Course reviewed, pricing set, marketing prepared
5. **Launch & Iteration** (ongoing) → Course live, student feedback incorporated

**L3: Milestones (7 milestones)**
- M1: Curriculum finalized (Day 5)
- M2: First 5 videos filmed (Day 10)
- M3: All videos filmed (Day 17)
- M4: Editing complete (Day 21)
- M5: Course uploaded to Udemy (Day 24)
- M6: Course approved + live (Day 28)
- M7: First 10 students enrolled (Day 35)

**Duration:** 5 weeks
**Time saved vs L1-L6:** 45 minutes

---

### Example 3: Personal Fitness Transformation (Standard Track)

**L1: Overview**
```
What: 12-week fitness transformation program targeting 10kg weight loss + strength gains (bench press 60kg → 80kg, squat 80kg → 100kg). Structured training 4x/week + macro-tracked nutrition.

Why: Chose progressive overload strength training + calorie deficit approach because: (1) proven for body recomposition, (2) sustainable long-term, (3) builds muscle while losing fat. Rejected cardio-only approach (loses muscle) and extreme diets (not sustainable). 12 weeks is minimum for visible transformation.

How: 4-day split (Push/Pull/Legs/Upper), track macros (2000 kcal, 40% protein, 30% carb, 30% fat), weekly weigh-ins + progress photos. Tools: Google Sheets for tracking, MyFitnessPal for nutrition, gym membership. Weekly review: adjust calories if weight plateau >2 weeks, deload every 4th week for recovery.
```

**L2: Phases (3 phases)**
1. **Foundation** (Weeks 1-4) → Habit formation, baseline strength established
2. **Progression** (Weeks 5-8) → Linear progression, calorie deficit optimized
3. **Refinement** (Weeks 9-12) → Push limits, final cut to goal weight

**L3: Milestones (6 milestones)**
- M1: Baseline metrics recorded (Day 1)
- M2: 4 weeks consistent (no missed workouts) (Week 4)
- M3: -5kg weight loss (Week 6)
- M4: Strength +10% on all lifts (Week 8)
- M5: -8kg weight loss (Week 10)
- M6: Final goal: -10kg + strength targets hit (Week 12)

**Duration:** 12 weeks
**Time saved vs L1-L6:** 40 minutes (fitness doesn't need L4-L6 task lists)

---

## Integration with Step 08 Deep Plan

**Step 08 will:**
1. Detect track from workflow plan (`track: standard`)
2. Recommend L1-L3 as default
3. Load this template if user accepts
4. Guide user through L1 → L2 → L3 sequentially
5. Auto-generate summary section
6. Save to workflow plan under "Deep Plan (L1-L3)" section

**Output location:**
- Workflow plan: `{bmb_creations_output_folder}/life-os/workflow-plans/{idea-id}.md`
- Section: `## Deep Plan (L1-L3)`

---

## FAQ

**Q: When should I use L1-L3 vs L1-L6?**
A: Use L1-L3 for Standard Track ideas (moderate complexity, proven approaches, <6 months timeline). Use L1-L6 for Deep Track ideas (high complexity, breakthrough innovation, >6 months, 4+ people).

**Q: Can I upgrade L1-L3 to L1-L6 later?**
A: Yes! Your L1-L3 becomes the foundation. Add L4 (stages), L5 (tasks), L6 (atomic actions) when needed. Typical upgrade time: 30-45 minutes.

**Q: What if my idea is too simple for L1-L3?**
A: Use Quick Track instead (no deep plan). Quick Track gives you Go/NoGo in 15-20 minutes without planning overhead.

**Q: What if L1-L3 reveals my idea is more complex than I thought?**
A: System will detect this and offer track escalation to Deep Track. You can accept or continue with L1-L3 and revisit later.

**Q: How detailed should L2 phases be?**
A: Each phase should have 3-5 key activities (bullet points). If you find yourself writing 10+ activities, consider upgrading to L1-L6 for better task management.

**Q: Do I need RACI assignments in L1-L3?**
A: Only if multi-person team. For solo or 2-person projects, skip RACI and just note who's responsible in phase descriptions.

---

**Template Version:** 1.0
**Last Updated:** 2025-02-05
**Compatible with:** Life OS v3.0, Step 08 Deep Plan
