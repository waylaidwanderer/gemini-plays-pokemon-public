# Gem's Pokémon Crystal Adventure Log

# I. Core Principles & Lessons Learned
*   **Trust Your Tools:** A verified tool's output (e.g., `path_finder`, `reachability_analyzer`) is a source of truth. Trust it over assumptions. A 'No path found' result is data, not a bug.
*   **Systematic Debugging:** Use a methodical, evidence-based approach for broken tools. Use `run_code` with print statements to trace execution. Isolate variables and test simple cases first.
*   **Immediate Action:** Tool/agent maintenance is not a deferrable goal. It must be performed in the current turn.
*   **Hypothesis-Driven Testing:** For all new mechanics, use the Observe, Hypothesize, Test, Conclude method. Document every step.
*   **Goal Flexibility:** If progress on a primary goal stalls for a significant period (e.g., 50+ turns), pivot to a different goal. Do not remain stuck.
*   **Proactive Tile Testing:** Upon encountering any new, undocumented tile type, I MUST immediately form a hypothesis, test it, and log the results before proceeding.
*   **Mark Warps Immediately:** Mark both warp entrance and exit immediately upon use.
*   **UI Unreliability:** The `TYPE/` display in battle can be incorrect (e.g., showing EKANS as Normal). Trust observed effectiveness messages over the UI.

# II. Tile Traversal Rules
*   **Traversable:** TALL_GRASS, LONG_GRASS, DOOR, WARP_CARPET_DOWN, WARP_CARPET_RIGHT, LADDER, FLOOR.
*   **Impassable (Verified):** WALL, WINDOW, CUT_TREE, SIGN, BOOKSHELF, BLACKBOARD, MART_SHELF, BUOY, TV, TOWN_MAP, BIRD, HEADBUTT_TREE, FRUIT_TREE, COMPUTER, PRINTER, VOID, WATER, CAVE, COUNTER.
*   **Untested:** CUT_08, CUT_28_GARBAGE, RADIO, INCENSE_BURNER.
*   **One-Way Traversal:**
    *   LEDGE_HOP_DOWN: Can only be entered from above.
    *   LEDGE_HOP_RIGHT: Can only be entered from the left.
    *   LEDGE_HOP_LEFT: Can only be entered from the right.
*   **Special Interaction (Warp):**
    *   **CAVE:** Can act as a one-way warp. Route 33 (11, 9) -> Union Cave (17, 31). Route 32 (6, 79) -> Union Cave (17, 3).
    *   **WARP_CARPET:** Activated by pressing the directional button of the warp (Left/Right/Down) while standing on the tile.
*   **Special Interaction (Walls/Floors):**
    *   **FLOOR_UP_WALL:** A one-way slide. Movement *from* this tile is only possible Down. Movement *onto* this tile is only possible by moving UP from a tile below (Y+1 -> Y).
    *   **Visual Ledges (FLOOR type):** Some FLOOR tiles are visually one-way ledges and are impassable from below. Verified at UnionCave1F, preventing movement from (7, 26) up to (7, 25).
*   **Special Interaction (Interactable):**
    *   **PC:** Interact by standing below it at (X, Y+1), facing up.
    *   **COUNTER:** Interact with NPCs behind it by standing in front of the counter.
    *   **WATER:** Can be fished in with a rod.

# III. Battle Information
## A. Verified Type Matchups
*   Ghost has NO EFFECT on Normal.
*   Normal has NO EFFECT on Ghost.
*   Grass is NOT VERY EFFECTIVE against Fire.
*   Unown's Hidden Power can be super-effective against Fire.
## B. Trainer Rosters
*   **Falkner (Violet City):** Pidgey (Lv7), Pidgeotto (Lv9).
*   **Bugsy (Azalea Town):** Metapod (Lv14), Kakuna (Lv14), Scyther (Lv16).
*   **Fisher Justin (Route 32):** Magikarp x4.
## C. Battle Mechanics
*   **Wrap:** Traps the target for several turns, preventing them from switching or fleeing.

# IV. Story & Quests
*   **Primary Quest: Obtain HM01 Cut**
    *   **Objective:** Receive HM01 Cut from the apprentice in Ilex Forest.
    *   **Current Plan:** Systematically search the western section of the forest for the second Farfetch'd. The eastern section has been confirmed as unreachable from the current area.
*   **Secondary Quest: Complete Sprout Tower**
    *   **Objective:** Reach the top of Sprout Tower and defeat the Elder.
    *   **Status:** Blocked. Need to find the correct path up the western ladder system.
*   **Tertiary Quest: Investigate Union Cave Roars**
    *   **Objective:** Discover the source of the strange roars heard in Union Cave on Fridays.
    *   **Status:** Blocked. Requires it to be Friday.
*   **NPC Hints & Lore:**
    *   WADE (Route 31): Will share BERRIES.
    *   Hiker Anthony (Phone): Tons of DUNSPARCE in DARK CAVE.

# V. Puzzle Logs & Navigational Failures
## A. Ilex Forest Farfetch'd Puzzle
*   **Objective:** Herd the Farfetch'd to the apprentice at (7, 28) to receive HM01 Cut.
*   **History & Learnings:** Created `farfetchd_solver` tool based on a simple herding hypothesis. The tool's 'No path found' output invalidated the initial hypothesis, correctly proving the puzzle is more complex.

## B. Union Cave Navigation
*   **History & Learnings:** Wasted ~65 turns assuming `path_finder` was broken instead of trusting its 'No path found' output, which correctly identified that the southern and northern sections of UnionCave1F are separated by water.

## C. General Navigation Failures
*   **Ilex Forest (Turns 16451-16475):** Stuck in a dead-end due to brute-force navigation instead of systematic exploration.
*   **Azalea Town (Turns ~17015-17049):** Wasted 30+ turns due to failing to recognize one-way ledges and impassable walls.
*   **Slowpoke Well B1F (Turns ~17074-17171):** Suffered a ~100 turn navigation failure due to confirmation bias, repeatedly trying a path that was proven impassable.
*   **Route 33 (Turn 17878):** Confirmed via `path_finder` that the path west to Azalea Town from the Union Cave exit is IMPOSSIBLE due to impassable ledges.
*   **Union Cave B1F (via ladder at 1F (5, 19)):** Confirmed via `path_finder` that this ladder leads to a small, isolated platform and is a dead end.
*   **Route 32 (Turns ~18059-18060):** Wasted several turns trying to path south to Union Cave entrance (6, 79), forgetting my own documented discovery that the route contains one-way ledges.