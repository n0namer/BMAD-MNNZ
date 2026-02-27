# Step 02 - Frontmatter Validation

Checked frontmatter for all step files in steps-c/e/v/x against frontmatter-standards.md.

| Step File | Status | Unused Vars | Violations |
| --- | --- | --- | --- |
| steps-c\step-00-foundation-check.md | PASS | - | - |
| steps-c\step-00-goals-discovery.md | FAIL | optional, workflowPlanFile | - |
| steps-c\step-00.1-portfolio-intake.md | FAIL | id, title, version, status, category, track, estimated_duration, nextStepFile, requires, outputs | - |
| steps-c\step-00.5-project-stage.md | PASS | - | - |
| steps-c\step-00.6-resource-assessment.md | PASS | - | - |
| steps-c\step-00.7-optimization-intelligence.md | PASS | - | - |
| steps-c\step-01-collect-ideas.md | FAIL | workflowPlanTemplate | - |
| steps-c\step-02-roles-discovery.md | PASS | - | - |
| steps-c\step-03-specialist-match.md | PASS | - | - |
| steps-c\step-04-consilium-lite.md | FAIL | trackType, estimatedTime, specialists, perspectives | - |
| steps-c\step-04-consilium.md | FAIL | advancedElicitationTask | - |
| steps-c\step-04.5-triz-analysis.md | FAIL | mode, type, estimatedTime, nextStepFile, returnToCaller, triggers, automatic, manual, requires, outputs, calledFrom, templates, quick, structured, ariz, dataRef, workflowPlanFile | - |
| steps-c\step-05-scoring.md | FAIL | stageGateMap | - |
| steps-c\step-06-integration.md | PASS | - | - |
| steps-c\step-06.5-portfolio-dashboard.md | FAIL | stepType, estimatedMinutes, trackApplicable, prerequisites, outputs | - |
| steps-c\step-07-calendar-sync.md | PASS | - | - |
| steps-c\step-08-deep-plan.md | FAIL | track_defaults, quick, default_action, recommended_depth, message, standard, default_action, recommended_depth, message, deep, default_action, recommended_depth, message | - |
| steps-c\step-08.5-final-polish.md | FAIL | nextStepFile, requirementsRegistry, glossary | - |
| steps-c\step-08.7-activation-decision.md | FAIL | ideaFile | - |
| steps-c\step-08.8-activation-setup.md | FAIL | nextStepFile | - |
| steps-c\step-08.9-workflow-plan-polish.md | FAIL | nextStepFile, requirementsRegistry, glossary | - |
| steps-c\step-08b-milestone-planning.md | FAIL | stepType, estimatedMinutes, trackApplicable, prerequisites, outputs, capacityRef | - |
| steps-c\step-08c-gantt-generation.md | FAIL | stepType, estimatedMinutes, trackApplicable, prerequisites, outputs | - |
| steps-c\step-09-complete.md | FAIL | nextStepFile | - |
| steps-c\step-09-task-layer.md | FAIL | nextStepFile | - |
| steps-e\step-01-update-project.md | PASS | - | - |
| steps-e\step-02-rescoring.md | PASS | - | - |
| steps-e\step-02-update-resources.md | FAIL | nextStepFile, portfolioFolder | - |
| steps-e\step-02-update-specialist.md | FAIL | nextStepFile, specialistsFolder | - |
| steps-e\step-03-kill-project.md | PASS | - | - |
| steps-e\step-03-update-goals.md | FAIL | nextStepFile, goalsFolder | - |
| steps-e\step-04-deep-plan.md | PASS | - | - |
| steps-v\step-00-return-to-plan.md | PASS | - | - |
| steps-v\step-01-daily-review.md | FAIL | estimatedDuration, isOptional | - |
| steps-v\step-02-weekly-review.md | FAIL | estimatedDuration | - |
| steps-v\step-03-monthly-review.md | FAIL | estimatedDuration, references, protocol, metrics, templates | - |
| steps-v\step-04-quarterly-review.md | FAIL | nextStepFile | - |
| steps-v\step-05-refactoring-summary.md | PASS | - | - |
| steps-v\step-v-05-retrospective.md | PASS | - | - |
| steps-v\step-v-06-portfolio-view.md | FAIL | estimatedDuration | - |
| steps-v\step-v-07-decision-queue.md | FAIL | estimatedDuration | - |
| steps-x\step-x-01-kickoff.md | FAIL | nextStepFile, trackerTemplateFile | - |
| steps-x\step-x-01b-daily-todos.md | FAIL | nextStepFile, workflowPlanFile | - |
| steps-x\step-x-01c-today-view.md | FAIL | estimatedDuration, dataFiles, templates, filters, balancing, calendar | - |
| steps-x\step-x-02-weekly-pulse.md | FAIL | category, duration, frequency, required | - |
| steps-x\step-x-03-milestone-gate.md | FAIL | category, required, estimated_minutes | - |
| steps-x\step-x-04-pivot-or-kill.md | FAIL | category, required, estimated_minutes | - |

## Summary
- Files checked: 47
- Failures: 32
- Passes: 15

## Notes
- This automated check flags unused frontmatter variables and forbidden path patterns. Manual review still needed for semantic correctness.
