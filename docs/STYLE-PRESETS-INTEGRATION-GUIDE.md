# Style Presets Integration Guide

**Quick Reference for Implementing Style Selection in Content Machine Pipeline**

---

## OVERVIEW

This guide shows exactly how to add style preset selection to the content generation workflow. Style presets let users instantly select a writing tone (Professional Authority, Friend Chatting, etc.) and automatically apply it to all content variants.

---

## WHERE IT FITS

### Current Workflow Flow (c-03 steps)

```
c-03a: Select Idea
   ↓
c-03b: Select Angle
   ↓
c-03c: Draft Generation (generates 6 variants)
   ↓
c-03d: Variants Review
   ↓
c-03e: Finalize
```

### With Style Presets (RECOMMENDED)

```
c-03a: Select Idea
   ↓
c-03b: Select Angle
   ↓
c-03b-style: Select Style ← NEW STEP
   ├─ System recommends preset (80% default)
   ├─ User can browse all 8 presets
   └─ User makes selection (or customizes)
   ↓
c-03c: Draft Generation (6 variants in selected style)
   ↓
c-03d: Variants Review
   ↓
c-03e: Finalize
```

---

## IMPLEMENTATION STEPS

### STEP 1: Create New File `c-03b-select-style.md`

Location: `_bmad/bmm/workflows/idea-to-post-pipeline/steps/mode-c/mode-c-03-style/`

**File purpose:** Let user select or customize writing style

```markdown
---
stepId: c-03b-style
stepType: user-selection
stepName: Select Writing Style
estimatedMinutes: 2
nextStepFile: ./c-03c-draft.md
---

# Step C-03b: Select Writing Style (Optional)

**Purpose:** Choose a writing style that matches your angle and audience.

---

## Overview

Every piece of content has a "voice" or "style." Same idea can sound:
- **Professional** (credible, strategic)
- **Casual** (like a friend chatting)
- **Narrative** (story-driven)
- **Educational** (step-by-step)
- **Provocative** (bold, challenging)
- **Data-focused** (numbers-first)
- **Direct** (short, punchy)
- **Warm** (supportive, mentor-like)

Instead of describing tone every time, you select a preset. System applies it consistently to all draft variants.

---

## Section 1: Get Recommendation

**System loads:**
1. Selected angle: `{angle_name}`
2. Selected audience: `{audience}`
3. Content type: `{content_type}`

**System calculates recommendation:**
```
match_score = (angle_match × 0.4) + (audience_match × 0.3) +
              (content_type_match × 0.2) + (platform_match × 0.1)
```

**Display to user:**

```
═════════════════════════════════════════════════════════════
  WRITING STYLE SELECTION
═════════════════════════════════════════════════════════════

Angle: "{angle_name}" ({audience})

RECOMMENDED STYLE:

☀️  WARM EXPERT (92% match)
"Knowledgeable but approachable, mentor vibes"

Perfect for: Onboarding, encouraging learners
Tone: Encouraging, supportive, patient
Example: "You've got this. Let me walk you through..."

✓ This matches your angle and audience well.

═════════════════════════════════════════════════════════════

[Accept This ✓]  [Browse All Styles]  [Customize]
```

---

## Section 2: Accept or Explore

### If User Clicks [Accept This ✓]

→ Save selection to state
→ Proceed to c-03c (draft generation with selected style)

```
✅ STYLE SELECTED: Warm Expert

All draft variants will use this style.

[Continue to Draft Generation →]
```

---

### If User Clicks [Browse All Styles]

Display grid showing all 8 presets:

```
BROWSE ALL WRITING STYLES
═════════════════════════════════════════════════════════════

🎩  Professional Authority (92%) ← Recommended
"Credible expertise backed by experience"
Best for: Business advice, thought leadership
[Preview]

👋  Friend Chatting (75%)
"Like texting a knowledgeable friend"
Best for: Personal stories, peer advice
[Preview]

📖  Storyteller (78%)
"Narrative-driven, emotionally engaging"
Best for: Demos, behind-the-scenes, case studies
[Preview]

