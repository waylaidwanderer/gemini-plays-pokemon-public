# Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable.
- PIT: Warp for player (to 1F), destination for boulders.
- LADDER: Warp between floors.
- Strength: Active (Turn 30009). Required to push boulders.

# Blackthorn Gym 2F State
- Boulders: B6 (3, 5), B7 (6, 1), B8 (8, 13).
- Pits: (2, 5), (8, 3), (8, 7).
- Crossing Points:
  - Row 1: Gap in Column 2, but Cody (NPC) blocks Column 4.
  - Row 9: Gap in Column 2 at (2, 9).
  - Row 11: Gap in Column 4, but Fran (NPC) is there.
  - Row 13: Crossing Column 4, but Column 2 is a WALL.

# Strategy
- Goal: Drop all three boulders into pits.
- Current Status: B8 is at (8, 13).
- Plan:
  1. Solve the puzzle using BFS via run_code.
  2. Execute the sequence.