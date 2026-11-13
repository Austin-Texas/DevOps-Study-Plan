# DevOps Platform — Reusable UI & Development Prompt
**Session:** November 13, 2026  
**Project:** Senior DevOps Engineering Platform  
**Repository:** `Austin-Texas/DevOps-Study-Plan`  
**Live site:** https://austin-texas.github.io/DevOps-Study-Plan/

> This is the approved design direction and implementation checklist from our iterative Commands-page work. Apply the same conventions to other pages **only when requested**. Preserve all existing functionality and data.

## 1. Approved visual direction
- Modern, clean, iOS-like light/dark UI; rounded white cards, subtle borders and shadows, consistent typography and spacing.
- Preserve the existing sidebar and global header, navigation (Topics, Commands, Resources, Projects), responsive behavior, and page content.
- Prefer compact, efficient layouts over large blank sections or unnecessarily tall cards.
- Desktop Commands layout: two columns, left for command entry/filter and expandable category cards, right for command location/status, notes, and original reference. On narrow screens stack columns.
- Opening accordions, editing notes, or expanding the original reference must **not move the adjacent column's content down**. Use independent column flow and an internally scrollable, bounded-height reference viewer where appropriate.
- Command categories use compact accordion rows; arrow points right/down when collapsed and down/up when expanded, consistently. Show the count; display compact command cards inside the expanded category.
- Command detail popup remains open after saving, displays a clear success indicator, exits edit mode and shows the updated read-only details; only the user closes it.
- Changes to a command must immediately update the corresponding command card and any category counts/placement.
- The original Linux command reference remains editable, with a single Copy button, Edit action, and preserved original examples. No duplicate buttons.
- The stats bar (Topics / Hours / Overall / Mastered) should be **visually hidden across pages**, not removed from the DOM if application code still depends on those IDs.

## 2. Command Notebook behavior
- Input to add a command; filter to find saved commands; grouped, expandable command categories.
- Auto-classify using command syntax and executable/subcommand, not incidental usernames, home paths, or arbitrary arguments.
- Examples: `sudo -iu hakkari` and `sudo -iu james` are Linux user/identity commands; `sudo apt update` is Linux package management; `show ip route` is Cisco routing; `terraform plan` is Terraform; `ansible --version` is Ansible.
- Recognize Linux, Cisco, Terraform/OpenTofu, Ansible, Docker, Kubernetes, Windows/PowerShell, AWS, Git, and other relevant tooling. Create a relevant category when needed; avoid putting recognizable commands into Other/Unclassified.
- Check duplicates with normalized syntax and relevant argument placeholders. A command already present should produce a **colored, distinct 'Already saved' message** identifying its exact category/path, not a false 'newly saved' message.
- A newly added command shows a green success message and its category/path. Keep status near the input/category preview.
- Each command card supports open/detail, edit and delete. Detail view shows explanation, correctly separated flags/tokens and meanings, and copyable examples. Never display literal escaped `\\n` in flag explanations.
- Save edits persistently using the application's existing storage mechanism and refresh all rendered views immediately.
- Do not create a separate Notes and Warnings field on every command. Keep contextual safety explanations only where needed for dangerous examples.
- Preserve the original command-reference examples and allow their editing without losing other command data.

## 3. Additional notes panel
- Right column has a collapsible **+ Add more notes** section, under the colored save/location message.
- Users can add unlimited separate notes, edit/delete each, and see save confirmation. Keep the add-note form accessible after saving.
- Opening notes does not reflow or shift the left-hand command cards; maintain independent columns.
- Do not replace or merge existing notes when adding a new one.

