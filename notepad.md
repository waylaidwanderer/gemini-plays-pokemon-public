# Tile Mechanics
- FLOOR_UP_WALL: Blocks SOUTH movement (acting as a ledge). Passable from SOUTH to NORTH.
- LEDGE_HOP_DOWN: Blocks NORTH movement. Found at Row 15 (X=3-17).
- ROCK: Smashable rocks act as WALLs.
- Vertical Walls: X=3, 5, 9, 11, 17, 20.

# Suicune Quest (Cianwood)
- Started: Turn 49630
## Strategy: Zigzag Sea Route (Verified Logic)
Reach (14, 10) by surfing through specific buoy gaps.
1. Surf North along X=24 to (24, 16).
2. Move West along Row 16 to (20, 16) (Bypasses X=22 wall).
3. Move North along X=20 to (20, 14) (Bypasses Row 15 wall).
4. Move West along Row 14 to (18, 14) (Bypasses X=19 wall).
5. Move North/West to find landing point at (16, 11) or nearby.
6. Walk to (14, 10) to trigger Suicune.

# Navigation Logic
- Buoy Walls: Horizontal (Row 15, Row 9) and Vertical (X=18, X=22, X=26).
- Gaps: Search for WATER tiles within BUOY lines to cross barriers.
- Landing: Look for FLOOR tiles adjacent to WATER to return to land.
- Priority: Stay on the far eastern edge (X=24+) to avoid internal city obstacles.