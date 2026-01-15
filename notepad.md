# Suicune Quest (Cianwood)
- Quest Start: Turn 48900

## Execution Plan (Terrestrial Maze)
1. Clear text and land at (22, 32). <- CURRENT TASK
2. Walk to (19, 33), then south to (19, 47) (Bypasses Row 34 and Row 46).
3. Walk to (12, 47), then south to (12, 49) (Bypasses Row 48).
4. Walk to (11, 49), then south to (11, 51) (Bypasses Row 50).
5. Walk west to (2, 51), then north to (2, 12).
6. Walk east to (14, 12), then north to (14, 10) to trigger Suicune.

## Strategy: Terrestrial Maze
The southern water is a dead end. To reach the western corridor (X=2), I must navigate a series of gaps in the city's ledge lines:
- Row 34: Gap at X=10-19.
- Row 46: Gap at X=19.
- Row 48: Gap at X=12-19.
- Row 50: Gap at X=10-11.
By zig-zagging between these gaps, I can reach the southern corridor at Row 51.

## Tile Mechanics (Cianwood)
- FLOOR_UP_WALL: One-way ledge. Blocks South movement.
- LEDGE_HOP_DOWN: One-way ledge. Blocks North movement.

## Failed Hypotheses
- Southern Surf Bypass: Eastern channel ends at Row 45.
- Island Hop (13, 16): Dead end pocket at (11, 14).

## Progress Summary
- All 16 Badges obtained.
- Current Focus: Suicune tracking.