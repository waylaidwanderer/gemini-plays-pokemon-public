# Tile Mechanics (Global)
- FLOOR: Passable. Standard movement.
- WALL: Impassable silver blocks.
- Verified REAL Walls: (6, 0), (7, 11), (8, 9), (7, 10).
- Verified FLOOR: (7, 12), (7, 13).

# Blackthorn Gym 2F Puzzle Analysis
- Start Turn: 30151
- Boulders: B6 (3, 3), B7 (6, 1), B8 (8, 14).
- Pits: P1 (2, 5), P2 (8, 3), P3 (8, 7).
- NPCs (Solid): Cody (4, 1), Fran (4, 11).
- Problem: B8 is currently blocked from reaching P3 by real walls at (8, 9) and (7, 10).

# Strategy: Fake Wall Identification
1. Use analyze_missing_links to test which silver blocks must be floor for a solution to exist.
2. Systematically test those tiles by walking on them or pushing boulders into them.
3. Once the 'fake' path is found, execute the solution.

# Progress Log
- Turn 30160: (7, 11) confirmed as REAL WALL.
- Turn 30161: Moving to (8, 15) to prepare for B8 pushes while analyzing map links.