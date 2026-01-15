# Tile Mechanics
- FLOOR_UP_WALL: Blocks SOUTH movement. Passable from SOUTH to NORTH (Hypothesis).
- LEDGE_HOP_DOWN: Blocks NORTH movement. Found at Row 15 (X=3-17).
- ROCK: Smashable rocks act as WALLs.
- Vertical Walls: X=3, 5, 7, 9, 11, 17, 20.

# Suicune Quest (Cianwood)
- Started: Turn 49630
## Strategy: The Ultimate Land Bypass (Final)
Reach (14, 10) by navigating internal land corridors to reach the X=2 highway.
1. Move West to (8, 46) via Row 45 detour (around Pokefan F at 10, 46).
2. Move South to (8, 48) and West to (6, 48) (Crossing X=7 gap at 7, 48).
3. Move North along X=6 to (6, 35).
4. Move West to (2, 35) (Crossing X=5 gap at 5, 35 and X=3 gap at 3, 35).
5. Move North along X=2 highway to (2, 12) (Bypassing Row 15 ledge).
6. Move East along Row 12 to (14, 12).
7. Move North to (14, 10) to trigger Suicune.

# Verification Notes
- X=2 is a clear vertical highway from Row 51 to Row 14.
- Row 12 is a clear horizontal highway from X=2 to X=16.
- Gaps: (11, 46), (7, 48), (5, 35), (3, 35).
- Hypothesis: FLOOR_UP_WALL at (6, 46) allows NORTH progress (Testing at Step 3).
- SUPER REPEL is active (Turn 49722).