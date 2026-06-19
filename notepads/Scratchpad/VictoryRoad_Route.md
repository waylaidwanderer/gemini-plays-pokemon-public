# Scratchpad: Victory Road Route & Puzzle States
- Turn 106651: Standing at (21, 5) on Map 0_198 (Victory Road 3F East)
- Real-World Timestamp: Friday, June 19, 2026 at 9:02 AM PDT

## Goal
Exit Victory Road via 2F East to Route 23 North!

## Active Route to Exit (True Bypass Protocol):
1. Traverse 3F East to the southern ladder at (27, 15) via Western Bypass:
   - From (23, 2), walk Up 1 step to Row 1, and walk Left to Column 14 (9 steps Left).
   - Walk Down Column 14 to Row 13 (12 steps Down).
   - Walk Right along Row 13 to Column 26 (12 steps Right).
   - Walk Down Column 26/27 to the ladder at (27, 15) (2 steps Down) and take the ladder DOWN to 2F East.
2. On 2F East plateau (z=1), walk to 2F West ground level:
   - Land at (26, 14) [z=1]. Walk Left along Row 14/13/12 on the plateau to Column 14.
   - Walk Up Column 14 to Row 1 (13 steps Up).
   - Walk Right along Row 1 to Column 28 (13 steps Right) to reach the exit at (28, 1) on 2F East.

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