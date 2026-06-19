# Scratchpad: Victory Road Route & Puzzle States
- Turn 106772: Standing at (27, 8) on Map 0_198 (Victory Road 3F East)
- Real-World Timestamp: Friday, June 19, 2026 at 9:35 AM PDT

## Goal
Exit Victory Road via 2F East to Route 23 North!

## Active Route to Exit (True 2F East Plateau Bypass):
1. Step Left onto the ladder at (26, 8) on 3F East to go DOWN to 2F East.
2. Walk north on 2F East from (27, 7) to the exit doorway at (28, 1) on 2F East!

## Detailed Step-by-Step Pathing Verification:
- **Phase 1 (Plateau Crossover on 2F East)**:
  - From (13, 8) on the 2F East plateau, we verified that Column 14 is blocked on the north side at Row 7 by a solid rock wall of TYPE_2889.
  - We walked South along Column 14 to Row 13: (13, 8) -> (14, 8) -> (14, 13).
  - Walked East on the plateau Row 13 towards the ladder. Juggler NPC at (21, 13) blocked Row 13 directly.
  - Detoured around Juggler by stepping Down to Row 14: (20, 13) -> (20, 14) -> (24, 14).
  - Climbed the plateau ladder at (25, 14) to 3F East, landing at (27, 15) on 3F East.
- **Phase 2 (3F East Vertical Corridor)**:
  - Landed at (27, 15) facing DOWN.
  - Walked North along Column 27 to (27, 8): (27, 15) -> (27, 11) -> (27, 8).
  - Encountered a wild Onix at (27, 8), fled successfully.
  - We are now positioned at (27, 8) facing DOWN, with the 3F East ladder at (26, 8) directly to our Left.

## Physical Verifications & Proof of Work:
- Turn 106311: Stood at (28, 0) on 3F East, faced UP, and pressed UP. Result: solid collision bump, proving Row 0 Column 28 is impassable.
- Turn 106514: Faced UP at (27, 0) on 3F East and pressed UP. Result: solid collision bump, proving (27, 0) has no exit warp.
- Turn 106521: Stood at (28, 1) on 3F East facing UP. Result: no warp triggered, proving (28, 1) on 3F East has no exit warp.
- Turn 106559: Stood at (23, 7) on 3F East and took the ladder DOWN to 2F East.
- Turn 106584: Tested walking Down from (25, 11) to (25, 12). Result: BUMP (height mismatch), proving Column 25 has an elevation block at Row 12 on ground level.
- Turn 105982: Tested (28, 6) on 2F East and confirmed it was a BUMP (solid rock wall), proving Column 28 is blocked on Row 6.
- Turn 105998: Tested (27, 6) on 2F East and confirmed it was a BUMP (solid rock wall), proving Column 27 is blocked on Row 6.
- Turn 106598: Verified visually that Column 23 Row 9 on 3F East is blocked by solid wall of TYPE_2889, requiring us to detour via the Western ground corridor (Column 14) on 3F East.
- Turn 106760: Confirmed visually that player is standing at (19, 13) facing Right on 2F East on the plateau. Juggler is at (21, 13). (20, 13) is open, (20, 14) is open, (21, 14) is open, (22, 14) is open, (23, 14) is open, (24, 14) is open. We can bypass Juggler by stepping Down to Row 14 and walking Right.
- Conclusion: The exit warp is definitively on 2F East at (28, 1), and we must use the True Bypass Protocol via 3F East, the (27, 15) ladder, 2F East plateau Column 15, and 2F East Row 1 to reach the exit safely.