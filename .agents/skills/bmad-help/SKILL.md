---
name: bmad-help
description: 'Single entry point for BMad in local agents and ChatGPT Web. Inspects the target project, resolves BMad configuration and artifacts, identifies the current phase, selects the next skill, executes it when requested, and writes results back to the target source of truth.'
---

# BMad Help — Universal Entry Point

## Purpose

Use this skill as the single entry point into BMad.

It must work in two environments:

1. **Local mode** — the agent has a checkout, shell, and project filesystem.
2. **Remote/Web mode** — ChatGPT or another remote agent receives a link to this file and works through GitHub or connected sources without a local checkout.

The user should not need to know the BMad catalog, phase names, file paths, or which specialist skill to invoke.

## Desired Outcomes

When this skill completes, the user should:

1. **Know where the target project is** — repository or declared source of truth.
2. **Know the actual state** — active module, current phase, completed, draft, missing, and stale artifacts.
3. **Know what is next** — optional steps first and one next required step.
4. **Know why** — recommendation tied to evidence and BMad gates, not memory or guesswork.
5. **Get execution, not only advice** — if the user says to act, continue into the selected skill immediately.
6. **Get write-back** — update the existing source of truth or create the required artifact at the resolved path.
7. **Stay oriented** — surface only the minimum context needed for the current decision.

## Canonical BMad Control Plane

When this file is opened by URL, treat the following repository as the canonical BMad control plane:

- Repository: `https://github.com/n0namer/BMAD-MNNZ`
- Help catalog: `_bmad/_config/bmad-help.csv`
- Canonical skills: `.agents/skills/<skill-name>/SKILL.md`
- Config resolver: `_bmad/scripts/resolve_config.py`
- Default configuration: `_bmad/config.toml`

**Important:** BMAD-MNNZ supplies the workflow rules. It is not automatically the target project. Never write a different project's artifacts into BMAD-MNNZ.

## Target Project Resolution

Resolve the target project in this order:

1. Repository, document, Notion page, Google Drive file, or other source explicitly named in the user's current request.
2. The repository or source already established as the current project's source of truth in the conversation.
3. The connected GitHub repository associated with the current project/chat.
4. A repository URL found in the current project instructions or project files.

Do not treat the canonical BMAD-MNNZ repository as the target merely because this skill lives there.

If several candidates exist, choose the one most directly tied to the user's requested deliverable and state the assumption. Ask only when writing to the wrong source would cause material harm and no safe inference is possible.

## Source-of-Truth Hierarchy

For project facts and deliverables, use this priority:

1. User's explicit instruction in the current request.
2. Target project's declared source of truth and project instructions.
3. Target project's committed configuration and customizations.
4. Existing target artifacts and their latest revisions.
5. Conversation context.
6. Canonical BMad defaults.

Never replace verified project facts with canonical examples.

## Bootstrap Procedure

Always perform these steps before recommending or executing another BMad skill.

### Step 1 — Resolve the target root

Record:

- target repository/source;
- branch or document revision when available;
- requested outcome;
- whether the user asked for advice, review, creation, editing, or full execution.

### Step 2 — Detect BMad installation

In the target repository, look for:

- `_bmad/_config/bmad-help.csv`
- `_bmad/config.toml`
- `_bmad/custom/config.toml`
- `.agents/skills/`
- `_bmad-output/`
- `docs/`
- `AGENTS.md`, `README.md`, project indexes, and source-of-truth declarations.

There are two valid states:

- **Installed:** use the target project's catalog, configuration, customizations, and local skill copies.
- **Not installed:** use the canonical BMAD-MNNZ catalog and skills as the workflow engine, while reading and writing artifacts only in the target project/source.

Do not require BMad to be copied into every target repository before it can be used.

### Step 3 — Resolve configuration

#### Local mode

Run:

```bash
uv run --python 3.11 {project-root}/_bmad/scripts/resolve_config.py --project-root {project-root}
```

If `uv` is unavailable, use Python 3.11+.

#### Remote/Web mode

Read and merge these target-project files in order, with later values overriding earlier values:

1. `_bmad/config.toml`
2. `_bmad/config.user.toml`
3. `_bmad/custom/config.toml`
4. `_bmad/custom/config.user.toml`

Apply the same merge rules as `resolve_config.py`:

- scalar: later value wins;
- table: deep merge;
- keyed arrays using `code` or `id`: merge by key;
- other arrays: append.

Replace `{project-root}` with the target repository root.

If target configuration is absent, use these fallback output locations:

- planning: `_bmad-output/planning-artifacts/`
- implementation: `_bmad-output/implementation-artifacts/`
- tests: `_bmad-output/test-artifacts/`
- project knowledge: `docs/`

A target project's established document location overrides these fallbacks.

### Step 4 — Load the catalog

Use the target project's `_bmad/_config/bmad-help.csv` when present. Otherwise use the canonical catalog from BMAD-MNNZ.

Catalog columns:

```text
module,skill,display-name,menu-code,description,action,args,phase,preceded-by,followed-by,required,output-location,outputs
```

Interpretation:

- `phase` defines the high-level sequence;
- `preceded-by` and `followed-by` are recommended ordering hints;
- `required=true` is a real gate;
- `output-location` and `outputs` define where evidence of completion should exist;
- `_meta` rows point to module documentation.

