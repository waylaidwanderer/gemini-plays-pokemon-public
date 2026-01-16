# Suicune Quest: Cianwood City
## Active Strategy: The Western Highway (X=2)
Direct land access to the northern plateau is blocked by one-way ledges and walls. I must navigate to the western coast via a specific gap sequence.

### Verified Path to Suicune
1. Navigate to (13, 24). (Done)
2. Surf West to (9, 24).
3. Walk West through the gap at (5, 24).
4. Walk North to (4, 21), then North through the UP_WALL at (4, 20).
5. Walk West to (2, 20) to reach the Western Highway.
6. Walk North along X=2 to Row 10.
7. Walk East to (14, 10).

## Global Tile Mechanics
- FLOOR: Land (Traversable).
- WALL, BUOY, DOOR: Impassable.
- WATER: Requires Surf.
- LEDGE_HOP_DOWN: One-way South. Blocks North movement. (e.g. 10, 15)
- FLOOR_UP_WALL: One-way North. Blocks Down movement. (e.g. 6-8, 34; 13, 50; 21, 46)

## Battle Plan: Eusine
- Lead: Calcifer (Lv64 Typhlosion).
- Strategy: Flamethrower sweep.
- Status: Fully healed.

## Tool Notes
- find_path_v9.6: Optimized for land/surf transitions and one-way barriers. Marker-based blocking refined to rock/blocked keywords.