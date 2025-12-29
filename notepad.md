# Tile Mechanics (Global)
- FLOOR: Passable terrain.
- WALL: Impassable silver blocks. Absolute barrier for player and boulders.
- PIT: Player falls to 1F. Boulder destination (forms bridge on 1F).
- LADDER: Warp between floors. Deactivates Strength.
- Strength: Active (Turn 30101).

# Blackthorn Gym 2F State
- Boulders: B6 (3, 3), B7 (6, 1), B8 (8, 13).
- Pits: (2, 5), (8, 3), (8, 7).
- NPCs: Cody (4, 1), Fran (4, 11). Solid barriers.
- Obstacles: Row 8 wall (2,8)-(4,8). Row 14/15 wall (7,14)-(7,15).
- Crossing Points: Row 13 gap at (4, 13).

# Time Tracking
- Puzzle Start Turn: 29931.
- Attempt 1: Turns 29931-30103. (Zero progress).
- Attempt 2 Start: Turn 30104.

# Strategy: Boulder Puzzle
- Goal: Drop all boulders into pits.
- Plan:
  1. Push B8 UP from (8, 13) towards (8, 7) Pit.
  2. Use dynamic `solve_blackthorn_boulders` for B6 and B7.
  3. Execute pushes precisely.