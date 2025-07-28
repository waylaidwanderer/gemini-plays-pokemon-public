# Gem's Pokémon Crystal Adventure Log

# I. Core Directives & Lessons Learned
*   **Proactive Data Management:** All new information, corrected misunderstandings, and strategic plans must be recorded *immediately* in the turn they are discovered. Data management is not a secondary task; it is the highest priority.
*   **Tool Consolidation:** Redundant tools with overlapping logic must be consolidated into a single, robust tool to serve as the single source of truth. This prevents logic desynchronization and repetitive failure loops.
*   **Agent Usage Discipline:** Use reasoning agents for significant or complex decisions only. Rely on personal judgment for trivial encounters to conserve turns. Proactively use the `procedural_overseer` agent to detect and break out of repetitive, failing loops.
*   **Investigate Contradictions:** A persistent contradiction between a verified custom tool and the game environment is a strong indicator of a potential bug in the tool. Instead of dismissing the alert, the tool itself must be rigorously debugged.
*   **Scientific Method:** When debugging or solving puzzles, I must form a clear hypothesis and test it methodically. All hypotheses and tests must be documented.
*   **Verify Location:** Always verify my current map and coordinates before planning any navigation, especially after a map transition.

## B. Tile Traversal Rules
*   **Traversable:** TALL_GRASS, LONG_GRASS, DOOR, WARP_CARPET_LEFT, WARP_CARPET_DOWN, LADDER, FLOOR.
*   **Impassable (to walk on):** WALL, WINDOW, PC, VOID, CUT_TREE, SIGN, BOOKSHELF, BLACKBOARD, MART_SHELF, BUOY, TV, TOWN_MAP, RADIO, INCENSE_BURNER, COUNTER, BIRD, HEADBUTT_TREE, FRUIT_TREE.
*   **One-Way Traversal:**
    *   LEDGE_HOP_DOWN: Can only be entered from above.
    *   LEDGE_HOP_RIGHT: Can only be entered from the left.
    *   LEDGE_HOP_LEFT: Can only be entered from the right.
    *   FLOOR_UP_WALL (Hypothesis): Cannot be entered from above (moving down). Cannot be exited from by moving up. Sideways movement between adjacent FLOOR_UP_WALL tiles is permitted. Entry from below (moving up) and exiting by moving down to a FLOOR tile are pending verification.
*   **Special Interaction (Warp):**
    *   **CAVE:** Can act as a one-way warp. The tile at Route 33 (11, 9) is a confirmed one-way entrance to Union Cave (17, 31). The tile at Route 32 (6, 79) is a confirmed one-way entrance to Union Cave (17, 3). Should be treated as impassable for pathfinding.
*   **Special Interaction (Fishing):**
    *   WATER: Impassable to walk on, but can be fished in with a rod.

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

## A. Current Quest
*   **Current Quest:** Investigate the strange tree on Route 36.

## B. NPC Hints & Lore
*   A Fisher in Union Cave at (14, 19) mentioned that strange roars can be heard from deep within the cave on weekends.

# IV. Stalled Quests & Concluded Investigations

*   **HM01 Cut Quest (Stalled):** The quest is confirmed to be stalled. Both the Charcoal Man in Azalea Town and his apprentice in Ilex Forest are in a dialogue loop, even after solving the Farfetch'd puzzle. The path north in Ilex Forest is blocked by a CUT_TREE at (8, 25), making progress impossible until a new trigger is found.
*   **Azalea Town NPCs (Post-Well):** Neither Kurt nor the Charcoal Man had new dialogue immediately after clearing the Slowpoke Well and solving the Farfetch'd puzzle.
*   **Slowpoke Well:** Re-exploration confirmed no missed triggers or reachable unseen areas.
*   **Union Cave Unseen Tiles (Confirmed):** Pathfinding attempts to the western section of the cave from the eastern side have failed, suggesting the areas are disconnected.
*   **Union Cave Warp (Failed):** The WARP_CARPET_DOWN at (17, 3) cannot be activated with 'A' or by pressing 'Down'. It appears to be a one-way entrance from Route 32.

