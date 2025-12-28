# Ice Path B1F Boulder Puzzle
- Goal: Fill all 4 pits with boulders in a single session.
- Current Session: Started Turn 28627.
- Reset Trigger: Leaving the floor (ladders or falling through pits).

## Hypotheses
1. Boulders reset to fixed spawn points: (11, 7), (7, 8), (8, 9), (17, 7).
2. Pits become traversable on B2F once filled on B1F.

## Observations
- Game State Map Events show all 4 pits as active warps. Conclusion: Boulders have reset.

## Strategy: DECISIVE ACTION
1. Visually confirm all 4 boulders at spawn points.
2. Call `puzzle_strategist_v1` with confirmed coordinates.
3. Execute push sequences without leaving the floor.

## Tile Mechanics
- FLOOR: Walkable.
- WALL: Impassable.
- ICE: Sliding mechanic.
- PIT: Warp to B2F. Resets boulders if entered. Must be filled to solve B2F.
- BOULDER: Movable object. Resets on floor change.

## Navigation Notes
- Section 3 (Right): (17, 5), (17, 8), (17, 10), (17, 13) are WALLs. Use Column 18/19.
- Row 1 and Row 16: Safe non-ice corridors.