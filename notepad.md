# Blackthorn Gym (Puzzle Progress)
- Start Turn: 34763
- Pits (2F): P1 (8, 3), P2 (2, 5), P3 (8, 7).
- Boulders (2F): B6 (3, 3), B7 (6, 1), B8 (8, 11).
- Status: Strength is ACTIVE. Boulders RESET.

# Tile Mechanics (2F)
- WALL: Impassable. (4, 0-12), (2, 8), (3, 8), (4, 8), (8, 8, 9), (7, 10, 11), (9, 12+).
- LADDER: Impassable for boulders. (1, 7), (7, 9).
- Gap: (4, 13) is the primary connection between left and right.
- Push Mechanic: Player STAYS in their tile after a push. (Verified Turn 34791, 34815).

# Puzzle Analysis (2F)
- Strategy:
  1. B8 (8, 14) -> P2 (2, 5) via Row 13 and Column 0.
  2. B6 (3, 3) -> P3 (8, 7) via Row 13 and Column 8.
  3. B7 (6, 1) -> P1 (8, 3) via Column 8.

# Strategy: Blackthorn Gym 2F
- Step 1: Activate Strength.
- Step 2: Push B8 (8, 14) to (8, 13).
- Step 3: Push B8 to (0, 13).
- Step 4: Push B8 to P2 (2, 5).
- Step 5: Push B6 to P3 (8, 7).
- Step 6: Push B7 to P1 (8, 3).

# Failed Hypotheses
- H1: Cody is passable. (Failed, Turn 34770)
- H2: B6 can reach P2 from the left side. (Failed, Turn 34775 - Col 4 blocks)
- H3: Player stays in tile after push. (Failed, Turn 34782)
- H4: B8 can reach pits via Column 8. (Failed, Turn 34801 - (8, 9) is WALL)