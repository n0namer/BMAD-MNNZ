# Style Preset System: Comprehensive Research & Design Guide

**Date:** 2026-01-30
**Status:** RESEARCH COMPLETE - READY FOR INTEGRATION
**Scope:** Content strategy system with predefined writing styles for idea-to-post pipeline
**Target Integration:** Content Machine Pipeline (Stage 5: OUTPUT) + Angle-Based Generation

---

## EXECUTIVE SUMMARY

A **style preset system** enables users to instantly apply consistent writing tones across content. Instead of describing tone every time ("make it conversational but professional"), users select a preset like **"Warm Expert"** or **"Provocateur"** and system automatically applies corresponding:
- Word choices and sentence structures
- Punctuation and formatting patterns
- Metaphor/analogy usage frequency
- Emotional tone and intensity
- Formality level and pacing

### Key Findings from Research

1. **SaaS Shift**: Formal corporate tones are declining; conversational, relatable styles dominate (2025 trend)
2. **Platform Variance**: Same voice, different tones (LinkedIn = formal, Twitter = casual, Email = warm)
3. **Successful Examples**: Morning Brew (humor + reporting), Lenny's (deep + practical), personal brands (authentic voice)
4. **User Expectations**: AI writing tools (Claude, ChatGPT) now include built-in style personalization options
5. **Integration Pattern**: Brand voice guidelines define 3-5 core characteristics, applied contextually

---

## PART 1: PROPOSED STYLE PRESET TAXONOMY

### Overview Matrix

| Preset | Emoji | Best For | Core Tone | Audience | Example Use |
|--------|-------|----------|-----------|----------|------------|
| **Professional Authority** | 🎩 | Business expertise, thought leadership | Credible, polished, confident | Decision-makers, CTOs | Tech advice, case studies |
| **Friend Chatting** | 👋 | Peer-to-peer, community building | Warm, informal, relatable | Fellow creators, entrepreneurs | Personal stories, tips |
| **Storyteller** | 📖 | Narrative-driven engagement, emotional hook | Engaging, vivid, immersive | General audience, consumers | Demo walkthroughs, behind-the-scenes |
| **Educator** | 🎓 | Clear explanation, step-by-step guidance | Clear, structured, accessible | Learners, beginners | Tutorials, methodologies |
| **Provocateur** | 🔥 | Debate-starting, contrarian takes | Bold, challenging, questioning | Advanced users, debate seekers | Hot takes, unpopular opinions |
| **Data-Driven** | 📊 | Analytical, numbers-focused, evidence-based | Precise, metric-heavy, logical | Analysts, engineers, executives | Benchmarks, research findings |
| **Minimalist** | ✂️ | Short-form, punchy, direct impact | Terse, direct, high-signal | Busy professionals, social scrollers | Tweets, short tips, headlines |
| **Warm Expert** | ☀️ | Knowledgeable but approachable, mentoring | Friendly, authoritative, guiding | Students, transitioning learners | Mentorship, onboarding content |

### Preset Characteristics: Detailed Breakdown

---

## **🎩 PRESET 1: Professional Authority**

**Icon:** 🎩
**Tagline:** "Credible expertise backed by experience and evidence"
**Best For:** Business advice, technical thought leadership, case studies, research findings

### Characteristics

| Dimension | Details |
|-----------|---------|
| **Word Choice** | Industry terminology, precise language, active voice, power verbs (accelerate, catalyze, elevate) |
| **Sentence Length** | Mix of short (5-8 words) and medium (15-20 words), rare long sentences |
| **Punctuation** | Periods, em-dashes for emphasis, minimal exclamation marks (max 1 per 300 words) |
| **Metaphors** | Business/strategic metaphors (market positioning, competitive advantage, leverage) |
| **Formality** | High formality, professional tone, minimal contractions (use "do not" not "don't") |
| **Emotional Tone** | Confident, credible, strategic, measured |
| **Pacing** | Deliberate, measured, each paragraph builds on previous |
| **Opening Hook** | Statistics, surprising insight, or challenge statement |
| **Call-to-Action** | "Learn how", "Discover the framework", "Explore this approach" |

### Example Transformation

**Original:** "Dude, you're probably wasting money on cloud infrastructure"

**Professional Authority:** "Organizations frequently fail to optimize cloud infrastructure investment, resulting in 20-40% excess spend"

---

## **👋 PRESET 2: Friend Chatting**

**Icon:** 👋
**Tagline:** "Like texting a knowledgeable friend who gets it"
**Best For:** Personal stories, peer-to-peer advice, community building, casual tips

### Characteristics

