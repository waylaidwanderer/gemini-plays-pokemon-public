# Suicune Quest (Cianwood)
- Quest Start: Turn 48900

## Strategy: Western Corridor Ascent
To reach the northern plateau at (14, 10), Gem must bypass the Row 15 ledge (LEDGE_HOP_DOWN), which blocks all NORTH movement except at the western corridor (X=0-2). The city's other "ledges" (Row 34, 46, 48, 50) are FLOOR_UP_WALL tiles that block SOUTH movement but allow NORTH traversal.

## Execution Plan (Northern Gap Route)
1. Move North in the central corridor to Row 26.
   - Path: (6, 33) -> (6, 26). <- CURRENT TASK
2. Move West through the X=5 wall gap.
   - Path: (6, 26) -> (4, 26).
3. Move North to Row 22 and West through the X=3 wall gap.
   - Path: (4, 26) -> (4, 22) -> (2, 22).
4. Walk North along X=2 past the Row 15 ledge.
   - Path: (2, 22) -> (2, 12).
5. Walk East to the plateau and North to trigger Suicune.
   - Path: (2, 12) -> (14, 12) -> (14, 10).

## Verified Tile Mechanics
- FLOOR_UP_WALL: Blocks DOWN (South) movement. (Verified: (12, 50) blocked south from (12, 49); (6, 34) blocked south from (6, 33)). Allows NORTH movement.
- LEDGE_HOP_DOWN: Blocks NORTH movement. (Verified: (10, 15) is impassable from the south).
- Wall Gaps: (9, 33), (5, 24-28), (3, 20-22), (3, 30-33).
- Objects: (4, 25), (5, 29), (8, 16), (9, 17), (10, 27) are ROCK objects (walls).

## Failed Hypotheses
- Row 44/45 West: Blocked by wall at (5, 44) and (5, 45).
- Island Hop (13, 16): Dead end pocket at (11, 14).
- Southern Surf Bypass: Eastern channel ends at Row 45.

## Progress Summary
- Badges: 16/16.
- Current Focus: Moving to the Row 26 gap.