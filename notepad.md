# Blackthorn Gym (Puzzle Progress)
- Start Turn: 34763
- Pits: P1 (8, 3), P2 (2, 5), P3 (8, 7).
- Boulders (Reset): B6 (3, 3), B7 (6, 1), B8 (8, 14).
- Status: Strength ACTIVE.

# Game Mechanics
- Strength: Deactivated by ladders/warps.
- Pushing: Player moves into boulder's old tile. (Verified Turn 34856).
- Reset: Ladders (1, 7) and (7, 9) reset boulders.

# Tile Mechanics (2F)
- WALL: (4, 0, 2-10, 12), (2, 8), (3, 8), (4, 8), (8, 8, 9), (7, 10, 11, 14, 15), (9, 12-17).
- GAP: (4, 1) and (4, 13-17) are passable.
- B8 Status: Testing if (8, 9) is a WALL by pushing B8 UP.
- Goal: Push B8 (8, 12) -> (8, 11) -> (8, 10) -> (8, 9).
- Verified: (9, 13) is a WALL. (4, 12) is a WALL. (7, 10, 11) are WALLs.

# Strategy: Blackthorn Gym 2F
- Step 1: Verify Column 9 collision at (9, 13).
- Step 2: Verify Column 7 collision at (7, 13).
- Step 3: Use run_code BFS solver with verified map.