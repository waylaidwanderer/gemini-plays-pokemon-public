# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- PIT: Impassable. Falling into a pit warps the player to the floor below (1F).
- LADDER: Warp to the floor below (1F).
- BOULDER: Object. Can be pushed with Strength. Impassable.

# Blackthorn Gym Boulder Puzzle
- Boulders on 2F (Current Positions):
    - ID 6: (3, 3) (Verified Turn 30266)
    - ID 7: (6, 1) (Verified Turn 30266)
    - ID 8: (8, 14) (Verified Turn 30267)
- Pits on 2F:
    - P1: (2, 5) - UNFILLED
    - P2: (8, 3) - UNFILLED
    - P3: (8, 7) - FILLED (Verified on 1F Turn 30257, need to verify on 2F)
- Goal: Fill P1 and P2 to complete the bridge on 1F.
- Strategy: Verify P3 is a floor on 2F, then use solve_blackthorn_boulders.

# Verified Map Constraints (2F)
- Row 0 and Row 17: Boundaries.
- Column 0 and Column 9: Boundaries.
- Column 2 Wall: Rows 10-17.
- Column 4 Wall: Rows 2-10, 12.
- Column 6 Wall: Rows 2-4, 6, 8.
- Column 8 Wall: Rows 8-9.