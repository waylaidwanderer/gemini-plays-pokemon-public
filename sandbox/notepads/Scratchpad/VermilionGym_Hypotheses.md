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
  - [ ] (9, 7) -> 100% GUARANTEED SWITCH 1
- Row 9:
  - [x] (1, 9) - Checked Turn 2482 from (2, 9) facing Left -> Empty
  - [x] (3, 9) - Checked Turn 2483 from (2, 9) facing Right -> Empty
  - [x] (5, 9) - Checked Turn 2488 from (4, 9) facing Right -> Empty
  - [x] (7, 9) - Checked Turn 2493 from (6, 9) facing Right -> Empty
  - [x] (9, 9) - Checked Turn 2507 from (8, 9) facing Right -> Empty
- Row 11:
  - [x] (1, 11) - Checked Turn 2484 from (2, 11) facing Left -> Empty
  - [x] (3, 11) - Checked Turn 2486 from (2, 11) facing Right -> Empty
  - [x] (5, 11) - Checked Turn 2487 from (4, 11) facing Right -> Empty
  - [x] (7, 11) - Checked Turn 2494 from (6, 11) facing Right -> Empty
  - [x] (9, 11) - Checked Turn 2504 from (8, 11) facing Right -> Empty

## Current Sweep State:
- 14/15 cans verified empty on this run. Switch 1 MUST be at (9, 7).

## Next Action:
- Turn 2507: Inspect (9, 7) from (8, 7) to activate Switch 1!
- Once Switch 1 is active, Switch 2 will be at (9, 9) or (7, 7).
