# Success Metrics Protocol

## Overview

Success metrics are **project-level KPIs** measured throughout execution, separate from milestone-specific criteria.

## User Explanation Template

```
📊 **Success Metrics (Project-Level)**

These are the key performance indicators (KPIs) that measure overall project success. Unlike milestone criteria (which are binary pass/fail), these metrics track continuous progress.

**Requirements:**
- Must be quantifiable (numbers, percentages, counts)
- Measured regularly (weekly/milestone checkpoints)
- 3-5 metrics total (avoid metric overload)

**Good Examples:**
✅ "80% task completion rate" (measurable)
✅ "Deploy to production within ±20% timeline variance" (quantifiable tolerance)
✅ "Reduce process time from 60min to 15min" (before/after numbers)
✅ "Maintain <5% bug rate across releases" (percentage threshold)

**Bad Examples:**
❌ "Better user experience" (not measurable)
❌ "High quality output" (subjective)
❌ "Fast delivery" (no numbers)
```

## Auto-Suggest Template

```
💡 **Suggested Success Metrics:**

Based on scoring criteria and deep plan:

1. **Timeline Variance:** ±{X}% from target dates
   - {Rationale from deep plan timeline}

2. **Quality Threshold:** {Metric from scoring criteria}
   - {How this was scored}

3. **Resource Efficiency:** {Metric from resource assessment}
   - {Resource constraint from plan}

4. **Impact Measure:** {Primary impact from scoring}
   - {How success is defined}

**Review and customize:**
```

## Per-Metric Confirmation Template

```
📈 **Metric {N}: {Suggested metric name}**

**Suggested Definition:**
{Auto-suggested metric definition with numbers}

**Questions:**
1. Is this metric measurable and realistic? [Y/N]
2. What's the target value/range? [number ± tolerance]
3. How often should this be measured? [Weekly/Milestone/Final]

**Customization:**
If you want to change this metric, provide:
- New metric name
- Measurement method (how to calculate)
- Target value/range
- Measurement frequency
```

## Metric Output Structure

```markdown
### Success Metric {N}: {Name}
**Definition:** {How measured}
**Target:** {Number/percentage ± tolerance}
**Frequency:** {Weekly / At milestones / Final only}
**Current Value:** [TBD - will track during execution]
**Status:** On Track / At Risk / Off Track
```

## Validation Rules

- ✅ Metric must include numbers or percentages
- ✅ Target must have tolerance range (e.g., ±20%)
- ✅ Measurement method must be objective (no subjective judgment)
- ✅ Frequency must be realistic (not "daily" for long projects)

## Execution Rule

**CRITICAL:** All metrics must be confirmed before proceeding.
