# Global Mechanics
## Tile Mechanics
- FLOOR_UP_WALL: Blocks SOUTH movement. Allows NORTH movement. Found at Rows 34, 46, 48, 50 in various columns. (Verified: (12, 50) and (6, 34) block Down).
- LEDGE_HOP_DOWN: Blocks NORTH movement. Found at (10, 15).
- ROCK: Smashable rocks act as WALLs until Rock Smash is used.

# Suicune Quest (Cianwood)
- Quest Start: Turn 48900

## Strategy: Western Corridor Ascent
The northern plateau (14, 10) is blocked by a Row 15 ledge (LEDGE_HOP_DOWN) across the center and east. The only access is via the Western Corridor (X=0-2).

## Execution Plan (Route: Southern Bypass -> X=4 Corridor)
1. Move to (12, 47) via X=12 thoroughfare. <- CURRENT TASK
2. Cross to X=8 at Row 47.
3. Move to (8, 48) and cross to (4, 48).
4. Ascend X=4 corridor to Row 35.
5. Cross to X=2 at Row 35.
6. Ascend X=2 corridor to Row 12.
7. Move East to (14, 12) and North to (14, 10).

## Lessons Learned
- X=3 and X=5 walls are mostly solid. Gaps exist at Row 21-22, 24-28, 30-35.
- Central thoroughfares (X=6, X=8) are blocked by buildings (Gym, Center, Houses).
- Row 15 buoy wall in water blocks eastern access to the plateau.

## Progress Summary
- Turn 49531: Player at (6, 33). Moving to X=12.