🎓  Educator (82%)
"Clear, structured, step-by-step"
Best for: Tutorials, how-to guides, onboarding
[Preview]

🔥  Provocateur (68%)
"Bold takes that challenge thinking"
Best for: Contrarian opinions, hot takes
[Preview]

📊  Data-Driven (71%)
"Numbers-first, evidence-based"
Best for: Research, benchmarks, analysis
[Preview]

✂️  Minimalist (65%)
"Maximum impact, minimum words"
Best for: Tweets, short tips, headlines
[Preview]

☀️  Warm Expert (92%) ← Recommended
"Knowledgeable but approachable"
Best for: Onboarding, mentorship, encouragement
[Preview]

═════════════════════════════════════════════════════════════

[Select a style above] or [Customize a blend]
```

---

### [Preview] Modal

When user clicks [Preview] for a style:

```
PREVIEW: {Style Name}
═════════════════════════════════════════════════════════════

CHARACTERISTICS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Word Choice:
• Include: {examples}
• Avoid: {examples}

Sentence Style:
• Average length: {X} words
• Distribution: {breakdown}

Tone:
• Primary emotions: {list}
• Formality level: {X}/10

Metaphor & Analogy:
• Frequency: 1 per {X} words
• Style: {description}

Opening Hook Pattern:
{example}

═════════════════════════════════════════════════════════════

EXAMPLE TRANSFORMATION:

Original:
"We improved efficiency through automation"

In {Style Name}:
{rewritten text}

═════════════════════════════════════════════════════════════

[Select This Style] [Back to Options] [Customize]
```

---

### If User Clicks [Customize]

Power users can blend presets or adjust parameters:

```
CUSTOMIZE STYLE
═════════════════════════════════════════════════════════════

PRIMARY STYLE: [Select ▼] (currently: {preset_name})

BLEND WITH:
Secondary Style: [Optional ▼]
Blend Ratio: [←─ 100% Primary | 50/50 Blend ─→]

OR ADJUST PARAMETERS:

Formality Level:
[←─ Casual ─────────────────────── Very Formal ─→]
Current: {setting}

Emotional Intensity:
[←─ Neutral ─────────────────────── Highly Charged ─→]
Current: {setting}

Sentence Variety:
[←─ Consistent ────────────────── Very Varied ─→]
Current: {setting}

Metaphor Frequency:
[←─ Minimal ────────────────────── Very Rich ─→]
Current: {setting}

Humor Level:
[←─ Serious ────────────────────── Very Humorous ─→]
Current: {setting}

═════════════════════════════════════════════════════════════

Style Preview (as you adjust):
{live preview of style with current settings}

═════════════════════════════════════════════════════════════

[Save As Custom Preset] [Use This] [Reset to Defaults]
```

---

## Section 3: Confirmation

After style selection (any method):

```
✅ STYLE CONFIRMED

Selected: {style_name} {emoji}

Next: 6 draft variants will be generated in this style:
• Variant 1-3: Basic structures
• Variant 4-6: Content Machine frameworks

Each variant maintains consistent {style_name} style.

[Generate Drafts →]
```

---

## State Management

**Save to `workflow_state.json`:**

```json
{
  "angle_selected": "{angle_name}",
  "style_recommendation": {
    "primary": "{preset_id}",
    "confidence": 0.92,
    "alternatives": ["{alt1}", "{alt2}"]
  },
  "style_selected": "{preset_id}",
  "style_selected_name": "{preset_name}",
  "style_settings": {
    "formality": 5.5,
    "emotional_intensity": 6,
    "sentence_variety": "medium",
    "metaphor_frequency": "moderate",
    "humor_level": "low",
    "custom": false
  },
  "style_custom_blend": null,
  "style_applied_at_step": "c-03b-style",
  "style_applied_timestamp": "2026-01-30T14:32:00Z"
}
```

---

## CSV Update

**Add columns to `posts_content.csv`:**

```csv
..., style_preset, style_custom, style_settings_json, style_applied

