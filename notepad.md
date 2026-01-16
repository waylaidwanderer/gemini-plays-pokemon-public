# Suicune Quest: Cianwood City
## Verified Strategy: The Terrace Climb
The northern plateau (14, 10) is accessible via a series of one-way "upward" transitions that bypass the ledge system. This is a pure land route requiring a detour to the southern part of the city. Land travel south in Cianwood is blocked at Row 46 (Hypothesis: FLOOR_UP_WALL is one-way North).

### Execution Plan
1. Re-entry: Return to Cianwood City via the (0, 45) warp in Route 41. (In Progress)
2. Path Analysis: Use run_code in Cianwood to find a definitive path to the southern beach, accounting for buoys, ledges, and smashable rocks.
3. Verification: Test the FLOOR_UP_WALL mechanic by attempting to move South onto (6, 46) from (6, 45).
4. Southern Approach: Once at the southern beach, follow the terrace sequence to Suicune.

## Tile Mechanics
- FLOOR: Land (Traversable).
- FLOOR_UP_WALL: One-way North (Hypothesis). Blocks DOWN movement (e.g., (6, 46), (6, 34), (4, 30), (4, 20)).
- LEDGE_HOP_DOWN: One-way South. Blocks NORTH movement (e.g., (10, 15)).

## Battle Plan: Eusine
- Expected Team: Drowzee (Lv23), Haunter (Lv23), Electrode (Lv25).
- Lead: Calcifer (Lv64 Typhlosion). Strategy: Flamethrower sweep.