## 4. Critical regression found and fixed
- A prior change removed the `#stats-bar` markup to remove the visible statistics strip. Application JavaScript still referenced its child IDs (`stat-topics`, `stat-hours`, `stat-pct`, `stat-mastered`), causing blank page content.
- Fix committed as `648b5a6`: restore required statistics DOM and hide it with CSS (`#stats-bar { display: none !important; }`).
- **Rule:** Never remove DOM nodes that are referenced by JavaScript without updating all references. Prefer non-destructive CSS hiding for purely visual removal. Check browser console and test every tab.
- A GitHub commit is not proof of live deployment. Confirm GitHub Pages finishes publishing and inspect the deployed site before saying the change is live.

## 5. Required workflow for every future page change
1. Read this guide, `README.md`, and the current implementation in `index.html`.
2. Inspect the relevant functions, CSS selectors, DOM IDs, event handlers, and persistent data before editing.
3. Identify exact requested UI change; leave unrelated pages and features untouched.
4. Back up or preserve existing content; make a small, scoped patch rather than rewriting large sections.
5. Check syntax, initialization, navigation, tabs, command input, editing, notes, accordion behavior, local persistence, and light/dark themes.
6. Check responsive layout and confirm expanding one column does not shift the other.
7. Verify the exact requested visual change, ideally on the deployed GitHub Pages site.
8. Commit with a descriptive message and report the commit SHA, deployed URL, and verification status. Never claim a deployment was checked unless it actually was.
9. Do not overwrite browser-local user data or reset progress. If data migration is necessary, preserve old keys and provide backward compatibility.
10. If the user asks to apply this style to another page, **reuse the patterns and behaviors**, not a blind copy of Commands-only content.

## 6. Reusable prompt for future chats
> Open GitHub repository `Austin-Texas/DevOps-Study-Plan` and read `docs/DEVOPS-UI-DESIGN-AND-CHANGE-PROMPT-2026-11-13.md` plus `README.md`. Apply the documented approved design and interaction patterns to **[NAME OF PAGE]**, keeping its existing data and functionality. Use the compact iOS-like responsive layout, independent two-column flow when appropriate, collapsible category cards, meaningful save/duplicate feedback, persistent edits, and non-destructive changes. Do not reintroduce the stats strip or remove required DOM IDs. Test all tabs, existing features, and the published page before reporting completion. Tell me exactly what changed and provide the commit SHA.

## 7. Scope and accuracy
This document records the intended/approved behavior from the conversation, **not a claim that every item is fully implemented or live-verified**. The final repair was committed as `648b5a6`; deployment and UI regression checks must still be independently verified.


## 8. Screenshot-approved Ansible implementation (November 13 follow-up)
The user's screenshot clarifies the approved design beyond the initial written guide:
- Use one rounded, white Command Notebook container with a bold title and short description.
- Inside it, use **two independent, equally sized desktop columns**. Left: command entry and Add button, small storage hint, filter, then compact accordion category list. Right: muted-gray category/location status card, expandable **+ Add more notes**, then expandable **Original [Technology] command reference (preserved) · Editable**.
- Each category header has an arrow, name and right-aligned command count. Expanded categories reveal compact white command cards with inline edit/delete actions. No large blank areas or oversized cards.
- The status panel remains aligned with the input region; use green for successful saves and amber/orange for duplicates, including the saved category/path.
- Notes and reference expansion must not push down the left column. Maintain independent column layout and internal scrolling for long references.
- Retain centered white editing dialogs, explicit save confirmation, and update the visible command card after edits. Save persists in the browser.
- The screenshot is the reference for the overall proportions, card density, typography, and background. Do not change the approved light/dark theme colors or sidebar.
- The Ansible Commands implementation was introduced in commit `221ed4e`. It includes its own browser-local command additions, modifications, deletions, notes, and editable reference. The Linux notebook remains separate and unchanged.
- **Important:** Other technology pages received a shared compact reference style earlier, but do not yet have the full Ansible/Linux notebook feature set. Extend only upon explicit request, and verify deployment and interactions.


## 9. Mandatory feature parity: Linux → Ansible and future technology notebooks

**Requirement:** The Ansible Automation → Commands page must reproduce **all** of the Linux Administration → Commands notebook's interaction patterns, not just its visual style. Apply this checklist to future technology pages when requested. The icons must be visible and usable, not merely described in documentation.

