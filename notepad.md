# Ice Path B1F Boulder Puzzle
- Goal: Fill all 4 pits with boulders in a single session.
- Reset Trigger: Leaving floor (ladders or falling through pits).
- Status: All 4 pits are currently EMPTY (verified by Game State Map Events).

## Verified Boulder Locations (This Session)
1. Boulder 1: (11, 4) - Visually confirmed (Turn 28962).
2. Boulder 2: UNKNOWN - Searching North.
3. Boulder 3: UNKNOWN - Searching North.
4. Boulder 4: UNKNOWN - Searching North.

## Strategy: DECISIVE ACTION
1. Visually confirm all 4 boulders in the northern area (Rows 0-16).
2. Once all 4 are in the mental map, call `puzzle_strategist_v1` for the solution.
3. Execute push sequences without leaving B1F.

## Tile Mechanics
- FLOOR: Walkable.
- WALL: Impassable.
- ICE: Sliding mechanic.
- PIT: Warp to B2F. Resets ALL boulders if player enters. Must be filled to solve B2F.
- BOULDER: Movable with Strength. Resets on floor change.

## Navigation Notes
- Section 3 (Right): (17, 5), (17, 8), (17, 10), (17, 13) are WALLs. Use Column 18/19.
- Row 1 and Row 16: Safe non-ice corridors. Avoid (12, 6) and (11, 11) - they are WALLs.