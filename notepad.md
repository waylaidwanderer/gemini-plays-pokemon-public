# Blackthorn Gym (Puzzle Progress)
- Start Turn: 34763
- Pits (2F): P1 (8, 3), P2 (2, 5), P3 (8, 7).
- Boulders (2F): B6 (3, 3), B7 (6, 1), B8 (8, 14).
- Status: Strength is ACTIVE.

# Tile Mechanics (2F)
- WALL: Impassable. (4, 0-10, 12), (2, 8), (3, 8), (4, 8), (8, 8, 9).
- NPC: Impassable (Cody 4,1, Fran 4,11).
- Gap: (4, 13) is the only FLOOR tile connecting the left (Cols 0-3) and right (Cols 5-9) sides.
- Push Mechanic: Player stays in tile after push. (Confirmed Turn 34782).

# Puzzle Analysis (2F)
- P1 (8, 3) entry: (8, 2) DOWN. Stand at (8, 1).
- P2 (2, 5) entry: (1, 5) RIGHT. Stand at (0, 5).
- P3 (8, 7) entry: (8, 6) DOWN. Stand at (8, 5).
- Goal: B8 to P2 (2, 5), B6 to P3 (8, 7), B7 to P1 (8, 3).
- B8 (8, 14) -> P2 (2, 5) Path:
  1. Push B8 UP to (8, 13).
  2. Push B8 LEFT to (1, 13) via (4, 13).
  3. Push B8 UP to (1, 5).
  4. Push B8 RIGHT to (2, 5) PIT.
- B6 (3, 3) -> P3 (8, 7) Path:
  1. Push B6 DOWN to (3, 13).
  2. Push B6 RIGHT to (8, 13) via (4, 13).
  3. Push B6 UP to (8, 6).
  4. Push B6 DOWN to (8, 7) PIT.

# Strategy: Blackthorn Gym 2F
- Step 1: Push B8 to P2 (2, 5).
- Step 2: Push B6 to P3 (8, 7).
- Step 3: Push B7 to P1 (8, 3).

# Failed Hypotheses
- H1: Cody is passable. (Failed, Turn 34770)
- H2: B6 can reach P2 from the left side. (Failed, Turn 34775 - Col 4 blocks)
- H3: Player moves into tile after push. (Failed, Turn 34782)