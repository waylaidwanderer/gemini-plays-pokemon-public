# Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable silver blocks.
- PIT: Warp for player (to 1F), destination for boulders.
- LADDER: Warp between floors.
- Strength: Active (Turn 30009). Required to push boulders.

# Blackthorn Gym 2F State
- Boulders: B6 (3, 6), B7 (6, 1).
- Pits: (2, 5), (8, 3).
- B8: Pushed into Pit (8, 7) on Turn 29670.
- Crossing Points:
  - Row 1: Gap in Column 2, but Cody (NPC) blocks Column 4.
  - Row 9: Gap in Column 2 at (2, 9).
  - Row 13: Gap in Column 4 at (4, 13).

# Strategy: Boulder Puzzle
- Goal: Drop B6 into Pit (2, 5) and B7 into Pit (8, 3).
- Puzzle Start Turn: 29931.
- Current Phase: Investigating Cody at (4, 1).
- Verified Walls: (4, 5), (9, 13), (2, 13), (3, 0).