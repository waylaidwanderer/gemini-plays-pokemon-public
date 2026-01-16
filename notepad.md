# Suicune Quest: Cianwood City
## Strategy: The Inland Sea Route
The northern plateau (14, 10) is accessible via the western coast highway (X=2). Central land routes are blocked by one-way ledges and walls.

### Execution Plan
1. Return to Sea: Walk to (12, 28) and Surf to (9, 24). (In Progress)
2. Land at (9, 24) and walk West to (4, 24).
3. Coast Entry: Navigate to (2, 20) via the (4, 20) UP_WALL gap.
4. Highway North: Walk North along X=2 to Row 14.
5. Final Approach: Walk East to (8, 14), North to (8, 12), and East to (14, 10).

## Tile Mechanics
- FLOOR: Land (Traversable).
- WALL, BUOY, DOOR: Impassable.
- WATER: Requires Surf.
- FLOOR_UP_WALL: One-way North. Blocks DOWN movement. (e.g., Row 50; (6, 46); (8, 48); (4, 20); (4, 30)).
- LEDGE_HOP_DOWN: One-way South. Blocks NORTH movement. (e.g., (10, 15)).

## Battle Plan: Eusine
- Expected Team: Drowzee (Lv23), Haunter (Lv23), Electrode (Lv25).
- Lead: Calcifer (Lv64 Typhlosion).
- Strategy: Flamethrower sweep.
- Status: Fully healed.

## Tool Mechanics
- find_path_v9.9: Multi-modal BFS with one-way awareness and safety truncation. avoid_labels parameter for custom avoidance.