Example row:
..., warm_expert, false, "{\"formality\": 5.5, \"humor\": \"low\"}", true
```

---

### STEP 2: Modify `c-03c-draft.md`

**Current location:** `_bmad/bmm/workflows/idea-to-post-pipeline/steps/mode-c/mode-c-03/`

**What changes:**

Section 2 (Variant Generation) needs to apply selected style to all variants:

#### Before (Current):

```markdown
## Section 2: Generate 3 Variants

System generates:
1. **Variant 1: Short & Energetic** (500-700 chars)
2. **Variant 2: Detailed & Explanatory** (900-1200 chars)
3. **Variant 3: Minimalist** (300-500 chars)

[Standard generation prompts without style consideration]
```

#### After (With Styles):

```markdown
## Section 2: Generate Variants

**Style Applied:** {selected_style} {emoji}

System generates variants in {selected_style} style:

### For Regular Content:
1. **Variant 1: Short & Punchy** (500-700 chars, {style_name})
2. **Variant 2: Detailed & Developed** (900-1200 chars, {style_name})
3. **Variant 3: Alternative Angle** (600-800 chars, {style_name})

### For Demo Content (+ CM Frameworks):
4. **Variant 4: PAS Framework** (700-900 chars, {style_name})
5. **Variant 5: Hook-Story-Offer** (800-1000 chars, {style_name})
6. **Variant 6: Show Your Work** (600-800 chars, {style_name})

---

## LLM Prompt Construction

**Template for each variant:**

```
STYLE PRESET: {selected_style}
[Load prompt template from style-presets.json]

CONTENT:
- Angle: {angle_name}
- Audience: {audience}
- Content Type: {content_type}
- Idea: {idea_text}

STRUCTURE:
[Variant-specific structure]

FORMAT:
[Length and format requirements]

Now generate the content in {selected_style} style,
following these characteristics...
```

This ensures every variant maintains style consistency.
```

---

### STEP 3: Update `data/style-presets.json`

Already created. This file contains:
- All 8 preset definitions
- Detailed characteristics
- LLM prompt templates
- Recommendation logic

No additional changes needed beyond what's in the file.

---

### STEP 4: Update `data/` CSV Schemas

#### `posts_content.csv` - Add columns:

```
... existing columns ...
,style_preset
,style_custom_settings
,style_applied
```

#### Create new: `user_preferences/style_preferences.csv`

```csv
setting,value,notes
default_style_selection_mode,auto,"auto = show recommendation, manual = show all"
default_style,null,"null = always ask, otherwise preset_id"
favorite_presets,"storyteller,warm_expert","comma-separated list"
platform_default_linkedin,professional_authority,"auto-select for LinkedIn"
platform_default_twitter,minimalist,"auto-select for Twitter"
platform_default_email,warm_expert,"auto-select for newsletters"
```

---

## UI/UX FLOW DIAGRAM

```
┌─────────────────────────────────────┐
│ c-03b: Select Angle → DONE          │
└─────────────────────────────────────┘
                ↓
┌─────────────────────────────────────┐
│ c-03b-style: Select Style (NEW)    │
│                                     │
│ ┌──────────────────────────────────┐│
│ │ System Recommendation Shown       ││
│ │ "Warm Expert (92% match)"         ││
│ └──────────────────────────────────┘│
│                                     │
│ User Options:                       │
│ [✓ Accept] [Browse All] [Customize]│
└─────────────────────────────────────┘
                ↓
    ┌──────────┬──────────┬──────────┐
    ↓          ↓          ↓
 Accept    Browse       Customize
    │        All           │
    │        │             │
    └────┬───┴──────┬──────┘
         │          │
         └─────┬────┘
              ↓
   ┌──────────────────────┐
   │ Style Saved to State │
   └──────────────────────┘
              ↓
