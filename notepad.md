# Game Mechanics & Systems

## Tile Traversal Rules
- **Impassable:** BOOKSHELF, BUOY (assumed), COUNTER, CUT_TREE, HEADBUTT_TREE, INCENSE_BURNER, MART_SHELF, PC, PILLAR (usually), RADIO, TOWN_MAP, TV, VOID, WALL, WATER, WINDOW, TABLE.
- **Traversable (Visual Obstacles):** PLANT (The sprite is an obstacle, but the tile type is FLOOR).
- **Traversable:** FLOOR, GRASS, LONG_GRASS, TALL_GRASS, UNKNOWN.
- **One-Way (Ledges):**
  - LEDGE_HOP: General one-way tile.
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

# Gym Information
- **Goldenrod Gym:** Normal-type. Fighting-type moves are recommended.

# Untested Assumptions & Alternative Hypotheses
- **Assumption:** The strange dialogue from Gramps and Granny ('Your O', 'your Glyph') is related to the Unown I caught.
  - **Alternative Hypothesis:** It could be a default dialogue that triggers if you don't have any Pokémon in the Day-Care, and 'O' or 'Glyph' is just a placeholder or a bug.
  - **Test to Falsify:** The next time I have a free party slot and some money, I will deposit a common Pokémon (like a Pidgey) and then immediately talk to them again. If the dialogue changes to refer to the Pidgey by name, my initial hypothesis is likely correct. If it stays the same, the dialogue is likely just a default script.
- **Assumption:** HM Flash is in Violet City.
  - **Alternative Hypothesis:** HM Flash might be in a different city, or the solution to Dark Cave doesn't require Flash.
  - **Test to Falsify:** If a systematic search of all buildings and NPCs in Violet City yields no HM, I must conclude it is not here and proceed to the next available area.
- **Assumption:** The two `WEIRD_TREE` objects on Route 37 are Sudowoodo that require the SQUIRT BOTTLE.
  - **Alternative Hypothesis:** They could be a different type of event tree requiring a different item/trigger, or a permanent story blockade.
  - **Test to Falsify:** Next time on Route 37, use the SQUIRT BOTTLE on them. If nothing happens, the assumption is false.

# Tool Development & Philosophy

## Tool Development Philosophy (Self-Correction)
- **Correction (Turn 28227):** My previous assumptions about my pathfinding tools being faulty were incorrect. The tools were functioning as designed. The errors stemmed from my misinterpretation of the output, incorrect manual pathing attempts, and failure to investigate in-game obstacles. This highlights the critical need to trust my tools and carefully verify my own actions before assuming a tool is broken. I must always trust my tools' outputs first and verify the in-game situation for obstacles before attempting to debug the tool itself. This is a recurring failure in my methodology that I must correct.

## Map Marker Strategy for Pathfinding
- **Problem:** My `path_and_execute` tool treats all '📍' markers as impassable walls, which is incorrect for non-blocking NPCs and has caused repeated pathing failures.
- **Immediate Workaround:** I will use the '💬' emoji to mark non-blocking, dialogue-only NPCs. My pathfinder does not recognize this emoji, so it will not treat them as obstacles.
- **Long-Term Goal:** I need to update the `path_and_execute` tool to have more sophisticated logic, allowing it to differentiate between blocking and non-blocking markers instead of relying on this workaround.

## Agent/Tool Ideas
- **`strategic_battle_advisor` (Agent):** A more advanced battle agent that takes into account my entire party, the opponent's known movesets, and suggests not just the best move but also whether to switch Pokémon.
- **`battle_state_parser` (Tool):** A supporting tool for the battle advisor. It would parse raw screen text and game state during a battle and output a structured JSON object with current HP, status, known moves, etc., for both my Pokémon and the opponent.
- **`puzzle_data_compiler` (Agent):** An agent to maintain a structured summary of a complex puzzle's state. I would feed it observations turn-by-turn, and it would compile the data, which could then be used as input for the `puzzle_solver_assistant`.
- **`use_hm` (Tool):** A tool to automate the menu navigation for using an HM move outside of battle. It would take a Pokémon's name and the move name as input and generate the necessary button presses.
- **`repel_strategist` (Agent):** Agent to analyze location, party, and inventory to decide if using a Repel is more efficient than running from many wild battles.
- **`area_clearance_agent` (Agent):** Takes a list of NPC coordinates and unexplored warps on a map and generates a prioritized, efficient plan to visit each one, ensuring complete exploration.
- **`path_interruption_diagnoser` (Agent):** When movement is blocked, this agent would analyze the situation (e.g., tile type, presence of moving vs. static NPCs) and suggest the most logical next step, like recalculating a path or using `stun_npc`.
- **`auto_clear_dialogue` (Tool):** A tool to automatically press 'A' to clear any on-screen dialogue, like phone calls.
- **`inventory_manager` (Agent):** An agent to analyze the bag and suggest the least valuable item to toss when inventory is full.

