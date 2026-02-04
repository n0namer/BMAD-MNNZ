---
workflowName: life-os
version: 1
planDate: 2026-02-01
status: DRAFT
validationStatus: COMPLETE
validationDate: 2026-02-03
validationReport: validation-report-20260203-231448.md
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
- Create flow: step‑01 collect idea → step‑02 roles discovery → step‑03 specialist match → step‑04 consilium → step‑05 scoring → step‑06 integration → step‑07 calendar sync → step‑08 deep plan (optional) → step‑09 complete.
- Edit flow: update project → rescore → kill project → deep plan.
- Validate flow: return‑to‑plan → daily/weekly/monthly review.

## Tools & Data
- Data references in data/ (MCDA, stage‑gate, portfolio health, integration patterns, etc.).
- Memory storage: Markdown + Claude Flow.




