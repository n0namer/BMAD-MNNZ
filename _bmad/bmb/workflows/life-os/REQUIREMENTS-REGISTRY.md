# Requirements Registry

## Overview
This registry lists regulatory, portfolio, PDCA and IDEAL hooks that Life OS workflows depend on. Whenever a step references equirementsRegistry, it should patch this file with:
- Requirement title
- Status (Pending / In-Progress / Complete)
- Link to evidence artifact (plan, decision log, metrics)
- Assigned role and follow-up owner

## Sample Entries
1. **Portfolio Capacity Guardrails** — ensures no more than 3 active projects; evidence stored in data/wip-enforcement.md and portfolio-wip-management.md.
2. **IDEAL Consilium Traceability** — log of MCDA/triz outcomes tied to step-04-consilium.md and the consilium plan.
3. **Validation Coverage** — ensures daily, weekly, monthly and quarterly checks run; evidence captured under steps-v/ and alidation-report-....

## Maintenance
- Update this file each time a new requirement is validated or changes.
- Coordinate with decision logs (decision-log.md) to preserve causality.
