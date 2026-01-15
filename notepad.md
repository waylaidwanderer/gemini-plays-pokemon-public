# Tile Mechanics
- FLOOR_UP_WALL: Blocks SOUTH movement (acting as a ledge). Passable from SOUTH to NORTH.
- LEDGE_HOP_DOWN: Blocks NORTH movement. Found at Row 15 (X=3-17).
- ROCK: Smashable rocks act as WALLs.
- Vertical Walls: X=3, 5, 9, 11, 17, 20.

# Suicune Quest (Cianwood)
- Started: Turn 49630
## Strategy: Eastern Sea Bypass (Row 51 Highway)
Reach (14, 10) by surfing along the eastern coast to bypass internal walls.
1. Move East to (24, 45).
2. Surf South along X=24 to (24, 51).
3. Move West along Row 51 to (2, 51) (The Southern Highway).
4. Move North along X=2 corridor to (2, 12).
5. Move East along Row 12 to (14, 12).
6. Move North to (14, 10) to trigger Suicune.

# Progress Notes
- Blocked: X=10 corridor blocked by WALL at (10, 40).
- Blocked: X=12 corridor blocked by FLOOR_UP_WALL at (12, 50).
- Verified: X=24 corridor is clear from Row 45 to Row 51.
- Verified: Row 51 is a clear horizontal path from X=24 to X=2.
- Verified: X=2 corridor is clear from Row 51 up to Row 12.
- Verified: Row 12 is clear from X=2 to X=14.
- Hypothesis: Sea route bypasses all land-based dead ends. (Executing).