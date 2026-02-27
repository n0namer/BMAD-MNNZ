# Goal Linkage & Traceability System

## PURPOSE

Create goal_id → project → milestone → tasks traceability chain for Life OS projects.

---

## TRIGGER DETECTION

```bash
# Check if goals.yaml exists
if [ -f "{bmb_creations_output_folder}/life-os/goals.yaml" ]; then
    echo "✅ Goals found - linking milestones to goals"
    GOALS_AVAILABLE=true
else
    echo "ℹ️ Goals not defined - skipping goal linkage"
    GOALS_AVAILABLE=false
fi
```

**If goals.yaml NOT found:** Skip entire linkage process, proceed to journal update.

---

## STEP 1: LOAD GOALS

**Load goals.yaml structure:**

```yaml
goals:
  finance:
    1_year:
      id: "FIN-1Y-001"
      description: "{goal_text}"
    3_years:
      id: "FIN-3Y-001"
      description: "{goal_text}"
    5_10_years:
      id: "FIN-5-10Y-001"
      description: "{goal_text}"
  business:
    1_year:
      id: "BIZ-1Y-001"
      description: "{goal_text}"
    3_years:
      id: "BIZ-3Y-001"
      description: "{goal_text}"
    5_10_years:
      id: "BIZ-5-10Y-001"
      description: "{goal_text}"
  health:
    1_year:
      id: "HLTH-1Y-001"
      description: "{goal_text}"
    3_years:
      id: "HLTH-3Y-001"
      description: "{goal_text}"
    5_10_years:
      id: "HLTH-5-10Y-001"
      description: "{goal_text}"
  personal:
    1_year:
      id: "PERS-1Y-001"
      description: "{goal_text}"
    3_years:
      id: "PERS-3Y-001"
      description: "{goal_text}"
    5_10_years:
      id: "PERS-5-10Y-001"
      description: "{goal_text}"
```

**Parse and extract:**
- All 12 goal IDs (FIN-*, BIZ-*, HLTH-*, PERS-*)
- Goal descriptions for matching
- Domain and timeframe tags

---

## STEP 2: MATCH MILESTONES TO GOALS

**For EACH milestone in the plan (L3 level), identify relevant goals:**

### MATCHING LOGIC

**1. Domain Match:** Extract milestone domain from keywords
- Keywords like "revenue", "income", "savings" → Finance
- Keywords like "product", "customers", "launch" → Business
- Keywords like "fitness", "health", "energy" → Health
- Keywords like "learning", "skill", "relationship" → Personal

**2. Timeframe Match:** Extract milestone timeframe from delivery date
- Delivery within 1 year → 1_year goals
- Delivery within 1-3 years → 3_years goals
- Delivery within 3-10 years → 5_10_years goals

**3. Semantic Match:** Calculate keyword overlap between milestone description and goal description
- 60%+ overlap → Strong link (primary goal)
- 30-60% overlap → Moderate link (secondary goal)
- <30% overlap → Weak link (skip)

### EXAMPLE

```
Milestone: "Launch MVP with 100 beta users (Q2 2024)"
Keywords: [launch, mvp, users, product, beta]
Domain: Business (product, launch keywords)
Timeframe: 1_year (Q2 2024 = within 1 year)

Goal (BIZ-1Y-001): "Launch first SaaS product with 100 users by year-end"
Keywords: [launch, saas, product, users]
Overlap: 3/5 keywords match (60%)
→ Strong link → Primary Goal: BIZ-1Y-001

Goal (FIN-1Y-001): "Generate $10K MRR from new product"
Keywords: [generate, revenue, product, mrr]
Overlap: 1/5 keywords match (20%)
→ Weak link → Skip
```

---

## STEP 3: USER CONFIRMATION

**Present to user:**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 Goal Linkage (Traceability)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

I've identified goal links for each milestone.
Please confirm or adjust:

**Milestone 1:** Launch MVP with 100 beta users (Q2 2024)
Linked Goals:
  - [Primary] BIZ-1Y-001: "Launch first SaaS product with 100 users"
  - [Secondary] FIN-1Y-001: "Generate $10K MRR from new product"

Confirm? [Y/n] or adjust: ___

**Milestone 2:** Achieve $5K MRR (Q3 2024)
Linked Goals:
  - [Primary] FIN-1Y-001: "Generate $10K MRR from new product"

Confirm? [Y/n] or adjust: ___

**Milestone 3:** Scale to 500 users (Q4 2024)
Linked Goals:
  - [Primary] BIZ-1Y-001: "Launch first SaaS product with 100 users"
  - [Secondary] BIZ-3Y-001: "Build sustainable product business"

Confirm? [Y/n] or adjust: ___

