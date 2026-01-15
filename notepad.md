# Suicune Quest (Cianwood)
- Quest Start: Turn 48900

## Strategy: The Great Southern Loop
To reach the northern plateau at (14, 10), Gem must bypass the city's one-way upward ledges (Row 34, 46, 48, 50). The confirmed path is to reach the southern corridor at Row 51 and then use the western corridor (X=2). This route avoids the central walls and the buoy-blocked water channels.

## Execution Plan
1. Move to (12, 45) via the Row 34 gap at (12, 34). <- CURRENT TASK
2. Reach Row 51 via the staggered gaps:
   - (12, 45) -> (18, 45) -> (18, 47) (Row 46 gap)
   - (18, 47) -> (12, 47) -> (12, 49) (Row 48 gap)
   - (12, 49) -> (11, 49) -> (11, 51) (Row 50 gap)
3. Walk west to (2, 51), then north along X=2 to (2, 12).
4. Walk east along Row 12 to (14, 12).
5. Walk north to (14, 10) to trigger Suicune sighting.

## Verified Tile Mechanics
- FLOOR_UP_WALL: Blocks DOWN (South) movement. (Verified: (6, 34) blocked south from (6, 33)). Allows NORTH movement.
- LEDGE_HOP_DOWN: Blocks NORTH movement. (Verified: (10, 15) is impassable from the south).
- Ledge Gaps: (12, 34), (18, 46), (12, 48), (11, 50).
- Wall Gaps: (9, 33) at Row 33.

## Failed Hypotheses
- Direct West from (6, 33): Blocked by ledge at (6, 34) and wall at (5, 33).
- Island Hop (13, 16): Dead end pocket at (11, 14).
- Southern Surf Bypass: Eastern channel ends at Row 45.

## Progress Summary
- Badges: 16/16.
- Current Focus: Navigating the Great Southern Loop.