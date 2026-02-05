# Final Polish - Coherence Check Details

**Reference:** Used by `steps-c/step-08.5-final-polish.md`

**Purpose:** Detailed protocols for 5-dimension coherence review

---

## 5 Coherence Dimensions (Detailed Protocols)

### Dimension 1: Timeline Consistency

**What to check:**
1. ✅ Do Foundation Steps (0.5/0.6/0.7) data align?
   - Project stage completion % used in timeline calculations?
   - Speed multiplier reflected in timeline estimates?
   - Optimization suggestions considered in final timeline?

2. ✅ Does Deep Plan timeline match scoring assumptions?
   - If scoring assumes "12 weeks traditional", does Deep Plan reflect adjusted timeline (e.g., 3-4 days with LLM 20x)?
   - Are L5/L6 task durations realistic given speed multiplier?

3. ✅ Do all timeline references use same units (weeks/days/hours)?
   - No mixing "12 weeks" in one place and "3 months" in another
   - Consistent rounding (e.g., always "3-4 days" not "3.5 days" then "4 days")

**Common Issues:**
- ❌ Foundation says "Speed Multiplier 20x" but timeline uses traditional 1x calculations
- ❌ Project stage shows "50% complete" but timeline doesn't account for existing work
- ❌ Optimization suggests "Supabase for instant backend" but timeline includes "2 weeks backend setup"

**How to report:**
```
Timeline Consistency: [✅ PASS / ⚠️ ISSUES FOUND]

Issues:
- Issue: Deep Plan shows "12 weeks" but Step 0.6 Speed Multiplier is 20x
  Location: Section "Deep Plan Timeline", L2 phases
  Fix: Change "12 weeks" → "3-4 days (12 weeks ÷ 20x = 3.6 days)"
```

---

### Dimension 2: Goal Alignment

**What to check:**
1. ✅ Does idea align with user's goals (from goals.yaml)?
   - Personal goals referenced and addressed?
   - Project/business goals considered in planning?
   - Partner goals (if multi-stakeholder) acknowledged?

2. ✅ Consilium recommendations consistent with goals?
   - Do specialists address goal-related concerns?
   - If goal is "learn new technology", do specialists recommend learning path?
   - If goal is "maximize profit", do specialists focus on ROI?

3. ✅ Scoring reflects goal alignment criterion?
   - "Alignment" score matches how well idea fits goals
   - If idea conflicts with personal goals but aligns with business goals → documented and scored appropriately

**Common Issues:**
- ❌ Goals.yaml says "focus on health sphere" but idea is finance project (no explanation)
- ❌ Consilium recommends "spend 40h/week" but personal goals say "max 20h/week available"
- ❌ Scoring gives high "Alignment" score but idea doesn't match any stated goal

**How to report:**
```
Goal Alignment: [✅ PASS / ⚠️ ISSUES FOUND]

Issues:
- Issue: Idea is finance project but goals.yaml shows "health sphere" as top priority
  Location: Step 01 Idea Capture, Goals reference
  Fix: Add explanation: "Finance project serves health goal indirectly (funding for health startup)"
  OR: Lower "Alignment" score from 8/10 to 6/10 to reflect partial fit
```

---

### Dimension 3: Specialist Consistency

**What to check:**
1. ✅ All mentioned specialists have recommendations?
   - No "mentioned but never consulted" specialists
   - If Step 03 says "6 specialists matched", consilium should have 6 perspectives

2. ✅ No contradictions between specialist inputs?
   - Technical Architect says "3 weeks" vs Product Manager says "12 weeks" → which is authoritative?
   - Database Specialist recommends "PostgreSQL" vs Backend Dev recommends "MongoDB" → resolved how?

3. ✅ Consilium reflects all specialist perspectives?
   - If 6 specialists consulted, consilium should synthesize all 6 views
   - Majority opinion documented (e.g., "4/6 specialists recommend Supabase")
   - Dissenting views acknowledged (e.g., "Database Specialist prefers Firebase due to X, but team chose Supabase for Y reason")

