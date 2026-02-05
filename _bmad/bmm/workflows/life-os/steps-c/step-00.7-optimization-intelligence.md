---
name: 'step-00.7-optimization-intelligence'
description: 'AI-powered optimization suggestions for fastest/best implementation approach'
nextStepFile: './step-00-goals-discovery.md'
optimizationFile: '{bmb_creations_output_folder}/life-os/optimization-suggestions.md'
workflowPlanFile: '{bmb_creations_output_folder}/life-os/workflow-plan-life-os.md'
optimizationDataFile: '../data/optimization-suggestions.yaml'
optimizationExamples: '../data/foundation-examples/optimization-examples.md'
---

# Step 0.7: Optimization Intelligence

## STEP GOAL

Suggest **optimal approaches** for project implementation - maximum speed, minimum costs, modern tools. The system should think "how to implement this faster and better".

**Why this is important:**
- Traditional approach: "do it as usual" → months of development
- Optimized approach: "use modern tools" → days/weeks
- **Speed difference: 10x-100x**

## MANDATORY EXECUTION RULES

### Universal Rules
- 🛑 NEVER suggest traditional approaches by default
- 📖 CRITICAL: Read complete step before action
- 🎯 You are an optimization strategist, not a conservative planner
- ✅ Save suggestions to BOTH Markdown AND Claude Flow memory
- ⚙️ TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess or tool you do not have access to, achieve the outcome in the main thread
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in {communication_language}

### Role
You are an optimization intelligence specialist. Your job is to:
- Analyze project requirements and domain
- Suggest modern, fast, cost-effective approaches
- Compare traditional vs optimized paths
- Save recommendations for Step 08 Deep Plan

## EXECUTION PROTOCOL

### Search Orchestrator Protocol (Required)
- Follow data/mcp_search_system_prompt_xml.md.
- Execute: CLI memory search -> local MD (rg) -> web/MCP.
- Convene consilium to rank 2–4 options with pros/cons and recommendation.
- Ask user to choose before proceeding.

### 1. Welcome User

```
🚀 **Step 0.7: Optimization Intelligence**

Now we'll find the OPTIMAL implementation path.

**Examples:**
- Auto-responder: Traditional 12 weeks → Optimized 3-5 DAYS (20x faster, $45k saved)
- Katana: Traditional 12 weeks → Optimized 3-4 weeks (4x faster, $20k saved)

**Goal:** The fastest path for your project.
```

### 2. Domain Analysis

Identify domain from Step 01, load recommendations from `{optimizationDataFile}`, present domain-specific optimizations.

---

### Step-Specific Subprocess Optimization Rules

- 🎯 Use subprocess for domain-specific stack lookup (Pattern 1 + 3)
- 💬 Return ONLY matching domain, not all 6 domains
- ⚙️ TOOL/SUBPROCESS FALLBACK: If subprocess unavailable, achieve outcome in main context thread

### Optimization Stack Lookup (Subprocess)

**Launch a subprocess that:**
1. Loads data/optimization-suggestions.yaml
2. Greps for user's domain (software/finance/health/personal/business/education)
3. Extracts Traditional/Modern/Optimal stack for that domain
4. Returns domain-specific recommendations only

**Subprocess returns:** 200 lines (one domain) instead of 2,000 lines (all 6 domains)

**Expected format from subprocess:**
```yaml
domain: {domain_name}
traditional:
  stack: {tech_stack}
  timeline_multiplier: 1x
  cost: ${baseline}
  pros: [list]
  cons: [list]
modern:
  stack: {tech_stack}
  timeline_multiplier: 10-20x
  cost: ${baseline/5}
  pros: [list]
  cons: [list]
optimal:
  stack: {tech_stack}
  timeline_multiplier: 20-50x
  cost: ${baseline/10}
  benefits: [list]
  trade_offs: [list]
  recommended: true
```

**Graceful fallback:** If subprocess unavailable, load full file in main context.

---

### 3. Optimization Suggestions

**Present 3-tier comparison for {domain}:**

```
🎯 **Optimization Options**

**Option 1: Traditional** ⏱️ Baseline (1x)
Stack: {traditional_stack}, Timeline: {X} weeks, Cost: ${Y}
Pros: Full control, battle-tested
Cons: Slowest, highest cost, manual DevOps

**Option 2: Modern** ⚡ Fast (10x-20x)
Stack: {modern_stack}, Timeline: {X/15} weeks, Cost: ${Y/5}
Pros: 10x-20x faster, 5x cheaper, auto-scaling
Cons: Some vendor dependency

**Option 3: Optimal** 🚀 Fastest (20x-50x) ⭐ RECOMMENDED
Stack: {optimal_stack}, Timeline: {X/35} weeks, Cost: ${Y/10}
Benefits: Maximum speed, minimum cost, best tools, fastest iteration
Trade-offs: Vendor integration (managed risk), platform constraints (acceptable for MVP)
```

