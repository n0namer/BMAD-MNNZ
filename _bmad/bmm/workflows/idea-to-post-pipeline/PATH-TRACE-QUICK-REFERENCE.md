# PATH TRACE: QUICK REFERENCE
**Navigation & Flow Maps for idea-to-post-pipeline Workflow**

---

## FLOW MAP: NORMAL CONTENT (11 Steps)

```
┌─────────────────────────────────────────────────┐
│           NORMAL CONTENT FLOW (11 steps)        │
│        (content_type != "demo")                 │
└─────────────────────────────────────────────────┘

    ╔══════════════════════════════════════╗
    ║  START: User selects [3] WRITE POST  ║
    ║  from c-00-menu.md                   ║
    ╚══════════════════════════════════════╝
              │
              ↓
    ┌─────────────────────────────────┐
    │ c-01: Add Idea                  │
    │ - Collect raw idea text         │
    │ - Set content_type = "normal"   │
    │ - Validate criteria             │
    └─────────────────────────────────┘
              │ nextStepFile
              ↓
    ┌─────────────────────────────────┐
    │ c-01b: Dedup Check              │
    │ - Compare against existing      │
    │ - [1] Duplicate → reject        │
    │ - [2] New angle → add related   │
    │ - [3] Different → add & override│
    └─────────────────────────────────┘
              │ Pass: nextStepFile
              ↓
    ┌─────────────────────────────────┐
    │ c-02a: Load Ideas               │
    │ - Display existing ideas        │
    │ - Let user select for research  │
    └─────────────────────────────────┘
              │ nextStepFile
              ↓
    ┌─────────────────────────────────┐
    │ c-02b: Select Idea              │
    │ - User picks which idea         │
    │ - Confirm selection             │
    └─────────────────────────────────┘
              │ nextStepFile
              ↓
    ┌─────────────────────────────────┐
    │ c-02c: Research Execute         │
    │ - Find 5-8 angles               │
    │ - Get sources & facts           │
    │ - Save to ideas_research.csv    │
    │ - ⚠️ SKIP Section 2.5            │
    │   (Section 2.5 = demo only)     │
    └─────────────────────────────────┘
              │ nextStepFile
              ↓
    ┌─────────────────────────────────┐
    │ c-02d: Display Results          │
    │ - Show all angles               │
    │ - Show sources & facts          │
    │ - User selects angle            │
    │ - ⚠️ SKIP Section 2.5            │
    │   (pain points = demo only)     │
    └─────────────────────────────────┘
              │ nextStepFile
              ↓
    ┌─────────────────────────────────┐
    │ c-03a: Select Idea (again)      │
    │ - Confirm idea for writing      │
    └─────────────────────────────────┘
              │ nextStepFile
              ↓
    ┌─────────────────────────────────┐
    │ c-03b: Select Angle             │
    │ - User selects which angle      │
    │                                 │
    │ ✅ CONDITIONAL CHECK:           │
    │ IF content_type == "demo"       │
    │   → Route to c-03b1             │
    │ ELSE (normal)                   │
    │   → Route to c-03c              │
    │                                 │
    │ ✅ THIS IS NORMAL PATH          │
    │   → nextStepFile: c-03c-draft   │
    └─────────────────────────────────┘
              │ nextStepFile: ./c-03c-draft.md
              ↓ (SKIP c-03b1 & c-03b2)
    ┌─────────────────────────────────┐
    │ c-03c: Draft (3 variants)       │
    │ - Generate DRAFT 1: Direct      │
    │ - Generate DRAFT 2: Story       │
    │ - Generate DRAFT 3: Data-driven │
    │ - User selects one              │
    │ - ✅ 3 variants total           │
    │ - ❌ No variants 4-6 (no CM)    │
    └─────────────────────────────────┘
              │ nextStepFile
              ↓
    ┌─────────────────────────────────┐
    │ c-03d: Variants                 │
    │ - Generate 250-char version     │
    │ - Generate 100-char version     │
    │ - User reviews sizes            │
    └─────────────────────────────────┘
              │ nextStepFile
              ↓
    ┌─────────────────────────────────┐
    │ c-03e: Finalize                 │
    │ - Save post to posts_content.csv│
    │ - Set status = "draft"          │
    │ - Return post_id                │
    └─────────────────────────────────┘
              │ nextStepFile
              ↓
    ╔══════════════════════════════════════╗
    ║  RETURN: Back to c-00-menu.md        ║
    ║  User can create more posts or      ║
    ║  switch to another operation        ║
    ╚══════════════════════════════════════╝

SUMMARY:
- Total steps: 11
- Entry: c-01-add-idea
- Exit: c-03e-finalize → c-00-menu
- Key decision: c-03b-select-angle (routes normal vs demo)
- Variants generated: 3
- Demo extensions: NONE (skipped)
```

