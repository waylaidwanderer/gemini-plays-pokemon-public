# Suicune Quest: Cianwood City
## Objective
Trigger the Suicune sighting at (14, 10) in Cianwood City (Map 22_3).

## Strategy: The Western Bypass (Land Route)
1. Obtain Rock Smash: Talk to Pokefan M at (17, 33). (Dialogue triggered, but TM not received. Re-evaluating need.)
2. Wall Gap: Walk West from (16, 33) to (5, 34) to pass through the internal wall.
3. Terrace Ascent: Walk North through Column 4 and climb the one-way slopes:
   - Climb 1: (4, 30) [UP_WALL]
   - Climb 2: (4, 20) [UP_WALL]
4. Northern Loop: Walk North to Row 14, East to (8, 14), North to Row 12, and East to (14, 12).
5. Trigger Event: Reach (14, 10).

## Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- WATER: Requires Surf.
- BUOY: Impassable (Water barrier).
- DOOR: Warp point.
- LEDGE_HOP_DOWN: One-way South jump. Impassable from North/East/West.
- FLOOR_UP_WALL: One-way North climb. Impassable from North/East/West.
- SMASHABLE_ROCK (Object): Impassable. Requires Rock Smash to clear.

- **Start Turn:** 50283
- **Status:** Searching for TM08 Rock Smash.
- **Plan:**
  1. Talk to Lass at (14, 44). (Completed: Talks about Chuck)
  2. Check Pharmacy (15, 47). (Next)
  3. Investigate Lugia Speech House (15, 37).
  4. Check Route 36 (Guy who gives TM08 after Sudowoodo).

## Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- WATER: Requires Surf.
- BUOY: Impassable (Water barrier).
- DOOR: Warp point.
- LEDGE_HOP_DOWN: One-way South jump. Impassable from North/East/West.
- FLOOR_UP_WALL: One-way North climb. Impassable from North/East/West.
- SMASHABLE_ROCK (Object): Impassable. Requires Rock Smash to clear.

## Failed Hypotheses
- **Hypothesis 1:** Pokefan M (18, 33) gives TM08.
  - **Attempts:** 10+ (Turns 50278-50314)
  - **Result:** Hint only.
- **Hypothesis 2:** Pokefan F (10, 46) gives TM08.
  - **Attempts:** 1 (Turn 50300)
  - **Result:** Hint only.
- **Hypothesis 3:** Mania (2, 4) gives TM08.
  - **Attempts:** 1 (Turn 50291)
  - **Result:** Dead end.
- **Hypothesis 4:** Rock Smash is not required for the Western Bypass.
  - **Attempts:** 1 (Turn 50310, pathfinder check)
  - **Result:** Pathfinder failed to find a route without Rock Smash. Verified.
- **Hypothesis 5:** Lass (14, 44) gives TM08.
  - **Attempts:** 1 (Turn 50321)
  - **Result:** Talks about Chuck. Dead end.