# Ice Path B1F Boulder Puzzle
- Start Turn: 28627 | Start Time: Sunday, Dec 28, 5:32 AM
- Current Turn: 28957 | Current Time: Sunday, Dec 28, 8:02 AM
- Goal: Fill all 4 pits with boulders in a single session.
- Reset Trigger: Leaving floor or falling through pits.
- Status: All 4 pits are currently EMPTY (verified by Map Events).

## Boulder Spawn Points
1. Boulder 1: (11, 7)
2. Boulder 2: (7, 8)
3. Boulder 3: (8, 9)
4. Boulder 4: (17, 7)

## Strategy
1. Navigate to each spawn point to visually confirm boulders.
2. Once all 4 are in the mental map, call `puzzle_strategist_v1`.
3. Execute push sequences without leaving B1F.

## Tile Mechanics
- FLOOR: Walkable.
- WALL: Impassable.
- ICE: Sliding.
- PIT: Warp to B2F. Resets boulders. Must be filled.
- BOULDER: Movable with Strength. Resets on floor change.

## Navigation
- Section 3: (17, 5), (17, 8), (17, 10), (17, 13) are WALLs. Use Column 18/19.
- Row 1 and Row 16: Safe non-ice corridors.