---

## FLOW MAP: DEMO CONTENT (15 Steps)

```
┌─────────────────────────────────────────────────┐
│         DEMO CONTENT FLOW (15 steps)            │
│    (content_type == "demo")                     │
│    Includes Content Machine Stage 2-4           │
└─────────────────────────────────────────────────┘

    ╔══════════════════════════════════════╗
    ║  START: User selects [3] WRITE POST  ║
    ║  from c-00-menu.md                   ║
    ║  Sets content_type = "demo"          ║
    ╚══════════════════════════════════════╝
              │
              ↓
    ┌─────────────────────────────────┐
    │ c-01: Add Idea                  │
    │ - Collect raw idea text         │
    │ - Set content_type = "demo" ✅   │
    │ - Validate criteria             │
    │ - Store in workflow_state.json  │
    └─────────────────────────────────┘
              │ nextStepFile
              ↓
    ┌─────────────────────────────────┐
    │ c-01b: Dedup Check              │
    │ - Compare against existing      │
    │ - Same logic as normal          │
    └─────────────────────────────────┘
              │ Pass: nextStepFile
              ↓
    ┌─────────────────────────────────┐
    │ c-02a: Load Ideas               │
    │ - Display existing ideas        │
    └─────────────────────────────────┘
              │ nextStepFile
              ↓
    ┌─────────────────────────────────┐
    │ c-02b: Select Idea              │
    │ - User picks which idea         │
    │ - Confirm selection             │
    └─────────────────────────────────┘
              │ nextStepFile
              ↓
    ┌─────────────────────────────────┐
    │ c-02c: Research Execute         │
    │ - Find 5-8 angles               │
    │ - Get sources & facts           │
    │ - ✅ EXECUTE Section 2.5:        │
    │   "Генерация Болей" (Demo only) │
    │   - For EACH angle: generate    │
    │     3-5 pain points             │
    │   - Store in pain_points_json   │
    │   - Save to ideas_research.csv  │
    │ - ✅ Pain points saved ready    │
    │   for later display & use       │
    └─────────────────────────────────┘
              │ nextStepFile
              ↓
    ┌─────────────────────────────────┐
    │ c-02d: Display Results          │
    │ - Show all angles               │
    │ - Show sources & facts          │
    │ - ✅ EXECUTE Section 2.5:        │
    │   "Боли Предпринимателей"       │
    │   - Display pain points for     │
    │     each angle                  │
    │   - Show which pains will be    │
    │     in variants 4-6             │
    │ - User selects angle            │
    └─────────────────────────────────┘
              │ nextStepFile
              ↓
    ┌─────────────────────────────────┐
    │ c-03a: Select Idea (again)      │
    │ - Confirm idea for writing      │
    └─────────────────────────────────┘
              │ nextStepFile
              ↓
    ┌─────────────────────────────────┐
    │ c-03b: Select Angle             │
    │ - User selects which angle      │
    │                                 │
    │ ✅ CONDITIONAL CHECK:           │
    │ IF content_type == "demo"       │
    │   → Route to c-03b1 ✅          │
    │ ELSE (normal)                   │
    │   → Route to c-03c              │
    │                                 │
    │ ✅ THIS IS DEMO PATH            │
    │   → nextStepFile: c-03b1        │
    └─────────────────────────────────┘
              │ nextStepFile: ./c-03b1-offer-check.md
              ↓ (Content Machine Stage 4)
    ┌─────────────────────────────────┐
    │ c-03b1: Offer Filter            │
    │ (Content Machine Stage 4)       │
    │ - Determine offer types         │
    │ - User selects which products   │
    │   services, training, etc.      │
    │ - Save selection to             │
    │   workflow_state.json           │
    └─────────────────────────────────┘
              │ nextStepFile
              ↓
    ┌─────────────────────────────────┐
    │ c-03b2: Offer Generation        │
    │ (Content Machine Stage 3)       │
    │ - Auto-generate 2-4 offers      │
    │ - Based on:                     │
    │   - Angle selected              │
    │   - Pain points from c-02c      │
    │   - Offer types from c-03b1     │
    │ - Save offers to                │
    │   workflow_state.json           │
    │ - ✅ Offers ready for variants  │
    └─────────────────────────────────┘
              │ nextStepFile
              ↓
    ┌─────────────────────────────────┐
    │ c-03c: Draft (6 variants)       │
    │ (Content Machine Stage 5)       │
    │ - Generate DRAFT 1: Direct      │
    │ - Generate DRAFT 2: Story       │
    │ - Generate DRAFT 3: Data-driven │
    │ - ✅ Generate DRAFT 4: PAS      │
    │   + Pains from c-02c            │
    │ - ✅ Generate DRAFT 5: Hook-... │
    │   + Pains from c-02c            │
    │   + Offers from c-03b2          │
    │ - ✅ Generate DRAFT 6: Show Work│
    │   + Pains from c-02c            │
    │   + Soft offer from c-03b2      │
    │ - ✅ 6 variants total           │
    │ - User selects one              │
    │ - CTR scores calculated for all │
    └─────────────────────────────────┘
              │ nextStepFile
              ↓
    ┌─────────────────────────────────┐
    │ c-03d: Variants                 │
    │ - Generate 250-char version     │
    │ - Generate 100-char version     │
    │ - User reviews sizes            │
    │ - All 6 variants expanded       │
    └─────────────────────────────────┘
              │ nextStepFile
              ↓
    ┌─────────────────────────────────┐
    │ c-03e: Finalize                 │
    │ - Save ALL 6 variants to        │
    │   posts_content.csv             │
    │ - Include metadata:             │
    │   - pain_points_json            │
    │   - generated_offers_json       │
    │   - visual_context              │
    │ - Set status = "draft"          │
    │ - Return post_id                │
    └─────────────────────────────────┘
              │ nextStepFile
              ↓
    ╔══════════════════════════════════════╗
    ║  RETURN: Back to c-00-menu.md        ║
    ║  User can create more posts or      ║
    ║  switch to another operation        ║
    ╚══════════════════════════════════════╝

SUMMARY:
- Total steps: 15 (11 normal + 4 demo-specific)
- Entry: c-01-add-idea (with content_type = "demo")
- Exit: c-03e-finalize → c-00-menu
- Key decision: c-03b-select-angle (routes to c-03b1 for demo)
- Variants generated: 6 (3 standard + 3 Content Machine)
- Demo extensions:
  - c-02c Section 2.5: Pain points generation
  - c-02d Section 2.5: Pain points display
  - c-03b1: Offer filter (new step)
  - c-03b2: Offer generation (new step)
  - c-03c Drafts 4-6: Content Machine frameworks
```

