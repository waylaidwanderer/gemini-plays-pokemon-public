# Tile Mechanics
- FLOOR_UP_WALL: Blocks SOUTH movement (acting as a ledge). Passable from SOUTH to NORTH.
- LEDGE_HOP_DOWN: Blocks NORTH movement. Found at Row 15 (X=3-17).
- ROCK: Smashable rocks act as WALLs.
- Vertical Walls: X=3, 5, 9, 11, 17, 20.

# Suicune Quest (Cianwood)
- Started: Turn 49630
## Strategy: Verified Sea Route (Final)
Reach (14, 10) by surfing through the eastern gaps.
1. Move to (23, 16) and Up to (23, 15) (Gap 1).
2. Move East to (27, 15) and North to (27, 9) (Gap 2).
3. Move North to (27, 8) and West to (16, 8).
4. Move South to land at (16, 11) (Jumping ledge at 16, 10).
5. Walk to (14, 10) to trigger Suicune.

# Navigation Logic
- Buoy Walls: Horizontal (Row 15, Row 9) and Vertical (X=18, X=22, X=26).
- Gaps: Search for WATER tiles within BUOY lines to cross barriers.
- Landing: Look for FLOOR tiles adjacent to WATER to return to land.
- Priority: Stay on the far eastern edge (X=24+) to avoid internal city obstacles.