# Gem's Pokémon Crystal Adventure Log

# I. Core Directives & Lessons Learned
*   **Proactive Data Management:** Record all new information immediately. If a task can be done now, do it now. Never defer.
*   **Trust Your Tools:** Trust verified tools. If a tool reports no path, the area is unreachable.
*   **Mark Warps Immediately:** Mark both warp entrance and exit immediately upon use.
*   **Avoid Repetitive Failures:** Document and pivot from failing strategies.
*   **Verify Location:** Always verify map and coordinates before navigating.
*   **Link NPC Markers:** Link all NPC markers to their `object_id`.
*   **Fix Tools Immediately:** Fixing a broken tool or agent is the highest priority.
*   **Apply Learned Lessons:** Consistently review and apply documented strategies, especially for navigation, to avoid repeating mistakes.
*   **Utilize Created Tools:** Actively use custom agents and tools once they have been created for their intended purpose.

## B. Tile Traversal Rules
*   **Traversable:** TALL_GRASS, LONG_GRASS, DOOR, WARP_CARPET_DOWN, LADDER, FLOOR.
*   **Impassable (Verified):** WALL, WINDOW, CUT_TREE, SIGN, BOOKSHELF, BLACKBOARD, MART_SHELF, BUOY, TV, TOWN_MAP, BIRD, HEADBUTT_TREE, FRUIT_TREE, COMPUTER, PRINTER, VOID, WATER, CAVE.
*   **Special Interaction (Impassable but Interactable):**
    *   **PC:** Impassable. Interact by standing below it at (X, Y+1), facing up, and pressing 'A'.
    *   **COUNTER:** Impassable. Interact with NPCs behind it by standing in front of the counter and pressing 'A'.
*   **One-Way Traversal:**
    *   LEDGE_HOP_DOWN: Can only be entered from above.
    *   LEDGE_HOP_RIGHT: Can only be entered from the left.
    *   LEDGE_HOP_LEFT: Can only be entered from the right.
*   **Special Interaction (Warp):**
    *   **CAVE:** Can act as a one-way warp. The tile at Route 33 (11, 9) is a confirmed one-way entrance to Union Cave (17, 31). The tile at Route 32 (6, 79) is a confirmed one-way entrance to Union Cave (17, 3). Should be treated as impassable for pathfinding.
    *   **WARP_CARPET_RIGHT:** Requires being on the tile, facing the direction of the warp, and then pressing the directional button again.
    *   **WARP_CARPET_LEFT:** Requires being on the tile, facing the direction of the warp, and then pressing the directional button again.
*   **Special Interaction (Weird Walls):**
    *   **FLOOR_UP_WALL:** A special one-way tile. **Verified Rule:** Can only be traversed by moving UP onto it from a tile below (Y+1 -> Y). It is impassable from all other directions (above, left, right, and when trying to move down onto it). Verified at SlowpokeWellB1F (9,3)->(9,2).
*   **Special Interaction (Fishing):**
    *   **WATER:** Impassable to walk on, but can be fished in with a rod.
*   **CUT_08 (Untested):** A variant of a cuttable tree.
*   **CUT_28_GARBAGE (Untested):** A variant of a cuttable tree.
*   **RADIO (Untested):** A radio, likely impassable.
*   **INCENSE_BURNER (Untested):** An incense burner, likely impassable.
*   **VOID (Verified):** Impassable. Appears to be a visual boundary marker.
*   **WARP_CARPET_LEFT (Verified):** Requires being on the tile, facing the direction of the warp, and then pressing the directional button again.

# II. Battle Information

## A. Verified Type Matchups
*   Ghost has NO EFFECT on Normal.
*   Normal has NO EFFECT on Ghost.
*   Unown's Hidden Power (type unknown) can be super-effective against Fire.

## B. Trainer Rosters
*   **Falkner (Violet City):** Pidgey (Lv7), Pidgeotto (Lv9).
*   **Bugsy (Azalea Town):** Metapod (Lv14), Kakuna (Lv14), Scyther (Lv16).
*   **Fisher Justin (Route 32):** Magikarp (Lv5), Magikarp (Lv5), Magikarp (Lv15), Magikarp (Lv5).

# III. Story & Quests
*   **Current Quest:** Solve the Ruins of Alph puzzles.
*   **NPC Hints & Lore:**
    *   Fisher (Union Cave, 14, 19): Strange roars on weekends.
    *   WADE (Route 31): Will share BERRIES.
    *   Hiker Anthony (Phone): Tons of DUNSPARCE in DARK CAVE.

# V. Puzzle Logs