---

## DECISION TREE: CONDITIONAL ROUTING

```
┌──────────────────────────────────────────────────┐
│       MAIN DECISION POINT: c-03b-select-angle    │
└──────────────────────────────────────────────────┘

At step c-03b, system checks: content_type = ?

    ┌─────────────────────┬─────────────────────┐
    │                     │                     │
    ↓                     ↓                     ↓

    IF content_type       IF content_type       FALLBACK
    == "demo"             != "demo"             (ERROR)
    (TRUE)                (FALSE)               (None expected)
    │                     │
    │                     │
    ↓                     ↓

    ROUTE TO:             ROUTE TO:
    c-03b1-offer-check    c-03c-draft
    (Offer Filter)        (Direct to Draft)

    nextStepFile:         nextStepFile:
    ./c-03b1-...          ./c-03c-draft

    │                     │
    ↓                     ↓

    c-03b1                c-03c
    (2 steps ahead)       (Direct)
    ├─ c-03b1             ├─ 3 variants
    ├─ c-03b2             └─ Normal flow
    ├─ c-03c (6 variants)
    └─ Continue...

RESULT:
- Normal path: 11 steps
- Demo path: 15 steps
- Difference: +4 steps (offer filter, generation, +3 CM drafts)
```

---

## STEP-BY-STEP NAVIGATION TABLE

| Step | File Name | NextStep (Normal) | NextStep (Demo) | Input | Output |
|------|-----------|-------------------|-----------------|-------|--------|
| 1 | c-01-add-idea.md | c-01b | c-01b | User idea text | idea in inbox |
| 2 | c-01b-dedup-check.md | c-02a | c-02a | Dedup decision | dedup result |
| 3 | c-02a-load-ideas.md | c-02b | c-02b | (none) | ideas list |
| 4 | c-02b-select-idea.md | c-02c | c-02c | Idea selection | selected_idea_id |
| 5 | c-02c-research.md | c-02d | c-02d | Research query | angles + ✅ pain_points |
| 6 | c-02d-results.md | c-03a | c-03a | Angle selection | selected_angle_id |
| 7 | c-03a-select-idea.md | c-03b | c-03b | Confirmation | confirmed_idea_id |
| 8 | c-03b-select-angle.md | **c-03c** | **c-03b1** | Angle selection | ROUTES based on type |
| 8b | c-03b1-offer-check.md | n/a | c-03b2 | Offer type selection | ✅ offer_types |
| 8c | c-03b2-offer-generation.md | n/a | c-03c | Auto | ✅ generated_offers |
| 9 | c-03c-draft.md | c-03d | c-03d | Draft selection | **3 variants** / **6 variants** |
| 10 | c-03d-variants.md | c-03e | c-03e | Variant selection | 250 & 100-char versions |
| 11 | c-03e-finalize.md | c-00-menu | c-00-menu | Approval | Post saved to CSV |

