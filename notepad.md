# Suicune Quest: Cianwood City
- **Start Turn:** 49885
- **Current Status:** Heading North via the Western Corridor (X=2).

## Active Strategy: The Western Corridor Bypass
To reach Suicune at (14, 10), we must bypass the central wall (X=5) and the northern ledge (Row 15).
1. Navigate to (2, 18) via the gap at (5, 18).
2. Walk North along X=2 to Row 12.
3. Walk East along Row 12 to (14, 12).
4. Walk North to trigger Suicune at (14, 10).

## Tile Mechanics
- FLOOR: Traversable.
- WALL / BUOY: Impassable.
- WATER: Requires Surf.
- DOOR: Warp. BFS tools should treat as walls unless targeting the warp.
- LEDGE_HOP_DOWN: One-way (South). Blocks North.
- FLOOR_UP_WALL: Impassable from the North.

## Verified Obstacles
- Row 15: Ledge blocks North at X=10. WALLs at X=3-9 and X=12-17.
- X=5 Wall: Blocks East/West from Row 15 to Row 32. Gaps at Row 13-14, 18.
- Row 22: Water blocks land travel at X=10-11.

## Battle Plan: Eusine
- Lead: Calcifer (Lv64 Typhlosion).
- Strategy: Flamethrower sweep.
- Status: Fully healed.

## Tool Lessons
- `find_path_v8` can accidentally route through warps (e.g., Turn 50021). Always verify paths near buildings and manually guide past warps if needed.