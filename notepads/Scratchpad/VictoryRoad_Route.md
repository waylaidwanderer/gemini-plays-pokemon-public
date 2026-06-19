# Scratchpad: Victory Road Route & Puzzle States
- Current Turn: 106586
- Current Position: (25, 11) on Map 0_194 (Victory Road 2F East)
- Started Victory Road Navigation: Turn 97592
- Real-World Timestamp: Friday, June 19, 2026 at 8:40 AM PDT

## Goal
Exit Victory Road via 2F East to Route 23 North!

## Active Route to Exit (True Bypass Protocol):
1. Walk back to (23, 7) on 2F East:
   - Walk Left 2 steps from (25, 11) to (23, 11) (2 steps Left).
   - Walk Up 4 steps from (23, 11) to (23, 7) and take the ladder UP to 3F East.
2. Traverse 3F East to the southern ladder at (27, 15):
   - From (23, 7) on 3F East, walk Down Column 23 to Row 13 (6 steps Down).
   - Walk Right along Row 13 to Column 26 (3 steps Right).
   - Walk Down Column 26 to Row 15 (2 steps Down) and take the ladder (27, 15) DOWN to 2F East.
3. On 2F East plateau (z=1), walk to 2F West ground level:
   - Land at (26, 14) [z=1]. Walk Left along Row 14/13 to Column 14 (12 steps Left).
   - Walk Up Column 14 to Row 9 (5 steps Up) and walk Left to Column 13.
   - Walk to the stairs at (5, 10) or descend to ground level on the West side.
4. From 2F West ground level, walk north to Row 2, and walk Right along the northern corridor to the exit at (28, 1) on 2F East.

## Physical Verifications & Proof of Work:
- Turn 106311: Stood at (28, 0) on 3F East, faced UP, and pressed UP. Result: solid collision bump, proving Row 0 Column 28 is impassable.
- Turn 106514: Faced UP at (27, 0) on 3F East and pressed UP. Result: solid collision bump, proving (27, 0) has no exit warp.
- Turn 106521: Stood at (28, 1) on 3F East facing UP. Result: no warp triggered, proving (28, 1) on 3F East has no exit warp.
- Turn 106559: Stood at (23, 7) on 3F East and took the ladder DOWN to 2F East.
- Turn 106584: Tested walking Down from (25, 11) to (25, 12). Result: BUMP (height mismatch), proving Column 25 has an elevation block at Row 12 on ground level.
- Turn 105982: Tested (28, 6) on 2F East and confirmed it was a BUMP (solid rock wall), proving Column 28 is blocked on Row 6.
- Turn 105998: Tested (27, 6) on 2F East and confirmed it was a BUMP (solid rock wall), proving Column 27 is blocked on Row 6.
- Conclusion: Row 6 is completely blocked on 2F East, meaning the northeastern ground pocket (Rows 7-9, Columns 25-28) is completely cut off from Row 11 on ground level. We must use 3F East to reach the ladder at (27, 15) and traverse 2F West to access the northern ground corridor and exit at (28, 1).