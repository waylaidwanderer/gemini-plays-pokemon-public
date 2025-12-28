# Ice Path B1F Puzzle Status
- Start Turn: 28759 | Start Time: Sunday, Dec 28, 5:32 AM
- Status: Boulders RESET on floor change. All 4 must be pushed in one session.
- Boulder 1: (10, 5) | Target Pit 1: (11, 2)
- Boulder 3: (8, 9) | Target Pit 3: (5, 12)
- Boulder 4: (17, 7) | Target Pit 4: (12, 13)

# Tile Mechanics
- FLOOR: Walkable. (Verified: Row 1, Row 16, and various patches).
- WALL: Impassable.
- ICE: Sliding mechanic. Moving onto ice causes player to slide in that direction until hitting a wall or floor.
- PIT: Warp to B2F. Must be filled with a boulder to become traversable on B2F.
- BOULDER: Movable object. Pushed by facing it and walking into it while Strength is active. Resets to original position if the player leaves the floor.

# Map Sections (B1F)
- Section 1 (Left): (0, 1) to (8, 16). Contains Ladder to 1F (3, 15), Pit 2 (Filled), and Pit 3 (5, 12).
- Section 2 (Middle): (9, 1) to (13, 15). Contains Boulder 1 (10, 5), Pit 1 (11, 2), and Pit 4 (12, 13).
- Section 3 (Right): (14, 1) to (19, 16). Contains Ladder to B2F (17, 3) and Boulder 4 (17, 7).

# Strategies
## Fill Pit 1 (11, 2) with Boulder 1 (10, 5)
1. At (10, 6), face UP and push to (10, 1). (Player at 10, 2).
2. Move to (9, 1).
3. Face RIGHT and push to (11, 1). (Player at 10, 1).
4. Move to (11, 0).
5. Face DOWN and push into Pit 1 (11, 2).

## Fill Pit 3 (5, 12) with Boulder 3 (8, 9)
1. Push LEFT to (6, 9).
2. Move to (6, 11).
3. Push LEFT to (4, 11).
4. Move to (4, 12).
5. Push RIGHT into Pit 3 (5, 12).

## Fill Pit 4 (12, 13) with Boulder 4 (17, 7)
1. Use puzzle_strategist_v1 to generate sequence.

# Lessons Learned
- Boulders reset if you leave the floor.
- You push the tile you are facing.
- Row 1 and Row 16 are non-ice corridors.
- Pit 2 (4, 7) is filled. (Marker placed).