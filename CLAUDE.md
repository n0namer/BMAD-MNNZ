# Claude Code Configuration - Claude Flow V3

## 🚨 AUTONOMY LEVEL 4 - MANDATORY PRE-FLIGHT CHECKS

**CRITICAL: Run these checks BEFORE starting ANY work. NO EXCEPTIONS.**

### FIRST: Check if CLAUDE.md Exists (Project Setup Detection)

**Claude MUST check this FIRST, before everything else.**

**For detailed guidance on WHEN to suggest setup, see:**
👉 `/docs/CLAUDE-SETUP-SUGGESTIONS.md`

This file contains:
- When Claude should suggest setup
- What Claude should say
- Examples of different scenarios
- Decision tree for Claude to follow

```bash
# Check if CLAUDE.md exists in current folder
if [ ! -f "CLAUDE.md" ]; then
  echo "⚠️ CLAUDE.md not found in this project!"
  echo "This project needs setup to enable Autonomy Level 4"
  echo ""
  echo "To setup, run one of these from template project:"
  echo "  Windows: .\scripts\setup-claude-md.ps1 -TargetProject \"$(pwd)\""
  echo "  macOS/Linux: bash scripts/setup-claude-md.sh $(pwd)"
  echo ""
  echo "OR copy manually from: C:\Users\NIKITA\.claude-flow\CLAUDE.md"
  exit 1
fi

echo "✅ CLAUDE.md found - Autonomy Level 4 enabled"
```

**If CLAUDE.md NOT found:**
- ❌ STOP - Do NOT proceed with work
- ❌ SUGGEST setup script
- ❌ Explain what needs to be done

**If CLAUDE.md found:**
- ✅ Continue to system checks below
- ✅ Load all Autonomy Level 4 rules
- ✅ Proceed with work

---

## 📚 Documentation Index

**Core instructions** (this file - optimized for performance):
- Autonomy Level 4 checks & pre-flight
- Pre-session checklist
- Swarm orchestration essentials
- Memory-first workflow basics
- Session end protocol

