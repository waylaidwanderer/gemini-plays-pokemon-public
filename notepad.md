# Tile Mechanics
- FLOOR_UP_WALL: Blocks SOUTH. Allows NORTH. Verified: Down at (24, 45) failed (Turn 49602).
- LEDGE_HOP_DOWN: Blocks NORTH. Found at Row 15 (X=3-17).
- ROCK: Smashable rocks act as WALLs.
- Vertical Walls: X=3, 5, 9, 11, 17, 20.

# Suicune Quest (Cianwood)
## Strategy: The S-Curve Maze Bypass
Reach (14, 10) by navigating internal corridors to avoid all dead ends.
1. Move West to (6, 33) via gaps at (9, 33) and (7, 33).
2. Move North along X=6 to (6, 29).
3. Move West through gap at (5, 29) to (4, 29).
4. Move North along X=4 to (4, 22).
5. Move West through gap at (3, 22) to (2, 22) (Western Corridor).
6. Walk North along X=2 to (2, 12) (bypasses Row 15 ledge).
7. Walk East along Row 12 to (14, 12) and North to (14, 10).
- Current Step: Navigating to (2, 12) via the S-curve.

# Progress Notes
- Verified: Row 29 gap at (5, 29) crosses X=5 wall.
- Verified: Row 22 gap at (3, 22) crosses X=3 wall.
- Verified: X=2 corridor is clear from Row 22 to Row 12.
- Blocked: Row 34 ledge (X=6-8) is a wall from the North (FLOOR_UP_WALL).
- Blocked: X=14 corridor blocked by water at Row 27.
- Blocked: X=9 corridor blocked by wall at Row 30.
- Blocked: X=5 wall solid at Row 33.
- Blocked: X=3 wall solid at Row 23-33.
- Row 12: Clear horizontal path from X=2 to X=14.