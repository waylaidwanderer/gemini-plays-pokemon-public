# Tile Mechanics (Global)
- FLOOR: Passable.
- WALL: Impassable silver blocks. (8, 8) is solid.
- PIT: Warp for player (to 1F). Target for boulders. (8, 7) is empty.
- LADDER: Warp between floors. Deactivates Strength.
- Strength: Inactive. Reactivate by interacting with a boulder (A button).

# Blackthorn Gym 2F State
- Boulders: B6 (3, 3), B7 (6, 1), B8 (8, 11).
- Pits: (2, 5), (8, 3), (8, 7).
- NPCs: Cody (4, 1), Fran (4, 11). Both solid barriers.
- Barriers: Column 4 is a wall from Row 0-12 (except Cody/Fran). Column 2 is a wall from Row 10-17. Row 8 wall at (2,8)-(4,8).

# Time Tracking
- Puzzle Start Turn: 29931.
- Attempt 1: Turns 29931-30103. (Zero progress).
- Attempt 2 Start: Turn 30104.

# Strategy: Boulder Puzzle
- Goal: Fill all pits with boulders.
- Plan:
  1. Navigate to (8, 12) to get behind Boulder 8.
  2. Activate Strength by facing UP and pressing A.
  3. Use `puzzle_analyst` to determine the high-level sequence.
  4. Use `solve_blackthorn_boulders` to get specific button presses.
  5. Execute pushes carefully.