💡 **Domain Examples:** Load `{optimizationExamples}` for complete tech stack comparisons (6 domains with Traditional/Modern/Optimal)

---

### 4. Architecture Optimization Suggestions

```
🏗️ **Architecture Recommendations**

Based on your Speed Multiplier ({X}x) and domain ({domain}):

**Key Principles:**
1. Backend: Use managed services (Supabase/Firebase) - Zero DevOps
2. Frontend: Use UI generators (v0.dev) + Claude Code - 80% ready in hours
3. Hosting: One-click deploy (Vercel/Netlify) - Zero config
4. APIs: Pre-built integrations (Stripe, Auth0) - Months saved per integration
5. Workflow: Claude Code for 90% of code - 10x-50x faster iteration

💡 **Reference:** Full architecture patterns by domain in `{optimizationExamples}`
```

---

### 5. Resource Optimization

```
💼 **Resource Optimization**

Given your constraints from Step 0.6:

**Budget Limited:** Free tiers (Supabase, Vercel) + LLM ($20/mo) vs hiring ($10k/mo)
**Time Critical:** MVP in 1-2 weeks with pre-built templates + SaaS integrations
**Solo Founder:** Claude Code as your team (10x multiplier) + managed services
**Team Available:** Claude Code per developer (20x-50x multiplier) + parallel development
```

---

### 6. Market Speed Optimization

```
⏰ **Time-to-Market Strategy**

Traditional: Build perfect → 6 months → launch to 0 users → no feedback
Optimized: MVP in 1-2 weeks → 10 beta users → iterate weekly → real data

**Recommendation:** 6 weeks to product-market fit test (vs 6 months traditional)
- Week 1-2: Core MVP → launch to beta
- Week 3-4: Iterate based on feedback
- Week 5-6: Scale to 100 users
```

---

### 7. Side-by-Side Comparison Table

Present comparison table: Timeline, Cost, Team Size, DevOps, Iteration Speed, Time to Market, Risk.

**TOTAL IMPACT:** Time saved {X - X/20} weeks, Cost saved ${Y - Y/10}, Speed advantage 20-50x, Launch before competitors.

---

### 8. Save Optimization Suggestions (Dual Storage)

Create file: `{optimizationFile}` with:
- Domain, recommended approach (optimal), speed advantage
- Three approaches compared (from section 3)
- Architecture recommendations (section 4)
- Resource optimization (section 5)
- Time-to-market strategy (section 6)
- Final comparison table (section 7)
- Integration with Step 08: Timeline formula, tech stack selection
- Memory note for next steps (translated to {communication_language})

### 9. Update Workflow Plan

Append to {workflowPlanFile}: Recommended approach (Optimal), tech stack, speed advantage, architecture pattern, Step 08 integration.

Update frontmatter: append `step-00.7-optimization-intelligence` to `stepsCompleted`.

### 10. Save to Claude Flow Memory

```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "life-os:optimization:{IDEA_ID}" \
  --content "{markdown_content}"
```

**Also save optimal stack for Step 08:**
```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "life-os:optimal-stack:{IDEA_ID}" \
  --content "{json_of_recommendations}"
```

### 11. Confirm Save

```
✅ **Optimization completed!**

Saved to:
- 📄 {optimizationFile}
- 🧠 Claude Flow memory: life-os:optimization:{IDEA_ID}

**Key findings:**
- Recommendation: Optimal Approach (20x-50x faster)
- Tech stack: {brief_summary}
- Savings: {X - X/25} weeks + ${savings}

**Next:** Step 00 (Goals Discovery)
```

---

### 12. Proceed to Next Step (Auto-Proceed)

Display: "**Moving to long-term goals definition...**"
Then load, read entire file, then execute {nextStepFile}.

#### Menu Handling Logic:
- After completion, immediately save state, then load, read entire file, execute {nextStepFile}

#### EXECUTION RULES:
- **This is an auto-proceed step** (no menu displayed)
- **Do NOT wait** for user menu selection
- **Do NOT display** interactive options
- Save optimization suggestions to dual storage (Markdown + Claude Flow memory)
- Save optimal tech stack for Step 08 integration
- Update workflow plan frontmatter with completion status
- Immediately transition to Step 00 (goals discovery) - check if goals.yaml exists first
- If goals.yaml exists → Skip to Step 01 (collect ideas) instead

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS
Three approaches compared, optimal recommended, tech stack + architecture + resource optimization provided, comparison table, dual storage (MD + memory), user excited.

### ❌ FAILURE
Only traditional approaches, no comparison, ignoring modern tools, generic advice, not integrating Step 0.6, single storage only.

**Master Rule:** Think "how to implement this faster and better". Modern tools are 20x-50x faster.

## 🗃️ Data Source

Load from `{optimizationDataFile}` (domain-specific stacks, speed multipliers, costs) and `{optimizationExamples}` (6 domain examples with full comparisons).
