# Tile Mechanics (Global)
- FLOOR: Passable. Standard movement.
- WALL: Impassable silver blocks.
- Verified REAL Walls: (6, 0), (7, 11), (8, 9), (7, 10), (5, 12).
- Verified FLOOR: (7, 12), (7, 13), (4, 11).

# Blackthorn Gym 2F Puzzle Analysis
- Start Turn: 30151
- Boulders: B6 (3, 3), B7 (7, 1), B8 (8, 14).
- Pits: P1 (2, 5), P2 (8, 3), P3 (8, 7).
- NPCs (Solid): Cody (4, 1), Fran (4, 11).
- Problem: B8 is currently blocked from reaching P3 by real walls at (8, 9), (7, 10), and (7, 11). Direct northern and western paths from its current corridor are sealed.

# Strategy: Systematic Fake Wall Search
1. B8 is likely the last boulder to solve. Focus on B6 and B7 first.
2. B6 at (3, 3) needs to reach P1 at (2, 5).
   - Hypothesis: Tile (4, 3) or (4, 5) is a FAKE WALL (FLOOR). This would allow pushing B6 left.
   - Hypothesis: Tile (2, 3) or (2, 4) is a FAKE WALL (FLOOR). This would allow pushing B6 into the pit from the right.
3. B7 at (7, 1) needs to reach P2 at (8, 3).
   - Hypothesis: Tile (8, 0), (8, 1), or (8, 2) is a FAKE WALL (FLOOR).
4. Test x=4 wall by walking on it. Starting with (4, 3).