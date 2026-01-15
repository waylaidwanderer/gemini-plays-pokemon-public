# Tile Mechanics
- FLOOR_UP_WALL: Blocks SOUTH movement (acting as a ledge). Passable from SOUTH to NORTH.
- LEDGE_HOP_DOWN: Blocks NORTH movement. Found at Row 15 (X=3-17).
- ROCK: Smashable rocks act as WALLs.
- Vertical Walls: X=3, 5, 9, 11, 17, 20.

# Suicune Quest (Cianwood)
- Started: Turn 49630
## Strategy: The Internal Highway (Final)
Reach (14, 10) by landing at (23, 33) and taking the inland gaps.
1. Move South to (27, 33) and West to (23, 33).
2. Land at (23, 33) and move West along Row 33 to (12, 33).
3. Move North along X=12 to (12, 28) and West to (11, 28).
4. Move North along X=11 to (11, 15).
5. Move North through gap at (11, 15) to (11, 14).
6. Move East along Row 14 to (14, 14) and North to (14, 10).

# Verification Notes
- (11, 15) is a verified FLOOR gap in the Row 15 ledge.
- X=12 and X=11 provide a clear path from Row 33 to Row 15 (bypassing Row 30-32 walls).
- Row 33 is a clear horizontal highway across the city.
- SUPER REPEL is active (Turn 49722).

# Navigation Logic
- Buoy Walls: Horizontal (Row 15, Row 9) and Vertical (X=18, X=22, X=26).
- Gaps: Search for WATER tiles within BUOY lines to cross barriers.
- Landing: Look for FLOOR tiles adjacent to WATER to return to land.
- Priority: Stay on the far eastern edge (X=24+) to avoid internal city obstacles.