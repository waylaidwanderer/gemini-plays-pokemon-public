# Tile Mechanics (Global)
- FLOOR: Passable terrain.
- WALL: Impassable silver blocks.
- PIT: Player falls to 1F. Boulder destination (forms bridge on 1F).
- LADDER: Warp between floors. Deactivates Strength.
- Strength: Active (Turn 30101).

# Blackthorn Gym 2F State
- Boulders (Verified): B6 (3, 3), B7 (6, 1), B8 (8, 14).
- Pits (Unfilled): (2, 5), (8, 3), (8, 7).
- NPCs: Cody (4, 1), Fran (4, 11). Solid barriers.
- Obstacles: Row 8 (2,8)-(4,8) is a wall. Row 14/15 (7,14)-(7,15) is a wall.
- Crossing Points: Row 13 (4, 13) is a gap in the central wall. Row 16 (6,16)-(8,16) allows bypassing the bottom-right walls.

# Time Tracking
- Puzzle Start Turn: 29931.
- Current Attempt Start: Turn 30091.

# Strategy: Boulder Puzzle
- Goal: Drop all boulders into pits.
- Plan:
  1. Activate Strength at (8, 15) by facing Boulder 8 and selecting YES.
  2. Clear confirmation text.
  3. Use `solve_blackthorn_boulders` (dynamic version) to get the push sequence.
  4. Execute pushes for B8, then B6 and B7.