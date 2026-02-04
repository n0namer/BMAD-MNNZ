# Life OS v3.0 Deployment Checklist

**Purpose:** Verify all components are properly installed and working.

**Target User:** System administrator or power user setting up Life OS

---

## Pre-Deployment Requirements

### System Requirements
- [ ] Node.js v20.0.0+ installed
- [ ] npm v9.0.0+ installed
- [ ] Git v2.30+ installed
- [ ] 4GB+ RAM available
- [ ] 2GB+ disk space available

### Claude Flow v3 Installation
```bash
# Check Claude Flow installation
npx claude-flow@v3alpha --version

# Should show: 3.0.0-alpha.X or higher
```

- [ ] Claude Flow CLI installed
- [ ] Version 3.0.0-alpha or higher

### Daemon Status
```bash
# Start daemon if not running
npx claude-flow@v3alpha daemon start

# Check status
npx claude-flow@v3alpha daemon status
```

Expected output:
```
+-- Worker Daemon ---+
| Status: ● RUNNING  |
| PID: XXXXX         |
| Workers Enabled: 5 |
+--------------------+
```

- [ ] Daemon running
- [ ] 5+ workers enabled (map, audit, optimize, consolidate, testgaps)

### Memory Backend
```bash
# Check memory backend
npx claude-flow@v3alpha memory status
```

Expected:
- Backend: hybrid or agentdb
- Location: ~/.claude-flow/agentdb-global/
- HNSW Indexing: Enabled

- [ ] Memory backend configured
- [ ] Global memory path exists
- [ ] HNSW indexing enabled

---

## Component Verification

### 1. Workflow Files (9 Create Steps)

**Check all step files exist:**
```bash
ls -la _bmad/bmm/workflows/life-os/steps-c/
```

Expected files:
- [ ] step-01-collect-ideas.md (with Design Thinking section)
- [ ] step-02-roles-discovery.md
- [ ] step-03-specialist-match.md
- [ ] step-04-consilium.md (with Six Hats + Auto-Suggest)
- [ ] step-04.5-triz-analysis.md (optional step)
- [ ] step-05-scoring.md (with domain criteria)
- [ ] step-06-integration.md
- [ ] step-07-calendar-sync.md
- [ ] step-08-deep-plan.md (with Auto-Linking)
- [ ] step-09-complete.md

**Verify modifications:**
```bash
# Check Design Thinking in Step 1
grep -n "Design Thinking" steps-c/step-01-collect-ideas.md

# Check Six Hats in Step 4
grep -n "Six Thinking Hats" steps-c/step-04-consilium.md

# Check [T] TRIZ menu in Steps 4, 5, 8
grep -n "\[T\]" steps-c/step-04-consilium.md
grep -n "\[T\]" steps-c/step-05-scoring.md
grep -n "\[T\]" steps-c/step-08-deep-plan.md
```

- [ ] Design Thinking embedded in Step 1
- [ ] Six Hats in Step 4
- [ ] [T] TRIZ menu in Steps 4, 5, 8
- [ ] Auto-Suggest in Step 4
- [ ] Auto-Linking in Step 8

---

### 2. TRIZ Templates (3 files)

**Check TRIZ templates:**
```bash
ls -la _bmad/bmm/workflows/life-os/templates/
```

Expected:
- [ ] triz-quick.template.md (~150-200 lines)
- [ ] triz-structured.template.md (~400-500 lines)
- [ ] ariz-full.template.md (~2,000+ lines)

**Verify content:**
```bash
# Check TRIZ Quick has 40 principles
grep -c "### Principle" templates/triz-quick.template.md
# Should output: 40

# Check ARIZ has 9 parts
grep -c "## PART" templates/ariz-full.template.md
# Should output: 9
```

- [ ] All 40 TRIZ principles in Quick template
- [ ] All 9 ARIZ parts in Full template
- [ ] Contradiction Matrix in Structured template

---

### 3. Domain Templates (24 files)

**Check Business templates (6):**
```bash
ls -la templates/business/
```
- [ ] okrs.template.md
- [ ] lean-canvas.template.md
- [ ] swot.template.md
- [ ] bmc.template.md
- [ ] vpc.template.md
- [ ] porters-five-forces.template.md

