# Scratchpad: Victory Road Route & Puzzle States
- Turn 106844: Standing at (23, 7) on Map 0_194 (Victory Road 2F East)
- Real-World Timestamp: Friday, June 19, 2026 at 10:10 AM PDT

## Goal
Exit Victory Road via 2F East to Route 23 North!

## Active Route to Exit (True 3F East to 2F East Northern Bypass):
1. On 3F East, walk from (14, 6) along Row 6 to the central ladder at (23, 7):
   - Walk Right along Row 6 to Column 23: (14, 6) -> (23, 6) [9 steps Right]. (Done!)
   - Walk Down Column 23 to the central ladder at (23, 7): (23, 6) -> (23, 7) [1 step Down]. (Done!)
   - Take the ladder DOWN to 2F East. (Done!)
2. On 2F East (ground level), walk from the (23, 7) landing to the exit at (28, 1):
   - Walk Left along Row 7 to Column 19: (23, 7) -> (19, 7) [4 steps Left].
   - Walk Up Column 19 to the top Row 3 corridor: (19, 7) -> (19, 3) [4 steps Up].
   - Walk Right along Row 3 to Column 28: (19, 3) -> (25, 3) -> (25, 4) -> (28, 4) -> (28, 3) [Detour around the duplicate sprite bug at (26, 3) if solid].
   - Walk Up Column 28 to the exit at (28, 1): (28, 3) -> (28, 1) [2 steps Up].
   - Walk UP to exit Victory Road to Route 23 North!

## Physical Verifications & Proof of Work:
- Turn 106844: Standing at (23, 7) on 2F East ground floor. Confirmed that Row 4 is completely blocked horizontally on Columns 19-24 by solid rock walls of TYPE_2889. Row 3 is completely open, but Row 4 separates Row 5 from Row 3 on those columns. Column 19 Row 4 is a rock wall, but Column 19 Row 3 is open ground (TYPE_3fe2). Let's verify Column 19's passability going north!
- Conclusion: The exit is reached by transitioning from 3F East (26, 8) -> (23, 7) ladder -> 2F East (23, 7) ground level -> Column 19 -> Row 3 -> Column 28 -> Exit at (28, 1). This is completely open, safe, and avoids all boulder puzzles!