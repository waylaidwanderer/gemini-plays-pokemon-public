# Tile Mechanics
- FLOOR_UP_WALL: Blocks SOUTH. Allows NORTH. Verified: Down at (12, 49) failed (Turn 49397); Up at (15, 51) worked (Turn 49319).
- LEDGE_HOP_DOWN: Blocks NORTH. Found at (10, 15).
- Vertical Walls: X=3, 5, 9, 11, 17, 20.

# Suicune Quest (Cianwood)
## Strategy: High-Altitude Western Bypass
Reach (14, 10) by weaving through wall gaps at Row 33, 26, and 22.
1. Move to (12, 33) via Row 45 thoroughfare. <- CURRENT TASK
2. Move West to (6, 33) (Gap at 9, 33).
3. Move North to (6, 26) and West to (4, 26) (Gap at 5, 26).
4. Move North to (4, 22) (Bypass rock at (4, 25) via (5, 26)).
5. Move West to (2, 22) (Gap at 3, 22).
6. Move North along Western Corridor (X=2) to Row 12.
7. Walk East to (14, 12) and North to (14, 10).

## Verified Tile Mechanics
- FLOOR_UP_WALL: Blocks SOUTH movement. Allows NORTH movement.
- LEDGE_HOP_DOWN: Blocks NORTH movement. Found at (10, 15).
- Wall Gaps: (9, 33), (5, 26), (3, 22), (18, 46), (12, 34).
- Dead End Pocket: (12-19, 46-49) blocks South/West exit at Row 49/50. Must exit via Row 46 or Row 45.

# Time Tracking
- Quest Start: Turn 48900
- Southern Loop Start: Turn 49598