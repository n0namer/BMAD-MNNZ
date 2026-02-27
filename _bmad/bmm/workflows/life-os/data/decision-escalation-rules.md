# Decision Escalation Rules

## Capacity Escalation

### No Slots Available (available_slots == 0)
**Warning:**
```
⚠️  No capacity available for activation.

Current: {current_active}/{max_capacity} projects active

Options:
1. Complete an existing project first
2. Kill an existing project to free capacity
3. Increase max_capacity (not recommended)
4. Continue anyway (portfolio will be over capacity)

Proceed? [1/2/3/4/Cancel]
```

**Recommendation:** Option 1 (complete project) or Option 2 (kill low-value project)

### Tight Capacity (available_slots == 1)
**Warning:**
```
⚠️  Only 1 capacity slot remaining.

Activating this idea will bring portfolio to max capacity.

Continue? [Y/N]
```

## Dependency Escalation

### Dependencies Not Met
**Warning:**
```
⚠️  Dependency not complete: {dep_id} ({dep_name})

Current status: {dep_status}
Estimated completion: {dep_completion_date}

Options:
1. Wait until dependency completes
2. Remove dependency and continue
3. Continue anyway (risk of rework)

Proceed? [1/2/3/Cancel]
```

**Recommendation:** Option 1 (wait) if dependency close to completion, otherwise Option 2

## Risk Escalation

### High Risk Activation
**Warning:**
```
⚠️  This is a HIGH RISK idea:
- {risk_factor_1}
- {risk_factor_2}
- {risk_factor_3}

Recommendation: WAIT or RECONSIDER

Continue with activation? [Y/N]
```

### Low Readiness Activation
**Warning:**
```
⚠️  Activation readiness is only {readiness}% (below 70% threshold)

Missing:
- {missing_factor_1}
- {missing_factor_2}

Recommendation: Complete planning before activation

Continue anyway? [Y/N]
```

## Strategic Misalignment Escalation

### Low Strategic Alignment
**Warning:**
```
⚠️  This idea has LOW strategic alignment.

Does not strongly support any current portfolio goals.

Consider:
1. Reconsider if this aligns with your priorities
2. Update portfolio goals if this is strategic
3. Kill this idea if no longer relevant

Continue with activation? [Y/N]
```

## Portfolio Balance Escalation

### Balance Warning
**Warning:**
```
⚠️  Portfolio balance may be affected:

Current: {current_balance}
After activation: {projected_balance}

Example: "60% business ideas, 40% technical ideas"
→ After: "75% business ideas, 25% technical ideas"

This may indicate over-focus on one area.

Continue? [Y/N]
```

## Duplicate/Overlap Detection

### Similar Idea Detected
**Warning:**
```
⚠️  Similar idea already in progress: {similar_id} ({similar_name})

Overlap detected:
- {overlap_factor_1}
- {overlap_factor_2}

Consider:
1. Wait until {similar_id} completes
2. Merge ideas into single project
3. Differentiate scope and continue

Proceed? [1/2/3/Cancel]
```

## Confirmation Template

**For ALL escalations requiring user decision:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️  {ESCALATION_TITLE}

{escalation_details}

{IF options_available:}
Options:
{options_list}

{IF recommendation_exists:}
💡 Recommendation: {recommendation}

Continue? [{options_keys}/Cancel]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Decision Recording

**After escalation resolved:**
```bash
# Store escalation decision in memory
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "decisions:escalation:{idea_id}:{escalation_type}:{date}" \
  --content "{escalation_type, user_choice, reasoning, override_reason if applicable}"
```

## Escalation Thresholds

| Condition | Threshold | Action |
|-----------|-----------|--------|
| Capacity | available_slots == 0 | BLOCK + offer options |
| Dependencies | Any dependency not met | WARN + allow override |
| Risk | risk_level == HIGH | WARN + allow override |
| Readiness | activation_readiness < 70% | WARN + allow override |
| Strategic alignment | strategic_alignment == LOW | WARN + suggest reconsider |
| Portfolio balance | deviation > 20% from target | INFO + allow continue |
