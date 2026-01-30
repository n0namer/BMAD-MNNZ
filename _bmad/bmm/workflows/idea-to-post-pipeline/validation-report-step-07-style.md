# Instruction Style Check - Validation Report

**Date:** 2026-01-30
**Workflow:** idea-to-post-pipeline
**Validator:** BMAD Workflow Validator Agent

---

## Workflow Domain

- **Type:** Creative content creation / Personal development / Collaborative content pipeline
- **Appropriate style:** **Intent-Based** (DEFAULT)
- **Rationale:** This workflow involves creative content generation (Telegram posts), collaborative user-AI interaction, personal brand development, and exploration of content angles. All of these domains fall under intent-based instruction as they require flexibility, adaptability to user preferences, and creative interpretation.

---

## Per-File Analysis

### Core Entry Files

**workflow.md:**
- Style: **Intent-Based**
- Appropriate: ✅
- Notes: Uses goal-oriented language ("Transform raw ideas into structured posts"), describes roles and relationships ("Content Strategist & Automation Engineer collaborating"), explains purpose rather than prescribing exact behaviors.

**step-00-menu.md:**
- Style: **Mixed (Intent-Based with Prescriptive elements)**
- Appropriate: ✅
- Notes: Contains intent-based goals ("Present all 4 operational modes clearly") but includes some prescriptive display templates. The prescriptive elements are appropriate here as they define UI consistency rather than restrict creative output.

**step-01-init.md:**
- Style: **Intent-Based**
- Appropriate: ✅
- Notes: Goals are described in terms of outcomes ("welcome the user, explain the workflow structure"), uses flexible language ("warm, inviting language").

**step-01b-continue.md:**
- Style: **Intent-Based**
- Appropriate: ✅
- Notes: Focuses on goals ("load the saved session state", "restore the user's context"), allows for flexible execution based on session state.

---

### CREATE Mode Files (steps-c/)

**c-00-menu.md:**
- Style: **Intent-Based**
- Appropriate: ✅
- Notes: Menu structure is intent-based ("Present CREATE Mode options and route user"), display templates are guides not rigid scripts.

**c-01-add-idea.md:**
- Style: **Intent-Based**
- Appropriate: ✅
- Notes: Encourages open input ("Расскажи мне идею для контента. Может быть что угодно"), validates against criteria rather than prescribing exact formats.

**c-02a-load-ideas.md, c-02b-select-idea.md:**
- Style: **Intent-Based**
- Appropriate: ✅
- Notes: Selection and loading are goal-oriented, user has freedom to choose.

**c-03c-draft.md:**
- Style: **Intent-Based**
- Appropriate: ✅
- Notes: Content generation is described by goals ("Generate 3 draft variations"), provides examples as inspiration rather than exact templates to copy.

**c-05c-apply-edits.md, c-05d-finalize.md:**
- Style: **Intent-Based**
- Appropriate: ✅
- Notes: Editing process is flexible, focused on improvement goals.

**c-06c-generate.md, c-06d-save.md:**
- Style: **Intent-Based**
- Appropriate: ✅
- Notes: Merge and save operations described by outcomes.

**c-08a-backup.md, c-08b-maintenance.md:**
- Style: **Intent-Based**
- Appropriate: ✅
- Notes: Administrative operations use goal-based language.

---

### EDIT Mode Files (steps-e/)

**e-00-menu.md:**
- Style: **Intent-Based**
- Appropriate: ✅
- Notes: Philosophy statement ("70% AI autonomy", "30% user approval") describes intent, not rigid scripts.

**e-01a-select-posts.md, e-01b-improvements.md:**
- Style: **Intent-Based**
- Appropriate: ✅
- Notes: Selection and improvement processes are goal-oriented.

**e-02a.md, e-02b-evaluate.md, e-02c.md:**
- Style: **Intent-Based**
- Appropriate: ✅
- Notes: Evaluation uses criteria-based approach, not prescriptive exact wording.

**e-03a-select-post.md, e-03b-generate.md, e-05c-compare.md:**
- Style: **Intent-Based**
- Appropriate: ✅
- Notes: A/B testing and comparison are exploratory, not prescriptive.

**e-07a-load-history.md, e-08a-select.md:**
- Style: **Intent-Based**
- Appropriate: ✅
- Notes: History and comparison operations focus on goals.

