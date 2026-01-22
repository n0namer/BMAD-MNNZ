---
name: 'step-03b-evidence-gathering'
description: 'Collect evidence from identified sources across all requirement categories'

nextStepFile: './step-03c-mcp-reconciliation.md'
outputFile: '{output_folder}/ember-consilium-{user_name}-{date}.md'

# Tasks
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'

# Data references
evaluationCriteria: '../data/evaluation-criteria.md'
---

# Step 3b: Evidence Gathering & Collection

## 🚨 MCP PARAMETER ANTI-RESTRICTION RULES

**FORBIDDEN RESTRICTIVE PARAMETERS:**

❌ DON'T: Unnecessarily restrict by language
octocode.searchCode({
  query: "authentication",
  extension: "py"  // ❌ TOO RESTRICTIVE unless Python specifically needed
})

✅ DO: Keep broad unless specific need
octocode.searchCode({
  query: "authentication implementation patterns",
  limit: 10  // Reasonable default
})

❌ DON'T: Use tiny limits
brave.webSearch({
  query: "scalability best practices",
  count: 3  // ❌ TOO FEW results
})

✅ DO: Use reasonable limits
brave.webSearch({
  query: "scalability best practices",
  count: 10  // ✅ Good default
})

❌ DON'T: Over-filter unnecessarily
brave.newsSearch({
  query: "API trends",
  freshness: "pd"  // ❌ Only past day - too restrictive
})

✅ DO: Use appropriate freshness
brave.newsSearch({
  query: "API trends",
  freshness: "pm"  // ✅ Past month - better balance
})

WHEN TO USE RESTRICTIONS:
- User explicitly asks for specific language
- Problem domain clearly requires specific tech
- Previous broad search returned irrelevant results

WHEN TO AVOID RESTRICTIONS:
- Default/initial searches
- Exploratory research
- When gathering diverse perspectives
- When problem could be solved multiple ways

PARAMETER REVIEW CHECKLIST:
Before each MCP call, verify:
- [ ] Is 'extension' needed? (usually NO)
- [ ] Is limit/count sufficient? (usually 10+ is better)
- [ ] Is freshness filter necessary? (usually broader is better)
- [ ] Am I restricting based on assumptions vs user needs?

---

## PROBLEM-SPECIFIC DATA REQUIREMENTS

🚨 THIS STEP REQUIRES ACTUAL DATA FROM USER'S PROBLEM

FORBIDDEN - Generic Processing:
- Working with placeholder "[user_problem]"
- Using example data instead of real data
- Proceeding without user's specific information
- Copying template text into output

REQUIRED - Problem-Specific Processing:
- Obtain user's actual problem description
- Use user's actual constraints/requirements
- Reference user's actual context
- Fill templates with real data from this decision

Data Validation Before Proceeding:

Check 1: Do I have user's actual problem?
User's Problem: "[actual description from user]"
Validation:
- Is this specific? [Yes/No]
- Is this the real problem? [Yes/No]
- Is this complete enough? [Yes/No]
If any No → ask user for clarification

Check 2: Do I have problem-specific context?
Context Available:
- Technical context: [actual technical details]
- Business context: [actual business constraints]
- Timeline: [actual deadline/timeframe]
- Resources: [actual team/budget/tools]
- Constraints: [actual limitations]
If any missing → ask user to provide

Check 3: Am I using this data in my work?
Review your output:
- Does it reference user's specific problem? [Yes/No]
- Does it use user's actual constraints? [Yes/No]
- Is it customized to user's context? [Yes/No]
- Would this work for a different problem? [If Yes → too generic]
If too generic → redo with problem-specific data

BEFORE EACH SECTION:
Ask yourself: "Am I working with real data or placeholders?"
- If placeholders → get real data first
- If real data → verify it's being used

ANTI-GENERIC CHECKLIST:
- [ ] No "[placeholder]" text in output
- [ ] No "for example" scenarios unless supplementing real analysis
- [ ] No generic template text unmodified
- [ ] All factors/criteria are specific to this problem
- [ ] All evidence relates to this problem
- [ ] All options address this problem specifically

## STEP GOAL:

To systematically collect evidence from identified sources across all requirement categories for comprehensive decision analysis foundation.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are an EMBER Consilium Analyst
- ✅ We engage in collaborative evidence collection, not unilateral research
- ✅ You bring systematic collection methodologies and documentation frameworks
- ✅ User brings domain expertise and source access for gathering
- ✅ Together we build comprehensive evidence foundation

