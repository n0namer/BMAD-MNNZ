# Template Usage Tracking System

**Version:** 1.0
**Date:** 2026-02-04
**Status:** Active

---

## Overview

The Template Usage Tracking System monitors when Life OS templates are used, filled, and completed. This data helps:

- **Identify popular templates** → Focus improvement efforts
- **Detect unused templates** → Deprecate or simplify
- **Measure template effectiveness** → Optimize based on usage patterns
- **Track cross-project reuse** → Understand template value

---

## Architecture

### Components

1. **template-tracker.js** - Core tracking module
   - Records usage events to global memory
   - Maintains usage summaries per template
   - Provides CLI for stats and reporting

2. **hooks-template-integration.js** - Hook integration
   - Integrates with claude-flow post-edit hook
   - Integrates with claude-flow post-task hook
   - Auto-detects template usage from file operations

3. **Global Memory Storage** - Persistent tracking
   - Namespace: `shared-knowledge`
   - Keys: `template-usage:*` and `template-usage-summary:*`
   - Cross-project visibility

---

## Usage Events

### Event Types

| Event | Trigger | Meaning |
|-------|---------|---------|
| **use** | Template file created from template | User started using template |
| **fill** | Template file modified (still has placeholders) | User is filling out template |
| **complete** | Template file fully filled (<5% placeholders) | Template completed |

### Automatic Tracking (via Hooks)

**Post-Edit Hook:**
```javascript
// Triggered automatically when template files are edited
// Location: ~/.claude-flow/hooks/post-edit.js

const { handlePostEdit } = require('./hooks-template-integration.js');

module.exports = (hookData) => {
  handlePostEdit(hookData);
};
```

**Post-Task Hook:**
```javascript
// Triggered automatically when tasks involving templates complete
// Location: ~/.claude-flow/hooks/post-task.js

const { handlePostTask } = require('./hooks-template-integration.js');

module.exports = (hookData) => {
  handlePostTask(hookData);
};
```

### Manual Tracking (CLI)

```bash
# Track template usage manually
node automation/template-tracker.js --template lean-canvas --action fill

# Track with additional metadata
node automation/template-tracker.js \
  --template daily-review \
  --action complete \
  --metadata '{"domain":"health","project":"fitness-2026"}'
```

---

## Data Storage Format

### Individual Usage Record

Stored in global memory with key: `template-usage:<template-name>:<timestamp>`

```json
{
  "template": "lean-canvas",
  "category": "business",
  "action": "fill",
  "timestamp": "2026-02-04T15:30:00.000Z",
  "domain": "business",
  "project": "startup-xyz"
}
```

### Usage Summary

Stored in global memory with key: `template-usage-summary:<template-name>`

```json
{
  "template": "lean-canvas",
  "total_uses": 12,
  "actions": {
    "use": 5,
    "fill": 4,
    "complete": 3
  },
  "first_used": "2026-01-15T10:00:00.000Z",
  "last_used": "2026-02-04T15:30:00.000Z"
}
```

---

## Reporting & Analytics

### View Usage Statistics

```bash
# Show all template usage stats
node automation/template-tracker.js --stats
```

**Output:**
```
📊 Template Usage Statistics

================================================================================

REVIEWS
--------------------------------------------------------------------------------
  daily-review                                 42 uses  Last: 2/4/2026
  weekly-review                                12 uses  Last: 2/3/2026
  monthly-review                                3 uses  Last: 2/1/2026
  quarterly-review                              1 uses  Last: 1/1/2026

BUSINESS
--------------------------------------------------------------------------------
  lean-canvas                                  15 uses  Last: 2/4/2026
  okrs                                          8 uses  Last: 1/28/2026
  swot                                          5 uses  Last: 1/20/2026
  business-model-canvas                         2 uses  Last: 1/10/2026

================================================================================
Total templates tracked: 24
Total uses: 150
Average uses per template: 6.25
```

### Find Unused Templates

```bash
# List templates that have never been used
node automation/template-tracker.js --list-unused
```

**Output:**
```
📋 Unused Templates

================================================================================

FINANCE
--------------------------------------------------------------------------------
  - monte-carlo
  - real-options
  - kelly-criterion

HEALTH
--------------------------------------------------------------------------------
  - recovery-protocols
  - macros-tracking

================================================================================
Total unused: 5/40 (12.5%)
```

---

## Integration with Memory Hooks

### Hook Installation

**Step 1: Copy integration script**
```bash
cp _bmad/bmm/workflows/life-os/automation/hooks-template-integration.js \
   ~/.claude-flow/hooks/
```

**Step 2: Update post-edit hook**
```bash
# Edit ~/.claude-flow/hooks/post-edit.js
cat >> ~/.claude-flow/hooks/post-edit.js << 'EOF'

// Template usage tracking
const { autoDetectAndTrack } = require('./hooks-template-integration.js');

module.exports = (hookData) => {
  // Existing post-edit logic...

  // Add template tracking
  autoDetectAndTrack('post-edit', hookData);
};
EOF
```

**Step 3: Update post-task hook**
```bash
# Edit ~/.claude-flow/hooks/post-task.js
cat >> ~/.claude-flow/hooks/post-task.js << 'EOF'

// Template usage tracking
const { autoDetectAndTrack } = require('./hooks-template-integration.js');

module.exports = (hookData) => {
  // Existing post-task logic...

  // Add template tracking
  autoDetectAndTrack('post-task', hookData);
};
EOF
```

