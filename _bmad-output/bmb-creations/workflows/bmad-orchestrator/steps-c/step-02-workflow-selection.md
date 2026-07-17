---
name: 'step-02-workflow-selection'
description: 'Analyze task and propose appropriate BMAD workflows from the library'

nextStepFile: './step-03-orchestration-plan.md'
workflowLibrary: '{project-root}/.clinerules/workflows/'
workflowPlanFile: '{bmb_creations_output_folder}/workflows/bmad-orchestrator/workflow-plan-bmad-orchestrator.md'
intermediateFolder: '{bmb_creations_output_folder}/workflows/bmad-orchestrator/intermediate'
selectionTemplate: '{bmb_creations_output_folder}/workflows/bmad-orchestrator/intermediate/workflow-selection-template.md'
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step 2: Workflow Selection

## STEP GOAL:

To analyze the user's task and propose appropriate BMAD workflows from the library (75+ workflows available) that best match their needs.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are an orchestration architect
- ✅ Analyze task and match to BMAD workflow patterns
- ✅ Present options clearly with reasoning
- ✅ Let user confirm or adjust selections

### Step-Specific Rules:

- 🎯 Focus ONLY on workflow selection
- 🚫 FORBIDDEN to plan orchestration yet (that's step 3)
- 💬 Present 2-4 workflow options with clear reasoning
- 🚪 User must confirm before proceeding

## YOLO MODE AUTO-SELECTION

**CRITICAL: Check YOLO configuration BEFORE user menu:**

```
IF yolo_level >= 4:
  → Auto-select workflow using MCP search results
  → Pick BEST MATCH from CSV (highest confidence score)
  → Skip user menu entirely
  → Auto-proceed to step-03
  → Log: "YOLO Level {level} - Auto-selected {workflow_name} (confidence: {score}%)"

IF yolo_level >= 3 and < 4:
  → Present options via Party Mode (no user menu)
  → Auto-pick best consensus choice
  → Log decision reasoning
  → Auto-proceed to step-03

IF yolo_level < 3:
  → Show workflow selection with [A/P/C] menu as normal
  → Wait for user confirmation
```

---

## EXECUTION PROTOCOLS:

- 🎯 Load workflow-manifest.csv and match task to workflows
- 💬 Present matched workflows with reasoning from manifest descriptions
- 📖 Update frontmatter stepsCompleted when complete
- 🚫 FORBIDDEN to load next step until selections confirmed (unless YOLO mode >= 3)

**Reference:** See `/data/manifest-integration-guide.md` for CSV lookup patterns and tool selection.

### 2a. Load and Parse Workflow Manifest CSV

Load workflow manifest: `{project-root}/_bmad/_config/workflow-manifest.csv`

Execute bash to parse CSV and match workflows:

```bash
#!/bin/bash
# CSV Integration: Load workflow manifest and parse into memory structures

PROJECT_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
MANIFEST_CSV="${PROJECT_ROOT}/_bmad/_config/workflow-manifest.csv"

# STEP 1: Verify manifest exists
if [ ! -f "$MANIFEST_CSV" ]; then
  echo "❌ ERROR: workflow-manifest.csv not found at $MANIFEST_CSV"
  exit 1
fi

# STEP 2: Create temporary associative arrays for CSV data
declare -A WORKFLOW_NAME
declare -A WORKFLOW_DESC
declare -A WORKFLOW_MODULE
declare -A WORKFLOW_PATH

# STEP 3: Read CSV and populate arrays (skip header line 1)
# CSV Format: name,description,module,path
# Fields are quoted; escaped quotes are """"
line_num=0
while IFS=',' read -r name desc module path; do
  line_num=$((line_num + 1))
  [ $line_num -eq 1 ] && continue  # Skip header

  # Remove surrounding quotes from all fields
  name="${name%\"}" && name="${name#\"}"
  desc="${desc%\"}" && desc="${desc#\"}"
  module="${module%\"}" && module="${module#\"}"
  path="${path%\"}" && path="${path#\"}"

  # Unescape escaped quotes: """" → "
  desc=$(echo "$desc" | sed 's/""/"/g')

  # Store in arrays (workflow name as key)
  WORKFLOW_NAME["$name"]="$name"
  WORKFLOW_DESC["$name"]="$desc"
  WORKFLOW_MODULE["$name"]="$module"
  WORKFLOW_PATH["$name"]="$path"

done < "$MANIFEST_CSV"

echo "✅ Loaded ${#WORKFLOW_NAME[@]} BMAD workflows from manifest"
echo ""
echo "📊 Workflow Distribution by Module:"
for module in core bmm bmb cis tea; do
  count=0
  for name in "${!WORKFLOW_MODULE[@]}"; do
    [ "${WORKFLOW_MODULE[$name]}" = "$module" ] && count=$((count + 1))
  done
  [ $count -gt 0 ] && echo "  • $module: $count workflows"
done
```

**Output:** Three arrays stored in memory:
- `WORKFLOW_NAME[@]` - All 51 workflow names
- `WORKFLOW_DESC[@]` - Description for semantic matching
- `WORKFLOW_MODULE[@]` - Module category (core, bmm, bmb, cis, tea)
- `WORKFLOW_PATH[@]` - Full file path for loading

### 2b. Semantic Matching & Confidence Scoring

For each matched workflow, calculate confidence score:

```bash
#!/bin/bash
# Scoring function: Evaluate workflow relevance to user task

function score_workflow() {
  local workflow_name="$1"
  local task_type="$2"
  local domain="$3"
  local user_keywords="$4"

  local score=0
  local description="${WORKFLOW_DESC[$workflow_name]}"
  local module="${WORKFLOW_MODULE[$workflow_name]}"

  # SCORING CRITERIA:
  # (1) Domain matching (0-30 points)
  case "$module" in
    "bmm")
      if [[ "$domain" =~ (prd|ux|arch|epic|story|implementation|review) ]]; then
        score=$((score + 30))
      fi ;;
    "bmb")
      if [[ "$domain" =~ (agent|workflow|module|builder) ]]; then
        score=$((score + 30))
      fi ;;
    "cis")
      if [[ "$domain" =~ (design|innovation|problem|story|brainstorm) ]]; then
        score=$((score + 30))
      fi ;;
    "tea")
      if [[ "$domain" =~ (test|quality|automation|coverage|atdd) ]]; then
        score=$((score + 30))
      fi ;;
    "core")
      score=$((score + 10))  # Core workflows are baseline relevant
      ;;
  esac

  # (2) Task type matching (0-25 points)
  case "$task_type" in
    "create")  [[ "$description" =~ [Cc]reate ]] && score=$((score + 25)) ;;
    "edit")    [[ "$description" =~ [Ee]dit ]] && score=$((score + 25)) ;;
    "validate")[[ "$description" =~ [Vv]alidate ]] && score=$((score + 25)) ;;
    "update")  [[ "$description" =~ [Uu]pdate ]] && score=$((score + 20)) ;;
    "sync")    [[ "$description" =~ [Ss]ync ]] && score=$((score + 20)) ;;
    "analyze") [[ "$description" =~ [Aa]nalyze ]] && score=$((score + 25)) ;;
  esac

  # (3) Keyword matching (0-30 points - bonus for each match)
  if [ ! -z "$user_keywords" ]; then
    keyword_matches=0
    for keyword in $user_keywords; do
      if [[ "$description" =~ $keyword ]]; then
        keyword_matches=$((keyword_matches + 1))
      fi
    done
    score=$((score + (keyword_matches * 6)))
  fi

  # (4) Description comprehensiveness bonus (0-10 points)
  desc_length=${#description}
  if [ $desc_length -gt 150 ]; then
    score=$((score + 10))
  elif [ $desc_length -gt 100 ]; then
    score=$((score + 5))
  fi

  # Cap score at 100
  [ $score -gt 100 ] && score=100

  echo "$score"
}

# STEP 4: Score ALL workflows
declare -A SCORES
echo "🔍 Scoring workflows against task context..."
echo ""

for workflow_name in "${!WORKFLOW_NAME[@]}"; do
  score=$(score_workflow "$workflow_name" "$TASK_TYPE" "$DOMAIN" "$USER_KEYWORDS")
  SCORES["$workflow_name"]="$score"
done

# STEP 5: Sort workflows by score and display top matches
echo "📊 Top Matched Workflows (Sorted by Confidence):"
echo ""

# Create array of [score name] pairs and sort
declare -a scored_workflows
for name in "${!SCORES[@]}"; do
  scored_workflows+=("${SCORES[$name]} $name")
done

# Sort descending and take top 4
top_matches=$(printf '%s\n' "${scored_workflows[@]}" | sort -rn | head -4)

counter=0
while IFS=' ' read -r score name; do
  counter=$((counter + 1))
  module="${WORKFLOW_MODULE[$name]}"
  desc="${WORKFLOW_DESC[$name]}"
  path="${WORKFLOW_PATH[$name]}"

  printf "%d. [%3d%% confidence] %s (%s)\n" "$counter" "$score" "$name" "$module"
  printf "   Description: %s\n" "$desc"
  printf "   Path: %s\n\n" "$path"
done <<< "$top_matches"

# Save top 4 for presentation
TOP_MATCH_1=$(echo "$top_matches" | sed -n '1p' | cut -d' ' -f2-)
TOP_MATCH_2=$(echo "$top_matches" | sed -n '2p' | cut -d' ' -f2-)
TOP_MATCH_3=$(echo "$top_matches" | sed -n '3p' | cut -d' ' -f2-)
TOP_MATCH_4=$(echo "$top_matches" | sed -n '4p' | cut -d' ' -f2-)

SCORE_1=$(echo "$top_matches" | sed -n '1p' | cut -d' ' -f1)
SCORE_2=$(echo "$top_matches" | sed -n '2p' | cut -d' ' -f1)
SCORE_3=$(echo "$top_matches" | sed -n '3p' | cut -d' ' -f1)
SCORE_4=$(echo "$top_matches" | sed -n '4p' | cut -d' ' -f1)
```

### 2c. Present Matched Workflows to User

**Display formatted workflow options with confidence scoring:**

"**Analyzing your task and matching to BMAD workflow library...**

Your task context:
- **Type:** [create/update/validate/analyze]
- **Domain:** [prd/ux/arch/testing/code/etc.]
- **Keywords:** [identified from your input]

**Scanning 51 workflows across 5 modules...**

**Top Matched Workflows (by confidence):**

**1. ${TOP_MATCH_1}** — ${WORKFLOW_MODULE[$TOP_MATCH_1]} module (${SCORE_1}% confidence)
   - **When to use:** ${WORKFLOW_DESC[$TOP_MATCH_1]}
   - **Why this match:** Highest semantic match to your task type and domain
   - **Path:** ${WORKFLOW_PATH[$TOP_MATCH_1]}

**2. ${TOP_MATCH_2}** — ${WORKFLOW_MODULE[$TOP_MATCH_2]} module (${SCORE_2}% confidence)
   - **When to use:** ${WORKFLOW_DESC[$TOP_MATCH_2]}
   - **Why this match:** Strong alternative approach, different angle
   - **Path:** ${WORKFLOW_PATH[$TOP_MATCH_2]}

**3. ${TOP_MATCH_3}** — ${WORKFLOW_MODULE[$TOP_MATCH_3]} module (${SCORE_3}% confidence)
   - **When to use:** ${WORKFLOW_DESC[$TOP_MATCH_3]}
   - **Why this match:** Complementary workflow for multi-stage tasks
   - **Path:** ${WORKFLOW_PATH[$TOP_MATCH_3]}

**4. [Recommended Multi-Workflow Combo]**
   - **Sequence:** ${TOP_MATCH_1} → ${TOP_MATCH_2} (if needed)
   - **Why:** Sequential cascade for comprehensive coverage
   - **Best for:** Complex multi-step tasks requiring multiple phases

---

**What would you like to do?**
- [1] Use primary workflow
- [2] Use alternative workflow
- [3] Combine multiple workflows
- [S] Search for specific workflow
- [H] Help me choose"

## CONTEXT BOUNDARIES:

- Discovery from Step 1 informs workflow selection
- We know the task and files
- Now we match to BMAD workflows
- Don't plan execution order yet

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Load Workflow Library

Load workflow manifest database: `{project-root}/_bmad/_config/workflow-manifest.csv`

This CSV contains:
- **51 BMAD workflows** organized by module (bmm, bmb, cis, tea, core)
- **Name, description, path** for each workflow
- Use this to match user task to appropriate workflows

**Execute CSV loading and parsing:**

```bash
# Set project root (resolve from current working directory)
PROJECT_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
MANIFEST_CSV="${PROJECT_ROOT}/_bmad/_config/workflow-manifest.csv"

# Verify manifest exists
if [ ! -f "$MANIFEST_CSV" ]; then
  echo "❌ ERROR: workflow-manifest.csv not found at $MANIFEST_CSV"
  exit 1
fi

# Parse CSV: Extract name, description, module, path
# Format: name,description,module,path (quoted with escaped quotes)
# Create associative arrays for lookup

declare -A WORKFLOW_NAME
declare -A WORKFLOW_DESC
declare -A WORKFLOW_MODULE
declare -A WORKFLOW_PATH

# Read CSV and populate arrays (skip header line 1)
while IFS=',' read -r name desc module path; do
  # Remove quotes from all fields
  name="${name%\"}" && name="${name#\"}"
  desc="${desc%\"}" && desc="${desc#\"}"
  module="${module%\"}" && module="${module#\"}"
  path="${path%\"}" && path="${path#\"}"

  # Unescape escaped quotes """"" → "
  desc=$(echo "$desc" | sed 's/""/"/g')

  # Store in arrays (use name as key)
  WORKFLOW_NAME["$name"]="$name"
  WORKFLOW_DESC["$name"]="$desc"
  WORKFLOW_MODULE["$name"]="$module"
  WORKFLOW_PATH["$name"]="$path"
done < <(tail -n +2 "$MANIFEST_CSV")

echo "✅ Loaded ${#WORKFLOW_NAME[@]} BMAD workflows from manifest"

# Optional: Show statistics by module
echo ""
echo "📊 Workflow Distribution:"
for module in core bmm bmb cis tea; do
  count=$(grep "\"$module\"" "$MANIFEST_CSV" | wc -l)
  [ $count -gt 0 ] && echo "  • $module: $count workflows"
done
```

**Save this in memory for matching:**
- Variable `WORKFLOW_NAME` - Array of all workflow names
- Variable `WORKFLOW_DESC` - Array of descriptions for semantic matching
- Variable `WORKFLOW_MODULE` - Array of module categories
- Variable `WORKFLOW_PATH` - Array of file paths

### 2. Analyze Task Against Patterns & Perform Semantic Matching

Based on discovery from Step 1, extract task context and perform semantic matching:

**Extract task context from Step 1 discovery:**

```bash
# Load discovery file from step-01 (if available)
DISCOVERY_FILE="{bmb_creations_output_folder}/workflows/bmad-orchestrator/intermediate/discovery-{sessionId}.md"

# Extract key task attributes
TASK_TYPE="${TASK_TYPE:-unknown}"  # From user input: create/update/sync/analyze/fix
DOMAIN="${DOMAIN:-general}"         # From discovery: prd/ux/arch/testing/coding/etc
FILE_TYPES="${FILE_TYPES:-}"        # File types mentioned by user
USER_KEYWORDS="${USER_KEYWORDS:-}"  # Key phrases from user input

echo "🔍 Task Context:"
echo "  Type: $TASK_TYPE"
echo "  Domain: $DOMAIN"
echo "  Files: $FILE_TYPES"
echo "  Keywords: $USER_KEYWORDS"
```

**Perform semantic matching using keyword scoring:**

```bash
# Function: Score workflow relevance based on task
# Returns: score (0-100) for each workflow
function score_workflow() {
  local workflow_name="$1"
  local description="${WORKFLOW_DESC[$workflow_name]}"
  local module="${WORKFLOW_MODULE[$workflow_name]}"
  local score=0

  # Module matching (25 points max)
  case "$module" in
    "bmm") [[ "$DOMAIN" =~ (prd|ux|arch|epic|story|implementation|review) ]] && score=$((score + 25)) ;;
    "bmb") [[ "$DOMAIN" =~ (agent|workflow|module|builder) ]] && score=$((score + 25)) ;;
    "cis") [[ "$DOMAIN" =~ (design|innovation|problem|story) ]] && score=$((score + 25)) ;;
    "tea") [[ "$DOMAIN" =~ (test|quality|automation|coverage) ]] && score=$((score + 25)) ;;
    "core") score=$((score + 10)) ;; # Core is always somewhat relevant
  esac

  # Task type matching (20 points max)
  case "$TASK_TYPE" in
    "create")  [[ "$description" =~ [Cc]reate ]] && score=$((score + 20)) ;;
    "edit")    [[ "$description" =~ [Ee]dit ]] && score=$((score + 20)) ;;
    "update")  [[ "$description" =~ [Uu]pdate ]] && score=$((score + 15)) ;;
    "validate")[[ "$description" =~ [Vv]alidate ]] && score=$((score + 20)) ;;
    "sync")    [[ "$description" =~ [Ss]ync ]] && score=$((score + 15)) ;;
    "analyze") [[ "$description" =~ [Aa]nalyze ]] && score=$((score + 20)) ;;
  esac

  # Keyword matching (30 points max - bonus for each matching keyword)
  keyword_matches=0
  for keyword in $USER_KEYWORDS; do
    if [[ "$description" =~ $keyword ]]; then
      keyword_matches=$((keyword_matches + 1))
    fi
  done
  score=$((score + (keyword_matches * 5)))
  [ $score -gt 100 ] && score=100

  # Description length bonus (small reward for comprehensive descriptions)
  desc_length=${#description}
  [ $desc_length -gt 150 ] && score=$((score + 5))
  [ $score -gt 100 ] && score=100

  echo "$score"
}

# Score all workflows and rank them
declare -A SCORES

for workflow_name in "${!WORKFLOW_NAME[@]}"; do
  score=$(score_workflow "$workflow_name")
  SCORES["$workflow_name"]="$score"
done

# Sort workflows by score (top 10)
echo ""
echo "📊 Semantic Ranking (Top Matches):"
echo ""

sorted_workflows=($(
  for name in "${!SCORES[@]}"; do
    echo "${SCORES[$name]} $name"
  done | sort -rn | head -10 | cut -d' ' -f2-
))

# Display top matches with details
for i in "${!sorted_workflows[@]}"; do
  idx=$((i + 1))
  name="${sorted_workflows[$i]}"
  score="${SCORES[$name]}"
  module="${WORKFLOW_MODULE[$name]}"
  desc="${WORKFLOW_DESC[$name]}"

  printf "%d. [%3d%% match] %s (%s)\n" "$idx" "$score" "$name" "$module"
  printf "   ↳ %s\n\n" "$desc"
done
```

**Present matched options to user:**

"**Let me analyze your task and match it to BMAD workflow patterns from our library of 51 workflows...**

Your task involves:
- **Type:** $TASK_TYPE (creating/updating/synchronizing/analyzing)
- **Domain:** $DOMAIN (PRD/UX/Architecture/Testing/Implementation/etc.)
- **Context:** $FILE_TYPES

**Scanning workflow library for matches using semantic ranking...**

**Potential workflow matches (ranked by relevance):**"

**Option 1: [Primary Match - Highest Score]**
- **Workflow:** `${sorted_workflows[0]}` (${WORKFLOW_MODULE[${sorted_workflows[0]}]} module)
- **Match Score:** ${SCORES[${sorted_workflows[0]}]}%
- **Description:** ${WORKFLOW_DESC[${sorted_workflows[0]}]}
- **Why:** [Highest semantic match based on task type and domain]
- **Best for:** [When you need primary workflow for this task]

**Option 2: [Alternative 1 - Second Score]**
- **Workflow:** `${sorted_workflows[1]}` (${WORKFLOW_MODULE[${sorted_workflows[1]}]} module)
- **Match Score:** ${SCORES[${sorted_workflows[1]}]}%
- **Description:** ${WORKFLOW_DESC[${sorted_workflows[1]}]}
- **Why:** [Secondary match - good alternative approach]
- **Best for:** [When you want different perspective]

**Option 3: [Alternative 2 - Third Score]**
- **Workflow:** `${sorted_workflows[2]}` (${WORKFLOW_MODULE[${sorted_workflows[2]}]} module)
- **Match Score:** ${SCORES[${sorted_workflows[2]}]}%
- **Description:** ${WORKFLOW_DESC[${sorted_workflows[2]}]}
- **Why:** [Third alternative - different angle]
- **Best for:** [When you want complementary approach]

**Option 4: [Recommended Combo - Multi-Workflow]**
- **Workflows:** `${sorted_workflows[0]}` → `${sorted_workflows[3]}` → (if needed)
- **Why:** [Sequential workflow cascade for comprehensive coverage]
- **Best for:** [Complex multi-step tasks requiring multiple stages]

### 2.6 MCP Search for Best Practices

For each top 4 matched workflow, retrieve best practices using MCP tools in parallel execution:

**RETRIEVE Phase - Execute 4 Concurrent Searches:**

```javascript
// All 4 searches execute in parallel for matched workflows
const mcpSearches = [
  // 1. Claude Flow Memory - Global patterns from all projects
  {
    source: "memory",
    call: mcp__claude-flow__memory_search({
      query: "workflow selection best practices for {task_type} and {domain}",
      limit: 5,
      namespace: "shared-knowledge:best-practices"
    })
  },
  // 2. OctoCode GitHub - Real implementations and patterns
  {
    source: "github",
    call: mcp__octocode__githubSearchCode({
      queries: [{
        mainResearchGoal: "Find {task_type} workflow implementation patterns",
        researchGoal: "Discover best practices for {domain} workflows",
        reasoning: "Learn from successful {task_type} implementations",
        keywordsToSearch: ["{task_type}", "workflow", "{domain}", "best-practice"],
        limit: 3
      }]
    })
  },
  // 3. Brave Web Search - Latest articles and guides
  {
    source: "web",
    call: mcp__brave-search__brave_web_search({
      query: "{task_type} workflow best practices {domain} 2026",
      count: 3
    })
  },
  // 4. Context7 Library Documentation - Framework references
  {
    source: "docs",
    call: mcp__context7__query-docs({
      libraryId: "/orchestration/frameworks",
      query: "{task_type} workflow patterns and best practices for {domain}"
    })
  }
];

// Execute all searches concurrently
const allResults = await Promise.all(mcpSearches.map(s => s.call));
```

**JUDGE Phase - Evaluate All Results:**

```javascript
// Score and filter findings from all 4 sources
const evaluatedResults = [];

allResults.forEach((searchResults, sourceIndex) => {
  const source = mcpSearches[sourceIndex].source;
  const sourceReliability = {
    memory: 0.85,  // HIGH - Curated from successful projects
    github: 0.80,  // HIGH - Real code implementations
    docs: 0.85,    // HIGH - Official framework documentation
    web: 0.60      // MEDIUM - Mix of quality sources
  }[source];

  // Process each result
  searchResults.forEach(result => {
    const evaluation = {
      source: source,
      sourceReliability: sourceReliability,
      relevanceScore: calculateRelevance(result, taskType, domain),  // 0-1.0
      confidenceLevel: getConfidenceLevel(relevanceScore),  // HIGH/MEDIUM/LOW
      finding: result.content,
      reasoning: generateReasoning(result, taskType, domain)
    };

    // Filter: Keep only MEDIUM (>=0.5) or HIGH (>=0.8) confidence
    if (evaluation.confidenceLevel !== 'LOW') {
      evaluatedResults.push(evaluation);
    }
  });
});

// Sort by confidence level + relevance score
evaluatedResults.sort((a, b) => {
  const levelScore = (level) => level === 'HIGH' ? 100 : (level === 'MEDIUM' ? 50 : 0);
  return (levelScore(b.confidenceLevel) + b.relevanceScore * 10) -
         (levelScore(a.confidenceLevel) + a.relevanceScore * 10);
});
```

**Confidence Scoring Logic:**

| Score | Level | Relevance | Action |
|-------|-------|-----------|--------|
| >= 0.8 | HIGH | Best match | Auto-recommend, proceed |
| 0.5-0.8 | MEDIUM | Good match | Present options, ask preference |
| < 0.5 | LOW | Poor match | Filter out or trigger Advanced Elicitation |

**Source Reliability Breakdown:**

| Source | Type | Reliability | Use For |
|--------|------|-------------|---------|
| Claude Flow Memory | MCP | 85% (HIGH) | Patterns from successful projects |
| OctoCode GitHub | MCP | 80% (HIGH) | Real code from top repositories |
| Context7 Docs | MCP | 85% (HIGH) | Official framework documentation |
| Brave Web Search | MCP | 60% (MEDIUM) | Latest articles, requires review |

**CONSILIUM Phase - Convoke Expert Council:**

Present findings based on consensus level:

```javascript
// Calculate consensus across all sources
const decisionFramework = {
  primaryRecommendation: evaluatedResults[0],  // Highest score
  alternatives: evaluatedResults.slice(1, 3),   // Next 2 options
  conflictingViews: findConflicts(evaluatedResults),
  consensusLevel: calculateConsensus(evaluatedResults)  // 0-1.0
};

// Decision logic
if (decisionFramework.consensusLevel >= 0.8) {
  // HIGH confidence consensus
  presentAutomaticRecommendation(decisionFramework.primaryRecommendation);
  suggestProceeding();
} else if (decisionFramework.consensusLevel >= 0.5) {
  // MEDIUM confidence - present alternatives
  presentMultipleOptions(
    decisionFramework.primaryRecommendation,
    decisionFramework.alternatives
  );
  askUserForPreference();
} else {
  // LOW confidence - deeper analysis needed
  triggerAdvancedElicitation();
}
```

**DECISION Phase - Present Consolidated Findings:**

Display to user in this format:

```
**Best Practices Retrieved for Top 4 Matched Workflows:**

✅ **Workflow 1: {workflow_name}** (Confidence: HIGH - 0.87)

Primary Finding:
- Source: Claude Flow Memory (HIGH reliability - 85%)
- Key Practice: {consolidated_best_practice}
- Reasoning: {why_this_matters}
- Recommendation: {specific_action}

Alternative Approaches:
- Source 2: {source} - {alternative_insight} (MEDIUM - 0.72)
- Source 3: {source} - {alternative_insight} (MEDIUM - 0.68)

📊 Consensus Level: {consensus_percentage}% across all sources
🎯 Recommendation: {consolidated_decision}

---

✅ **Workflow 2: {workflow_name}** (Confidence: MEDIUM - 0.71)
[Similar format for remaining top 3 workflows]

---

**Overall Selection Guidance:**
- Recommended: Use Workflow 1 (highest consensus: 87%)
- Alternative: Workflow 2 if different approach needed
- Multi-step: Workflow 1 → Workflow 4 for comprehensive coverage
```

**Error Handling - Graceful Degradation:**

```bash
# If MCP source fails, fall back to next available source
function safe_mcp_search() {
  local primary_source="$1"
  local fallback_source="$2"

  if ! execute_mcp_call "$primary_source"; then
    echo "⚠️ Source ($primary_source) unavailable, falling back to $fallback_source"
    execute_mcp_call "$fallback_source" || {
      echo "❌ All sources unavailable, using local workflow ranking"
      return 1
    }
  fi
}

# Example fallback chain: Memory → GitHub → Docs → Web
safe_mcp_search "memory" "github"
safe_mcp_search "github" "docs"
safe_mcp_search "docs" "web"
```

### 2.7 Store Findings in Global Memory

After MCP search evaluation, persist findings for cross-project reuse:

```bash
# Store consolidated best practices in global memory
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge:best-practices" \
  --key "workflow-selection:{task_type}:{domain}:{date}" \
  --content "$(cat << 'EOF'
## Workflow Selection Best Practices

**Task Type:** {task_type}
**Domain:** {domain}
**Consensus Level:** {consensus_percentage}%
**Timestamp:** {ISO_timestamp}

### Top 4 Matched Workflows & Practices

#### 1. {workflow_name} — PRIMARY MATCH (87% confidence)
- Best Practice: {consolidated_finding}
- Sources: Memory (85%) + GitHub (80%)
- Recommendation: {action}
- Use When: {use_case}

#### 2. {workflow_name} — ALTERNATIVE (71% confidence)
- Best Practice: {consolidated_finding}
- Sources: Docs (85%) + Web (60%)
- Use When: {use_case}

#### 3. {workflow_name} — COMPLEMENTARY (68% confidence)
- Best Practice: {consolidated_finding}
- Use When: {use_case}

#### 4. {workflow_name} — SUPPORTING (62% confidence)
- Best Practice: {consolidated_finding}
- Use When: {use_case}

### Decision Framework

**Consensus Analysis:**
- HIGH consensus (≥80%): Strong agreement across all sources
- MEDIUM consensus (50-79%): Mixed recommendations, alternatives exist
- LOW consensus (<50%): Insufficient data, manual selection recommended

**Source Distribution:**
- Memory (85%): {count} relevant patterns found
- GitHub (80%): {count} implementations found
- Docs (85%): {count} references found
- Web (60%): {count} articles found

### Cost-Benefit Analysis

**Using Recommended Workflow:**
- Token savings: ~20-30% (reusable pattern)
- Quality improvement: +15% (following best practices)
- Risk mitigation: HIGH (proven approach)

**Using Alternative Workflows:**
- Pros: Different perspective, novel approaches
- Cons: Less proven, potentially higher risk

**Multi-Workflow Sequence:**
- Recommended: {workflow_1} → {workflow_2}
- Duration: ~{estimated_hours} hours
- Coverage: {comprehensive_benefit_description}

### Learnings for Future Sessions

- ✅ Pattern successfully identified and ranked
- ✅ Best practice consensus achieved at {consensus_percentage}%
- ✅ Cross-project knowledge reused from {source_count} sources
- ✅ Stored for instant retrieval in future {task_type} + {domain} tasks

**Token Impact:** This analysis saved ~15-25% tokens by reusing patterns from other projects.

EOF
)"

# Verify storage was successful
if npx claude-flow@v3alpha memory retrieve \
  --key "workflow-selection:{task_type}:{domain}:{date}" \
  --namespace "shared-knowledge:best-practices" \
  >/dev/null 2>&1; then
  echo "✅ Findings stored in global memory"
  echo "📦 Future {task_type} tasks will reuse these best practices"
else
  echo "⚠️ Storage failed - findings retained in local session"
fi
```

**Impact for Cross-Project Reuse:**

Next time ANY project works on {task_type} + {domain}:
- ✅ Best practices instantly found (no new MCP searches needed)
- ✅ Consensus level known upfront
- ✅ Recommended workflows pre-ranked
- ✅ Token savings: 15-25% on workflow selection phase

### 3. Wait for User Selection

"**Which workflow(s) would you like to use?**

You can:
- Select one of the options above (1, 2, 3, 4)
- Request workflows from specific category (BMM/BMB/CIS/TEA/Agents)
- Search workflows by keyword
- Combine multiple workflows
- Let me auto-select based on analysis

What would you prefer?"

**Handle responses:**
- IF user selects number: Confirm and document
- IF user wants category: Show workflows from that category
- IF user searches: Find matching workflows
- IF user wants multiple: Note for orchestration planning
- IF auto-select: Use best match and confirm

### 4. Confirm Selections

"**Confirmed selections:**

1. [Workflow name] — for [purpose]
2. [Workflow name] — for [purpose] (if multiple)

**Available for orchestration:** 75+ BMAD workflows

Is this correct? Any adjustments needed?"

### 5. Update Plan Document

Update `{workflowPlanFile}` with workflow selections:

```markdown
## Workflow Selections

**Selected Workflows:**
1. [Workflow name] — [purpose/reasoning]
2. [Workflow name] — [purpose/reasoning] (if multiple)

**Available in Library:** 75+ BMAD workflows

**Auto-Select:** [Yes/No]

**User Preferences:**
[Any specific preferences mentioned]
```

Update frontmatter: `stepsCompleted: ['step-01-discovery', 'step-02-workflow-selection']`

### 6. Create Workflow Selection Intermediate File

Create workflow selection file in `{intermediateFolder}`:

**File:** `workflow-selection-{sessionId}.md`

Use template `{selectionTemplate}` and populate with:
- sessionId: From session
- timestamp: Current date/time
- taskType: Type of task (create/update/sync/analyze)
- complexity: Estimated complexity
- primaryWorkflows: List of selected workflows with reasoning
- supportingWorkflows: Any secondary workflows
- executionOrder: Proposed order (for orchestration planning)

### 7. Transition to Orchestration Planning

"Perfect! We have our workflow(s) selected from the library of 75+ BMAD workflows. Now let's plan the orchestration — determining execution order, parallel zones, and conflict detection."

### 8. Present MENU OPTIONS (YOLO-Aware)

**CONDITIONAL MENU PRESENTATION:**

```
IF yolo_level >= 4:
  → Auto-select best workflow match
  → Update plan: stepsCompleted: ['step-01-discovery', 'step-02-workflow-selection']
  → Load: {nextStepFile}
  → Log: "YOLO Level {level} - Auto-selected {workflow_name}, skipped menu"
  → No approval needed

IF yolo_level >= 3 and < 4:
  → Execute Party Mode (no traditional [A/P/C] menu)
  → Use consensus to select workflow
  → Auto-proceed to step-03
  → Log: "YOLO Level {level} - Party Mode consensus selected {workflow_name}"

IF yolo_level < 3:
  → Display: **Select an Option:** [A] Advanced Elicitation [P] Party Mode [C] Continue
  → ALWAYS halt and wait for user input
```

#### EXECUTION RULES (Manual Mode - yolo_level < 3):

- ALWAYS halt and wait for user input
- ONLY proceed to next step when user selects 'C'
- User can chat or ask questions - always respond and redisplay menu

#### Menu Handling Logic (For Manual Mode):

- IF A: Execute {advancedElicitationTask} for deeper exploration
- IF P: Execute {partyModeWorkflow} for multi-agent discussion
- IF C: Update plan frontmatter, then load `{nextStepFile}`
- IF Any other: Help user, then redisplay menu

#### YOLO Mode Auto-Selection (level >= 3):

- Select workflow with highest confidence score
- Update plan: stepsCompleted: ['step-01-discovery', 'step-02-workflow-selection']
- Load: `{nextStepFile}` (step-03-orchestration-plan.md)
- Log selection reasoning with timestamp

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Appropriate BMAD workflows identified from 75+ library
- User confirmed selections
- Reasoning documented
- Plan updated with selections
- Ready for orchestration planning

### ❌ SYSTEM FAILURE:

- Wrong workflow category selected
- No user confirmation
- Not documenting selections

**Master Rule:** Match task to workflow pattern from 75+ library, confirm with user, then plan orchestration.
