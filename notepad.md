# Ice Path B1F Boulder Puzzle
- Goal: Fill all 4 pits with boulders in a single session.
- Reset Trigger: Leaving floor (ladders or falling through pits).

## Strategy: FORCE RESET
1. Current State: Boulders missing from spawn points, pits are active warps.
2. Action: Use ladder at (3, 15) to change floors and force a reset.
3. Return to B1F and visually confirm boulders at (11, 7), (7, 8), (8, 9), (17, 7).
4. Call `puzzle_strategist_v1` and execute pushes without leaving the floor.

## Tile Mechanics
- FLOOR: Walkable.
- WALL: Impassable.
- ICE: Sliding.
- PIT: Warp to B2F. Resets ALL boulders if entered. Must be filled to solve B2F.
- BOULDER: Movable with Strength. Resets on floor change.

## Navigation Notes
- Section 3: (17, 5), (17, 8), (17, 10), (17, 13) are WALLs. Use Column 18/19.
- Row 1 and Row 16: Safe non-ice corridors. Avoid (12, 6) and (11, 11) - they are WALLs.