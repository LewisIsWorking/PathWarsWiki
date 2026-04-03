# Chevron Lists v2.3.0 — Full Test Suite

Reload Window first (Ctrl+Shift+P → Reload Window)

---

## TEST 1 — Outline View
Open View → Outline. Sections below should appear with item counts.
Expand OutlineTest_Alpha — should show 3 children.
Click BetaNumbered_One — cursor should jump to that line.
Write result:


> OutlineTest_Alpha
>> - AlphaItem_One
>> - AlphaItem_Two
>> - AlphaItem_Three

> OutlineTest_Beta
>> 1. BetaNumbered_One
>> 2. BetaNumbered_Two

---

## TEST 2 — File Statistics
Run: CL: Show File Statistics
Panel should show: 8 sections (this file), item counts, word counts, avg items/section.
Write result:


---

## TEST 3 — Insert Template
Run: CL: Insert Template → select "Session Notes"
Should expand with Tab stops.
Write result:


---

## TEST 4 — Search Items (Workspace)
Run: CL: Search Items (Workspace)
Type "AlphaItem" — should show items from this file.
Write result:


---

## TEST 5 — Filter Sections (Workspace)
Run: CL: Filter Sections (Workspace)
Type "Beta" — should show OutlineTest_Beta.
Write result:


---

## TEST 6 — Colour Preset
Run: CL: Switch Colour Preset → select "Sunset"
Headers below should turn coral/red.
Write result:

> SunsetTestHeader
>> - SunsetItem

Run again → select "Default" to restore.

---

## TEST 7 — Diagnostics
Look at the Problems panel (View → Problems).
The empty section below should show an Information diagnostic.
The duplicate header should show an Information diagnostic.
The bad numbering should show a Warning diagnostic.
Write result:

> EmptySection

> DuplicateHeader
>> - item one

> DuplicateHeader
>> - item two

> NumberingTest
>> 1. first
>> 3. skipped two

---

## TEST 8 — Fix Numbering
Place cursor anywhere in the NumberingTest section above.
Run: CL: Fix Numbering
The "3. skipped two" line should correct itself to "2. skipped two".
Write result:


---

## TEST 9 — Filter by Tag
The items below have #tags.
Run: CL: Filter by Tag
Select "#urgent" — should show the two urgent items with live preview.
Write result:

> TagTestSection
>> - Deploy server #urgent #backend
>> - Review PR #urgent
>> - Update docs #low-priority
>> - Fix tests #backend

---

## TEST 10 — Linked Sections
Hover over [[OutlineTest_Alpha]] — should show a preview of Alpha's items.
Press F12 on [[OutlineTest_Alpha]] — should jump to that header.
Hover over [[NonExistentSection]] — should show a warning.
Write result:

> LinksTestSection
>> - See [[OutlineTest_Alpha]] for context
>> - Also check [[OutlineTest_Beta]]
>> - Broken link [[NonExistentSection]]

---
