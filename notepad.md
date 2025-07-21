# Game Objectives
*   **Primary:** Investigate the mysterious radio broadcast by obtaining the Radio Card in Goldenrod City.

# Side Quests & Rematches
*   **Camper Todd:** Wants a rematch on Route 34.

# Game Systems & Tools
*   **`bfs_pathfinder` Tool:** 
    *   **Status:** Unreliable. Fails on paths with unseen tiles.
    *   **Refinement Plan:** Modify the code to handle unseen tiles, perhaps by pathing to the edge of the seen area in the desired direction instead of failing completely.
*   **`strategy_advisor` Agent:** Its system prompt was refined to forbid suggesting fainting. Needs to be tested to confirm the fix.
*   **Future Agent Idea:** An `exploration_planner` agent could analyze the map's seen/unseen tiles to suggest the most efficient exploration targets.

# Tile Mechanics (Verified & To Be Verified)
*   **Verified Traversable:**
    *   `FLOOR`: Standard ground.
    *   `TALL_GRASS`: Triggers wild encounters.
    *   `WATER`: Requires SURF.
    *   `WATERFALL`: Traversable downwards. Requires Waterfall HM to ascend.
    *   `CAVE`: Warp point.
*   **Verified Impassable:**
    *   `WALL`/`VOID`: Standard barriers.
    *   `HEADBUTT_TREE`: Impassable, can be headbutted.
*   **One-Way Traversal (Verified):**
    *   `LEDGE_HOP_DOWN`: Can only be moved down from.
    *   `LEDGE_HOP_LEFT`: Can only be moved left from.
    *   `FLOOR_UP_WALL`: Can only be moved up from the tile below it.
*   **To Be Verified:**
    *   `BUOY`: Assumed impassable, but needs to be tested by attempting to move onto it.

# Bag Mechanics
*   **Tossing Items:** My hypothesis that the entire stack must be tossed was incorrect. Selling a single, non-stacked item successfully freed up an inventory slot. The exact conditions for the 'TOSS' command failing remain unknown, but selling seems to be a reliable workaround for a full bag.