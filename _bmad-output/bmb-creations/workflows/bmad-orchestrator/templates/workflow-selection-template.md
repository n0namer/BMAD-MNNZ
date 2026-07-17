---
title: "Workflow Selection Results"
workflow_id: "[auto-generated: selection-YYYY-MM-DD-HHmmss]"
session_date: "[YYYY-MM-DD]"
selected_workflow: "[workflow name]"
confidence_score: "[0-100]"
reasoning: "[Why this workflow was selected]"
mcp_sources_used: "[memory|octocode|brave|context7|none]"
user_context: "[Brief task description from user]"
status: "READY_FOR_EXECUTION"
---

# Workflow Selection Results

**Created:** [timestamp]
**Session:** [session_id]
**User Task:** [Original user task description]

---

## Selected Workflow

### Primary Recommendation

| Field | Value |
|-------|-------|
| **Workflow ID** | [workflow_id] |
| **Workflow Name** | [workflow_name] |
| **Module** | [bmm\|bmb\|tea\|cis\|core] |
| **Type** | [planning\|implementation\|testing\|design\|analysis] |
| **Est. Duration** | [X minutes] |
| **Steps Count** | [N] |
| **Complexity** | [low\|medium\|high] |
| **Confidence Score** | [XX]% |

**Workflow Path:** `[path/to/workflow.md]`

**Description:** [Workflow purpose and what it delivers]

---

## Confidence Scoring Analysis

### CSV Matching Results

| Match Type | Score | Details |
|-----------|-------|---------|
| **Name Match** | [0-100] | [Exact\|Partial\|None] |
| **Tag Match** | [0-75] | Matched tags: [tag1, tag2, ...] |
| **Module Match** | [0-50] | User context maps to module: [module] |
| **Category Match** | [0-40] | Task category alignment |
| **CSV Total Score** | [0-100] | **[Weighted calculation]** |

### MCP Search Results (if applicable)

#### Memory (ReasoningBank Patterns)
- **Status:** [Searched\|Not searched\|Failed]
- **Results Found:** [N] patterns
- **Top Match:** [Pattern description] (Confidence: [XX]%)
- **Score Contribution:** [XX] points

#### OctoCode (GitHub Code Patterns)
- **Status:** [Searched\|Not searched\|Failed]
- **Results Found:** [N] repositories
- **Top Match:** [Repo/pattern description] (Confidence: [XX]%)
- **Score Contribution:** [XX] points

#### Brave/Tavily (Public Web Search)
- **Status:** [Searched\|Not searched\|Failed]
- **Results Found:** [N] articles/resources
- **Top Match:** [Article/resource title] (Confidence: [XX]%)
- **Score Contribution:** [XX] points

#### Context7 (Library Documentation)
- **Status:** [Searched\|Not searched\|Failed]
- **Results Found:** [N] library references
- **Top Match:** [Library/doc reference] (Confidence: [XX]%)
- **Score Contribution:** [XX] points

### Final Score Calculation

```
CSV Score:           [XX] × 0.60 = [XX] points
MCP Score:           [XX] × 0.40 = [XX] points
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FINAL CONFIDENCE:    [XX]%
```

**Interpretation:**
- **85-100%:** Excellent match - Auto-proceed
- **70-84%:** Good match - Proceed with note
- **55-69%:** Fair match - Consider alternatives
- **<55%:** Weak match - Ask user or show alternatives

---

## Alternative Workflows

### Option 2: [Workflow Name]

| Field | Value |
|-------|-------|
| **Workflow ID** | [workflow_id_2] |
| **Module** | [module_2] |
| **Confidence** | [XX]% |
| **Why Consider** | [Alternative benefits] |

**Relevance:** [How this differs from primary choice]

---

### Option 3: [Workflow Name]

| Field | Value |
|-------|-------|
| **Workflow ID** | [workflow_id_3] |
| **Module** | [module_3] |
| **Confidence** | [XX]% |
| **Why Consider** | [Alternative benefits] |

**Relevance:** [How this differs from primary choice]

---

## Dependencies Analysis

### Required Workflows (Must Complete First)
- [ ] [Dependency 1] - [Reason why needed]
- [ ] [Dependency 2] - [Reason why needed]

### Recommended Prerequisites (Optional but Helpful)
- [ ] [Recommended 1] - [Why helpful]
- [ ] [Recommended 2] - [Why helpful]

### Compatible Parallel Workflows
- [ ] [Parallel 1] - [Can run at same time as selected workflow]
- [ ] [Parallel 2] - [Can run at same time as selected workflow]

---

## Reasoning & Justification

### Why This Workflow?

**Primary Factors:**
1. **Best Match for Task:** [Explanation of how workflow addresses user's task]
2. **Optimal Complexity:** [Workflow complexity matches task requirements]
3. **Time Efficiency:** [Estimated duration fits user's timeframe]
4. **Expert Coverage:** [Relevant expertise provided by workflow steps]

**Supporting Evidence:**
- CSV matching: [Tag matches and relevance factors]
- MCP validation: [Which MCP sources confirmed relevance]
- Domain alignment: [How module expertise matches task]
- Workflow maturity: [Workflow tested and validated]

### Potential Limitations

- **Limitation 1:** [Description and workaround]
- **Limitation 2:** [Description and workaround]
- **Limitation 3:** [Description and workaround]

### When to Use Alternatives

Choose Option 2 if: [Condition 1]
Choose Option 3 if: [Condition 2]

---

## Workflow Metadata

### Tags
`[tag1]` `[tag2]` `[tag3]` `[tag4]` `[tag5]`

### Related Workflows
- [Related workflow 1] - [Relationship type: precedes/follows/complements]
- [Related workflow 2] - [Relationship type: precedes/follows/complements]

### BMAD Module Info

**Module:** [bmm\|bmb\|tea\|cis\|core]
**Category:** [analysis\|planning\|solutioning\|implementation\|testing]
**Agent Types:** [List of recommended agents for this workflow]

---

## Next Steps

### To Execute This Workflow

1. **Review:** Confirm this workflow matches your needs
2. **Prepare:** Gather any input materials or context needed
3. **Start:** Launch workflow execution (Step 04)
4. **Track:** Monitor progress through phases
5. **Validate:** Review outputs at checkpoints

### If You Want to Adjust Selection

- [ ] Choose Alternative Option 2
- [ ] Choose Alternative Option 3
- [ ] Provide more specific task description
- [ ] Ask for manual workflow selection
- [ ] Modify scope/requirements

---

## Selection Metadata

**Confidence Calculation Method:** CSV + MCP hybrid
**CSV Manifest Version:** [Version/date]
**MCP Sources Queried:** [memory, octocode, brave, context7]
**Selection Timestamp:** [ISO 8601 timestamp]
**Selected By:** [claude-code\|orchestrator\|user]
**Validated By:** [Validation step status]

---

## Traceability

**Related Documents:**
- Orchestration Plan: [`orchestration-session-[SESSION-ID].md`]
- Task Definition: [From step-01 discovery]
- Execution Results: [Will be populated in step-04]

**Session Context:**
- Session ID: [session_id]
- YOLO Level: [0-3]
- Approval Method: [auto\|manual\|hybrid]

---

*Template Version: 2.0 | Last Updated: 2026-02-26*
