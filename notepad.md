# Gem's Pokémon Crystal Adventure Log

# I. Core Principles & Lessons Learned
*   **Trust Your Tools:** A verified tool's output (e.g., 'No path found') is a source of truth. Trust it over your own assumptions about map connectivity.
*   **Systematic Debugging:** When a tool is broken, use a methodical, evidence-based approach. Use `run_code` with print statements to trace execution. Isolate variables and test simple cases before complex ones.
*   **Immediate Action:** Tool/agent maintenance is not a deferrable goal. It must be performed in the current turn.
*   **Hypothesis-Driven Testing:** For all new mechanics, use the Observe, Hypothesize, Test, Conclude method. Document every step in the relevant log.
*   **Goal Flexibility:** If progress on a primary goal stalls for a significant period (e.g., 50+ turns) despite trying multiple documented hypotheses, I MUST pivot to a different primary or secondary goal. Do not remain stuck on a single objective indefinitely.
*   **Proactive Tile Testing:** Upon encountering any new, undocumented tile type, I MUST immediately form a hypothesis about its traversability and conduct a simple test (e.g., trying to walk on it from all four directions). The results MUST be logged in the notepad before proceeding.
*   **Mark Warps Immediately:** Mark both warp entrance and exit immediately upon use.

# II. Tile Traversal Rules
*   **Traversable:** TALL_GRASS, LONG_GRASS, DOOR, WARP_CARPET_DOWN, LADDER, FLOOR.
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
*   Unown's Hidden Power can be super-effective against Fire.
## B. Trainer Rosters
*   **Falkner (Violet City):** Pidgey (Lv7), Pidgeotto (Lv9).
*   **Bugsy (Azalea Town):** Metapod (Lv14), Kakuna (Lv14), Scyther (Lv16).
*   **Fisher Justin (Route 32):** Magikarp x4.
## C. Battle Mechanics
*   **Wrap:** Traps the target for several turns, preventing them from switching or fleeing.

# IV. Story & Quests
*   **Current Quest:** Solve the Ruins of Alph puzzles.
*   **NPC Hints & Lore:**
    *   Fisher (Union Cave, 14, 19): Strange roars on weekends.
    *   WADE (Route 31): Will share BERRIES.
    *   Hiker Anthony (Phone): Tons of DUNSPARCE in DARK CAVE.

# V. Puzzle Logs

## A. Ilex Forest Farfetch'd Puzzle
*   **Objective:** Herd the Farfetch'd to the apprentice at (7, 28) to receive HM01 Cut.
*   **History & Learnings:**
    1.  **Hypothesis 1 (Simple Herding):** Assumed a simple push mechanic. Created `farfetchd_solver` tool.
    2.  **Test 1:** Tool reported 'No path found'.
    3.  **Conclusion 1:** My hypothesis of a direct herding path was invalidated. The tool was correct; my assumption was wrong.
*   **Current Strategy:** Systematically test different starting positions for the Farfetch'd, using the solver to check for a valid path after each manual repositioning.

## B. Union Cave Navigation
*   **Objective:** Pathfind to Hiker Daniel at (4, 6).
*   **History & Learnings:**
    1.  **Hypothesis 1 (Broken Tool):** Assumed `path_finder` was bugged after it repeatedly failed to find a path.
    2.  **Test 1:** Diagnostic trace revealed the algorithm was working perfectly.
    3.  **Conclusion 1:** The tool was correct. No land path exists between the southern and northern sections of UnionCave1F; they are separated by water.
    4.  **Lesson Learned:** Trust tool outputs over intuition. A 'No path found' result is data, not a bug.

# VI. Navigational & Cognitive Failures Log
*   **Ilex Forest (Turns 16451-16475):** Stuck in a dead-end due to brute-force navigation instead of systematic exploration.
*   **Azalea Town (Turns ~17015-17049):** Wasted 30+ turns due to failing to recognize one-way ledges and impassable walls, indicating poor map analysis.
*   **Slowpoke Well B1F (Turns ~17074-17171):** Suffered a ~100 turn navigation failure due to confirmation bias, repeatedly trying a path that was proven impassable.
*   **Union Cave Navigation (Turns ~17812-17877):** Wasted ~65 turns assuming a tool was broken instead of trusting its 'No path found' output, which correctly identified a water-separated area. **Lesson:** Trust the tools.
*   **Route 33 (Turn 17878):** Confirmed via `path_finder` that the path west to Azalea Town from the Union Cave exit is IMPOSSIBLE. The route is a one-way trap due to impassable ledges. The only way to proceed is to re-enter Union Cave at (11, 9). This is a critical lesson in trusting my tools over visual assessment.
*   **Union Cave B1F (via ladder at 1F (5, 19)):** Confirmed via `path_finder` that this ladder leads to a small, isolated platform with no path to the southern part of the floor. It is a dead end. The only exit is back up the ladder.
*   **Route 32 (Turns ~18059-18060):** Wasted several turns trying to path south to Union Cave entrance (6, 79), forgetting my own documented discovery that the route contains one-way ledges making it impossible to travel north from that section. This is a critical failure in consulting my own documentation. **Lesson:** ALWAYS trust the tools and review relevant notes before planning a route.
*   Grass is NOT VERY EFFECTIVE against Fire.
*   **UI Unreliability:** The `TYPE/` display in battle can be incorrect (e.g., showing EKANS as Normal). Trust observed effectiveness messages over the UI.