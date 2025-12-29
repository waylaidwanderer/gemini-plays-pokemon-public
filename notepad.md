# Tile Mechanics (Global)
- FLOOR: Passable. Standard traversable terrain.
- WALL: Impassable silver blocks. Absolute barrier for player and boulders.
- PIT: Hazardous for player (warp to 1F). Target for boulders (forms bridge on 1F).
- LADDER: Warp between floors. Deactivates Strength.
- Strength: Active (Turn 30101). Reactivate by interacting with a boulder (A button).

# Blackthorn Gym 2F State
- Boulders: B6 (3, 3), B7 (6, 1), B8 (8, 12).
- Pits: (2, 5), (8, 3), (8, 7).
- NPCs: Cody (4, 1), Fran (4, 11). Both act as solid obstacles.
- Barriers: Column 4 wall Row 0-12. Column 2 wall Row 10-17. Row 8 wall at (2,8)-(4,8).
- Crossings: Row 13 gap at (4, 13) is the primary crossing. Row 1 gap at (2, 1).

# Time Tracking
- Puzzle Start Turn: 29931.
- Current Attempt Start: Turn 30104.

# Strategy: Boulder Puzzle
- Goal: Drop all boulders into pits.
- Plan:
  1. Verify the state of Pit (8, 7) and Boulder 8.
  2. Map out paths: B8 -> (8, 7), B7 -> (8, 3), B6 -> (2, 5).
  3. Identify and test potential "fake walls" blocking boulder paths (e.g., Row 0 or Row 4/8/12).
  4. Use `solve_blackthorn_boulders` with confirmed coordinates.