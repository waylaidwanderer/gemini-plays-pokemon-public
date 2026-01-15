# Tile Mechanics
- FLOOR_UP_WALL: Blocks SOUTH movement (acting as a ledge). Passable from SOUTH to NORTH.
- LEDGE_HOP_DOWN: Blocks NORTH movement. Found at Row 15 (X=3-17).
- ROCK: Smashable rocks act as WALLs.
- Vertical Walls: X=3, 5, 9, 11, 17, 20.

# Suicune Quest (Cianwood)
- Started: Turn 49630
## Strategy: The Western Corridor Highway
Reach (14, 10) by using the western corridor (X=2) to bypass all ledges.
1. Solve Sea Maze: (27, 20) -> (27, 16) -> (21, 16) -> (21, 21) -> (19, 21) -> (19, 26) -> (17, 26) -> (17, 24) -> (12, 24) -> (12, 28). Land.
2. Move South along X=12 to (12, 35).
3. Move West along Row 35 to (2, 35) (Crossing X=5 gap at 5, 35).
4. Move North along X=2 to (2, 12) (Bypassing Row 15 ledge).
5. Move East along Row 12 to (14, 12) and North to (14, 10).

# Verification Notes
- Sea Maze gaps: (22, 16), (19, 21), (18, 26), (16, 24).
- (12, 28) is a FLOOR landing tile.
- (5, 35) is a verified FLOOR gap in the X=5 wall.
- X=2 corridor bypasses the Row 15 ledge.
- SUPER REPEL is active (Turn 49722).

# Navigation Logic
- Buoy Walls: Horizontal (Row 15, Row 9) and Vertical (X=18, X=22, X=26).
- Gaps: Search for WATER tiles within BUOY lines to cross barriers.
- Landing: Look for FLOOR tiles adjacent to WATER to return to land.
- Priority: Stay on the far eastern edge (X=24+) to avoid internal city obstacles.