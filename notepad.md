# Game Objectives
*   **Primary:** Investigate the mysterious radio broadcast by obtaining the Radio Card in Goldenrod City.
*   **Secondary:** Cross Route 27 to reach the main part of Johto.
*   **Tertiary:** Find a rematch with Camper Todd on Route 34.

# Exploration Plan: Route 27
*   **Current Location:** Dead-end island at (52, 12).
*   **Immediate Goal:** Get back on the water at (51, 12) by facing the water and using SURF.
*   **Hypothesis:** The southern water channel is the main path forward.
*   **Plan:** 
    1.  Surf east along the southern channel.
    2.  **Test `BUOY` tile:** Navigate to the `BUOY` at (26, 14) and attempt to move onto it to confirm if it's impassable.
    3.  Continue exploring eastward to find the route's exit or a path to the upper ledge.

# Game Systems & Tools
*   **`bfs_pathfinder` Tool:** 
    *   **Status:** Fully operational. The refined logic correctly handles unseen tiles and pathing to the map edge.
*   **`strategy_advisor` Agent:** Its system prompt was refined to forbid suggesting fainting. Needs to be tested to confirm the fix.
*   **Future Agent Idea:** An `exploration_planner` agent could analyze the map's seen/unseen tiles to suggest the most efficient exploration targets.

# Tile Mechanics
*   **Verified Traversable:**
    *   `FLOOR`: Standard ground.
    *   `TALL_GRASS`: Triggers wild encounters.
    *   `WATER`: Requires SURF. Can only be entered by facing the tile and pressing 'A'.
    *   `CAVE`/`DOOR`: Warp point.
*   **Verified Impassable:**
    *   `WALL`/`VOID`: Standard barriers.
    *   `HEADBUTT_TREE`: Impassable, can be headbutted.
    *   `BUOY`: Confirmed impassable after attempting to move onto the tile at (27, 16).
    *   `ROOF`: Impassable.
*   **One-Way Traversal (Verified):**
    *   `LEDGE_HOP_DOWN`: Can only be moved down from.
    *   `LEDGE_HOP_LEFT`: Can only be moved left from.

# Tile Mechanics
*   **Verified Traversable:**
    *   `FLOOR`: Standard ground.
    *   `TALL_GRASS`: Triggers wild encounters.
    *   `WATER`: Requires SURF. Can only be entered by facing the tile and pressing 'A'.
    *   `CAVE`/`DOOR`: Warp point.
*   **Verified Impassable:**
    *   `WALL`/`VOID`: Standard barriers.
    *   `HEADBUTT_TREE`: Impassable, can be headbutted.
*   **One-Way Traversal (Verified):**
    *   `LEDGE_HOP_DOWN`: Can only be moved down from.
    *   `LEDGE_HOP_LEFT`: Can only be moved left from.
*   `BUOY`: Confirmed impassable after attempting to move onto the tile at (27, 16).

# Misc Notes
*   **Bag is Full:** Cannot pick up the Rare Candy at (53, 12) until a slot is freed.
*   `ROOF`: Visually represented by `WALL` tiles. Confirmed impassable.