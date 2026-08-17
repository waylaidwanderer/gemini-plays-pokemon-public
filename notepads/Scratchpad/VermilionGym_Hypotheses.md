# Vermilion Gym - Trash Can Switch Matrix & Trial Log

## Puzzle Mechanics (Empirical)
- 15 trash cans arranged in a 3x5 grid:
  - Row 7: (1, 7), (3, 7), (5, 7), (7, 7), (9, 7)
  - Row 9: (1, 9), (3, 9), (5, 9), (7, 9), (9, 9)
  - Row 11: (1, 11), (3, 11), (5, 11), (7, 11), (9, 11)
- Switch 1 is chosen randomly upon map entry / after failing Switch 2.
- Once Switch 1 is found and activated, Switch 2 is located in an immediately adjacent trash can (North, South, East, or West).
- If an incorrect can is inspected while searching for Switch 2, the locks reset and Switch 1 re-randomizes.

## Active Run Checklist (Current Attempt: Turn 2400+)
- Row 7:
  - [ ] (1, 7)
  - [ ] (3, 7)
  - [ ] (5, 7)
  - [ ] (7, 7)
  - [ ] (9, 7)
- Row 9:
  - [x] (1, 9) - Checked Turn 2409 from (2, 9) facing Left -> Empty ("Nope, there's only trash here.")
  - [x] (3, 9) - Checked Turn 2410 from (2, 9) facing Right -> Empty ("Nope, there's only trash here.")
  - [x] (5, 9) - Checked Turn 2411 from (4, 9) facing Right -> Empty ("Nope, there's only trash here.")
  - [x] (7, 9) - Checked Turn 2412 from (6, 9) facing Right -> Empty ("Nope, there's only trash here.")
  - [x] (9, 9) - Checked Turn 2413 from (8, 9) facing Right -> Empty ("Nope, there's only trash here.")
- Row 11:
  - [x] (1, 11) - Checked Turn 2408 from (2, 11) facing Left -> Empty ("Nope, there's only trash here.")
  - [x] (3, 11) - Checked Turn 2407 from (4, 11) facing Left -> Empty ("Nope, there's only trash here.")
  - [x] (5, 11) - Checked Turn 2406 from (6, 11) facing Left -> Empty ("Nope, there's only trash here.")
  - [x] (7, 11) - Checked Turn 2402 from (8, 11) facing Left -> Empty ("Nope, there's only trash here.")
  - [x] (9, 11) - Checked Turn 2400 from (8, 11) facing Right -> Empty ("Nope, there's only trash here.")

## Current Deduction:
- Rows 9 and 11 are 100% empty. Switch 1 MUST be located in Row 7 ((1,7), (3,7), (5,7), (7,7), or (9,7)).

## Next Planned Checks:
- Turn 2414: Inspect (9, 7) from (8, 7) facing Right.
