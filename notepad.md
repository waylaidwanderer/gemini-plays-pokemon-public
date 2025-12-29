# Tile Mechanics (Global)
- FLOOR: Passable.
- WALL: Impassable silver blocks. Absolute barrier.
- PIT: Player falls to 1F. Boulder destination (forms bridge on 1F).
- LADDER: Warp between floors. Deactivates Strength.
- Strength: Inactive. Reactivate by interacting with a boulder (A button).

# Blackthorn Gym 2F State
- Boulders: B6 (3, 3), B7 (6, 1), B8 (8, 11).
- Pits: (2, 5), (8, 3), (8, 7).
- NPCs: Cody (4, 1), Fran (4, 11). Both solid.

# Time Tracking
- Puzzle Start Turn: 29931.
- Attempt 1: Turns 29931-30103 (Manual/brittle tools). Zero progress.
- Attempt 2 Start: Turn 30104.

# Strategy: Boulder Puzzle
- Goal: Fill all pits with boulders.
- Plan:
  1. Activate Strength at Boulder 8 (8, 11).
  2. Use `puzzle_analyst` to find a path for B8 that avoids walls.
  3. Use `solve_blackthorn_boulders` (dynamic) for precise pushes.