## B. Technical Investigations & Hallucinations
*   **CRITICAL HALLUCINATION (Turn 11733):** I believed I had already transitioned to Route 33 and was trying to pathfind from there. The system corrected me; I was still at the exit of Azalea Town (39, 15). This highlights the need to always verify my current location before planning.
*   **CRITICAL HALLUCINATION (Turn 11840):** I incorrectly assumed the map exit at Route 33 (0, 15) was a warp. I must verify all warps in the game state data before setting them as navigation goals.
*   **Route 33 North Path (Confirmed Blocked):** Manually attempting to move north from (9, 10) confirmed that the tile at (9, 9) is an impassable wall. My pathfinding tools were correct; the northern unseen area is unreachable from this side due to one-way ledges.
*   **CRITICAL HALLUCINATION (Turn 12026):** I completely misunderstood my location. I believed I had successfully navigated through Union Cave and was exploring Route 32. In reality, I had exited the cave and immediately re-entered through the northern warp at (6, 79), which I mistook for a path forward. This highlights a critical need to slow down and verify my location after every single map transition, no matter how certain I feel.
*   **CRITICAL HALLUCINATION (Turn 12744 & 12797):** I have repeatedly become disoriented about my location after map transitions, believing I was on a different map or outside when I was still inside. This is a recurring issue. I MUST verify my map and coordinates before every single navigational plan.

# V. Key Items & HMs
*   **OLD ROD:** Received from the Fishing Guru in the Route 32 Pokémon Center. Allows fishing in bodies of water.

# VI. Held Items
*   **POISON BARB:** Received from FRIEDA on Route 32 on a Friday. Boosts the power of poison-type moves.
*   **Scientific Method for Mechanics:** When encountering a new or unclear game mechanic, I must adopt a strict 'test-first' approach. 1. Form a clear, simple hypothesis. 2. Design and execute a manual in-game test to confirm or deny it. 3. Document the verified results in the notepad. 4. Only after a mechanic is fully verified should I implement it in a custom tool.

# VII. Methodical Mechanics Testing

## A. LEDGE_HOP_DOWN Traversal
*   **Hypothesis:** `LEDGE_HOP_DOWN` tiles are one-way and cannot be traversed from below (i.e., by moving up).
*   **Test:** Stood at Route 33 (12, 14) and attempted to move up to the `LEDGE_HOP_DOWN` tile at (12, 13).
*   **Conclusion:** Movement was blocked. The hypothesis is confirmed. This tile type is impassable from below.

## Route 33 Layout
*   **Hypothesis:** Route 33 is a one-way path from east to west.
*   **Evidence:** The entrance from Union Cave is at (11, 9). The path leads west over a series of `LEDGE_HOP_LEFT` and `LEDGE_HOP_DOWN` tiles. My own testing confirms these are one-way. It is impossible to travel east along the northern path from Azalea Town.
*   **Conclusion:** The northern unseen tiles flagged by the system are unreachable from the southern half of the route. The alerts can be safely ignored when entering from Azalea Town.

# VII. Methodical Mechanics Testing (Pathfinder Debugging)

## A. Pathfinder Debugging Plan - Union Cave
*   **Objective:** Fully understand the traversal rules for the `FLOOR_UP_WALL` tile type to fix the `pathfinder` tool.
*   **Location:** Union Cave 1F, northern section (accessible from Route 32).
*   **Procedure:**
    1.  Travel to the `FLOOR_UP_WALL` tiles located near (15, 4).
    2.  **Test 1 (Entry from Below):** Stand on a `FLOOR` tile at (15, 5) and attempt to move UP to the `FLOOR_UP_WALL` at (15, 4). Document result.
    3.  **Test 2 (Exit Downwards):** From (15, 4), attempt to move DOWN to (15, 5). Document result.
    4.  **Test 3 (Exit Upwards):** From (15, 4), attempt to move UP to the `WALL` at (15, 3). Document result (expected to fail).
    5.  **Test 4 (Sideways Movement):** From (15, 4), attempt to move RIGHT to (16, 4) and LEFT to (14, 4). Document results.
*   **Conclusion:** Only after all tests are complete and documented will I attempt to modify the `pathfinder` tool's code.