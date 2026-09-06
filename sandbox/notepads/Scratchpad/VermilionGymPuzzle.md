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
- Cycle 6: Switch 1 at (5, 11) [Turn 3432]. Tested adjacent Can (3, 11) -> reset [Turn 3434].
- Cycle 7: Switch 1 at (7, 9) [Turn 3449]. Tested adjacent Can (9, 9) -> reset [Turn 3453].

## Strategic Pivot (Turn 3453)
- Completed 7 consecutive cycles in Vermilion Gym.
- Exited Gym to explore Route 11 and Diglett's Cave for a Ground-type counter before returning.

## Cycle 8 (Turn 3561+)
- DIGBY secured with TM28 Dig (Ground STAB, Electric immune).
- Can (5, 11) tested: empty [Turn 3563].
- Can (3, 11) tested: empty [Turn 3568].
- Can (1, 11) tested: empty [Turn 3570].
- Can (1, 9) tested: empty [Turn 3572].
- Can (3, 9) tested: empty [Turn 3573].
- Can (1, 7) tested: empty [Turn 3574].
- Can (3, 7) tested: empty [Turn 3575].
- Can (5, 7) tested: empty [Turn 3576].
- Can (7, 7) tested: empty [Turn 3577].
- Switch 1 found at Can (9, 7) [Turn 3578]!
- Tested adjacent Can (7, 7) -> reset [Turn 3580].

## Cycle 9 (Turn 3580+)
- Can (7, 7) tested: empty [Turn 3582].
- Can (9, 7) tested: empty [Turn 3583].
- Can (7, 9) tested: empty [Turn 3584].
- Can (9, 9) tested: empty [Turn 3585].
- Can (7, 11) tested: empty [Turn 3586].
- Switch 1 found at Can (9, 11) [Turn 3587]!
- Tested adjacent Can (7, 11) -> reset [Turn 3589].

## Cycle 10 (Turn 3589+)
- Can (7, 11) tested: empty [Turn 3591].
- Can (9, 11) tested: empty [Turn 3592].
- Can (7, 9) tested: empty [Turn 3593].
- Can (9, 9) tested: empty [Turn 3594].
- Can (7, 7) tested: empty [Turn 3595].
- Switch 1 found at Can (9, 7) [Turn 3596]!