[Continue for all milestones...]
```

**Allow user to:**
- Accept auto-detected links ([Y])
- Remove incorrect links
- Add missing links manually
- Adjust primary/secondary classification

---

## STEP 4: UPDATE PROJECT PLAN

**Add goal references to each milestone:**

**Before (without goal linkage):**
```markdown
### L3: Milestones

**M1: Launch MVP with 100 beta users**
- Timeline: Q2 2024
- Success Criteria: 100 active beta users, feedback collected
- Deliverables: MVP deployed, beta signup flow, onboarding emails
```

**After (with goal linkage):**
```markdown
### L3: Milestones

**M1: Launch MVP with 100 beta users**
- Timeline: Q2 2024
- Success Criteria: 100 active beta users, feedback collected
- Deliverables: MVP deployed, beta signup flow, onboarding emails
- **Linked Goals:**
  - **[PRIMARY]** BIZ-1Y-001: "Launch first SaaS product with 100 users by year-end"
  - **[SECONDARY]** FIN-1Y-001: "Generate $10K MRR from new product"
- **Goal Progress:** Completes 100% of BIZ-1Y-001, enables 50% of FIN-1Y-001
```

**Traceability Chain:**
```
BIZ-1Y-001 (Goal: Launch SaaS product)
  ↓
Project: SaaS Dashboard MVP
  ↓
M1: Launch MVP with 100 beta users (Milestone)
  ↓
L5: Implement user authentication, billing, analytics (Tasks)
  ↓
L6: Write auth middleware, integrate Stripe API, add tracking (Actions)
```

---

## STEP 5: CALCULATE METRICS

**Coverage Metrics:**
```
Goal Linkage Coverage = (milestones with goal_id) / total milestones
Example: 5 milestones, 4 linked → 80% coverage

Goal Distribution:
- Finance: 2 milestones linked (40%)
- Business: 4 milestones linked (80%)
- Health: 0 milestones linked (0%)
- Personal: 1 milestone linked (20%)

Timeframe Distribution:
- 1-year goals: 4 milestones (80%)
- 3-year goals: 1 milestone (20%)
- 5-10 year goals: 0 milestones (0%)
```

### RISK FLAGS

**⚠️ Flag 1: Single-Goal Focus**
- **Trigger:** >70% milestones linked to same goal
- **Warning:** "Plan heavily focused on one goal. May neglect other life areas."
- **Recommendation:** "Add milestones supporting underrepresented goals (Health, Personal)."

**⚠️ Flag 2: Short-Term Bias**
- **Trigger:** >80% milestones linked to 1-year goals, <20% to 3+ year goals
- **Warning:** "Plan achieves short-term goals but doesn't build toward long-term vision."
- **Recommendation:** "Add milestones creating long-term assets (skills, systems, relationships)."

**⚠️ Flag 3: No Goal Linkage**
- **Trigger:** <50% milestones linked to goals
- **Warning:** "Weak goal alignment. High risk project doesn't serve defined goals."
- **Recommendation:** "Either: (1) Adjust plan to better serve goals, OR (2) Reconsider if project is priority."

---

## STEP 6: OUTPUT FORMAT

**Add to project plan:**
```markdown
## Goal Linkage (Traceability)

**Coverage:** {percentage}% milestones linked to goals

**Linked Goals:**
- FIN-1Y-001: {N} milestones
- BIZ-1Y-001: {N} milestones
- HLTH-3Y-001: {N} milestones
- PERS-1Y-001: {N} milestones

**Traceability Matrix:**

| Milestone | Linked Goals | Goal Progress |
|-----------|--------------|---------------|
| M1: Launch MVP | BIZ-1Y-001 (PRIMARY), FIN-1Y-001 (SECONDARY) | Completes 100% BIZ-1Y-001 |
| M2: $5K MRR | FIN-1Y-001 (PRIMARY) | Achieves 50% of FIN-1Y-001 |
| M3: 500 users | BIZ-1Y-001, BIZ-3Y-001 | Exceeds BIZ-1Y-001, enables BIZ-3Y-001 |

{If flags triggered}
⚠️ **Risk Flags:**
- {flag_description}
- Recommendation: {recommendation}
```

**Save to Claude Flow memory:**
```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "life-os:projects:{project_id}:goal-linkage" \
  --content "{milestone_goal_mapping + coverage_metrics + risk_flags}"
```

---

## GRACEFUL FALLBACK

**If goals.yaml does NOT exist:**
- Skip entire linkage process
- Do NOT add goal linkage section to project plan
- Proceed to journal update without traceability
- Display: "ℹ️ Goal linkage skipped (goals not defined). Define goals in Step 00 to enable traceability."
