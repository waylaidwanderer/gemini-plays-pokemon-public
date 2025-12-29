# Tile Mechanics (Global)
- FLOOR: Passable.
- WALL: Impassable silver blocks.
- PIT: Player falls to 1F. Boulder destination (forms bridge on 1F).
- LADDER: Warp between floors. Deactivates Strength.
- Strength: Inactive. Reactivate by interacting with a boulder.

# Blackthorn Gym 2F State
- Boulders: B6 (3, 3), B7 (6, 1). B8 status unknown.
- Pits: (2, 5), (8, 3), (8, 7).
- NPCs: Cody (4, 1), Fran (4, 11). Both solid barriers.
- Verified Walls: (4, 5), (9, 13), (2, 13), (3, 0) - all solid.

# Time Tracking
- Puzzle Start Turn: 29931.

# Strategy: Boulder Puzzle
- Goal: Drop all boulders into pits.
- Current Plan:
  1. Verify if B8 is in pit (8, 7).
  2. Activate Strength.
  3. Use `solve_blackthorn_boulders` with dynamic XML parsing.