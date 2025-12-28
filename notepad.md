# Ice Path B1F Boulder Puzzle
- Goal: Fill all 4 pits with boulders in a single session.
- Reset Trigger: Leaving floor (ladders or falling through pits).

## Strategy: DECISIVE ACTION (Post-Reset)
1. Current State: Just returned to B1F from B2F. Boulders should be at spawn points.
2. Step 1: Confirm Boulder 4 at (17, 7). (Turn 28988: Not at (17, 7)).
3. Step 2: Confirm Boulder 1 at (11, 7).
4. Step 3: Confirm Boulder 2 at (7, 8).
5. Step 4: Confirm Boulder 3 at (8, 9).
6. Call `puzzle_strategist_v1` and execute.

## Tile Mechanics
- FLOOR: Walkable.
- WALL: Impassable.
- ICE: Sliding.
- PIT: Warp to B2F. Resets ALL boulders if entered. Must be filled to solve B2F.
- BOULDER: Movable with Strength. Resets on floor change.
- STRENGTH: Persists through battles but is LOST on floor changes (ladders/pits). (Note: Re-activated Turn 28979). Verified Turn 28988: Strength is ACTIVE.

## Navigation Notes
- Section 3: (17, 5), (17, 8), (17, 10), (17, 13) are WALLs. Use Column 18/19.
- Row 1 and Row 16: Safe non-ice corridors. Avoid (12, 6) and (11, 11) - they are WALLs.