# Game Mechanics & Systems

## Tile Traversal Rules
- **Impassable:** BOOKSHELF, BUOY (assumed), COUNTER, CUT_TREE, HEADBUTT_TREE, INCENSE_BURNER, MART_SHELF, PC, PILLAR (usually), RADIO, TOWN_MAP, TV, VOID, WALL, WATER, WINDOW.
- **Traversable:** FLOOR, GRASS, LONG_GRASS, TALL_GRASS, UNKNOWN.
- **Warps:** CAVE, DOOR (conditional), LADDER (directional), WARP_CARPET (directional), WARP_CARPET_UP (directional), WARP_CARPET_DOWN (directional, sometimes one-way, may require pressing 'Down' to activate), WARP_CARPET_RIGHT (directional), WARP_CARPET_LEFT (directional).
- **One-Way:** LEDGE_HOP (directional).
- **One-Way (Upward Ledge):** FLOOR_UP_WALL (cannot be moved *down from* this tile, and cannot be moved *down onto* this tile).

## Evolution Methods
- Some POKEMON evolve only by being traded: MACHOKE, KADABRA, HAUNTER, and GRAVELER.

## Respawning Obstacles (CONFIRMED MECHANIC)
- **Initial Observation (Turn 26648):** The `CUT_TREE` at (8, 25) in Ilex Forest, which was previously removed, respawned after re-entering the area.
- **Confirmation (Turn 27669):** The `CUT_TREE` at (13, 5) on Route 31, which was also previously removed, has respawned.
- **Conclusion:** Obstacles cleared with HMs like CUT are not permanently removed. They respawn when re-entering a map. This is a consistent game mechanic and must be factored into all future path planning. My pathfinding tools must always treat `CUT_TREE` tiles as impassable unless I have just cut them in the current session on the map.

## Known Bugs / Strange Mechanics
- **Item Tossing Bug:** Attempting to 'TOSS' a single-stack item (e.g., BERRY x1) from the bag menu fails and resets the menu. Tossing one item from a multi-item stack (e.g., POTION x9 -> x8) also fails to free an inventory slot. The only confirmed way to free a slot is to have a Pokémon 'HOLD' a single-stack item.

## Goldenrod Flower Shop Tile Mechanics
- **WARP_CARPET_DOWN**: Can be a bidirectional warp, unlike the one-way exit previously discovered. This suggests the tile's function can vary by location.

# Active Quests & Notes

## Mail Delivery
- **Status:** On Hold.
- **Task:** Deliver SPEAROW with MAIL to an officer.
- **Attempt 1 (Failed):** An officer in the Route 35 Goldenrod Gate gave the quest.
- **Attempt 2 (Failed):** An officer in the Route 31 Violet Gate was not the recipient. The quest is on hold until the correct NPC is found.

## Goldenrod City - Pokemon Center 2F (Link Club)
- **Observation:** The second floor contains five rooms, each with a warp. All entrances are currently blocked by Link Receptionist NPCs.
- **Clue:** A receptionist at (13, 3) stated, 'the TIME CAPSULE is being adjusted.'
- **Conclusion:** These rooms are the CABLE TRADE CENTER, CABLE CLUB COLOSSEUM, and TIME CAPSULE. All are related to link features and are currently inaccessible as they are blocked by receptionists. This area is a dead end for now.

# Gym Information
- **Goldenrod Gym:** Normal-type. Fighting-type moves are recommended.

# Untested Assumptions & Alternative Hypotheses
- **Assumption:** The strange dialogue from Gramps and Granny ('Your O', 'your Glyph') is related to the Unown I caught.
  - **Alternative Hypothesis:** It could be a default dialogue that triggers if you don't have any Pokémon in the Day-Care, and 'O' or 'Glyph' is just a placeholder or a bug.
  - **Test to Falsify:** The next time I have a free party slot and some money, I will deposit a common Pokémon (like a Pidgey) and then immediately talk to them again. If the dialogue changes to refer to the Pidgey by name, my initial hypothesis is likely correct. If it stays the same, the dialogue is likely just a default script.
- **Assumption:** The only path to Ecruteak City is east through the National Park.
  - **Alternative Hypothesis:** There may be another path, possibly through an unexplored section of Dark Cave or a different exit from Goldenrod City.
  - **Test to Falsify:** After reaching Ecruteak via the main path, I will return to these locations to perform a more thorough search for alternate routes.
- **Assumption:** The Bug-Catching Contest is an optional side quest.
  - **Alternative Hypothesis:** Participation or victory in the contest might be required to unlock the path forward.
  - **Test to Falsify:** If my progress through the National Park is blocked, I will return and attempt to join the contest to see if it triggers a story event.

# Tool Development & Philosophy

## Tool Development Philosophy (Self-Correction)
- **Correction (Turn 28227):** My previous assumptions about my pathfinding tools being faulty were incorrect. The tools were functioning as designed. The errors stemmed from my misinterpretation of the output, incorrect manual pathing attempts, and failure to investigate in-game obstacles. This highlights the critical need to trust my tools and carefully verify my own actions before assuming a tool is broken. I must always trust my tools' outputs first and verify the in-game situation for obstacles before attempting to debug the tool itself. This is a recurring failure in my methodology that I must correct.

## Agent/Tool Ideas
- **`strategic_battle_advisor` (Agent):** A more advanced battle agent that takes into account my entire party, the opponent's known movesets, and suggests not just the best move but also whether to switch Pokémon.
- **`battle_state_parser` (Tool):** A supporting tool for the battle advisor. It would parse raw screen text and game state during a battle and output a structured JSON object with current HP, status, known moves, etc., for both my Pokémon and the opponent.
- **`puzzle_data_compiler` (Agent):** An agent to maintain a structured summary of a complex puzzle's state. I would feed it observations turn-by-turn, and it would compile the data, which could then be used as input for the `puzzle_solver_assistant`.
- **`use_hm` (Tool):** A tool to automate the menu navigation for using an HM move outside of battle. It would take a Pokémon's name and the move name as input and generate the necessary button presses.

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

# Untested Assumptions & Alternative Hypotheses (Updated)
- **Assumption:** The elevator is the only way to move between non-adjacent floors in the Dept. Store.
  - **Alternative Hypothesis:** There might be a hidden staircase or a warp that connects, for example, the 2nd floor directly to the 4th floor, bypassing the 3rd.
  - **Test to Falsify:** After exploring all visible stairs and the elevator, I will systematically walk along every wall on every floor, pressing 'A' to check for hidden passages.
- **Assumption:** All clerks in the Dept. Store are non-essential, providing only flavor text or shop services.
  - **Alternative Hypothesis:** One of the clerks might be a key NPC who gives an item or triggers an event necessary for story progression.
  - **Test to Falsify:** I must speak to every single clerk on every floor to ensure I don't miss any critical dialogue.
## Goldenrod Dept. Store 5F Tile Mechanics
- **WARP_CARPET_LEFT**: Untested, assumed traversable warp.
- **WARP_CARPET_RIGHT**: Untested, assumed traversable warp.
## Goldenrod Magnet Train Station Tile Mechanics
- **FLOOR**: Traversable.
- **WALL**: Impassable.
- **VOID**: Impassable.
- **WARP_CARPET_DOWN**: Traversable warp.