### Step-Specific Rules:

- 🎯 Focus only on evidence collection from identified sources (not validation)
- 🚫 FORBIDDEN to assess quality or make judgments yet
- 💬 Approach: Comprehensive multi-source collection with systematic documentation
- 📋 Document all sources and findings transparently

## EXECUTION PROTOCOLS:

- 🎯 Collect evidence from all identified source categories
- 💾 Document sources and findings comprehensively
- 📖 Complete evidence foundation for validation phase
- 🚫 Only collect evidence - validation comes next

## CONTEXT BOUNDARIES:

- Available context: Sources identified in step-3a1
- Focus: Evidence collection, source gathering, systematic documentation
- Limits: Do not assess quality or make recommendations
- Dependencies: Source identification completed

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Load Source Identification & MCP Configuration

"**Loading source identification and activating adaptive MCP stack...**"

Load source identification from {outputFile}:
- Source categories established
- Category-source mappings completed
- MCP tools configured from previous step
- Collection readiness confirmed

**Activate Configured MCP Stack:**
```
Активные MCP инструменты: [list from step 3a]
Режим работы: Автоматизированный сбор с human oversight
Цель: Evidence-based сбор данных по всем категориям
```

### 2. MCP-Driven Technical Evidence Collection

"**Launching MCP-automated technical evidence collection...**"

**Technical Evidence Categories (MCP-Enhanced):**
- Current technology stack assessment (via octocode-mcp + context7-mcp)
- Technical constraints and limitations (via brave-search-mcp + perplexity-mcp)
- Scalability and performance requirements (via sequentialthinking)
- Integration capabilities and APIs (via octocode-mcp)
- Security and compliance requirements (via brave-search-mcp)

**Automated MCP Collection:**
```javascript
// MCP Orchestration Logic
const technicalEvidence = await Promise.all([
  octocode.mcp.searchCode({query: "technology stack assessment"}),
  context7.mcp.queryDocs({libraryId: "tech-stack", query: "constraints"}),
  brave.mcp.webSearch({query: "scalability best practices"}),
  perplexity.mcp.ask({messages: [{role: "user", content: "API integration patterns"}]})
]);
```

### 3. MCP-Driven Business Evidence Collection

"**Launching MCP-automated business evidence collection...**"

**Business Evidence Categories (MCP-Enhanced):**
- Strategic objectives and priorities (via perplexity-mcp)
- Financial constraints and budgets (via brave-search-mcp)
- Market opportunities and threats (via brave-news-search-mcp)
- Competitive positioning (via perplexity-mcp)
- ROI expectations and timelines (via sequentialthinking)

**Automated MCP Collection:**
```javascript
const businessEvidence = await Promise.all([
  perplexity.mcp.research({messages: [{role: "user", content: "strategic objectives analysis"}]}),
  brave.mcp.webSearch({query: "market analysis reports"}),
  brave.mcp.newsSearch({query: "industry trends", freshness: "pm"}),
  sequentialthinking.mcp.reason({thought: "ROI calculation methodology"})
]);
```

### 4. MCP-Driven Operational Evidence Collection

"**Launching MCP-automated operational evidence collection...**"

**Operational Evidence Categories (MCP-Enhanced):**
- Current process workflows (via octocode-mcp + context7-mcp)
- Team capabilities and resources (via sequentialthinking)
- Training requirements (via brave-search-mcp)
- Change management considerations (via perplexity-mcp)
- Support and maintenance needs (via octocode-mcp)

**Automated MCP Collection:**
```javascript
const operationalEvidence = await Promise.all([
  context7.mcp.queryDocs({libraryId: "process-docs", query: "workflow optimization"}),
  octocode.mcp.searchCode({query: "team resource management"}),
  brave.mcp.webSearch({query: "change management best practices"}),
  perplexity.mcp.ask({messages: [{role: "user", content: "training program effectiveness"}]})
]);
```

### 5. MCP-Driven Risk Evidence Collection

"**Launching MCP-automated risk evidence collection...**"

**Risk Evidence Categories (MCP-Enhanced):**
- Implementation risks and challenges (via sequentialthinking + brave-search-mcp)
- Operational disruption potential (via perplexity-mcp)
- Security and compliance risks (via brave-search-mcp)
- Financial and budgetary risks (via brave-news-search-mcp)
- Timeline and dependency risks (via octocode-mcp)

