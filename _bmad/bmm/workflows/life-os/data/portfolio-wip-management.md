# Portfolio WIP Management

## WIP Limit Enforcement

### Visual WIP Status

- 🟢 **WIP: 0-2/3** (healthy capacity)
- 🟡 **WIP: 2/3** (approaching limit)
- 🔴 **WIP: 3/3 FULL** (must defer/kill before adding)

### WIP Decision Framework

When WIP limit is exceeded (>3 projects):

#### Option 1: Kill a Project
**Use when:**
- Project no longer aligns with goals
- ROI is significantly lower than expected
- Resources better used elsewhere

**Process:**
1. Review all active projects by priority/alignment
2. Identify lowest-value project
3. Document kill decision and rationale
4. Archive project artifacts
5. Free up capacity

#### Option 2: Defer a Project
**Use when:**
- Project valuable but not time-sensitive
- Dependencies not yet ready
- Capacity temporarily constrained

**Process:**
1. Select project to defer
2. Document pause point and context
3. Set review/restart date
4. Free up capacity
5. Add to deferred backlog

#### Option 3: Override (Add Despite Limit)
**Use when:**
- New project is critical/urgent
- Short duration (<2 weeks)
- Minimal resource overlap

**Process:**
1. Document override rationale
2. Set clear end date for override period
3. Plan WIP reduction after completion
4. Monitor capacity closely

### WIP Check Command

```bash
# Check current WIP status
npx claude-flow@v3alpha memory search -q "project status:active"

# Count active projects
npx claude-flow@v3alpha memory search -q "wip:active" | wc -l
```

## Portfolio Health Commands

```bash
# View portfolio allocation
npx claude-flow@v3alpha memory search -q "portfolio:allocation"

# Check bucket balance
npx claude-flow@v3alpha memory search -q "strategic-bucket:*"

# Review capacity commitments
npx claude-flow@v3alpha memory search -q "timeline:capacity"
```

## Rebalancing Strategies

### When Core Business > 60%
- Defer low-priority core work
- Increase innovation investment
- Build infrastructure debt backlog

### When Innovation > 40%
- Consolidate experiments
- Kill low-signal experiments
- Focus on proven opportunities

### When Infrastructure < 10%
- Schedule tech debt sprint
- Identify critical enablers
- Plan platform upgrades

### When Operations > 25%
- Automate repetitive tasks
- Consolidate maintenance windows
- Review operational efficiency
