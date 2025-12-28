# Ice Path B1F Boulder Puzzle
- Puzzle Start Turn: 28986 (Returned from B2F)
- Goal: Fill all 4 pits with boulders in a single session.
- Reset Trigger: Leaving floor (ladders or falling through pits).
- Strategy: Verify all 4 boulders at spawn points, then use puzzle_strategist_v1.

## Boulder Search Status
- Boulder 1: Spawn Point (11, 7) - Checking...
- Boulder 2: Spawn Point (5, 7) - Checking...
- Boulder 3: Spawn Point (8, 9) - Checking...
- Boulder 4: Spawn Point (17, 7) - Checking...

## Tile Mechanics
- FLOOR: Walkable.
- WALL: Impassable.
- PIT: Warp to B2F. Resets ALL boulders if player enters. Must be filled.
- LADDER: Warp to 1F/B2F. Resets ALL boulders if player enters.
- ICE: Sliding mechanic. Moving onto ICE causes player to slide until hitting a WALL or non-ICE tile.
- BOULDER: Movable with Strength. Resets on floor change.

## Navigation Notes
- Section 3 (Right): (17, 5), (17, 8), (17, 10), (17, 13) are WALLs. Use Column 18/19.
- Row 1: Safe non-ice corridor.
- Avoid (12, 6) and (11, 11) - they are WALLs.

## Lessons Learned
- Strength is lost immediately upon changing floors (using ladders or falling through pits).
- Navigation tools may accidentally path through warps/ladders (e.g., (17, 3)). Always check for warps on the intended path and use intermediate coordinates to bypass them.
- `find_map_objects` only detects objects currently on the screen. Manual scouting is required to verify off-screen spawn points.
- Confirmation bias: Boulders reset whenever the floor is exited and re-entered. I must verify all four points before solving.