**Automated MCP Collection:**
```javascript
const riskEvidence = await Promise.all([
  sequentialthinking.mcp.reason({thought: "implementation risk assessment"}),
  brave.mcp.webSearch({query: "operational disruption case studies"}),
  brave.mcp.newsSearch({query: "security compliance updates"}),
  perplexity.mcp.research({messages: [{role: "user", content: "financial risk analysis"}]})
]);
```

**MCP Output Reconciliation Protocol:**

When MCP servers return conflicting information:
```
EXAMPLE CONFLICT:
brave-search: "Option A is market leader, 45% share"
perplexity: "Option B shows rapid growth, +30% YoY"
octocode: "Option A has poor documentation, 2.3 GitHub stars"

RECONCILIATION STEPS:
1. Identify conflict type: [Different metrics / Contradictory claims / Temporal divergence]
2. Assess MCP credibility: Each MCP scored on output quality (1-5)
3. Weight MCP outputs by credibility × recency × relevance
4. Document unresolved conflicts explicitly
5. If conflict unresolvable: FLAG for manual investigation
6. Adjust confidence: -5% per unresolved MCP conflict
```

**MCP Conflict Summary:**
- Total MCP conflicts detected: [count]
- Resolved conflicts: [count] ([method used])
- Unresolved conflicts: [count] ([impact on confidence])
- Confidence adjustment: -[X]% due to MCP conflicts

### 6. Document Evidence Findings

"**Documenting evidence findings in the consilium report...**"

Update {outputFile} with evidence collection:

```markdown
## Evidence Collection

### Evidence Overview
**Total Sources Identified:** [count]
**Sources by Category:** [technical/business/operational/risk breakdown]
**Collection Date:** [current date]

### Technical Evidence Sources
- [Source 1]: [description] - [type: internal/external/expert/data]
- [Source 2]: [description] - [type: internal/external/expert/data]
- [Additional technical sources...]

### Business Evidence Sources
- [Source 1]: [description] - [type: internal/external/expert/data]
- [Source 2]: [description] - [type: internal/external/expert/data]
- [Additional business sources...]

### Operational Evidence Sources
- [Source 1]: [description] - [type: internal/external/expert/data]
- [Source 2]: [description] - [type: internal/external/expert/data]
- [Additional operational sources...]

### Risk Evidence Sources
- [Source 1]: [description] - [type: internal/external/expert/data]
- [Source 2]: [description] - [type: internal/external/expert/data]
- [Additional risk sources...]

### Key Findings Summary
- **Technical:** [summary of major findings]
- **Business:** [summary of major findings]
- **Operational:** [summary of major findings]
- **Risk:** [summary of major findings]
```

### 7. Update Consilium Progress

Update {outputFile} frontmatter:
```yaml
stepsCompleted: ['step-01-problem-analysis', 'step-02-decision-block-v2', 'step-03a1-evidence-identification', 'step-03a2-evidence-gathering']
progress: 35
currentPhase: 'evidence-collection'
lastStep: 'step-03a2-evidence-gathering'
evidenceCollectionComplete: true
```

### 8. Present MENU OPTIONS

Display: "**Select an Option:** [A] Advanced Elicitation [P] Party Mode [C] Continue to Evidence Validation"

#### Menu Handling Logic:

- IF A: Execute {advancedElicitationTask} for deeper evidence collection
- IF P: Execute {partyModeWorkflow} to discuss evidence sources with other agents
- IF C: Save evidence collection to {outputFile}, update frontmatter stepsCompleted, then only then load, read entire file, then execute {nextStepFile}
- IF Any other comments or queries: help user respond then [Redisplay Menu Options](#8-present-menu-options)

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'
- After other menu items execution, return to this menu
- User can chat or ask questions - always respond and then end with display again of the menu options

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN C is selected and evidence collection is saved to {outputFile} will you then load and read fully {nextStepFile} to execute and begin evidence validation.

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Evidence collected from all identified source categories
- All requirement categories comprehensively addressed
- Sources properly categorized and findings documented
- Collection process completed systematically
- Progress updated to 35% with evidence foundation established

### ❌ SYSTEM FAILURE:

- Evidence not collected from all identified categories
- Sources not properly categorized or incomplete
- Findings not systematically documented
- Collection process incomplete or inadequate
- Documentation inadequate or missing

**Master Rule:** Evidence gathering establishes the raw foundation for analysis - all identified sources must be systematically collected.
