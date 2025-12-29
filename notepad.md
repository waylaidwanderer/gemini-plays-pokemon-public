# Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable silver blocks.
- PIT: Warp for player (to 1F), destination for boulders.
- LADDER: Warp between floors.
- Strength: Active (Turn 30009). Required to push boulders.

# Blackthorn Gym 2F State
- Boulders (Current):
  - B6: (3, 4)
  - B7: (6, 1)
  - B8: (8, 12)
- Pits: (2, 5), (8, 3), (8, 7).
- Crossing Points:
  - Row 1: Main horizontal corridor.
  - Row 13: Horizontal corridor, but (2, 13) is labeled WALL.

# Strategy: Finding the Path
- Problem: All pits seem unreachable for boulders due to WALL constraints (especially Row 0 blocking Down pushes from Row 1).
- Hypothesis: One of the 'WALL' tiles is actually passable or an NPC tile becomes passable after defeat.
- Test 1: Is (4, 1) (Cody's tile) passable? Result: NO (Turn 30069).
- Test 2: Is (3, 0) a fake wall?
- Test 3: Is (2, 13) actually a WALL?
- Test 4: Is (3, 8) actually a WALL?

# Puzzle Start Turn: 29931.