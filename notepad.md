# Tile Mechanics (Global)
- FLOOR: Passable. Standard traversable terrain.
- WALL: Impassable silver blocks. Absolute barrier for player and boulders.
- PIT: Hazardous for player (warp to 1F). Target for boulders (forms bridge on 1F).
- LADDER: Warp between floors. Deactivates Strength.
- Strength: Inactive. Reactivate by interacting with a boulder (A button).

# Blackthorn Gym 2F State
- Boulders: B6 (3, 3), B7 (6, 1), B8 (8, 14).
- Pits: (2, 5), (8, 3), (8, 7).
- NPCs: Cody (4, 1), Fran (4, 11). Both act as solid obstacles.
- Barriers: Column 4 wall Row 0-12. Column 2 wall Row 10-17. Row 8 wall at (2,8)-(4,8).
- Crossings: Row 13 gap at (4, 13) is the only way to the right side from Column 3. Row 1 gap at (2, 1).

# Time Tracking
- Puzzle Start Turn: 29931.
- Current Attempt Start: Turn 30091.

# Strategy: Boulder Puzzle
- Goal: Drop all boulders into pits.
- Plan:
  1. Confirm B8 is pushable by standing at (8, 15).
  2. If B8 is pushable, move it to (8, 13) -> (4, 13) -> (6, 13) -> (6, 7) -> (8, 7) Pit.
  3. Re-evaluate B6 and B7 after B8 is cleared.