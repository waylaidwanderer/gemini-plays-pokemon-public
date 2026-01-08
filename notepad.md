# Blackthorn Gym (Puzzle Progress)
- Start Turn: 34763
- Pits: P1 (8, 3), P2 (2, 5), P3 (8, 7).
- Boulders (Reset): B6 (3, 3), B7 (6, 1), B8 (8, 12).
- Status: Strength ACTIVE.
- Verified Walls: (4, 10), (4, 11), (4, 12), (8, 9).

# Puzzle Analysis (2F)
- Problem: B8 (8, 12) is trapped if (7, 11) and (9, 12/13) are walls.
- Goal: Verify (7, 11) collision. If it's floor, B8 can be pushed right into Column 9.
- Goal: Search for a 4th boulder in the corners.

# Strategy: Blackthorn Gym 2F
- Step 1: Test Fran (4, 11) collision.
- Step 2: If failed, exit Gym to attempt full reset.
- Step 3: Map out Column 6 and 5 for alternative routes.