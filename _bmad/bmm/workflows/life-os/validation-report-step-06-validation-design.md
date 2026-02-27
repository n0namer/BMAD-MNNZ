# Step 06 - Validation Design Check

## Validation Criticality
- Workflow is a portfolio management/decision system with quality gates and reviews; validation/review steps are appropriate and expected.

## Validation Steps (steps-v)
| File | Loads data/ | Systematic | Auto-proceed | Criteria | Anti-lazy | Status | Issues |
| --- | --- | --- | --- | --- | --- | --- | --- |
| steps-v\step-00-return-to-plan.md | Yes | Yes | Yes | Yes | No | WARN | missing anti-lazy language |
| steps-v\step-01-daily-review.md | Yes | Yes | Yes | Yes | No | WARN | missing anti-lazy language |
| steps-v\step-02-weekly-review.md | Yes | Yes | Yes | Yes | No | WARN | missing anti-lazy language |
| steps-v\step-03-monthly-review.md | Yes | Yes | No | Yes | No | WARN | no explicit auto-proceed language; missing anti-lazy language |
| steps-v\step-04-quarterly-review.md | Yes | Yes | No | Yes | No | WARN | no explicit auto-proceed language; missing anti-lazy language |
| steps-v\step-05-refactoring-summary.md | Yes | Yes | No | Yes | No | WARN | no explicit auto-proceed language; missing anti-lazy language |
| steps-v\step-v-05-retrospective.md | Yes | No | No | Yes | No | WARN | missing systematic check sequence; no explicit auto-proceed language; missing anti-lazy language |
| steps-v\step-v-06-portfolio-view.md | Yes | Yes | No | Yes | No | WARN | no explicit auto-proceed language; missing anti-lazy language |
| steps-v\step-v-07-decision-queue.md | Yes | Yes | No | Yes | No | WARN | no explicit auto-proceed language; missing anti-lazy language |

## Validation Data Files
- data/*.md files found: 167
- Validation steps should reference specific data/ standards where applicable.

## Summary
- Steps checked: 9
- Warnings: 9
- Passes: 0

**Status:** WARN (validation steps present but many lack explicit data/standards references or anti-lazy language)
