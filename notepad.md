# Ice Path B1F Puzzle Status
- Current Session Start: Turn 28627 (Last floor change)
- Status: Boulders RESET on floor change. All 4 must be pushed in one session.
- Pit 1 (11, 2): FILLED (Turn 28912).
- Pit 2 (4, 7): FILLED (Turn 28885).
- Pit 3 (5, 12): Empty.
- Pit 4 (12, 13): Empty.
- Boulder 3: UNKNOWN (Not at 8, 9). Must search southern area (Rows 21-35).
- Boulder 4: (17, 7) (Needs verification).

# Tile Mechanics
- FLOOR: Walkable.
- WALL: Impassable.
- ICE: Sliding mechanic.
- PIT: Warp to B2F. Becomes traversable on B2F once filled.
- BOULDER: Movable object. Resets if player leaves the floor.

# Map Sections (B1F)
- Section 1 (Left): (0, 1) to (8, 16). Contains Ladder to 1F (3, 15), Pit 2 (Filled), and Pit 3 (5, 12).
- Section 2 (Middle): (9, 1) to (13, 15). Contains Pit 1 (Filled), and Pit 4 (12, 13).
- Section 3 (Right): (14, 1) to (19, 16). Contains Ladder to B2F (17, 3) and Boulder 4 (17, 7).

# Strategies
## Fill Pit 4 (12, 13) with Boulder 4 (17, 7)
1. Verify Boulder 4 at (17, 7).
2. Use puzzle_strategist_v1 to generate sequence.

## Fill Pit 3 (5, 12) with Boulder 3
1. Search southern area (Rows 21-35) to locate Boulder 3.
2. Use puzzle_strategist_v1.

# Lessons Learned
- Boulders reset if you leave the floor (including falling through pits).
- Pit 1 (11, 2) and Pit 2 (4, 7) are currently filled in this session.
- Row 1 and Row 16 are non-ice corridors.
- (17, 13) is a WALL, must go around through Column 18.