# Ice Path B1F Puzzle Status
- Start Turn: 28759 | Start Time: Sunday, Dec 28, 5:32 AM
- Status: Boulders RESET on floor change. All 4 must be pushed in one session.
- Pit 2 (4, 7): FILLED (Turn 28885). (Marker placed).
- Boulder 1: (11, 1) | Target Pit 1: (11, 2)
- Boulder 3: (??)
- Boulder 4: (17, 7) | Target Pit 4: (12, 13)

# Tile Mechanics
- FLOOR: Walkable. (Verified: Row 1, Row 16, and various patches).
- WALL: Impassable.
- ICE: Sliding mechanic. Moving onto ice causes player to slide in that direction until hitting a wall or floor.
- PIT: Warp to B2F. Must be filled with a boulder to become traversable on B2F.
- BOULDER: Movable object. Pushed by facing it and walking into it while Strength is active. Resets to original position if the player leaves the floor.

# Map Sections (B1F)
- Section 1 (Left): (0, 1) to (8, 16). Contains Ladder to 1F (3, 15), Pit 2 (Filled), and Pit 3 (5, 12).
- Section 2 (Middle): (9, 1) to (13, 15). Contains Boulder 1 (11, 1), Pit 1 (11, 2), and Pit 4 (12, 13).
- Section 3 (Right): (14, 1) to (19, 16). Contains Ladder to B2F (17, 3) and Boulder 4 (17, 7).

# Strategies
## Fill Pit 1 (11, 2) with Boulder 1 (11, 1)
- Current State: Boulder at (11, 1). Player at (9, 1).
- Steps:
  1. Move to (11, 0).
  2. Face DOWN and push into Pit 1 (11, 2).

## Fill Pit 3 (5, 12) with Boulder 3
- Current State: Boulder 3 location UNKNOWN.
- Steps:
  1. Explore bottom of map (Rows 20-35) to locate Boulder 3.
  2. Use puzzle_strategist_v1.

## Fill Pit 4 (12, 13) with Boulder 4 (17, 7)
- Current State: Boulder 4 at (17, 7).
- Steps:
  1. Navigate to Boulder 4.
  2. Use puzzle_strategist_v1.

# Lessons Learned
- Boulders reset if you leave the floor.
- You push the tile you are facing.
- Row 1 and Row 16 are non-ice corridors.
- Pit 2 (4, 7) is filled. (Marker placed).