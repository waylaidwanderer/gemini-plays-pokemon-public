# Ice Path B1F Puzzle Status
- Start Turn: 28759 | Start Time: Sunday, Dec 28, 5:32 AM
- Status: Boulders RESET on floor change. All 4 must be pushed in one session.
- Boulder 1: (11, 7) | Target Pit 1: (11, 2)
- Boulder 2: (5, 7) | Target Pit 2: (4, 7)
- Boulder 3: (??) | Target Pit 3: (5, 12)
- Boulder 4: (17, 7) | Target Pit 4: (12, 13)

# Map Sections (B1F)
- Section 1 (Left): (0, 1) to (8, 16). Contains Ladder to 1F (3, 15), Boulder 2 (5, 7), Pit 2 (4, 7), and Pit 3 (5, 12).
- Section 2 (Middle): (9, 1) to (13, 15). Contains Boulder 1 (11, 7), Pit 1 (11, 2), and Pit 4 (12, 13).
- Section 3 (Right): (14, 1) to (19, 16). Contains Ladder to B2F (17, 3) and Boulder 4 (17, 7).

# Connectivity
- Section 3 <-> Section 2: Row 16 corridor (9, 16) to (18, 16).
- Section 2 <-> Section 1: Row 1 gap at (9, 1) <-> (8, 1) (via ICE sliding).
- Section 2 <-> Section 1: Row 16 corridor.

# Strategies
## Fill Pit 2 (4, 7) with Boulder 2 (5, 7)
1. Move to (5, 8). (Done)
2. Push UP to (5, 6). (Next step)
3. Navigate to (6, 6) via Row 16 and Row 1.
   Path: (5, 7) -> (5, 8) -> (9, 8) -> (9, 16) -> (12, 16) -> (12, 1) -> (8, 1) -> (6, 1) -> (6, 2) -> (5, 2) -> (5, 5) -> (6, 5) -> (6, 6).
4. Push LEFT to (4, 6). (Player at 5, 6).
5. Move to (4, 5).
6. Push DOWN into Pit 2 (4, 7).

## Fill Pit 1 (11, 2) with Boulder 1 (11, 7)
1. Complete "Fill Pit 2" strategy.
2. Navigate to (11, 8).
3. Push UP to (11, 5). (Player at 11, 6).
4. Push LEFT to (10, 5). (Player at 11, 5).
5. Push UP to (10, 2). (Player at 10, 3).
6. Push RIGHT into Pit 1 (11, 2). (Player at 10, 2).

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