---
name: ruflo-factory-operator
description: Use when starting or resuming software development in a project managed with Ruflo, BMad, CrewSync, Codex, Graphify or Codebase Memory, especially in a fresh agent/session or before releasing parallel coding work.
---

# Ruflo Factory Operator

## Core principle

Recover project truth, prove the plan, then spend worker tokens. This skill is project-agnostic: shared Factory rules never replace the target repository's BMad/AGENTS/Git/tests/runtime truth.

Keep this portable skill concise. Historical evidence may inform investigation, but must be labeled historical/superseded and never treated as current policy; current project/profile policy is authoritative. Do not create a duplicate manual, tracker, or source of truth.

## Mandatory startup

1. Resolve **one target project** from explicit user intent, cwd/Git root, or Ruflo registry. Freeze that project scope before reading any global READY backlog.
2. Read the target project's AGENTS/BMad/Git/tests/runtime evidence first. Existing dirty work belongs to its current owner unless explicitly assigned.
3. If the shared Ruflo runtime is available, read fully:
   - `D:\Users\NIKITA\Documents\DEV\ruflo\docs\RUFLO_FACTORY_OPERATOR.md`
   - `D:\Users\NIKITA\Documents\DEV\ruflo\docs\AI_FACTORY_BOOTSTRAP.md`
   - `RUFLO_OPERATING_CONTRACT.md` when changing Factory/retrieval/learning behavior.
4. Activate canonical `bmad-help`, recover the active authoritative plan/status, and never create a competing PLAN/TODO/status source.
5. Inspect branch/HEAD/recent commits/dirty state, deterministic tests/runtime evidence, Ruflo profile/evidence, and the **project-scoped** live CrewSync state.
6. When a curated Factory Codex home exists, use it instead of inheriting unrelated global skills/plugins/auth.
7. Inventory existing capabilities/resources before proposing new infrastructure.

If local Factory docs are unavailable, do not invent machine capabilities. Continue read-only from this skill plus project truth and report the missing evidence.

## Hard project-scope guard

The global Factory/CrewSync backlog is **not** permission to work on another project. A free worker slot may be filled only with:
- READY work owned by the current target project; or
- a shared Factory task whose description/evidence explicitly states that it blocks the current target project.

Never launch, stop, repair, replan, index, deploy, or otherwise mutate a foreign project merely to keep workers busy. Cross-project work requires explicit user scope or a separately authorized coordinator.

## Planning and release gate

For unfamiliar, multi-step, architectural, cross-repository, or materially changed work, no product implementation task is released before `PLAN_ACCEPTED`. A tiny already-accepted task may skip the multi-node planning DAG only when BMad/project truth already defines dependencies, exact scopes, acceptance, deterministic validation and evidence.

Planning must cover: source-of-truth freeze; TRIZ/ideal result; resource/capability inventory; constraints/contradictions; Value of Information; pre-mortem; dependency/resource DAG; critical and near-critical path; independent plan reviews; replan triggers; release gate.

Materialize planning state in the existing BMad/CrewSync path, not a parallel plan. Every implementation node must define one outcome, dependencies, read scope, exact write scope, acceptance, deterministic validation, evidence, risk/model policy, and `replan_if`.

## Execution after acceptance

Use current `factory-policy.json` and the target project profile, not examples embedded in old docs.

- Ruflo owns the logical DAG, dynamic role planning, retrieval, routing and accepted learning.
- CrewSync is the transactional guard for project-scoped ownership/blocking; CrewSync holder identity is **not** the logical agent role.
- Select local or cloud execution transport from the target project profile; do not infer transport from worker availability or old examples.
- Official `@claude-flow/codex` is the bounded repository executor.
- Prefer Ruflo Agent Pool/Agent Teams for decomposable work. Swarm is conditional. Hive/native Codex multi-agent remain experimental until full correctness/recovery evidence passes.
- Active concurrency is dynamic: min(project READY depth, disjoint writable scopes, project/profile cap, host/token budget). Do not optimize agent count.
- Use up to the configured cap only for useful independent work. Do not create read-only filler tasks to reach a number.
- Multiple writers may run concurrently only when exact write scopes are proven disjoint. Otherwise serialize the conflicting surface.
- Freeze the target project before scheduling. A worker slot is useful only when it advances accepted, project-scoped work; never fill capacity with foreign or filler work.

The portable model rule is: use the cheapest currently allowed model/reasoning sufficient for the bounded role. Never silently inherit or escalate. The central policy/profile is authoritative.

## Dynamic quality team

A writer never self-accepts. Ruflo derives QA roles from task risk:
- minimum: implementer -> verifier/tester -> independent reviewer -> reducer;
- conditional: architect, security, performance or other specialist roles only when risk/acceptance requires them.

Verifier/reviewer roles use distinct Ruflo agent identities and fresh Codex threads. Read-only QA roles may fan out in parallel after the candidate exists. The reducer adjudicates findings against current source/tests; it does not vote-count stale reviewer prose.

## Write authorization and stale-worker safety

Caller-supplied booleans such as `valid:true` never grant write authority. Factory writers require a central, project/task/scope-bound signed permission derived from current CrewSync ownership/resource blocks. Permission must be short-lived and tied to a monotonically increasing generation so an older worker cannot write after ownership changes. Verify the signature, task, project, exact scope, expiry, and generation before spawn and again at mutation hooks; deterministic post-work scope/readback remains required.

## Completion reconciliation

Worker exit, CrewSync DONE, wrapper timeout and deterministic result are separate facts. Completion must be idempotent. A duplicate completion of the same terminal task is not a new failure. A wrapper timeout must not erase already-produced deterministic GREEN evidence, and a stale RUNNING receipt after process exit must become explicit repair/reconcile work rather than silent success.

## Acceptance and learning

Qualified acceptance is ordered lexicographically: correctness/SoT integrity -> triggered architecture/security/performance gates -> deterministic tests/runtime evidence -> BMad write-back/readback -> then speed/token/cost. Worker/CrewSync DONE is candidate evidence only. Only accepted outcomes may become Ruflo success learning.

## Anti-drift

- no foreign-project work from a global READY list;
- no duplicate project plan/status;
- Factory orchestration/control-plane code is Node.js or Python with direct argv process launch; do not introduce `.ps1`, `.cmd` shims, `cmd /c`, `powershell -Command`, `pwsh -Command`, or `shell:true`. On Windows, Factory-spawned child processes use hidden-window mode so parallel workers never open desktop console windows;
- no broad repo study when exact scope is known;
- no overlapping writers on the same surface;
- no destructive reset/clean/stash of foreign work;
- no claiming retrieval/SONA/HNSW helped unless invocation and task-level contribution are evidenced;
- replan on material SoT/architecture/security/ownership change, invalidated capability/resource assumption, repeated critical-path failure or reviewer disagreement.
