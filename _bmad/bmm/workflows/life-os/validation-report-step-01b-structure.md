# Step 01b - Structure Validation

## Folder Structure
- workflow.md: present
- steps-c/, steps-e/, steps-v/, steps-x/: present
- data/, templates/, docs/, output/, automation/: present
- workflow-plan.md: present
- Additional artifacts/archives present (validation reports, remediation docs, archives)

## Step File Size Check
_Limits: <200 OK, 200-300 WARN, >300 EXCEEDS_

| Step File | Lines | Status |
| --- | ---: | --- |
| steps-c\step-00-foundation-check.md | 298 | WARN |
| steps-c\step-00-goals-discovery.md | 427 | EXCEEDS |
| steps-c\step-00.1-portfolio-intake.md | 193 | OK |
| steps-c\step-00.5-project-stage.md | 363 | EXCEEDS |
| steps-c\step-00.6-resource-assessment.md | 292 | WARN |
| steps-c\step-00.7-optimization-intelligence.md | 381 | EXCEEDS |
| steps-c\step-01-collect-ideas.md | 303 | EXCEEDS |
| steps-c\step-02-roles-discovery.md | 235 | WARN |
| steps-c\step-03-specialist-match.md | 212 | WARN |
| steps-c\step-04-consilium-lite.md | 171 | OK |
| steps-c\step-04-consilium.md | 335 | EXCEEDS |
| steps-c\step-04.5-triz-analysis.md | 264 | WARN |
| steps-c\step-05-scoring.md | 452 | EXCEEDS |
| steps-c\step-06-integration.md | 140 | OK |
| steps-c\step-06.5-portfolio-dashboard.md | 284 | WARN |
| steps-c\step-07-calendar-sync.md | 235 | WARN |
| steps-c\step-08-deep-plan.md | 216 | WARN |
| steps-c\step-08.5-final-polish.md | 233 | WARN |
| steps-c\step-08.7-activation-decision.md | 239 | WARN |
| steps-c\step-08.8-activation-setup.md | 297 | WARN |
| steps-c\step-08.9-workflow-plan-polish.md | 271 | WARN |
| steps-c\step-08b-milestone-planning.md | 315 | EXCEEDS |
| steps-c\step-08c-gantt-generation.md | 278 | WARN |
| steps-c\step-09-complete.md | 173 | OK |
| steps-c\step-09-task-layer.md | 211 | WARN |
| steps-e\step-01-update-project.md | 141 | OK |
| steps-e\step-02-rescoring.md | 130 | OK |
| steps-e\step-02-update-resources.md | 233 | WARN |
| steps-e\step-02-update-specialist.md | 217 | WARN |
| steps-e\step-03-kill-project.md | 122 | OK |
| steps-e\step-03-update-goals.md | 283 | WARN |
| steps-e\step-04-deep-plan.md | 145 | OK |
| steps-v\step-00-return-to-plan.md | 122 | OK |
| steps-v\step-01-daily-review.md | 194 | OK |
| steps-v\step-02-weekly-review.md | 188 | OK |
| steps-v\step-03-monthly-review.md | 276 | WARN |
| steps-v\step-04-quarterly-review.md | 269 | WARN |
| steps-v\step-05-refactoring-summary.md | 123 | OK |
| steps-v\step-v-05-retrospective.md | 213 | WARN |
| steps-v\step-v-06-portfolio-view.md | 328 | EXCEEDS |
| steps-v\step-v-07-decision-queue.md | 186 | OK |
| steps-x\step-x-01-kickoff.md | 145 | OK |
| steps-x\step-x-01b-daily-todos.md | 273 | WARN |
| steps-x\step-x-01c-today-view.md | 247 | WARN |
| steps-x\step-x-02-weekly-pulse.md | 203 | WARN |
| steps-x\step-x-03-milestone-gate.md | 219 | WARN |
| steps-x\step-x-04-pivot-or-kill.md | 231 | WARN |

## Findings
- Many step files exceed the 300-line absolute maximum; these should be split or moved to /data/ references.
- Multiple step files are in the 200-300 warning range; consider sharding reference blocks into /data/.
- Folder organization is coherent, but contains many extra artifacts (reports/archives) in root; consider moving all reports into _archive/ or docs/ for clarity.

## Plan vs Files
- workflow-plan.md lists a simplified create flow (step-01..step-09) and validate flow (return-to-plan, daily/weekly/monthly).
- All planned steps exist as files.
- Additional foundation steps (step-00.*) and advanced steps (08b/08c/08.7/08.8/08.9, steps-x) exist beyond plan; plan should be updated to reflect these if they are required in current workflow.

## Status
**Result:** WARN (size violations + plan drift)
