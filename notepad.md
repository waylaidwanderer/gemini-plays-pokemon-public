# Ice Path B1F Puzzle Status
- Start Turn: 28759 | Start Time: Sunday, Dec 28, 5:32 AM
- Boulder 1: (10, 1) | Target Pit 1: (11, 2)
- Boulder 2: (5, 6) | Target Pit 2: (4, 7)
- Boulder 3: (??) | Target Pit 3: (5, 12)
- Boulder 4: (17, 7) | Target Pit 4: (12, 13)

# Map Sections (B1F)
- Section 1 (Left): (0, 1) to (7, 16). Contains Ladder to 1F (3, 15), Boulder 2 (5, 6), Pit 2 (4, 7), and Pit 3 (5, 12).
- Section 2 (Middle): (9, 1) to (13, 15). Contains Pit 1 (11, 2) and Pit 4 (12, 13).
- Section 3 (Right): (14, 1) to (19, 16). Contains Ladder to B2F (17, 3) and Boulder 4 (17, 7).

# Connectivity
- Section 3 <-> Section 2: Row 16 gap at (14, 16) to (13, 16).
- Section 2 <-> Section 1: Row 9 gap at (9, 9) to (8, 9).
- Row 1 (ICE): Connects all sections, but causes sliding. Stop at Boulders or Walls.

# Strategies
## Fill Pit 1 (11, 2) with Boulder 1 (10, 1)
1. Slide LEFT from (17, 1) to hit Boulder 1 and stop at (11, 1).
2. Walk to (12, 1), then slide RIGHT to (17, 1).
3. Navigate to Section 1 via Section 3 -> Section 2 -> Section 1 gaps.
   Path: (17, 1) -> (17, 4) -> (18, 4) -> (18, 16) -> (14, 16) -> (13, 16) -> (13, 9) -> (9, 9) -> (8, 9) -> (7, 9).
4. Walk to (7, 1).
5. Slide RIGHT from (7, 1) to hit Boulder 1 and stop at (9, 1).
6. Activate Strength.
7. Push Boulder 1 RIGHT to (11, 1). (Player at 10, 1).
8. Walk to (11, 0).
9. Push Boulder 1 DOWN into Pit 1 (11, 2).

## Fill Pit 2 (4, 7) with Boulder 2 (5, 6)
1. Navigate to (6, 6) in Section 1.
2. Push LEFT to (4, 6). (Player at 5, 6).
3. Push DOWN into Pit 2 (4, 7). (Player at 4, 6).

## Fill Pit 4 (12, 13) with Boulder 4 (17, 7)
1. Navigate to (17, 6).
2. Push DOWN to (17, 12).
3. Push LEFT to (12, 12).
4. Push DOWN into Pit 4 (12, 13).

# Game Mechanics
- FLOOR: Walkable. Standard behavior.
- ICE (Rows 1-2): Sliding mechanic. Verified.
- PIT: Warp to B2F. Filling a pit creates a permanent stopper on B2F. Verified.
- BOULDER: Resets on ladder use. Permanent if in pit. Verified.
- STRENGTH: Deactivates after floor change. Verified.

# Lessons Learned
- Boulders on B1F fall into pits to become stoppers on B2F.
- The B2F ice puzzle requires all 4 stoppers to reach the ladder at (9, 11).
- Navigation between sections requires specific gaps in the walls (Row 9 and Row 16).