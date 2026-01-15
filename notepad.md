# Suicune Quest (Cianwood)
- Quest Start: Turn 48900

## Strategy: The Great Southern Loop
To reach the northern plateau at (14, 10), Gem must bypass the city's one-way upward ledges (Row 34, 46, 48, 50) and the northern Row 15 ledge. The confirmed path is to reach the southern corridor at Row 51 and then use the western corridor (X=0-2).

## Execution Plan
1. Move to (12, 49) via X=12 thoroughfare.
   - Path: (6, 22) -> (6, 33) -> (12, 33) -> (12, 49). <- CURRENT TASK
2. Reach Row 51 via the (11, 50) gap.
   - Path: (12, 49) -> (11, 49) -> (11, 51).
3. Walk west to (2, 51), then north along X=2 to (2, 12).
4. Walk east along Row 12 to (14, 12).
5. Walk north to (14, 10) to trigger Suicune sighting.

## Verified Tile Mechanics
- FLOOR_UP_WALL: Blocks DOWN (South) movement. (Verified: (12, 50) blocked south from (12, 49); (6, 34) blocked south from (6, 33)). Allows NORTH movement.
- LEDGE_HOP_DOWN: Blocks NORTH movement. (Verified: (10, 15) is impassable from the south).
- Ledge Gaps (Southbound): (12, 34), (12, 46), (12, 48), (11, 50).
- Wall Gaps: (9, 33), (11, 47), (11, 50), (5, 35).

## Failed Hypotheses
- Northern Gap Route (X=5): Blocked by wall at (5, 22).
- Row 44/45 West: Blocked by wall at (5, 44) and (5, 45).
- Island Hop (13, 16): Dead end pocket at (11, 14).

## Progress Summary
- Badges: 16/16.
- Current Focus: Reaching the southern corridor.