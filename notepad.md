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
- Hypothesis 1: (4, 5) is a fake wall.
  - Test: Attempt to move into (4, 5) from (3, 5).
- Hypothesis 2: (2, 13) is a fake wall.
  - Test: Attempt to move into (2, 13) from (1, 13).
- Hypothesis 3: (6, 3) is a fake wall.
  - Test: Attempt to move into (6, 3) from (7, 3).
- Phase 1: Activate Strength by interacting with B6.
- Phase 2: Move to (3, 5) and test (4, 5).