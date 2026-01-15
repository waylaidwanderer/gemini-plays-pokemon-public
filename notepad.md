# Suicune Quest (Cianwood)
- Quest Start: Turn 48900

## Strategy: Western Loop Route
To reach the northern plateau at (14, 10), Gem must bypass the central walls and the Row 15 ledge. The confirmed path is to use the western corridor (X=2), accessible via the Row 26 cross-over.

## Execution Plan
1. Move to (12, 33) via the X=12 thoroughfare. <- CURRENT TASK
   - Path: (10, 47) -> (12, 47) -> (12, 33).
2. Move West through the (9, 33) gap to the central corridor.
   - Path: (12, 33) -> (6, 33).
3. Move North to Row 26 and West to the Western Corridor.
   - Path: (6, 33) -> (6, 26) -> (2, 26).
4. Move North to Row 12 and East to the plateau.
   - Path: (2, 26) -> (2, 12) -> (14, 12).
5. Move North to (14, 10) to trigger Suicune sighting.

## Verified Tile Mechanics
- FLOOR_UP_WALL: Blocks DOWN (South) movement. (Verified: (12, 50) and (10, 48) blocked south). Allows NORTH movement.
- LEDGE_HOP_DOWN: Blocks NORTH movement. (Verified: (10, 15) is impassable from the south).
- Wall Gaps: (9, 33) at Row 33, X=4-11 at Row 26.
- Corridors: X=12 (Northbound), X=2 (Bi-directional).

## Failed Hypotheses
- Row 44/45 West: Blocked by wall at (5, 44) and (5, 45).
- Island Hop (13, 16): Dead end pocket at (11, 14).
- Northern Gap Route (X=5): Blocked by wall at (5, 22).

## Progress Summary
- Badges: 16/16.
- Current Focus: Reaching the Row 33 gap.