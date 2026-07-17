# SAMPLE TEST DATA FOR CONTENT MACHINE PIPELINE

**Ready-to-use test data for all scenarios**

---

## FILE 1: ideas_inbox.csv (After Test Case 1)

```csv
id,date_added,source,raw_idea,content_type,idea_metadata,category,status,notes
1,2026-01-30,routine,"Generated 80+ high-quality documents in 2 hours using BMAD",demo,"{""visual_context"":""BMAD interface showing document generation workflow with results panel displaying 80+ documents"",""tools_used"":[""BMAD"",""Claude"",""PDF export""],""demonstrated_result"":""80+ professional documents ready for publication"",""context_type"":""business automation"",""business_problem"":""document bottleneck for entrepreneurs""}",demo,active,"Screenshot analyzed via Vision API - context extracted successfully"
2,2026-01-30,user_input,"How to scale personal brand without hiring freelance writers - system over hiring",text,"{""source"":""user_inspiration""}",personal-branding,active,"Standard text idea workflow"
```

**Key Points:**
- Record 1: Content Machine demo input (full metadata JSON)
- Record 2: Standard text idea (minimal metadata)
- Column `idea_metadata` contains JSON (shown with escaped quotes here)

---

## FILE 2: ideas_research.csv (After Research Stage)

```csv
id,original_idea_id,research_date,main_angle,sub_angles_count,best_angle_id,angles_list,sources_count,avg_relevance
1,1,2026-01-30,"Document Automation & Speed",5,"angle_1","[""Speed of document generation"",""Scalability without hiring"",""Process documentation"",""Quality consistency"",""Knowledge capture""]",12,88
2,2,2026-01-30,"Personal Brand Scaling",5,"angle_1","[""Systems vs hiring"",""Content efficiency"",""Personal brand leverage"",""Time management for founders"",""Authentic scaling""]",9,85
```

**Key Points:**
- Each idea gets research with 5 angles minimum
- angles_list is JSON array (shown as string here)
- avg_relevance is average across all sources

---

## FILE 3: pain_points.json (In workflow_state.json context)

**For angle_1 (Document Automation & Speed):**

```json
{
  "angle_1": {
    "angle_name": "Document Automation & Speed",
    "pains": [
      {
        "pain": "Manual document creation is extremely slow (1 doc = 30 min → 80 docs = 40+ hours)",
        "business_impact": "Delays product launches and market response",
        "severity": "critical"
      },
      {
        "pain": "No documented processes means business cannot be delegated or sold",
        "business_impact": "Founder dependency = low business valuation",
        "severity": "critical"
      },
      {
        "pain": "Dependency on founder's expertise for all document creation",
        "business_impact": "Cannot scale team or exit business",
        "severity": "high"
      },
      {
        "pain": "Hiring specialized document writers is expensive (lawyers, marketers, analysts)",
        "business_impact": "Cost barrier to scaling documentation quality",
        "severity": "high"
      },
      {
        "pain": "No version control or quality consistency in document archives",
        "business_impact": "Clients see unprofessional documentation",
        "severity": "medium"
      }
    ]
  }
}
```

---

## FILE 4: offer_filter.csv (User Preferences)

```csv
offer_type,willing,price_range_expected,effort_level,notes
training,yes,500-2000,medium,"Individual sessions or mini-groups - scalable teaching model"
setup,yes,3000-7000,high,"3-5 day implementation projects - custom to client needs"
templates,yes,100-500,low,"Template packs and reference guides - one-time creation"
consulting,yes,200-500/hour,medium,"Process consultation and architecture sessions - extracting knowledge"
full_dev,no,,,""
```

**Usage:** Save to `user_preferences/offer_filter.csv` on first run
**Reuse:** On second and subsequent demo ideas, use same filter without re-prompting

---

## FILE 5: generated_offers.json (Automated Generation Output)

**For angle_1 (Document Automation & Speed):**

