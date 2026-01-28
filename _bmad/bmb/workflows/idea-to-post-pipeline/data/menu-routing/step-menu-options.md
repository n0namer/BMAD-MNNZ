# Step Menu Options & Routing Template

## Menu Display Format

```
═════════════════════════════════════════════════════════════

  {STEP_TITLE}

═════════════════════════════════════════════════════════════

{MENU_OPTIONS}

═════════════════════════════════════════════════════════════
```

## Common Menu Patterns

### VALIDATION MODE MENUS

Pattern for V-XX validation steps:

```
[1] Option 1 description
[2] Option 2 description
[3] Option 3 description
...
[?] HELP — Show detailed info
[M] BACK to MENU — Return to main menu
[X] EXIT — Return to start
```

### CREATE MODE MENUS

Pattern for C-XX creation steps:

```
[S] SAVE — Save current work
[C] CONTINUE — Proceed to next
[E] EDIT — Modify content
[P] PREVIEW — View output
[?] HELP
[M] BACK to MENU
```

### EDIT MODE MENUS

Pattern for E-XX edit steps:

```
[1] {First Option}
[2] {Second Option}
[?] PREVIEW
[A] APPLY
[R] REVERT
[?] HELP
[M] BACK
```

### YOLO MODE MENUS

Pattern for YOLO quick steps:

```
[G] GO — Execute action
[R] REVIEW — Check work
[S] SAVE — Save results
[X] EXIT
```

## Data Format

Store menu configuration:
```json
{
  "step_id": "step-name",
  "menu_type": "validation|creation|editing|yolo",
  "title": "Step Title",
  "options": [
    { "id": "1", "label": "Option 1", "next": "next-step" },
    { "id": "2", "label": "Option 2", "next": "next-step" },
    { "id": "?", "label": "HELP", "action": "show_help" },
    { "id": "M", "label": "BACK", "action": "menu" }
  ],
  "default_selection": "1",
  "timeout_seconds": 0,
  "error_message": "Invalid selection"
}
```

## Usage in Steps

Replace large menu blocks with:
```markdown
Load menu from: `../../data/menu-routing/step-menu-options.md`

Present menu type: {menu_type}
Step ID: {step_id}

Wait for user selection: [{options}]
```

## EXECUTION RULE

**ALWAYS halt and wait for user input after presenting menu.**
**ONLY proceed when user makes explicit selection.**
