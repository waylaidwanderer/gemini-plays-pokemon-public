# Suicune Quest: Cianwood City
## Verified Strategy: The Terrace Climb
The northern plateau (14, 10) is accessible via a series of one-way "upward" transitions that bypass the ledge system. This is a pure land route requiring a detour to the southern part of the city. Land travel south is blocked at Row 46 (Hypothesis: FLOOR_UP_WALL is one-way North), so a Surf detour is required.
- Quest Start: Turn 50120 (approx)

### Execution Plan
1. Surf Detour: Surf south from (28, 45) via the eastern channel (Cols 30-31) and land on the beach at (23, 51).
2. Southern Approach: Walk West to (6, 51) and North to (6, 47).
3. First Climb: Move North from (6, 47) through (6, 46) [UP_WALL] to reach Row 45.
4. Second Climb: Move North from (6, 35) through (6, 34) [UP_WALL] to reach Row 33.
5. Third Climb: Move West to (4, 31) and North through (4, 30) [UP_WALL] to reach Row 29.
6. Fourth Climb: Move North from (4, 21) through (4, 20) [UP_WALL] to reach Row 19.
7. Plateau Entry: Walk to (4, 14), then East to (8, 14), then North to (8, 12).
8. Final Approach: Walk East along Row 12 to (14, 12) and North to Suicune at (14, 10).

## Tile Mechanics
- FLOOR: Land (Traversable).
- FLOOR_UP_WALL: One-way North (Hypothesis). Blocks DOWN movement (e.g., (6, 46), (6, 34), (4, 30), (4, 20)).
- LEDGE_HOP_DOWN: One-way South. Blocks NORTH movement (e.g., (10, 15)).

## Battle Plan: Eusine
- Expected Team: Drowzee (Lv23), Haunter (Lv23), Electrode (Lv25).
- Lead: Calcifer (Lv64 Typhlosion). Strategy: Flamethrower sweep.

## Hallucination Correction
- Previous claim that the plateau is "inaccessible from land" was incorrect. The UP_WALL tiles are traversable from the South, providing a valid path.

## Map Markers
- (14, 10): ✨ Suicune Trigger Point
- (6, 34): 🧗 Terrace Climb 1
- (4, 30): 🧗 Terrace Climb 2
- (4, 20): 🧗 Terrace Climb 3
- (5, 29), (10, 27), (4, 25), (4, 19): 🪨 Smashable Rocks.