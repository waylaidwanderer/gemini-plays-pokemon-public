# Ice Path B2F Boulder Verification
- Session Start Turn: 29016
- Goal: Verify if boulders 1-4 are present in their target pits on B2F.
- Reset Logic: If boulders are missing, return to B1F and restart puzzle.

## Target Pit Coordinates (B2F)
- Boulder 1: (11, 4) - Checking...
- Boulder 2: (4, 6) - Checking...
- Boulder 3: (4, 12) - Checking...
- Boulder 4: (12, 12) - Checking...

## Tile Mechanics
- FLOOR: Walkable.
- WALL: Impassable.
- ICE: Sliding mechanic. Moving onto ICE causes player to slide until hitting a WALL or non-ICE tile.
- BOULDER: If in a pit, acts as a WALL/STOP point for sliding.

## Navigation Notes
- Current Position: (17, 1) (Ladder area).
- Plan: Scout central ice area to identify boulder presence.

## Lessons Learned
- Boulders pushed into pits on B1F appear as objects on B2F.
- Falling through a pit may or may not reset the boulders on B1F. Verifying now.