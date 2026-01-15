# Suicune Quest (Cianwood)
- Quest Start: Turn 48900

## Strategy: Western Corridor Ascent
To reach the northern plateau at (14, 10), Gem must bypass the Row 15 ledge (LEDGE_HOP_DOWN), which blocks all NORTH movement except at the western corridor (X=0-2). The city's other "ledges" (Row 34, 46, 48, 50) are FLOOR_UP_WALL tiles that block SOUTH movement but allow NORTH traversal.

## Execution Plan (Southern Bypass Route)
1. Move to the eastern thoroughfare via the Row 28 bypass.
   - Path: (6, 22) -> (6, 26) -> (11, 26) -> (11, 28) -> (12, 28). <- CURRENT TASK
2. Move South to Row 47 and West through the wall gap.
   - Path: (12, 28) -> (12, 47) -> (8, 47).
3. Navigate North to Row 35 via the X=4 corridor.
   - Path: (8, 47) -> (8, 44) -> (4, 44) -> (4, 35).
4. Move West through the X=3 wall gap to the Western Corridor (X=2).
   - Path: (4, 35) -> (2, 35).
5. Walk North along X=2 past the Row 15 ledge.
   - Path: (2, 35) -> (2, 12).
6. Walk East to the plateau and North to trigger Suicune.
   - Path: (2, 12) -> (14, 12) -> (14, 10).

## Verified Tile Mechanics
- FLOOR_UP_WALL: Blocks DOWN (South) movement. (Verified: (12, 50) blocked south from (12, 49); (6, 34) blocked south from (6, 33)). Allows NORTH movement.
- LEDGE_HOP_DOWN: Blocks NORTH movement. (Verified: (10, 15) is impassable from the south).
- Wall Gaps: (9, 33), (9, 47), (5, 24-28), (5, 35), (3, 20-22), (3, 30-35), (4, 43).
- Objects: (4, 25), (4, 19), (5, 29), (8, 16), (9, 17), (10, 27) are ROCK objects (walls).

## Failed Hypotheses
- Direct West from (6, 22): Blocked by wall at X=5.
- Middle Corridor (X=4): Dead end at Row 15.
- Island Hop (13, 16): Dead end pocket at (11, 14).

## Progress Summary
- Badges: 16/16.
- Current Focus: Moving to the Row 26 bypass.