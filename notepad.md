# Blackthorn Gym (Puzzle Progress)
- Start Turn: 34763
- Pits: P1 (8, 3), P2 (2, 5), P3 (8, 7).
- Boulders Found: B6 (3, 3), B7 (6, 1), B8 (8, 14).
- Status: Strength ACTIVE.

# Puzzle Analysis (2F)
- Key Insight: Boulders can cross between the left side (Cols 0-3) and right side (Cols 5-9) via the gaps at (4, 1) [Cody] and (4, 13) [South Gap].
- Root Assumption Corrected: Boulder 8 does NOT have to stay on the right side, and B6/B7 do not have to stay on the left/middle.
- Mechanics Verified:
  - Pushing: Player moves into the boulder's old tile after a push.
  - Reset: Ladders (1, 7) and (7, 9) reset boulder positions.

# Strategy: Blackthorn Gym 2F
- Step 1: Run BFS solver to find the optimal sequence of pushes across the gaps.
- Step 2: Execute the sequence.
- Step 3: Challenge Gym Leader Clair.

# Tile Mechanics (2F)
- WALL: (4, 0, 2-10, 12), (2, 8), (3, 8), (4, 8), (8, 8, 9), (7, 10, 11, 14, 15), (9, 12-17).
- GAP: (4, 1) and (4, 13-17) are passable.
- LADDER: Walkable for player, impassable for boulders.
- PIT: Target for boulders, warp for player.