**Detailed guides** (`.claude-flow/docs/` - comprehensive references):
- [Knowledge Base](KNOWLEDGE-BASE.md) - SuperMemory KB system, 12 categories, auto-population
- [BMAD Workflows](BMAD-WORKFLOWS.md) - Auto-detection, proactive system, step-by-step execution
- [CLI Reference](CLI-REFERENCE.md) - 26 commands, 140+ subcommands, examples
- [Agents Reference](AGENTS-REFERENCE.md) - 60+ agent types, selection guide
- [Hooks Reference](HOOKS-REFERENCE.md) - 17 hooks, 12 workers, auto-KB population
- [Setup Guide](SETUP-GUIDE.md) - System requirements, installation, verification
- [RuVector Setup](RUVECTOR-SETUP.md) - PostgreSQL vector backend configuration
- [Troubleshooting](TROUBLESHOOTING.md) - Common issues and solutions
- [Migration Guide](MIGRATION.md) - V2 to V3 migration
- [Issue #967](ISSUE-967-MCP-CLI.md) - MCP vs CLI storage workaround

**Quick Reference:**
- Check daemon: `npx claude-flow@v3alpha daemon status`
- Search memory: `npx claude-flow@v3alpha memory search -q "pattern"`
- System health: `npx claude-flow@v3alpha doctor --fix`

---

## 🆕 NEW PROJECT ONBOARDING (FIRST TIME SETUP)

**When Claude detects a NEW project with CLAUDE.md (no prior session state), execute this sequence:**

### Step 1: Welcome Message
```
🎉 New Project Detected!
Initializing Autonomy Level 4 for {project_name}...
```

### Step 2: Run Full Pre-Flight Checks
```bash
# 1. Check daemon
npx claude-flow@v3alpha daemon status

# 2. Start daemon if needed
npx claude-flow@v3alpha daemon start

# 3. Enable all workers
npx claude-flow@v3alpha daemon worker enable --all

# 4. Initialize session
npx claude-flow@v3alpha hooks session-start --session-id "session-$(date +%s)"

# 5. Verify memory backend
npx claude-flow@v3alpha memory status

# 6. Verify global namespace
npx claude-flow@v3alpha memory namespace list
```

### Step 3: Verify Global Memory Connection
```bash
# Search for existing patterns from other projects
npx claude-flow@v3alpha memory search -q "shared knowledge"

# Should find patterns from ~/.claude-flow/agentdb-global/
```

### Step 4: Status Report to User
```
✅ Project Setup Complete!

System Status:
- ✓ Daemon running (PID: {pid})
- ✓ Memory connected to ~/.claude-flow/agentdb-global/
- ✓ Global knowledge available ({count} patterns from other projects)
- ✓ Background workers enabled (5/5)
- ✓ All hooks active

Ready for work!
- Autonomy Level 4 active
- Memory-first workflow enabled
- BMAD workflows available
- Cross-project knowledge accessible

Type your task or ask "help" for options.
```

### Step 5: Remember Session State
```bash
# Store that onboarding was done
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "sessions:projects:{project_name}:initialized" \
  --value "{timestamp}"
```

**IMPORTANT:** Only run this sequence ONCE per project on first use. After that, use regular Pre-Session Checklist.

---

### Pre-Session Checklist (AUTOMATIC)

Claude MUST execute this sequence at the start of EVERY session (after CLAUDE.md check):

```bash
# 1. Check daemon status
npx claude-flow@v3alpha daemon status

# 2. If daemon stopped → START IT
npx claude-flow@v3alpha daemon start

# 3. Enable ALL background workers
npx claude-flow@v3alpha daemon worker enable --all

# 4. Verify QUIC sync is enabled (autosync between local & global memory)
npx claude-flow@v3alpha config get memory.quic_sync.enabled

# 5. Verify consolidate worker is running (memory deduplication & HNSW optimization)
npx claude-flow@v3alpha daemon status | grep consolidate

# 6. Initialize session with memory
npx claude-flow@v3alpha hooks session-start --session-id "session-$(date +%s)"

# 7. Verify memory backend and sync status
npx claude-flow@v3alpha memory stats

# 8. Verify global namespace exists
npx claude-flow@v3alpha memory namespace list | grep shared-knowledge
```

**If any check fails → FIX IT before proceeding with user request.**

### 🔄 AutoSync Verification

**QUIC Sync Status:**
- ✅ QUIC sync **enabled**: Auto-replicates memory between local and global (~.claude-flow/agentdb-global/)
- ✅ Latency target: <1ms
- ✅ Port: 4433

**Consolidation Worker:**
- ✅ **consolidate** worker: Runs every 5min (configurable), deduplicates entries, optimizes HNSW index
- ✅ 100% success rate (should always see "100%" in daemon status)
- ✅ Auto-triggered by: post-task hooks, session-end, every 300s

**What AutoSync Does:**
1. ✅ **Local → Global sync**: When you save with CLI, automatically pushed to RuVector
2. ✅ **Deduplication**: consolidate worker removes duplicate patterns
3. ✅ **HNSW optimization**: Rebuilds vector index for faster searches (150x-12,500x speedup)
4. ✅ **Memory cleanup**: Removes expired entries (TTL-based)
5. ✅ **Cross-project access**: All projects immediately see updated patterns

### Health Check Results Interpretation

| Check | Expected | If Failed |
|-------|----------|-----------|
| Daemon | Running | `npx claude-flow@v3alpha daemon start` |
| Workers | 5+ enabled | `npx claude-flow@v3alpha daemon worker enable --all` |
| Memory Backend | hybrid | `npx claude-flow@v3alpha memory backend set hybrid` |
| Global Namespace | exists | `npx claude-flow@v3alpha memory namespace create --global --name shared-knowledge` |
| HNSW Indexing | enabled | Already configured in `~/.claude-flow/config.json` |

### Auto-Fix Protocol

```bash
# Run doctor to auto-fix common issues
npx claude-flow@v3alpha doctor --fix

# Verify all systems operational
npx claude-flow@v3alpha status --watch false
```

---

## 🚨 AUTOMATIC SWARM ORCHESTRATION

**When starting work on complex tasks, Claude Code MUST automatically:**

1. **Initialize the swarm** using MCP tools
2. **Spawn concurrent agents** using Claude Code's Task tool
3. **Coordinate via hooks** and memory

### 🚨 CRITICAL: MCP + Task Tool in SAME Message

**When user says "spawn swarm" or requests complex work, Claude Code MUST in ONE message:**
1. Call MCP tools to initialize coordination
2. **IMMEDIATELY** call Task tool to spawn REAL working agents
3. Both MCP and Task calls must be in the SAME response

**MCP alone does NOT execute work - Task tool agents do the actual work!**

### 🤖 INTELLIGENT 3-TIER MODEL ROUTING (ADR-026)

**The routing system has 3 tiers for optimal cost/performance:**

| Tier | Handler | Latency | Cost | Use Cases |
|------|---------|---------|------|-----------|
| **1** | Agent Booster (WASM) | <1ms | $0 | Simple transforms (var→const, add types, etc.) - **Skip LLM entirely** |
| **2** | Haiku | ~500ms | $0.0002 | Simple tasks, low complexity (<30%) |
| **3** | Sonnet/Opus | 2-5s | $0.003-0.015 | Complex reasoning, architecture, security (>30%) |

**When you see these recommendations:**

1. `[AGENT_BOOSTER_AVAILABLE]` → The task can be handled by Agent Booster (352x faster, $0)
   - Use the Edit tool directly for simple code transforms
   - Intent types: `var-to-const`, `add-types`, `add-error-handling`, `async-await`, `add-logging`, `remove-console`

2. `[TASK_MODEL_RECOMMENDATION] Use model="X"` → Use that model in Task tool:
```javascript
// If hook recommends: [TASK_MODEL_RECOMMENDATION] Use model="opus"
Task({
  prompt: "...",
  subagent_type: "coder",
  model: "opus"  // ← USE THE RECOMMENDED MODEL
})
```

**Model Selection Logic:**
| Complexity | Model | Use For |
|------------|-------|---------|
| Agent Booster intent detected | **Skip LLM** | var→const, add-types, remove-console (352x faster) |
| High (architecture, system design, security) | **opus** | Complex reasoning, multi-step planning |
| Medium (features, refactoring, debugging) | **sonnet** | Balanced capability and speed |
| Low (formatting, simple fixes, docs) | **haiku** | Fast, cost-effective tasks |

**CRITICAL:** Always check for `[AGENT_BOOSTER_AVAILABLE]` or `[TASK_MODEL_RECOMMENDATION]` before spawning agents.

### 🛡️ Anti-Drift Coding Swarm (PREFERRED DEFAULT)

**To prevent goal drift, context drift, and agent desynchronization, ALWAYS use this configuration for coding swarms:**

```javascript
mcp__ruv-swarm__swarm_init({
  topology: "hierarchical",  // Single coordinator enforces alignment
  maxAgents: 8,              // Smaller team = less drift surface
  strategy: "specialized"    // Clear roles reduce ambiguity
})
```

**Why This Prevents Drift:**
| Choice | Anti-Drift Benefit |
|--------|-------------------|
| **hierarchical** | Coordinator validates each output against goal, catches divergence early |
| **maxAgents: 6-8** | Fewer agents = less coordination overhead, easier alignment |
| **specialized** | Clear boundaries - each agent knows exactly what to do, no overlap |

**Consensus for Hive-Mind:** Use `raft` (leader maintains authoritative state)

**Additional Anti-Drift Measures:**
- Frequent checkpoints via `post-task` hooks
- Shared memory namespace for all agents
- Short task cycles with verification gates

---

## 🌍 Global Shared Memory (Глобальная Общая Память)

**CRITICAL: Always maximize memory usage across ALL projects to save 32-50% tokens!**

### ✅ What's Configured

- **Backend**: RuVector (PostgreSQL + HNSW) or Hybrid (SQLite + AgentDB)
- **Location**: `~/.claude-flow/agentdb-global/`
- **Global Namespace**: `shared-knowledge` and `kb:*` (Knowledge Base)
- **Search Speed**: 150x-12,500x faster via HNSW indexing
- **Auto-Save**: All changes via hooks (post-edit, post-task, intelligence)
- **Token Savings**: 32-50% reduction (ReasoningBank -32%, caching -10%, batch -20%)

### 🔧 Memory Access Methods

⚠️ **CRITICAL: MCP and CLI use DIFFERENT storage backends (Issue #967)**

**1. CLI Method** (`npx claude-flow@v3alpha memory ...`) - **RECOMMENDED for Knowledge Base**

- **Storage**: Global RuVector/AgentDB (`~/.claude-flow/agentdb-global/`)
- **Visibility**: ALL projects see the same data
- **Use for**: Knowledge Base operations (kb:\* namespace), cross-project patterns
- **Pros**: Global persistence, HNSW indexing, cross-project access
- **Cons**: npx overhead (~100-200ms)

**2. MCP Tools** (`mcp__claude-flow__memory_*`) - **LOCAL storage only (until PR #989)**

- **Storage**: Local file (`.claude-flow/memory/store.json`)
- **Visibility**: ONLY current project
- **Use for**: Swarm orchestration, task coordination (NOT Knowledge Base)
- **Pros**: Faster (no npx), native integration
- **Cons**: Local only, not shared across projects

**⚠️ DO NOT use MCP memory tools for Knowledge Base until Issue #967 is resolved**

See [Issue #967 details](./.claude-flow/docs/ISSUE-967-MCP-CLI.md) for workaround and timeline.

### 🎯 When to Save Knowledge

**ALWAYS save to global memory when:**
1. **Code patterns discovered** → Architecture, design patterns, best practices
2. **Learnings from tasks** → Success/failure reasons, optimization tips
3. **API/library patterns** → Usage examples, configuration best practices
4. **Domain knowledge** → Business logic, system behavior, requirements
5. **BMAD patterns** → BMM, BMB, GDS, CIS workflows and best practices
6. **Performance tips** → Optimization techniques, bottlenecks, solutions
7. **Security findings** → Vulnerabilities, fixes, security patterns
8. **Cross-project solutions** → Reusable solutions for similar problems

### 📁 Namespace Organization

```
shared-knowledge/
├── architecture:*          # System designs, patterns
├── patterns:*              # Reusable code/workflow patterns
├── bmad:*                  # BMAD best practices (bmm, bmb, gds, cis)
├── performance:*           # Optimization techniques
├── security:*              # Security findings, fixes
├── api-patterns:*          # API usage examples
├── config:*                # Configuration templates
├── learnings:*             # Task-specific learnings
└── solutions:*             # Cross-project solutions
```

### 💾 How to Save Knowledge

**Automatic (via hooks - NO ACTION NEEDED):**
```bash
# After every code edit:
post-edit hook → extracts patterns → saves to shared-knowledge:patterns

# After every task:
post-task hook → captures learnings → saves to shared-knowledge:learnings

# Daily consolidation:
consolidate worker → deduplicates → optimizes storage
```

**Manual save (when special knowledge discovered):**

**Using CLI:**
```bash
# Save architectural decision
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "architecture:project-pattern" \
  --content "Pattern description and code examples"

# Save BMAD best practice
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "bmad:bmm:pattern-name" \
  --content "Best practice explanation"

# Save performance optimization
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "performance:optimization-type" \
  --content "Technique details and metrics"
```

**Using MCP Tools (preferred in Claude Code):**

```javascript
// Save architectural decision
mcp__claude-flow__memory_store({
  key: "shared-knowledge:architecture:project-pattern",
  value: "Pattern description and code examples"
})

// Save BMAD best practice
mcp__claude-flow__memory_store({
  key: "shared-knowledge:bmad:bmm:pattern-name",
  value: "Best practice explanation"
})

// Save performance optimization
mcp__claude-flow__memory_store({
  key: "shared-knowledge:performance:optimization-type",
  value: "Technique details and metrics"
})
```

### 🔍 How to Search & Retrieve Knowledge

**Search across all projects:**

**Using CLI:**
```bash
# Find patterns
npx claude-flow@v3alpha memory search -q "authentication pattern"

# Search BMAD knowledge
npx claude-flow@v3alpha memory search -q "BMAD best practices"

# Search performance tips
npx claude-flow@v3alpha memory search -q "database query optimization"
```

**Using MCP Tools (preferred in Claude Code):**

```javascript
// Find patterns
mcp__claude-flow__memory_search({
  query: "authentication pattern",
  limit: 10
})

// Search BMAD knowledge
mcp__claude-flow__memory_search({
  query: "BMAD best practices",
  limit: 10
})

// Search performance tips
mcp__claude-flow__memory_search({
  query: "database query optimization",
  limit: 10
})

// Retrieve specific pattern
mcp__claude-flow__memory_retrieve({
  key: "shared-knowledge:patterns:auth-jwt"
})
```

**IMPORTANT: Use search BEFORE writing code** → 80% chance of finding reusable pattern

### 📊 Token Savings Breakdown

| Source | Savings | How |
|--------|---------|-----|
| **ReasoningBank retrieval** | -32% | Fetch patterns before reasoning |
| **Agent Booster edits** | -15% | Pre-compute transformations |
| **Pattern caching** | -10% | Reuse instead of regenerating |
| **Optimal batch size** | -20% | Parallel operations via memory hints |
| **Total** | **-50-75%** | Combined effect |

**Example:** With global memory, a 5000-token task → ~2500 tokens (50% savings)

### 🚀 Usage Pattern

**When starting ANY work:**

```
1. SEARCH memory first
   MCP: mcp__claude-flow__memory_search({ query: "[task description]", limit: 10 })
   CLI: npx claude-flow@v3alpha memory search -q "[task description]"

2. If pattern found → REUSE pattern (-32% tokens)

3. If new code written → SAVE to memory
   MCP: mcp__claude-flow__memory_store({ key: "shared-knowledge:...", value: "..." })
   CLI: npx claude-flow@v3alpha memory store --namespace "shared-knowledge" ...

4. Hooks auto-extract patterns post-task
```

### ⚙️ Configuration Files

**Global Memory Config:** `~/.claude-flow/config.json`
```json
{
  "memory": {
    "backend": "hybrid",
    "path": "~/.claude-flow/agentdb-global",
    "vector": {
      "enabled": true,
      "indexing": "hnsw",
      "dimensions": 1536,
      "ef_construction": 200,
      "search_timeout_ms": 100
    },
    "quic_sync": {
      "enabled": true,
      "port": 4433,
      "latency_target_ms": 1
    }
  }
}
```

**Hooks Active:**
- ✅ `post-edit` → Pattern extraction
- ✅ `post-task` → Learning capture
- ✅ `consolidate` → Daily optimization
- ✅ `intelligence` → Neural learning

### 🚨 RULES FOR GLOBAL MEMORY

1. **ALWAYS search before coding** → Reuse existing patterns
2. **ALWAYS tag knowledge properly** → Use namespace prefixes (architecture:, patterns:, bmad:)
3. **STORE complete context** → Include why, how, when, limitations
4. **AVOID duplicates** → Search first, then save
5. **UPDATE patterns** → If you find better version, update in memory

### 📈 Performance Impact

**Measured (from last 26 executions):**
- Token reduction: **32.3%** (target 30-50%)
- Pattern confidence: **85%** (target 80%+)
- Routing accuracy: **87%** (target 85%+)
- Command success: **94%** (target 90%+)
- Search latency: **<100µs** (HNSW working, CLI overhead ~2s)

---

## 🚨 KNOWN ISSUE: MCP vs CLI Storage Separation (Issue #967)

**Problem:** MCP tools and CLI use DIFFERENT backends due to architectural limitation in v3.0.0-alpha.

### 🔴 WHAT NOT TO DO (Common Mistakes)

❌ **WRONG:** Using MCP to save cross-project knowledge
```javascript
// DON'T DO THIS for global memory!
mcp__claude-flow__memory_store({
  key: "shared-knowledge:story-3-1:completion",
  value: "..."  // Saves to LOCAL .claude-flow/memory/store.json only!
})
```

❌ **WRONG:** Expecting CLI saved data in MCP (or vice versa)
```bash
# This saves to GLOBAL memory
npx claude-flow@v3alpha memory store --namespace "shared-knowledge" --key "story-3-1:completion" --value "..."

# But this WON'T find it (different backend!)
mcp__claude-flow__memory_retrieve({ key: "shared-knowledge:story-3-1:completion" })
```

❌ **WRONG:** Mixing storage backends in same workflow
```javascript
// DON'T: Save with MCP, search with CLI
mcp__claude-flow__memory_store({ ... })  // Local
// ... later ...
const results = await bash("npx claude-flow@v3alpha memory search -q '...'")  // Global - different data!
```

### ✅ WHAT TO DO (Correct Approach)

✅ **CORRECT:** Separate by use case
```
MCP memory_* tools    → Task coordination (local, current project only)
CLI memory commands   → Knowledge Base (global, cross-project)
```

✅ **CORRECT:** Save cross-project knowledge with CLI
```bash
# Use CLI for global memory (with HNSW indexing, cross-project access)
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "story-3-1:completion" \
  --value "Story 3-1 Jupyter Notebook Implementation COMPLETED..."
```

✅ **CORRECT:** Use MCP only for orchestration
```javascript
// MCP for swarm coordination (local, fast)
mcp__claude-flow__swarm_init({ topology: "hierarchical" })
mcp__claude-flow__agent_spawn({ agentType: "coder" })

// Task tool for actual work (real agents, real code)
Task({ subagent_type: "coder", prompt: "..." })
```

✅ **CORRECT:** Cross-project pattern retrieval
```bash
# Use CLI to search global memory from ANY project
npx claude-flow@v3alpha memory search -q "jupyter notebook patterns"
# Returns results from ~.claude-flow/agentdb-global/ (all projects!)
```

### 📊 Quick Decision Matrix

| Goal | Tool | Storage | Visibility | Speed |
|------|------|---------|-----------|-------|
| Orchestrate task agents | MCP swarm_init/agent_spawn | - | - | Fast |
| Save code result for other projects | **CLI memory store** | RuVector global | ✅ All projects | 100ms |
| Save code result for THIS project only | MCP memory_store | Local JSON | ❌ Current only | <1ms |
| Search cross-project patterns | **CLI memory search** | RuVector global | ✅ All projects | <100ms |
| Coordinate between parallel agents | MCP memory_store | Local JSON | ❌ Current only | <1ms |

### 🎯 Real-World Scenarios

**SCENARIO 1: Saving implementation pattern for other projects**

**WRONG:**
```javascript
// Pattern from this project saved locally (can't be reused)
mcp__claude-flow__memory_store({
  key: "pattern:jupyter-notebook-structure",
  value: "..."  // Only this project sees it
})
```

**CORRECT:**
```bash
# Pattern saved globally (reusable across all projects)
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "patterns:jupyter-notebook-best-practices" \
  --value "Jupyter notebook pattern: 9-cell structure with markdown headers, error handling, HNSW vector indexing..."
```

**SCENARIO 2: Coordinating parallel task execution**

**CORRECT (MCP for coordination):**
```javascript
// Local coordination between agents - MCP is fine here
mcp__claude-flow__swarm_init({ topology: "hierarchical" })
mcp__claude-flow__agent_spawn({ agentType: "coder" })

// This data doesn't need to be visible in other projects
mcp__claude-flow__memory_store({
  key: "temp:task-coordination:agent-results",
  value: "..."  // Local only - that's OK
})
```

**SCENARIO 3: Archiving completed work for future reference**

**WRONG:**
```javascript
// Valuable knowledge locked in local storage
mcp__claude-flow__memory_store({
  key: "learned:optimization-technique",
  value: "..."  // Can't be found from other projects
})
```

**CORRECT:**
```bash
# Valuable knowledge saved globally
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "performance:optimization-technique" \
  --value "Optimization technique description with metrics and constraints..."
```

**Status:** PR #989 in review (ETA: 2-4 weeks)

📖 **[Full documentation and workaround details →](./.claude-flow/docs/ISSUE-967-MCP-CLI.md)**

---

## 🐘 RuVector Setup & Configuration

**RuVector = PostgreSQL with vector extensions for Claude Flow global memory**

**Benefits:**

- ✅ Global memory accessible from ALL projects
- ✅ HNSW indexing (150x-12,500x faster search)
- ✅ Persistent storage with backups and replication
- ✅ Handles 100K+ entries with <100ms search

**Quick Start:**

```bash
# 1. Start container
docker run -d --name ruvector-central \
  -e POSTGRES_PASSWORD=ruvector_pass \
  -p 5432:5432 ruvnet/ruvector-postgres:latest

# 2. Install driver
cd ~/.claude-flow && npm install pg dotenv

# 3. Initialize schema
npx claude-flow@v3alpha ruvector init --host localhost --port 5432 --database central_vectors --user postgres
```

📖 **[Complete installation, configuration, and troubleshooting guide →](./.claude-flow/docs/RUVECTOR-SETUP.md)**

---

## 🗂️ Knowledge Base (SuperMemory-Style)

**Claude Flow = SuperMemory: Centralized knowledge base with HNSW indexing (150x-12,500x faster)**

**12 KB Categories:** code-patterns, architecture, documentation, research, APIs, workflows, troubleshooting, performance, security, tools, dependencies, learnings

**Quick Commands:**
```bash
npx claude-flow@v3alpha memory search -q "your query"        # Search across all KB
npx claude-flow@v3alpha memory store --namespace "kb:code-patterns" --key "name" --content "..."  # Save
npx claude-flow@v3alpha kb:stats                             # KB statistics
```

**Auto-Populate:** Hooks automatically save 80% of KB entries:
- `post-task` hook → categorizes learnings and solutions
- `post-edit` hook → extracts code patterns and configs
- `consolidate` worker → removes duplicates, optimizes HNSW index

**Token Savings:** Pattern reuse saves -32% tokens on average

📖 **[Complete Knowledge Base guide →](./.claude-flow/docs/KNOWLEDGE-BASE.md)**

---

## 🧠 MEMORY-FIRST WORKFLOW (MANDATORY)

**RULE: ALWAYS search memory BEFORE writing code. Workflow: Search → Find Pattern → Reuse → Execute → Auto-Save via Hooks**

```
1. Search KB first: npx claude-flow@v3alpha memory search -q "[your task]"
2. Pattern found? → Reuse (-32% tokens) | Not found? → Create new work
3. Save automatically: hooks auto-save 80% via post-task + post-edit
4. Available everywhere: Global memory shared across all projects
```

📖 **[Complete Memory-First Workflow guide →](./.claude-flow/docs/KNOWLEDGE-BASE.md)**

---

## 🤖 BMAD WORKFLOWS

**Auto-Detection: Claude proactively suggests BMAD workflows for planning, design, testing, implementation, and retrospectives**

**Common Workflows:**
- Sprint Planning, Product Brief, Architecture Design
- Create PRD, UX Design, Epics & Stories
- Implementation (Dev Story, Quick Dev, Code Review)
- Testing (TestArch Framework, ATDD, CI/CD, Test Design)
- Documentation & Analysis

📖 **[Complete BMAD Workflows guide →](./.claude-flow/docs/BMAD-WORKFLOWS.md)**

**Quick Start:** When Claude detects keywords like "design", "plan", "test", "implement" → suggests appropriate workflow with step-by-step execution

**Suggestion Template (ALWAYS OFFER PROACTIVELY):**
```
💡 **BMAD Recommendation**: {Workflow Name}

I noticed you're working on {detected_task}.
The "{Workflow Name}" workflow can help structure this work.

📋 What's included:
- {N} required steps (~{est_time} total)
- Clear checkpoints between phases
- Structured outputs and validation

[Start workflow] [Not now] [Tell me more]
```

**Rules:**
- Suggest only ONCE per workflow per session
- If user declines → Remember, don't re-suggest that session
- If user explicitly rejects BMAD → Don't suggest more in this session

---

### 2. WORKFLOW EXECUTION PROTOCOL

**When user accepts workflow, execute step-by-step with tracking:**

**STEP 1: Create tracking file**
```markdown
Create: `.bmad/current-workflow.md`

# {Workflow Name}
Started: {timestamp}
Status: IN_PROGRESS
User: {user_message_trigger}

## Progress Tracker
- [ ] 1. {Step Name} [REQUIRED] ~{est_minutes} min
- [ ] 2. {Step Name} [REQUIRED] ~{est_minutes} min
- [ ] 3. {Step Name} [optional] ~{est_minutes} min

Current Step: 1
Completion: 0/{total_required_steps} required steps done
```

**STEP 2: Execute each step with guidance**

For EVERY step, show:
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📍 Step {N}/{total}: {Step Name}
[REQUIRED/optional] ~{est_minutes} min

💡 What to do:
{Instructions from workflow}

📤 Expected output:
- {Output item 1}
- {Output item 2}
- File: {filename if applicable}

Ready?
[✅ Done] [❓ Help] [⏭️ Skip]
```

**STEP 3: Handle user responses**

**IF [✅ Done]:**
- Verify output exists (if file-based)
- Check quality (matches expected output pattern)
- Update tracker: `- [x] N. {name}`
- Auto-advance to next step

**IF [❓ Help]:**
- Provide 2-3 examples specific to user's domain
- Offer to break into micro-steps
- Stay on same step until user marks [✅ Done]

**IF [⏭️ Skip]:**
- Check if marked REQUIRED
  - **If REQUIRED:** Show warning with risk details
    ```
    ⚠️ This is a required step. Risks if skipped:
    - {Risk 1}
    - {Risk 2}

    Skip anyway? [Yes, understand risk] [No, let me do it]
    ```
  - **If user confirms skip:** Mark as `- [⚠️] N. {name} [SKIPPED]`
  - **If optional:** Mark as `- [○] N. {name} [SKIPPED]`

**CRITICAL RULE:** Cannot proceed to Step N+1 until Step N is marked [✅ Done] or explicitly skipped.

---

### 3. VALIDATION & CHECKPOINTS

**Per-step automatic validation:**
```bash
# If workflow specifies expected output file:
if [ ! -f "{expected_file}" ]; then
  echo "⚠️ Expected output not found: {expected_file}"
  echo "Please create/complete this before continuing"
  [Retry validation] [Skip validation]
fi
```

**Phase checkpoints (REQUIRE APPROVAL):**
- ✅ **After Analysis** → User reviews findings and confirms
- ✅ **After Design** → User reviews decisions and approves approach
- ✅ **After Implementation** → User reviews outputs before moving on

**Checkpoint Pattern:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔐 **{Phase} CHECKPOINT**

Before proceeding, please review:
- {Artifact 1}: {location}
- {Artifact 2}: {location}

Ready to continue? [Approved] [Need to fix] [Pause workflow]
```

---

### 4. PAUSE & RESUME

**When user pauses (says "pause", "stop", "continue later", times out):**

Update `.bmad/current-workflow.md`:
```markdown
Status: PAUSED
Paused at: {timestamp}
Current step: {N}
Next: {Step Name}
```

**On next session start:**

If `.bmad/current-workflow.md` exists with Status: PAUSED:
```
ℹ️ **Unfinished workflow detected**

{Workflow Name} - {X}% complete
Paused at: Step {N} ({Step Name})
Last active: {how_long_ago}

[Continue from Step {N}] [Archive and start new] [Ignore]
```

**If user chooses [Continue]:**
- Load workflow state
- Resume at exact step N
- Restore context and progress

---

### 5. COMPLETION & TRACKING

**When all required steps completed:**

```
🎉 **{Workflow Name} COMPLETE!**

📊 Final Summary:
✅ {N} required steps completed
○ {M} optional steps skipped
⏱️  Total time: {actual_duration}
📁 Outputs created: {count}

Quality Score: {rating based on skips}
- 5⭐ All required steps done, no skips
- 4⭐ All required steps done, optional skipped
- 3⭐ 1+ required steps skipped

How was this workflow?
👍 Helpful | 👎 Too rigid | 💬 Feedback: ___
```

**Post-completion automation:**

1. **Log to usage file:**
```bash
# Append to _bmad/_memory/usage-log.md
## {ISO_DATE} - {Workflow Name}
- **Status**: ✅ COMPLETED
- **Duration**: {actual_minutes} min
- **Steps**: {done}/{total_required} required + {optional_done}/{optional_total} optional
- **Quality**: {⭐⭐⭐⭐⭐}
- **User Feedback**: {feedback}
- **Outputs**:
  * {artifact1.md}
  * {artifact2.md}
  * {file3}
```

2. **Archive workflow state:**
```bash
mv .bmad/current-workflow.md \
   .bmad/_archive/{workflow}-{date}-{status}.md
```

3. **Store in global memory:**
```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "bmad:usage:{workflow}:{date}" \
  --content "{workflow summary + outputs + quality rating}"
```

---

### 6. ADAPTIVE LEARNING

**Track patterns to improve over time:**

**Metrics to capture:**
- Workflow completion rate (how many started → completed)
- Where users typically get stuck (step + time spent)
- Which optional steps are always skipped
- Average duration vs. estimated duration
- Quality ratings per workflow

**How Claude adapts:**

- If workflow completed 3+ times successfully → Suggest more proactively
- If workflow abandoned 2+ times → Reduce suggestion frequency
- If specific step always skipped → Auto-mark as commonly optional
- If duration estimate wrong by >50% → Update estimate

**Storage:**
```bash
npx claude-flow@v3alpha memory store \
  --namespace "user-context" \
  --key "bmad:preferences:{workflow}" \
  --content "{completion_rate, stuck_points, duration_actual, quality_trend}"
```

---

### 7. PROACTIVE ASSISTANCE (Stuck Detection)

**If user on one step >5 minutes without progress:**

```
💡 **Stuck on Step {N}?**

I notice you've been on "{Step Name}" for a while.
Can I help?

- 📖 Explain in more detail
- 💡 Show 3 examples specific to your domain
- 🔨 Break this into micro-steps (easier)
- ⏭️ Skip this step (if optional)
- 🔄 Start over with this step
- 💬 Describe what's confusing
```

**Quality validation for quick completions:**

If step usually takes {X} min but completed in {X/5} min:
```
⚠️ **Quality check**

Step {N} usually takes ~{X} minutes.
You finished in {actual_time}.

Quick validation:
- ☐ {Requirement 1}?
- ☐ {Requirement 2}?
- ☐ {Requirement 3}?

All covered? [Yes] [Need to redo]
```

---

### 8. ERROR RECOVERY

**Scenario 1: Workflow file not found**
```
⚠️ **Cannot load workflow**: {path}

Possible causes:
- File moved or deleted
- Path misconfigured
- Workflow directory restructured

Options:
[Retry load] [Choose different workflow] [Manual mode]
```

**Scenario 2: Tracker file corrupted**
```
⚠️ **Progress file corrupted**

Can restore from archive and continue,
or start workflow fresh.

Options:
[Restore from archive] [Start fresh] [Manual mode]
```

**Scenario 3: User confused about workflow purpose**
```
Let me clarify what we're doing:

We're in: {Workflow Name}
Purpose: {Why this workflow helps}
Current: Step {X} of {total}

This step ({Step Name}) is important because:
{Explanation}

Want to:
✅ Continue with guidance
⏸️  Pause (progress saved)
🔄 Start different workflow
❌ Exit without saving
```

---

### 9. INTEGRATION WITH EXISTING BMAD SECTION

**This section EXTENDS lines 402-454 (BMAD AUTO-SELECTION):**

| Component | Purpose | Interaction |
|-----------|---------|-------------|
| Lines 402-454 | Passive auto-selection | User triggers workflow |
| Lines 455+ | Proactive detection | Claude detects keywords and suggests |
| Together | Complete BMAD system | Passive + Active coverage |

**Memory integration:**
- ✅ Uses existing `shared-knowledge:bmad:*` namespace
- ✅ Adds new `user-context:bmad:*` for personalization
- ✅ Extends SESSION END PROTOCOL with BMAD tracking

---

### 🔄 Auto-Start Swarm Protocol

### Pre-Swarm Checklist (MANDATORY)

**BEFORE spawning swarm, ensure:**
1. ✅ Daemon running (`npx claude-flow@v3alpha daemon status`)
2. ✅ Memory searched for existing solution
3. ✅ Session initialized
4. ✅ Background workers enabled

**If any check fails → RUN PRE-FLIGHT CHECKS first**

---

When the user requests a complex task (multi-file changes, feature implementation, refactoring), **immediately execute this pattern in a SINGLE message:**

```javascript
// STEP 1: Initialize swarm coordination via MCP (in parallel with agent spawning)
// USE ANTI-DRIFT CONFIG: hierarchical + specialized + small team
mcp__ruv-swarm__swarm_init({
  topology: "hierarchical",
  maxAgents: 8,
  strategy: "specialized"
})

// STEP 2: Spawn agents concurrently using Claude Code's Task tool
// ALL Task calls MUST be in the SAME message for parallel execution
Task("Coordinator", "You are the swarm coordinator. Initialize session, coordinate other agents via memory. Run: npx claude-flow@v3alpha hooks session-start", "hierarchical-coordinator")
Task("Researcher", "Analyze requirements and existing code patterns. Store findings in memory via hooks.", "researcher")
Task("Architect", "Design implementation approach based on research. Document decisions in memory.", "system-architect")
Task("Coder", "Implement the solution following architect's design. Coordinate via hooks.", "coder")
Task("Tester", "Write tests for the implementation. Report coverage via hooks.", "tester")
Task("Reviewer", "Review code quality and security. Document findings.", "reviewer")

// STEP 3: Batch all todos
TodoWrite({ todos: [
  {content: "Initialize swarm coordination", status: "in_progress", activeForm: "Initializing swarm"},
  {content: "Research and analyze requirements", status: "in_progress", activeForm: "Researching requirements"},
  {content: "Design architecture", status: "pending", activeForm: "Designing architecture"},
  {content: "Implement solution", status: "pending", activeForm: "Implementing solution"},
  {content: "Write tests", status: "pending", activeForm: "Writing tests"},
  {content: "Review and finalize", status: "pending", activeForm: "Reviewing code"}
]})

// STEP 4: Store swarm state in memory
mcp__claude-flow__memory_usage({
  action: "store",
  namespace: "swarm",
  key: "current-session",
  value: JSON.stringify({task: "[user's task]", agents: 6, startedAt: new Date().toISOString()})
})
```

### 📋 Agent Routing (Anti-Drift)

| Code | Task | Agents |
|------|------|--------|
| 1 | Bug Fix | coordinator, researcher, coder, tester |
| 3 | Feature | coordinator, architect, coder, tester, reviewer |
| 5 | Refactor | coordinator, architect, coder, reviewer |
| 7 | Performance | coordinator, perf-engineer, coder |
| 9 | Security | coordinator, security-architect, auditor |
| 11 | Memory | coordinator, memory-specialist, perf-engineer |
| 13 | Docs | researcher, api-docs |

**Codes 1-11: hierarchical/specialized (anti-drift). Code 13: mesh/balanced**

### 🎯 Task Complexity Detection

**AUTO-INVOKE SWARM when task involves:**
- Multiple files (3+)
- New feature implementation
- Refactoring across modules
- API changes with tests
- Security-related changes
- Performance optimization
- Database schema changes

**SKIP SWARM for:**
- Single file edits
- Simple bug fixes (1-2 lines)
- Documentation updates
- Configuration changes
- Quick questions/exploration

## 🚨 CRITICAL: CONCURRENT EXECUTION & FILE MANAGEMENT

**ABSOLUTE RULES**:
1. ALL operations MUST be concurrent/parallel in a single message
2. **NEVER save working files, text/mds and tests to the root folder**
3. ALWAYS organize files in appropriate subdirectories
4. **USE CLAUDE CODE'S TASK TOOL** for spawning agents concurrently, not just MCP

### ⚡ GOLDEN RULE: "1 MESSAGE = ALL RELATED OPERATIONS"

**MANDATORY PATTERNS:**
- **TodoWrite**: ALWAYS batch ALL todos in ONE call (5-10+ todos minimum)
- **Task tool (Claude Code)**: ALWAYS spawn ALL agents in ONE message with full instructions
- **File operations**: ALWAYS batch ALL reads/writes/edits in ONE message
- **Bash commands**: ALWAYS batch ALL terminal operations in ONE message
- **Memory operations**: ALWAYS batch ALL memory store/retrieve in ONE message

### 📁 File Organization Rules

**NEVER save to root folder. Use these directories:**
- `/src` - Source code files
- `/tests` - Test files
- `/docs` - Documentation and markdown files
- `/config` - Configuration files
- `/scripts` - Utility scripts
- `/examples` - Example code

---

## 📋 System Requirements

| Component | Minimum | Recommended | Notes |
|-----------|---------|-------------|-------|
| **Node.js** | v20.0.0 | v20.10+ | Required for Claude Flow CLI |
| **npm** | v9.0.0 | v10.0+ | Package manager |
| **Docker** | v20.10 | v24.0+ | For RuVector (optional) |
| **Git** | v2.30 | v2.40+ | Version control |
| **Memory (RAM)** | 4GB | 8GB+ | Daemon + workers + agents |
| **Disk Space** | 2GB | 10GB+ | Knowledge Base + vectors |
| **OS** | Windows 10, macOS 11, Ubuntu 20.04 | Latest versions | Cross-platform support |

### Optional Components

| Component | Purpose | Installation |
|-----------|---------|-------------|
| **RuVector** | PostgreSQL vector backend | `docker run ruvnet/ruvector-postgres:latest` |
| **PostgreSQL** | Alternative to SQLite | v13.0+ |
| **CUDA** | GPU acceleration (future) | v11.7+ |

### Network Requirements

- **Port 5432**: PostgreSQL/RuVector (if using)
- **Port 3000**: MCP Server (default)
- **Port 4433**: QUIC sync (cross-project memory)
- **Internet**: For CLI downloads, embeddings API (optional)

### Performance Expectations

| Dataset Size | Search Time | Memory Usage | Storage |
|--------------|-------------|--------------|---------|
| <1K entries | <10ms | ~100MB | ~50MB |
| 1K-10K entries | <100ms | ~500MB | ~500MB |
| 10K-100K entries | <500ms | ~2GB | ~5GB |
| >100K entries | <2s | ~4GB+ | ~10GB+ |

📖 **[Troubleshooting guide →](./.claude-flow/docs/TROUBLESHOOTING.md)**

---

## Project Configuration

This project is configured with Claude Flow V3 (Anti-Drift Defaults):
- **Topology**: hierarchical (prevents drift via central coordination)
- **Max Agents**: 8 (smaller team = less drift)
- **Strategy**: specialized (clear roles, no overlap)
- **Consensus**: raft (leader maintains authoritative state)
- **Memory Backend**: hybrid (SQLite + AgentDB)
- **HNSW Indexing**: Enabled (150x-12,500x faster)
- **Neural Learning**: Enabled (SONA)

## 🚀 V3 CLI Commands (26 Commands, 140+ Subcommands)

**Core:** `init`, `agent`, `swarm`, `memory`, `mcp`, `task`, `session`, `config`, `status`, `start`, `workflow`, `hooks`, `hive-mind`

**Advanced:** `daemon`, `neural`, `security`, `performance`, `providers`, `plugins`, `deployment`, `embeddings`, `claims`, `migrate`, `process`, `doctor`, `completions`

**Quick Examples:**
```bash
npx claude-flow@v3alpha doctor --fix           # Health check
npx claude-flow@v3alpha daemon start           # Start daemon
npx claude-flow@v3alpha memory search -q "..."  # Search KB
npx claude-flow@v3alpha kb:save code-patterns "name" "content"  # Save
```

📖 **[Complete CLI Reference →](./.claude-flow/docs/CLI-REFERENCE.md)**

---

## 🚀 Available Agents (60+ Types)

**Core Development:** `coder`, `reviewer`, `tester`, `planner`, `researcher`

**Specialized:** `security-architect`, `backend-dev`, `mobile-dev`, `ml-developer`, `cicd-engineer`, `system-architect`

**Swarm Coordination:** `hierarchical-coordinator`, `mesh-coordinator`, `consensus-builder`, `byzantine-coordinator`, `raft-manager`

**SPARC:** `sparc-coord`, `sparc-coder`, `specification`, `architecture`, `pseudocode`

📖 **[Full Agents Reference (60+ types) →](./.claude-flow/docs/AGENTS-REFERENCE.md)**

## 🪝 V3 Hooks System (17 Hooks + 12 Workers)

**17 Core Hooks:** `pre-edit`, `post-edit`, `pre-task`, `post-task`, `session-start`, `session-end`, `route`, `explain`, `pretrain`, `intelligence`, and more

**12 Background Workers:** `ultralearn`, `optimize`, `consolidate`, `predict`, `audit`, `map`, `preload`, `deepdive`, `document`, `refactor`, `benchmark`, `testgaps`

**Auto-Population:** Hooks save 80% of Knowledge Base automatically:
- `post-task` hook → categorizes learnings and solutions
- `post-edit` hook → extracts code patterns and configs
- `consolidate` worker → removes duplicates every 30 minutes
- `audit` worker → detects security findings

**Quick Commands:**
```bash
npx claude-flow@v3alpha hooks session-start         # Initialize
npx claude-flow@v3alpha hooks post-task --success true  # Record
npx claude-flow@v3alpha hooks worker list           # Check workers
```

📖 **[Complete Hooks Reference →](./.claude-flow/docs/HOOKS-REFERENCE.md)**

---

## 🧠 Intelligence System (RuVector)

V3 includes the RuVector Intelligence System:
- **SONA**: Self-Optimizing Neural Architecture (<0.05ms adaptation)
- **MoE**: Mixture of Experts for specialized routing
- **HNSW**: 150x-12,500x faster pattern search
- **EWC++**: Elastic Weight Consolidation (prevents forgetting)
- **Flash Attention**: 2.49x-7.47x speedup

The 4-step intelligence pipeline:
1. **RETRIEVE** - Fetch relevant patterns via HNSW
2. **JUDGE** - Evaluate with verdicts (success/failure)
3. **DISTILL** - Extract key learnings via LoRA
4. **CONSOLIDATE** - Prevent catastrophic forgetting via EWC++

## 📦 Embeddings Package (v3.0.0-alpha.12)

Features:
- **sql.js**: Cross-platform SQLite persistent cache (WASM, no native compilation)
- **Document chunking**: Configurable overlap and size
- **Normalization**: L2, L1, min-max, z-score
- **Hyperbolic embeddings**: Poincaré ball model for hierarchical data
- **75x faster**: With agentic-flow ONNX integration
- **Neural substrate**: Integration with RuVector

## 🐝 Hive-Mind Consensus

### Topologies
- `hierarchical` - Queen controls workers directly
- `mesh` - Fully connected peer network
- `hierarchical-mesh` - Hybrid (recommended)
- `adaptive` - Dynamic based on load

### Consensus Strategies
- `byzantine` - BFT (tolerates f < n/3 faulty)
- `raft` - Leader-based (tolerates f < n/2)
- `gossip` - Epidemic for eventual consistency
- `crdt` - Conflict-free replicated data types
- `quorum` - Configurable quorum-based

## V3 Performance Targets

| Metric | Target | Status |
|--------|--------|--------|
| HNSW Search | 150x-12,500x faster | **Implemented** (persistent) |
| Memory Reduction | 50-75% with quantization | **Implemented** (3.92x Int8) |
| SONA Integration | Pattern learning | **Implemented** (ReasoningBank) |
| Flash Attention | 2.49x-7.47x speedup | In progress |
| MCP Response | <100ms | Achieved |
| CLI Startup | <500ms | Achieved |
| SONA Adaptation | <0.05ms | In progress |

## 🔧 Environment Variables

```bash
# Configuration
CLAUDE_FLOW_CONFIG=./claude-flow.config.json
CLAUDE_FLOW_LOG_LEVEL=info

# Provider API Keys
ANTHROPIC_API_KEY=sk-ant-...
OPENAI_API_KEY=sk-...
GOOGLE_API_KEY=...

# MCP Server
CLAUDE_FLOW_MCP_PORT=3000
CLAUDE_FLOW_MCP_HOST=localhost
CLAUDE_FLOW_MCP_TRANSPORT=stdio

# Memory
CLAUDE_FLOW_MEMORY_BACKEND=hybrid
CLAUDE_FLOW_MEMORY_PATH=./data/memory
```

## 🔍 Doctor Health Checks

Run `npx claude-flow@v3alpha doctor` to check:
- Node.js version (20+)
- npm version (9+)
- Git installation
- Config file validity
- Daemon status
- Memory database
- API keys
- MCP servers
- Disk space
- TypeScript installation

## 🚀 Quick Setup

```bash
# Add MCP servers
claude mcp add claude-flow npx claude-flow@v3alpha mcp start
claude mcp add ruv-swarm npx ruv-swarm mcp start  # Optional
claude mcp add flow-nexus npx flow-nexus@latest mcp start  # Optional

# Start daemon
npx claude-flow@v3alpha daemon start

# Run doctor
npx claude-flow@v3alpha doctor --fix
```

## 🎯 Claude Code vs MCP Tools

### Claude Code Handles ALL EXECUTION:
- **Task tool**: Spawn and run agents concurrently
- File operations (Read, Write, Edit, MultiEdit, Glob, Grep)
- Code generation and programming
- Bash commands and system operations
- TodoWrite and task management
- Git operations

### MCP Tools ONLY COORDINATE:
- Swarm initialization (topology setup)
- Agent type definitions
- Task orchestration
- Memory management
- Neural features
- Performance tracking

**KEY**: MCP coordinates the strategy, Claude Code's Task tool executes with real agents.

## 📦 Publishing to npm

### 🚨 CRITICAL: ALWAYS PUBLISH BOTH PACKAGES + UPDATE ALL TAGS

**When publishing CLI changes, you MUST:**
1. Publish `@claude-flow/cli`
2. Publish `claude-flow` (umbrella)
3. Update ALL dist-tags for BOTH packages

```bash
# STEP 1: Build and publish CLI
cd v3/@claude-flow/cli
npm version 3.0.0-alpha.XXX --no-git-tag-version
npm run build
npm publish --tag alpha
npm dist-tag add @claude-flow/cli@3.0.0-alpha.XXX latest

# STEP 2: Publish umbrella
cd /workspaces/claude-flow
npm version 3.0.0-alpha.YYY --no-git-tag-version
npm publish --tag v3alpha

# STEP 3: Update ALL umbrella tags (CRITICAL - DON'T SKIP!)
npm dist-tag add claude-flow@3.0.0-alpha.YYY latest
npm dist-tag add claude-flow@3.0.0-alpha.YYY alpha
```

**Verification (MUST DO before telling user):**
```bash
npm view @claude-flow/cli dist-tags --json
npm view claude-flow dist-tags --json
# BOTH packages need: alpha AND latest pointing to newest version
```

### All Tags That Must Be Updated
| Package | Tag | Command Users Run |
|---------|-----|-------------------|
| `@claude-flow/cli` | `alpha` | `npx @claude-flow/cli@alpha` |
| `@claude-flow/cli` | `latest` | `npx @claude-flow/cli@latest` |
| `claude-flow` | `alpha` | `npx claude-flow@alpha` ⚠️ EASY TO FORGET |
| `claude-flow` | `latest` | `npx claude-flow@latest` |
| `claude-flow` | `v3alpha` | `npx claude-flow@v3alpha` |

**The umbrella `alpha` tag is MOST commonly forgotten - users run `npx claude-flow@alpha`!**

## Support

- Documentation: https://github.com/ruvnet/claude-flow
- Issues: https://github.com/ruvnet/claude-flow/issues

---

Remember: **Claude Flow coordinates, Claude Code creates!**

---

## 📊 SESSION END PROTOCOL

**At the end of EVERY session (when user says "done", "thanks", or session ending), Claude MUST:**

```bash
# 1. Export session metrics
npx claude-flow@v3alpha hooks session-end --export-metrics true

# 2. Trigger memory consolidation
npx claude-flow@v3alpha hooks worker dispatch --trigger consolidate

# 3. Store session summary in memory
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "sessions:$(date +%Y%m%d):summary" \
  --content "[tasks completed + patterns learned + artifacts created]"

# 4. Verify all knowledge saved
npx claude-flow@v3alpha memory stats
```

**This ensures:**
- All learnings preserved across sessions
- Memory optimized for next session
- Cross-session knowledge continuity

---

## 🆕 NEW PROJECT SETUP (Quick Start for Other Projects)

**When starting work in a NEW project folder:**

### Option 1: Automatic Setup (Recommended)

**Windows (PowerShell):**
```powershell
# Copy and run from your new project folder
& "C:\Users\NIKITA\.claude-flow\scripts\setup-claude-md.ps1" -TargetProject "."
```

**macOS/Linux (Bash):**
```bash
bash ~/.claude-flow/scripts/setup-claude-md.sh .
```

**What this does:**
1. ✅ Copies CLAUDE.md to your new project
2. ✅ Creates .claude-flow directory
3. ✅ Copies config from global ~/.claude-flow/
4. ✅ Updates .gitignore

### Option 2: Manual Setup

If you prefer manual setup:

```bash
# 1. Copy CLAUDE.md from central storage
cp ~/.claude-flow/CLAUDE.md ./CLAUDE.md

# 2. Create .claude-flow directory
mkdir -p .claude-flow

# 3. Copy global config (optional, uses global ~/.claude-flow/ by default)
cp ~/.claude-flow/config.json .claude-flow/config.json

# 4. Add to .gitignore
echo ".claude-flow" >> .gitignore
```

### Important: Memory is GLOBAL

**Critical:** The memory database is stored in `~/.claude-flow/agentdb-global/`

- ✅ All projects share the SAME global memory
- ✅ No duplication of knowledge
- ✅ Cross-project pattern reuse
- ✅ Consistent 32-50% token savings everywhere

**You do NOT need to copy or initialize memory per project - it's automatic!**

### Verification in New Project

After setup, verify everything works:

```bash
# Should show RUNNING
npx claude-flow@v3alpha daemon status

# Should show ✓ shared-knowledge exists
npx claude-flow@v3alpha memory namespace list

# Should show hybrid backend
npx claude-flow@v3alpha memory status
```

---

# important-instruction-reminders

## 🔧 Setup Scripts (Claude MUST Know These!)

**CRITICAL: Claude must ALWAYS check if CLAUDE.md exists when starting work in a new project.**

### What These Scripts Do:
- `scripts/setup-claude-md.sh` (Linux/macOS) - Auto-setup for Unix systems
- `scripts/setup-claude-md.ps1` (Windows) - Auto-setup for PowerShell

### When Claude MUST Suggest Setup:

**If Claude detects working in a new/unknown project folder:**
1. Check if `CLAUDE.md` exists in current folder
2. If MISSING → **IMMEDIATELY suggest:**
   ```
   ⚠️ This project doesn't have CLAUDE.md configured.
   Run setup script to enable Autonomy Level 4:

   Windows: .\scripts\setup-claude-md.ps1 -TargetProject "."
   macOS/Linux: bash scripts/setup-claude-md.sh .
   ```
3. **DO NOT proceed with work** until setup is complete

### Setup Script Locations:
- **Source scripts:** `/scripts/setup-claude-md.sh` and `setup-claude-md.ps1`
- **Updated to:** Any new project folder
- **Memory:** Always uses global `~/.claude-flow/agentdb-global/` (automatic)

### What Gets Copied:
- ✅ CLAUDE.md (this file) → enables all Autonomy Level 4 features
- ✅ .claude-flow/config.json → local configuration
- ✅ Updates .gitignore → prevents accidental commits

---

## 🚨 Project Detection Logic (For Claude)

**Claude MUST execute this check at session start:**

```
IF current_directory != "pipeline-final-test" THEN
  IF CLAUDE.md not found THEN
    SUGGEST: "Run setup script from template project"
  ELSE
    LOAD: CLAUDE.md configurations
    PROCEED: with Autonomy Level 4 rules
  END
ELSE
  PROCEED: with Autonomy Level 4 rules (template project)
END
```

---

## 🔄 Central Storage Reference

**Master copy location:** `C:\Users\NIKITA\.claude-flow\`

This is the source of truth for:
- CLAUDE.md (latest version) → `C:\Users\NIKITA\.claude-flow\CLAUDE.md`
- Setup scripts → `C:\Users\NIKITA\.claude-flow\scripts\`
- Global memory → `C:\Users\NIKITA\.claude-flow\agentdb-global\`
- Config → `C:\Users\NIKITA\.claude-flow\config.json`

**Backup copy for version control:** `C:\Users\NIKITA\pipeline-final-test\`

**New projects automatically use central storage - no manual sync needed.**

---

# 🚦 PROJECT PRIORITY: CONTINUATION AUTOPILOT ("дальше"/"продолжай")

**Priority Rule:** В этом репозитории, когда пользователь пишет `дальше`, `продолжай`, `continue` **или фразы с тем же смыслом** (например: `поехали дальше`, `продолжи`, `go on`), это означает запуск следующего шага по плану.  
**Precedence:** Это приоритетнее общего роутинга, но НЕ отменяет системные/безопасностные ограничения и явные инструкции пользователя.

## Canonical Plan File
Используй этот файл как источник исполнения:
`d:\Users\NIKITA\Documents\DEV\BMAD-MNNZ\_bmad-output\planning-artifacts\life-os-sync-plan-2026-02-08.md`

## Execution Contract
1. Открой canonical plan file.
2. Найди первый незакрытый пункт в `Priority Autopilot Checklist ([]/[x])`.
3. Выполни ровно этот шаг/команду.
4. Отмечай `[x]` только после сохранения артефактов и прохождения проверок шага.
5. Добавь краткую пометку о завершении (timestamp + ключевые пути артефактов + статус).
6. На следующем `дальше/продолжай` повтори шаг 1.

## Mandatory Validate Loop
Если в плане указана валидация, действуй циклом до `PASS`:
`EDIT -> VALIDATE -> (если NEEDS FIX) EDIT -> VALIDATE` — повторять до успеха.

Do what has been asked; nothing more, nothing less.
NEVER create files unless they're absolutely necessary for achieving your goal.
ALWAYS prefer editing an existing file to creating a new one.
NEVER proactively create documentation files (*.md) or README files. Only create documentation files if explicitly requested by the User.
Never save working files, text/mds and tests to the root folder.
After spawning a swarm, wait, don't continuously check status.
**If working in a project without CLAUDE.md → SUGGEST SETUP SCRIPT FIRST before doing work.**

---

## 🚀 FOR USERS: Setting Up a New Project

**To use this system in a new project:**

### Option 1: Automatic Setup (Recommended)
```powershell
# Windows - from your NEW project folder
C:\Users\NIKITA\.claude-flow\scripts\setup-claude-md.ps1 -TargetProject "."

# Then tell Claude: "This is a new project, set me up"
```

```bash
# macOS/Linux - from your NEW project folder
bash ~/.claude-flow/scripts/setup-claude-md.sh .

# Then tell Claude: "This is a new project, set me up"
```

### Option 2: Manual Copy
```bash
# 1. Copy CLAUDE.md from central storage
cp ~/.claude-flow/CLAUDE.md ./CLAUDE.md

# 2. Create .claude-flow directory
mkdir -p .claude-flow

# 3. Update .gitignore
echo ".claude-flow" >> .gitignore
```

### Step 3: Tell Claude
When you open Claude Code in the new project:

```
Me: "This is a new project. I have CLAUDE.md set up. Initialize everything please."
```

Claude will:
1. ✅ Detect new project
2. ✅ Run full onboarding sequence
3. ✅ Verify all systems
4. ✅ Show status report
5. ✅ Connect to global memory

### What You Get
- ✅ Autonomy Level 4 active
- ✅ Global memory shared with all projects (~/.claude-flow/agentdb-global/)
- ✅ 32-50% token savings from pattern reuse
- ✅ BMAD workflows ready to use
- ✅ Cross-project knowledge available

---

## 🎯 Memory is Global, Not Per-Project

Important:
- **CLAUDE.md**: Copied to each project (enables features)
- **Memory (.claude-flow/agentdb-global/)**: Shared globally (ONE for all projects)
- **Config (.claude-flow/config.json)**: Local override (optional)

Result: All projects instantly have access to patterns learned in other projects.
