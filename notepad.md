# Suicune Quest (Cianwood)
- Quest Start: Turn 48900

## Strategy: The Great Southern Loop
Northern plateau is blocked by jump-down ledges. Direct northern access from city center is impossible due to upward-only ledges (Row 34, 46, 48, 50).
The confirmed path is to reach the southern edge of the map (Row 51) and then use the western corridor (X=2).

## Execution Plan
1. Use Super Repel (In progress).
2. Walk to (19, 45), then south through gap to (19, 47). (Bypasses Row 46).
3. Walk west to (11, 47), then south through gap at (11, 50) to (11, 51). (Bypasses Row 48, 50).
4. Walk west to (2, 51), then north along X=2 to (2, 12).
5. Walk east to (14, 12), then north to (14, 10) to trigger Suicune.

## Verified Tile Mechanics
- FLOOR_UP_WALL: One-way. Blocks DOWN (South) movement. Verified at (12, 50), (13, 50), (12, 49)->(12, 50) failed.
- LEDGE_HOP_DOWN: One-way. Blocks NORTH movement. Verified at (10, 15).

## Failed Hypotheses
- Island Hop (13, 16): Dead end alcove at (11, 14).
- Southern Surf: Eastern channel ends at Row 45.

## Progress Summary
- Badges: 16/16.
- Current Focus: Suicune tracking.