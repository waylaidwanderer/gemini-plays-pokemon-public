# Game Mechanics & Systems

## Tile Traversal Rules
- **Impassable:** BOOKSHELF, BUOY (assumed), COUNTER, CUT_TREE, HEADBUTT_TREE, INCENSE_BURNER, MART_SHELF, PC, PILLAR (usually), RADIO, TOWN_MAP, TV, VOID, WALL, WATER, WINDOW.
- **Traversable:** FLOOR, GRASS, LONG_GRASS, TALL_GRASS, UNKNOWN.
- **Warps:** CAVE, DOOR (conditional), LADDER (directional), WARP_CARPET (directional), WARP_CARPET_UP (directional), WARP_CARPET_DOWN (directional, sometimes one-way, may require pressing 'Down' to activate), WARP_CARPET_RIGHT (directional), WARP_CARPET_LEFT (directional).
- **One-Way:** LEDGE_HOP (directional).
- **One-Way (Upward Ledge):** FLOOR_UP_WALL (cannot be moved *down from* this tile, and cannot be moved *down onto* this tile).

## Evolution Methods
- Some POKEMON evolve only by being traded: MACHOKE, KADABRA, HAUNTER, and GRAVELER.

## Tool Mechanics
- **`stun_npc` Tool:** This tool can only affect NPCs that are currently visible on the screen ("live objects"). Attempting to use it on an off-screen NPC will result in an error.

---

# Appendix: Core Lessons & Puzzles

## HEADBUTT_TREE Mechanics Test
- **Observation:** The `HEADBUTT_TREE` tile type is impassable.
- **Hypothesis 1 (Turn 24065):** The `HEADBUTT_TREE` is an interactable object that responds to the 'A' button.
- **Test:** Stood at (25, 4), faced down, and pressed 'A' on the tree at (25, 5).
- **Result:** No text appeared, and no action occurred.
- **Conclusion:** Hypothesis 1 is FALSE. The tree does not respond to a standard 'A' button interaction. It is likely that the move 'Headbutt' is required to interact with these trees. For now, they are impassable obstacles.

## Day-Care & Unown
- The Day-Care Lady on Route 34 mentioned my 'Glyph' has 'grown a lot'. This dialogue triggered even without an Unown in my party, suggesting it's tied to the Pokedex entry for Unown. She seems connected to the Ruins of Alph mystery.

## Route 34 - Day-Care Yard
- A hidden SUPER POTION at (17, 19) is currently blocked by a Pokémon sprite and is unobtainable. Repeated 'A' presses only re-trigger the Pokémon's dialogue.

## Goldenrod City - Pokemon Center 2F (Link Club)
- **Observation:** The second floor contains five rooms, each with a warp. All entrances are currently blocked by Link Receptionist NPCs.
- **Clue:** A receptionist at (13, 3) stated, 'the TIME CAPSULE is being adjusted.'
- **Conclusion:** These rooms are related to the 'Time Capsule' feature and are inaccessible at this time. I have investigated them as much as is currently possible.

## Goldenrod City Tile Mechanics
- **FLOOR**: Traversable. Verified in Goldenrod City.
- **WALL**: Impassable. Verified in Goldenrod City.
- **WATER**: Impassable. Verified in Goldenrod City.
- **VOID**: Impassable. Verified in Goldenrod Gym.
- **DOOR**: Traversable warp. Verified in Goldenrod City.
- **WARP_CARPET_DOWN (One-Way Exit):** A specific instance of this tile at (5, 29) on map 3_54 was found to be a one-way exit, returning the player to the previous map. This suggests some warp carpets may not be bidirectional.
- **WARP_CARPET_RIGHT**: Traversable warp. Activated by pressing Right.

# Gym Information
- **Goldenrod Gym:** Normal-type. Fighting-type moves are recommended.

## Side Quests
- GINA on Route 34 has an item for me.
- Snubbull is a Normal-type Pokémon.

