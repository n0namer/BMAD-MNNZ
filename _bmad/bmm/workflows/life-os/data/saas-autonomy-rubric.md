# SaaS Autonomy Rubric - 4 Pillars Scoring Guide

**Purpose:** Detailed scoring anchors for evaluating SaaS autonomous operation capability (6th criterion in MCDA scoring for SaaS/software projects).

**When to Use:** Apply ONLY when `domain = 'saas'` OR `domain = 'software'` (detected in Step 01 or explicitly stated by user).

**Critical Context:** This rubric evaluates how autonomously a SaaS product can operate without manual team intervention. Critical for:
- Solo founders aiming for passive income
- Small teams (2-5 people) evaluating operational overhead
- Strategic decisions about product-led growth vs. high-touch sales

---

## The 4 Autonomy Pillars

**Formula:**
```
SaaS_Autonomy_Score = (Self_Signup × 0.25) + (Self_Billing × 0.30) +
                      (Self_Service_Support × 0.30) + (Autonomous_Operation × 0.15)

Result: 1.0-5.0 scale (consistent with other MCDA criteria)
```

**Weight Rationale:**
- Self-Billing (0.30) + Self-Service Support (0.30) = 60% of score → These drive most operational costs
- Self-Signup (0.25) = 25% → Critical for growth velocity
- Autonomous Operation (0.15) = 15% → Infrastructure cost, but often one-time setup

---

## Pillar 1: Self-Signup (0.25 weight)

**Definition:** Can users sign up and get instant access without sales calls, demos, or manual provisioning?

### Scoring Anchors (1-5 scale)

**Score: 1/5 - Enterprise Sales Process**
- **Behavior:** Multi-step enterprise sales cycle required
- **Characteristics:**
  - RFP/RFI process (weeks to months)
  - In-person demos or presentations required
  - Custom contracts and negotiations
  - Manual provisioning after contract signed
  - Legal review and procurement involved
- **Team Implication:** Sales team + solutions engineers required (10+ people)
- **Example:** Enterprise CRM with custom integration (Salesforce enterprise)

---

**Score: 2/5 - Sales-Assisted Signup**
- **Behavior:** Sales calls required but faster than enterprise
- **Characteristics:**
  - Initial demo call (30-60 min) required before access
  - Sales qualification ("Are you a good fit?")
  - Trial requires manual approval (24-48h delay)
  - Provisioning semi-automated (requires human trigger)
  - Standard contracts (not fully custom)
- **Team Implication:** Small sales team required (3-5 people)
- **Example:** Mid-market B2B tools (HubSpot mid-tier, Pipedrive)

---

**Score: 3/5 - Self-Service Trial with Manual Approval**
- **Behavior:** User can request trial, but approval needed
- **Characteristics:**
  - Signup form available (no initial call)
  - Manual approval within 1-24 hours
  - Trial starts automatically after approval
  - Email verification + basic qualification questions
  - Credit card NOT required for trial
- **Team Implication:** 1-2 people handling approvals (part-time)
- **Example:** B2B tools with compliance requirements (data security review needed)

---

**Score: 4/5 - Instant Trial, Credit Card for Upgrade**
- **Behavior:** Instant trial access, payment required only for upgrade
- **Characteristics:**
  - Signup takes <2 minutes
  - No approval needed for trial
  - Email verification (instant)
  - Trial limits (time-based or usage-based)
  - Credit card required ONLY for paid plan
  - Instant upgrade after payment
- **Team Implication:** Zero human intervention for signups (fully automated)
- **Example:** Notion, Figma, Linear (product-led growth SaaS)

---

**Score: 5/5 - 1-Click Instant Signup (Frictionless)**
- **Behavior:** Absolute minimum friction to start using product
- **Characteristics:**
  - Signup with Google/GitHub OAuth (1-click)
  - Instant access (no email verification delay)
  - Credit card optional even for paid features (bill later or freemium)
  - No approval, no waiting, no forms beyond OAuth
  - Instant provisioning (<5 seconds)
- **Team Implication:** Zero human touch, maximum conversion rate
- **Example:** Vercel, Railway, GitHub (developer-focused frictionless onboarding)

---

## Pillar 2: Self-Billing (0.30 weight)

**Definition:** Is payment and subscription management fully automated without manual invoicing or follow-up?

