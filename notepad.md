# Game Mechanics & Systems

## Tile Traversal Rules (Consolidated)
- **Impassable:** BOOKSHELF, BUOY (assumed), COUNTER, CUT_TREE, HEADBUTT_TREE, INCENSE_BURNER, MART_SHELF, PC, PILLAR (usually), POKEDEX, RADIO, TOWN_MAP, TV, VOID, WALL, WATER, WINDOW, TABLE.
- **Traversable (Visual Obstacles):** PLANT (The sprite is an obstacle, but the tile type is FLOOR).
- **Traversable:** FLOOR, GRASS, LONG_GRASS, TALL_GRASS.
- **One-Way (Ledges):**
  - LEDGE_HOP: General one-way tile.
  - LEDGE_HOP_DOWN: One-way down.
  - LEDGE_HOP_LEFT: One-way left.
  - LEDGE_HOP_RIGHT: One-way right.
  - FLOOR_UP_WALL: Cannot be moved *down from* this tile, and cannot be moved *down onto* this tile.
- **Warps (Directional/Conditional):**
  - CAVE: Standard warp point.
  - DOOR: Standard warp, sometimes conditional based on story events.
  - LADDER: Directional warp that requires facing the ladder to use.
  - WARP_CARPET: General directional warp mat.
  - WARP_CARPET_UP: Moves player up one floor.
  - WARP_CARPET_DOWN: Moves player down one floor. Can be one-way and may require pressing 'Down' to activate.
  - WARP_CARPET_LEFT: Moves player left.
  - WARP_CARPET_RIGHT: Moves player right.

## Evolution Methods
- Some POKEMON evolve only by being traded: MACHOKE, KADABRA, HAUNTER, and GRAVELER.

## Respawning Obstacles (CONFIRMED MECHANIC)
- **Initial Observation (Turn 26648):** The `CUT_TREE` at (8, 25) in Ilex Forest, which was previously removed, respawned after re-entering the area.
- **Confirmation (Turn 27669):** The `CUT_TREE` at (13, 5) on Route 31, which was also previously removed, has respawned.
- **Conclusion:** Obstacles cleared with HMs like CUT are not permanently removed. They respawn when re-entering a map. This is a consistent game mechanic and must be factored into all future path planning. My pathfinding tools must always treat `CUT_TREE` tiles as impassable unless I have just cut them in the current session on the map.

## Known Bugs / Strange Mechanics
- **Item Tossing Bug:** Attempting to 'TOSS' a single-stack item (e.g., BERRY x1) from the bag menu fails and resets the menu. Tossing one item from a multi-item stack (e.g., POTION x9 -> x8) also fails to free an inventory slot. The only confirmed way to free a slot is to have a Pokémon 'HOLD' a single-stack item.

# Active Quests & Notes

## Mail Delivery
- **Status:** On Hold.
- **Task:** Deliver SPEAROW with MAIL to an officer.
- **Attempt 1 (Failed):** An officer in the Route 35 Goldenrod Gate gave the quest.
- **Attempt 2 (Failed):** An officer in the Route 31 Violet Gate was not the recipient. The quest is on hold until the correct NPC is found.

## GINA's Item
- **Status:** COMPLETE.
- **Task:** Received LEAF STONE from GINA on Route 34 after making space in my bag.

## Miltank Healing
- **Status:** On Hold.
- **Task:** Find a BERRY to heal the sick Miltank on Route 39.
- **Location:** Moomoo Farm, barn building.
- **Failed Attempt:** Spoke to Wade on Route 31 after he called about having berries. He did not provide a BITTER BERRY or any other kind of berry. The solution lies elsewhere.

# Gym Information
- **Goldenrod Gym:** Normal-type. Fighting-type moves are recommended.

# Tool Development & Philosophy

## Tool Development Philosophy (Self-Correction)
- **Correction (Turn 28227):** My previous assumptions about my pathfinding tools being faulty were incorrect. The tools were functioning as designed. The errors stemmed from my misinterpretation of the output, incorrect manual pathing attempts, and failure to investigate in-game obstacles. This highlights the critical need to trust my tools and carefully verify my own actions before assuming a tool is broken. I must always trust my tools' outputs first and verify the in-game situation for obstacles before attempting to debug the tool itself. This is a recurring failure in my methodology that I must correct.

## Tool Implementation Priority

## Agent/Tool Ideas
- **`multi_map_navigator` (Tool):** A tool that can plan a route across multiple maps. It would take a final destination (e.g., a city or route number) and generate a sequence of `path_and_execute_v3` calls to navigate through each map segment automatically.

- **`battle_state_parser` (Tool):** A supporting tool for the battle advisor. It would parse raw screen text and game state during a battle and output a structured JSON object with current HP, status, known moves, etc., for both my Pokémon and the opponent.
- **`puzzle_data_compiler` (Agent):** An agent to maintain a structured summary of a complex puzzle's state. I would feed it observations turn-by-turn, and it would compile the data, which could then be used as input for the `puzzle_solver_assistant`.

- **`area_clearance_agent` (Agent):** Takes a list of NPC coordinates and unexplored warps on a map and generates a prioritized, efficient plan to visit each one, ensuring complete exploration.

# Key Items
- BICYCLE: Received from the Goldenrod Bike Shop owner. Allows for faster travel.
- ITEMFINDER: Received from a man in Ecruteak City. Used to find hidden items.

<details>
<summary>Day-Care Mystery (Route 34)</summary>

