# Tile Mechanics
- FLOOR_UP_WALL: Blocks SOUTH. Allows NORTH. Verified: Down at (24, 45) failed (Turn 49602).
- LEDGE_HOP_DOWN: Blocks NORTH. Found at Row 15 (X=3-17).
- ROCK: Smashable rocks act as WALLs.
- Vertical Walls: X=3, 5, 9, 11, 17, 20.

# Suicune Quest (Cianwood)
## Strategy: Internal Maze Loop
Reach (14, 10) by navigating the internal corridors to bypass walls/ledges.
1. Move East along Row 44 to (12, 44).
2. Move North along X=12 to (12, 33).
3. Move West through gap at (9, 33) to (6, 33).
4. Move North along X=6 to (6, 26).
5. Move West through gap at (5, 26) to (4, 26).
6. Move South along X=4 to (4, 51).
7. Move West along Row 51 to (2, 51).
8. Walk North along X=2 to (2, 12).
9. Walk East along Row 12 to (14, 12) and North to (14, 10).
- Current Step: Navigating to (12, 33) via Row 44 and X=12 corridor.

# Progress Notes
- Blocked: X=5 wall at Row 44 (Turn 49641).
- Blocked: X=7 wall at Row 47 (Turn 49640).
- Blocked: X=11 wall at Row 49 (Turn 49640).
- Blocked: Row 46 ledge (X=6) blocks South.
- Verified: X=4 corridor is clear from Row 26 to Row 51.
- Verified: X=6 corridor is clear from Row 33 to Row 26.
- Verified: X=12 corridor is clear from Row 44 to Row 33.
- Gap (9, 33): Allows crossing X=9 wall.
- Gap (5, 26): Allows crossing X=5 wall.
- Row 12: Clear horizontal path from X=2 to X=14.
- Row 51: Clear horizontal path from X=4 to X=2.