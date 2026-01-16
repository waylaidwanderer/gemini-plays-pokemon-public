# Suicune Quest: Cianwood City
## Strategy: The Northwest Entrance
The Whirl Islands (Map 22_3) are partitioned into four disconnected sections. The goal (14, 10) is in the Northwest section, which is likely only accessible via the Northwest island entrance on Route 41.

### Tile Mechanics
- FLOOR_UP_WALL: One-way North (Allows Ascent, Blocks Descent). Verified at (6, 46).
- LEDGE_HOP_DOWN: One-way South.
- BUOY: Impassable water barrier.
- Map Edge (WATER): Does not always trigger a warp. (0, 49) is a dead end.

### Hypothesis Log
1. Route 41 (0, 45) transitions to Cianwood (29, 45) (SE section). (Verified)
2. The NW section (14, 10) is disconnected from the SE section. (Verified via land/water BFS)
3. The NW island entrance on Route 41 leads to the NW section of the cave. (Pending)