## Tool Development Philosophy (Self-Correction)
- **Problem:** My `path_and_execute` tool has failed repeatedly, causing movement blockages and wasted turns. My approach of fixing bugs reactively is inefficient.
- **Solution:** I must adopt a proactive, test-driven approach to tool development.
- **New Principle:** Before relying on a complex tool for a critical task, I must first build and use diagnostic tools to verify its core logic. For pathfinding, this means creating a tool to visualize the algorithm's understanding of the map (`find_all_reachable_tiles`). This will allow me to identify and fix logical errors in a controlled way, rather than discovering them through trial-and-error during gameplay.
- **Correction (Turn 26941):** My previous diagnoses of `find_path_to_nearest_unseen` and `path_and_execute` being faulty were incorrect. The tools were functioning as designed. The errors stemmed from my misinterpretation of the output and incorrect manual pathing attempts. This highlights the critical need to trust my tools and carefully verify my own actions before assuming a tool is broken.

## Respawning Obstacles (CONFIRMED MECHANIC)
- **Initial Observation (Turn 26648):** The `CUT_TREE` at (8, 25) in Ilex Forest, which was previously removed, respawned after re-entering the area.
- **Confirmation (Turn 27669):** The `CUT_TREE` at (13, 5) on Route 31, which was also previously removed, has respawned.
- **Conclusion:** Obstacles cleared with HMs like CUT are not permanently removed. They respawn when re-entering a map. This is a consistent game mechanic and must be factored into all future path planning. My pathfinding tools must always treat `CUT_TREE` tiles as impassable unless I have just cut them in the current session on the map.

## Goldenrod Flower Shop Tile Mechanics
- **WARP_CARPET_DOWN**: Can be a bidirectional warp, unlike the one-way exit previously discovered. This suggests the tile's function can vary by location.

## Known Bugs / Strange Mechanics
- **Item Tossing Bug:** Attempting to 'TOSS' a single-stack item (e.g., BERRY x1) from the bag menu fails and resets the menu. Tossing one item from a multi-item stack (e.g., POTION x9 -> x8) also fails to free an inventory slot. The only confirmed way to free a slot is to have a Pokémon 'HOLD' a single-stack item.

## SQUIRT BOTTLE Quest & WEIRD_TREE Puzzle (SOLVED)
- **Objective:** Clear the WEIRD_TREE on Route 36.
- **Solution:**
  1. Defeat Gym Leader Whitney in Goldenrod Gym.
  2. Speak to the Lass at (9, 6) in the Gym. This prompts Whitney to give you the Plain Badge and TM45.
  3. Go to the Goldenrod Flower Shop. The woman at (2, 3) will give you the SQUIRT BOTTLE.
  4. Travel to Route 36 and use the SQUIRT BOTTLE on the WEIRD_TREE at (35, 9).
  5. The tree reveals itself as a Sudowoodo. After the encounter, the path is clear.
  6. An NPC at (36, 9) will then give you TM08 (Rock Smash).

## Route 35 Tile Mechanics
- **FLOOR**: Traversable. Verified on Route 35.
- **WALL**: Impassable. Verified on Route 35.
- **TALL_GRASS**: Traversable, triggers wild encounters. Verified on Route 35.
- **HEADBUTT_TREE**: Impassable. Verified on Route 35.
- **WATER**: Impassable. Verified on Route 35.
- **DOOR**: Traversable warp. Verified on Route 35.
- **WARP_CARPET_DOWN**: Traversable warp. Verified on Route 35.

## National Park Tile Mechanics
- **FLOOR**: Traversable. Verified in National Park.
- **WALL**: Impassable. Verified in National Park.
- **TALL_GRASS**: Traversable, triggers wild encounters. Verified in National Park.
- **LONG_GRASS**: Traversable, triggers wild encounters. Verified in National Park.
- **WARP_CARPET_DOWN**: Traversable warp. Verified in National Park.
- **WARP_CARPET_RIGHT**: Traversable warp. Activated by pressing Right. Verified in National Park.

# Blocked Quests
- **Mail Delivery:** An attempt to deliver the mail to an officer in the Route 31 Violet Gate failed; he was not the recipient. The quest is on hold until the correct NPC is found.

## Violet City Tile Mechanics
- **FLOOR**: Traversable. Verified in Violet City.
- **WALL**: Impassable. Verified in Violet City.
- **WATER**: Impassable. Verified in Violet City.
- **DOOR**: Traversable warp. Verified in Violet City.
- **HEADBUTT_TREE**: Impassable. Verified in Violet City.
- **CUT_TREE**: Impassable (respawns). Verified in Violet City.
- **LEDGE_HOP_DOWN**: One-way traversal. Verified in Violet City.
- **WARP_CARPET_RIGHT**: Traversable warp. Activated by pressing Right. Verified in Violet City.

