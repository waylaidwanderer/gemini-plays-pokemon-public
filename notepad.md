# Blackthorn Gym (Puzzle Progress)
- Start Turn: 34763
- Pits: P1 (8, 3), P2 (2, 5), P3 (8, 7).
- Boulders (Reset): B6 (3, 3), B7 (6, 1), B8 (8, 14).
- Status: Strength ACTIVE.

# Game Mechanics
- Strength: Deactivated by ladders/warps.
- Pushing: Player moves into boulder's old tile. (Verified Turn 34814).
- Reset: Ladders (1, 7) and (7, 9) reset boulders.

# Tile Mechanics (2F)
- WALL: (4, 0, 2-10, 12), (2, 8), (3, 8), (4, 8), (8, 8, 9), (7, 10, 11), (9, 12-17).
- GAP: (4, 1) and (4, 13-17) are passable.
- B8 Status: Trapped in Col 8 corridor if (8, 9) is WALL.

# Strategy: Blackthorn Gym 2F
- Step 1: Clear text at (8, 15).
- Step 2: Push B8 UP to (8, 13) and check if I move to (8, 14).
- Step 3: Run comprehensive BFS solver to find path for B6 and B7 if B8 is stuck.