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
- Assignments Hypothesis:
  - B6 -> Pit P2 (2, 5)
  - B7 -> Pit P1 (8, 3)
  - B8 -> Pit P3 (8, 7)
- Connectivity:
  - Cody (4, 1) and Fran (4, 11) are solid.
  - Strip 1 (Cols 0-1) and Strip 2 (Cols 2-3) connect at Row 1 and Rows 13-17.
  - Strip 2 (Cols 2-3) and Strip 3 (Cols 5-9) connect via ladders (1, 7) <-> (7, 9) on 1F.
  - Strip 3 (Cols 5-9) is mostly open but has internal walls.

# Strategy & Progress
- Status: On 1F (1, 6), returning to 2F. Strength active.
- Plan: Verify if B6 reset to (3, 3) or remained at (3, 5) upon return to 2F.

# Resource Locations
- Route 45: Good training spot for Haunter (Night Shade).