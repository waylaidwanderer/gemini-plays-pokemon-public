# Tile Mechanics (Global)
- FLOOR: Passable. Standard movement.
- WALL: Impassable silver blocks. Absolute barrier to players and boulders.
- PIT: Player falls to 1F. Boulders falling in create bridges on 1F.
- LADDER: Warp between floors. Resets boulder positions. Deactivates Strength.

# Blackthorn Gym 2F Puzzle Analysis
- Start Turn: 30151
- Boulders: B6 (3, 3), B7 (6, 1), B8 (8, 14).
- Pits: P1 (2, 5), P2 (8, 3), P3 (8, 7).
- NPCs (Solid): Cody (4, 1), Fran (4, 11).
- Key Barriers: 
  - (8, 9) and (8, 8) are WALLS, blocking B8 from a direct north push to P3.
  - (7, 10) is a WALL.
  - (4, 0) to (4, 12) is a vertical WALL line.
  - (2, 10) to (2, 17) is a vertical WALL line.
- Verified Constraints:
  - B8 cannot be pushed north past (8, 10).
  - B8 cannot be pushed left at y=12, 13, 14 due to walls at x=9 blocking player.
  - B8 cannot be pushed left at y=11 due to wall at (7, 11).

# Strategy: Systematic Solver
1. Reactivate Strength.
2. Use a comprehensive Sokoban solver (via run_code) that accounts for:
   - Player positioning requirements for every push.
   - Map boundaries and internal walls.
   - Static NPCs.
   - Boulder-boulder collisions.
3. Execute the resulting sequence precisely.

# Progress Log
- Turn 30148: Floor reset. Boulders at initial positions.
- Turn 30151: Strength activation in progress.

# Solver Failure Analysis
- Turn 30151: solver_blackthorn_boulders and run_code (custom solver) both returned "No solution found".
- Implication: The puzzle is unsolvable with current map data (internal walls).
- Hypothesis: Some "WALL" tiles are actually passable.
- Target: Row 0 (0-9, 0) and surrounding "silver blocks".
- Plan: Navigate to (6, 1) and test Up into (6, 0).

# Observation: Boulder 7 Displacement
- Turn 30155: Pushed Boulder 7 from (6, 1) to (7, 1) while navigating to (6, 1).
- Status: Boulder 7 is now at (7, 1). Tile (6, 1) is now clear FLOOR.
- Current Test: Moving to (6, 1) and testing UP into (6, 0).