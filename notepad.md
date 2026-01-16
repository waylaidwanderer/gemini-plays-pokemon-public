# Suicune Quest: Cianwood City
## Active Strategy: The Western Highway (X=2)
Direct land access to the northern plateau is blocked by one-way ledges and central walls. The only viable land route is via the western coast corridor.

### Execution Path
1. Navigate south to Row 33 to clear the central wall (X=9). (Done)
2. Navigate to (4, 31) via Row 33.
3. Move Up into (4, 30) (UP_WALL bypass).
4. Walk West to (2, 30) to reach the Western Highway.
5. Walk north along X=2 to Row 14.
6. Walk east to (14, 12) via Row 12.
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