---

## CONDITIONAL SECTIONS REFERENCE

### Section 2.5: Pain Points Generation & Display

**Location:** c-02c-research.md (Step 5)

**Trigger:** `content_type == "demo"`

**Action:** Automatically generate 3-5 pain points for each angle

**Output:**
- Saved to: `pain_points_json` column in ideas_research.csv
- Structure: `{"angle_1": {"pains": ["pain1", "pain2", ...]}, ...}`

**Next:** c-02d displays these (Section 2.5 also)

---

**Location:** c-02d-results.md (Step 6)

**Trigger:** `content_type == "demo"`

**Action:** Display pain points for each angle

**Purpose:** Show user what pains will be addressed in CM variants

**Next:** c-03b-select-angle (conditional routing)

---

### Content Machine Integration

**Variants Generated per Content Type:**

| Content Type | Variant Count | Which Variants |
|-------------|---------------|-----------------|
| normal | 3 | 1-3: Direct, Story, Data |
| demo | 6 | 1-3: Direct, Story, Data + 4-6: PAS, Hook-Story-Offer, Show Work |

**Demo Variants (4-6) Include:**
- Variant 4 (PAS): Problems from pain_points_json
- Variant 5 (Hook-Story): Pain points + generated_offers_json
- Variant 6 (Show Work): Pain points + soft offer

---

## FILES INVOLVED IN NORMAL PATH

```
c-01-add-idea.md
c-01b-dedup-check.md
c-02a-load-ideas.md
c-02b-select-idea.md
c-02c-research.md (Section 2.5 SKIPPED)
c-02d-results.md (Section 2.5 SKIPPED)
c-03a-select-idea.md
c-03b-select-angle.md (Routes to c-03c)
c-03c-draft.md (Generates 3 variants)
c-03d-variants.md
c-03e-finalize.md
c-00-menu.md (Return)

DATA FILES:
- ideas_inbox.csv (read/write)
- ideas_research.csv (read/write)
- angles_library.csv (write if angle selected)
- posts_content.csv (write at finalize)
```

---

## FILES INVOLVED IN DEMO PATH

```
c-01-add-idea.md (content_type = "demo")
c-01b-dedup-check.md
c-02a-load-ideas.md
c-02b-select-idea.md
c-02c-research.md (Section 2.5 EXECUTED - pain generation)
c-02d-results.md (Section 2.5 EXECUTED - pain display)
c-03a-select-idea.md
c-03b-select-angle.md (Routes to c-03b1)
✅ c-03b1-offer-check.md (NEW for demo)
✅ c-03b2-offer-generation.md (NEW for demo)
c-03c-draft.md (Generates 6 variants with CM frameworks)
c-03d-variants.md
c-03e-finalize.md
c-00-menu.md (Return)

DATA FILES:
- ideas_inbox.csv (read/write)
- ideas_research.csv (read/write + pain_points_json)
- angles_library.csv (write if angle selected)
- posts_content.csv (write with CM metadata)
- workflow_state.json (temp: offer types + generated offers)
```

---

## ERROR HANDLING PATHS

```
At any step, user can:

[M] Back to MENU
  → Return to c-00-menu.md
  → Progress saved (up to current step)
  → Can resume or switch operation

[?] HELP
  → Show detailed help for current step
  → Return to current step (no progress loss)

Timeout (2+ minutes no response):
  → Display prompt: "Are you still here?"
  → Save session state
  → Offer to resume later
```

---

## QUICK LOOKUP: NEXT STEPS

| Currently at... | Want to go to... | What to do |
|-----------------|------------------|-----------|
| c-01-add-idea | c-01b-dedup-check | Press [Enter] or automatic |
| c-01b-dedup-check | c-02a-load-ideas | Select [Y] for "Add to Inbox" |
| c-02d-results | c-03a-select-idea | Select angle [1-8] or [W] |
| c-03b-select-angle | c-03c-draft (normal) | Press [Enter] (automatic route) |
| c-03b-select-angle | c-03b1-offer-check (demo) | Press [Enter] (automatic route) |
| c-03e-finalize | c-00-menu | Press [Y] to save and return |
| Any step | c-00-menu | Select [M] for "Back to MENU" |

---

**Generated:** 2026-01-30
**Purpose:** Quick reference for workflow navigation
**Audience:** Developers, agents, QA testers
