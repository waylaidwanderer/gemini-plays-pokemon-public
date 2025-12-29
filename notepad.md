# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- PIT: Impassable. Falling into a pit warps the player to the floor below (1F).
- LADDER: Warp to the floor below (1F).
- BOULDER: Object. Can be pushed with Strength. Impassable.

# Blackthorn Gym Boulder Puzzle
- Start Turn: 30123
- Boulders on 2F (Verified Positions):
    - ID 6: (3, 3) (Verified Turn 30266)
    - ID 7: (6, 1) (Verified Turn 30266)
    - ID 8: (8, 14) (Verified Turn 30267)
- Pits on 2F:
    - P1: (2, 5) - UNFILLED
    - P2: (8, 3) - UNFILLED
    - P3: (8, 7) - UNFILLED (Fell through Turn 30268)
- Strategy: Use run_code to calculate the shortest path of pushes for all three boulders.

# Verified Bridge Gaps (1F)
- (7, 7): Filled (Corresponds to 2F Pit at 8, 7) - WAIT, I fell through (8, 7) on 2F.
- (4, 3): Gap
- (3, 7): Gap
- (5, 7): Gap
- (4, 7): Gap
- Note: I need to re-verify the 1F gaps carefully. 1F (8, 7) had a boulder, but 2F (8, 7) was a pit. This means (8, 7) on 2F fills (8, 7) on 1F. Wait, the bridge is at Y=7 and Y=3.
- (7, 7) on 1F is a warp to Clair.
- (6, 7) on 1F is floor.
- (8, 7) on 1F is a filled pit.
- (3, 7), (4, 7), (5, 7) on 1F are gaps.
- (4, 3) on 1F is a gap.
- Pits on 2F: (2, 5), (8, 3), (8, 7).
- Hypothesis: 
    - (8, 7) 2F -> (8, 7) 1F (Done)
    - (8, 3) 2F -> (8, 3) 1F?
    - (2, 5) 2F -> (3, 7) 1F?
- I need to test this.

# Verified Map Constraints (2F)
- Row 0: WALL.
- Column 4 Wall: Rows 2-10, 12.
- Column 6 Wall: Rows 2-4, 6, 8.
- Column 7 Wall: Rows 4, 6, 10-11, 14-15.
- Column 2 Wall: Rows 2, 8, 10-17.
- Column 5 Wall: Rows 10, 12, 16-17.
- Column 8 Wall: Rows 4, 8-9.
- Column 9 Wall: Rows 4, 12-17.
- NPCs: Cody (4, 1), Fran (4, 11). Both solid.