# Appendix: Solved Puzzles & Lessons Learned

## HEADBUTT_TREE Mechanics Test
- **Observation:** The `HEADBUTT_TREE` tile type is impassable.
- **Hypothesis 1 (Turn 24065):** The `HEADBUTT_TREE` is an interactable object that responds to the 'A' button.
- **Test:** Stood at (25, 4), faced down, and pressed 'A' on the tree at (25, 5).
- **Result:** No text appeared, and no action occurred.
- **Conclusion:** Hypothesis 1 is FALSE. The tree does not respond to a standard 'A' button interaction. It is likely that the move 'Headbutt' is required to interact with these trees. For now, they are impassable obstacles.

## SQUIRT BOTTLE Quest & WEIRD_TREE Puzzle (SOLVED)
- **Objective:** Clear the WEIRD_TREE on Route 36.
- **Solution:**
  1. Defeat Gym Leader Whitney in Goldenrod Gym.
  2. Speak to the Lass at (9, 6) in the Gym. This prompts Whitney to give you the Plain Badge and TM45.
  3. Go to the Goldenrod Flower Shop. The woman at (2, 3) will give you the SQUIRT BOTTLE.
  4. Travel to Route 36 and use the SQUIRT BOTTLE on the WEIRD_TREE at (35, 9).
  5. The tree reveals itself as a Sudowoodo. After the encounter, the path is clear.
  6. An NPC at (36, 9) will then give you TM08 (Rock Smash).

## SQUIRT BOTTLE Investigation (SOLVED)
- **Problem:** The SQUIRT BOTTLE is missing from my bag.
- **Hypothesis 1:** The Teacher NPC in the Goldenrod Flower Shop will provide a replacement. **Result: FALSE.**
- **Hypothesis 2:** The Lass NPC in the Goldenrod Flower Shop will provide a replacement or clue. **Result: FALSE.**
- **Hypothesis 3:** Whitney in the Goldenrod Gym will provide a replacement or clue. **Result: FALSE.**
- **Hypothesis 4:** One of my party Pokémon is holding the item. **Result: TRUE (Ignis was holding it).**
- **Hypothesis 5:** The item is in the PC's Item Storage. **Result: FALSE.**
- **Hypothesis 6:** A Pokémon in the PC is holding the item. **Result: FALSE.**
- **Conclusion:** My bag was full during the initial conversation, so the item was automatically given to my lead Pokémon to hold.

## HM Move Mechanics
- **Forgetting HMs:** It has been confirmed that HM moves (like CUT) cannot be forgotten via TM replacement. This suggests a special NPC, the 'Move Deleter', may be required to remove them, a common feature in later games. This needs to be verified.

## HEADBUTT Mechanic
- Received TM02 (HEADBUTT) from a Rocker NPC in Ilex Forest at (15, 14).
- My Typhlosion, Ignis, already knows this move.
- This move can be used on `HEADBUTT_TREE` tiles outside of battle by facing the tree and pressing 'A'.
- **Test 1 (Turn 28043):** Used HEADBUTT on the tree at (16, 14). Result: "Nope. Nothing…".

## Dark Cave Notes

## Tile Traversal Rules (Initial Observations)
- **Traversable:** FLOOR
- **Impassable:** WALL, WATER
- **One-Way:** LEDGE_HOP_DOWN, LEDGE_HOP_LEFT
- **Warp:** WARP_CARPET_DOWN

## Route 31 Cooltrainer (SOLVED)
- **Hypothesis:** The Cooltrainer M blocking the path on Route 31 must be defeated to proceed.
- **Test:** After stunning him, I interacted with him at (33, 8).
- **Result:** He gave flavor text about needing a POKéMON with a light-up move for Dark Cave. No battle was initiated.
- **Conclusion:** Hypothesis is FALSE. He is a non-battling NPC who provides a hint. He was also not blocking the path, which was a major misinterpretation on my part.

