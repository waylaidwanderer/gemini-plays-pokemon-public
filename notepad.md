# Tile Mechanics
- FLOOR_UP_WALL: Blocks SOUTH movement (acting as a ledge). Passable from SOUTH to NORTH.
- LEDGE_HOP_DOWN: Blocks NORTH movement. Found at Row 15 (X=3-17).
- ROCK: Smashable rocks act as WALLs.
- Vertical Walls: X=3, 5, 9, 11, 17, 20.

# Suicune Quest (Cianwood)
- Started: Turn 49630
## Strategy: Eastern Sea Bypass (X=27 Corridor)
Reach (14, 10) by surfing along the far eastern edge of the map.
1. Move Right to (27, 26).
2. Move North along X=27 to (27, 8) (Bypasses Row 9 and X=26 buoy walls).
3. Move West along Row 8 to (14, 8) (Bypasses X=22 wall at Row 8 gap).
4. Move South to (14, 10) to trigger Suicune sighting.

# Verification Notes
- X=27 is a clear vertical corridor from Row 33 to Row 0.
- Row 8 is a clear horizontal corridor north of the major buoy walls.
- (27, 9) is a verified gap in the Row 9 buoy wall.
- SUPER REPEL is active (Turn 49722).

# Navigation Logic
- Buoy Walls: Horizontal (Row 15, Row 9) and Vertical (X=18, X=22, X=26).
- Gaps: Search for WATER tiles within BUOY lines to cross barriers.
- Landing: Look for FLOOR tiles adjacent to WATER to return to land.
- Priority: Stay on the far eastern edge (X=24+) to avoid internal city obstacles.