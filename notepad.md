# Suicune Quest: Cianwood City
## Active Strategy: Western Bypass (X=2)
The northern plateau (14, 10) is accessible via the western coast highway (X=2). Central land routes are blocked by ledges and walls.

### Execution Plan
1. Navigate to (10, 26) to clear the central rocks. (In Progress)
2. Navigate to (12, 44) to clear the X=9 wall.
3. Navigate to (4, 46) via the (6, 46) UP_WALL bypass.
4. Navigate to (2, 20) via the (4, 20) UP_WALL bypass.
5. Walk North along X=2 to Row 14.
6. Walk East to (14, 12) via Row 12.
7. Trigger Suicune sighting at (14, 10).

## Global Tile Mechanics
- FLOOR: Land (Traversable).
- WALL, BUOY, DOOR: Impassable.
- WATER: Requires Surf.
- LEDGE_HOP_DOWN: One-way South. Blocks North movement. (e.g. 10, 15)
- FLOOR_UP_WALL: One-way North. Blocks Down movement. (e.g. 6-8, 34; 4, 20; 6, 46)

## Battle Plan: Eusine
- Lead: Calcifer (Lv64 Typhlosion).
- Strategy: Flamethrower sweep.
- Status: Fully healed.

## Tool Notes
- find_path_v9.8: Handles land/surf, one-way barriers, and safety truncation. v9.8 returns [] if no path found.