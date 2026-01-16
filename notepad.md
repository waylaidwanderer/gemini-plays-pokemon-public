# Suicune Quest: Cianwood City
- **Quest Start:** Turn 49885
- **Status:** Landing at (23, 33) to begin the "Terrace Loop".

## Strategy: The Terrace Loop
The northern plateau (14, 10) is accessible via the western coastal highway (X=2). This path uses a series of terrace gaps to bypass central walls.

### Execution Plan
1. Land at Shore: Move Left to (23, 33) and land. (Done)
2. Central Traverse: Walk West along Row 33 to (16, 33), then North to (16, 32). (In Progress)
3. Corridor Entry: Walk West along Row 32 to (9, 32).
4. Northern Ascent: Walk North along X=9 to Row 25.
5. West Coast Entry: Walk West along Row 25 to (4, 25), then North to Row 21.
6. Mechanical Bypass: Move North through (4, 20) [UP_WALL] to reach Row 20.
7. Highway Dash: Walk West to (2, 20), then North along X=2 to Row 10.
8. Victory: Walk East to (14, 10) to trigger Suicune.

## Verified Mechanics
- Row 32: Clear horizontal gap from X=16 to X=9.
- Row 25: Clear horizontal gap from X=9 to X=4.
- UP_WALL: Blocks DOWN movement. Moving UP is allowed. (e.g., (4, 20)).
- X=2 Highway: Clear north-south path from Row 20 to Row 10.

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