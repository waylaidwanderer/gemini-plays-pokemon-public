# Tile Mechanics (Global)
- FLOOR: Passable. Standard movement.
- WALL: Impassable silver blocks. Note: (7, 11) is a FAKE WALL (actually FLOOR).
- PIT: Player falls to 1F. Boulders falling in create bridges on 1F.
- LADDER: Warp between floors. Resets boulder positions. Deactivates Strength.

# Blackthorn Gym 2F Puzzle Analysis
- Start Turn: 30151
- Boulders: B6 (3, 3), B7 (6, 1), B8 (8, 14).
- Pits: P1 (2, 5), P2 (8, 3), P3 (8, 7).
- NPCs (Solid): Cody (4, 1), Fran (4, 11).
- Key Barriers: 
  - (8, 9) and (8, 8) are confirmed REAL WALLS.
  - (6, 0) is a confirmed REAL WALL.
  - (7, 11) is confirmed FAKE WALL (FLOOR) (Turn 30145).
- Hypotheses:
  - (7, 10) is FAKE WALL (FLOOR).
  - (5, 10) or (6, 10) might be involved.

# Strategy: Systematic Solver
1. Reactivate Strength (Done).
2. Verify (7, 11) and (7, 10) by walking on them.
3. Update solver with verified floor tiles and find solution.

# Progress Log
- Turn 30157: (6, 0) confirmed as REAL WALL.
- Turn 30159: Corrected pathing to avoid trainer at (4, 1). Heading to (7, 11).