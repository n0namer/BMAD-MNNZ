---
name: 'step-08.8-activation-setup'
description: 'L2-S4: Execute activation and setup project structure'
nextStepFile: '../steps-x/step-x-01-kickoff.md'
ideaFile: '{bmb_creations_output_folder}/life-os/ideas-bank/planned/idea-{NNN}-{sphere}-{name}.md'
projectsFolder: '{bmb_creations_output_folder}/life-os/projects-bank/'
activationScript: '../scripts/create-project-from-idea.sh'
---

# Step 8.8: Activation Setup (L2-S4)

## STEP GOAL

Execute activation of planned idea into active project: create project folder structure, copy plan, archive idea, and setup traceability.

**Previous Step:** Step 8.7 (Decision made to activate)

💡 **Setup Reference:** `../data/activation-decision-guide.md`

## MANDATORY EXECUTION RULES

**Universal:**
- 🛑 This step ONLY runs if user selected [A] ACTIVATE in Step 8.7
- 📖 Read complete step file first
- 💬 Facilitator role - guide user through setup
- ✅ Always speak in `{communication_language}`
- 🎯 MUST call activation script to ensure proper structure

**Step-Specific:**
- 💾 MUST update both idea and project metadata with cross-references
- 📁 MUST archive idea to `ideas-bank/archive/activated/`
- 🔗 MUST create bidirectional traceability (origin_idea ↔ became_project)

## EXECUTION PROTOCOLS

Follow Search Orchestrator protocol (CLI memory → local MD → web/MCP) for setup best practices.

---

## MANDATORY SEQUENCE

### 1. Confirm Activation Decision

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚡ ACTIVATING PROJECT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Idea:** {idea_name}
**Sphere:** {sphere}
**Status:** PLANNED → ACTIVE

Ready to create project structure and activate?
[Y] Yes, proceed | [N] Cancel activation
```

If [N]: Return to Step 8.7 menu.

### 2. Execute Activation Script

**Call activation script:**
```bash
# Windows
powershell -File "{activationScript}" -IdeaFile "{ideaFile}"

# macOS/Linux
bash "{activationScript}" "{ideaFile}"
```

**The script performs:**
1. Create project folder: `projects-bank/active/project-{NNN}-{name}/`
2. Create project structure:
   ```
   project-{NNN}-{name}/
   ├── project.md          # Main project file
   ├── plan.md             # Detailed plan (from L1-L6)
   ├── tasks/              # Task breakdown
   ├── artifacts/          # Deliverables
   ├── logs/               # Daily logs
   └── retrospective/      # Learnings
   ```
3. Copy plan from idea to `project.md`
4. Update project.md frontmatter:
   ```yaml
   id: project-{NNN}
   name: {project_name}
   status: active
   created_date: {ISO_DATE}
   origin_idea: idea-{NNN}-{sphere}-{name}
   sphere: {sphere}
   priority: {high|medium|low}
   estimated_duration: {duration}
   progress: 0%
   ```
5. Archive idea:
   - Move to: `ideas-bank/archive/activated/idea-{NNN}-activated-{DATE}.md`
   - Update frontmatter:
     ```yaml
     status: activated
     activated_date: {ISO_DATE}
     became_project: project-{NNN}
     ```

### 3. Verify Project Structure

**Check files created:**
```bash
# Verify project folder exists
ls -la "{projectsFolder}/active/project-{NNN}-{name}/"

# Verify all required files
[ -f project.md ] && echo "✓ project.md"
[ -f plan.md ] && echo "✓ plan.md"
[ -d tasks/ ] && echo "✓ tasks/"
[ -d artifacts/ ] && echo "✓ artifacts/"
[ -d logs/ ] && echo "✓ logs/"
[ -d retrospective/ ] && echo "✓ retrospective/"
```

**If any file missing:**
```
⚠️  Activation incomplete: Missing {file_name}

Manual creation required:
1. Create file/folder: {path}
2. Copy template from: {template_path}
3. Update frontmatter

Continue? [Y/N]
```

### 4. Display Activation Summary

**Confirmation Message:**
```
✅ PROJECT ACTIVATED!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📁 Project Created:
   projects-bank/active/project-{NNN}-{name}/

