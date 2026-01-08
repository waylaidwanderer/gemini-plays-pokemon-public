# Blackthorn Gym (Puzzle Progress)
- Start Turn: 34763
- Pits: P1 (8, 3), P2 (2, 5), P3 (8, 7).
- Boulders (Reset): B6 (3, 3), B7 (6, 1), B8 (8, 12).
- Status: Strength ACTIVE.
- Verified Walls: (4, 10), (4, 11), (4, 12), (8, 9).

# Puzzle Analysis (2F)
- Pushing: Player ALWAYS stays in their current tile after a push. (Verified Turn 34815, 34850, 34868).
- B8 Verification: Pushing B8 UP to test if (8, 9) is truly a wall.
- B8 Backup Strategy: If (8, 9) is WALL, push B8 DOWN to Row 13, then across to Column 6 to reach P3 (8, 7).
- B6/B7 Strategy: Use Row 1 gaps to reach opposite pits.

# Strategy: Blackthorn Gym 2F
- Step 1: Test Fran (4, 11) collision.
- Step 2: If failed, exit Gym to attempt full reset.
- Step 3: Map out Column 6 and 5 for alternative routes.