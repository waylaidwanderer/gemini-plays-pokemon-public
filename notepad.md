# Tile Mechanics
- FLOOR_UP_WALL: Blocks SOUTH. Allows NORTH. Verified: Down at (24, 45) failed (Turn 49602).
- LEDGE_HOP_DOWN: Blocks NORTH. Found at Row 15 (X=3-17).
- ROCK: Smashable rocks act as WALLs.
- Vertical Walls: X=3, 5, 9, 11, 17, 20.

# Suicune Quest (Cianwood)
## Strategy: Great Southern Loop (Refined)
Reach (14, 10) by bypassing all land ledges via the Row 50 gap at (10, 50).
1. Move South along X=12 to (12, 49).
2. Move West along Row 49 to (10, 49).
3. Move South to (10, 50) (Ledge Gap).
4. Move West along Row 50 to (2, 50) (Western Corridor).
5. Walk North along X=2 to (2, 12) (bypasses Row 15 ledge).
6. Walk East along Row 12 to (14, 12).
7. Walk North to (14, 10).
- Current Step: Moving to (2, 51) via the 'Outer Western Loop' (Row 44 detour).

# Progress Notes
- Verified: (10, 50) is FLOOR (Ledge Gap).
- Verified: (12, 50) is FLOOR_UP_WALL (Blocks South).
- Verified: Row 49 is a clear horizontal path from X=12 to X=10.
- Verified: X=2 corridor (Row 50 to Row 12) bypasses the Row 15 ledge (X=3-17).
- Verified: Row 12 is a clear horizontal path from X=2 to X=14.
- Failed Attempt: Upper Western Bypass blocked by FLOOR_UP_WALL at (4, 30) and (6, 34).
- Failed Attempt: Moving Down at (7, 33) into FLOOR_UP_WALL (Turn 49633). Row 34 is a ledge.