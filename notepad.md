# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- PIT: Impassable. Falling into a pit warps the player to the floor below (1F).
- LADDER: Warp to the floor below (1F).
- BOULDER: Object. Can be pushed with Strength. Impassable.

# Blackthorn Gym Boulder Puzzle
- Boulders on 2F:
    - ID 6: (3, 3) (Verified Turn 30255)
    - ID 7: (7, 1) (Verified Turn 30255)
    - ID 8: (8, 13) (Verified Turn 30256)
- Pits on 2F:
    - P1: (2, 5)
    - P2: (8, 3)
    - P3: (8, 7) (Summary says a boulder was pushed here)
- Goal: Fill remaining pits to complete the bridge on 1F.
- Strategy: Go to 1F and verify which pits are filled. Then return to 2F to push the remaining boulders.

# Verified Map Constraints (2F)
- Row 0 and Row 17: Boundaries.
- Column 0 and Column 9: Boundaries.
- Column 2 Wall: Rows 10-17.
- Column 4 Wall: Rows 2-10, 12.
- Column 6 Wall: Rows 2-4, 6, 8.
- Column 8 Wall: Rows 8-9.