```json
{
  "angle_1": [
    {
      "offer_type": "training",
      "title": "BMAD Document Generation Mastery",
      "description": "Learn to generate 80+ professional documents in 2 hours like in the demo. You'll get the complete workflow, pre-built templates, and step-by-step process documentation. Training includes hands-on practice with your own document types.",
      "cta": "Interested in learning this skill? Drop a line in DMs – we can discuss individual sessions or small group training options.",
      "pain_solved": "Manual document creation is extremely slow; dependency on founder expertise",
      "effort_level": "medium",
      "reasoning": "Routine demonstrates real tool (BMAD) producing concrete, scalable results. Training is highly scalable teaching model, solves both speed and delegation pains.",
      "target_audience": "Founders who manage their own documentation; marketing/ops teams struggling with document volume"
    },
    {
      "offer_type": "setup",
      "title": "BMAD Workflow Setup for Your Business (3-5 Days)",
      "description": "I'll design and deploy a document generation workflow customized to your specific needs. Your team gets a fully functional system, complete training, and handoff documentation. All setup and configuration done - you just use it.",
      "cta": "Tell me about your documentation bottleneck – I'll show you exactly how this works for your specific case.",
      "pain_solved": "No documented processes; business cannot scale without founder; hiring specialists is expensive",
      "effort_level": "high",
      "reasoning": "Setup addresses three critical pains: process documentation, team scaling, cost reduction. High effort and high value justify premium pricing.",
      "target_audience": "Growing companies with documentation bottleneck; businesses wanting to improve valuation through process documentation"
    },
    {
      "offer_type": "templates",
      "title": "BMAD Template Pack for Document Generation",
      "description": "40+ pre-built BMAD schemas and templates for different document types (contracts, proposals, policies, guides, etc.). Adapt them to your context and start generating immediately. Includes step-by-step setup instructions.",
      "cta": "Want to skip the setup phase? Grab the template pack and start generating in hours instead of weeks.",
      "pain_solved": "No standardized templates; inconsistent documentation quality; knowledge scattered",
      "effort_level": "low",
      "reasoning": "Templates solve consistency and knowledge capture problems with minimal effort. High scalability, low delivery cost = good margin product.",
      "target_audience": "Teams that want to implement systems themselves; companies looking for quick wins"
    }
  ]
}
```

---

## FILE 6: Draft Posts with Offers Embedded

**DRAFT 1: Hook-Story-Offer Framework**

```
═══════════════════════════════════════════════════════════════════

DRAFT 1 - HOOK-STORY-OFFER

═══════════════════════════════════════════════════════════════════

Content:

BMAD turned my biggest bottleneck into a superpower. 📚

Here's what happened: 80+ documents that used to take weeks... now generated in 2 hours. Not AI-written rough drafts that need rewriting. Clean, structured, publication-ready docs.

The breakthrough? Stopped thinking "how do I write these documents" and started thinking "how do I build a system that writes them."

That system: BMAD templates + Claude's contextual understanding = a document factory.

Two things became clear:
1. Most founders think documentation is a writing problem. It's actually a systems problem.
2. Once it becomes a system, it scales without you.

80 documents in 2 hours isn't magic. It's using the right tool + the right process.

Now here's what's interesting: this workflow is genuinely valuable for anyone drowning in documentation work. I've helped founders go from "documents scattered everywhere" to "document generation system that runs automatically."

Not a course. Not a template collection (though we use those). Direct mentorship on building this exact system for your business.

Want to learn? Drop a line in DMs – we can talk about individual sessions or small group options.

If not now, stay tuned – more of these automation wins coming.

═══════════════════════════════════════════════════════════════════

Framework: Hook-Story-Offer
Quality Score: 92/100
CTR Potential: 4.5%
Engagement Score: 4.8/5.0
Offers Embedded: 2 (training mentorship, setup services implied)
```

**DRAFT 2: Problem-Agitate-Solution (PAS) Framework**

```
═══════════════════════════════════════════════════════════════════

DRAFT 2 - PROBLEM-AGITATE-SOLUTION

═══════════════════════════════════════════════════════════════════

Content:

Your documentation work is eating your life.

Think about it: 40+ hours per month writing documents. Formatting. Updating versions. Explaining to people why documents keep changing. Your processes live in your head because nobody has time to document them properly. You can't delegate. You can't sell the business because "no documented processes = business is you."

Meanwhile, there's a system that can generate 80+ professional documents in 2 hours.

Not rough AI drafts that need rewriting. Publication-ready, structured documents that your team can use immediately.

The difference? Most people think "documentation" is a writing problem. It's actually a systems problem.

I've worked with founders to build this system. Their teams now generate in 2 hours what used to take 2 weeks. Same quality or better. Zero heroic efforts.

The pattern is always the same: document generation becomes invisible (in a good way). It just happens.

Want to build this for your business? Message me. We can explore what this looks like for your specific situation.

═══════════════════════════════════════════════════════════════════

Framework: Problem-Agitate-Solution
Quality Score: 88/100
CTR Potential: 4.2%
Engagement Score: 4.4/5.0
Offers Embedded: 1 (consulting/setup services)
```