**Common Issues:**
- ❌ Step 03 lists "Technical Architect, Product Manager, UX Designer" but consilium only has Technical Architect input
- ❌ Technical Architect says "use Supabase" but Database Specialist says "use Firebase" with no resolution
- ❌ Consilium presents 1 specialist view as team consensus without noting it's 1/6 opinion

**How to report:**
```
Specialist Consistency: [✅ PASS / ⚠️ ISSUES FOUND]

Issues:
- Issue: Step 03 matched 6 specialists but consilium only shows 3 perspectives
  Location: Step 04 Consilium section
  Fix: Add missing specialist perspectives OR clarify "3 specialists consulted deeply, 3 reviewed recommendations"

- Issue: Technical Architect recommends Supabase, Database Specialist recommends Firebase (contradiction)
  Location: Consilium section
  Fix: Add synthesis: "Team chose Supabase (4/6 specialists) over Firebase (1/6) due to better TypeScript support and auto-generated APIs"
```

---

### Dimension 4: Terminology Consistency

**What to check:**
1. ✅ Terms used consistently throughout?
   - Project name same everywhere (e.g., "Katana" not "Katana" then "SaaS for Beauty")
   - Technology stack names consistent (e.g., "Supabase" not "Supabase/Backend/Database service")
   - Role names consistent (e.g., "Technical Architect" not "Tech Lead" then "Solutions Architect")

2. ✅ Russian terms defined (per GLOSSARY-SYSTEM.md)?
   - If using Speed Multiplier → explained with Russian translation on first use
   - If using Точка А → explained with analogy
   - All BMAD-specific terms have glossary entry inline

3. ✅ Abbreviations explained on first use?
   - LLM → "LLM (Large Language Model / Большая Языковая Модель)"
   - MCDA → "MCDA (Multi-Criteria Decision Analysis)"
   - MVP → "MVP (Minimum Viable Product / Минимально Жизнеспособный Продукт)"

**Common Issues:**
- ❌ Project called "Katana" in Step 01, "SaaS for Beauty Industry" in Step 05, "Beauty Tech Platform" in Step 08
- ❌ Speed Multiplier used in calculations but never defined
- ❌ LLM abbreviation used without explanation

**How to report:**
```
Terminology Consistency: [✅ PASS / ⚠️ ISSUES FOUND]

Issues:
- Issue: Project name inconsistent (3 different names used)
  Location: Step 01 (Katana), Step 05 (SaaS for Beauty), Step 08 (Beauty Tech)
  Fix: Standardize to "Katana (SaaS for Beauty Industry)" everywhere

- Issue: "Speed Multiplier" used in calculations but never defined
  Location: Step 0.6 timeline adjustment, Deep Plan timeline
  Fix: Add glossary entry on first use with Russian translation and analogy
```

---

### Dimension 5: Completeness

**What to check:**
1. ✅ All required sections present?
   - Foundation Steps data referenced (0.5, 0.6, 0.7)?
   - Consilium section complete with synthesis and recommendation?
   - Deep Plan with minimum L1-L4 structure?
   - Scoring with all 4 criteria (Complexity, Impact, Alignment, Resource Efficiency)?

2. ✅ No "TBD" or placeholder content?
   - All sections filled with real data (not "TODO: Add specialists")
   - All calculations completed (not "Timeline: TBD after resource assessment")
   - All references resolved (not "See goals.yaml - link TBD")

3. ✅ References to data files correct?
   - goals.yaml path correct and file exists?
   - Template files referenced correctly?
   - Step file references (previousStepFile, nextStepFile) point to actual files?

**Common Issues:**
- ❌ Consilium section says "TBD - need to run Six Hats analysis"
- ❌ Deep Plan only has L1-L2 (missing L3-L4 required for quality gate)
- ❌ Scoring missing "Resource Efficiency" criterion (only 3/4 present)
- ❌ Reference to "goals.yaml" but path is wrong or file doesn't exist

