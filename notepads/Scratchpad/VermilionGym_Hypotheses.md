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
  - [ ] (5, 7)
  - [x] (7, 7) - Checked Turn 2464 from (8, 7) facing Left -> Empty
  - [x] (9, 7) - Checked Turn 2463 from (8, 7) facing Right -> Empty
- Row 9:
  - [ ] (1, 9)
  - [ ] (3, 9)
  - [ ] (5, 9)
  - [ ] (7, 9)
  - [ ] (9, 9)
- Row 11:
  - [ ] (1, 11)
  - [ ] (3, 11)
  - [ ] (5, 11)
  - [ ] (7, 11)
  - [ ] (9, 11)

## Next Action:
- Turn 2465: Inspect (7, 9) from (8, 9) facing Left.
