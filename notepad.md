# Suicune Quest (Cianwood)
- Quest Start: Turn 48900

## Tile Mechanics (Cianwood)
- FLOOR: Standard traversable ground.
- WALL: Impassable barrier.
- FLOOR_UP_WALL: One-way ledge. Blocks DOWN (South) movement.
- LEDGE_HOP_DOWN: One-way ledge. Blocks NORTH movement.

## Execution Plan (Terrestrial Zig-Zag)
1. Walk to (19, 45) via (19, 33). <- CURRENT TASK
2. Walk South to (19, 47). (Bypasses Row 46 ledge).
3. Walk to (12, 47), then South to (12, 49). (Bypasses Row 48 ledge).
4. Walk to (10, 49), then South to (10, 51). (Bypasses Row 50 ledge).
5. Walk West to (2, 51), then North to (2, 14).
6. Walk East to (14, 12), then North to (14, 10).
7. Trigger Suicune sighting.

## Failed Hypotheses
1. Island Hop (13, 16) via (11, 15): Dead end alcove at (11, 14). (Verified Turn 49428).
2. Southern Surf Bypass: Eastern channel ends at Row 45. (Verified Turn 49446).
3. Terrestrial Path (West): Blocked by wall lines and upward ledges at Row 34.

## Reflection Turn #49457
- Pathing: Navigating around Pokefan M to reach the X=19 corridor.
- Strategy: Using the identified gaps in ledge lines (Row 46 @ X=19, Row 48 @ X=12, Row 50 @ X=10) to reach the southern edge.
- Maintenance: Repel active. Party ready.