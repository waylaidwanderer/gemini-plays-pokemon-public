# Suicune Quest (Cianwood)
- Quest Start: Turn 48900

## Strategy: Western Corridor Ascent
To reach the northern plateau at (14, 10), Gem must bypass the Row 15 ledge (LEDGE_HOP_DOWN), which blocks all NORTH movement except at the western corridor (X=0-2). The city's other "ledges" (Row 34, 46, 48, 50) are FLOOR_UP_WALL tiles that block SOUTH movement but allow NORTH traversal.

## Execution Plan
1. Backtrack to X=12 and move North to the Row 33 gap.
   - Path: (6, 44) -> (12, 44) -> (12, 33). (Done)
2. Move West through the (9, 33) wall gap to the central corridor.
   - Path: (12, 33) -> (6, 33). <- CURRENT TASK
3. Move South to Row 35 to bypass the Wall at X=5.
   - Path: (10, 33) -> (10, 35).
4. Move West through the (5, 35) gap to the Western Corridor (X=2).
   - Path: (10, 35) -> (2, 35).
5. Walk North along X=2 past the Row 15 ledge.
   - Path: (2, 35) -> (2, 12).
6. Walk East to the plateau and North to trigger Suicune.
   - Path: (2, 12) -> (14, 12) -> (14, 10).

## Verified Tile Mechanics
- FLOOR_UP_WALL: Blocks DOWN (South) movement. (Verified: (12, 50) blocked south from (12, 49); (6, 34) blocked south from (6, 33)). Allows NORTH movement.
- LEDGE_HOP_DOWN: Blocks NORTH movement. (Verified: (10, 15) is impassable from the south).
- Wall Gaps: (11, 47), (9, 33), (5, 35).
- Ledge Gaps: (12, 34), (18, 46), (12, 48), (11, 50).

## Failed Hypotheses
- Row 44/45 West: Blocked by wall at (5, 44) and (5, 45).
- Island Hop (13, 16): Dead end pocket at (11, 14).
- Southern Surf Bypass: Eastern channel ends at Row 45.

## Progress Summary
- Badges: 16/16.
- Current Focus: Backtracking to X=12.