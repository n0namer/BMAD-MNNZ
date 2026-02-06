# VALIDATION AGENT 5: EXACT DIFFS FOR ALL FIXES

**Purpose:** Copy-paste ready diffs for all 3 issues found
**Usage:** Use these exact changes to fix issues immediately
**Time:** ~15 minutes total (1 + 5 + 5 minutes)

---

## FIX #1: c-03b1-offer-check.md (Line 3)

### Current Content
```yaml
---
stepId: c-03b1
stepType: user-input
stepName: Фильтр Офферов — "Мне Не Лень?" (Content Machine Stage 4)
estimatedMinutes: 2
nextStepFile: ./c-03b2-offer-generation.md
---
```

### Fixed Content
```yaml
---
stepId: c-03b1
type: user-input
stepName: Фильтр Офферов — "Мне Не Лень?" (Content Machine Stage 4)
estimatedMinutes: 2
nextStepFile: ./c-03b2-offer-generation.md
---
```

### Change
```diff
--- c-03b1-offer-check.md
+++ c-03b1-offer-check.md
@@ -1,6 +1,6 @@
 ---
 stepId: c-03b1
-stepType: user-input
+type: user-input
 stepName: Фильтр Офферов — "Мне Не Лень?" (Content Machine Stage 4)
 estimatedMinutes: 2
 nextStepFile: ./c-03b2-offer-generation.md
```

---

## FIX #2: c-03b2-offer-generation.md (Line 3)

### Current Content
```yaml
---
stepId: c-03b2
stepType: automated
stepName: Генерация Офферов On-the-Fly (Content Machine Stage 3)
estimatedMinutes: 1
nextStepFile: ./c-03c-draft.md
---
```

### Fixed Content
```yaml
---
stepId: c-03b2
type: automated
stepName: Генерация Офферов On-the-Fly (Content Machine Stage 3)
estimatedMinutes: 1
nextStepFile: ./c-03c-draft.md
---
```

### Change
```diff
--- c-03b2-offer-generation.md
+++ c-03b2-offer-generation.md
@@ -1,6 +1,6 @@
 ---
 stepId: c-03b2
-stepType: automated
+type: automated
 stepName: Генерация Офферов On-the-Fly (Content Machine Stage 3)
 estimatedMinutes: 1
 nextStepFile: ./c-03c-draft.md
```

---

## FIX #3A: posts_content_template.csv (Header Row)

### Current Content (First Line)
```csv
id,research_id,angle_used,publish_date,platform,post_title_short,content_500_chars,content_250_chars,content_100_chars,quality_score,ctr_potential,engagement_score,status,notes
```

### Fixed Content (First Line)
```csv
id,research_id,angle_used,publish_date,platform,post_title_short,content_500_chars,content_250_chars,content_100_chars,quality_score,ctr_potential,engagement_score,status,notes,pain_points_json,generated_offers_json
```

### Change
```diff
--- posts_content_template.csv (Header)
+++ posts_content_template.csv (Header)
-id,research_id,angle_used,publish_date,platform,post_title_short,content_500_chars,content_250_chars,content_100_chars,quality_score,ctr_potential,engagement_score,status,notes
+id,research_id,angle_used,publish_date,platform,post_title_short,content_500_chars,content_250_chars,content_100_chars,quality_score,ctr_potential,engagement_score,status,notes,pain_points_json,generated_offers_json
```

### Example Data Row (Add Empty Columns)
```
Old:
1,1,"angle_1",2026-01-28,telegram,"3 часа вместо недели","3 часа вместо недели: как ИИ подтягивает контент 👉 Хочешь попробовать?","3 часа вместо недели — вот что ИИ даёт контенту","Как ИИ ускоряет контент",92,4.5,4.8,ready,"Отличный пост для публикации"

New:
1,1,"angle_1",2026-01-28,telegram,"3 часа вместо недели","3 часа вместо недели: как ИИ подтягивает контент 👉 Хочешь попробовать?","3 часа вместо недели — вот что ИИ даёт контенту","Как ИИ ускоряет контент",92,4.5,4.8,ready,"Отличный пост для публикации","[""Slow docs"", ""One person dependency""]","[{""title"": ""Training""}]"
```

