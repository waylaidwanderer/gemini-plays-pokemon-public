# Suicune Quest (Cianwood)
- Quest Start: Turn 48900

## Strategy: The Great Southern Loop
To reach the northern plateau at (14, 10), Gem must bypass the city's one-way upward ledges (Row 34, 46, 48, 50). The confirmed path is to reach the southern corridor at Row 51 and then use the western corridor (X=2). This route avoids the central walls and the buoy-blocked water channels.

## Execution Plan
1. Move to (20, 45) via (10, 39) and (20, 39). <- CURRENT TASK
2. Reach Row 51 via (18, 46) and (11, 50) gaps.
   - Detailed Path: (20, 45) -> (19, 45) -> (19, 46) -> (18, 46) -> (18, 47) -> (18, 49) -> (11, 49) -> (11, 51).
3. Walk west to (2, 51), then north along X=2 to (2, 12).
4. Walk east along Row 12 to (14, 12).
5. Walk north to (14, 10) to trigger Suicune sighting.

## Verified Tile Mechanics
- FLOOR_UP_WALL: Blocks DOWN (South) movement. (Verified: Move Down at (12, 49) into (12, 50) failed in Turn 49397).
- LEDGE_HOP_DOWN: Blocks NORTH movement. (Verified: (10, 15) is impassable from the south).
- Wall X=5/9: Mostly solid with specific gaps at (9, 33) and (5, 35).
- Column X=2: Clear corridor from Row 53 to Row 14.

## Failed Hypotheses
- Island Hop (13, 16): Dead end pocket at (11, 14) due to walls at Row 13.
- Southern Surf Bypass: Eastern channel ends at Row 45.
- Direct Northern Channel: Blocked by buoy wall at Row 15.

## Progress Summary
- Badges: 16/16.
- Current Focus: Suicune overworld sighting.