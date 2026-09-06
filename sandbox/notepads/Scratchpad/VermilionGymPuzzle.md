# Scratchpad: Vermilion Gym Lock Puzzle

## Clues & Gym Floor Layout
- Gym Guide: "LT. SURGE is very cautious! You'll have to break a code to get to him!"
- 15 Trash Cans in 5x3 Grid:
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
- All 3 Gym Trainers Defeated: Rocker at (3, 8), Sailor at (0, 10), Gentleman at (9, 6).

## Verified Empirical Mechanics
1. Inspecting an empty can: "Nope, there's only trash here."
2. Finding Switch 1: "Hey! There's a switch under the trash! Turn it on! The 1st electric lock opened!"
3. Finding Switch 2: Must be in a cardinally adjacent can while Switch 1 is active.
4. Failing Switch 2: "Nope! There's only trash here. Hey! The electric locks were reset!"
   - When locks reset, Switch 1 re-rolls to a random can.
   - Any adjacent can can be Switch 2 (prior testing before Switch 1 was active does not invalidate an adjacent can).

## Switch 1 History
- Cycle 1: Found at (1, 11) [Turn 3319]. Tested (1, 9) -> reset [Turn 3323].
- Cycle 2: Found at (1, 11) [Turn 3329]. Tested (1, 7) -> reset [Turn 3331/3333].
- Cycle 3: Found at (1, 7) [Turn 3354]. Tested (1, 9) -> reset [Turn 3356].
- Cycle 4 (Current): Testing Can (1, 9) at (0, 9) facing East on Turn 3357.
- Can (1, 9): Checked Turn 3359 -> Only trash.
- Can (1, 7): Inspecting Turn 3359.