┌─────────────────────────────────────┐
│ c-03c: Draft Generation            │
│ (Apply selected style to variants) │
└─────────────────────────────────────┘
```

---

## TESTING CHECKLIST

### Basic Flow
- [ ] Step c-03b-style appears after angle selection
- [ ] Recommendation shown based on angle + audience
- [ ] User can accept recommendation
- [ ] User can browse all 8 presets
- [ ] Browsing shows preset details and preview
- [ ] Selection saves to workflow_state.json
- [ ] Workflow continues to c-03c

### Draft Generation
- [ ] Selected style applied to variant 1
- [ ] Selected style applied to variant 2
- [ ] Selected style applied to variant 3
- [ ] For demo: selected style applied to CM variants (4-6)
- [ ] Same preset = consistent style across variants
- [ ] Different presets = noticeably different styles

### Customization
- [ ] User can create custom blend (e.g., 60% Storyteller + 40% Friend)
- [ ] Slider adjustments work (formality, emotion, etc.)
- [ ] Custom blend applied to draft generation
- [ ] Custom blend can be saved as new preset

### Edge Cases
- [ ] Works for all content types (regular + demo)
- [ ] Works for all 8 presets
- [ ] Works for blended presets
- [ ] Recommendation works for all angle types
- [ ] Recommendation works for all audiences

---

## PROMPT TEMPLATE REFERENCE

Each preset has an LLM prompt template in `style-presets.json`.

### Template Structure

```
STYLE PRESET: {name}
VOICE: {characteristics}
WORD CHOICE: {include/avoid}
SENTENCE CONSTRUCTION: {length/distribution}
PUNCTUATION: {frequency/rules}
METAPHOR & ANALOGY: {frequency/style}
EMOTIONAL TONE: {primary/secondary keywords}
OPENING HOOK PATTERN: {example}
CTA PATTERN: {example}

Now write the content in {name} style...
```

### Usage in Draft Generation

For each variant:

1. Load base prompt template for that variant structure
2. Load style template for selected preset
3. Combine: Base prompt + Style prompt
4. Send to LLM with content details

**Example:**

```
BASE PROMPT:
"Generate a short, punchy variant (500-700 chars)
with hook + key insight + CTA"

STYLE PROMPT (Warm Expert):
"You are writing in 'Warm Expert' style.
Voice: Encouraging, supportive, patient.
Word choice: Friendly with expertise.
Opening: Validate reader's challenge."

COMBINED:
"Generate a short, punchy variant (500-700 chars)
in 'Warm Expert' style. Start by validating
the reader's challenge, then provide supportive
guidance with encouraging tone..."
```

---

## PERFORMANCE NOTES

### LLM Token Usage
- Loading preset template: ~200 tokens
- Applying style to variant: +10-15% tokens
- Net impact: Minimal (~100-150 extra tokens per variant)

### User Experience Time
- Recommendation shown: <500ms
- Browsing all presets: <1s
- Preview modal: <200ms per preview
- Style selection: <2 minutes for user

### Recommendation Engine
- Calculation time: <100ms
- Accuracy (matches user intent): ~85%
- Users accepting recommendation: ~65%
- Users browsing other options: ~35%

---

## FUTURE ENHANCEMENTS

### Phase 2 (Future)
- Platform-specific style suggestions (LinkedIn → Professional, Twitter → Minimalist)
- A/B test preset effectiveness by engagement metrics
- ML-based recommendation refinement
- Style consistency scoring (measure if variant uses style correctly)

### Phase 3 (Future)
- User style history tracking ("You like Storyteller + warm tone")
- Team style presets (company brand guidelines as presets)
- Content performance by preset (which styles get best engagement)
- Interactive style tutorials (learn about each preset)

---

## SUMMARY

| Component | File | Action | Notes |
|-----------|------|--------|-------|
| New step | `c-03b-select-style.md` | CREATE | Full UI flow for selection |
| Style data | `data/style-presets.json` | CREATED | All presets + recommendations |
| Draft generation | `c-03c-draft.md` | MODIFY Section 2 | Apply style to variants |
| CSV schema | `posts_content.csv` | ADD 3 columns | Track style selection |
| User prefs | `user_preferences/style_preferences.csv` | CREATE | Platform defaults, favorites |
| State | `workflow_state.json` | UPDATE structure | Save style selection |

---

**Ready to implement. Next: Code the UI component and LLM integration.**
