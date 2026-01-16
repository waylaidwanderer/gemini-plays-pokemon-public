# Suicune Quest: Cianwood City
## Active Strategy: The Cut Bypass
The northern plateau (14, 10) is accessible by clearing a cuttable tree at (11, 13).
1. Navigate to (11, 14). (In Progress)
2. Face North and use CUT (KIMCHI).
3. Walk North to Row 12.
4. Walk East to (14, 12).
5. Walk North to trigger Suicune at (14, 10).

## Global Tile Mechanics
- FLOOR: Traversable.
- WALL, BUOY: Impassable. Note: Some WALL tiles are cuttable trees (e.g., 11, 13).
- WATER: Requires Surf.
- DOOR: Warp. BFS tools treat as walls unless targeting the warp.
- LEDGE_HOP_DOWN: One-way South. Blocks North movement. (e.g. 10, 15)
- FLOOR_UP_WALL: Impassable from the North. Blocks Down movement. (e.g. 6-8, 34)

## Verified Obstacles (Cianwood)
- Row 15: Ledge (10, 15) blocks North. WALLs (12-17, 15) block access from the East.
- X=12 Wall: Blocks East/West from Row 12 to Row 15. Gap at Row 11.
- X=9 Wall: Blocks East/West from Row 34 to Row 40. Gap at Row 33.
- X=5 Wall: Blocks East/West from Row 15 to Row 33, with gaps at Row 18, 19, 24-28.

## Battle Plan: Eusine
- Lead: Calcifer (Lv64 Typhlosion).
- Strategy: Flamethrower sweep.
- Status: Fully healed.

## Failed Hypotheses
- Hypothesis: Reach plateau via Western Corridor (X=2). Result: Blocked by wall at (3, 18).
- Hypothesis: Reach plateau via Surf from Row 16. Result: Blocked by wall at (14, 15).
- Hypothesis: Reach plateau via Eastern land bridge. Result: Blocked by wall at X=12.
Conclusion: The tree at (11, 13) is the only confirmed entrance.