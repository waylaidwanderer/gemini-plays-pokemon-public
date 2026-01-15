# Suicune Quest (Cianwood)
- Quest Start: Turn 48900

## Strategy: Western Corridor Ascent
To reach the northern plateau at (14, 10), Gem must bypass the Row 15 ledge (LEDGE_HOP_DOWN), which blocks all NORTH movement except at the western corridor (X=0-2). The city's other "ledges" (Row 34, 46, 48, 50) are FLOOR_UP_WALL tiles that block SOUTH movement but allow NORTH traversal.

## Execution Plan
1. Walk North along X=12 to Row 33.
   - Path: (12, 49) -> (12, 33). <- CURRENT TASK
2. Move West through the (9, 33) wall gap to the central corridor.
   - Path: (12, 33) -> (6, 33).
3. Move South to Row 35 to bypass the Wall at X=5.
   - Path: (6, 33) -> (6, 35).
4. Move West through the (5, 35) wall gap to the Western Corridor (X=2).
   - Path: (6, 35) -> (2, 35).
5. Walk North along X=2 past the Row 15 ledge.
   - Path: (2, 35) -> (2, 12).
6. Walk East to the plateau and North to trigger Suicune.
   - Path: (2, 12) -> (14, 12) -> (14, 10).

## Verified Tile Mechanics
- FLOOR_UP_WALL: Blocks DOWN (South) movement. (Verified: (12, 50) blocked south from (12, 49)). Allows NORTH movement. (Verified: (15, 51) -> (15, 50) -> (15, 49) worked).
- LEDGE_HOP_DOWN: Blocks NORTH movement. (Verified: (10, 15) is impassable from the south).
- Wall Gaps: (11, 47), (11, 50), (9, 33), (5, 35).

## Failed Hypotheses
- Island Hop (13, 16): Dead end pocket at (11, 14) due to walls at Row 13.
- Southern Surf Bypass: Eastern channel ends at Row 45.
- Direct Northern Channel: Blocked by buoy wall at Row 15.

## Progress Summary
- Badges: 16/16.
- Current Focus: Suicune overworld sighting.