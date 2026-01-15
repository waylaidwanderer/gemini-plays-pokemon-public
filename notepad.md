# Global Mechanics
## Tile Mechanics
- FLOOR_UP_WALL: Blocks SOUTH movement. Allows NORTH movement. Found at Rows 34, 46, 48, 50.
- LEDGE_HOP_DOWN: Blocks NORTH movement. Found at (10, 15).
- WALL: Impassable.
- ROCK: Smashable rock (acts as WALL).

# Suicune Quest (Cianwood)
- Quest Start: Turn 48900

## Strategy: Great Southern Surf Loop
The northern plateau (14, 10) is reached via the Western Corridor (X=0-2). Access to this corridor is only guaranteed at Row 51. To reach Row 51 without being blocked by ledges, Gem must Surf in the Outer Sea (X=24) and land at (23, 51).

## Execution Plan
1. Move to (23, 32) and Surf. <- CURRENT TASK
2. Move South to Row 51 and land at (23, 51).
3. Walk West to (2, 51).
4. Walk North along Western Corridor (X=2) to Row 12.
5. Walk East to (14, 12) and North to (14, 10) to trigger Suicune.

## Lessons Learned
- Land paths (X=4, X=6, X=8, X=12) are all blocked by ledges or walls before reaching the plateau.
- Row 15 ledge blocks all central/eastern access to the plateau.
- Row 51 is the only confirmed "bottom" thoroughfare.
- Ledge Gaps: (12, 34) is a rare gap allowing South movement past Row 34.

## Progress Summary
- Turn 49547: At (6, 26). Moving to Surf point.