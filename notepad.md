# Suicune Quest: Cianwood City
## Active Strategy: The Great Western Bypass
Direct landing on the northern plateau is blocked by ledges. The only valid path is to loop around the entire island via the western corridor (X=2).

### Execution Plan
1. Return to Mainland: Surf south from (13, 16) to (13, 28). (In Progress)
2. Reach Southern Clearway: Walk to (13, 51).
3. Cross to West Side: Walk to (4, 51).
4. Coastal Highway: Walk north along X=2/X=4 to Row 10.
5. Trigger Event: Walk east to (14, 10).

## Global Tile Mechanics
- FLOOR: Land (Traversable).
- WALL, BUOY, DOOR: Impassable.
- WATER: Requires Surf.
- LEDGE_HOP_DOWN: One-way South. Blocks North movement. (e.g. 10, 15)
- FLOOR_UP_WALL: Impassable from the North. Blocks Down movement. (e.g. 6-8, 34)

## Battle Plan: Eusine
- Lead: Calcifer (Lv64 Typhlosion).
- Strategy: Flamethrower sweep. (Lv23-25 targets).
- Status: Fully healed.

## Tool Lessons
- find_path_v9: BFS optimized for land/surf transitions. Limited to 50 buttons per turn. Handles obstacle markers. v9.5 adds 'A' button logic for Surfing.