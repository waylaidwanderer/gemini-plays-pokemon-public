# Vermilion Gym - Trash Can Switch Matrix & Empirical Trial Log

## Empirical Engine Analysis (Reconciled Turn 2461)
- wFirstTrashCan is FIXED upon map entry / lock reset, and is NOT re-rolled by inspecting an empty can.
- Switch 1 resides in one specific trash can for the duration of the current search cycle.
- Once Switch 1 is triggered, Switch 2 is assigned to an adjacent can (North, South, East, or West).
- If Switch 2 fails, locks reset and a new Switch 1 is selected.

## Complete 15-Can Systematic Manual Sweep (Active):
- Row 7:
  - [ ] (1, 7)
  - [ ] (3, 7)
  - [x] (5, 7) - Checked Turn 2471 from (6, 7) facing Left -> Empty
  - [x] (7, 7) - Checked Turn 2464 from (8, 7) facing Left -> Empty
  - [x] (9, 7) - Checked Turn 2463 from (8, 7) facing Right -> Empty
- Row 9:
  - [ ] (1, 9)
  - [ ] (3, 9)
  - [x] (5, 9) - Checked Turn 2470 from (6, 9) facing Left -> Empty
  - [x] (7, 9) - Checked Turn 2465 from (8, 9) facing Left -> Empty
  - [x] (9, 9) - Checked Turn 2466 from (8, 9) facing Right -> Empty
- Row 11:
  - [ ] (1, 11)
  - [ ] (3, 11)
  - [x] (5, 11) - Checked Turn 2469 from (6, 11) facing Left -> Empty
  - [x] (7, 11) - Checked Turn 2468 from (8, 11) facing Left -> Empty
  - [x] (9, 11) - Checked Turn 2467 from (8, 11) facing Right -> Empty

## Current Deduction:
- Columns 5, 7, and 9 are 100% empty (9/15 checked). Switch 1 is in Columns 1 or 3 (6 candidates remaining).

## Next Action:
- Turn 2472: Inspect (3, 7) from (4, 7) facing Left.
