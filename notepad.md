# Blackthorn Gym (Puzzle Progress)
- Start Turn: 34763
- Pits (2F): P1 (8, 3), P2 (2, 5), P3 (8, 7).
- Boulders (2F): B6 (3, 3), B7 (6, 1), B8 (8, 12).
- Status: Strength is ACTIVE. Boulders RESET.
- Push Mechanic: Player moves into boulder's old tile. (Verified Turn 34815).

# Puzzle Analysis (2F)
- Pits: P1 (8, 3), P2 (2, 5), P3 (8, 7).
- Boulders: B6 (3, 3), B7 (6, 1), B8 (8, 12).
- Gaps in Col 4: (4, 1) [Cody gone], (4, 13-17) [Open].
- Strategy:
  1. B7 (6, 1) -> P1 (8, 3).
  2. B6 (3, 3) -> P2 (2, 5) via (3, 13) -> (1, 13) -> (1, 5) -> P2.
  3. B8 (8, 12) -> P3 (8, 7) via (8, 5) -> (5, 5) -> (5, 7) -> (7, 7) -> P3.

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