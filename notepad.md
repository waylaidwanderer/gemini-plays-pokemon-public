# Suicune Quest (Cianwood)
- Quest Start: Turn 48900

## Strategy: The Row 28 Corridor
The most efficient path to the northern plateau at (14, 10) is via the western corridor (X=2). Row 28 is a clear terrestrial passage that crosses Wall X=9 and Wall X=5 without obstacles, providing access to the western edge of the map.

## Execution Plan
1. Move to (20, 33) to bypass building. <- CURRENT TASK
2. Move West through (9, 33) to (8, 33).
3. Move to (8, 35), then West through (5, 35) to (2, 35).
4. Walk North through western corridor (X=2) to (2, 12).
5. Walk East to (14, 12), then North to (14, 10) to trigger Suicune.

## Verified Tile Mechanics
- FLOOR_UP_WALL: Blocks DOWN (South) movement. (Verified: Attempted Down at (12, 49) into (12, 50) failed in Turn 49397).
- LEDGE_HOP_DOWN: Blocks NORTH movement. (Verified at (10, 15)).
- Row 28: Obstacle at (3, 28) (WALL) blocks direct passage.
- Row 33/35 Gaps: (9, 33) and (5, 35) are traversable gaps in city walls.

## Failed Hypotheses
- Southern Ledge Maze: Too complex; Row 28 is a direct bypass.
- Inner Channel (X=12): Blocked at Row 15 by buoy wall.
- Island Hop (13, 16): Dead end pocket at (11, 14).

## Progress Summary
- Badges: 16/16.
- Current Focus: Suicune tracking.