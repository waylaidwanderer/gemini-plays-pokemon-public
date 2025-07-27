# Gem's Pokémon Crystal Adventure Log

# I. Core Directives & Lessons Learned

*   **Proactive Data Management:** All new information, corrected misunderstandings, and strategic plans must be recorded *immediately* in the turn they are discovered. Data management is not a secondary task; it is the highest priority.
*   **Agent Usage Discipline:** Use reasoning agents (`battle_strategist`, etc.) for significant or complex decisions only. Rely on personal judgment for trivial encounters to conserve turns. Proactively use the `procedural_overseer` agent to detect and break out of repetitive, failing loops.
*   **Investigate Contradictions:** A persistent contradiction between a verified custom tool and the game environment (e.g., system alerts) is a strong indicator of a potential bug in the tool. Instead of dismissing the alert, the tool itself must be rigorously debugged.
*   **Scientific Method:** When debugging or solving puzzles, I must form a clear hypothesis and test it methodically. All hypotheses and tests must be documented.
*   **Verify Location:** Always verify my current map and coordinates before planning any navigation, especially after a map transition.
*   **Tool Synchronization:** Tools with shared logic (like pathfinding and exploration) MUST be updated together to avoid contradictory results.

## B. Tile Traversal Rules
*   **Traversable:** FLOOR, TALL_GRASS, LONG_GRASS, DOOR, LADDER.
*   **Impassable:** WALL, WINDOW, PC, VOID, CUT_TREE, SIGN, BOOKSHELF, BLACKBOARD, MART_SHELF, WATER, BUOY, TV, TOWN_MAP, RADIO, INCENSE_BURNER, COUNTER, BIRD, HEADBUTT_TREE, FRUIT_TREE, CAVE.

*   **One-Way Traversal:**
    *   LEDGE_HOP_DOWN: Can only be entered from above.
    *   LEDGE_HOP_RIGHT: Can only be entered from the left.
    *   LEDGE_HOP_LEFT: Can only be entered from the right.
    *   FLOOR_UP_WALL: Can only be entered from below. It is a one-way tile that acts as a ledge you jump up.
*   **Warp Carpets:** Generally activated by pressing the corresponding direction (e.g., `WARP_CARPET_RIGHT` requires pressing 'Right'). However, some, like the one at Union Cave (17, 3), may be one-way entrances and cannot be activated from the exit side.

# II. Battle Information

## A. Verified Type Matchups
*   Ghost has NO EFFECT on Normal.
*   Normal has NO EFFECT on Ghost.
*   Unown's Hidden Power (type unknown) can be super-effective against Fire.

## B. Gym Leader Teams
*   **Falkner (Violet City):** Pidgey (Lv7), Pidgeotto (Lv9).
*   **Bugsy (Azalea Town):** Metapod (Lv14), Kakuna (Lv14), Scyther (Lv16).

# III. Story & Quests

## A. Current Quest
*   **Current Quest:** Investigate the strange tree on Route 36.

## B. NPC Hints & Lore
*   A Fisher in Union Cave at (14, 19) mentioned that strange roars can be heard from deep within the cave on weekends.

# IV. Concluded Investigations

*   **Ilex Forest (Stalled):** The HM01 Cut quest is stalled. The apprentice's dialogue remains unchanged even after the Farfetch'd he was looking for has disappeared. The northern section of the forest is inaccessible from the south due to one-way ledges.
*   **Azalea Town NPCs (Post-Well):** Neither Kurt nor the Charcoal Man had new dialogue immediately after clearing the Slowpoke Well and solving the Farfetch'd puzzle.
*   **Slowpoke Well:** Re-exploration confirmed no missed triggers or reachable unseen areas.
*   **Union Cave Unseen Tiles:** The western section of the cave, containing the unseen tiles, is physically disconnected from the eastern section by walls and water. The unseen tiles are genuinely unreachable from either entrance.
*   **Union Cave Warp (Failed):** The WARP_CARPET_DOWN at (17, 3) cannot be activated with 'A' or by pressing 'Down'. It appears to be a one-way entrance from Route 32.

## B. Technical Investigations
*   **CRITICAL HALLUCINATION (Turn 11733):** I believed I had already transitioned to Route 33 and was trying to pathfind from there. The system corrected me; I was still at the exit of Azalea Town (39, 15). This highlights the need to always verify my current location before planning.
*   **CRITICAL HALLUCINATION (Turn 11840):** I incorrectly assumed the map exit at Route 33 (0, 15) was a warp. I must verify all warps in the game state data before setting them as navigation goals.
*   **Route 33 North Path (Confirmed Blocked):** Manually attempting to move north from (9, 10) confirmed that the tile at (9, 9) is an impassable wall. My pathfinding tools were correct; the northern unseen area is unreachable from this side due to one-way ledges.
*   **CRITICAL HALLUCINATION (Turn 12026):** I completely misunderstood my location. I believed I had successfully navigated through Union Cave and was exploring Route 32. In reality, I had exited the cave and immediately re-entered through the northern warp at (6, 79), which I mistook for a path forward. This highlights a critical need to slow down and verify my location after every single map transition, no matter how certain I feel.

# V. Key Items & HMs
*   **OLD ROD:** Received from the Fishing Guru in the Route 32 Pokémon Center. Allows fishing in bodies of water.

# VI. Held Items
*   **POISON BARB:** Received from FRIEDA on Route 32 on a Friday. Boosts the power of poison-type moves.