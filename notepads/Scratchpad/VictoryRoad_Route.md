# Scratchpad: Victory Road Route & Puzzle States
- Turn 106741: Standing at (13, 8) on Map 0_194 (Victory Road 2F East)
- Real-World Timestamp: Friday, June 19, 2026 at 9:26 AM PDT

## Goal
Exit Victory Road via 2F East to Route 23 North!

## Active Route to Exit (True 2F East Plateau Bypass):
1. Return to 2F East via the (23, 7) ladder:
   - Walk Up Column 14 to Row 6: (14, 10) -> (14, 6) [4 steps Up].
   - Walk Right along Row 6 to Column 23: (14, 6) -> (23, 6) [9 steps Right].
   - Walk Down Column 23 to the ladder at (23, 7): (23, 6) -> (23, 7) [1 step Down].
   - Take the ladder DOWN to 2F East.
2. On 2F East, navigate to the plateau via the southeastern stairs:
   - Land at (23, 7) [z=0]. Walk Down Column 23 to Row 11: (23, 7) -> (23, 11) [4 steps Down].
   - Walk Right along Row 11 through the open gate at (24, 11) to Column 28: (23, 11) -> (28, 11) [5 steps Right].
   - Walk Down Column 28 to Row 16: (28, 11) -> (28, 16) [5 steps Down].
   - Walk Left along Row 16 to Column 24: (28, 16) -> (24, 16) [4 steps Left].
   - Walk Down to Row 17 to bypass the boulder at (23, 16): (24, 16) -> (24, 17) [1 step Down].
   - Walk Left along Row 17 to Column 21: (24, 17) -> (21, 17) [3 steps Left].
   - Walk Up Column 21 to the stairs at (21, 15): (21, 17) -> (21, 15) [2 steps Up] (climbs onto plateau z=1).
3. On the 2F East plateau, walk to the exit:
   - From (21, 15) [z=1], walk Up to Row 13: (21, 15) -> (21, 13) [2 steps Up].
   - Walk Left along Row 13 on the plateau to Column 14: (21, 13) -> (14, 13) [7 steps Left].
   - Walk Up Column 14 to Row 1: (14, 13) -> (14, 1) [12 steps Up].
   - Walk Right along Row 1 to the exit at (28, 1) on 2F East: (14, 1) -> (28, 1) [14 steps Right].

## Physical Verifications & Proof of Work:
- Turn 106311: Stood at (28, 0) on 3F East, faced UP, and pressed UP. Result: solid collision bump, proving Row 0 Column 28 is impassable.
- Turn 106514: Faced UP at (27, 0) on 3F East and pressed UP. Result: solid collision bump, proving (27, 0) has no exit warp.
- Turn 106521: Stood at (28, 1) on 3F East facing UP. Result: no warp triggered, proving (28, 1) on 3F East has no exit warp.
- Turn 106559: Stood at (23, 7) on 3F East and took the ladder DOWN to 2F East.
- Turn 106584: Tested walking Down from (25, 11) to (25, 12). Result: BUMP (height mismatch), proving Column 25 has an elevation block at Row 12 on ground level.
- Turn 105982: Tested (28, 6) on 2F East and confirmed it was a BUMP (solid rock wall), proving Column 28 is blocked on Row 6.
- Turn 105998: Tested (27, 6) on 2F East and confirmed it was a BUMP (solid rock wall), proving Column 27 is blocked on Row 6.
- Turn 106598: Verified visually that Column 23 Row 9 on 3F East is blocked by solid wall of TYPE_2889, requiring us to detour via the Western ground corridor (Column 14) on 3F East.
- Conclusion: The exit warp is definitively on 2F East at (28, 1), and we must use the True Bypass Protocol via 3F East, the (27, 15) ladder, 2F East plateau Column 15, and 2F East Row 1 to reach the exit safely.