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
- Aisles: Vertical (cols 0, 2, 4, 6, 8), Horizontal (rows 6, 8, 10, 12)
- Barrier: Located at rows 4..5 blocking passage to Lt. Surge.
- All 3 Gym Trainers Defeated: Rocker at (3, 8), Sailor at (2, 10), Gentleman at (9, 6).

## Verified Empirical Observations
1. Inspecting an empty can: "Nope, there's only trash here."
2. Finding Switch 1: "Hey! There's a switch under the trash! Turn it on! The 1st electric lock opened!"
3. Inspecting a non-switch can while Switch 1 is active: "Nope! There's only trash here. Hey! The electric locks were reset!"
   - Confirmed: When locks reset, Switch 1 re-rolls to a can.

## Compressed History of Completed Cycles
- Cycle 1: Switch 1 at (1, 11) [Turn 3319]. Tested (1, 9) -> reset [Turn 3323].
- Cycle 2: Switch 1 at (1, 11) [Turn 3329]. Tested non-adjacent (1, 7) -> reset [Turn 3333].
- Cycle 3: Switch 1 at (1, 7) [Turn 3354]. Tested (1, 9) -> reset [Turn 3356].
- Cycle 4: Switch 1 at (3, 9) [Turn 3371]. Tested (3, 11) -> reset [Turn 3372].
- Cycle 5: Switch 1 at (1, 7) [Turn 3410]. Tested (3, 7) -> reset [Turn 3414].

## Active Cycle 6 (Current)
- Can (3, 7): Tested [Turn 3418] -> Only trash.
- Can (1, 7): Tested [Turn 3419] -> Only trash.
- Can (5, 7): Tested [Turn 3423] -> Only trash.
- Can (7, 7): Tested [Turn 3424] -> Only trash.
- Can (9, 7): Tested [Turn 3425] -> Only trash. (All 5 Row 7 cans empty).
- Can (9, 9): Tested [Turn 3427] -> Only trash.
- Can (7, 9): Tested [Turn 3428] -> Only trash.
- Can (9, 11): Tested [Turn 3429] -> Only trash.
- Can (7, 11): Tested [Turn 3430] -> Only trash. (Columns 7 and 9 fully empty).
- Can (5, 11): Switch 1 FOUND! [Turn 3432]
- 1st electric lock opened!
- Adjacent cans for Switch 2:
  - Can (3, 11) [West]
  - Can (5, 9) [North]
  - Can (7, 11) [East]