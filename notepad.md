# Tile Mechanics (Global)
- FLOOR: Standard walkable tile.
- WALL: Impassable collision (pillars, statues, rocks, NPCs).
- LADDER: Two-way warp between floors. (1, 7) and (7, 9).
- PIT: A hole that leads to 1F. Boulders fall through to fill gaps on 1F. Empty pits are impassable/warp for player on 2F.
- BOULDER: Pushable object. Requires STRENGTH. Pushing moves it one tile. Player STAYS in original tile. (Verified Turn 34566)

# Blackthorn Gym Puzzle Analysis
- Goal: Fill three pits on 2F to bridge gaps on 1F.
- Boulders: B6 (3, 3), B7 (6, 1), B8 (8, 14) [Default Positions].
- Pits: P1 (8, 3), P2 (2, 5), P3 (8, 7).
- Assignments: B6 -> P2 (2, 5), B7 -> P1 (8, 3), B8 -> P3 (8, 7).
- Connectivity:
  - Cody (4, 1) and Fran (4, 11) are solid.
  - Strip 1 (Cols 0-1) and Strip 2 (Cols 2-3) connect at Row 6/7.
  - Strip 2 (Cols 2-3) and Strip 3 (Cols 5-9) connect via ladders (1, 7) <-> (7, 9) on 1F.
  - Strips 1, 2, and 3 connect at Row 1 (Top) and Row 13 (Bottom).

# Strategy & Progress
- Status: Back on 2F (3, 4). B6 at (3, 3) confirmed. Strength NOT active.
- Plan: Activate Strength on B6, then follow master plan.

# Resource Locations
- Route 45: Good training spot for Haunter (Night Shade).