## Tool Discrepancy (SOLVED, Turn 28952)
- **Problem:** `find_reachable_unseen_tiles` reported (37, 15) as reachable, but `path_and_execute` failed to find a path to it.
- **Conclusion:** `find_reachable_unseen_tiles` had a logic flaw and could not be fully trusted. It likely didn't account for complex barriers like ledges or water that the pathfinder does. This has since been fixed by integrating the robust pathfinding logic from `path_and_execute`.

# Key Items
- BICYCLE: Received from the Goldenrod Bike Shop owner. Allows for faster travel.

## Day-Care Tile Test (SOLVED)
- **System Critique:** Suggested testing 'TABLE' and 'PLANT' tiles.
- **Observation:** Tiles at (2, 4) and (5, 4) have table/plant sprites but are listed as 'FLOOR' in map data.
- **Test 1 (Turn 29321):** Moved from (1, 4) to (2, 4). Result: Move successful. The tile is traversable.
- **Test 2 (Turn 29327):** Moved from (5, 5) to (5, 4). Result: Move successful. The tile is traversable.
- **Conclusion:** Visual sprites do not always indicate impassable terrain. The tile's `type` attribute is the source of truth.

## Day-Care Mystery (Route 34)
- **Initial Observation:** Day-Care Man and Woman mentioned my Unown 'O' and something called 'Glyph' despite me never depositing 'O'.
- **Test 1 (Interaction @ 14, 18):**
  - **Result:** Dialogue appeared: "It's O that was left with the DAY-CARE MAN. It has no interest in Glyph."
- **Test 2 (Interaction @ 17, 19):**
  - **Result:** Dialogue appeared: "It's Glyph that was left with the DAY-CARE LADY. It has no interest in O."
- **Conclusion:** The two Pokémon in the yard, "O" and "Glyph", were left with the Day-Care couple. They do not seem to get along. The game is somehow linking my caught Unown 'O' to the 'O' in the Day-Care, even though I never deposited it. The mystery is ongoing.

# Ecruteak City Notes

## General Info
- Met BILL in the Pokémon Center upon first entry (Turn 29604). He announced the TIME CAPSULE is finished and left for Goldenrod City.
- A man mentioned there are hidden items in the BURNED TOWER, which may be related to finding Morty.

## Ecruteak Gym
- **Leader:** Morty
- **Title:** The Mystic Seer of the Future
- **Likely Type:** Ghost or Psychic

## Key Items
- **ITEMFINDER:** Received from a man in the city. Used to find hidden items.

## Tile Traversal Rules & Tests
- **Traversable:** FLOOR
- **Impassable:** WALL, HEADBUTT_TREE
- **Pokecenter Tests:**
  - `PC` at (9, 1): Confirmed impassable.
  - `COUNTER` at (4, 2): Confirmed impassable.

# Ecruteak Itemfinder House Notes

## Tile Traversal Rules (Initial Observations)
- **Traversable:** FLOOR
- **Impassable:** WALL, POKEDEX

# Dance Theater Notes

## Tile Traversal Rules (Initial Observations)
- **Traversable:** FLOOR
- **Impassable:** WALL
- **Warp:** WARP_CARPET_DOWN

# Dance Theater Notes

## Tile Traversal Rules (Initial Observations)
- **Traversable:** FLOOR
- **Impassable:** WALL
- **Warp:** WARP_CARPET_DOWN
- **One-Way:** LEDGE_HOP_DOWN

# Data Correction (Turn 29763)
- Per overwatch critique, formally documenting that `COUNTER` and `MART_SHELF` tile types are impassable.

## Dance Theater Gentleman (Lesson Learned)
- **Hypothesis:** Defeating all Kimono Girls would cause the Gentleman at (7, 10) to give a reward.
- **Test:** Defeated all five Kimono Girls and repeatedly interacted with the Gentleman between turns 29727 and 29738.
- **Result:** The Gentleman only repeated his initial, pre-defeat dialogue. No new outcome was triggered.
- **Conclusion:** Hypothesis is FALSE. Repeatedly interacting with an NPC that provides no new information is an invalid strategy and will not yield new results. This confirms my general interaction rule: if an NPC doesn't change their dialogue after a significant event, move on.