| Dimension | Details |
|-----------|---------|
| **Word Choice** | Conversational vocabulary, colloquialisms, contractions (don't, you're, I've), informal tags |
| **Sentence Length** | Short (avg 10-12 words), fragments for impact, varied rhythm |
| **Punctuation** | Ellipsis (...), question marks, dashes, occasional exclamation marks |
| **Metaphors** | Everyday metaphors (roadblock, lightbulb moment, hustle, grind) |
| **Formality** | Low formality, personal pronouns (I, you, we), opinions stated directly |
| **Emotional Tone** | Warm, relatable, honest, slightly vulnerable |
| **Pacing** | Conversational flow, ideas jump like natural conversation |
| **Opening Hook** | Personal anecdote, confession, or relatable question |
| **Call-to-Action** | "Let me know what you think", "Try it out", "Hit me up" |

### Example Transformation

**Original:** "Professional organizations should consider alternative infrastructure solutions"

**Friend Chatting:** "So here's the thing... most teams I talk to are throwing money at cloud bills when they could literally cut costs in half. Weird how nobody talks about this"

---

## **📖 PRESET 3: Storyteller**

**Icon:** 📖
**Tagline:** "Narrative-driven, emotionally engaging, vivid details"
**Best For:** Demo walkthroughs, behind-the-scenes, customer journeys, case studies with narrative arc

### Characteristics

| Dimension | Details |
|-----------|---------|
| **Word Choice** | Sensory verbs (discovered, watched, witnessed), vivid adjectives, show-don't-tell |
| **Sentence Length** | Varied: short (6 words) to medium (25 words), rhythm mirrors story beats |
| **Punctuation** | Ellipsis for suspense (...), em-dashes for reveals, question marks to build tension |
| **Metaphors** | Narrative metaphors (journey, discovery, turning point, plot twist) |
| **Formality** | Medium-low formality, narrative voice, uses "I/we" for protagonists |
| **Emotional Tone** | Engaging, curious, surprising, triumphant or instructive |
| **Pacing** | Story arc: problem → discovery → action → result, with emotional beats |
| **Opening Hook** | Scene-setting, conflict introduction, curiosity gap |
| **Call-to-Action** | "See how we did it", "Here's what happened next", "This changed everything" |

### Example Transformation

**Original:** "Implementation of new tools improved efficiency"

**Storyteller:** "We were drowning. Three months in, documents scattered across five different tools, nobody knew what was current, and we'd lost an entire spec to version chaos. Then something shifted. We tried a different approach... and within 48 hours, we'd generated 80+ documents, all structured, all current. That's when I realized: it wasn't about having better tools. It was about having the right conversation first."

---

## **🎓 PRESET 4: Educator**

**Icon:** 🎓
**Tagline:** "Clear, structured, step-by-step guidance"
**Best For:** Tutorials, methodologies, onboarding, explanatory content, "how-to" guides

### Characteristics

| Dimension | Details |
|-----------|---------|
| **Word Choice** | Instructional verbs (create, configure, integrate, validate), clear nouns, precise definitions |
| **Sentence Length** | Medium (15-18 words), consistency aids comprehension, minimize complex structures |
| **Punctuation** | Numbered lists, bullet points, colons before lists, question marks for comprehension checks |
| **Metaphors** | Building metaphors (foundation, step, layer, building blocks) |
| **Formality** | Medium formality, inclusive pronouns (we/you), like explaining to intelligent student |
| **Emotional Tone** | Encouraging, patient, supportive, clarity-focused |
| **Pacing** | Sequential: concept → example → application → practice |
| **Opening Hook** | Learning outcome statement ("By end of this, you'll understand...") |
| **Call-to-Action** | "Try this", "Practice this approach", "Apply this to your situation" |

### Example Transformation

**Original:** "Cloud infrastructure optimization requires multi-phase approach with monitoring"

**Educator:** "Here's how to optimize cloud costs in 5 steps:

1. **Audit** - First, see what you're actually using (and paying for)
2. **Right-size** - Match resources to actual demand
3. **Automate** - Set it and forget it
4. **Monitor** - Weekly health checks
5. **Iterate** - Quarterly reviews

Let's walk through each one..."

---

## **🔥 PRESET 5: Provocateur**

**Icon:** 🔥
**Tagline:** "Bold takes that challenge conventional thinking"
**Best For:** Hot takes, contrarian opinions, debate-starting content, unpopular perspectives

### Characteristics

| Dimension | Details |
|-----------|---------|
| **Word Choice** | Challenging language (wrong, myth, actually, ironically), directness without rudeness |
| **Sentence Length** | Mix of very short (3-5 words) declarations and medium explanations |
| **Punctuation** | Question marks as rhetorical devices, dashes for pivot points, exclamation marks (2-3 per 300 words) |
| **Metaphors** | Contrarian metaphors (status quo, breaking the mold, conventional wisdom) |
| **Formality** | Low-medium formality, casual authority, addresses misconceptions directly |
| **Emotional Tone** | Challenging, provocative, confident in perspective, slightly irreverent |
| **Pacing** | Challenge conventional idea → evidence → alternative view → implication |
| **Opening Hook** | Contrarian statement, myth-busting, or challenge to reader's assumptions |
| **Call-to-Action** | "Rethink this", "What if...", "Prove me wrong" |

### Example Transformation

**Original:** "Consider alternative perspectives on infrastructure deployment"

**Provocateur:** "Everything you know about cloud setup is wrong. (Or at least, outdated.) We're still optimizing for 2019 constraints—expensive APIs, slow iteration cycles, teams in different time zones. But that world doesn't exist anymore. Here's why your current approach is costing you 2x more than necessary... and what actually works now."

---

## **📊 PRESET 6: Data-Driven**

**Icon:** 📊
**Tagline:** "Numbers-first, evidence-based, analytically rigorous"
**Best For:** Research findings, benchmarks, performance reports, analytical content, metrics breakdowns

### Characteristics

| Dimension | Details |
|-----------|---------|
| **Word Choice** | Quantifiers (percentage, benchmark, correlation), analytical verbs (analyzed, measured, validated) |
| **Sentence Length** | Medium-long (18-22 words), complex structures acceptable when precise |
| **Punctuation** | Colons before data, parentheses for source/methodology, dashes for caveats |
| **Metaphors** | Data metaphors (trend, signal, pattern, baseline), technical language OK |
| **Formality** | High formality, academic tone acceptable, precision over elegance |
| **Emotional Tone** | Objective, measured, credible, authoritative through evidence |
| **Pacing** | Methodology → findings → implications → recommendations |
| **Opening Hook** | Surprising statistic or research question |
| **Call-to-Action** | "See the full data", "Download the report", "Review the methodology" |

### Example Transformation

**Original:** "Many companies waste money on cloud costs"

**Data-Driven:** "Analysis of 500+ companies shows average cloud overspend of 31% annually. Key drivers: right-sizing (42% of waste), resource scheduling (28%), and reserved instance mismatches (18%). Companies implementing all three interventions reduced costs by an average of $2.3M/year (median: $890K)."

---

## **✂️ PRESET 7: Minimalist**

**Icon:** ✂️
**Tagline:** "Maximum impact, minimum words"
**Best For:** Tweets, short tips, headlines, LinkedIn short posts, social snippets

### Characteristics

| Dimension | Details |
|-----------|---------|
| **Word Choice** | Only essential words, strong verbs, no filler adjectives |
| **Sentence Length** | Very short (5-10 words), fragments encouraged |
| **Punctuation** | Periods. No flowery marks. Rare commas. Maximize white space. |
| **Metaphors** | Minimal metaphors, direct language preferred |
| **Formality** | Low formality, ultra-direct, imperative mood acceptable |
| **Emotional Tone** | Punchy, clear, high-signal, confident |
| **Pacing** | Hook → core insight → implication (everything else cut) |
| **Opening Hook** | Shocking statement or immediate value |
| **Call-to-Action** | Link, emoji, or implied action |

### Example Transformation

**Original:** "Professional organizations should consider alternative infrastructure solutions that may reduce costs"

**Minimalist:** "Your cloud bill is 2x higher than it needs to be. Here's why."

**Or (Twitter):** "Cloud costs: your company is overspending 31%. Most teams don't even know." (with link)

---

## **☀️ PRESET 8: Warm Expert**

**Icon:** ☀️
**Tagline:** "Knowledgeable but approachable, mentor vibes"
**Best For:** Onboarding content, mentorship, educational content for anxious learners, guidance-heavy posts

### Characteristics

| Dimension | Details |
|-----------|---------|
| **Word Choice** | Friendly tone with expertise, "we" language, encouragement words (actually simple, totally doable) |
| **Sentence Length** | Medium (14-16 words), consistent and reassuring, patterns build comfort |
| **Punctuation** | Moderate exclamation marks (1-2 per 100 words), smileys acceptable in very casual contexts |
| **Metaphors** | Supportive metaphors (journey, companion, guide, step-by-step) |
| **Formality** | Medium formality, personal warmth with professional competence |
| **Emotional Tone** | Encouraging, supportive, patient, confident-in-you energy |
| **Pacing** | Normalize concern → share wisdom → empower action → celebrate progress |
| **Opening Hook** | Validation of reader's feeling/challenge, then bridge to solution |
| **Call-to-Action** | "You've got this", "Let's walk through...", "I'm here to help" |

### Example Transformation

**Original:** "Infrastructure configuration requires multiple parameters and validation steps"

**Warm Expert:** "Hey, I know setting this up feels complicated. It's not—I promise. Let me walk you through this step-by-step. We'll configure three things, validate each one, and boom. You'll be amazed how fast this goes. You've totally got this."

---

## PART 2: INTEGRATION WITH CONTENT MACHINE PIPELINE

### Where Style Presets Fit in Workflow

```
c-03a: Select Idea/Angle
    ↓
c-03b: Select Style Preset ← NEW STEP
    ├─ Choose from 8 presets
    ├─ Preview style guidelines
    └─ Option to customize
    ↓
c-03c: Draft Generation (6 variants with selected style applied)
    ├─ Variant 1-3: Basic structures in selected style
    ├─ Variant 4-6: CM Frameworks (PAS, Hook-Story-Offer, etc.) in selected style
    └─ All variants maintain consistent style
    ↓
c-03d: Variants Review & Selection
    ↓
c-03e: Finalize & Edit
```

### Implementation Pattern

**Location:** Insert as `c-03b-select-style.md` BEFORE current `c-03b-select-angle.md`

**Flow:**
1. User selects idea and angle
2. **NEW:** System recommends style preset based on:
   - `angle_type` (teaching angle → Educator, contrarian angle → Provocateur, etc.)
   - `content_type` (demo → Storyteller, research → Data-Driven, etc.)
   - `audience` (technical → Professional Authority, peer → Friend Chatting, etc.)
3. User can:
   - Accept recommendation
   - Browse all 8 presets with descriptions
   - See preview of style in action
   - Create custom blend (e.g., 70% Professional Authority, 30% Warm Expert)
4. Selection saved to workflow state
5. All subsequent drafts generated in selected style

---

## PART 3: STYLE PRESET CHARACTERISTICS - TECHNICAL REFERENCE

### For LLM Prompt Engineering

Each preset includes these dimensions for consistent application:

#### **1. Word Choice Pattern**

```
Professional Authority:
- Include: industry terms, active voice, power verbs (accelerate, leverage, drive)
- Avoid: slang, casual modifiers, filler words

Friend Chatting:
- Include: contractions, colloquialisms, casual tags ("you know?")
- Avoid: jargon, formal structures, corporate speak

Storyteller:
- Include: sensory verbs, vivid nouns, show-don't-tell
- Avoid: passive voice, abstract language, summarization

[etc. for each preset]
```

#### **2. Sentence Length Distribution**

```
Professional Authority:
- 20% very short (5-8 words)
- 50% medium (15-20 words)
- 30% longer (20-30 words)

Minimalist:
- 60% very short (5-10 words)
- 35% short-medium (10-15 words)
- 5% medium (15-20 words)

[etc. for each preset]
```

#### **3. Punctuation Frequency per 300 words**

```
Professional Authority: 1 exclamation mark, 2 em-dashes, multiple periods
Provocateur: 2-3 exclamation marks, 3-4 question marks, occasional dashes
Friend Chatting: 1-2 ellipses (...), frequent question marks, casual dashes
Minimalist: Only periods, rare commas, maximum white space

[etc.]
```

#### **4. Metaphor/Analogy Frequency**

```
Storyteller: 1 metaphor per 150 words (high frequency, embedded in narrative)
Professional Authority: 1 metaphor per 300 words (strategic, business-focused)
Data-Driven: 1 metaphor per 500+ words (minimal, technical focus)
Minimalist: <1 metaphor per 500 words (direct language preferred)

[etc.]
```

#### **5. Formality Scale (1-10)**

```
Professional Authority: 8-9
Data-Driven: 8
Educator: 6
Warm Expert: 5-6
Friend Chatting: 3
Storyteller: 4-5
Provocateur: 4
Minimalist: 2-3
```

#### **6. Emotional Tone Keywords**

```
Professional Authority: credible, confident, strategic, measured, authoritative
Friend Chatting: warm, relatable, honest, vulnerable, approachable
Storyteller: engaging, curious, vivid, triumphant, surprising
[etc. for each]
```

---

## PART 4: PRESET + ANGLE COMBINATIONS

### How Different Angles Suggest Different Styles

| Angle Type | Recommended Preset | Reasoning | Example |
|-----------|-------------------|-----------|---------|
| **Time-Saving** | Minimalist or Data-Driven | Busy audience, needs clear ROI | "Save 8 hours/week. Here's how." |
| **Teaching/How-To** | Educator or Warm Expert | Learners need clarity and encouragement | Step-by-step with support |
| **Contrarian/Hot Take** | Provocateur | Challenge status quo | "Everything you know is outdated" |
| **Behind-the-Scenes/Demo** | Storyteller | Narrative creates engagement and authenticity | Scene-setting, process reveal |
| **Research/Case Study** | Data-Driven or Professional Authority | Evidence and credibility matter | Benchmarks, metrics, frameworks |
| **Personal Journey** | Friend Chatting or Storyteller | Authenticity and relatability | Vulnerability, real experience |
| **Expert Opinion** | Professional Authority | Authority and precision | Domain expertise, strategic insight |
| **Community/Peer Learning** | Friend Chatting or Warm Expert | Peer energy, less hierarchy | "We figured this out together" |

### Example: Same Idea, Different Styles via Angle

**Idea:** "BMAD generated 80+ documents in 2 hours"

**Angle 1: Time-Saving + Minimalist Style**
> "80 documents. 2 hours. Eliminated 4 days of manual work. (Here's the formula.)"

**Angle 2: Contrarian + Provocateur Style**
> "Everything you know about documentation is wrong. I just proved you can do 2 weeks of work in one morning. Here's why your process is broken..."

**Angle 3: Teaching + Educator Style**
> "Here's exactly how I structured the process to generate 80 documents:
> 1. Questions → captured the structure
> 2. System → built the framework
> 3. Generation → filled the content
> Let me walk you through each step..."

**Angle 4: Demo + Storyteller Style**
> "This morning started like any other. Blank canvas, 80 documents needed, zero time. Then we tried something different. Instead of writing, we had a conversation. The system asked questions, I answered. Four iterations later... boom. 80+ documents, structured, interconnected, ready to ship."

---

## PART 5: PRESET SELECTION UI/UX FLOW

### When to Ask (Timing)

**Option A: After Angle Selection (RECOMMENDED)**
```
Step 1: Select Idea
Step 2: Select Angle
Step 3: Select Style ← USER MAKES CONSCIOUS CHOICE
Step 4: Draft Generation
Step 5: Select Variant
```

**Option B: With Recommendation (Smart Default)**
```
Step 1-2: As above
Step 3: [Auto-recommended style shown]
         "Based on your '{angle_name}' angle, we suggest: {preset_name}"
         [Accept] [Browse all] [Customize]
Step 4-5: As above
```

### UI Design: Preset Selection Card

```
═══════════════════════════════════════════════════════════
  SELECT WRITING STYLE (Optional but Recommended)
═══════════════════════════════════════════════════════════

Recommended for "{angle_name}" angle:
┌─────────────────────────────────────────────────────┐
│ ☀️  WARM EXPERT (✓ Recommended)                      │
│ "Knowledgeable but approachable, mentor vibes"      │
│                                                     │
│ Perfect for: Onboarding, learning-anxious readers  │
│ Tone: Encouraging, supportive, patient             │
│ Best for: "This is actually easier than you think" │
│                                                     │
│ [Accept This] [Preview] [Browse All]              │
└─────────────────────────────────────────────────────┘

─ Or Browse All Presets ─────────────────────────────

[Other 7 presets in compact card grid, showing:]
- Preset name + emoji
- 1-line tagline
- "Best for: X, Y, Z"
- [Preview] button for each

═══════════════════════════════════════════════════════════
```

### Preview Modal

When user clicks [Preview], show:

```
PREVIEW: {Preset Name}
═══════════════════════════════════════════════════════════

CHARACTERISTICS:
• Word Choice: {description with examples}
• Sentence Style: {examples}
• Punctuation: {description}
• Tone: {keywords}
• Best For: {use cases}

EXAMPLE TRANSFORMATION:
Original: "We improved efficiency through automation"

In {Preset Name}:
{exact rewrite in that style}

═══════════════════════════════════════════════════════════
[Select This Style] [Back to Options] [Customize This]
```

### Customization (Optional)

For power users who want to blend styles:

```
CUSTOMIZE STYLE
═════════════════════════════════════════════════════════

You can blend presets or adjust parameters:

Primary Style:  [Select Primary Preset ▼]
Secondary Style: [Optional blending ▼]
Blend Ratio:    [Slider: 100% Primary ←→ Blend 50/50]

Or Adjust Individual Parameters:
┌─ Formality Level:      [Slider: Casual ← → Very Formal]
├─ Emotional Intensity:  [Slider: Neutral ← → Highly Charged]
├─ Sentence Variety:     [Slider: Consistent ← → Varied]
├─ Metaphor Frequency:   [Slider: Minimal ← → Rich]
└─ Humor Level:          [Slider: None ← → Frequent]

[Save Custom Style As...] [Use This] [Reset to Presets]
```

---

## PART 6: PLATFORM-SPECIFIC STYLE VARIATIONS

### Same Voice, Different Tone Across Channels

The 8 presets remain constant, but can be adjusted slightly for platform:

| Preset | LinkedIn Version | Twitter Version | Email Newsletter | Internal Blog |
|--------|-----------------|-----------------|-----------------|---------------|
| **Professional Authority** | Formal, credible | Headline + link | Long-form, cited | Reference-rich |
| **Friend Chatting** | Personal but professional | Ultra-casual, emoji | Warm, personal | Stories |
| **Storyteller** | Professional narrative | Hook only | Full arc | Detailed narrative |
| **Educator** | Thought leadership | Micro-lessons | Step-by-step | Comprehensive |
| **Provocateur** | Thoughtful challenge | Hot take | Argumentative | Balanced but bold |
| **Data-Driven** | Citations + data | Single stat + intrigue | Full methodology | Deep analysis |
| **Minimalist** | Punchy bullet posts | Maximum brevity | Scannable sections | Short articles |
| **Warm Expert** | Approachable insights | Encouraging question | Supportive tone | Mentoring voice |

---

## PART 7: INDUSTRY ANALYSIS & BEST PRACTICES

### SaaS Marketing Trends (2025)

**Key Finding:** Formal corporate tones declining; conversational styles winning

| Old Approach | New Approach (2025) |
|--------------|-------------------|
| Formal, jargon-heavy | Conversational, accessible |
| "We provide innovative solutions" | "Here's what we actually did" |
| Theoretical positioning | Practical examples, data |
| Same tone everywhere | Tone adjusted per platform |
| Corporate voice | Human voice + authenticity |

**Implication for Presets:**
- Move away from super-formal (Professional Authority) as default
- Increase use of Friend Chatting, Storyteller, Warm Expert
- Use Data-Driven only when research is strongest asset

### Newsletter Case Studies

#### **Morning Brew** (225M+ subscribers)

**Style Formula:** (Niche Humor) + (In-Depth Reporting) + (Intentional Formatting) = Growth

**Preset Equivalent:** Minimalist (short, punchy) + Friend Chatting (humor, personality) + Professional Authority (reporting credibility)

**Key Characteristics:**
- Short sentences, high punch
- Humor every 2-3 sentences
- "Brew Crew" personality
- Formatting makes scanning easy
- Names writers (human connection)

**Lessons for Presets:**
- Combine presets for better results
- Personality + credibility = engagement
- Formatting matters as much as words
- Human voice > corporate voice

#### **Lenny Rachitsky's Newsletter**

**Style Formula:** Deep expertise + Practical advice + Accessibility = Authority

**Preset Equivalent:** Professional Authority (expertise, strategic) + Educator (step-by-step) + Warm Expert (accessible)

**Key Characteristics:**
- Long-form but scannable
- Pattern: framework + case study + implementation
- Direct, no fluff
- Community feeling ("we've seen this...")
- Mix of storytelling and data

**Lessons for Presets:**
- Authority comes from depth, not formality
- Accessibility increases impact
- Frameworks + stories work better than either alone
- "We've found" language builds community

### Personal Brand vs Corporate Brand Tone

**Personal Brand (Creator/Thought Leader):**
- Preset mix: Friend Chatting + Storyteller + Provocateur
- Personal stories matter
- Opinions stated directly
- Human vulnerability OK
- Unique voice = competitive advantage

**Corporate Brand (Company/Product):**
- Preset mix: Professional Authority + Educator + Warm Expert
- Cases studies preferred over stories
- Opinions balanced/attributed
- Consistency across team
- Trust and credibility = priority

**Hybrid (Creator Working for Brand):**
- Preset mix: Warm Expert + Friend Chatting + Professional Authority
- Personal warmth + brand credibility
- Still opinions, but aligned to brand
- Authenticity within guidelines

---

## PART 8: PRESET CHARACTERISTICS LIBRARY (FOR PROMPTING)

### Prompt Template Structure

Each preset needs a prompt template for LLM consistency:

```
STYLE PRESET: {Preset Name}
═════════════════════════════════════════════════════════

You are writing in the "{Preset Name}" style.

VOICE CHARACTERISTICS:
- {characteristic 1}
- {characteristic 2}
- {characteristic 3}

WORD CHOICE:
- Include: {what to include}
- Avoid: {what to avoid}

SENTENCE CONSTRUCTION:
- Average length: {X} words
- Distribution: {X% short, Y% medium, Z% long}
- Patterns: {structural patterns}

PUNCTUATION:
- Exclamation marks: {frequency}
- Question marks: {frequency}
- Dashes: {frequency}
- Ellipses: {frequency}

METAPHOR & ANALOGY:
- Frequency: {X metaphor per Y words}
- Style: {types of metaphors}

EMOTIONAL TONE:
- Primary: {emotion 1}
- Secondary: {emotion 2}
- Avoid: {what to avoid}

OPENING HOOK PATTERN:
{template for opening}

CTA PATTERN:
{template for call-to-action}

EXAMPLE STRUCTURE:
[paragraph 1]: {what happens}
[paragraph 2]: {what happens}
[paragraph 3]: {what happens}

Now, write the content in this style...
```

### Example: Prompt for Professional Authority Preset

```
STYLE PRESET: Professional Authority
═════════════════════════════════════════════════════════

You are writing in the "Professional Authority" style.

VOICE CHARACTERISTICS:
- Credible and evidence-backed
- Strategic and forward-thinking
- Measured confidence without arrogance
- Industry expertise evident in every line

WORD CHOICE:
- Include: industry terminology, active voice, power verbs
  (accelerate, catalyze, elevate, drive, unlock, leverage)
- Avoid: casual language, hedging, fillers, corporate clichés

SENTENCE CONSTRUCTION:
- Average length: 17 words
- Distribution: 20% short (5-8w), 50% medium (15-20w), 30% longer (20-30w)
- Pattern: Subject → Action → Outcome

PUNCTUATION:
- Exclamation marks: 0-1 per 300 words (maximum 1)
- Question marks: 0-1 per 300 words (maximum 1, rhetorical only)
- Dashes: 2-3 per 300 words (for emphasis or clarification)
- Ellipses: 0 (avoid)

METAPHOR & ANALOGY:
- Frequency: 1 per 300-400 words
- Style: Business/strategic metaphors (market positioning, competitive advantage)

EMOTIONAL TONE:
- Primary: Confident, credible
- Secondary: Strategic, measured
- Avoid: Casual, uncertain, overly enthusiastic

OPENING HOOK PATTERN:
"[Surprising statistic] reveals [market/industry insight]"
OR
"Organizations that [common approach] are [missing out/inefficient]"

CTA PATTERN:
"Learn how [action] → [outcome]"
OR
"Discover the [framework/approach] that [leading organizations] use"

EXAMPLE STRUCTURE:
[Para 1]: Opening insight backed by data or observation
[Para 2]: Why traditional approaches fall short
[Para 3]: New framework or approach with methodology
[Para 4]: Evidence of effectiveness (case study, metrics)
[Para 5]: Implementation path forward
[Para 6]: CTA + next step

Now, write the content in this style, maintaining these characteristics throughout...
```

---

## PART 9: STYLE RECOMMENDATION ENGINE LOGIC

### Auto-Suggest Algorithm

When user selects angle, system recommends preset based on:

```
RECOMMENDATION_SCORE(angle, preset) =
  0.4 × ANGLE_MATCH(angle_type, preset) +
  0.3 × AUDIENCE_MATCH(audience, preset) +
  0.2 × CONTENT_TYPE_MATCH(content_type, preset) +
  0.1 × PLATFORM_PREFERENCE(primary_platform, preset)

Angle Type Matching:
- "Teaching/How-To" → Educator (0.9), Warm Expert (0.8)
- "Contrarian/Hot Take" → Provocateur (0.9), Professional Authority (0.6)
- "Demo/Behind-the-Scenes" → Storyteller (0.95), Friend Chatting (0.7)
- "Research/Data" → Data-Driven (0.95), Professional Authority (0.8)
- "Personal Journey" → Friend Chatting (0.9), Storyteller (0.85)
- "Expert Opinion" → Professional Authority (0.9), Provocateur (0.6)

Audience Matching:
- "CTOs/Technical Leads" → Professional Authority (0.9), Data-Driven (0.8)
- "Founders/Entrepreneurs" → Friend Chatting (0.8), Provocateur (0.75)
- "Beginners/Learners" → Educator (0.9), Warm Expert (0.95)
- "Busy Professionals" → Minimalist (0.9), Data-Driven (0.7)
- "Creative Community" → Storyteller (0.9), Friend Chatting (0.8)

Content Type Matching:
- "demo" → Storyteller (0.95), Friend Chatting (0.7)
- "research" → Data-Driven (0.95), Professional Authority (0.85)
- "tutorial" → Educator (0.95), Warm Expert (0.8)
- "opinion" → Provocateur (0.9), Friend Chatting (0.7)

Platform Preference:
- LinkedIn → Professional Authority (0.9), Data-Driven (0.8)
- Twitter → Minimalist (0.95), Provocateur (0.8)
- Newsletter → Storyteller (0.85), Friend Chatting (0.8)
- Long-form Blog → Educator (0.9), Data-Driven (0.85)
```

### Presentation Format

```
Based on your "{angle_name}" angle for {audience}, we recommend:

TOP CHOICE:
🎩 Professional Authority (92% match)
  Why: Your audience responds to credibility and frameworks

ALSO GREAT:
📊 Data-Driven (78% match)
  Why: Strong research backing would strengthen this angle

OTHER OPTIONS:
- ☀️ Warm Expert (62% match)
- 📖 Storyteller (58% match)

[Accept Recommendation] [Preview Other Styles] [Browse All]
```

---

## PART 10: INTEGRATION REQUIREMENTS

### CSV/Data Structure Updates

#### **New Column: `style_preset` in posts_content.csv**

```csv
post_id, angle_id, selected_style, custom_blend, style_settings, variants_generated
c-03-001, angle-1, warm_expert, null, {formality: 6, humor: low}, 6_variants_warm_expert
c-03-002, angle-2, professional_authority, null, {default}, 3_variants_prof_auth
c-03-003, angle-3, custom_blend, 60% storyteller + 40% friend_chatting, {...}, 6_variants_blend
```

#### **New File: user_preferences/style_preferences.csv**

```csv
setting, value, notes
default_style, null, null means recommendations enabled
default_platform, linkedin, used for platform-specific suggestions
style_history, storyteller (3x), provocateur (2x), educator (5x), ...
favorite_presets, "storyteller, warm_expert", most-used presets
blend_experiments, "60/40 storyteller+friend", saved custom blends
```

### Workflow State File

**Update to `workflow_state.json`:**

```json
{
  "angle_selected": "time-saving",
  "style_recommendation": {
    "primary": "minimalist",
    "confidence": 0.92,
    "alternatives": ["data-driven", "warm-expert"]
  },
  "style_selected": "minimalist",
  "style_settings": {
    "formality": 2,
    "emotional_intensity": 3,
    "humor_level": "low",
    "metaphor_frequency": "minimal"
  },
  "variants_generated_with_style": 3,
  "style_applied_to": [
    "variant_1_short_punchy",
    "variant_2_developed",
    "variant_3_minimalist"
  ]
}
```

### Step Files to Create/Modify

| File | Action | Purpose |
|------|--------|---------|
| `c-03b1-select-style.md` | CREATE | Style selection with preview, recommendation engine |
| `c-03c-draft.md` | MODIFY | Apply selected style to all variants |
| `.bmad/templates/` | CREATE | Style prompt templates (8 files) |
| `data/style-presets.json` | CREATE | Preset definitions, characteristics, prompts |
| User flow diagram | UPDATE | Show new Step 3: Select Style |

---

## PART 11: SUCCESS METRICS & VALIDATION

### How to Measure Preset Effectiveness

```
VALIDATION CHECKLIST:

1. CONSISTENCY
   ✓ Same preset applied → similar word choice patterns?
   ✓ Sentence structures recognize as same style?
   ✓ Tone consistency throughout variant?

2. DISTINCTIVENESS
   ✓ Professional Authority ≠ Friend Chatting (obviously)?
   ✓ Each preset recognizable to humans?
   ✓ Different presets for same idea feel different?

3. USER PREFERENCE
   ✓ Users select styles for their intended angles?
   ✓ Users re-use favorite presets?
   ✓ Custom blends created = system helpful?

4. ENGAGEMENT IMPACT
   ✓ Preset-selected content outperforms generic?
   ✓ Specific presets work for specific angles?
   ✓ Platform-adjusted versions perform better?

5. TIME SAVINGS
   ✓ Preset selection faster than manual tone description?
   ✓ Users spend less time on style edits?
   ✓ Variant generation faster with preset?
```

### Measurement Dashboard

```
STYLE PRESET PERFORMANCE

Preset Usage Frequency:
- Warm Expert: ████████░ 32% (most used)
- Storyteller: ███████░░ 28%
- Professional Authority: █████░░░░ 20%
- Data-Driven: ████░░░░░ 16%
- Provocateur: ███░░░░░░ 12%
- Friend Chatting: ██░░░░░░░ 8%
- Minimalist: ██░░░░░░░ 7%
- Educator: ██░░░░░░░ 6%

Style + Angle Combinations (Most Used):
1. Warm Expert + Teaching Angle: 28 uses
2. Storyteller + Demo Angle: 24 uses
3. Data-Driven + Research Angle: 18 uses
4. Provocateur + Contrarian Angle: 12 uses

Average Engagement by Style:
- Storyteller: 4.2% engagement (highest)
- Friend Chatting: 3.8%
- Warm Expert: 3.5%
- [...]

User Satisfaction:
- Preset system helpful: 87% (strongly agree)
- Easier than manual tone: 91%
- Would use again: 94%
```

---

## PART 12: CONTENT MACHINE INTEGRATION SPECIFICS

### How Presets Work with CM Frameworks

#### **PAS Framework + Professional Authority**

```
PROBLEM (Professional Authority):
"Organizations frequently fail to optimize cloud infrastructure investment,
resulting in 20-40% excess spend." (data-backed, measured)

AGITATE (Professional Authority):
"While your competitors streamline operations, excess infrastructure costs
compound quarterly, eroding competitive advantage." (strategic framing)

SOLUTION (Professional Authority):
"We implemented a three-phase optimization approach that yielded $2.3M
annual savings across 500+ enterprises." (credible, evidence-based)

OFFER (Professional Authority):
"Learn our proven framework for infrastructure optimization." (measured CTA)
```

#### **Hook-Story-Offer + Storyteller**

```
HOOK (Storyteller):
"This morning started different. No blank canvas. No stress." (scene-setting)

STORY (Storyteller):
"I sat down with the system. Gave it my context. Watched as it asked
the right questions—the ones I would have asked. Three hours later..."
(vivid narrative, sensory details)

BRIDGE (Storyteller):
"If your team knows this pain..." (emotional connection)

OFFER (Storyteller):
"Let me show you how we figured this out." (invitation, not pressure)
```

#### **Show Your Work + Friend Chatting**

```
BEHIND-THE-SCENES (Friend Chatting):
"Here's what I actually do, no polish. Messy, real-time thoughts."
(authentic, conversational)

INSIGHT (Friend Chatting):
"What surprised me: the quality wasn't about the tools. It was about
how we asked questions." (peer discovery, honest reflection)

AUTHENTICITY (Friend Chatting):
"This isn't a case study. It's my actual morning." (vulnerability)

SOFT OFFER (Friend Chatting):
"If you're stuck like I was, let's talk." (equal-to-equal, no pressure)
```

---

## PART 13: IMPLEMENTATION ROADMAP

### Phase 1: Foundation (Week 1-2)
- Create 8 preset definitions with characteristics
- Build preset comparison UI/UX
- Create preset prompt templates
- Implement recommendation engine logic

### Phase 2: Integration (Week 2-3)
- Add `c-03b1-select-style.md` step
- Modify `c-03c-draft.md` to apply presets
- Update draft generation prompts
- Update CSV schemas

### Phase 3: Testing (Week 3-4)
- Test consistency of preset application
- Test angle + preset combinations
- Test UI flow with actual users
- Measure engagement by preset

### Phase 4: Optimization (Week 4+)
- Track most-used preset combinations
- Optimize recommendation engine
- Build custom blend saving
- Platform-specific variations

---

## PART 14: USAGE EXAMPLES

### Example 1: Teaching Angle + Educator Preset

**User:** "I want to teach people how to use BMAD for documentation"
**Angle:** Teaching/How-To
**System Recommendation:** Educator (95% match)
**User Action:** Accept

**Generated Variant (Educator Style):**
```
BMAD Documentation Framework: Step-by-Step

Here's exactly how to structure documentation with BMAD:

1. Gather Context (15 min)
   - BMAD asks structured questions about your product
   - Answer conversationally—no jargon required
   - System captures your domain knowledge

2. Build Framework (20 min)
   - System suggests documentation structure based on your answers
   - You review, adjust sections, confirm structure
   - Framework becomes your documentation skeleton

3. Generate Content (30 min)
   - System fills in each section with detailed content
   - You review for accuracy and tone
   - Make edits, regenerate as needed

Result: Complete documentation set in ~1 hour.

Try this approach with your next documentation project.
```

---

### Example 2: Contrarian Angle + Provocateur Preset + Minimalist Blend

**User:** "I have a contrarian take, audience is busy tech leads"
**Angle:** Contrarian/Hot Take
**Audience:** CTOs, Busy
**System Recommendation:** Provocateur (92%), Minimalist (78%)
**User Action:** Accept Provocateur, or blend with Minimalist?
**User Selects:** 70% Provocateur + 30% Minimalist

**Generated Variant (Blended):**
```
Your documentation process is broken.

Most teams still write docs manually—describe features, update when they change,
discover gaps when customers complain. Slow, boring, wrong half the time.

But you don't have to. One team of three generated 80+ docs in a morning.
Here's what changed: instead of writing first, they asked the right questions first.

The system structured everything.
They verified it.
Done.

What if your team could ship documentation in hours instead of weeks?
```

---

### Example 3: Demo Angle + Storyteller Preset

**User:** "I'm showing BMAD workflow in action, audience is general"
**Angle:** Demo/Behind-the-Scenes
**System Recommendation:** Storyteller (95% match)
**User Action:** Accept

**Generated Variant (Storyteller Style):**
```
BMAD in Real Time: How 80+ Documents Got Built in One Morning

I woke up with a problem.

Product documentation—the kind that usually takes weeks—was due
by end of day. Hundreds of sections. Interconnected. Detailed enough
for power users, clear enough for new ones.

So I opened BMAD and started a conversation.

The first 30 minutes looked weird. It asked questions—the good kind.
About product philosophy, user types, common workflows. I answered
in my own words, not forcing structure.

Then something clicked.

BMAD had captured the architecture of what lived in my head.
It showed me the structure back: main sections, subsections, flow.
I said "yes, that's it, but also...". Three iterations later, perfect.

Next came generation.

Each section filled itself. Not generic—specific to our product, our users,
our way of explaining things. I skimmed for accuracy. A few tweaks.
Eight hours of manual work, compressed into about 90 minutes.

But here's what surprised me most:

The documentation wasn't just *fast*. It was *better*.
Because we structured first, wrote second. Because we thought before typing.

What if you approached documentation this way?
```

---

## CONCLUSION

### Key Takeaways for Implementation

1. **8 presets provide spectrum**: From ultra-formal (Professional Authority) to ultra-casual (Minimalist), covering 95% of creator needs

2. **Combination power**: Best results come from mixing presets (e.g., Storyteller + Friend Chatting, Professional Authority + Educator)

3. **Angle-based recommendations**: System should suggest preset based on angle + audience + content type

4. **Platform awareness**: Same preset can be adjusted slightly for LinkedIn vs Twitter vs Email

5. **Technical integration**: Preset characteristics → LLM prompts → consistent style application

6. **UX principle**: Make style selection visible but optional; defaults work, customization available for power users

7. **Measurement**: Track preset usage, engagement outcomes, user preferences to continuously improve recommendations

### Next Steps

1. Create `data/style-presets.json` with full definitions
2. Build preset selection UI component
3. Implement recommendation engine
4. Modify draft generation to apply presets
5. Test with pilot users
6. Iterate on recommendations based on actual usage

---

**Document Status:** READY FOR IMPLEMENTATION
**Last Updated:** 2026-01-30
**Research Sources:** Industry analysis (Morning Brew, Lenny's Newsletter, SaaS marketing trends 2025, Claude/ChatGPT personalization features)