📋 Files Created:
   ✓ project.md (main file with plan)
   ✓ plan.md (L1-L6 breakdown)
   ✓ tasks/ (task structure)
   ✓ artifacts/ (deliverables folder)
   ✓ logs/ (daily logs)
   ✓ retrospective/ (learnings)

🔗 Traceability:
   Origin: idea-{NNN}-{sphere}-{name}
   Archived: ideas-bank/archive/activated/

📊 New Capacity: {ACTIVE_COUNT+1} / 5 active projects

Next Steps:
1. Review project.md
2. Break down tasks/ folder
3. Start execution (or use PDCA planning)

Ready to start work? [Y]es | [N]o, configure first
```

### 5. Initialize Project (If [Y] Selected)

**Options:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🚀 PROJECT INITIALIZATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[K] Start Kickoff (recommended)
    → Run Step X-01 (Project Kickoff)
    → Setup tools, tasks, and tracking

[P] Use PDCA Planning
    → Structured Plan-Do-Check-Act
    → Deeper task breakdown

[M] Manual Setup
    → Configure project manually
    → Start execution immediately

[L] Later
    → Return to main menu
    → Configure project later

Choice: [K/P/M/L]
```

**Route based on choice:**
- [K]: Load `../steps-x/step-x-01-kickoff.md`
- [P]: Load PDCA planning workflow
- [M]: Show manual setup instructions
- [L]: Return to main menu

### 6. Update Memory

**After activation:**
```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "life-os:activation:project-{NNN}" \
  --content "{\"idea_id\":\"idea-{NNN}\",\"project_id\":\"project-{NNN}\",\"activated_date\":\"{ISO_DATE}\",\"capacity\":\"{NEW_COUNT}/5\",\"plan_depth\":\"{L1-L3|L1-L6}\"}"
```

---

## QUALITY GATES

**Required Before Proceeding:**
- ☐ Project folder created with all subfolders
- ☐ project.md copied from idea plan
- ☐ Frontmatter updated (origin_idea, became_project)
- ☐ Idea archived to ideas-bank/archive/activated/
- ☐ Traceability verified (bidirectional links)

**Red Flags:**
- Missing project folder structure
- Idea not archived
- Missing traceability links
- Frontmatter incomplete

---

## SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- Project folder created with proper structure (6 files/folders)
- Plan copied to project.md
- Frontmatter complete with traceability
- Idea archived with activation metadata
- Memory updated
- User knows next steps

### ❌ FAILURE:
- Incomplete folder structure
- Missing traceability links
- Idea not archived
- Skipping memory update
- User confused about next steps

**Master Rule:** Activation must create complete, traceable project structure.

---

## NOTES

**Activation Script Location:** `./scripts/create-project-from-idea.sh`

**If script missing:**
```
⚠️  Activation script not found: {activationScript}

Manual activation steps:
1. Create folder: projects-bank/active/project-{NNN}-{name}/
2. Copy plan to project.md
3. Create subfolders: tasks/, artifacts/, logs/, retrospective/
4. Archive idea to ideas-bank/archive/activated/
5. Update frontmatter in both files

Recommend: Create activation script first
```

**Script Creation:**
```bash
# Windows
New-Item -Path "./scripts/create-project-from-idea.ps1" -ItemType File

# macOS/Linux
touch ./scripts/create-project-from-idea.sh
chmod +x ./scripts/create-project-from-idea.sh
```

**Time Estimate:**
- Script execution: 30 seconds
- Verification: 1 min
- Initialization choice: 2 min
- **Total: 3-5 min**

---

## HANDOFF TO NEXT STEP

**If user selected [K] Start Kickoff:**
- Load: `../steps-x/step-x-01-kickoff.md`
- Context: New project activated, ready for kickoff
- Input: project-{NNN}-{name} folder path

**If user selected [P] PDCA Planning:**
- Load: PDCA workflow (if implemented)
- Context: New project activated, needs detailed planning

**If user selected [M] Manual or [L] Later:**
- Return to main menu
- Save state: project activated, awaiting user action
