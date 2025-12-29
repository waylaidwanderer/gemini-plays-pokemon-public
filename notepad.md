# Tile Mechanics (Global)
- FLOOR: Passable. Standard traversable terrain.
- WALL: Impassable silver blocks. Absolute barrier for player and boulders.
- PIT: Hazardous for player (warp to 1F). Target for boulders (forms bridge on 1F).
- LADDER: Warp between floors (1F/2F). Deactivates Strength.
- Strength: Inactive. Reactivate by interacting with a boulder (A button).

# Blackthorn Gym 2F State
- Boulders: B6 (3, 3), B7 (6, 1). B8 status unverified.
- Pits: (2, 5), (8, 3), (8, 7).
- NPCs: Cody (4, 1), Fran (4, 11). Both act as solid obstacles.
- Barriers: Column 4 is a wall Row 0-12 (except Cody/Fran). Column 2 is a wall Row 10-17.
- Crossings: Row 13 gap at (4, 13). Row 1 gap at (2, 1).

# Time Tracking
- Puzzle Start Turn: 29931.
- Current Attempt Start: Turn 30091.

# Strategy: Boulder Puzzle
- Goal: Drop all boulders into pits.
- Plan:
  1. Verify B8 and Pit (8, 7) status.
  2. Activate Strength.
  3. Use `solve_blackthorn_boulders` (dynamic version) to get sequence.
  4. Execute pushes.