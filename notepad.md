# Tile Mechanics
- FLOOR_UP_WALL: Blocks SOUTH movement. Passable from SOUTH to NORTH.
- LEDGE_HOP_DOWN: Blocks NORTH movement. Found at Row 15 (X=3-17).
- Vertical Walls: X=3, 5, 7, 9, 11, 17, 20.

# Suicune Quest (Cianwood)
## Strategy: Sea Route Bypass (Verified)
Reach (14, 10) by surfing around the city via the eastern buoy gaps.
1. SURF from (23, 33) into the eastern sea. (Done)
2. Move North along X=24 to (24, 15).
3. Move West to (23, 15) (Gap in Row 15 BUOY wall).
4. Move North along X=23/24 to Row 9.
5. Move East to (27, 9) (Gap in Row 9 BUOY wall).
6. Move North to Row 8 and West to (14, 8) (Above the plateau).
7. Move South to land at (16, 11) and walk to (14, 10).

# Progress Notes
- Blocked: All land routes (X=2, 4, 6, 10, 12) are blocked by SOUTH-blocking ledges (FLOOR_UP_WALL).
- Verified: X=27 is a clear vertical corridor for surfing.
- Verified: (27, 9) is a gap in the buoy walls.
- SUPER REPEL is active (Turn 49722).
- Stagnation Check: Abandoned 8 land-based routes; Sea Route is the final priority.

# Tool Maintenance
- find_path_v6_fixed_refined_v2_new: Needs update with commit message.
- menu_navigator_refined_v2: Needs update with commit message.