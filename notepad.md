# Ice Path B1F Puzzle Status
- Start Turn: 28759 | Start Time: Sunday, Dec 28, 5:32 AM
- Status: Boulders RESET on floor change. All 4 must be pushed in one session.
- Boulder 1: (11, 7) | Target Pit 1: (11, 2)
- Boulder 2: (7, 8) | Target Pit 2: (4, 7)
- Boulder 3: (??) | Target Pit 3: (5, 12)
- Boulder 4: (17, 7) | Target Pit 4: (12, 13)

# Map Sections (B1F)
- Section 1 (Left): (0, 1) to (8, 16). Contains Ladder to 1F (3, 15), Boulder 2 (7, 8), Pit 2 (4, 7), and Pit 3 (5, 12).
- Section 2 (Middle): (9, 1) to (13, 15). Contains Boulder 1 (11, 7), Pit 1 (11, 2), and Pit 4 (12, 13).
- Section 3 (Right): (14, 1) to (19, 16). Contains Ladder to B2F (17, 3) and Boulder 4 (17, 7).

# Connectivity
- Section 3 <-> Section 2: Row 16 corridor (9, 16) to (18, 16).
- Section 2 <-> Section 1: Row 1 gap at (9, 1) <-> (8, 1) (via ICE sliding).
- Section 2 <-> Section 1: Row 16 corridor.

# Strategies
## Fill Pit 2 (4, 7) with Boulder 2 (7, 8)
1. Navigate to (12, 1). (Current Pos: 12, 5).
2. Move Left to slide to (2, 1).
3. Walk to (8, 8) via (5, 8) -> (5, 9) -> (8, 9) -> (8, 8).
4. Activate Strength.
5. Push LEFT to (5, 8). (Player at 6, 8).
6. Navigate to (5, 9).
7. Push UP to (5, 6). (Player at 5, 7).
8. Navigate to (6, 6).
9. Push LEFT to (4, 6). (Player at 5, 6).
10. Navigate to (4, 5).
11. Push DOWN into Pit 2 (4, 7).

## Fill Pit 1 (11, 2) with Boulder 1 (11, 7)
1. Complete "Fill Pit 2" strategy.
2. Navigate to (11, 8).
3. Push UP to (11, 5). (Player at 11, 6).
4. Push LEFT to (10, 5). (Player at 11, 5).
5. Push UP to (10, 2). (Player at 10, 3).
6. Push RIGHT into Pit 1 (11, 2). (Player at 10, 2).

# Game Mechanics
- FLOOR: Walkable.
- ICE: Sliding mechanic. Row 1 is confirmed ICE.
- PIT: Warp to B2F. Must fill to solve B2F.
- BOULDER: RESETS on floor change (verified Turn 28854). Must do all in one run.
- STRENGTH: Deactivates after every floor change.

# Lessons Learned
- Boulders reset! My previous note about them being permanent was wrong. I must push all four without leaving the floor.
- Row 16 is a safe corridor across the entire map.
- Row 1 allows fast travel between sections via sliding.
- Avoid (12, 6) - it's a WALL. (Corrected Turn 28854).