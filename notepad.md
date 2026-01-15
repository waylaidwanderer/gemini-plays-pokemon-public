# Suicune Quest (Cianwood)
- Quest Start: Turn 48900

## Strategy: Western Corridor Ascent
To reach the northern plateau at (14, 10), Gem must bypass the Row 15 ledge (LEDGE_HOP_DOWN), which blocks all NORTH movement except at the western corridor (X=0-2). The city's other "ledges" (Row 34, 46, 48, 50) are FLOOR_UP_WALL tiles that block SOUTH movement but allow NORTH traversal.

## Execution Plan
1. Walk North to Row 45 and West to bypass the X=11/14 walls.
   - Path: (12, 49) -> (12, 45) -> (6, 45). <- CURRENT TASK
2. Walk North to Row 35 to reach the wall gap at (5, 35).
   - Path: (6, 45) -> (6, 35).
3. Move West through the (5, 35) gap to the Western Corridor (X=2).
   - Path: (6, 35) -> (2, 35).
4. Walk North along X=2 past the Row 15 ledge.
   - Path: (2, 35) -> (2, 12).
5. Walk East to the plateau and North to trigger Suicune.
   - Path: (2, 12) -> (14, 12) -> (14, 10).

## Verified Tile Mechanics
- FLOOR_UP_WALL: Blocks DOWN (South) movement. (Verified: (12, 50) blocked south from (12, 49)). Allows NORTH movement. (Verified: (15, 51) -> (15, 50) -> (15, 49) worked).
- LEDGE_HOP_DOWN: Blocks NORTH movement. (Verified: (10, 15) is impassable from the south).
- Wall Gaps: (11, 47), (9, 33), (5, 35).

## Failed Hypotheses
- Island Hop (13, 16): Dead end pocket at (11, 14).
- Southern Surf Bypass: Eastern channel ends at Row 45.
- Great Southern Loop: Unnecessary as FLOOR_UP_WALL ledges allow North movement.

## Progress Summary
- Badges: 16/16.
- Current Focus: Ascending the Western Corridor.