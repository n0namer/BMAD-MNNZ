---
projectId: idea-004
title: "Бот для ВК (аналог Salebot)"
status: PLANNED
startDate: 2026-03-01
endDate: 2026-06-30
mvpDate: 2026-04-30
capacityPerWeek: 10-12 hours
bucket: Growth / Innovation
score: 3.90/5.00
---

# Бот для ВК (аналог Salebot)

## Overview
Self-hosted + privacy-first альтернатива Salebot для автоматизации коммуникации ВКонтакте. Serverless архитектура, visual flow builder, template marketplace.

## Timeline

**Phase 1: MVP (Mar-Apr 2026)**
- **2026-03-01** - Kickoff: Infrastructure setup, ВК API research
- **2026-03-15** - Week 2: Webhook system + basic flow engine prototype
- **2026-04-01** - Month 1: Visual flow builder MVP (5 templates)
- **2026-04-15** - Week 6: Beta testing (10-20 users)
- **2026-04-30** - Phase 1 Complete: MVP ready (100 beta signups target)

**Phase 2: Beta (May 2026)**
- **2026-05-31** - Drag-and-drop UI + 3 CRM integrations + analytics

**Phase 3: Launch (Jun 2026)**
- **2026-06-30** - Marketplace + white-label + Product Hunt launch

## Capacity
- Phase 1 (MVP): 10-12 hours/week
- Phase 2 (Beta): 8-10 hours/week
- Phase 3 (Launch): 12-15 hours/week
- Total: 200-300 hours over 4 months

## Key Success Metrics
- 100 beta users by 2026-04-30
- 1000 users by 2026-12-31
- $10K MRR by 2027-02-28
- "10 minutes to first bot" UX achieved

## Dependencies
- ВК API (external, stable)
- AWS Lambda / Cloud Functions
- CRM integration APIs (Phase 2)

## Risks & Mitigations
- Risk: API ВК changes → Mitigation: API monitoring + fallback mechanisms
- Risk: Rate limits (20 req/sec) → Mitigation: Queue system from day 1
- Risk: Unit-economics → Mitigation: Serverless (target <5K₽/month for 1000 users)
- Risk: GDPR compliance → Mitigation: Consultant in Phase 2

## Notes
- WIP conditional: verify portfolio WIP <3 before start date
- BMAD Workflow (BMB-002) to be started after Deep Plan
- Focus: self-hosted + privacy-first positioning vs Salebot
