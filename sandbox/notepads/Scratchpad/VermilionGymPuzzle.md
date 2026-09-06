# Scratchpad: Vermilion Gym Lock Puzzle

## Clues & Dialogue
- Gym Guide: "LT. SURGE is very cautious! You'll have to break a code to get to him!"

## Structure & Coordinates
- 5x3 Grid of 15 Trash Cans:
  - Rows: 7, 9, 11
  - Cols: 1, 3, 5, 7, 9
- Grid Matrix Map:
  - Row 7:  (1, 7)  (3, 7)  (5, 7)  (7, 7)  (9, 7)
  - Row 9:  (1, 9)  (3, 9)  (5, 9)  (7, 9)  (9, 9)
  - Row 11: (1, 11) (3, 11) (5, 11) (7, 11) (9, 11)
- Aisles:
  - Vertical: cols 0, 2, 4, 6, 8
  - Horizontal: rows 6, 8, 10, 12
- Barrier: Located at rows 4..5 blocking passage to Lt. Surge.

## Empirical Testing Log
- Attempt 1:
  - Found Switch 1 at Can (1, 11) [Turn 3319].
  - Tested adjacent Can (1, 9) while Switch 1 active [Turn 3323] -> Only trash, locks reset.
- Attempt 2:
  - Found Switch 1 at Can (1, 11) [Turn 3329].
  - Tested Can (1, 7) while Switch 1 active [Turn 3331] -> Only trash, locks reset.
- Attempt 3 (Current):
  - Testing Can (1, 11) on Turn 3331 to observe if Switch 1 persists or re-rolls.
  - If Switch 1 is at (1, 11), adjacent untested can while active is (3, 11).
- Can (1, 11): Checked Turn 3336 -> Only trash. (Switch 1 re-rolled).
- Can (3, 11): Inspecting Turn 3336.
- Can (3, 11): Checked Turn 3337 -> Only trash.
- Can (5, 11): Inspecting Turn 3337.
- Can (5, 11): Checked Turn 3338 -> Only trash.
- Can (7, 11): Inspecting Turn 3338.
- Can (7, 11): Checked Turn 3339 -> Only trash.
- Can (9, 11): Inspecting Turn 3339.
- Can (9, 11): Checked Turn 3341 -> Only trash. (All Row 11 cans empty in Cycle 2).
- Can (9, 9): Inspecting Turn 3341.