## Untested Assumptions & Alternative Hypotheses (Post-Reflection)
- **Assumption:** The only path to Ecruteak City is east through the National Park.
  - **Alternative Hypothesis:** There may be another path, possibly through an unexplored section of Dark Cave or a different exit from Goldenrod City.
  - **Test to Falsify:** After reaching Ecruteak via the main path, I will return to these locations to perform a more thorough search for alternate routes.
- **Assumption:** The Bug-Catching Contest is an optional side quest.
  - **Alternative Hypothesis:** Participation or victory in the contest might be required to unlock the path forward.
  - **Test to Falsify:** If my progress through the National Park is blocked, I will return and attempt to join the contest to see if it triggers a story event.

## Route 36 Tile Mechanics
- **FLOOR**: Traversable. Verified on Route 36.
- **WALL**: Impassable. Verified on Route 36.
- **HEADBUTT_TREE**: Impassable. Verified on Route 36.
- **TALL_GRASS**: Traversable, triggers wild encounters. Verified on Route 36.
- **WARP_CARPET_LEFT**: Traversable warp. Activated by pressing Left.
- **WARP_CARPET_DOWN**: Traversable warp. Verified on Route 36 at Ruins of Alph entrance.
- **DOOR**: Present at (47, 17), function unverified.
- **FLOOR_UP_WALL**: Present from (51, 16) to (53, 16), likely one-way ledges.

## Tool Development Notes (Self-Critique)
- **Critique on Hardcoded Menu Navigation:** Relying on a hardcoded sequence of button presses for menu navigation is extremely brittle and prone to failure if the menu state is not exactly as predicted. This design is inefficient. **Action:** Perform menu navigation manually until a more robust, screen-aware solution can be developed.

## Future Tool/Agent Ideas
- **Inventory Management Agent:** An agent that takes the current bag state and a goal (e.g., 'free up 1 slot') and outputs a concrete plan (e.g., 'Give BITTER BERRY to Aether').
- **Screen-Aware Menu Navigator:** A long-term project to create a tool that can read the screen to navigate menus dynamically, avoiding the brittleness of hardcoded button sequences.
## SQUIRT BOTTLE Investigation
- **Problem:** The SQUIRT BOTTLE is missing from my bag.
- **Hypothesis 1:** The Teacher NPC in the Goldenrod Flower Shop will provide a replacement. **Result: FALSE.**
- **Hypothesis 2:** The Lass NPC in the Goldenrod Flower Shop will provide a replacement or clue. **Result: FALSE.**
- **Hypothesis 3:** Whitney in the Goldenrod Gym will provide a replacement or clue. **Result: FALSE.**
- **Hypothesis 4:** One of my party Pokémon is holding the item. **Result: FALSE (Ignis was holding a BERRY).**
- **Hypothesis 5:** The item is in the PC's Item Storage. **Result: FALSE.**
- **Hypothesis 6:** A Pokémon in the PC is holding the item. **Result: FALSE.**
- **Current Hypothesis:** My bag was full during the initial conversation with the Flower Shop lady.
- **Next Step:** Return to the Goldenrod Flower Shop to test this.

## National Park Tile Mechanics
- **FLOOR**: Traversable. Verified in National Park.
- **WALL**: Impassable. Verified in National Park.
- **TALL_GRASS**: Traversable, triggers wild encounters. Verified in National Park.
- **LONG_GRASS**: Traversable, triggers wild encounters. Verified in National Park.
- **WARP_CARPET_RIGHT**: Traversable warp. Activated by pressing Right. Verified in National Park.

## Route 36 National Park Gate Tile Mechanics
- **FLOOR**: Traversable. Verified in Route 36 National Park Gate.
- **WALL**: Impassable. Verified in Route 36 National Park Gate.
- **COUNTER**: Impassable. Verified in Route 36 National Park Gate.
- **PC**: Impassable. Verified in Route 36 National Park Gate.
- **WARP_CARPET_LEFT**: Traversable warp. Activated by pressing Left. Verified in Route 36 National Park Gate.
- **WARP_CARPET_RIGHT**: Traversable warp. Activated by pressing Right. Verified in Route 36 National Park Gate.

---

# Appendix: Solved Puzzles & Lessons Learned