**DRAFT 3: Show Your Work (Behind-the-Scenes) Framework**

```
═══════════════════════════════════════════════════════════════════

DRAFT 3 - SHOW YOUR WORK

═══════════════════════════════════════════════════════════════════

Content:

Generated 80+ documents today. In 2 hours.

Used to take 3 weeks.

Here's the one thing that changed my approach: I stopped asking "how do I write these documents faster" and started asking "how do I build a system that does it for me?"

The system: BMAD templates + Claude. I describe the context, it generates structured, publication-ready documents.

Why share this?

Most founders think documentation is a writing bottleneck. It's actually a systems bottleneck.

Once you solve it as a system, it becomes leverage. Your team doesn't write documentation anymore – they configure it. At scale.

This is what "going from founder-dependent to founder-scale" actually looks like.

Not in theory. In actual day-to-day work.

═══════════════════════════════════════════════════════════════════

Framework: Show Your Work (Behind-the-Scenes)
Quality Score: 85/100
CTR Potential: 3.9%
Engagement Score: 4.2/5.0
Offers Embedded: 0 (pure engagement/thought leadership)
```

---

## FILE 7: posts_content.csv (Final CSV Export)

```csv
id,research_id,angle_used,publish_date,platform,post_title_short,content_500_chars,content_250_chars,content_100_chars,quality_score,ctr_potential,engagement_score,status,notes
1,1,"angle_1",NULL,telegram,"80+ docs in 2 hours with BMAD","BMAD turned my biggest bottleneck into a superpower. 80+ documents in 2 hours, not weeks. The breakthrough: thinking 'systems' not 'writing.' If this interests you, DMs are open.","80+ docs in 2 hours with BMAD","BMAD documents",92,4.5,4.8,draft,"Content Machine: Hook-Story-Offer framework with 2 offers embedded"
2,1,"angle_1",NULL,telegram,"Document systems beat document writing","Your docs are written like 1995. 40+ hours monthly on formatting. BMAD + Claude generates 80+ documents in 2 hours. Difference: thinking systems not writing.","Document systems win","Process not writing",88,4.2,4.4,draft,"Content Machine: PAS framework with 1 offer embedded"
3,1,"angle_1",NULL,telegram,"Generated 80+ docs today. In 2 hours.","Generated 80+ documents today in 2 hours (used to be 3 weeks). The shift: 'How do I write faster?' → 'How do I build a system?'","Behind-the-scenes: 80+ docs","Building doc systems",85,3.9,4.2,draft,"Content Machine: Show Your Work framework (engagement focus)"
4,1,"angle_1",NULL,telegram,"BMAD: Where 3 weeks becomes 2 hours","Key insight: it's systems, not writing. BMAD templates + Claude understanding. One time this clicks, documentation scales without you.","Systems over writing","Rethinking documentation",90,4.4,4.6,draft,"Content Machine: Variant of Draft 1 – alternative hook"
5,1,"angle_1",NULL,telegram,"Your team doesn't write docs anymore","The transformation: from 'I write everything' to 'system generates documents.' Founder dependency gone. Delegation now possible.","Team generates docs","Scaling documentation",87,4.1,4.3,draft,"Content Machine: Variant of Draft 2 – rephrased problem"
6,1,"angle_1",NULL,telegram,"BMAD: The systems thinking behind fast docs","Deep dive into the decision that changed documentation workflow. Why systems thinking is the competitive advantage in document generation.","System thinking in docs","Process improvement",86,3.8,4.1,draft,"Content Machine: Variant of Draft 3 – extended process angle"
```

