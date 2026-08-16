# Vermilion Gym - Switch Puzzle Log & Strategy

## Puzzle Mechanics (Gen 1 Red/Blue)
- 15 Trash Cans in 5x3 Grid across rows 7, 9, 11 (cols 1, 3, 5, 7, 9).
- Switch 1 is randomly assigned upon gym entry and re-randomized upon any failed Switch 2 check.
- When Switch 1 is found at (cx, cy), Switch 2 is guaranteed to be in one of the cardinally adjacent cans.
- Success requires activating Switch 1 and immediately checking the correct adjacent can.

## Serpentine Search Order
1. Can (1, 7) [0, 7 R]
2. Can (1, 9) [0, 9 R]
3. Can (1, 11) [0, 11 R]
4. Can (3, 11) [4, 11 L]
5. Can (3, 9) [4, 9 L]
6. Can (3, 7) [4, 7 L]
7. Can (5, 7) [4, 7 R]
8. Can (5, 9) [4, 9 R]
9. Can (5, 11) [4, 11 R]
10. Can (7, 11) [6, 11 R]
11. Can (7, 9) [6, 9 R]
12. Can (7, 7) [6, 7 R]
13. Can (9, 7) [8, 7 R]
14. Can (9, 9) [8, 9 R]
15. Can (9, 11) [8, 11 R]

## Trial History
- Turn 2258: Switch 1 found at Can (5, 11). Tested neighbor (3, 11) -> Failed/Reset on Turn 2260.
- Current Cycle: Can (1, 7) = Trash [Turn 2283], Can (1, 9) = Trash [Turn 2284], Can (1, 11) = Trash [Turn 2285], Can (3, 11) = Trash [Turn 2286], Can (3, 9) = Trash [Turn 2287], Can (3, 7) = Trash [Turn 2288], Can (5, 7) = Trash [Turn 2289], Can (5, 9) = Trash [Turn 2290], Can (5, 11) = Trash [Turn 2291]. Testing Can (7, 11).
