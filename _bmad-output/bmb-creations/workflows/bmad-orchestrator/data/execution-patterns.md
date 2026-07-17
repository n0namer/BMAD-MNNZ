# Execution Patterns

## Parallel Zone Execution Pattern

### Setup
```
"**Executing Parallel Zone [N]**

Workflows in this zone:
{{#workflows}}
- {{name}}{{/workflows}}

These workflows have no conflicts and can run simultaneously."
```

### Execution via Subagents
```
"Launching parallel execution...

{{#workflows}}
▶️ Starting: {{name}}
  Input: {{input}}
  Expected Output: {{output}}

{{/workflows}}

**Subagent Results:**
{{#results}}
- {{workflow}}: {{status}} ({{duration}})
{{/results}}"
```

### Result Aggregation
```
"**Parallel Zone [N] Complete**

Results:
{{#results}}
✅ {{workflow}}: {{result}}
  Output: {{output}}
{{/results}}

{{#failures}}
❌ {{workflow}}: {{error}}
  Recovery: {{recoveryAction}}
{{/failures}}"
```

## Sequential Phase Execution Pattern

### Single Workflow Execution
```
"**Executing Phase [N]: {{phaseName}}**

Workflow: {{workflowName}}
Type: Sequential (depends on previous)

**Inputs:**
{{#inputs}}
- {{file}}
{{/inputs}}

**Starting execution...**"
```

### Progress Reporting
```
"**Phase [N] Progress**

⏳ {{workflowName}} in progress...
Current step: {{currentStep}}
Estimated: {{estimatedRemaining}}"
```

### Completion
```
"**✅ Phase [N] Complete: {{phaseName}}**

Workflow: {{workflowName}}
Duration: {{duration}}
Status: Success

**Outputs:**
{{#outputs}}
- {{file}} ({{lines}} lines)
{{/outputs}}"
```

## Checkpoint Pattern

### Checkpoint Creation
```
"**📍 CHECKPOINT: Phase {{phase}} Complete**

Saving state...
- Workflows completed: {{completedCount}}
- Files modified: {{modifiedCount}}
- Context usage: {{tokensUsed}}/{{tokenLimit}}

**Options:**
[C] Continue to next phase
[P] Pause orchestration
[A] Advanced Elicitation on results
[S] Save and exit (resume later)

Select: [C/P/A/S]"
```

### State Save
```yaml
checkpoint_data:
  phase: {{phaseNumber}}
  timestamp: "{{timestamp}}"
  completed_workflows: {{completedWorkflows}}
  pending_workflows: {{pendingWorkflows}}
  modified_files: {{modifiedFiles}}
  context_usage: {{tokenUsage}}
  session_file: "intermediate/checkpoint-phase-{{phase}}.md"
```

## Large File Handling Pattern

### Detection
```
"**Large File Detected**

File: {{filename}}
Size: {{lines}} lines ({{sizeKB}} KB)
Threshold: {{threshold}} lines

**Strategy:** Range Read Mode
- Will read only relevant sections
- Context window: {{windowSize}} lines
- Sections to process: {{sectionCount}}"
```

### Range Read Execution
```
"**Processing Section {{current}}/{{total}}**

File: {{filename}}
Lines: {{startLine}} - {{endLine}}
Section: {{sectionName}}

Reading... ✓
Processing... ✓
Updating... ✓"
```

### Progress Tracking
```
"**Large File Processing Progress**

{{filename}}:
{{#sections}}
[{{status}}] {{sectionName}} (lines {{start}}-{{end}})
{{/sections}}

Overall: {{percent}}% complete"
```

## Failure Handling Pattern

### Failure Detection
```
"**⚠️ WORKFLOW FAILURE**

Workflow: {{workflowName}}
Phase: {{phaseNumber}}
Error: {{errorMessage}}

**Failure Analysis:**
- Type: {{failureType}}
- Recoverable: {{isRecoverable}}
- Impact: {{impactScope}}"
```

### Recovery Options
```
"**Recovery Options:**

[R] Retry workflow
[S] Skip workflow and continue
[A] Abort orchestration
[M] Manual intervention
[D] Debug with Advanced Elicitation

Select: [R/S/A/M/D]"
```

### Retry with Backoff
```
"**Retry Attempt {{attempt}}/{{maxAttempts}}**

Workflow: {{workflowName}}
Wait time: {{backoffSeconds}}s

Retrying..."
```

## Pause and Resume Pattern

### Pause
```
"**⏸️ ORCHESTRATION PAUSED**

Current Phase: {{phaseNumber}}
Workflow: {{workflowName}}
Progress: {{percent}}%

**Session saved to:**
{{sessionFile}}

**To resume later:**
1. Run: bmad-orchestrator
2. Select: Continue Existing Session
3. Session ID: {{sessionId}}"
```

### Resume
```
"**▶️ RESUMING ORCHESTRATION**

Session: {{sessionId}}
Restored from: {{checkpointFile}}

**State restored:**
- Phase: {{phaseNumber}}
- Completed: {{completedWorkflows}}
- Pending: {{pendingWorkflows}}

**Continuing from Phase {{nextPhase}}...**"
```

## Context Management Pattern

### Warning Threshold
```
"**⚠️ Context Usage Warning**

Current: {{currentTokens}} tokens ({{percent}}%)
Threshold: {{warningThreshold}} tokens
Limit: {{maxTokens}} tokens

**Recommendations:**
- Checkpoint now recommended
- Consider range read for large files
- Next phase may require subagents"
```

### Critical Threshold
```
"**🛑 CRITICAL: Context Limit Approaching**

Current: {{currentTokens}} tokens ({{percent}}%)
CRITICAL: {{criticalThreshold}} tokens

**Automatic actions:**
- Forcing checkpoint save
- Switching to range read mode
- Will use subagents for parallel work"
```

## Subagent Result Collection

### Parallel Result Aggregation
```
"**Collecting Subagent Results**

{{#subagents}}
Subagent {{id}} ({{workflow}}):
- Status: {{status}}
- Duration: {{duration}}
- Output files: {{files}}
{{/subagents}}

**Aggregating... ✓**
**Validating... ✓**
**Checkpointing... ✓**"
```

### Result Validation
```
"**Validating Subagent Outputs**

{{#results}}
{{workflow}}:
- Expected: {{expectedOutput}}
- Actual: {{actualOutput}}
- Valid: {{isValid}}
{{/results}}

{{#invalid}}
⚠️ {{workflow}}: Output validation failed
  Expected: {{expected}}
  Got: {{actual}}
{{/invalid}}"
```

## Execution Summary Pattern

### Phase Summary
```
"**Phase {{number}} Execution Summary**

Workflows: {{workflowCount}}
Duration: {{duration}}
Success Rate: {{successRate}}%

| Workflow | Status | Duration | Output |
|----------|--------|----------|--------|
{{#workflows}}
| {{name}} | {{status}} | {{duration}} | {{output}} |
{{/workflows}}"
```

### Final Summary
```
"**🎉 EXECUTION COMPLETE**

**Statistics:**
- Total Phases: {{totalPhases}}
- Total Workflows: {{totalWorkflows}}
- Successful: {{successfulCount}}
- Failed: {{failedCount}}
- Skipped: {{skippedCount}}
- Total Duration: {{totalDuration}}

**Files Created/Modified:**
{{#files}}
- {{path}} ({{action}})
{{/files}}

**Next: Cascade Synchronization**"
```
