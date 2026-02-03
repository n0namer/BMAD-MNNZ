---
workflowName: life-os
version: 1
planDate: 2026-02-01
status: DRAFT
validationStatus: COMPLETE
validationDate: 2026-02-03
validationReport: validation-report-20260203-160745.md
---

# Life OS Workflow Plan

## Discovery
- Goal: Life & Business Operating System with portfolio management, specialist consultation, scoring, and persistent memory.
- Users: Individual managing personal + business projects.
- Success: Clear guided flow from idea → decision → calendar; low friction review cadence.

## Classification
- Module: bmm
- Tri‑modal: yes (steps-c / steps-e / steps-v)
- Continuable: no (single-session flow per run)
- Output: workflow plan + project file + decision log

## Requirements
- Interaction style: intent‑based facilitation, 1–2 questions at a time.
- Outputs: plan file, decisions log, project file, metrics updates.
- References: MCDA + stage‑gate + portfolio health + integration patterns.
- WIP limit: enforce max 2 active projects.

## Design
- Create flow: step‑01 collect idea → step‑02 specialist match → step‑03 consilium → step‑04 scoring → step‑05 integration → step‑06 calendar sync.
- Edit flow: update project → rescore → kill project.
- Validate flow: daily/weekly/monthly review.

## Tools & Data
- Data references in data/ (MCDA, stage‑gate, portfolio health, integration patterns, etc.).
- Memory storage: Markdown + Claude Flow.
