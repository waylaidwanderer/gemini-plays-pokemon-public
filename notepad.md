# Ice Path B1F Puzzle Status
- Start Turn: 28759 | Start Time: Sunday, Dec 28, 5:32 AM
- Status: Boulders RESET on floor change. All 4 must be pushed in one session.
- Pit 1 (11, 2): FILLED (Turn 28912). (Marker placed).
- Pit 2 (4, 7): FILLED (Turn 28885). (Marker placed).
- Boulder 3: (8, 9)? | Target Pit 3: (5, 12)
- Boulder 4: (17, 7) | Target Pit 4: (12, 13)

# Tile Mechanics
- FLOOR: Walkable. (Verified: Row 1, Row 16, and various patches).
- WALL: Impassable.
- ICE: Sliding mechanic. Moving onto ice causes player to slide in that direction until hitting a wall or floor.
- PIT: Warp to B2F. Must be filled with a boulder to become traversable on B2F.
- BOULDER: Movable object. Pushed by facing it and walking into it while Strength is active. Resets to original position if the player leaves the floor.

# Map Sections (B1F)
- Section 1 (Left): (0, 1) to (8, 16). Contains Ladder to 1F (3, 15), Pit 2 (Filled), and Pit 3 (5, 12).
- Section 2 (Middle): (9, 1) to (13, 15). Contains Boulder 1 (Pitted), Pit 1 (Filled), and Pit 4 (12, 13).
- Section 3 (Right): (14, 1) to (19, 16). Contains Ladder to B2F (17, 3) and Boulder 4 (17, 7).

# Strategies
## Fill Pit 3 (5, 12) with Boulder 3 (8, 9)
1. Navigate to (7, 9).
2. Face RIGHT and push to (9, 9). (Player at 8, 9).
3. Move to (9, 8).
4. Face DOWN and push to (9, 11). (Player at 9, 10).
5. Move to (10, 11).
6. Face LEFT and push to (4, 11). (Player at 5, 11).
7. Move to (4, 10).
8. Face DOWN and push to (4, 12). (Player at 4, 11).
9. Move to (3, 12).
10. Face RIGHT and push into Pit 3 (5, 12). (Player at 4, 12).

## Fill Pit 4 (12, 13) with Boulder 4 (17, 7)
1. Navigate to Boulder 4 at (17, 7).
2. Use puzzle_strategist_v1 to generate sequence.

# Lessons Learned
- Boulders reset if you leave the floor.
- You push the tile you are facing.
- Row 1 and Row 16 are non-ice corridors.
- Pit 1 (11, 2) and Pit 2 (4, 7) are filled. (Markers placed).