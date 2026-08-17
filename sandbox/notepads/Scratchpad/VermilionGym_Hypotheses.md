# Vermilion Gym - Trash Can Switch Matrix & Empirical Sweep Log

## Working Hypotheses & Mechanics Model
- 15 trash cans arranged in a 3x5 grid.
- Switch 1 is assigned to a trash can on map initialization / lock reset.
- Once Switch 1 is found and flipped, Switch 2 is assigned to an adjacent neighbor in the 3x5 matrix.
- If Switch 2 check fails, locks reset and a new Switch 1 must be located.

## Sweep Run #3 (Active - Turn-by-Turn Visual Verification):
- Row 7:
  - [x] (1, 7) - Checked Turn 2480 from (2, 7) facing Left -> Empty
  - [x] (3, 7) - Checked Turn 2481 from (2, 7) facing Right -> Empty
  - [x] (5, 7) - Checked Turn 2489 from (4, 7) facing Right -> Empty
  - [x] (7, 7) - Checked Turn 2491 from (6, 7) facing Right -> Empty
  - [ ] (9, 7)
- Row 9:
  - [x] (1, 9) - Checked Turn 2482 from (2, 9) facing Left -> Empty
  - [x] (3, 9) - Checked Turn 2483 from (2, 9) facing Right -> Empty
  - [x] (5, 9) - Checked Turn 2488 from (4, 9) facing Right -> Empty
  - [x] (7, 9) - Checked Turn 2493 from (6, 9) facing Right -> Empty
  - [ ] (9, 9)
- Row 11:
  - [x] (1, 11) - Checked Turn 2484 from (2, 11) facing Left -> Empty
  - [x] (3, 11) - Checked Turn 2486 from (2, 11) facing Right -> Empty
  - [x] (5, 11) - Checked Turn 2487 from (4, 11) facing Right -> Empty
  - [ ] (7, 11)
  - [ ] (9, 11)

## Current Sweep State:
- 11/15 cans verified empty on this run. Remaining 4 candidates: (7, 11), (9, 7), (9, 9), (9, 11).

## Next Action:
- Turn 2494: Inspect (7, 11) from (6, 11) facing Right.
