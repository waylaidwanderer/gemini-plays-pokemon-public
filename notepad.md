# Game Mechanics & Systems

## Tile Traversal Rules
- **Impassable:** BOOKSHELF, BUOY (assumed), COUNTER, CUT_TREE, HEADBUTT_TREE, INCENSE_BURNER, MART_SHELF, PC, PILLAR (usually), RADIO, TOWN_MAP, TV, VOID, WALL, WATER, WINDOW.
- **Traversable:** FLOOR, GRASS, LONG_GRASS, TALL_GRASS, UNKNOWN.
- **Warps:** CAVE, DOOR (conditional), LADDER (directional), WARP_CARPET (directional), WARP_CARPET_UP (directional), WARP_CARPET_DOWN (directional, sometimes one-way, may require pressing 'Down' to activate), WARP_CARPET_RIGHT (directional).
- **One-Way:** LEDGE_HOP (directional).
- **One-Way (Upward Ledge):** FLOOR_UP_WALL (cannot be moved *down from* this tile, and cannot be moved *down onto* this tile).

## Evolution Methods
- Some POKEMON evolve only by being traded: MACHOKE, KADABRA, HAUNTER, and GRAVELER.

## Tool Mechanics
- **`stun_npc` Tool:** This tool can only affect NPCs that are currently visible on the screen ("live objects"). Attempting to use it on an off-screen NPC will result in an error.

---

# Appendix: Core Lessons & Puzzles

## Cut Mechanic (CRITICAL DISCOVERY)
- The `CUT_TREE` tile is an interactable obstacle. To pass, one must face it from an adjacent tile and press 'A' to trigger the prompt to use the move CUT. After using CUT, the tile becomes a standard FLOOR tile, and the path is permanently cleared.

## Ilex Forest Puzzle
- The correct solution involved a multi-stage chase, herding the Farfetch'd through the forest by interacting with it from specific directions and using twig piles to alter its path, ultimately leading it to its owner's apprentice.

## HEADBUTT_TREE Mechanics Test
- **Observation:** The `HEADBUTT_TREE` tile type is impassable.
- **Hypothesis 1 (Turn 24065):** The `HEADBUTT_TREE` is an interactable object that responds to the 'A' button.
- **Test:** Stood at (25, 4), faced down, and pressed 'A' on the tree at (25, 5).
- **Result:** No text appeared, and no action occurred.
- **Conclusion:** Hypothesis 1 is FALSE. The tree does not respond to a standard 'A' button interaction. It is likely that the move 'Headbutt' is required to interact with these trees. For now, they are impassable obstacles.

## Goldenrod Dept. Store B1F Puzzle
- **Conclusion:** The puzzle was solved by repeatedly using the elevator to leave and re-enter the basement, which triggered box movements. A final interaction with the Machop completed the sequence, although a visual bug left impassable collision where the boxes used to be.

## Day-Care & Unown
- The Day-Care Lady on Route 34 mentioned my 'Glyph' has 'grown a lot'. This dialogue triggered even without an Unown in my party, suggesting it's tied to the Pokedex entry for Unown. She seems connected to the Ruins of Alph mystery.

## Route 34 - Day-Care Yard
- A hidden SUPER POTION at (17, 19) is currently blocked by a Pokémon sprite and is unobtainable. Repeated 'A' presses only re-trigger the Pokémon's dialogue.

## Untested Assumptions & Alternative Hypotheses
- **Goldenrod Dept. Store B1F Puzzle:**
  - **Assumption:** The puzzle is bugged or unsolvable, as the box collision remains after they visually disappear.
  - **Alternative Hypothesis:** There is a different, undiscovered trigger for the final phase of the puzzle. The visual change was a clue. The trigger might involve talking to another NPC, having a specific item/Pokémon, or an event outside the basement.
  - **Test to Falsify:** After exhausting other objectives in Goldenrod, I will return to the Dept. Store and systematically test new potential triggers.

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
- **TALL_GRASS**: Traversable, triggers wild encounters. Verified in National Park.

## Tool Development Philosophy (Self-Correction)
- **Problem:** My `path_and_execute` tool has failed repeatedly, causing movement blockages and wasted turns. My approach of fixing bugs reactively is inefficient.
- **Solution:** I must adopt a proactive, test-driven approach to tool development.
- **New Principle:** Before relying on a complex tool for a critical task, I must first build and use diagnostic tools to verify its core logic. For pathfinding, this means creating a tool to visualize the algorithm's understanding of the map (`find_all_reachable_tiles`). This will allow me to identify and fix logical errors in a controlled way, rather than discovering them through trial-and-error during gameplay.
- **Correction (Turn 26941):** My previous diagnoses of `find_path_to_nearest_unseen` and `path_and_execute` being faulty were incorrect. The tools were functioning as designed. The errors stemmed from my misinterpretation of the output and incorrect manual pathing attempts. This highlights the critical need to trust my tools and carefully verify my own actions before assuming a tool is broken.

## Route 36 Tile Mechanics
- **FLOOR**: Traversable. Verified on Route 36.
- **WALL**: Impassable. Verified on Route 36.
- **HEADBUTT_TREE**: Impassable. Verified on Route 36.
- **TALL_GRASS**: Traversable, triggers wild encounters. Verified on Route 36.

## WEIRD_TREE Puzzle (Route 36)
- **Observation:** The WEIRD_TREE at (35, 9) is blocking the path.
- **Hypothesis 1 (Turn 26588):** The tree is a standard interactable object that responds to the 'A' button.
- **Test:** Stood at (36, 9), faced the tree, and pressed 'A'.
- **Result:** No text appeared, and no action occurred.
- **Conclusion:** Hypothesis 1 is FALSE.
- **Hypothesis 2:** The tree requires a key item to interact with. Based on a hint from an NPC in the Goldenrod Flower Shop (who mentioned a gift after beating the Gym Leader), the SQUIRT BOTTLE is the likely key item.
- **Plan:** Return to Goldenrod City, locate the Flower Shop, obtain the SQUIRT BOTTLE, and return to test this hypothesis.

## Respawning Obstacles (CRITICAL DISCOVERY)
- **Observation (Turn 26648):** The `CUT_TREE` at (8, 25) in Ilex Forest, which was previously removed to solve the Farfetch'd puzzle, has respawned.
- **Conclusion:** Obstacles cleared with HMs like CUT are not permanently removed and may reappear after leaving and re-entering an area. This must be considered for all future path planning.

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

## Route 36 National Park Gate Tile Mechanics
- **FLOOR**: Traversable. Verified in the gatehouse.
- **COUNTER**: Impassable. Verified in the gatehouse.

# Blocked Quests
- **Mail Delivery:** The Officer in the Route 35 Goldenrod Gate is currently unreachable due to the counter layout. The quest is on hold.