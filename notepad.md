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
*   **Traversable:** TALL_GRASS, LONG_GRASS, DOOR, WARP_CARPET_DOWN, LADDER, FLOOR, WARP_CARPET_RIGHT.
*   **Impassable (Verified):** WALL, WINDOW, CUT_TREE, SIGN, BOOKSHELF, BLACKBOARD, MART_SHELF, BUOY, TV, TOWN_MAP, BIRD, HEADBUTT_TREE, FRUIT_TREE, COMPUTER, PRINTER, VOID, WATER, CAVE, COUNTER.
*   **Failure to Test New Mechanics (Turn 20104):** Overwatch correctly identified that I had a list of untested tile types, violating my core principle of immediate testing. A script confirmed these tiles are not on the current map (Ilex Forest), meaning I failed to test them on a previous map when I first encountered them. **Correction:** I must adhere to the Observe, Hypothesize, Test, Conclude method for all new mechanics the moment they are discovered. I have removed the unactionable 'Untested' list for now.
*   **One-Way Traversal:**
    *   LEDGE_HOP_DOWN: Can only be entered from above.
    *   LEDGE_HOP_RIGHT: Can only be entered from the left.
    *   LEDGE_HOP_LEFT: Can only be entered from the right.
*   **Special Interaction (Warp):**
    *   **CAVE:** Can act as a one-way warp. Route 33 (11, 9) -> Union Cave (17, 31). Route 32 (6, 79) -> Union Cave (17, 3).
    *   **WARP_CARPET_DOWN:** Activated by pressing Down while standing on the tile.
    *   **WARP_CARPET_RIGHT:** Activated by pressing Right while standing on the tile.
*   **Special Interaction (Walls/Floors):**
    *   **FLOOR_UP_WALL:** A one-way slide. Movement *from* this tile is only possible Down. Movement *onto* this tile is only possible by moving UP from a tile below (Y+1 -> Y).
    *   **Visual Ledges (FLOOR type):** Some FLOOR tiles are visually one-way ledges and are impassable from below. Verified at UnionCave1F, preventing movement from (7, 26) up to (7, 25).
*   **Special Interaction (Interactable):**
    *   **PC:** Interact by standing below it at (X, Y+1), facing up.
    *   **COUNTER:** Interact with NPCs behind it by standing in front of the counter.
    *   **WATER:** Can be fished in with a rod.

# III. Battle Information
## A. Verified Type Matchups
*   Fire is SUPER-EFFECTIVE against Bug.
*   Fire is SUPER-EFFECTIVE against Grass.
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
*   **Primary Quest: Travel to Goldenrod City**
    *   **Objective:** Reach Goldenrod City by clearing the path through Ilex Forest.
    *   **Status:** Completed the Farfetch'd puzzle and received HM01 Cut. Now I need to catch a Pokémon that can learn Cut to clear the tree at (8, 25).
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
*   **Objective:** Herd the Farfetch'd to the apprentice at (7, 28).
*   **Puzzle Mechanics (Confirmed):** The puzzle is a scripted sequence. Interaction from a specific direction or stepping on specific tiles is required for each step. An incorrect interaction can cause a partial or full reset.
    *   **Full Reset:** Returns Farfetch'd to start (29, 22).
    *   **Partial Reset:** Can return Farfetch'd to a previous step in the sequence.
*   **Known Correct Sequence:**
    *   **Step 1:** Interact from West at (28, 22) -> Moves bird from (29, 22) to (28, 31).
    *   **Step 2:** Interact from South at (28, 32) -> Moves bird from (28, 31) to (15, 25).
    *   **Step 3 (Confirmed):** Stepping on the twig pile at (15, 27) causes the Farfetch'd at (15, 25) to move. Its new location is currently unknown.
*   **Confirmed Reset Trigger:** Interacting from the East at (21, 24) at the wrong time causes a full puzzle reset.

# VI. System Alert Verifications & Alternative Hypotheses
*   **Ilex Forest Unseen Tiles (Confirmed Unreachable):** My `reachability_analyzer` tool has definitively confirmed on multiple occasions (Turns 20968, 21230, 21298, 21303, and others) that the system-flagged unseen tiles at (7, 21), (9, 21), (0, 23), (1, 23), (2, 23), and (3, 23) are unreachable from my current position. This validates the hypothesis that the path is blocked by the CUT_TREE at (8, 25). I will trust my tool and ignore this specific alert until I obtain HM01 Cut.
*   **Farfetch'd Puzzle Reset (Tested Turn 20915):**
    *   **Hypothesis:** Leaving and re-entering Ilex Forest will cause a hard reset of the Farfetch'd puzzle, returning the bird to its starting position (29, 22).
    *   **Test:** I left the forest via the gatehouse and immediately re-entered.
    *   **Conclusion:** The hypothesis was **false**. The Farfetch'd did not return to (29, 22). Instead, the puzzle state reverted to a mid-point, with the Farfetch'd at (15, 25). This indicates leaving the map causes a partial, not a full, reset.
*   **Farfetch'd Puzzle Logic (Alternative Hypothesis):**
    *   **Hypothesis:** The puzzle is not a single linear sequence but a state machine. The bird moves between a few key locations, and the correct interaction depends on its current state (location). An interaction that causes a reset from one state might be a valid move from another.
    *   **Test to Disprove:** Find a situation where the previously confirmed 'reset' move (interacting from the East at (21, 24)) results in a successful step forward instead of a full puzzle reset. This would confirm the state machine hypothesis.

# VII. Team Strategy (from team_analyst)
*   **Training Priority:** MIASma (Gastly) should be trained up.
*   **Move Optimization:** Replace Vulcan's EMBER with a better coverage move. Conserve MIASma's HYPNOSIS. Level Gambit via switching.
*   **Team Weaknesses:** Critical weakness to Water-types. Lack of coverage for Rock, Ground, or Psychic types.

# VIII. Future Test Plans
*   **Farfetch'd Puzzle State Machine Test:** If the known linear sequence fails again after a full reset, I will test the alternative hypothesis that the puzzle is a state machine. The test will be to intentionally perform a different incorrect action at a known failure point to see if it results in a partial reset instead of a full one. This would indicate the puzzle's state influences the outcome of interactions.
*   **Farfetch'd Puzzle Step 3 (Hypotheses Falsified):** My documented sequence for step 3 is incorrect. After the bird moves to (15, 25), interacting from the south (15, 26) or north (15, 24) does not work, even after a full puzzle reset.
*   **New Hypothesis (Twig Noise):** I hypothesize that the puzzle is not solved by direct interaction at this stage. Instead, stepping on the piles of twigs on the ground may create a noise that causes the Farfetch'd at (15, 25) to move.
*   **Test:** I will navigate to the twig pile at (14, 27) and step on it to observe the effect.