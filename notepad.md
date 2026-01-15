# Global Mechanics
## Tile Mechanics
- FLOOR_UP_WALL: Blocks SOUTH movement. Allows NORTH movement. Found at Rows 34, 46, 48, 50.
- LEDGE_HOP_DOWN: Blocks NORTH movement. Found at (10, 15).
- WALL: Impassable.
- ROCK: Smashable rock (acts as WALL).

# Suicune Quest (Cianwood)
- Quest Start: Turn 48900

## Strategy: Western Corridor Ascent (Land Route)
The northern plateau (14, 10) is reached by weaving through wall gaps to the Western Corridor (X=0-2), which bypasses the Row 15 ledge.

## Execution Plan
1. Land at (23, 32) and move to (12, 33). <- CURRENT TASK
2. Move Left to (6, 33) via (9, 33) gap.
3. Move North to (6, 26) and Left to (4, 26) via (5, 26) gap.
4. Move North to (4, 22) and Left to (2, 22) via (3, 22) gap.
5. Move North to (2, 12) and East to (14, 12).
6. Move North to (14, 10) to trigger Suicune.

## Lessons Learned
- Row 15 Ledge (10, 15) blocks North.
- Plateaus are isolated; access is from X < 3.
- FLOOR_UP_WALL tiles are one-way (North only).
- Sea Bypass is longer and landing points are unconfirmed.

## Progress Summary
- Turn 49544: Landed at (23, 32). Moving to (12, 33).