### Scoring Anchors (1-5 scale)

**Score: 1/5 - Manual Invoicing**
- **Behavior:** Invoices sent manually, payment requires human follow-up
- **Characteristics:**
  - PDF invoices created manually (or semi-manually)
  - Payment by wire transfer or PO
  - Manual tracking of payments received
  - Manual follow-up for late payments
  - No automatic service suspension for non-payment
  - Accounting reconciliation done manually
- **Team Implication:** Finance/accounting team required (2-3 people)
- **Example:** Traditional consultancy or high-touch B2B services

---

**Score: 2/5 - Automated Invoicing, Manual Payment**
- **Behavior:** System generates invoices, but payment still requires manual steps
- **Characteristics:**
  - Automated invoice generation (PDF emailed)
  - Payment by check/wire (manual confirmation)
  - Manual payment tracking (requires human to check bank account)
  - Manual follow-up for overdue invoices
  - Service suspension requires manual action
- **Team Implication:** 1 finance person handling payments + follow-up
- **Example:** B2B SaaS with enterprise customers (annual contracts, NET-30 terms)

---

**Score: 3/5 - Recurring Credit Card Billing**
- **Behavior:** Automated recurring billing, but limited dunning
- **Characteristics:**
  - Recurring charges (monthly/annual) via Stripe/PayPal
  - Automatic retries for failed payments (1-2 attempts)
  - Basic dunning emails (automated "payment failed" notices)
  - Manual intervention needed for complex failures
  - No usage-based billing (flat pricing only)
  - Grace period before suspension (3-7 days)
- **Team Implication:** Minimal intervention (1 person part-time for edge cases)
- **Example:** Most B2C SaaS (Netflix, Spotify)

---

**Score: 4/5 - Usage-Based Billing (Automated)**
- **Behavior:** Billing adapts to actual usage, fully automated
- **Characteristics:**
  - Metered billing (per user, per API call, per GB, etc.)
  - Automatic invoice adjustments based on usage
  - Multiple retry attempts with smart dunning (3-5 attempts over 2 weeks)
  - Automatic payment method update prompts
  - Graceful service degradation (not instant cutoff)
  - Webhook-driven (no human in loop)
- **Team Implication:** Zero human touch except for refund requests
- **Example:** AWS, Vercel, Stripe itself (usage-based pricing)

---

**Score: 5/5 - Fully Automated Billing + Dunning + Recovery**
- **Behavior:** Self-healing payment system with maximum recovery
- **Characteristics:**
  - Usage-based or hybrid billing (fully automated)
  - Advanced dunning sequence (up to 7 attempts over 30 days)
  - Automatic payment method updater (via Stripe/card networks)
  - Proactive "card expiring soon" reminders
  - Automatic recovery (re-activate immediately after payment)
  - Failed payment = temporary downgrade (not instant cutoff)
  - Revenue recovery rate >80%
- **Team Implication:** Zero human intervention, even for failures
- **Example:** Superhuman, Stripe Billing with advanced dunning, Notion (seamless payment recovery)

---

## Pillar 3: Self-Service Support (0.30 weight)

**Definition:** Can users solve problems and get answers without contacting human support agents?

### Scoring Anchors (1-5 scale)

**Score: 1/5 - Dedicated CSM or Account Manager Required**
- **Behavior:** Users need human support for routine tasks
- **Characteristics:**
  - Every user has assigned CSM (Customer Success Manager)
  - Regular check-in calls (weekly/monthly)
  - Support requests go through dedicated person
  - Onboarding requires multiple training sessions
  - Documentation exists but insufficient (users still need help)
  - Support contact rate: >50% of users per month
- **Team Implication:** CSM team scales linearly with users (10+ people for 100 customers)
- **Example:** Enterprise CRM with complex workflows (Salesforce enterprise)

---

**Score: 2/5 - Email/Ticket Support (24-48h Response)**
- **Behavior:** Users submit tickets, human agents respond
- **Characteristics:**
  - Email or support ticket system
  - Response time: 24-48 hours (no real-time support)
  - No self-service knowledge base (or very basic)
  - Users wait for human agent for most questions
  - Support contact rate: 30-50% of users per month
- **Team Implication:** Support team required (3-5 people for 1,000 users)
- **Example:** Traditional B2B SaaS (Zendesk, Jira before self-service improvements)

---

