# Suicune Quest: Cianwood City
## Verified Strategy: The Terrace Climb
The northern plateau (14, 10) is accessible via a series of one-way "upward" transitions that bypass the ledge system. This is a pure land route requiring a detour to the southern part of the city. Land travel south in Cianwood is blocked at Row 46 (Hypothesis: FLOOR_UP_WALL is one-way North).

### Execution Plan
1. Verification: Test the FLOOR_UP_WALL mechanic by attempting to move South onto (6, 46) from (6, 45). (In Progress)
2. Surf Detour: Return to Route 41 and Surf to (0, 51), then re-enter Cianwood City at (29, 51).
3. Southern Approach: Once at the southern beach, follow the terrace sequence to Suicune.

## Tile Mechanics
- FLOOR: Land (Traversable).
- FLOOR_UP_WALL: One-way North (Hypothesis). Blocks DOWN movement (e.g., (6, 46), (6, 34), (4, 30), (4, 20)).
- LEDGE_HOP_DOWN: One-way South. Blocks NORTH movement (e.g., (10, 15)).

## Battle Plan: Eusine
- Expected Team: Drowzee (Lv23), Haunter (Lv23), Electrode (Lv25).
- Lead: Calcifer (Lv64 Typhlosion). Strategy: Flamethrower sweep.

## Progress Log
- Turn 50120: Quest Start.
- Turn 50198: Attempted to move South into (6, 46); movement failed, confirming FLOOR_UP_WALL is one-way North.