## A. Ilex Forest Farfetch'd Puzzle
*   **Objective:** Herd two Farfetch'd to the apprentice at (7, 28) for HM01 Cut.
*   **Mechanic Hypothesis:** The Farfetch'd moves based on player position, not facing direction, and requires a clear, unobstructed tile to flee to.
*   **Status:** One Farfetch'd has been herded. The second Farfetch'd is currently at (15, 25).
*   **Tool Reminder:** A custom tool is needed to solve this puzzle systematically.

# XIV. Battle Mechanics (Newly Observed)
*   **Wrap:** Traps the target for several turns, preventing them from switching or fleeing.

# VI. Navigational Failures Log
*   **Ilex Forest (Turns 16451-16475):** Got stuck in the southwest dead-end area. Repeatedly tried to path north and east into walls.
    *   Blocked at (3, 39) when trying to move up from (3, 40).
    *   Blocked at (2, 34) when trying to move right from (1, 34).
    *   Blocked at (1, 39) when trying to move up from (1, 40).
    *   Blocked at (1, 32) by a HEADBUTT_TREE when trying to move up from (1, 33).
*   **Azalea Town (Turns ~17015-17049):** Became stuck in the eastern section of town for over 30 turns due to repeated, careless pathing errors.
    *   **Core Misunderstanding:** Failed to recognize that the eastern and western sections are separated by impassable walls and one-way ledges, requiring a long, looping path to navigate between them.
    *   **Failed Path West:** Repeatedly attempted to move west from (28, 13) into the wall at (27, 13).
    *   **Failed Path North:** Repeatedly attempted to move north from (28, 12) into the one-way ledge at (28, 11).
    *   **Conclusion:** This entire loop was caused by a failure to immediately document impassable tiles and a flawed assumption that a direct route existed. The correct path requires looping around the central buildings.
*   **Slowpoke Well B1F (Turns ~17074-17171):** Suffered a catastrophic navigation failure for approximately 100 turns. The core issue was a severe case of confirmation bias, where I incorrectly assumed the path west had to be through the northern corridors. This led to a repetitive loop of trying the same failed paths.
    *   **Failed Hypotheses:**
        1.  The path is north (failed repeatedly).
        2.  The path is south via a one-way ledge (failed, `FLOOR_UP_WALL` is impassable from above).
    *   **Root Cause:** Failure to systematically explore all possible routes, failure to immediately log dead ends with map markers, and a lack of goal flexibility. I should have pivoted to another objective much sooner instead of getting stuck.
    *   **Lesson Learned:** Trust the `exploration_strategist` agent's high-level guidance, but verify the path manually and systematically. Do not get locked into a single hypothesis. Be willing to abandon a failing approach and pivot to a new goal.

# VI. Strategic Pivots

## A. Ilex Forest Navigation (Turn 16503)
*   **Problem:** After 50+ turns of failed attempts, I have concluded that the main puzzle area of Ilex Forest is unreachable from the southern entrance (Azalea Town side).
*   **Old Strategy (Failed):** Repeatedly try to find a path north from the entrance at (3, 42).
*   **New Strategy:** Abandon the southern approach. Exit the forest and travel to Route 34 to find the northern entrance to Ilex Forest.

# VII. Gameplay Reflections
* **Puzzle Solving:** Must use a hypothesis-driven approach (Observe, Hypothesize, Test, Conclude) for puzzles instead of brute-force navigation. Document all attempts in the puzzle log.

# VIII. New Hypotheses & Mechanics (Post-Reflection)
*   **Tile Mechanic (VOID):** Added to impassable list. Appears to be a visual boundary marker.
*   **Cut Quest Hypothesis:** If the Farfetch'd puzzle fails to yield HM01, the alternative hypothesis is that the Ilex Forest Shrine at (8, 22) is involved. The next step would be to investigate the shrine.

# XI. Core Principles (Post-Reflection Updates)
*   **Goal Flexibility:** If progress on a primary goal stalls for a significant period (e.g., 50+ turns) despite trying multiple documented hypotheses, I MUST pivot to a different primary or secondary goal. Do not remain stuck on a single objective indefinitely.
*   **Proactive Tile Testing:** Upon encountering any new, undocumented tile type, I MUST immediately form a hypothesis about its traversability and conduct a simple test (e.g., trying to walk on it from all four directions). The results MUST be logged in the notepad before proceeding with any other actions.

# V. System Diagnostics Log
*   **Python Sandbox Failure (Turn 17224):** Confirmed that the Python sandbox container is not running. The `pathfinder` tool failed to execute. This contradicts previous assumptions and is now the highest priority issue to resolve.