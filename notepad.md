# Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable silver blocks.
- PIT: Warp for player (to 1F), destination for boulders.
- LADDER: Warp between floors.
- Strength: Active (Turn 30009). Required to push boulders.

# Blackthorn Gym 2F State
- Boulders (Current):
  - B6: (3, 3)
  - B7: (6, 1)
  - B8: (8, 12)
- Pits: (2, 5), (8, 3), (8, 7).
- Crossing Points:
  - Row 9: Gap in Column 2 at (2, 9).
  - Row 13: Gap in Column 4 at (4, 13).
  - Row 1: Gap in Column 4, but Cody (NPC) blocks (4, 1).
  - Row 11: Gap in Column 4, but Fran (NPC) blocks (4, 11).

# Strategy: Boulder Puzzle
- Goal: Drop all three boulders into pits.
- Puzzle Start Turn: 29931.
- Plan:
  1. Solve the puzzle using optimized BFS.
  2. Execute sequence.
- Verified Walls: (4, 5), (9, 13), (2, 13).