**Check Finance templates (6):**
```bash
ls -la templates/finance/
```
- [ ] npv.template.md
- [ ] dcf.template.md
- [ ] monte-carlo.template.md
- [ ] real-options.template.md
- [ ] capm.template.md
- [ ] kelly-criterion.template.md

**Check Health templates (6):**
```bash
ls -la templates/health/
```
- [ ] health-belief-model.template.md
- [ ] smart-goals.template.md
- [ ] habit-loop.template.md
- [ ] progressive-overload.template.md
- [ ] macros-tracking.template.md
- [ ] recovery-protocols.template.md

**Check Personal Dev templates (6):**
```bash
ls -la templates/personal/
```
- [ ] pomodoro.template.md
- [ ] atomic-habits.template.md
- [ ] eisenhower-matrix.template.md
- [ ] gtd.template.md
- [ ] growth-mindset.template.md
- [ ] deliberate-practice.template.md

**Verify YAML frontmatter:**
```bash
# Check random template has proper frontmatter
head -n 20 templates/business/okrs.template.md
```

Expected structure:
```yaml
---
template: okrs
domain: business
tier: 1
framework: OKRs
...
---
```

- [ ] All 24 domain templates present
- [ ] All have YAML frontmatter
- [ ] All have integration_points defined

---

### 4. Data Files (Infrastructure)

**Check core data files:**
```bash
ls -la data/
```

Required files:
- [ ] domain-framework-integration.md
- [ ] method-rankings.yaml
- [ ] framework-synergy-matrix.csv
- [ ] domain-template-architecture.md
- [ ] roles-base-enhanced.csv
- [ ] auto-suggest-engine.md
- [ ] deep-plan-templates.md (or .part-01.md + .part-02.md)
- [ ] metrics-and-learning-loop.md

**Verify file sizes:**
```bash
# Check key files are not empty
wc -l data/domain-framework-integration.md  # Should be ~1,000+
wc -l data/auto-suggest-engine.md           # Should be ~800+
wc -l data/deep-plan-templates.md           # Should be ~2,000+ (or split parts)
```

- [ ] All infrastructure files present
- [ ] Files have expected line counts (not empty)

---

### 5. TRIZ Quick Reference

**Verify TRIZ patterns file:**
```bash
wc -l data/triz-quick-patterns.md
# Should be ~1,500+ lines (39,000 words)
```

**Check structure:**
```bash
# Check has all sections
grep "^## " data/triz-quick-patterns.md
```

Expected sections:
- [ ] What is TRIZ
- [ ] When to Use in Life OS
- [ ] Types of Contradictions
- [ ] All 40 Inventive Principles
- [ ] Top 10 Most Common Principles
- [ ] Ideal Final Result (IFR)
- [ ] TRIZ Application Protocol
- [ ] Contradiction Matrix
- [ ] Life OS Integration Examples
- [ ] Memory Integration

---

## Functional Testing

### Test 1: End-to-End Simple Project (30 min)

**Run through all 9 steps manually:**

1. **Step 1:** Collect idea
   - [ ] Design Thinking questions appear
   - [ ] Workflow plan initialized

2. **Step 4:** Consilium
   - [ ] Six Hats auto-assigned
   - [ ] Auto-Suggest appears with framework recommendation
   - [ ] Confidence score >70%

3. **Step 5:** Scoring
   - [ ] Domain-specific criteria auto-added
   - [ ] MCDA calculated correctly
   - [ ] Stage Gate logic works (PASS/FAIL)

4. **Step 8:** Deep Plan
   - [ ] Auto-Linking check runs
   - [ ] If multiple frameworks, shows linking suggestions
   - [ ] L1-L6 structure generated

5. **Step 9:** Templates
   - [ ] Selected framework template filled
   - [ ] Auto-populated fields from workflow plan
   - [ ] YAML frontmatter correct

**Expected Time:** 25-35 minutes
**Result:** Complete project plan with 1 framework

### Test 2: TRIZ Integration (15 min)

**Trigger TRIZ:**
1. Create project with contradiction
2. At Step 4, divergence should be >40%
3. Auto-Suggest should recommend TRIZ

