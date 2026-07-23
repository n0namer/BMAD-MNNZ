---
name: bmad-human-review
description: 'Turns a dense product or planning corpus into a human-reviewable decision package without losing the stakeholder intent, evidence, or traceability. Use before specs or implementation when a named human must understand, correct, and explicitly approve product decisions.'
---

# BMad Human Review

## Purpose

Convert an existing product-document corpus into a compact review surface that a responsible human can understand and approve before downstream specification or implementation.

This skill does not simplify the product by deleting meaning. It separates:

1. **decisions the human must verify**;
2. **concise explanations needed to understand them**;
3. **evidence and delivery detail available on demand**.

The full source corpus remains authoritative evidence. The human review package becomes the approval interface.

## Use When

Activate when:

- a user says they must personally check AI-produced product documents;
- documents are accurate but too long or repetitive for stakeholder review;
- a stakeholder request must be preserved while the wording is made human-readable;
- PRD, architecture, UX, backlog, or specs must not advance before explicit human approval;
- the user asks whether documents are understandable, reviewable, or faithful to an upstream request.

Do not use as a prose-polishing pass. Use `bmad-editorial-review-prose` when the decisions and structure are already correct and only language needs improvement.

## Inputs

Resolve:

- the named human approver;
- the governing upstream sources, including direct stakeholder comments;
- the current product and planning artifacts;
- the downstream action being gated, usually `bmad-spec`, architecture, sprint planning, or implementation;
- the existing source of truth and its edit constraints.

Never infer approval from silence, document existence, or prior AI confidence.

## Core Principle: Progressive Disclosure

Produce three logical layers.

### Layer 1 — Human Decision Review

The only layer the approver must read completely. It contains:

- product truth in plain language;
- first user and buyer;
- Jobs and trigger;
- problem and reason to buy;
- offer and economic logic;
- first end-to-end scenario;
- first-release boundary;
- material hypotheses and risks;
- an explicit decision register.

### Layer 2 — Evidence and Rationale

Keep supporting analysis accessible through links, references, appendices, or existing tabs. Include alternatives, calculations, market evidence, quotations, confidence, and revision criteria only where needed to challenge a decision.

### Layer 3 — Delivery Artifacts

PRD, UX, architecture, epics, stories, readiness reports, and specs remain downstream or provisional until the human gate passes. Do not require the product approver to validate implementation detail line by line.

## Workflow

### 1. Reconstruct the stakeholder request

Extract the smallest faithful statement of what the stakeholder asked for. Separate:

- direct requests;
- interpretations made by Product;
- hypotheses introduced later;
- implementation choices.

Create a coverage map from stakeholder request to current decisions. Mark each item:

- `PRESERVED`;
- `DISTORTED`;
- `MISSING`;
- `ADDED — NEEDS APPROVAL`;
- `DELIVERY DETAIL — NOT A PRODUCT DECISION`.

Do not expose a large internal matrix unless useful. Surface all distortions, omissions, and material additions.

### 2. Audit human reviewability

Check whether the current package:

- states the conclusion before the rationale;
- distinguishes decision, fact, hypothesis, and implementation proposal;
- avoids repeating one decision across several sections;
- uses one stable term for each concept;
- lets the reviewer identify required decisions by scanning headings;
- allows the reviewer to finish the mandatory path in one focused session;
- links to evidence instead of embedding all evidence in the primary narrative;
- names the exact gate and approver.

Treat excessive length as a structural problem, not merely a word-count problem.

### 3. Build the Human Decision Review

Prefer updating an existing Review Pack rather than creating a competing document.

Use this structure unless the source requires another:

1. **What the stakeholder asked for**
2. **How Product understands the product**
3. **Decisions requiring human confirmation**
4. **First customer, Jobs, trigger, and alternatives**
5. **Offer and economic model**
6. **First end-to-end product slice**
7. **In scope / out of scope**
8. **Hypotheses, risks, and open questions**
9. **Approval register**
10. **What happens after approval**

For each material decision use:

```markdown
### D-XX — Decision title

**Proposed decision:** one clear statement.

**Why:** the minimum rationale required to judge it.

**Source:** upstream request or evidence pointer.

**If wrong:** consequence or revision trigger.

**Human status:** PROPOSED | APPROVED | REVISE | HYPOTHESIS | DEFERRED | REJECTED

**Human comment:**
```

Do not repeat the same rationale elsewhere in the mandatory review path.

### 4. Preserve traceability

Every material decision must point to:

- the upstream stakeholder request or governing artifact;
- supporting evidence when applicable;
- downstream artifacts affected by approval or revision.

Traceability may live in concise source references or a compact appendix. It must not dominate the review narrative.

### 5. Install the human gate

Before the gated downstream step, require all blocking decisions to be explicitly `APPROVED` by the named human.

Typical blocking decisions:

- product truth;
- first Job;
- first ICP;
- reason to buy;
- offer;
- economic viability assumptions;
- first end-to-end scenario;
- first-release boundary;
- critical legal, operational, or platform constraints.

Set downstream artifacts to `PROVISIONAL` or `BLOCKED BY HUMAN REVIEW` where appropriate. Existing technical work may be retained, but it must not be presented as approved product truth.

### 6. Validate

The package passes only if:

1. the stakeholder request is preserved without material omission or silent reinterpretation;
2. the named human can identify every blocking decision without reading the full corpus;
3. facts, Product decisions, hypotheses, and technical proposals are visibly distinct;
4. every blocking decision has an explicit status and comment location;
5. evidence remains reachable;
6. downstream specs or implementation are blocked until approval;
7. no existing authoritative artifact is silently replaced or duplicated.

## Output

Update the project's existing Review Pack or equivalent approval artifact in its source of truth.

Report:

- fidelity to the stakeholder request;
- human-reviewability findings;
- decisions requiring approval;
- exact artifact changed;
- downstream gate status;
- unresolved distortions or omissions.

## Routing

After completion:

- unresolved product disagreement → `bmad-correct-course`;
- prose-only cleanup → `bmad-editorial-review-prose`;
- structural cleanup of supporting documents → `bmad-editorial-review-structure`;
- all blocking decisions approved and intent ready to lock → `bmad-spec`;
- implementation must not begin before the named human approves the blocking register.

## Constraints

- Never equate shorter with better if meaning is lost.
- Never ask the human to approve architecture or backlog details that are not product decisions.
- Never hide uncertainty inside confident prose.
- Never duplicate the complete evidence corpus in the Human Decision Review.
- Never treat AI-generated status such as READY, PASS, or COMPLETE as human approval.
- Never change an intentionally preserved upstream artifact unless explicitly authorized.
