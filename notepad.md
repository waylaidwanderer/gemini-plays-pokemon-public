# Johto Progression: The Rock Smash Quest
## Primary Goal: Obtain TM08 Rock Smash
- **Strategy:** Find the NPC on Route 36 who gives TM08.
- **Quest Started:** Turn 50407.
- **Hypothesis:** The NPC is near the (35, 9) junction where Sudowoodo was.
- **Hypothesis 2:** The NPC is inside the National Park gatehouse (18, 9).
- **Hypothesis 3:** The NPC is inside the Ruins of Alph gatehouse (47, 13).
- **Next Step:** Explore the National Park gatehouse at (18, 9).

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
- **Dialogue vs Item:** NPC dialogue describing a move (e.g., Fisher at 44, 9) is flavor text. Only "GEM received TMxx" indicates a successful item acquisition.
- **Pathing:** Headbutt trees block direct paths. Navigation must account for these static obstacles.

## Verified Information & Failed Hypotheses
- Eastern Water Route (Cianwood): Blocked by Row 15 wall/buoy line.
- Cianwood NPCs: Hints only (Turns 50278-50364).
- Fisher at (44, 9): Flavor text only.
- Lass at (51, 8): No TM.
- Youngster Arthur at (45, 6): Hard Stone on Thursdays.
- PC Storage: TM08 not present. Skip PC checks until item is confirmed received.