- **Initial Observation:** Day-Care Man and Woman mentioned my Unown 'O' and something called 'Glyph' despite me never depositing 'O'.
- **Test 1 (Interaction @ 14, 18):**
  - **Result:** Dialogue appeared: "It's O that was left with the DAY-CARE MAN. It has no interest in Glyph."
- **Test 2 (Interaction @ 17, 19):**
  - **Result:** Dialogue appeared: "It's Glyph that was left with the DAY-CARE LADY. It has no interest in O."
- **Conclusion:** The two Pokémon in the yard, "O" and "Glyph", were left with the Day-Care couple. They do not seem to get along. The game is somehow linking my caught Unown 'O' to the 'O' in the Day-Care, even though I never deposited it. The mystery is ongoing.

</details>

# Ecruteak City Notes

## General Info
- Met BILL in the Pokémon Center upon first entry (Turn 29604). He announced the TIME CAPSULE is finished and left for Goldenrod City.
- A man mentioned there are hidden items in the BURNED TOWER, which may be related to finding Morty.

## Ecruteak Gym
- **Leader:** Morty
- **Title:** The Mystic Seer of the Future
- **Likely Type:** Ghost or Psychic

# Untested Assumptions & Alternative Hypotheses (Self-Assessment)
- **Assumption:** The path to my Rival, Crimson, in the Burned Tower is permanently blocked by the broken floor.
  - **Alternative Hypothesis:** An event, possibly triggered by exploring other parts of the tower or interacting with key NPCs like Morty and Eusine, is required to repair the floor or open an alternate route.
  - **Test to Falsify:** Systematically explore all other reachable areas and warps in the Burned Tower. If no progress is made, the assumption may be correct, but exploration must be exhausted first.
- **Assumption:** The mail delivery officer is on Route 31.
    - **Alternative Hypothesis:** The officer could be on any route connected to Goldenrod. I've only checked one gate.
    - **Test to Falsify:** Systematically check all other gates connected to major routes.

# Phone Contacts
- **TODD (CAMPER):** Met on Route 34. Calls with training tips.

# Archive: Solved Puzzles & Lessons Learned

<details>
<summary>Wade's Berries (Hypothesis Falsified)</summary>

- **Assumption:** Wade on Route 31 would give me a `BITTER BERRY` for the sick Miltank after calling me.
- **Test:** Defeated Wade in a rematch and spoke to him on Turn 31288.
- **Result:** Wade's dialogue was non-committal ("You'll hear from me..."). He did not provide any berries.
- **Conclusion:** Hypothesis is FALSE. The solution to the Miltank quest is not with Wade.

</details>

<details>
<summary>Day-Care Tile Test (SOLVED)</summary>

- **System Critique:** Suggested testing 'TABLE' and 'PLANT' tiles.
- **Observation:** Tiles at (2, 4) and (5, 4) have table/plant sprites but are listed as 'FLOOR' in map data.
- **Test 1 (Turn 29321):** Moved from (1, 4) to (2, 4). Result: Move successful. The tile is traversable.
- **Test 2 (Turn 29327):** Moved from (5, 5) to (5, 4). Result: Move successful. The tile is traversable.
- **Conclusion:** Visual sprites do not always indicate impassable terrain. The tile's `type` attribute is the source of truth.

</details>

<details>
<summary>Dance Theater Gentleman (Lesson Learned)</summary>

- **Hypothesis:** Defeating all Kimono Girls would cause the Gentleman at (7, 10) to give a reward.
- **Test:** Defeated all five Kimono Girls and repeatedly interacted with the Gentleman between turns 29727 and 29738.
- **Result:** The Gentleman only repeated his initial, pre-defeat dialogue. No new outcome was triggered.
- **Conclusion:** Hypothesis is FALSE. Repeatedly interacting with an NPC that provides no new information is an invalid strategy and will not yield new results. This confirms my general interaction rule: if an NPC doesn't change their dialogue after a significant event, move on.

</details>

<details>
<summary>Lessons Learned (Archive)</summary>

## Map Marker Discipline (Overwatch Critique, Turn 29822)
- **Failure:** I failed to immediately mark the warp at (6, 13) in the Dance Theater, violating the 'immediate update' directive.
- **Correction:** I must be diligent in marking **both** the entry and exit points of any warp immediately after using it. This is critical for maintaining accurate navigation data.

## VOID Tile
- **Observation (Turn 30248):** The `VOID` tile type is impassable. This was confirmed by the pathfinder failing to route through it and must be added to the consolidated list of impassable tiles.

## Missed Map Marker (Overwatch Critique, Turn 30601)
- **Failure:** I failed to mark the Ecruteak City side of the Burned Tower warp, violating the 'immediate update' directive.
- **Correction:** I must be diligent in marking **both** the entry and exit points of any warp immediately after using it. This is critical for maintaining accurate navigation data.

</details>

# Burned Tower Notes
- The rock at (15, 4) requires a POKéMON move to break it, likely Rock Smash. This path is currently blocked.
- **Assumption:** The legendary beasts will now be roaming the world.
  - **Alternative Hypothesis:** The event was just a cutscene, and they are not actually catchable yet, or they are in a specific, fixed location.
  - **Test to Falsify:** This is difficult to test directly. I must rely on future NPC dialogue or random encounters to confirm or deny their roaming status.
- **Puzzles/Special:** PIT (Appears to be a one-way warp, likely down. Needs testing.)