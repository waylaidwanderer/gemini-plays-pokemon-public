# Suicune Quest (Cianwood)
- Quest Start: Turn 48900

## Strategy: The Row 28 Corridor
The most efficient path to the northern plateau at (14, 10) is via the western corridor (X=2). Row 28 is a clear terrestrial passage that crosses Wall X=9 and Wall X=5 without obstacles, providing access to the western edge of the map.

## Execution Plan
1. Walk North to (18, 33). <- CURRENT TASK
2. Walk West to (12, 33), then North to (12, 28).
3. Walk West along Row 28 to (2, 28).
4. Walk North along X=2 to (2, 12).
5. Walk East along Row 12 to (14, 12).
6. Walk North to (14, 10) to trigger Suicune.

## Verified Tile Mechanics
- Row 28: Clear corridor (X=2 to X=12).
- X=2: Clear corridor (Row 14 to Row 53).
- Row 12: Clear corridor (X=2 to X=16).
- FLOOR_UP_WALL: Blocks DOWN (South) movement. (Verified at Row 34, 46, 48, 50).
- LEDGE_HOP_DOWN: Blocks NORTH movement. (Verified at (10, 15)).

## Failed Hypotheses
- Southern Ledge Maze: Too complex; Row 28 is a direct bypass.
- Inner Channel (X=12): Blocked at Row 15 by buoy wall.
- Island Hop (13, 16): Dead end pocket at (11, 14).

## Progress Summary
- Badges: 16/16.
- Current Focus: Suicune tracking.