**Score: 3/5 - Knowledge Base + Community Forum (50% Self-Service Rate)**
- **Behavior:** Mix of self-service and human support
- **Characteristics:**
  - Comprehensive knowledge base (searchable docs)
  - Community forum or Slack channel (users help users)
  - Email support available for edge cases
  - ~50% of questions answered via self-service
  - Response time for human support: 4-24 hours
  - Support contact rate: 15-30% of users per month
- **Team Implication:** 2-3 support agents for 5,000 users
- **Example:** Notion, Airtable (good docs + community)

---

**Score: 4/5 - In-App Help + Chatbot + Docs (80% Self-Service Rate)**
- **Behavior:** Most users never need to contact support
- **Characteristics:**
  - In-app contextual help (tooltips, guided tutorials)
  - AI chatbot handles 70-80% of common questions
  - Searchable knowledge base with video tutorials
  - Proactive help (detects user stuck, offers tips)
  - Email support for complex issues (used by <20% of users)
  - Support contact rate: 5-15% of users per month
- **Team Implication:** 1-2 support agents for 10,000 users
- **Example:** Figma, Linear (excellent in-app help + onboarding)

---

**Score: 5/5 - AI-Powered Support + Proactive Issue Detection (<1% Contact Rate)**
- **Behavior:** Users almost never need human support
- **Characteristics:**
  - AI assistant solves 95%+ of questions (GPT-4 level)
  - Proactive issue detection (system predicts problems before user notices)
  - Auto-healing (system fixes common issues automatically)
  - Interactive docs (users ask questions, AI answers in context)
  - Human support only for complex billing/legal issues
  - Support contact rate: <1% of users per month
- **Team Implication:** 1 support agent for 50,000+ users (edge cases only)
- **Example:** GitHub Copilot, Superhuman (AI-first support)

---

## Pillar 4: Autonomous Operation (0.15 weight)

**Definition:** Can the product run without daily manual work from the team (infrastructure, provisioning, monitoring)?

### Scoring Anchors (1-5 scale)

**Score: 1/5 - Heavy Manual Operations**
- **Behavior:** Daily manual work required to keep system running
- **Characteristics:**
  - Manual user provisioning (add users via admin panel)
  - Manual infrastructure scaling (resize servers when needed)
  - Manual backups (daily/weekly manual export)
  - Manual deployments (requires engineer intervention)
  - Manual monitoring (check dashboards daily)
  - On-call required (frequent manual interventions)
- **Team Implication:** DevOps/ops team required full-time (2-3 people)
- **Example:** Legacy on-premise software with manual admin

---

**Score: 2/5 - Some Automation, Weekly Admin Work**
- **Behavior:** Reduced manual work, but still requires weekly attention
- **Characteristics:**
  - Semi-automated provisioning (requires admin approval)
  - Auto-scaling exists but limited (requires tuning)
  - Automated backups (but manual restore process)
  - CI/CD pipeline exists (but deployments still need babysitting)
  - Weekly maintenance windows
  - On-call rotation needed
- **Team Implication:** 1-2 DevOps engineers (part-time admin work)
- **Example:** Traditional SaaS on AWS/GCP (moderate automation)

---

**Score: 3/5 - Mostly Automated (Monthly Admin Work)**
- **Behavior:** System mostly runs itself, occasional check-ins
- **Characteristics:**
  - Fully automated user provisioning
  - Auto-scaling works reliably
  - Automated backups + restore (tested)
  - Automated deployments (no human intervention for releases)
  - Monitoring with alerts (no daily dashboard checks)
  - Monthly health checks only
  - On-call rarely triggered (once per month or less)
- **Team Implication:** 1 DevOps engineer (20-30% time for maintenance)
- **Example:** Modern cloud-native SaaS (Vercel-deployed, Supabase backend)

---

**Score: 4/5 - Highly Automated (Quarterly Check-Ins)**
- **Behavior:** System self-heals, human only for capacity planning
- **Characteristics:**
  - Zero-touch provisioning
  - Intelligent auto-scaling (learns patterns)
  - Automated rollback on failures
  - Self-healing infrastructure (auto-restart failed services)
  - Proactive monitoring (system detects + fixes issues before impact)
  - Quarterly capacity planning only
  - On-call rarely triggered (once per quarter)
