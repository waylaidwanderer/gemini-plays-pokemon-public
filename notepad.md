# Tile Mechanics (Global)
- FLOOR: Passable. Standard terrain.
- WALL: Impassable silver blocks. Absolute barrier.
- PIT: Hazardous for player (warp to 1F). Target for boulders (forms bridge on 1F). Verified: Boulders in pits become passable floor on 1F.
- LADDER: Warp between floors. Deactivates Strength.
- Strength: Inactive. Reactivate by interacting with a boulder (A button).

# Blackthorn Gym 2F State
- Boulders: B6 (3, 3), B7 (6, 1). B8 status unverified.
- Pits: (2, 5), (8, 3), (8, 7).
- NPCs: Cody (4, 1), Fran (4, 11). Both act as solid obstacles.
- Barriers: Column 4 wall Row 0-12. Column 2 wall Row 10-17. Row 8 wall at (2,8)-(4,8).
- Crossing Point: Row 13 at (4, 13) is the only way to the right side from Column 3.

# Time Tracking
- Puzzle Start Turn: 29931.
- Current Attempt Start: Turn 30091.

# Strategy: Boulder Puzzle
- Goal: Drop all boulders into pits.
- Plan:
  1. Navigate to (8, 7) and (8, 12) to verify B8 and Pit status.
  2. Activate Strength.
  3. Use `solve_blackthorn_boulders` (dynamic version) to get sequence.
  4. Execute pushes.