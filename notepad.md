# Tile Mechanics (Global)
- FLOOR: Standard walkable tile.
- WALL: Impassable collision (pillars, statues, rocks, NPCs).
- LADDER: Two-way warp between floors. (1, 7) and (7, 9).
- PIT: A hole that leads to 1F. Boulders fall through to fill gaps on 1F. Empty pits are impassable/warp for player on 2F.
- BOULDER: Pushable object. Requires STRENGTH. Pushing moves it one tile. Player STAYS in original tile. (Verified Turn 34566)

# Blackthorn Gym Puzzle Analysis
- Start Turn: 34501
- Goal: Fill three pits on 2F to bridge gaps on 1F.
- Boulders: B6 (3, 3), B7 (6, 1), B8 (8, 14) [Default Positions].
- Pits: P1 (8, 3), P2 (2, 5), P3 (8, 7).
- Critical Mechanic: Changing floors (using ladders) RESETS all boulder positions on 2F. (Verified Turn 34592).
- Connectivity (2F only):
  - Strip 1 (Cols 0-1) and Strip 2 (Cols 2-3) connect at Row 1.
  - Strip 2 (Cols 2-3) and Strip 3 (Cols 5-9) connect at Row 13 and Row 14 (Col 4 is FLOOR here).
  - Cody (4, 1) and Fran (4, 11) are solid walls.

# Strategy & Progress
- Status: On 1F (1, 6). Returning to 2F via ladder at (1, 7).
- Plan: Return to 2F, activate Strength, and use solve_blackthorn_boulders_v3 WITHOUT ladder shortcuts.

# Resource Locations
- Route 45: Good training spot for Haunter (Night Shade).