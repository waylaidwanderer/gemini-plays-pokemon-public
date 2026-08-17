# Vermilion Gym - Trash Can Switch Matrix & Empirical Trial Log

## Empirical Engine Analysis (Reconciled Turn 2461)
- wFirstTrashCan is FIXED upon map entry / lock reset, and is NOT re-rolled by inspecting an empty can.
- Switch 1 resides in one specific trash can for the duration of the current search cycle.
- Once Switch 1 is triggered, Switch 2 is assigned to an adjacent can (North, South, East, or West).
- If Switch 2 fails, locks reset and a new Switch 1 is selected.

## Complete 15-Can Systematic Manual Sweep (Active):
- Row 7:
  - [x] (1, 7) - Checked Turn 2473 from (2, 7) facing Left -> Empty
  - [x] (3, 7) - Checked Turn 2472 from (4, 7) facing Left -> Empty
  - [x] (5, 7) - Checked Turn 2471 from (6, 7) facing Left -> Empty
  - [x] (7, 7) - Checked Turn 2464 from (8, 7) facing Left -> Empty
  - [x] (9, 7) - Checked Turn 2463 from (8, 7) facing Right -> Empty
- Row 9:
  - [x] (1, 9) - Checked Turn 2474 from (2, 9) facing Left -> Empty
  - [x] (3, 9) - Checked Turn 2475 from (2, 9) facing Right -> Empty
  - [x] (5, 9) - Checked Turn 2470 from (6, 9) facing Left -> Empty
  - [x] (7, 9) - Checked Turn 2465 from (8, 9) facing Left -> Empty
  - [x] (9, 9) - Checked Turn 2466 from (8, 9) facing Right -> Empty
- Row 11:
  - [x] (1, 11) - Checked Turn 2476 from (2, 11) facing Left -> Empty
  - [ ] (3, 11) -> **SWITCH 1 IS 100% HERE!** (14/15 other cans confirmed empty)
  - [x] (5, 11) - Checked Turn 2469 from (6, 11) facing Left -> Empty
  - [x] (7, 11) - Checked Turn 2468 from (8, 11) facing Left -> Empty
  - [x] (9, 11) - Checked Turn 2467 from (8, 11) facing Right -> Empty

## Switch 2 Candidates (Adjacent to (3, 11)):
- West neighbor: (1, 11) (turn Left from 2, 11)
- North neighbor: (3, 9) (step Up 2 to 2, 9 and face Right)
- East neighbor: (5, 11) (step via row 12 to 4, 11 and face Right)

## Next Action:
- Turn 2477: Activate Switch 1 at (3, 11) from (2, 11) facing Right.
