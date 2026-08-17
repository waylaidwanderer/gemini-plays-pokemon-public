# Vermilion Gym - Trash Can Switch Matrix & Trial Log

## Puzzle Mechanics Analysis
- 15 trash cans arranged in a 3x5 grid:
  - Row 7: (1, 7), (3, 7), (5, 7), (7, 7), (9, 7)
  - Row 9: (1, 9), (3, 9), (5, 9), (7, 9), (9, 9)
  - Row 11: (1, 11), (3, 11), (5, 11), (7, 11), (9, 11)
- Re-entered Gym at Turn 2423 to initialize fresh Switch 1 state.

## Systematic Check Plan (Run #2):
1. Check (1, 7) from (2, 7) facing Left.
   - If Switch 1 -> Test (3, 7) or (1, 9) for Switch 2.
2. If (1, 7) is empty -> Check (3, 7) from (2, 7) facing Right.
   - If Switch 1 -> Test (1, 7), (5, 7), or (3, 9) for Switch 2.
3. If (3, 7) is empty -> Continue systematic sweep across remaining cans.
