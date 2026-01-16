# Suicune Quest: Cianwood City
## Verified Strategy: The Terrace Climb
The northern plateau (14, 10) is accessible via a series of one-way "upward" transitions that bypass the ledge system. This is a pure land route requiring a detour to the southern part of the city. Land travel south in Cianwood is blocked at Row 46 (Hypothesis: FLOOR_UP_WALL is one-way North).

### Execution Plan
1. Re-entry: Return to Cianwood City via the (0, 45) warp in Route 41. (In Progress)
2. Surf South: In Cianwood, Surf south from (29, 45) along the eastern water channel to Row 51.
3. Landing: Land on the southern beach at (23, 51).
4. Southern Approach: Walk West to (6, 51) and North to (6, 47).
5. First Climb: Move North from (6, 47) through (6, 46) [UP_WALL] to reach Row 45.
6. Second Climb: Move North from (6, 35) through (6, 34) [UP_WALL] to reach Row 33.
7. Third Climb: Move West to (4, 31) and North through (4, 30) [UP_WALL] to reach Row 29.
8. Fourth Climb: Move North from (4, 21) through (4, 20) [UP_WALL] to reach Row 19.
9. Plateau Entry: Walk to (4, 14), then East to (8, 14), then North to (8, 12).
10. Final Approach: Walk East along Row 12 to (14, 12) and North to Suicune at (14, 10).

## Tile Mechanics
- FLOOR: Land (Traversable).
- FLOOR_UP_WALL: One-way North (Hypothesis). Blocks DOWN movement (e.g., (6, 46), (6, 34), (4, 30), (4, 20)).
- LEDGE_HOP_DOWN: One-way South. Blocks NORTH movement (e.g., (10, 15)).

## Observations
- Route 41 (0, 49) is NOT a transition point (confirmed via Left movement failure).
- Route 41 (0, 44) and (0, 45) ARE verified transitions.