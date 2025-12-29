# Tile Mechanics (Global)
- FLOOR: Passable terrain. Standard traversable.
- WALL: Impassable silver blocks. Absolute barrier.
- PIT: Hazardous for player (warp to 1F). Target for boulders (forms bridge on 1F).
- LADDER: Warp between floors. Deactivates Strength.
- Strength: Inactive. Reactivate by interacting with a boulder (A button).

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
  1. Navigate to (8, 15) to get behind Boulder 8.
  2. Activate Strength by facing UP and pressing A.
  3. Push B8 UP to (8, 13).
  4. Continue pushing B8 north to Pit (8, 7).
  5. Repeat for B6 and B7 using the dynamic solver.