---

## FIX #3B: c-03c-draft.md (Add Documentation)

### Location
After the existing "## SAVED DATA" section, add this new subsection:

### New Section to Add
```markdown
### CSV Columns for Content Machine Posts

When `content_type == "demo"`, the following additional columns are populated in `posts_content.csv`:

#### pain_points_json
- **Type:** JSON array
- **Purpose:** Store the business pain points addressed by this post
- **Source:** `pain_points_json[selected_angle]` from `ideas_research.csv` (populated in c-02c-research)
- **Format:** `["Pain 1", "Pain 2", "Pain 3"]`
- **Example:**
  ```json
  ["Slow documentation process", "Dependency on single person", "Scaling requires hiring"]
  ```
- **When Populated:** Only for Content Machine posts (content_type == "demo")
- **When Used:** For tracking which pain points were addressed in each post

#### generated_offers_json
- **Type:** JSON array of objects
- **Purpose:** Store the offers that were woven into this post
- **Source:** `generated_offers` from `workflow_state.json` (populated in c-03b2-offer-generation)
- **Format:**
  ```json
  [
    {
      "title": "Training / Mentorship",
      "description": "I'll teach you to use BMAD",
      "cta": "Learn more"
    },
    {
      "title": "Process Setup",
      "description": "I'll build this workflow for you",
      "cta": "Get setup"
    }
  ]
  ```
- **When Populated:** Only for Content Machine posts (content_type == "demo")
- **When Used:** For tracking which offers were included in which posts

#### Example Complete Row (Content Machine Post)

```csv
id,research_id,angle_used,publish_date,platform,post_title_short,content_500_chars,content_250_chars,content_100_chars,quality_score,ctr_potential,engagement_score,status,notes,pain_points_json,generated_offers_json
1,1,"angle_1",2026-01-28,telegram,"3 часа вместо недели","Full 500 char content...","3 часа вместо недели — вот что ИИ даёт контенту","Как ИИ ускоряет контент",92,4.5,4.8,ready,"Content Machine variant","[""Slow documentation"",""Single person dependency""]","[{""title"":""Training"",""cta"":""Learn""}]"
```
```

---

## FIX #3C: c-03b1-offer-check.md (Add File Locations)

### Location
Find the section "## Step 2: Сохранение State" and after the JSON example block, add:

### New Section to Add
```markdown
**Storage Location:**

The `workflow_state.json` file is created/updated in the project root directory:
- **Path:** `./workflow_state.json` (same level as `workflow.md`)
- **Lifecycle:**
  - Created: First time c-03b1 is executed
  - Updated: After each step in the workflow
  - Cleared: When user returns to main menu or workflow is restarted
- **Purpose:** Temporary session-based storage for multi-step data flow
- **Visibility:** Used internally by system, user doesn't need to interact with it

---

**Offer Filter Persistence:**

The `offer_filter.csv` file stores your preferences permanently:
- **Path:** `./user_preferences/offer_filter.csv`
- **Created:** First time you run a Content Machine (demo) idea
- **Updated:** Only when you explicitly choose [Да] to modify preferences
- **Reused:** Automatically for all future demo-ideas in this project
- **Manual Edit:** Can be edited directly in spreadsheet app if needed

---

**Directory Structure:**

System creates these directories automatically:
```
project-root/
├── workflow.md
├── workflow_state.json (temporary, per session)
├── ideas_inbox.csv
├── ideas_research.csv
├── posts_content.csv
└── user_preferences/
    └── offer_filter.csv (persistent profile)
```
```

---

## FIX #3D: workflow.md (Add Documentation)

### Location
Add new section after the "## 🎯 CONTENT MACHINE PIPELINE (New!)" section or at the end of the document:

