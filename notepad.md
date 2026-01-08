# Blackthorn Gym (Puzzle Progress)
- Start Turn: 34763
- Pits (2F): P1 (8, 3), P2 (2, 5), P3 (8, 7).
- Boulders (2F): B6 (3, 5), B7 (6, 1), B8 (8, 10).
- Status: Strength is ACTIVE. Boulder 8 is STUCK at (8, 10). Resetting via ladder.

# Tile Mechanics (2F)
- WALL: Impassable. (4, 0-12), (2, 8), (3, 8), (4, 8), (8, 8, 9), (7, 10, 11), (9, 12+).
- LADDER: Impassable for boulders. (1, 7), (7, 9).
- Gap: (4, 13) is the primary connection between left and right.
- Push Mechanic: Player moves into the tile previously occupied by the boulder.

# Puzzle Analysis (2F)
- Reset Strategy:
  - B8 (8, 14) -> (8, 13) -> (0, 13) -> (0, 5) -> (1, 5) -> P2 (2, 5).
  - B6 (3, 2) -> (3, 13) -> (5, 13) -> (5, 5) -> (8, 5) -> (8, 6) -> P3 (8, 7).
  - B7 (6, 1) -> (8, 1) -> (8, 2) -> P1 (8, 3).

# Strategy: Blackthorn Gym 2F
- Step 1: Reach ladder (7, 9) to reset boulders.
- Step 2: Push B8 to P2 via the long western route.
- Step 3: Push B6 to P3 via the central gap.
- Step 4: Push B7 to P1.

# Failed Hypotheses
- H1: Cody is passable. (Failed, Turn 34770)
- H2: B6 can reach P2 from the left side. (Failed, Turn 34775 - Col 4 blocks)
- H3: Player stays in tile after push. (Failed, Turn 34782)
- H4: B8 can reach pits via Column 8. (Failed, Turn 34801 - (8, 9) is WALL)