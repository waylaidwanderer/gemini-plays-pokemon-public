# Global Mechanics
## Tile Mechanics
- FLOOR_UP_WALL: Blocks SOUTH movement. Allows NORTH movement. Found at Rows 34, 46, 48, 50 in various columns. (Verified: (12, 50) and (6, 34) block Down).
- LEDGE_HOP_DOWN: Blocks NORTH movement. Found at (10, 15).
- ROCK: Smashable rocks act as WALLs until Rock Smash is used.

# Suicune Quest (Cianwood)
- Quest Start: Turn 48900

## Strategy: Western Corridor Ascent
The northern plateau (14, 10) is blocked by a Row 15 ledge (LEDGE_HOP_DOWN) across the center and east. The only access is via the Western Corridor (X=0-2).

## Execution Plan (Route: Row 12 Bypass)
1. Move to (12, 33) via X=12 thoroughfare. <- CURRENT TASK
2. Move Left to (6, 33) via (9, 33) gap.
3. Move North to (6, 12). (Check for walls at Row 15-17).
4. Move Left to (2, 12) if needed to bypass Row 15 ledge.
5. Move Right to (14, 12) and North to (14, 10).

## Lessons Learned
- X=9 wall gap: (9, 33).
- X=5 wall gap: (5, 26).
- X=3 wall gap: (3, 21), (3, 22), (3, 30).
- Row 15 Ledge (10, 15) blocks North. Access to plateau is from X < 9.
- Row 12 is a potential thoroughfare across the top of the map.

## Progress Summary
- Turn 49531: Player at (6, 33). Moving to X=12.