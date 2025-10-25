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
*   **Primary Quest: Obtain HM01 Cut**
    *   **Objective:** Receive HM01 Cut from the apprentice in Ilex Forest.
    *   **Current Plan:** My manual approach has been inefficient. I have now confirmed the puzzle is a scripted sequence. My current plan is to follow the scripted sequence I have discovered.
    *   **Contingency:** If 3 more systematic, agent-guided attempts to solve this puzzle fail, I will pivot my primary goal to 'Explore towards Goldenrod City' and find an alternate route.
*   **Secondary Quest: Complete Sprout Tower**
    *   **Objective:** Reach the top of Sprout Tower and defeat the Elder.
    *   **Status:** Blocked. Need to find the correct path up the western ladder system.
*   **Tertiary Quest: Investigate Union Cave Roars**
    *   **Objective:** Discover the source of the strange roars heard in Union Cave on Fridays.
    *   **Status:** Blocked. Requires it to be Friday.
*   **NPC Hints & Lore:**
    *   WADE (Route 31): Will share BERRIES.
    *   Hiker Anthony (Phone): Tons of DUNSPARCE in DARK CAVE.

# VI. Untested Assumptions & Alternative Hypotheses
*   **Farfetch'd Puzzle:** My current hypothesis is that interacting with the Farfetch'd from a specific direction pushes it in the opposite direction. **Alternative Hypothesis:** The Farfetch'd's movement is a fixed, scripted sequence, and each interaction simply advances it to the next point on its path, regardless of my approach vector. **Test:** If approaching from the south (15, 26) does not push it north, the 'push' hypothesis is weakened or incorrect.

*   **`reachability_analyzer` Discrepancy:**
    *   **Current Conclusion (Confirmed):** The reachability_analyzer tool has repeatedly and correctly confirmed that the system-flagged unseen tiles are unreachable from my current position. The blockage is almost certainly the CUT_TREE at (8, 25). I will trust my tool's analysis over the persistent system alert and will not re-investigate this until I have HM01 Cut.
    *   **Alternative Hypothesis:** The tool's A* or map parsing logic contains a subtle flaw that fails on this specific map's layout, possibly missing a traversable tile type or special movement rule.
    *   **Test to Disprove:** If I obtain HM01 Cut, use it on the tree at (8, 25), and the unseen tiles are *still* unreachable, then this alternative hypothesis becomes highly likely. At that point, I MUST perform a full diagnostic on the `reachability_analyzer` tool using `run_code` with print statements to trace its logic on this map's XML data.

**Farfetch'd Puzzle Update (Turn 20043):** My prediction for Step 5 was incorrect. The Farfetch'd moved to (15, 29), not (15, 25). This disproves a simple linear path. The sequence is more complex.
*   **Farfetch'd Puzzle (Alternative Hypothesis):** The bird's movement might be based purely on the number of interactions, not the direction of approach. **Test:** Next time, approach from a seemingly 'wrong' direction. If it moves to the same next point, this hypothesis is strengthened.

**Farfetch'd Puzzle Reset (Turn 20421):** My hypothesis was partially correct. It is a scripted sequence, but the direction of interaction is critical. Interacting with the Farfetch'd at (20, 24) from the north (20, 23) was the incorrect move and caused the puzzle to reset, returning the Farfetch'd to its starting position at (29, 22). This confirms that a specific interaction vector is required for each step. **New Plan:** Restart the puzzle from the beginning at (29, 22), but this time, I will systematically test directions at each step to find the correct sequence.

# V. Puzzle Logs & Navigational Failures (Refactored)
## A. Ilex Forest Farfetch'd Puzzle
*   **Objective:** Herd the Farfetch'd to the apprentice at (7, 28).
*   **Puzzle Mechanics (Confirmed):** The puzzle is a scripted sequence. Interaction from a specific direction is required for each step. An incorrect interaction can cause a partial or full reset.
    *   **Full Reset:** Returns Farfetch'd to start (29, 22).
    *   **Partial Reset:** Can return Farfetch'd to a previous step in the sequence.
*   **Known Correct Sequence:**
    *   **Step 1:** Interact from West at (28, 22) -> Moves bird from (29, 22) to (28, 31).
    *   **Step 2:** Interact from South at (28, 32) -> Moves bird from (28, 31) to (24, 35).
    *   **Step 3:** Interact from North at (24, 34) -> Moves bird from (24, 35) to (15, 29).
    *   **Step 4:** Interact from East at (16, 29) -> Moves bird from (15, 29) to (15, 25).
    *   **Step 5:** Interact from North at (15, 24) -> Moves bird from (15, 25) to (15, 29).
*   **Known Incorrect Moves:**
    *   At (20, 24), interacting from East (21, 24) causes a full reset.
    *   At (15, 25), interacting from South (15, 26) causes a unique reset to (20, 24).

# VII. Puzzle Progress & Hypotheses
*   **Farfetch'd Puzzle Update (Turn 20702):** Step 4 confirmed! Interacting with the Farfetch'd at (15, 29) from the east at (16, 29) successfully moved it to (15, 25).
*   **New Hypothesis:** Now that the bird is at (15, 25), all direct interactions seem to lead to a loop or a reset. My new hypothesis is that this is a checkpoint, and I must now speak to the apprentice at (7, 28) to trigger the next phase of the puzzle. I will travel there to test this.

# VIII. Reflection (Turn 20811)
*   **Farfetch'd Puzzle Untested Assumption:** My main conclusion is that the puzzle is a fixed, scripted sequence where interaction direction is key. **Alternative Hypothesis:** The puzzle's state is also influenced by another hidden factor, such as time of day, an item in my bag, or the state of another NPC. **Test to Disprove:** If I follow my documented "correct" sequence and it fails, this alternative hypothesis is strengthened.

# IX. Team Strategy (from team_analyst)
*   **Training Priority:** MIASma (Gastly) should be trained up.
*   **Move Optimization:** Replace Vulcan's EMBER with a better coverage move. Conserve MIASma's HYPNOSIS. Level Gambit via switching.
*   **Team Weaknesses:** Critical weakness to Water-types. Lack of coverage for Rock, Ground, or Psychic types.