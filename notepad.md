# Tile Mechanics
- FLOOR_UP_WALL: Blocks SOUTH movement (acting as a ledge). Passable from SOUTH to NORTH.
- LEDGE_HOP_DOWN: Blocks NORTH movement. Found at Row 15 (X=3-17).
- ROCK: Smashable rocks act as WALLs.
- Vertical Walls: X=3, 5, 9, 11, 17, 20.

# Suicune Quest (Cianwood)
## Strategy: Great Southern Loop (Refined)
Reach (14, 10) by bypassing all internal obstacles via the far southern and western corridors.
1. Move East to (10, 33).
2. Move South along X=10 to (10, 51) (passing through ledge gap at 10, 50).
3. Move West along Row 51 to (2, 51).
4. Move North along X=2 to (2, 14).
5. Move East to (5, 14) and North to (5, 12).
6. Move East along Row 12 to (14, 12).
7. Move North to (14, 10) to trigger Suicune.

# Progress Notes
- Verified: (10, 50) is a clear gap in the southern ledge.
- Verified: Row 51 is a clear horizontal path from X=10 to X=4.
- Verified: X=2 corridor is clear from Row 51 to Row 14.
- Verified: Row 12 is a clear horizontal path from X=5 to X=14.
- Blocked: X=4 corridor blocked by ledge (FLOOR_UP_WALL) at (4, 30).
- Blocked: X=6 corridor blocked by ledge (FLOOR_UP_WALL) at (6, 34).
- Blocked: X=12 corridor blocked by ledge (FLOOR_UP_WALL) at (12, 50).