- **Team Implication:** 1 DevOps engineer (10% time, mostly planning)
- **Example:** Serverless SaaS (AWS Lambda, Cloudflare Workers)

---

**Score: 5/5 - Fully Autonomous (Zero Admin, 99.9% Uptime)**
- **Behavior:** System operates without human intervention
- **Characteristics:**
  - 100% automated provisioning, scaling, healing
  - AI-driven capacity planning (system predicts needs)
  - Automated security patching
  - Chaos engineering (system tests itself)
  - No on-call needed (system handles all incidents)
  - 99.9%+ uptime (SLA-backed)
  - Human intervention only for major architecture changes
- **Team Implication:** Zero ongoing ops work (only for new features)
- **Example:** GitHub, Vercel, Cloudflare (fully automated cloud platforms)

---

## Interpretation Thresholds

**Overall SaaS Autonomy Score Interpretation:**

| Score Range | Classification | Team Size Needed | Business Model Fit | Passive Income Potential |
|-------------|---------------|------------------|-------------------|-------------------------|
| **4.5-5.0** | Highly Autonomous | Solo founder feasible | Product-led growth (PLG) | ✅ High (near-passive after setup) |
| **3.5-4.4** | Moderately Autonomous | Small team (2-5) | Hybrid PLG + light touch | ⚠️ Medium (some ongoing work) |
| **2.5-3.4** | Limited Autonomy | Medium team (5-10) | Sales-assisted growth | ❌ Low (requires active management) |
| **1.0-2.4** | Low Autonomy | Large team (10+) | High-touch sales + CSM | ❌ None (managed service, not SaaS) |

---

## System Flags & Recommendations

**Automatic Risk Flags:**

**⚠️ Flag 1: High Support Load Risk**
- **Trigger:** `SaaS_Autonomy < 3.0`
- **Warning:** "This SaaS design requires significant ongoing support team. Operational costs may exceed revenue for first 6-12 months."
- **Recommendation:** "Consider improving self-service capabilities (better docs, in-app help, chatbot) before launch."

---

**⚠️ Flag 2: Manual Operations Bottleneck**
- **Trigger:** `Autonomous_Operation < 2.5` (Pillar 4 low)
- **Warning:** "Manual operations work will limit scaling. Solo founder not feasible."
- **Recommendation:** "Invest in infrastructure automation (CI/CD, auto-scaling, monitoring) before acquiring users."

---

**⚠️ Flag 3: Consider Enterprise Model Instead**
- **Trigger:** `SaaS_Autonomy < 2.0`
- **Warning:** "This design is closer to a managed service than true SaaS. Passive income unlikely."
- **Recommendation:** "Either: (1) Redesign for more automation, OR (2) Pivot to B2B enterprise model with higher pricing to cover support costs."

---

## Integration with Step 05 Scoring

**How SaaS Autonomy Fits in MCDA:**

1. **Conditional Application:**
   - IF `domain = 'saas'` OR `domain = 'software'` → Include SaaS Autonomy as 6th base criterion
   - ELSE → Skip this criterion entirely

2. **Weight in Overall Score:**
   - SaaS Autonomy weight: **0.15** (15% of positive weight)
   - Combined with other criteria via 70/30 normalization (positive/negative balance)

3. **Example Scoring:**
   ```
   Assumptions: goals.yaml found, domain='saas'
   Base criteria: Impact, Confidence, Effort, Strategic Alignment, Risk, SaaS Autonomy

   Raw scores:
   - Impact: 4/5 (weight 0.25)
   - Confidence: 3/5 (weight 0.15)
   - Strategic Alignment: 5/5 (weight 0.25)
   - SaaS Autonomy: 4/5 (weight 0.15)
   - Effort: 4/5 (weight -0.20, negative)
   - Risk: 3/5 (weight -0.15, negative)

   Normalized weights (70/30 positive/negative):
   - Positive sum: 0.25 + 0.15 + 0.25 + 0.15 = 0.80 → normalize to 0.70
   - Negative sum: 0.20 + 0.15 = 0.35 → normalize to 0.30

   Normalized weights:
   - Impact: 0.219 (0.25 / 0.80 × 0.70)
   - Confidence: 0.131 (0.15 / 0.80 × 0.70)
   - Strategic: 0.219 (0.25 / 0.80 × 0.70)
   - SaaS Autonomy: 0.131 (0.15 / 0.80 × 0.70)
   - Effort: -0.171 (0.20 / 0.35 × 0.30)
   - Risk: -0.129 (0.15 / 0.35 × 0.30)

   Score calculation:
   Positive: (4 × 0.219) + (3 × 0.131) + (5 × 0.219) + (4 × 0.131) = 2.886
   Negative: (4 × 0.171) + (3 × 0.129) = 1.071
   Final Score: 2.886 - 1.071 = 1.815/5.0
   ```

