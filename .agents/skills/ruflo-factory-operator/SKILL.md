---
name: ruflo-factory-operator
description: Use when starting or resuming software development in a project managed with Ruflo, BMad, CrewSync, Codex, Graphify or Codebase Memory, especially in a fresh agent/session or before releasing parallel coding work.
---

# Ruflo Factory Operator

## Core principle

Recover project truth, prove the plan, then spend worker tokens. This skill is project-agnostic: shared Factory rules never replace the target repository's BMad/AGENTS/Git/tests/runtime truth.

## Mandatory startup

1. Resolve the target project from explicit user intent, cwd/Git root, or Ruflo registry.
2. If the shared Ruflo runtime is available, read fully:
   - D:\Users\NIKITA\Documents\DEV\ruflo\docs\RUFLO_FACTORY_OPERATOR.md
   - D:\Users\NIKITA\Documents\DEV\ruflo\docs\AI_FACTORY_BOOTSTRAP.md
   - RUFLO_OPERATING_CONTRACT.md when changing Factory/retrieval/learning behavior.
3. Activate canonical bmad-help, resolve project BMad configuration, and recover the active authoritative plan/status instead of creating a competing PLAN.
4. Inspect branch/HEAD/recent commits/dirty state, deterministic tests/runtime evidence, Ruflo profile/evidence, and live CrewSync sessions/tasks/claims/leases/locks.
5. When a curated Factory Codex home is configured, use it for Factory workers instead of inheriting unrelated global skills/plugins/auth; ambient global Codex state is not project truth.
6. Inventory existing capabilities/resources before proposing new code.

If local Factory docs are unavailable, do not invent machine capabilities. Continue read-only from this skill plus target-project truth and report the missing Factory evidence.

## Planning gate

For unfamiliar, multi-step, architectural, cross-repository, or materially changed work, no product implementation task is released before PLAN_ACCEPTED.

Answer from evidence before asking the human: goal; TRIZ Ideal Final Result; decomposition; benefits; available resources; capacity/time constraints; technical/organizational limits and contradictions; decision-relevant evidence; actors/ownership; observable final result; alternative-selection criteria; dependency priority; pre-mortem; resource-constrained DAG/critical path; stage gates and replan triggers. Ask only unresolved questions whose answer can change the decision.

Materialize planning work in CrewSync first: source-of-truth freeze -> parallel capability/gap/readiness analysis -> candidate DAG -> independent BMad/decomposition/cost/evidence reviews -> replan -> final DAG -> release gate. Implementation tasks are created only after the release gate records PLAN_ACCEPTED.

Every future implementation node must define: owner project/repo, goal/why-now, dependencies, read scope, exact write scope, acceptance, deterministic validation, required evidence, role/model/reasoning, worktree/sticky-lane binding when used, and replan_if.

## Execution after acceptance

Use the current Factory policy, not stale examples. Prefer native Ruflo task/agent/Agent-Pool primitives plus official @claude-flow/codex; CrewSync provides cross-process claim/lease/fencing; Codex executes bounded repository work in isolated writable scopes. Legacy Wave Engine/orchestrate.py is compatibility/benchmark tooling unless explicitly required.

Use the cheapest currently allowed model that is sufficient for the bounded role. Never silently inherit or escalate to a forbidden/expensive model. Prove the required project readiness level (structural, development, or full Factory) before the corresponding execution.

## Acceptance and learning

Worker/CrewSync DONE is candidate evidence, never project acceptance. Require deterministic validation, independent review appropriate to risk, coordinator semantic acceptance, BMad write-back and readback. Only accepted outcomes may become Ruflo success learning.

## Hard anti-drift rules

- No duplicate project plan/status source when BMad/project SoT already exists.
- No broad "study the repo and solve it" worker when exact scope can be selected.
- No overlapping concurrent writers or destructive reset/clean/stash of foreign work.
- No treating retrieval memory, registry presence, tests, or source/unit proof as stronger maturity than they actually prove.
- Replan on material SoT/architecture/security/ownership change, stale/missing capability, critical-path repeated failure, reviewer disagreement, or invalidated resource assumptions.