**Verify:**
- [ ] [T] menu option appears
- [ ] TRIZ modes selectable (Quick/Structured/Full)
- [ ] Template renders correctly
- [ ] Output saves to workflow plan

### Test 3: Multi-Framework Auto-Linking (20 min)

**Setup:**
1. Create business + finance project
2. Fill Lean Canvas (revenue, costs)
3. Fill NPV (should be at Step 5 or later)

**Verify:**
- [ ] Auto-Linking detects sources
- [ ] Shows preview of links
- [ ] Populates NPV from Lean Canvas
- [ ] Confidence scores reasonable (>80%)

### Test 4: Memory Integration (10 min)

**Verify memory storage:**
```bash
# After completing a project, check memory
npx claude-flow@v3alpha memory search -q "project name"
```

Expected:
- [ ] Project patterns stored
- [ ] Framework usage logged
- [ ] Learnings captured

**Test cross-project access:**
1. Complete project in folder A
2. Start new project in folder B
3. Search should find patterns from A

- [ ] Global memory works across projects
- [ ] Search latency <100ms (HNSW)

---

## Performance Benchmarks

### Memory Search Speed
```bash
# Benchmark memory search
time npx claude-flow@v3alpha memory search -q "test query"
```

Expected: <2 seconds total (CLI overhead ~1.8s, search <100ms)

- [ ] Search completes in <2 seconds

### HNSW Index Verification
```bash
# Check HNSW index stats
npx claude-flow@v3alpha memory stats
```

Expected output includes:
- Total entries: X
- HNSW indexed: Yes
- Search speedup: 150x-12,500x

- [ ] HNSW indexing active
- [ ] Search speedup verified

### Worker Performance
```bash
# Check worker success rates
npx claude-flow@v3alpha daemon status
```

All workers should show:
- Success: 100%
- Last Run: Recent (not "never")

- [ ] All workers 100% success
- [ ] Workers running regularly

---

## Integration Tests

**Run automated test suite:**
```bash
# If integration tests implemented as scripts
life-os test --suite all
```

**Or manual verification:**
1. Open `data/integration-tests.md` (if exists)
2. Execute Test Suite 1 (End-to-End)
3. Execute Test Suite 2 (Framework Integration)
4. Execute Test Suite 4 (TRIZ Integration)

Expected: All tests PASS

- [ ] Test Suite 1: PASS (End-to-End)
- [ ] Test Suite 2: PASS (Framework Integration)
- [ ] Test Suite 3: PASS (Six Hats)
- [ ] Test Suite 4: PASS (TRIZ)

---

## Documentation Verification

### User-Facing Docs

- [ ] workflow.md complete and readable
- [ ] workflow-plan.template.md functional
- [ ] All step files have clear instructions
- [ ] Templates have usage examples

### Technical Docs

- [ ] auto-suggest-engine.md complete
- [ ] deep-plan-templates.md complete
- [ ] domain-framework-integration.md complete
- [ ] metrics-and-learning-loop.md complete

### Templates

- [ ] All templates have usage instructions
- [ ] All have YAML frontmatter
- [ ] All have integration points documented

---

## Rollback Plan (If Issues Found)

### Backup Current State
```bash
# Before deployment, backup originals
cp -r _bmad/bmm/workflows/life-os/ _bmad/bmm/workflows/life-os.backup/
```

### Restore from Backup
```bash
# If issues found
rm -rf _bmad/bmm/workflows/life-os/
cp -r _bmad/bmm/workflows/life-os.backup/ _bmad/bmm/workflows/life-os/
```

### Partial Rollback

**Revert specific features:**
1. Remove Auto-Suggest: Edit step-04-consilium.md, remove Auto-Suggest Engine section
2. Remove Auto-Linking: Edit step-08-deep-plan.md, remove Auto-Linking section
3. Disable TRIZ: Remove [T] from menus in steps 4, 5, 8

---

## Sign-Off Checklist

**Before marking deployment complete:**

### Core Functionality
- [ ] All 9 workflow steps work end-to-end
- [ ] Design Thinking embedded (Step 1)
- [ ] Six Hats auto-assign (Step 4)
- [ ] TRIZ accessible (Steps 4, 5, 8)
- [ ] Auto-Suggest triggers correctly
- [ ] Auto-Linking works with >80% confidence