### Every command card
- **Edit (pencil ✎ icon):** opens the existing command in an editable modal. Editable fields include the command text, plain-language explanation, flag/token-by-token meanings (each on a separate line), and example. Editing an existing card must not create a duplicate.
- **Delete (trash 🗑 icon):** removes the intended command after confirmation. Immediately refresh the category and count; preserve unrelated commands.
- **Open/details (expand/open icon ↗ or card click):** opens a readable command-details modal with summary, a structured token/flag meaning table, and a copyable command example. Do not confuse opening with editing; provide an explicit pencil icon inside the modal to enter edit mode.
- **Copy:** one functional Copy action for each example, with temporary “Copied” feedback. Avoid duplicate Copy buttons.
- Icons must have descriptive titles/accessibility labels, keyboard focus states, and sufficiently large click targets. Icon clicks must not inadvertently trigger card-open actions.
- A newly saved or edited command must update the visible card **immediately**, including its text, category and count. Reclassify after a command-text edit.

### Editing workflow
- Modal initially opens in **read-only detail mode** with the Edit pencil icon, Delete icon and Close button.
- Pencil enters edit mode with fields for Command, What does it do?, Flags and meanings (one per line: token/flag | explanation), and Example.
- **Save changes** validates and persists edits, shows a clear green “Changes saved successfully” confirmation, and returns to read-only mode **without closing the modal**. The modal remains open until the user closes it.
- Hide/disable Save and Cancel after a successful save by leaving edit mode; the updated read-only details and example must appear immediately.
- Cancel discards unsaved changes and returns to the same read-only modal. Closing does not delete or undo previously saved changes.
- Parse token/flag explanations into distinct table rows; never show literal `\\n` escape sequences or collapse all explanations into one cell.

### Command entry and categories
- Add input and filter, auto-classification by executable and subcommand, expandable categories, counts and compact cards. Existing commands stay visible and are preserved.
- Recognize duplicates by normalized syntax; display **orange/amber “Already saved”** with exact category/path and do not add another card. Display **green “Saved successfully”** for a genuinely new command and show its location.
- Show a live category preview as the user types where feasible. Command syntax, not incidental username/path, determines category.
- Category accordion arrow changes direction when expanded/collapsed. Expanding a category must not shift the independent right column.

### Right column, notes and reference
- Status/category location panel, then **+ Add more notes**, then editable **Original [Technology] command reference (preserved)**.
- Notes: unlimited separate entries, each with its own **Edit pencil and Delete trash icons**, confirmation after saving, and persistent storage. Adding a note must not replace earlier notes.
- Reference: one Edit pencil action, one Copy button, an editable text area with Save/Cancel, and preserved original reference content. Reference viewer has bounded height and internal scrolling.
- No global “Notes and warnings” field for each command.
- Two equal desktop columns; stack on mobile. Expanding notes or reference must not move left-hand command cards.

### Persistence, safety and regression checks
- Use existing local persistence with stable IDs, preserving all prior user data and reference examples. Never reset Linux notebook data while implementing Ansible.
- Test: add, duplicate, filter, category expansion, open, edit, save, cancel, delete, copy, note add/edit/delete, reference edit/copy, modal staying open after save, immediate card refresh, and reload persistence.
- Verify Topics / Commands / Resources / Projects tabs, sidebar, light/dark mode, mobile layout and browser console. Keep required hidden statistics DOM nodes intact.
- **Parity is an acceptance criterion, not a claim of completion.** If a page is missing a feature, implement and test it before reporting that the page fully matches Linux.

## Ansible Automation progress display
- Hide the progress bar and topic-percentage strip inside the Ansible Automation page header, while keeping its title, icon, level, and hours metadata.
- Do not remove underlying progress calculations or affect the progress display of other technology pages.
- Preserve the existing global stats-bar hiding rule and all Commands notebook functionality.
