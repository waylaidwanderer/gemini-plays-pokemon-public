# Blackthorn Gym (Puzzle Progress)
- Start Turn: 34763
- Pits (2F): P1 (8, 3), P2 (2, 5), P3 (8, 7).
- Boulders (2F): B6 (3, 5), B7 (6, 1), B8 (8, 12).
- Status: Strength is ACTIVE.

# Tile Mechanics (2F)
- WALL: Impassable. (4, 0-10, 12), (2, 8), (3, 8), (4, 8), (8, 8, 9), (9, 12-17).
- Gap: (4, 13) is the primary connection between left and right.
- Push Mechanic: Player stays in tile after push. (Confirmed Turn 34791).

# Puzzle Analysis (2F)
- B7 (6, 1) -> P1 (8, 3) Path: (6, 1) -> (8, 1) -> (8, 2) -> P1.
- B8 (8, 12) -> P2 (2, 5) Path: (8, 12) -> (8, 13) -> (4, 13) -> (0, 13) -> (0, 5) -> (1, 5) -> P2.
- B6 (3, 5) -> P3 (8, 7) Path: (3, 5) -> (3, 13) -> (4, 13) -> (8, 13) -> (8, 11) -> (9, 11) -> (9, 7) -> P3.

# Strategy: Blackthorn Gym 2F
- Step 1: Push B8 (8, 12) to (8, 13).
- Step 2: Push B8 across to the left side.
- Step 3: Push B6 (3, 5) to the right side.
- Step 4: Complete P1, P2, P3.

# Failed Hypotheses
- H1: Cody is passable. (Failed, Turn 34770)
- H2: B6 can reach P2 from the left side. (Failed, Turn 34775 - Col 4 blocks)
- H3: Player stays in tile after push. (Failed, Turn 34782)