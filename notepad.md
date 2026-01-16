# Suicune Quest: Cianwood City
## Strategy: Western Bypass (X=2)
The northern plateau (14, 10) is accessible via the western coast corridor (X=2). Central land routes are blocked by one-way ledges and walls.

### Execution Plan
1. Southern Loop: Walk to (20, 51) to bypass the FLOOR_UP_WALL line at Row 50. (In Progress)
2. Cross to West: Walk west along Row 51 to (4, 51).
3. Coast Entry: Navigate to (2, 20) via the (4, 20) UP_WALL gap.
4. Highway North: Walk North along X=2 to Row 14.
5. Trigger: Walk East to (14, 10).

## Tile Mechanics
- FLOOR: Land (Traversable).
- WALL, BUOY, DOOR: Impassable.
- WATER: Requires Surf.
- LEDGE_HOP_DOWN: One-way South. Blocks North movement. (e.g. 10, 15)
- FLOOR_UP_WALL: One-way North. Blocks Down movement. (e.g. 12-19, 50; 6-8, 34; 4, 20; 6, 46)

## Battle Plan: Eusine
- Expected Team: Drowzee (Lv23), Haunter (Lv23), Electrode (Lv25).
- Lead: Calcifer (Lv64 Typhlosion).
- Strategy: Flamethrower sweep.
- Status: Fully healed.

## Tool Mechanics
- find_path_v9.9: Multi-modal (land/surf), one-way aware, safety truncation. avoid_labels parameter for custom avoidance.