---

### VALIDATE Mode Files (steps-v/)

**v-00-menu.md:**
- Style: **Intent-Based**
- Appropriate: ✅
- Notes: Despite being quality assurance, uses goal-based language ("automated quality assurance mode - 90% of the work is done automatically, you review results").

**v-01b-checks.md:**
- Style: **Mixed (Intent-Based with Criteria-Based elements)**
- Appropriate: ✅
- Notes: Quality checks use criteria (hook strength, problem clarity, etc.) which is appropriate for validation. These are evaluation criteria, not prescriptive scripts. The pass/fail logic is based on goals achieved, not exact wording.

**v-02b-audit.md, v-03b-analyze.md, v-04b-audit.md:**
- Style: **Intent-Based with Criteria**
- Appropriate: ✅
- Notes: Audit and analysis use quality dimensions, not rigid scripts.

**v-05b-predict.md, v-06b-batch-checks.md:**
- Style: **Intent-Based**
- Appropriate: ✅
- Notes: Prediction and batch operations are goal-oriented.

**v-07b-checks.md:**
- Style: **Intent-Based**
- Appropriate: ✅
- Notes: Idea validation uses flexible criteria.

---

### YOLO Mode Files (steps-yolo/)

**yolo-01-input.md:**
- Style: **Intent-Based**
- Appropriate: ✅
- Notes: Excellent intent-based design. Accepts "flexible natural language" input, explains "Think of it as a smart parser that understands flexible natural language instructions."

**yolo-01b-ideas-input.md:**
- Style: **Intent-Based**
- Appropriate: ✅
- Notes: Idea input is flexible and exploratory.

**yolo-02-parallel-execute.md:**
- Style: **Intent-Based**
- Appropriate: ✅
- Notes: Parallel execution described by goals ("Execute all requested operations in parallel"), implementation details are flexible.

**yolo-03-self-check.md:**
- Style: **Intent-Based**
- Appropriate: ✅
- Notes: Self-checking is goal-oriented (quality improvement).

**yolo-04-auto-improve.md:**
- Style: **Intent-Based**
- Appropriate: ✅
- Notes: Auto-improvement focuses on quality goals.

**yolo-05-variants.md:**
- Style: **Intent-Based**
- Appropriate: ✅
- Notes: Variant generation is creative and exploratory.

**yolo-06-summary.md:**
- Style: **Intent-Based**
- Appropriate: ✅
- Notes: Summary presentation is goal-oriented ("Present complete results with all created posts").

---

### Subprocess Files (subprocesses/)

**subprocess-parallel-research.md:**
- Style: **Intent-Based**
- Appropriate: ✅
- Notes: Technical orchestration described by goals and outcomes, not rigid step-by-step prescriptions.

**subprocess-parallel-write.md, subprocess-batch-validation.md:**
- Style: **Intent-Based**
- Appropriate: ✅
- Notes: Parallel operations described by architecture and goals.

**subprocess-auto-fix.md, subprocess-variant-generation.md:**
- Style: **Intent-Based**
- Appropriate: ✅
- Notes: Auto-fix and variant generation are exploratory processes.

---

### Template and Checklist Files

**templates/checklists/post-quality-checklist.md:**
- Style: **Criteria-Based (appropriate subset of Prescriptive)**
- Appropriate: ✅
- Notes: This is a quality checklist with specific criteria (hook strength, problem clarity, CTA). Checklists appropriately use specific criteria for evaluation, but they describe goals to achieve ("Hook сильный и привлекательный") not exact wording to use.

**templates/checklists/idea-validation-checklist.md:**
- Style: **Criteria-Based**
- Appropriate: ✅
- Notes: Validation criteria are goal-oriented.

**templates/checklists/edit-improvements-checklist.md:**
- Style: **Criteria-Based**
- Appropriate: ✅
- Notes: Improvement criteria focus on outcomes.

**templates/checklists/engagement-checklist.md:**
- Style: **Criteria-Based**
- Appropriate: ✅
- Notes: Engagement criteria are exploratory.

**templates/checklists/copy-audit-checklist.md:**
- Style: **Criteria-Based**
- Appropriate: ✅
- Notes: Copy audit uses quality dimensions, not prescriptive scripts.

---

### Reference Files

