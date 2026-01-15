# Global Mechanics
## Tile Mechanics
- FLOOR_UP_WALL: Blocks SOUTH movement. Allows NORTH movement. Found at Rows 34, 46, 48, 50.
- LEDGE_HOP_DOWN: Blocks NORTH movement. Found at (10, 15).
- WALL: Impassable.
- ROCK: Smashable rock (acts as WALL).

# Suicune Quest (Cianwood)
- Quest Start: Turn 48900
- Movement Attempt Start: Turn 49554

## Strategy: Outer Sea Surf Bypass
Reach the northern plateau (14, 10) by Surfing north in the Outer Sea (X=24) to bypass the Row 15 land ledge.

## Execution Plan (Route: Staggered Ledge Descent)
1. Swim South to (24, 45) and land at (23, 45). <- CURRENT TASK
2. Walk West to (18, 45) and South through Row 46 gap at (18, 46).
3. Walk West to (12, 47) and South through Row 48 gap at (12, 48).
4. Walk West to (10, 49) and South through Row 50 gap at (10, 50).
5. Walk West to (2, 51) and North along Western Corridor (X=2) to Row 12.
6. Walk East to (14, 12) and North to (14, 10).

## Lessons Learned
- Row 15 ledge blocks central/eastern access to the plateau.
- Row 34, 46, 48, 50 are FLOOR_UP_WALL ledges (North-only traversal).
- Gaps in ledges: (12, 34), (18, 46), (12, 48), (10, 50).
- Western Corridor (X=0-2) is the only confirmed land path to Row 12.

## Progress Summary
- Turn 49558: At (24, 32). Moving to (26, 45) in the Outer Sea to bypass the Row 34 ledge.