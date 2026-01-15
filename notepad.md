# Tile Mechanics
- FLOOR_UP_WALL: Blocks SOUTH movement (acting as a ledge). Passable from SOUTH to NORTH.
- LEDGE_HOP_DOWN: Blocks NORTH movement. Found at Row 15 (X=3-17).
- ROCK: Smashable rocks act as WALLs.
- Vertical Walls: X=3, 5, 9, 11, 17, 20.

# Suicune Quest (Cianwood)
- Started: Turn 49630
## Strategy: Verified Sea Route (Refined)
Reach (14, 10) by surfing through specific buoy and wall gaps.
1. Move Right to (27, 15).
2. Move North to (27, 10).
3. Move West to (23, 10) (Bypasses X=26 wall).
4. Move North to (23, 8) and West to (19, 8) (Bypasses X=22 wall).
5. Move South to (19, 11) and West to land at (16, 11).
6. Walk to (14, 10) to trigger Suicune.

# Navigation Logic
- Buoy Walls: Horizontal (Row 15, Row 9) and Vertical (X=18, X=22, X=26).
- Gaps: Search for WATER tiles within BUOY lines to cross barriers.
- Landing: Look for FLOOR tiles adjacent to WATER to return to land.
- Priority: Stay on the far eastern edge (X=24+) to avoid internal city obstacles.