### Templates
- [ ] All 30 frameworks available (3 TRIZ + 24 domain + 3 project)
- [ ] Templates render correctly
- [ ] YAML frontmatter valid

### Infrastructure
- [ ] Claude Flow daemon running
- [ ] Memory backend operational
- [ ] HNSW indexing active
- [ ] Workers at 100% success

### Documentation
- [ ] User guide complete
- [ ] Examples work as documented
- [ ] Technical docs accurate

### Performance
- [ ] Memory search <100ms (HNSW portion)
- [ ] No errors in daemon logs
- [ ] Token savings verified (>30%)

---

## Post-Deployment

### Monitoring (First 7 Days)

**Daily checks:**
```bash
# Check daemon health
npx claude-flow@v3alpha daemon status

# Check memory size
du -sh ~/.claude-flow/agentdb-global/

# Check for errors
tail -n 50 ~/.claude-flow/daemon.log
```

### User Feedback Collection

**After first 5 users:**
- Framework suggestions accurate? (target >85%)
- Auto-linking helpful? (target >90%)
- Time savings realized? (target 30%+)

### Metrics to Track

- Auto-Suggest acceptance rate
- Auto-Linking confidence scores
- Framework usage distribution
- Average project completion time
- Token savings per project

---

## Troubleshooting Common Issues

### Issue: Auto-Suggest not triggering
**Fix:** Check domain keywords in workflow plan, verify memory search works

### Issue: Auto-Linking shows 0 links
**Fix:** Need 2+ frameworks present, verify workflow plan populated

### Issue: TRIZ menu not appearing
**Fix:** Check Steps 4, 5, 8 have `[T]` in menu text

### Issue: Memory search slow (>2s)
**Fix:** Check HNSW indexing enabled, run `consolidate` worker

### Issue: Templates not rendering
**Fix:** Check YAML frontmatter syntax, verify file paths

### Issue: Daemon not starting
**Fix:** Check Node.js version, check port 3000 not in use, verify config.json

### Issue: Six Hats not auto-assigning
**Fix:** Check roles-base-enhanced.csv exists, verify Step 2 completed

---

## Verification Commands Quick Reference

```bash
# System health check
npx claude-flow@v3alpha doctor --fix

# Memory status
npx claude-flow@v3alpha memory status

# Daemon status
npx claude-flow@v3alpha daemon status

# Worker status
npx claude-flow@v3alpha daemon worker list

# Search test
npx claude-flow@v3alpha memory search -q "test"

# Config check
npx claude-flow@v3alpha config list

# Session test
npx claude-flow@v3alpha hooks session-start --session-id "test-$(date +%s)"
```

---

## Success Criteria Summary

**Deployment is successful when:**
1. All 9 workflow steps execute without errors
2. All 30 templates are accessible and render correctly
3. Auto-Suggest provides framework recommendations with >70% confidence
4. Auto-Linking connects 2+ frameworks with >80% confidence
5. TRIZ integration works in all 3 modes
6. Memory search completes in <2 seconds
7. Daemon runs with 100% worker success
8. No critical errors in logs
9. Documentation is complete and accurate
10. At least 1 end-to-end test passes successfully

---

**Deployment Version:** 1.0
**Last Updated:** 2026-02-04
**Estimated Deployment Time:** 2-3 hours (including testing)
**Sign-Off Required:** System Administrator + Power User

---

**✅ DEPLOYMENT COMPLETE** when all checkboxes checked.

## Appendix A: File Inventory

### Workflow Steps (9 files)
```
steps-c/step-01-collect-ideas.md
steps-c/step-02-roles-discovery.md
steps-c/step-03-specialist-match.md
steps-c/step-04-consilium.md
steps-c/step-04.5-triz-analysis.md
steps-c/step-05-scoring.md
steps-c/step-06-integration.md
steps-c/step-07-calendar-sync.md
steps-c/step-08-deep-plan.md
steps-c/step-09-complete.md
```