**Key Observations:**
- All 6 records from single idea/angle
- Quality scores vary (85-92)
- CTR potential varies (3.8-4.5)
- Engagement scores vary (4.1-4.8)
- Notes clearly identify Content Machine framework usage
- All marked as "draft" (ready for user review before publishing)

---

## FILE 8: workflow_state.json (Full State File)

```json
{
  "workflow_id": "idea-to-post-pipeline",
  "session_id": "test-session-cm-001",
  "currentMode": "CREATE",
  "currentStep": "c-03e-finalize",
  "content_type": "demo",
  "stepsCompleted": [
    "step-01-init",
    "c-01-add-idea",
    "c-01b-dedup-check",
    "c-02a-load-ideas",
    "c-02b-select-idea",
    "c-02c-research",
    "c-02d-results",
    "c-03b1-offer-check",
    "c-03b2-offer-generation",
    "c-03c-draft",
    "c-03d-variants"
  ],
  "context": {
    "demo_input": {
      "screenshot": "D:\\test_data\\bmad_screenshot_80docs.png",
      "description": "Generated 80+ high-quality documents in 2 hours using BMAD",
      "tools_used": ["BMAD", "Claude", "PDF export"],
      "visual_context": "BMAD interface showing document generation workflow with results panel displaying 80+ documents generated",
      "demonstrated_result": "80+ professional documents ready for publication",
      "context_type": "business automation",
      "business_problem": "document bottleneck for entrepreneurs"
    },
    "selected_idea": {
      "id": 1,
      "date_added": "2026-01-30",
      "raw_idea": "Generated 80+ high-quality documents in 2 hours using BMAD"
    },
    "research_results": {
      "research_id": 1,
      "angles": [
        {
          "angle_id": "angle_1",
          "name": "Document Automation & Speed",
          "description": "Fast document generation as competitive advantage",
          "relevance_score": 92
        },
        {
          "angle_id": "angle_2",
          "name": "Scalability Without Hiring",
          "description": "Document systems instead of hiring writers",
          "relevance_score": 89
        },
        {
          "angle_id": "angle_3",
          "name": "Process Documentation",
          "description": "Making business processes visible and transferable",
          "relevance_score": 87
        },
        {
          "angle_id": "angle_4",
          "name": "Quality Consistency",
          "description": "System-based documentation maintains quality at scale",
          "relevance_score": 85
        },
        {
          "angle_id": "angle_5",
          "name": "Knowledge Capture",
          "description": "Turning founder knowledge into documented processes",
          "relevance_score": 83
        }
      ],
      "total_sources": 12,
      "avg_relevance": 87
    },
    "selected_angle": {
      "angle_id": "angle_1",
      "name": "Document Automation & Speed"
    },
    "pain_points": {
      "angle_1": [
        "Manual document creation is extremely slow (1 doc = 30 min → 80 docs = 40+ hours)",
        "No documented processes means business cannot be delegated or sold",
        "Dependency on founder's expertise for all document creation",
        "Hiring specialized document writers is expensive",
        "No version control or quality consistency in document archives"
      ],
      "angle_2": [
        "Cannot hire fast enough to keep up with document demand",
        "Document writer salaries eat into profit margins",
        "Quality varies between different writers",
        "Knowledge scattered without systematic approach"
      ],
      "angle_3": [
        "Processes exist only in people's heads",
        "No way to train new team members efficiently",
        "Business cannot be delegated to managers",
        "Selling business impossible without documented processes"
      ],
      "angle_4": [
        "Inconsistent document style across company",
        "No way to enforce quality standards at scale",
        "Client perception of professionalism affected",
        "Rework required due to quality inconsistency"
      ],
      "angle_5": [
        "Founder knowledge is business liability",
        "No knowledge transfer mechanism",
        "Business cannot function without founder",
        "New team members take months to get up to speed"
      ]
    },
    "offer_filter": {
      "training": true,
      "setup": true,
      "templates": true,
      "consulting": true,
      "full_dev": false,
      "filter_created_date": "2026-01-30T14:22:00Z"
    },
    "generated_offers": {
      "angle_1": [
        {
          "offer_type": "training",
          "title": "BMAD Document Generation Mastery",
          "description": "Learn to generate 80+ professional documents in 2 hours like in the demo.",
          "cta": "Interested in learning this skill? Drop a line in DMs.",
          "pain_solved": "Manual document creation is extremely slow; founder expertise dependency",
          "effort_level": "medium",
          "reasoning": "Real tool, concrete results, scalable teaching model."
        },
        {
          "offer_type": "setup",
          "title": "BMAD Workflow Setup for Your Business (3-5 Days)",
          "description": "Custom document generation system built for your needs.",
          "cta": "Tell me about your documentation bottleneck.",
          "pain_solved": "No documented processes; business cannot scale; hiring is expensive",
          "effort_level": "high",
          "reasoning": "Addresses three critical pains simultaneously."
        },
        {
          "offer_type": "templates",
          "title": "BMAD Template Pack for Document Generation",
          "description": "40+ pre-built BMAD schemas for different document types.",
          "cta": "Want to skip the setup phase? Grab the template pack.",
          "pain_solved": "No standardized templates; inconsistent quality; knowledge scattered",
          "effort_level": "low",
          "reasoning": "Quick win, high scalability, good margins."
        }
      ]
    },
    "drafts": [
      {
        "draft_id": 1,
        "framework": "Hook-Story-Offer",
        "quality_score": 92,
        "ctr_potential": 4.5,
        "engagement_score": 4.8,
        "offers_embedded": 2,
        "offers_mentioned": ["training", "setup"],
        "content_preview": "BMAD turned my biggest bottleneck into a superpower. 80+ documents in 2 hours..."
      },
      {
        "draft_id": 2,
        "framework": "Problem-Agitate-Solution (PAS)",
        "quality_score": 88,
        "ctr_potential": 4.2,
        "engagement_score": 4.4,
        "offers_embedded": 1,
        "offers_mentioned": ["setup"],
        "content_preview": "Your documentation work is eating your life. 40+ hours monthly..."
      },
      {
        "draft_id": 3,
        "framework": "Show Your Work (Behind-the-Scenes)",
        "quality_score": 85,
        "ctr_potential": 3.9,
        "engagement_score": 4.2,
        "offers_embedded": 0,
        "offers_mentioned": [],
        "content_preview": "Generated 80+ documents today. In 2 hours..."
      }
    ],
    "variants": [
      {
        "variant_id": 4,
        "based_on_draft": 1,
        "framework": "Hook-Story-Offer (Alternative)",
        "quality_score": 90,
        "ctr_potential": 4.4,
        "engagement_score": 4.6,
        "offers_embedded": 2,
        "change_type": "alternative_hook"
      },
      {
        "variant_id": 5,
        "based_on_draft": 2,
        "framework": "PAS (Rephrased)",
        "quality_score": 87,
        "ctr_potential": 4.1,
        "engagement_score": 4.3,
        "offers_embedded": 1,
        "change_type": "problem_reframe"
      },
      {
        "variant_id": 6,
        "based_on_draft": 3,
        "framework": "Show Your Work (Extended)",
        "quality_score": 86,
        "ctr_potential": 3.8,
        "engagement_score": 4.1,
        "offers_embedded": 0,
        "change_type": "extended_process"
      }
    ]
  },
  "sessionMetadata": {
    "startTime": "2026-01-30T14:15:00Z",
    "lastUpdated": "2026-01-30T14:22:45Z",
    "totalDuration": "7 minutes 45 seconds",
    "userInteractions": 7,
    "csvUpdates": 2,
    "apiCalls": {
      "vision_api": 1,
      "claude_llm": 9,
      "web_search": 0
    }
  }
}
```

---

## USAGE INSTRUCTIONS

1. **For Test Case 1 (Full Demo):**
   - Use this sample data as reference
   - Files are generated automatically during execution
   - Verify actual output matches structure

2. **For Test Case 2 (Text Only):**
   - Skip offer_filter and generated_offers sections
   - Use only ideas_inbox and posts_content from text workflow

3. **For Error Testing:**
   - Corrupt workflow_state.json (remove closing brace)
   - Verify system recovery
   - Check .bak file creation

4. **For CSV Validation:**
   - Import posts_content.csv into spreadsheet
   - Verify numeric ranges
   - Check for proper escaping (double quotes)

---

**Sample Data Version:** 1.0
**Created:** 2026-01-30
**For Use With:** Content Machine Pipeline Tests
