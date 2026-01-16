# Suicune Quest: Cianwood City
## Active Strategy: Trigger Suicune
I have landed at (13, 16) and am currently at (13, 18).
1. Walk West to X=8 to clear the wall at X=9.
2. Walk North to Row 11 (the first horizontal gap in the X=12 wall).
3. Walk East to X=14.
4. Walk North to trigger Suicune at (14, 10).

## Global Tile Mechanics
- FLOOR: Traversable.
- WALL, BUOY: Impassable.
- WATER: Requires Surf.
- DOOR: Warp. BFS tools treat as walls unless targeting the warp.
- LEDGE_HOP_DOWN: One-way South. Blocks North movement. (e.g. 10, 15)
- FLOOR_UP_WALL: Impassable from the North. Blocks Down movement. (e.g. 6-8, 34)

## Verified Obstacles (Cianwood)
- Row 15: Ledge (10, 15) blocks North. WALLs (12-17, 15) block access from the East.
- X=12 Wall: Blocks East/West from Row 12 to Row 15. Gap at Row 11.
- X=9 Wall: Blocks East/West from Row 34 to Row 40. Gap at Row 33.
- X=5 Wall: Blocks East/West from Row 15 to Row 33, with gaps at Row 18, 19, 24-28.

## Battle Plan: Eusine
- Lead: Calcifer (Lv64 Typhlosion).
- Strategy: Flamethrower sweep.
- Status: Fully healed.