**How to report:**
```
Completeness: [✅ PASS / ⚠️ ISSUES FOUND]

Issues:
- Issue: Deep Plan only has L1-L2 structure (L3-L4 missing)
  Location: Step 08 Deep Plan section
  Fix: Complete Deep Plan to L4 minimum (quality gate requirement)

- Issue: Scoring missing "Resource Efficiency" criterion
  Location: Step 05 Scoring section
  Fix: Add Resource Efficiency scoring (1-10) with calculation

- Issue: Reference to goals.yaml path incorrect
  Location: Frontmatter, Step 00 Goals Discovery
  Fix: Update path to match actual file location
```

---

## Refinement Offer Template

When issues found, use this format:

```
🔧 RECOMMENDED REFINEMENTS

**Issue 1:** [Category - e.g., Timeline inconsistency]
- **Location:** [Specific section in workflow plan]
- **Problem:** [What's wrong - be specific]
- **Suggested Fix:** [Exact change to make]
- **Example:** [Show before/after if helpful]

**Issue 2:** [Category]
- **Location:** [Section]
- **Problem:** [Description]
- **Suggested Fix:** [Change]

[Repeat for all issues found]
```

---

## Quality Assessment Levels

After coherence check, assign overall assessment:

**EXCELLENT (5/5 dimensions pass):**
- All dimensions ✅ PASS
- No issues found
- Plan is coherent, consistent, and complete
- Ready for immediate approval

**GOOD (4/5 dimensions pass):**
- 1 dimension has minor issues (cosmetic)
- Issues are easy to fix (e.g., terminology standardization)
- Plan is structurally sound

**NEEDS REFINEMENT (3/5 or fewer pass):**
- 2+ dimensions have significant issues
- Issues affect plan quality (e.g., timeline contradictions, missing sections)
- Refinements strongly recommended before approval

---

## No Issues Found - Optional Enhancements

If all dimensions pass, offer OPTIONAL cosmetic improvements:

```
✅ NO ISSUES FOUND

The workflow plan is coherent, consistent, and complete.
Ready to mark as COMPLETE.

**Optional enhancements available (cosmetic only):**

1. **Formatting improvements:**
   - Add visual separators (━━━) between major sections
   - Use emoji indicators (✅/❌/⚠️) for status markers
   - Standardize heading levels (## for steps, ### for subsections)

2. **Clarity improvements:**
   - Expand glossary terms inline (add "Physical meaning" for key concepts)
   - Add cross-references between related sections (e.g., "See Step 0.6 for Speed Multiplier details")
   - Include section summaries at end of long sections

3. **Completeness additions:**
   - Add "What changed from initial idea" comparison section
   - Include "Key decisions and rationale" summary
   - Add "Next steps after workflow completion" roadmap

These are OPTIONAL - plan is already high quality.
Apply them only if you want extra polish.
```

---

## Custom Refinement Protocol

When user selects [C] Custom:

1. **Ask specifics:**
   ```
   What would you like to refine?

   Options:
   - [Section name] - Which section to modify?
   - [Change description] - What should change?
   - [Reason] - Why this refinement? (optional)

   Example: "Change Deep Plan timeline from 12 weeks to 3 days because we're using LLM 20x multiplier"
   ```

2. **Confirm understanding:**
   ```
   I understand:
   - Section: [Section name]
   - Change: [From X → To Y]
   - Reason: [Because Z]

   Is this correct? [Y/N]
   ```

3. **Apply change:**
   - Make exact change user requested
   - Do NOT expand scope beyond user's request
   - Update only specified section

4. **Confirm completion:**
   ```
   ✅ Custom refinement applied:
   - Section: [Section]
   - Changed: [What changed]

   Would you like to:
   - [A] Approve plan (done with refinements)
   - [C] Make another custom refinement
   - [R] Review recommended refinements again
   ```

---

**Status:** REFERENCE READY ✅
**Used by:** step-08.5-final-polish.md
**Purpose:** Detailed protocols for systematic coherence review
