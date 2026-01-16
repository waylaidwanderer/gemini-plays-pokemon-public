# Suicune Quest: Cianwood City
## Active Strategy: The Western Highway (X=2)
Direct land access to the northern plateau is blocked by one-way ledges and central walls. The only viable land route is via the western coast corridor.

### Execution Path
1. Navigate to (10, 51) via the central gap at (10, 34). (In Progress)
2. Walk West along Row 51 to (4, 51).
3. Walk North along X=4 to Row 20.
4. Move Left to X=2 to reach the Western Highway.
5. Walk North along X=2 to Row 14.
6. Walk East to (14, 12) via Row 12.
7. Trigger Suicune sighting at (14, 10).

## Global Tile Mechanics
- FLOOR: Land (Traversable).
- WALL, BUOY, DOOR: Impassable.
- WATER: Requires Surf.
- LEDGE_HOP_DOWN: One-way South. Blocks North movement. (e.g. 10, 15)
- FLOOR_UP_WALL: One-way North. Blocks Down movement. (e.g. 6-8, 34; 13, 50; 21, 46)

## Battle Plan: Eusine
- Lead: Calcifer (Lv64 Typhlosion).
- Strategy: Flamethrower sweep (against Lv23-25 targets).
- Status: Fully healed.

## Tool Notes
- find_path_v9.7: Handles land/surf transitions, starting state detection, and one-way barrier logic.