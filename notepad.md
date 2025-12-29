# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- PIT: Impassable. Falling into a pit warps the player to the floor below (1F).
- LADDER: Warp to the floor below (1F).
- BOULDER: Object. Can be pushed with Strength. Impassable.

# Blackthorn Gym Boulder Puzzle
- Start Turn: 30123
- Boulders Found (2F):
    - B6: (3, 3) (Verified Turn 30255)
    - B7: (7, 1) (Verified Turn 30255)
    - B9: (8, 13)? (Need to verify)
- Pits (2F):
    - P1: (2, 5)
    - P2: (8, 3)
    - P3: (8, 7) (Summary says one boulder was pushed here)
- Goal: Push boulders into pits to create bridges on 1F.
- Strategy: Verify all boulders on 2F, then check 1F to see which pits still need filling.

# Verified Map Constraints (2F)
- Row 0 and Row 17: Boundaries.
- Column 0 and Column 9: Boundaries.
- Column 2 Wall: Rows 10-17.
- Column 4 Wall: Rows 2-10, 12.
- Column 6 Wall: Rows 2-4, 6, 8.
- Column 8 Wall: Rows 8-9.