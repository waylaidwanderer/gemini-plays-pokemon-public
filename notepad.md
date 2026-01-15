# Tile Mechanics
- FLOOR_UP_WALL: Blocks SOUTH. Allows NORTH. Verified: Down at (24, 45) failed (Turn 49602).
- LEDGE_HOP_DOWN: Blocks NORTH. Found at Row 15 (X=3-17).
- ROCK: Smashable rocks act as WALLs.
- Vertical Walls: X=3, 5, 9, 11, 17, 20.

# Suicune Quest (Cianwood)
## Strategy: Western Bypass (Row 33/34)
Reach (14, 10) by bypassing ledges via the western corridor (X=2).
1. Move North along X=12 to (12, 33).
2. Move West through gap at (9, 33) to (6, 33).
3. Move South to (6, 34) and West through gap at (5, 34) to (4, 34).
4. Move South along X=4 to Row 51.
5. Move West along Row 51 to X=2 corridor.
6. Walk North along X=2 to Row 12 (bypasses Row 15 ledge).
7. Walk East to (14, 12) and North to (14, 10).
- Current Step: Navigating to (12, 33).

# Progress Notes
- X=4 Corridor: Clear from Row 34 to Row 51.
- Gap at (5, 34): Allows crossing X=5 wall.
- Gap at (9, 33): Allows crossing X=9 wall.
- Verified: Row 34 ledge (X=6-8) blocks South from (6, 33) to (6, 34). Wait, (6, 34) is the ledge.
- So (6, 33) to (6, 34) is DOWN onto a ledge. That works!
- Once on (6, 34), I can move West to (5, 34).
- X=2 Corridor: Clear from Row 51 to Row 12.
- Failed Attempt: Moving Down at (7, 33) into FLOOR_UP_WALL (Turn 49633). Row 34 is a ledge.