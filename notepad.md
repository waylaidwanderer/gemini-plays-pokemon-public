# Suicune Quest: Cianwood City
## Active Strategy: Western Bypass (X=2)
Land corridors near the plateau are blocked by ledges and walls. Investigation confirms a clear land path exists via the western edge (X=2).
1. Navigate south to Row 33 to clear the central wall (X=9).
2. Loop north to Row 18 to clear the western wall (X=5).
3. Loop south to Row 30 to clear the western wall (X=3).
4. Walk north along X=2 to Row 10.
5. Walk east to trigger Suicune at (14, 10).

## Global Tile Mechanics
- FLOOR: Land (Traversable).
- WALL, BUOY, DOOR: Impassable.
- WATER: Requires Surf.
- LEDGE_HOP_DOWN: One-way South. Blocks North movement. (e.g. 10, 15)
- FLOOR_UP_WALL: Impassable from the North. Blocks Down movement. (e.g. 6-8, 34)

## Battle Plan: Eusine
- Lead: Calcifer (Lv64 Typhlosion).
- Strategy: Flamethrower sweep.
- Status: Fully healed.

## Tool Lessons
- find_path_v9: BFS optimized for land/surf transitions and obstacle markers.