---

## User Interaction Templates

**Template 1: Pillar Scoring Questions**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 SaaS Autonomy Assessment
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

This SaaS/software idea requires autonomy evaluation.
Please score each pillar (1-5 scale):

**Pillar 1: Self-Signup (0.25 weight)**
How easy is signup for new users?
- 1 = Enterprise sales process (RFPs, demos, weeks)
- 3 = Self-service trial with manual approval (1-24h)
- 5 = 1-click instant signup (OAuth, <5 seconds)

Your score: ___ /5
Brief reasoning: ___

**Pillar 2: Self-Billing (0.30 weight)**
How automated is payment and subscription management?
- 1 = Manual invoicing (wire transfers, manual follow-up)
- 3 = Recurring credit card billing (basic dunning)
- 5 = Fully automated usage-based billing + smart dunning

Your score: ___ /5
Brief reasoning: ___

**Pillar 3: Self-Service Support (0.30 weight)**
How self-sufficient are users (without contacting support)?
- 1 = Dedicated CSM required (50%+ contact rate)
- 3 = Knowledge base + community (50% self-service rate)
- 5 = AI-powered support (<1% contact rate)

Your score: ___ /5
Brief reasoning: ___

**Pillar 4: Autonomous Operation (0.15 weight)**
How much manual work needed to run the infrastructure?
- 1 = Daily manual work (provisioning, scaling, monitoring)
- 3 = Mostly automated (monthly check-ins only)
- 5 = Fully autonomous (99.9% uptime, zero admin)

Your score: ___ /5
Brief reasoning: ___
```

---

**Template 2: Results Interpretation**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ SaaS Autonomy Score: {calculated_score}/5.0
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Classification:** {Highly/Moderately/Limited/Low} Autonomous

**Pillar Breakdown:**
- Self-Signup: {score}/5 × 0.25 = {contribution}
- Self-Billing: {score}/5 × 0.30 = {contribution}
- Self-Service Support: {score}/5 × 0.30 = {contribution}
- Autonomous Operation: {score}/5 × 0.15 = {contribution}

**Total:** {sum} = {calculated_score}/5.0

**Business Implications:**
- Team Size Needed: {solo founder / 2-5 team / 5-10 team / 10+ team}
- Business Model Fit: {Product-led growth / Hybrid / Sales-assisted / High-touch enterprise}
- Passive Income Potential: {High / Medium / Low / None}

{If score < 3.0}
⚠️ **High Support Load Risk**
This design requires significant ongoing support and operations work.
Consider improving automation before launch.

{If score < 2.0}
⚠️ **Consider Enterprise Model**
This is closer to a managed service than true SaaS.
Recommendation: Redesign for more automation OR pivot to high-touch enterprise pricing.
```

---

## Usage Notes for AI Facilitator

**When to Load This Rubric:**
1. User reaches Step 05 (Scoring)
2. Step 01 classified `domain = 'saas'` or `domain = 'software'`
3. OR user explicitly states "this is a SaaS product"

**How to Present:**
1. Show brief overview (4 pillars + weights)
2. Ask user to score each pillar (1-5)
3. Request brief reasoning for each score
4. Calculate overall SaaS Autonomy score using formula
5. Interpret results using thresholds table
6. Display any relevant risk flags
7. Integrate into MCDA calculation as 6th base criterion

**Common Pitfalls:**
- ❌ Do NOT apply SaaS Autonomy to non-SaaS projects (e.g., consulting, hardware, content)
- ❌ Do NOT skip reasoning (scores without context are not actionable)
- ❌ Do NOT apply to MVP validation (wait until idea is more concrete)

---

**Document Status:** ✅ COMPLETE
**Last Updated:** 2026-02-06
**Version:** 1.0
**Source:** IDEAL-BEHAVIOR-REFERENCE.md Section 1.10 (lines 678-800)
