# Ice Path B1F Puzzle Status
- Start Turn: 28759 | Start Time: Sunday, Dec 28, 5:32 AM
- Status: Boulders RESET on floor change. All 4 must be pushed in one session.
- Boulder 1: (11, 5) | Target Pit 1: (11, 2)
- Boulder 2: FILLED Pit 2 (4, 7)
- Boulder 3: (8, 9)? | Target Pit 3: (5, 12)
- Boulder 4: (17, 7)? | Target Pit 4: (12, 13)

# Map Sections (B1F)
- Section 1 (Left): (0, 1) to (8, 16). Contains Ladder to 1F (3, 15), Boulder 2 (Gone), Pit 2 (Filled), and Pit 3 (5, 12).
- Section 2 (Middle): (9, 1) to (13, 15). Contains Boulder 1 (11, 5), Pit 1 (11, 2), and Pit 4 (12, 13).
- Section 3 (Right): (14, 1) to (19, 16). Contains Ladder to B2F (17, 3) and Boulder 4 (17, 7).

# Connectivity
- Section 3 <-> Section 2: Row 16 corridor (9, 16) to (18, 16).
- Section 2 <-> Section 1: Row 1 gap at (9, 1) <-> (8, 1).
- Section 2 <-> Section 1: Row 16 corridor.

# Strategies
## Fill Pit 1 (11, 2) with Boulder 1 (11, 5)
1. Navigate to (11, 6).
2. Push LEFT to (10, 5). (Player at 11, 5).
3. Move to (10, 6).
4. Push UP to (10, 3). (Player at 10, 4).
5. Move to (9, 3).
6. Push RIGHT to (12, 3). (Player at 11, 3).
7. Move to (12, 4).
8. Push UP to (12, 2). (Player at 12, 3).
9. Move to (13, 2) (via Row 1).
10. Push LEFT into Pit 1 (11, 2). (Player at 12, 2).

## Fill Pit 3 (5, 12) with Boulder 3 (8, 9)
1. Navigate to (9, 9).
2. Push LEFT to (6, 9).
3. Navigate to (6, 8).
4. Push DOWN into Pit 3 (5, 12)... Wait, check coordinates.

## Fill Pit 4 (12, 13) with Boulder 4 (17, 7)
1. Navigate to (18, 7).
2. Push LEFT to (13, 7).
3. Navigate to (13, 6).
4. Push DOWN into Pit 4 (12, 13).

# Game Mechanics
- FLOOR: Walkable.
- ICE: Sliding mechanic. (Note: Row 1 is NOT ice, verified Turn 28856).
- PIT: Warp to B2F. Must fill to solve B2F.
- BOULDER: RESETS on floor change.
- STRENGTH: Deactivates after every floor change.

# Lessons Learned
- Boulders reset! Must do all in one run.
- Row 16 is a safe corridor across the entire map.
- Row 1 is standard FLOOR, not ice. (Corrected Turn 28856).
- Avoid (12, 6) - it's a WALL. (Corrected Turn 28854).