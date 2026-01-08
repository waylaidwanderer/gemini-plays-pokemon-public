# Blackthorn Gym (Puzzle Progress)
- Start Turn: 34763
- Pits (2F): P1 (8, 3), P2 (2, 5), P3 (8, 7).
- Boulders (2F): B6 (3, 3), B7 (6, 1), B8 (8, 11).
- Status: Strength is ACTIVE.

# Game Mechanics
- Strength: Deactivated when changing maps or using ladders. Must be re-activated on a boulder.
- Pushing: 
  - Hypothesis: The first push (with text box) keeps player in place. Subsequent pushes move player into the boulder's old tile.
  - Verification: Test at Turn 34831.
- Ladders: (1, 7) and (7, 9) reset boulder positions on 2F.

# Tile Mechanics (2F)
- WALL: Impassable. (4, 0, 2-10, 12), (2, 8), (3, 8), (4, 8), (8, 8, 9), (7, 10, 11), (9, 12-17).
- GAP: (4, 1) and (4, 13-17) are passable.
- NPC: Fran at (4, 11) is passable after defeat? (Verify).

# Strategy: Blackthorn Gym 2F
- Step 1: Verify push mechanic.
- Step 2: Define robust BFS tool for boulder navigation.
- Step 3: Solve puzzle.