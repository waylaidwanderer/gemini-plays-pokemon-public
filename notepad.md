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