### New Section to Add
```markdown
## 📁 Data Storage & File Locations

### Persistent Storage (Session-Independent)

These files persist across sessions and accumulate over time:

**ideas_inbox.csv**
- Location: Project root
- Purpose: All ideas ever added
- Columns: id, date_added, source, raw_idea, category, status, notes, content_type

**ideas_research.csv**
- Location: Project root
- Purpose: Research results for each idea
- Columns: id, original_idea_id, research_date, main_angle, angles_list, pain_points_json, ...

**posts_content.csv**
- Location: Project root
- Purpose: All posts created (drafts and published)
- Columns: id, research_id, angle_used, publish_date, ..., pain_points_json, generated_offers_json

**user_preferences/offer_filter.csv**
- Location: `user_preferences/` subdirectory
- Purpose: Your Content Machine profile (which offers you're willing to sell)
- Created: First time you use Content Machine mode (c-03b1)
- Updated: Only when you change your preferences

### Temporary Storage (Session-Dependent)

These files are temporary and specific to the current workflow session:

**workflow_state.json**
- Location: Project root
- Purpose: Multi-step data flow between steps
- Lifetime: From workflow start until user returns to menu
- Contents:
  - content_type (TEXT or DEMO)
  - selected_angle (current angle choice)
  - offer_filter_configured (boolean)
  - willing_offers (list of accepted offer types)
  - pain_points (generated pain points)
  - generated_offers (offers to embed in draft)
- Cleared: When workflow restarts or user goes back to menu
```

---

## VERIFICATION AFTER APPLYING FIXES

### Test 1: Field Names (30 seconds)

```bash
cd "D:/Users/NIKITA/Documents/DEV/BMAD-MNNZ/_bmad/bmm/workflows/idea-to-post-pipeline/steps-c"

# Check c-03b1
head -3 c-03b1-offer-check.md | tail -1
# Should output: type: user-input

# Check c-03b2
head -3 c-03b2-offer-generation.md | tail -1
# Should output: type: automated

# Check all steps use 'type:'
grep "^type:" c-*.md | wc -l
# Should output: 42
```

### Test 2: CSV Header (30 seconds)

```bash
cd "D:/Users/NIKITA/Documents/DEV/BMAD-MNNZ/_bmad/bmm/workflows/idea-to-post-pipeline/data/csv-templates"

# Check column count
head -1 posts_content_template.csv | tr ',' '\n' | wc -l
# Should output: 16

# Check new columns exist
head -1 posts_content_template.csv | grep "pain_points_json"
# Should output something (no error)

head -1 posts_content_template.csv | grep "generated_offers_json"
# Should output something (no error)
```

### Test 3: Documentation (1 minute)

```bash
cd "D:/Users/NIKITA/Documents/DEV/BMAD-MNNZ/_bmad/bmm/workflows/idea-to-post-pipeline"

# Check c-03c has new CSV section
grep -n "CSV Columns for Content Machine" steps-c/c-03c-draft.md
# Should find line number

# Check c-03b1 has location docs
grep -n "Storage Location" steps-c/c-03b1-offer-check.md | head -1
# Should find line number

# Check workflow.md has storage section
grep -n "Data Storage & File Locations" workflow.md
# Should find line number
```

---

## STEP-BY-STEP APPLY GUIDE

### Using a Text Editor (e.g., VS Code)

**Step 1: Fix c-03b1-offer-check.md**

1. Open file: `steps-c/c-03b1-offer-check.md`
2. Go to line 3
3. Replace `stepType:` with `type:`
4. Save file

**Step 2: Fix c-03b2-offer-generation.md**

1. Open file: `steps-c/c-03b2-offer-generation.md`
2. Go to line 3
3. Replace `stepType:` with `type:`
4. Save file

**Step 3: Fix posts_content_template.csv**

1. Open file: `data/csv-templates/posts_content_template.csv`
2. Go to line 1 (header)
3. At end of header, add: `,pain_points_json,generated_offers_json`
4. Save file