### Templates (30 files)
```
templates/triz-quick.template.md
templates/triz-structured.template.md
templates/ariz-full.template.md
templates/project-plan.template.md
templates/project-journal.template.md
templates/project-snapshot.template.md
templates/project-decisions.template.md
templates/business/*.template.md (6 files)
templates/finance/*.template.md (6 files)
templates/health/*.template.md (6 files)
templates/personal/*.template.md (6 files)
templates/project/*.template.md (4 files)
```

### Data Files (15+ files)
```
data/domain-framework-integration.md
data/method-rankings.yaml
data/framework-synergy-matrix.csv
data/domain-template-architecture.md
data/roles-base-enhanced.csv
data/roles-base.csv
data/auto-suggest-engine.md
data/deep-plan-templates.md (or .part-01.md + .part-02.md)
data/triz-quick-patterns.md
data/metrics-and-learning-loop.md
data/search-decision-protocol.md
data/template-integration-guide.md
data/bmad-workflow-mapping.md
data/integration-patterns.md
data/portfolio-health.md
data/stage-gate-mapping.part-*.md
data/strategic-buckets.md
data/timeline-allocation.md
data/wip-enforcement.md
```

### Main Workflow Files (3 files)
```
workflow.md
workflow-plan.md
workflow-plan.template.md
```

---

## Appendix B: Expected Directory Structure

```
_bmad/bmm/workflows/life-os/
├── workflow.md
├── workflow-plan.md
├── workflow-plan.template.md
├── DEPLOYMENT-CHECKLIST.md (this file)
├── steps-c/
│   ├── step-01-collect-ideas.md
│   ├── step-02-roles-discovery.md
│   ├── step-03-specialist-match.md
│   ├── step-04-consilium.md
│   ├── step-04.5-triz-analysis.md
│   ├── step-05-scoring.md
│   ├── step-06-integration.md
│   ├── step-07-calendar-sync.md
│   ├── step-08-deep-plan.md
│   └── step-09-complete.md
├── steps-e/
│   ├── step-01-update-project.md
│   ├── step-02-rescoring.md
│   ├── step-03-kill-project.md
│   └── step-04-deep-plan.md
├── steps-v/
│   ├── step-00-return-to-plan.md
│   ├── step-01-daily-review.md
│   ├── step-02-weekly-review.md
│   └── step-03-monthly-review.md
├── templates/
│   ├── triz-quick.template.md
│   ├── triz-structured.template.md
│   ├── ariz-full.template.md
│   ├── project-plan.template.md
│   ├── project-journal.template.md
│   ├── project-snapshot.template.md
│   ├── project-decisions.template.md
│   ├── business/
│   │   ├── okrs.template.md
│   │   ├── lean-canvas.template.md
│   │   ├── swot.template.md
│   │   ├── bmc.template.md
│   │   ├── vpc.template.md
│   │   └── porters-five-forces.template.md
│   ├── finance/
│   │   ├── npv.template.md
│   │   ├── dcf.template.md
│   │   ├── monte-carlo.template.md
│   │   ├── real-options.template.md
│   │   ├── capm.template.md
│   │   └── kelly-criterion.template.md
│   ├── health/
│   │   ├── health-belief-model.template.md
│   │   ├── smart-goals.template.md
│   │   ├── habit-loop.template.md
│   │   ├── progressive-overload.template.md
│   │   ├── macros-tracking.template.md
│   │   └── recovery-protocols.template.md
│   └── personal/
│       ├── pomodoro.template.md
│       ├── atomic-habits.template.md
│       ├── eisenhower-matrix.template.md
│       ├── gtd.template.md
│       ├── growth-mindset.template.md
│       └── deliberate-practice.template.md
└── data/
    ├── domain-framework-integration.md
    ├── method-rankings.yaml
    ├── framework-synergy-matrix.csv
    ├── domain-template-architecture.md
    ├── roles-base-enhanced.csv
    ├── roles-base.csv
    ├── auto-suggest-engine.md
    ├── deep-plan-templates.md
    ├── deep-plan-templates.part-01.md
    ├── deep-plan-templates.part-02.md
    ├── triz-quick-patterns.md
    ├── metrics-and-learning-loop.md
    └── [other data files...]
```

---

**End of Deployment Checklist**
