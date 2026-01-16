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
- **Status:** Searching for TM08 Rock Smash. Pokefan M (18, 33) gives a hint but no TM.
- **Plan:**
  1. Talk to Lass at (14, 40). (Next)
  2. Check Lugia Speech House at (15, 37).
  3. Stun Pokefan M (ID 2) and talk to him from the front (17, 34) or (18, 34).
  4. Re-verify Route 36 if Cianwood is a dead end.

## Failed Hypotheses
- **Hypothesis 1:** Pokefan M (18, 33) gives TM08 by just talking.
  - **Attempts:** 10+ (Turns 50278-50314)
  - **Result:** Hint only. NPC movement makes interaction difficult.
- **Hypothesis 2:** Talking to Pokefan F (10, 46) triggers the gift from her husband.
  - **Attempts:** 1 (Turn 50300)
  - **Result:** She mentions him, but he still doesn't give the TM.
- **Hypothesis 3:** Mania (2, 4) gives TM08.
  - **Attempts:** 1 (Turn 50291)
  - **Result:** Dead end.