**Step 4: Add CSV documentation to c-03c-draft.md**

1. Open file: `steps-c/c-03c-draft.md`
2. Find section: `## SAVED DATA`
3. After the existing data structure, add the "CSV Columns for Content Machine" section (from FIX #3B above)
4. Save file

**Step 5: Add file locations to c-03b1-offer-check.md**

1. Open file: `steps-c/c-03b1-offer-check.md`
2. Find section: `## Step 2: Сохранение State`
3. After the JSON example, add the "Storage Location" section (from FIX #3C above)
4. Save file

**Step 6: Add file locations to workflow.md**

1. Open file: `workflow.md`
2. At the end (or after CM section), add the "Data Storage & File Locations" section (from FIX #3D above)
3. Save file

### Using Command Line (Linux/Mac)

```bash
cd "D:/Users/NIKITA/Documents/DEV/BMAD-MNNZ/_bmad/bmm/workflows/idea-to-post-pipeline"

# Fix #1: c-03b1
sed -i 's/^stepType:/type:/' steps-c/c-03b1-offer-check.md

# Fix #2: c-03b2
sed -i 's/^stepType:/type:/' steps-c/c-03b2-offer-generation.md

# Fix #3: CSV header (more manual, see GUI steps above)
```

### Using PowerShell (Windows)

```powershell
cd "D:/Users/NIKITA/Documents/DEV/BMAD-MNNZ/_bmad/bmm/workflows/idea-to-post-pipeline"

# Fix #1: c-03b1
(Get-Content steps-c/c-03b1-offer-check.md) -replace '^stepType:', 'type:' | Set-Content steps-c/c-03b1-offer-check.md

# Fix #2: c-03b2
(Get-Content steps-c/c-03b2-offer-generation.md) -replace '^stepType:', 'type:' | Set-Content steps-c/c-03b2-offer-generation.md
```

---

## FINAL VALIDATION

### Checklist After All Fixes

- [ ] c-03b1-offer-check.md line 3: `type: user-input` (not `stepType:`)
- [ ] c-03b2-offer-generation.md line 3: `type: automated` (not `stepType:`)
- [ ] posts_content_template.csv has 16 columns (14 + 2 new)
- [ ] c-03c-draft.md has "CSV Columns for Content Machine" section
- [ ] c-03b1-offer-check.md has "Storage Location" documentation
- [ ] workflow.md has "Data Storage & File Locations" section
- [ ] All tests from "Verification After Applying Fixes" section pass
- [ ] No errors when opening any fixed files
- [ ] Compliance improved from 94% to 100%

---

## TROUBLESHOOTING

### If `sed` command doesn't work on Windows
→ Use PowerShell command above, or manually edit in text editor

### If CSV shows extra column
→ Verify you added comma correctly: `...,pain_points_json,generated_offers_json`

### If line numbers don't match
→ File may have changed; search for `stepType:` or `SAVED DATA` instead

### If verification tests fail
→ Check that you saved all files after making changes

---

## COMMIT MESSAGE FOR GIT

After applying all fixes:

```
fix: standardize step types and add Content Machine CSV columns

- Fix: c-03b1-offer-check.md — change stepType to type (line 3)
- Fix: c-03b2-offer-generation.md — change stepType to type (line 3)
- Add: pain_points_json and generated_offers_json columns to posts_content_template.csv
- Docs: Add CSV columns documentation to c-03c-draft.md
- Docs: Add file locations documentation to c-03b1-offer-check.md
- Docs: Add data storage section to workflow.md

These fixes improve specification compliance from 94% to 100%.
All Content Machine features now have complete CSV documentation.
File storage locations clearly documented for developers.

Validation Report: VALIDATION-AGENT-5-STEP-TYPES-REPORT.md
```

---

**END OF DIFFS**

Total Changes: 6 files modified
Total Lines: ~50 lines added/modified
Total Time: ~15 minutes
Risk Level: Zero (all cosmetic/documentation)