**data/reference/interaction-styles.md:**
- Style: **Intent-Based**
- Appropriate: ✅
- Notes: Excellent meta-documentation. Describes interaction philosophies (50/50 collaborative, 70/30 autonomous, etc.) which are inherently intent-based.

**data/reference/timing-sla.md:**
- Style: **Intent-Based**
- Appropriate: ✅
- Notes: SLA expectations are goal-based targets.

**data/reference/success-criteria.md:**
- Style: **Intent-Based**
- Appropriate: ✅
- Notes: Success metrics are outcome-focused.

**data/reference/faq.md:**
- Style: **Intent-Based**
- Appropriate: ✅
- Notes: FAQ uses exploratory, explanatory language.

---

## Positive Findings

### Excellent Intent-Based Examples

1. **YOLO Mode Input Parsing (yolo-01-input.md):**
   > "Здесь ты можешь сказать мне что угодно" and "я понимаю гибкие форматы!"

   This is excellent intent-based design that encourages flexible user input rather than prescribing exact formats.

2. **Role Descriptions (workflow.md):**
   > "Your Role: You are a Content Strategist & Automation Engineer collaborating with a solo entrepreneur..."

   Describes roles and relationships rather than scripted behaviors.

3. **Interaction Styles Matrix (interaction-styles.md):**
   > Defines modes by autonomy levels (50/50, 70/30, 90/10, 100%) which describe intent and philosophy, not rigid scripts.

4. **Validation Criteria (v-01b-checks.md):**
   > Uses criteria like "Hook strength: Strong/Weak" which evaluate goals achieved, not exact wording compliance.

5. **Creative Prompts (c-01-add-idea.md):**
   > "Может быть что угодно: Проблема которую ты видишь, Инсайт который хочешь поделиться..."

   Encourages open exploration rather than prescribing what to input.

### Well-Balanced Mixed Sections

1. **Menu Display Templates:** Some files contain display templates (ASCII art menus) which appear prescriptive but are appropriate for UI consistency. These are presentation guidelines, not content restrictions.

2. **Quality Checklists:** Validation checklists use specific criteria which could seem prescriptive, but they evaluate outcomes ("Hook сильный и привлекательный") rather than requiring exact wording.

---

## Issues

### Minor Observations (No Issues Requiring Fix)

1. **Execution Rules Sections:** Many files contain "MANDATORY EXECUTION RULES" which could appear prescriptive, but these are workflow orchestration rules (when to halt, when to proceed) rather than content creation restrictions. This is appropriate for workflow management.

2. **Display Templates:** Some display templates include specific Russian text. This is appropriate as it provides localization consistency, not content restriction.

3. **No Compliance/Legal/Medical/Financial Content:** The workflow does not contain any domains that would require Prescriptive style (legal disclaimers, medical advice, financial compliance). This is correct for a creative content workflow.

### No Issues Found

After thorough analysis, no inappropriate instruction styles were found. All files appropriately use Intent-Based instruction style for this creative/collaborative domain.

---

## Summary Statistics

| Category | Count | Style | Appropriate |
|----------|-------|-------|-------------|
| Core Entry Files | 4 | Intent-Based | ✅ 4/4 |
| CREATE Mode (steps-c/) | 10+ | Intent-Based | ✅ All |
| EDIT Mode (steps-e/) | 24+ | Intent-Based | ✅ All |
| VALIDATE Mode (steps-v/) | 8+ | Intent-Based/Criteria | ✅ All |
| YOLO Mode (steps-yolo/) | 7 | Intent-Based | ✅ All |
| Subprocesses | 7 | Intent-Based | ✅ All |
| Templates/Checklists | 10 | Criteria-Based | ✅ All |
| Reference Files | 4 | Intent-Based | ✅ All |

---

## Status: ✅ PASS

**Conclusion:** The idea-to-post-pipeline workflow correctly uses Intent-Based instruction style throughout. This is the appropriate style for creative content creation, collaborative workflows, and exploratory content generation.

- No Prescriptive elements found where Intent-Based should be used
- Criteria-based validation checklists are appropriate for quality assurance
- Menu templates and display formats are UI consistency elements, not content restrictions
- Excellent examples of flexible, goal-oriented instruction design

**Recommendation:** No changes needed. The workflow demonstrates best practices for Intent-Based instruction design in a creative domain.
