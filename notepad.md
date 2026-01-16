# Johto Progression: The Rock Smash Quest
## Primary Goal: Obtain TM08 Rock Smash
- **Strategy:** Find the NPC on Route 36 who gives TM08.
- **Quest Started:** Turn 50407.
- **Hypothesis 1:** The NPC is near the (35, 9) junction where Sudowoodo was.
  - **Status:** Failed. Junction is clear (FLOOR), but no NPC is present (Turns 50463-50490).
- **Hypothesis 2:** The NPC is inside the National Park gatehouse (18, 9).
  - **Status:** Testing.
- **Hypothesis 3:** The NPC is inside the Ruins of Alph gatehouse (47, 13).
- **Hypothesis 4 (Quest Analyst):** Talk to the Fat Man NPC just to the right of the junction.
  - **Audit:** Fisher at (44, 9) is to the right. He gives flavor text but no TM (Turns 50430-50438).
  - **Sub-Hypothesis:** Need to talk to him from a different side (e.g., from below at 44, 10).
- **Hypothesis 5:** I need to talk to the Flower Shop girl in Goldenrod to "reset" the trigger.
  - **Audit:** I have the SquirtBottle and Sudowoodo is gone. Trigger should be active.

## Secondary Goal: Trigger Suicune Sighting in Cianwood City
- **Location:** (14, 10) in Cianwood City.
- **Status:** Blocked by boulders at (4, 19) and (8, 16).

## Global Tile Mechanics
- FLOOR: Traversable.
- WALL / BUOY / HEADBUTT_TREE: Impassable.
- WATER: Requires Surf.
- DOOR / WARP_CARPET: Warp point.
- SMASHABLE_ROCK (Object): Requires Rock Smash.

## Lessons Learned
- **Dialogue vs Item:** NPC dialogue describing a move is flavor text. Only "received TMxx" counts.
- **Pathing:** Vertical tree lines at X=23-25 and X=31 block East-West movement on most rows. Row 14 is a long horizontal path but blocked at X=16.

## Verified Information & Failed Hypotheses
- Fisher at (44, 9): Flavor text only from the left.
- Youngster Arthur at (45, 6): Hard Stone on Thursdays.
- Sudowoodo Junction (35, 9): No NPC present.
- PC Storage: TM08 not present.
- **Hypothesis 6:** Visit the Goldenrod Flower Shop and talk to the clerk (reward for clearing Sudowoodo?).
- **Hypothesis 7:** Talk to the NPC at the junction (35, 9) again after a map refresh (enter/exit gatehouse).
- **Status:** Heading to (44, 10) to talk to Fisher from below. (Attempt 1)
- **Hypothesis 8:** TM08 is already in the PC.
  - **Audit:** Fisher at (44, 9) gives post-gift flavor text ("If any rocks are in your way, just smash 'em up!").
  - **Plan:** Talk to Fisher from below at (44, 10) one last time, then Fly to Violet City to check the PC.
- **Arthur (46, 6):** It is Friday. Arthur only gives the Hard Stone on Thursdays. Skip.