**Step 4: Verify installation**
```bash
# Test hooks are active
npx claude-flow@v3alpha hooks list | grep template
```

---

## Template Frontmatter Enhancement

### Standard Tracking Metadata

Add to all templates in frontmatter:

```yaml
---
template: lean-canvas
domain: business
tracking:
  enabled: true
  category: business
  auto_complete_threshold: 0.95  # 95% filled = complete
  usage_count: 0  # Auto-incremented by tracker
  last_used: null  # Auto-updated by tracker
---
```

### Completion Detection

**Heuristics:**
1. **Placeholder ratio** < 5% (`{{...}}` patterns remaining)
2. **Content length** > 500 characters (excluding whitespace)
3. **Frontmatter flag** `tracking.auto_complete_threshold` met

---

## Querying Usage Data

### Using CLI Memory Search

```bash
# Find all usage of a specific template
npx claude-flow@v3alpha memory search -q "template-usage:lean-canvas:" --limit 50

# Find all template completions
npx claude-flow@v3alpha memory search -q "action:complete" --limit 20

# Find usage by domain
npx claude-flow@v3alpha memory search -q "domain:business" --limit 30
```

### Using MCP Tools (in Claude Code)

```javascript
// Search for template usage patterns
const usageData = await mcp__claude_flow__memory_search({
  query: "template-usage-summary:",
  limit: 50
});

// Retrieve specific template summary
const summary = await mcp__claude_flow__memory_retrieve({
  key: "shared-knowledge:template-usage-summary:lean-canvas"
});
```

---

## Performance Impact

**Overhead:** ~10-20ms per tracked event (asynchronous, non-blocking)

**Storage:** ~200 bytes per usage record

**Search Performance:** <100ms with HNSW indexing

**Impact on workflows:** Negligible (tracking happens in background hooks)

---

## Analytics Insights

### Usage Patterns to Monitor

1. **Adoption Rate**
   - % of templates used at least once
   - Time from template creation to first use

2. **Completion Rate**
   - % of started templates that are completed
   - Average time from `use` to `complete`

3. **Popularity Trends**
   - Top 10 most-used templates
   - Usage frequency over time

4. **Domain Distribution**
   - Which domains use templates most
   - Template usage by project type

5. **Deprecation Candidates**
   - Templates unused for >90 days
   - Templates with high `use` but low `complete` ratio

### Export for Analysis

```bash
# Export all usage data to JSON
npx claude-flow@v3alpha memory search -q "template-usage:" --limit 1000 > template-usage-export.json

# Analyze with external tools (Python, R, Excel)
python analyze-template-usage.py template-usage-export.json
```

---

## Maintenance

### Cleanup Old Records

```bash
# Delete usage records older than 1 year
npx claude-flow@v3alpha memory delete --namespace "shared-knowledge" --pattern "template-usage:*" --older-than 365d
```

### Reset Usage Stats

```bash
# Clear all usage summaries (start fresh)
npx claude-flow@v3alpha memory delete --namespace "shared-knowledge" --pattern "template-usage-summary:*"
```

---

## Best Practices

1. **Let hooks do the work** - Don't manually track unless necessary
2. **Review stats monthly** - Identify trends and deprecation candidates
3. **Update templates based on data** - Improve high-use templates
4. **Deprecate unused templates** - Reduce clutter and maintenance burden
5. **Share insights** - Store learnings in global memory for cross-project benefit

---

## Future Enhancements

### Planned Features

- [ ] **Template effectiveness scoring** - Completion rate × usage frequency
- [ ] **Auto-deprecation warnings** - Notify when template unused >90 days
- [ ] **A/B testing support** - Track multiple template versions
- [ ] **User feedback integration** - "Was this template helpful?" ratings
- [ ] **Visual dashboard** - Web UI for usage analytics
- [ ] **Template recommendations** - "Users who used X also used Y"

---

## Troubleshooting

### No Usage Data Appearing

**Check:**
1. Hooks installed correctly: `npx claude-flow@v3alpha hooks list`
2. Memory backend accessible: `npx claude-flow@v3alpha memory status`
3. Global namespace exists: `npx claude-flow@v3alpha memory namespace list`

**Fix:**
```bash
# Reinstall hooks
bash _bmad/bmm/workflows/life-os/automation/install-hooks.sh

# Verify memory
npx claude-flow@v3alpha doctor --fix
```

### Duplicate Tracking Events

**Cause:** Hooks firing multiple times for same edit

**Fix:** Add debounce logic to `hooks-template-integration.js`

### Performance Degradation

**Cause:** Too many tracking records (>10,000)

**Fix:** Run cleanup to archive old records

```bash
# Archive records older than 90 days
node automation/template-tracker.js --archive --older-than 90
```

---

## Related Documentation

- [Knowledge Base System](./.claude-flow/docs/KNOWLEDGE-BASE.md)
- [Hooks Reference](./.claude-flow/docs/HOOKS-REFERENCE.md)
- [Memory-First Workflow](./.claude-flow/docs/KNOWLEDGE-BASE.md#memory-first-workflow)
- [Life OS Workflows](./BMAD-WORKFLOWS.md)

---

**Questions or Issues?**
Store feedback in memory: `npx claude-flow@v3alpha memory store --namespace "shared-knowledge" --key "feedback:template-tracking" --content "Your feedback here"`
