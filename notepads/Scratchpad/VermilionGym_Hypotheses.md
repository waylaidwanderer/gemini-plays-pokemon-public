# Vermilion Gym - Trash Can Switch Matrix & Trial Log

## Puzzle Mechanics Analysis
- 15 trash cans arranged in a 3x5 grid:
  - Row 7: (1, 7), (3, 7), (5, 7), (7, 7), (9, 7)
  - Row 9: (1, 9), (3, 9), (5, 9), (7, 9), (9, 9)
  - Row 11: (1, 11), (3, 11), (5, 11), (7, 11), (9, 11)
- Re-entered Gym at Turn 2423.

## Active Run Checklist (Run #2):
- Row 7:
  - [x] (1, 7) - Checked Turn 2424 from (2, 7) facing Left -> Empty
  - [x] (3, 7) - Checked Turn 2425 from (2, 7) facing Right -> Empty
  - [x] (5, 7) - Checked Turn 2435 from (4, 7) facing Right -> Empty
  - [x] (7, 7) - Checked Turn 2436 from (6, 7) facing Right -> Empty
  - [ ] (9, 7) -> **SWITCH 1 CONFIRMED HERE!** (14/15 other cans confirmed empty)
- Row 9:
  - [x] (1, 9) - Checked Turn 2426 from (2, 9) facing Left -> Empty
  - [x] (3, 9) - Checked Turn 2427 from (2, 9) facing Right -> Empty
  - [x] (5, 9) - Checked Turn 2434 from (4, 9) facing Right -> Empty
  - [x] (7, 9) - Checked Turn 2438 from (6, 9) facing Right -> Empty
  - [x] (9, 9) - Checked Turn 2441 from (8, 9) facing Right -> Empty
- Row 11:
  - [x] (1, 11) - Checked Turn 2428 from (2, 11) facing Left -> Empty
  - [x] (3, 11) - Checked Turn 2429 from (2, 11) facing Right -> Empty
  - [x] (5, 11) - Checked Turn 2433 from (4, 11) facing Right -> Empty
  - [x] (7, 11) - Checked Turn 2439 from (6, 11) facing Right -> Empty
  - [x] (9, 11) - Checked Turn 2440 from (8, 11) facing Right -> Empty

## Switch 2 Candidates (Adjacent to (9, 7)):
- West neighbor: (7, 7)
- South neighbor: (9, 9)

## Execution Plan:
1. Turn 2442: Activate Switch 1 at (9, 7) from (8, 7).
2. Turn 2443: Test Switch 2 at (7, 7) (turn Left from 8, 7 and press A).
3. If (7, 7) opens the door -> Challenge Lt. Surge immediately!
4. If (7, 7) resets -> Switch 2 was (9, 9).
