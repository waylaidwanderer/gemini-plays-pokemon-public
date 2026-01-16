# Suicune Quest: Cianwood City
## Verified Strategy: The Western Highway (X=2)
The northern plateau (14, 10) is accessible via the western coastal highway (X=2). This route bypasses all elevation traps by utilizing the southern clearway at Row 51.

### Execution Plan
1. Reach Southern Clearway: Navigate to (10, 51) via the gap at X=10, Row 50. (In Progress)
2. Access Highway: Walk West along Row 51 to (2, 51).
3. Coastal Dash: Walk North along X=2 to Row 14.
4. Final Approach: Walk East to X=8, North to Row 10, then East to Suicune at (14, 10).

## Verified Mechanics
- X=2 Highway: Clear land path from Row 51 to Row 14.
- Row 51: Completely clear land bridge across the island (X=2 to X=24).
- FLOOR_UP_WALL: One-way North. Blocks DOWN movement. Gap identified at (10, 50).

## Battle Plan: Eusine
- Expected Team: Drowzee (Lv23), Haunter (Lv23), Electrode (Lv25).
- Lead: Calcifer (Lv64 Typhlosion). Strategy: Flamethrower sweep.

## Map Markers
- (5, 29), (10, 27), (4, 25), (4, 19): Smashable Rocks.
- (14, 10): ✨ Suicune Trigger Point
- (16, 32): 📍 Terrace Loop Entry.
- (17, 33): 👤 Pokefan M (ID 2)

## Global Tile Mechanics
- FLOOR: Land (Traversable).
- WALL, BUOY, DOOR: Impassable.
- WATER: Requires Surf.
- LEDGE_HOP_DOWN: One-way South. Blocks North movement.
- FLOOR_UP_WALL: One-way North. Blocks Down movement.

## Tool Mechanics
- find_path_v9.9.1: Multi-modal BFS with one-way awareness, safety truncation, and unexplored area traversal.