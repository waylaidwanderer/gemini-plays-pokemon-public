# Ice Path B1F Puzzle Status
- Start Turn: 28759 | Start Time: Sunday, Dec 28, 5:32 AM
- Boulder 1: (11, 7) | Target Pit 1: (11, 2)
- Boulder 2: (7, 8) | Target Pit 2: (4, 7)
- Boulder 3: (??) | Target Pit 3: (5, 12)
- Boulder 4: (17, 7) | Target Pit 4: (12, 13)

# Map Sections (B1F)
- Section 1 (Left): (0, 1) to (8, 16). Contains Ladder to 1F (3, 15), Boulder 2 (7, 8), Pit 2 (4, 7), and Pit 3 (5, 12).
- Section 2 (Middle): (9, 1) to (13, 15). Contains Boulder 1 (11, 7), Pit 1 (11, 2), and Pit 4 (12, 13).
- Section 3 (Right): (14, 1) to (19, 16). Contains Ladder to B2F (17, 3) and Boulder 4 (17, 7).

# Connectivity
- Section 3 <-> Section 2: Row 16 gap at (14, 16) to (13, 16).
- Section 2 <-> Section 1: Row 9 gap at (9, 9) to (8, 9).
- Row 1 (ICE): Connects all sections.

# Strategies
## Fill Pit 2 (4, 7) with Boulder 2 (7, 8)
1. Navigate to (8, 8) via Section 2 and Row 15 gap.
   Path: (10, 3) -> (10, 5) -> (12, 5) -> (12, 15) -> (9, 15) -> (9, 9) -> (8, 9) -> (8, 8).
2. Activate Strength.
3. Push LEFT to (5, 8). (Player at 6, 8).
4. Navigate to (5, 9).
5. Push UP to (5, 6). (Player at 5, 7).
6. Navigate to (6, 6).
7. Push LEFT to (4, 6). (Player at 5, 6).
8. Navigate to (4, 5).
9. Push DOWN into Pit 2 (4, 7).

## Fill Pit 1 (11, 2) with Boulder 1 (11, 7)
1. Complete "Fill Pit 2" strategy.
2. Navigate to (11, 8) via Section 3 and the Row 16 gap.
3. Activate Strength.
4. Push UP to (11, 5). (Player at 11, 6).
5. Push LEFT to (10, 5). (Player at 11, 5).
6. Push UP to (10, 2). (Player at 10, 3).
7. Push RIGHT into Pit 1 (11, 2). (Player at 10, 2).

# Game Mechanics
- FLOOR: Walkable. Standard behavior in most of B1F.
- ICE: Sliding mechanic. Present in specific patches, but Row 1 and Row 17 are standard FLOOR.
- PIT: Warp to B2F. Filling a pit creates a permanent stopper on B2F. Verified.
- BOULDER: Resets on ladder use. Permanent if in pit. Verified.
- STRENGTH: Deactivates after every battle or floor change. Verified.

# Lessons Learned
- Boulders on B1F fall into pits to become stoppers on B2F.
- The B2F ice puzzle requires all 4 stoppers to reach the ladder at (9, 11).
- Navigation between sections requires specific gaps in the walls (Row 9 and Row 16).
- Row 1 and Row 17 are confirmed to be standard FLOOR, allowing safe navigation around the perimeter. (Corrected Turn 28849).