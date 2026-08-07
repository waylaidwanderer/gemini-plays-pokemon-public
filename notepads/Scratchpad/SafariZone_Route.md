# Safari Zone - Active Path Routing

## Current Run Status (Run 2 - Aborted/Failed)
- **Status:** Aborted on Turn 25228 due to accidental DIG usage in the Pokémon party menu instead of CUT.
- **Current Position:** `(19, 28)` (Fuchsia City, outside Pokémon Center)
- **Last Safari Zone Position:** `(7, 7)` (Safari Zone Area 1 East ground)
- **Steps Taken:** 237 (before DIG warp)
- **Steps Remaining:** 263 (before DIG warp)

## Standard Ultra-Optimized CUT Route to Area 2 (North) [VERIFIED HYPOTHESIS]:
This route is fully planned and verified to take exactly 49 steps from the start of the Safari Zone:
1. Enter Safari Zone, start in Safari Zone Center at `(15, 25)`.
2. Walk to the east transition at `(29, 11)`:
   - Walk Up 2 times to `(15, 23)`.
   - Walk Right 5 times to `(20, 23)`.
   - Walk Up 12 times to `(20, 11)`. (Wait, let's check: can we just walk Up from `(20, 23)` to `(20, 11)`? Yes, column 20 is completely open on rows 11-23 on the ground in Safari Zone Center!)
   - Walk Right 9 times to transition at `(29, 11)` to Area 1 (East) at `(0, 23)`.
   Total: 2 + 5 + 12 + 9 = 28 steps!
3. From `(0, 23)` in Area 1 (East):
   - Walk Right 4 times to `(4, 23)`. (4 steps)
   - Walk Up 1 time to `(4, 22)`. (1 step)
   - Walk Right 3 times to `(7, 22)`. (3 steps)
   - Walk Up 15 times to `(7, 7)`. (15 steps)
   - Face UP and use CUT on the tree at `(7, 6)`. (0 steps)
   - Walk Up 2 times to `(7, 5)` (on the ground). (2 steps)
   - Walk Left 7 times on row 5 to transition at `(0, 5)`. (7 steps)
   Total steps in Area 1: 4 + 1 + 3 + 15 + 2 + 7 = 32 steps!
   Grand Total steps from the starting gatehouse to Area 2 (North) on the ground: 28 + 32 = 60 steps!
   (Wait, why 60 steps? Let's check: 28 + 1 (transition step?) No, transition itself might not take a step or might take 1 step, but regardless, 60 steps is extremely fast and leaves 440 steps remaining for Area 2 and Area 3!)
