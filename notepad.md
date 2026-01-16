# Suicune Quest: Cianwood City
## Strategy: The Cut Bypass
1. Land at beach (13, 16). (Done)
2. Navigate to (11, 14). (Done)
3. Use CUT on tree at (11, 13). (In Progress)
4. Walk to Suicune at (14, 10).

## Global Tile Mechanics
- FLOOR: Land (Traversable).
- WALL, BUOY, DOOR: Impassable. (Cuttable trees are marked as WALL).
- WATER: Requires Surf.
- LEDGE_HOP_DOWN: One-way South. Blocks North movement. (e.g. 10, 15)
- FLOOR_UP_WALL: Impassable from the North. Blocks Down movement. (e.g. 6-8, 34)

## Battle Plan: Eusine
- Lead: Calcifer (Lv64 Typhlosion).
- Strategy: Flamethrower sweep.
- Status: Fully healed.

## Tool Lessons
- find_path_v9: Now handles markers (rock, wall, blocked) and treats cuttable markers as traversable for planning. Avoids doors (warps) unless targeted.