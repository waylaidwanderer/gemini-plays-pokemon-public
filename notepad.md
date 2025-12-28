# Ice Path B2F Boulder Verification
- Session Start Turn: 29016
- Goal: Fill all 4 pits with boulders on B2F.
- Reset Logic: Boulders on B2F do NOT reset when falling through pits (Turn 29020 verification).

## Confirmed Boulder Locations (B2F)
- Boulder 1: (11, 3). Target: (11, 4). Status: Confirmed (Turn 29020).
- Boulder 2: (4, 7). Target: (4, 6). Status: Confirmed (Turn 29019).
- Boulder 3: (3, 12). Target: (4, 12). Status: To be verified.
- Boulder 4: (12, 13). Target: (12, 12). Status: To be verified.

## Tile Mechanics
- FLOOR: Walkable.
- WALL: Impassable.
- ICE: Sliding mechanic. Moving onto ICE causes player to slide until hitting a WALL, non-ICE tile, or BOULDER.
- BOULDER: Acts as a WALL/STOP point for sliding. Can be pushed with Strength.

## Navigation Notes
- Current Position: (10, 3).
- Plan: Navigate to (1, 16) to scout Boulder 3 and 4, then solve.

## Lessons Learned
- Boulders pushed into pits on B1F land adjacent to the corresponding landing holes on B2F.
- They must be pushed a second time into the holes on B2F to complete the puzzle.
- Strength is required on B2F to move them.