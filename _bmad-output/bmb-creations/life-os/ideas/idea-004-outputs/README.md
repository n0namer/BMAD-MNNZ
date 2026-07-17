# Idea 004: Бот для ВК (аналог Salebot) - Life OS Outputs

**Processed:** 2026-02-05
**Status:** READY FOR EXECUTION
**Life OS Steps:** 2-8 COMPLETE

## Summary

Self-hosted + privacy-first альтернатива Salebot для автоматизации коммуникации ВКонтакте.

**Score:** 3.90 / 5.00 (78%)
**Timeline:** 2026-03-01 to 2026-06-30 (4 months)
**Capacity:** 200-300 hours total

## Key Decisions

1. **Positioning:** Self-hosted + privacy-first + API-first (vs Salebot cloud-only)
2. **Architecture:** Serverless (AWS Lambda), multi-tenant + self-hosted hybrid
3. **UX Target:** "10 minutes to first bot", drag-and-drop like Figma
4. **Go-to-Market:** Product Hunt + ВК dev community + digital agencies

## Files in This Folder

- **idea-004-business-vk-bot.md** - Original captured idea (Step 1)
- **workflow-plan-idea-004.md** - Complete workflow plan (Steps 2-8)
- **idea-004-vk-bot.md** - Project file with timeline & milestones
- **snapshot.md** - Current project snapshot & status
- **journal.md** - Decision journal & progress log
- **plan.md** - Detailed project plan with L1-L6 Deep Plan
- **decisions.md** - Complete decision log

## Specialists Consulted (Consilium)

- Product Strategist (high) - Positioning & roadmap
- Market Analyst (medium) - Competitive analysis (Salebot, Senler, MessageBot)
- Operations Lead (medium) - Infrastructure & CI/CD
- Creative Director (medium) - UX visual flow builder
- Backend Architect (high) - API integration & webhook system

## Six Thinking Hats Applied

- ⚪ White (Facts): Salebot 15K users, 990₽/мес, рынок 500K+ сообществ ВК
- 🔴 Red (Intuition): "Как в Figma" drag-and-drop критично
- ⚫ Black (Risks): API changes, rate limits, unit-economics, GDPR
- 🟡 Yellow (Benefits): Self-hosted, API-first, white-label B2B2C, marketplace
- 🟢 Green (Creativity): Serverless, AI-подсказки, template marketplace
- 🔵 Blue (Process): 3 phases (MVP → Beta → Launch), KPI: $10K MRR за 12 мес

## Scoring Breakdown

- **Impact:** 4/5 - Потенциал 25-50K пользователей, $10K MRR
- **Confidence:** 3/5 - API ВК известен, UX uncertainty
- **Effort:** 3/5 - 200-300 часов
- **Strategic Alignment:** 4/5 - Развитие навыков, portfolio SaaS
- **Risk:** 3/5 - API changes, competition, unit-economics
- **Market Opportunity:** 4/5 - Рынок существует, pain confirmed
- **Competitive Advantage:** 4/5 - Self-hosted unique, white-label

## Milestones

1. **2026-03-01** - Kickoff: Infrastructure, ВК API research
2. **2026-03-15** - Webhook system + flow engine prototype
3. **2026-04-01** - Visual flow builder MVP (5 templates)
4. **2026-04-15** - Beta testing (10-20 users)
5. **2026-04-30** - Phase 1 Complete: 100 beta signups target
6. **2026-05-31** - Phase 2: Drag-and-drop UI + CRM integrations
7. **2026-06-30** - Phase 3 Launch: Marketplace + Product Hunt

## Next Actions

1. Verify portfolio WIP <3 before 2026-03-01 start date
2. Complete BMAD Workflow (BMB-002) for detailed product roadmap
3. Infrastructure setup: AWS Lambda, ВК API credentials, database
4. Recruit 5-10 early beta testers from ВК dev community
5. Begin L4 execution: Research Salebot features & pricing

## Risk Mitigation Plan

- **API monitoring** + fallback mechanisms (If-Then Action #1)
- **Rate limiting** + queue system (BullMQ) from day 1 (If-Then Action #2)
- **Unit-economics validation** in MVP: target <5K₽/month per 1000 users (If-Then Action #3)
- **GDPR consultant** in Phase 2 for compliance
- **"10 min to first bot" UX testing** in beta with A/B tests (If-Then Action #4)

## Deep Plan Quality

- **Depth:** 6/6 levels (L1-L6) = 100% ✅
- **RACI Coverage:** 3/3 L2 nodes = 100% ✅
- **If-Then Actions:** 4 (target ≥2) ✅
- **Quality Gate:** PASS

## Status

✅ All Life OS steps (2-8) complete
✅ Ready for execution starting 2026-03-01
✅ Deep Plan with L1-L6 structure available
✅ Risk mitigation plan in place
