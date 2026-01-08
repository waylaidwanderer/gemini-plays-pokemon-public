# Blackthorn Gym (Puzzle Progress)
- Start Turn: 34763
- Pits (2F): P1 (8, 3), P2 (2, 5), P3 (8, 7).
- Boulders (2F): B6 (3, 3), B7 (6, 1), B8 (8, 12).
- Status: Strength is ACTIVE. Boulders RESET.
- Push Mechanic: Player moves into boulder's old tile (Push 2+).

# Puzzle Analysis (2F)
- Gaps in Column 4: (4, 1) [Cody gone], (4, 11) [Fran blocked], (4, 13-17) [Open].
- Boulder 8 is in Column 8 pocket.
- Goal: Move to (4, 13) to verify path to right side and run full solver.

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