### Step 5 — Discover actual project state

Search the resolved output locations using the catalog's `outputs` patterns.

Read only enough evidence to classify each relevant artifact as:

- `completed` — exists and contains a usable finished result;
- `draft` — exists but is explicitly draft, incomplete, placeholder-heavy, or missing acceptance criteria;
- `stale` — exists but conflicts with newer decisions or source-of-truth changes;
- `missing` — required output not found;
- `unknown` — access or evidence is insufficient.

Use indexes first when available, then inspect the smallest relevant set of files. Do not load the entire repository without need.

User statements can establish completion, but verify the artifact when access exists. Never fabricate project-specific details or claim an artifact was updated without a successful write action.

### Step 6 — Determine the active module and phase

Infer the active module from the user's requested outcome and existing artifacts.

Then identify:

1. the latest meaningfully completed phase;
2. unfinished optional steps relevant to the present goal;
3. the earliest unmet `required=true` gate;
4. any contradiction that requires `bmad-correct-course` before continuing.

Do not advance merely because a file exists. A broken, stale, or empty artifact does not satisfy a gate.

## Skill Resolution

When another skill is selected, load it in this order:

1. Target project: `.agents/skills/<skill-name>/SKILL.md`
2. Target project equivalent skill directory if project instructions specify another agent format.
3. Canonical BMAD-MNNZ: `.agents/skills/<skill-name>/SKILL.md`

Project-local skill instructions override canonical instructions for that project. Canonical instructions fill missing capabilities.

For multi-action skills, select the action from catalog context and user intent, for example:

- create a missing artifact;
- update an existing artifact after new evidence;
- validate or review a finished artifact.

## Routing Rules

### Advice request

If the user asks what to do next, return:

1. current state and evidence;
2. relevant optional step(s);
3. one next required step;
4. exact skill, menu code, action, arguments, and target path;
5. an offer to start the clear next step.

### Execution request

Treat phrases such as these as permission to continue, not stop at a recommendation:

- “делай”;
- “действуй”;
- “запусти BMad”;
- “обработай проект по этому скиллу”;
- “внеси изменения”;
- “доведи до следующего этапа”.

Then:

1. select the next justified skill;
2. load its `SKILL.md`;
3. follow that skill as the active working contract;
4. inspect the required project sources;
5. produce or update the artifact;
6. validate against its done criteria;
7. write back to the target source of truth;
8. report the exact changed paths and commit/revision.

Do not ask the user to invoke a second skill manually when the next step is clear and tools allow execution.

### Review request

If the user asks whether artifacts are correct or aligned:

1. identify the governing upstream artifacts;
2. select the relevant validation, editorial, adversarial, readiness, or specialist review skill;
3. create a findings report only when the selected skill requires one;
4. otherwise update the original artifact rather than multiplying documents;
5. preserve intentional originals when the user explicitly says not to change them.

## Write-Back Protocol

Write only to the target project's source of truth.

### Existing artifact

- Read the latest version first.
- Update it in place unless the selected skill explicitly requires a separate report.
- Preserve intentional structure, decisions, links, identifiers, and unrelated content.
- Do not create a competing duplicate document.

### Missing artifact

Create it at the resolved catalog/config path. If no path is declared, use the fallback directories above.

### External source of truth

If the project declares Google Docs, Notion, Airtable, or another connected source as authoritative, update that source when tools permit. Do not silently create a GitHub copy and call it authoritative. A repository pointer or export may be added only when useful and clearly labeled.

### GitHub writes

When authorized to change the repository:

- update the target file using its current blob SHA;
- use a focused commit message such as `bmad: update product brief`;
- do not write project artifacts into the canonical BMAD-MNNZ repository;
- verify the written file after the commit when practical.

If write access is unavailable, provide the complete patch-ready artifact and exact target path, and clearly state that it was not saved.

## Response Format

Use the resolved `core.communication_language` or `core.document_output_language`; otherwise use the user's language.

Keep orientation compact:

```markdown
## Current state
- Target: ...
- Module / phase: ...
- Evidence: ...

## Optional before the gate
- [CODE] **Display Name** — `skill-name`, action, args, reason

## Next required step
- [CODE] **Display Name** — `skill-name`, action, args
- Why now: ...
- Output path: ...

## Execution
- Started/completed: ...
- Changed: ...
- Validation: ...
- Remaining blocker: ...
```

For each recommendation include:

- `[menu-code]` and display name;
- skill name in backticks;
- action for multi-action skills;
- arguments when available;
- concise reason grounded in project evidence;
- exact expected output location.

Show optional items first, then one next required item. Do not dump the full catalog.

## Constraints

- Never confuse the canonical BMAD repository with the target project.
- Never fabricate project state, paths, completion, writes, or test results.
- Never rely only on conversation memory when repository/source evidence is available.
- Never create extra documents when an existing source-of-truth artifact should be updated.
- Never skip an unmet required gate without explicitly recording the exception and its risk.
- Recommend a fresh context window for each major specialist skill, but when the user explicitly asks to execute now, continue in the current chat after loading that skill and narrowing context to its required inputs.
- Prefer one clear next move over a catalog dump.
- Use remote module documentation from `_meta` rows when a general question cannot be answered from a specific skill.
