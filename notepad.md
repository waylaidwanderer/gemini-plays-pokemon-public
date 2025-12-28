# Ice Path B1F Puzzle Status
- Current Session Start: Turn 28627
- Status: Boulders RESET on floor change. All 4 must be pushed in one session.
- Pit 1 (11, 2): Empty.
- Pit 2 (4, 7): Empty.
- Pit 3 (5, 12): Empty.
- Pit 4 (12, 13): Empty.
- Boulder 1: (11, 7) (Searching).
- Boulder 2: (7, 8) (Searching).
- Boulder 3: (8, 9) (Searching).
- Boulder 4: (17, 7) (Searching).

# Tile Mechanics
- FLOOR: Walkable.
- WALL: Impassable.
- ICE: Sliding mechanic.
- PIT: Warp to B2F. Becomes traversable on B2F once filled.
- BOULDER: Movable object. Resets if player leaves the floor.

# Map Sections (B1F)
- Section 1 (Left): (0, 1) to (8, 16). Contains Ladder to 1F (3, 15), Pit 2, and Pit 3.
- Section 2 (Middle): (9, 1) to (13, 15). Contains Pit 1, and Pit 4.
- Section 3 (Right): (14, 1) to (19, 16). Contains Ladder to B2F (17, 3) and Boulder 4.

# Strategies
## Locate all Boulders
1. Search northern area spawn points: (11, 7), (7, 8), (8, 9), (17, 7).
2. Mark each boulder with a unique emoji.

# Lessons Learned
- Boulders reset if you leave the floor (including falling through pits).
- Pits are still warps in Game State Information, meaning they are NOT filled.
- Row 1 and Row 16 are non-ice corridors.
- (17, 8) and (17, 13) are WALLs, use Column 18 to go north in Section 3.