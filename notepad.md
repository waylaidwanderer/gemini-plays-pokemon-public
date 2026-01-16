# Johto Progression: The Rock Smash Quest
## Primary Goal: Obtain TM08 Rock Smash
- **Strategy:** Find the NPC on Route 36 who gives TM08.
- **Quest Started:** Turn 50407.
- **Hypothesis 1:** The NPC is near the (35, 9) junction where Sudowoodo was.
  - **Status:** Failed. Junction is clear (FLOOR), but no NPC is present (Turns 50463-50490).
- **Hypothesis 2:** The NPC is inside the National Park gatehouse (18, 9).
  - **Status:** Testing. Heading there now.
- **Hypothesis 3:** The NPC is inside the Ruins of Alph gatehouse (47, 13).
- **Hypothesis 4 (From Quest Analyst):** I need to defeat Whitney and get the SquirtBottle first.
  - **Audit:** I have the Plain Badge (Whitney defeated) and the SQUIRTBOTTLE in my Key Items. Sudowoodo is already gone. This trigger is already flipped.
- **Hypothesis 5:** I need to talk to the Flower Shop girl in Goldenrod to "reset" the trigger or receive a follow-up.

## Secondary Goal: Trigger Suicune Sighting in Cianwood City
- **Location:** (14, 10) in Cianwood City.
- **Status:** Blocked by boulders at (4, 19) and (8, 16).
- **Route to Suicune:** From (12, 17) -> (11, 16) -> (11, 12) -> (14, 12) -> (14, 10).

## Global Tile Mechanics
- FLOOR: Traversable.
- WALL / BUOY: Impassable.
- WATER: Requires Surf.
- DOOR / WARP_CARPET: Warp point.
- LEDGE_HOP_DOWN: One-way South jump.
- FLOOR_UP_WALL: One-way North climb.
- SMASHABLE_ROCK (Object): Impassable. Requires Rock Smash.
- HEADBUTT_TREE: Impassable. Can be shaken with Headbutt.

## Lessons Learned
- **Dialogue vs Item:** NPC dialogue describing a move (e.g., Fisher at 44, 9) is flavor text. Only "received TMxx" indicates acquisition.
- **Pathing:** Headbutt trees block direct paths.
- **Quest Prerequisite:** Sudowoodo must be cleared (Confirmed: SquirtBottle in inventory, junction is FLOOR).

## Verified Information & Failed Hypotheses
- Fisher at (44, 9): Flavor text only.
- Lass at (51, 8): No TM.
- Youngster Arthur at (45, 6): Hard Stone on Thursdays.
- Sudowoodo Junction (35, 9): No NPC present.
- PC Storage: TM08 not present. Skip PC checks.