# Tile Mechanics
- FLOOR_UP_WALL: Blocks SOUTH movement (acting as a ledge). Passable from SOUTH to NORTH.
- LEDGE_HOP_DOWN: Blocks NORTH movement. Found at Row 15 (X=3-17).
- ROCK: Smashable rocks act as WALLs.
- Vertical Walls: X=3, 5, 9, 11, 17, 20.

# Suicune Quest (Cianwood)
- Started: Turn 49630
## Strategy: Sea Route Bypass (Final)
Reach (14, 10) by surfing around the city via the eastern gap.
1. SURF from (23, 33) into the eastern sea. (Done)
2. Use SUPER REPEL to bypass encounters. (Done)
3. Move North to (24, 15) and West to (23, 15) (Gap in Row 15 BUOY wall).
4. Move North along X=23/24 to Row 9.
5. Move East to (27, 9) (Gap in Row 9 BUOY wall).
6. Move North to Row 8 and West to (16, 8) (Above the plateau).
7. Move South to land at (16, 11) and walk to (14, 10).

# Navigation Logic
- Buoy Walls: Horizontal (Row 15, Row 9) and Vertical (X=18, X=22, X=26).
- Gaps: Search for WATER tiles within BUOY lines to cross barriers.
- Landing: Look for FLOOR tiles adjacent to WATER to return to land.
- Priority: Stay on the far eastern edge (X=24+) to avoid internal city obstacles.