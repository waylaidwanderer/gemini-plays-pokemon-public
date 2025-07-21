# Game Objectives
*   **Primary:** Investigate the mysterious radio broadcast by obtaining the Radio Card in Goldenrod City.
*   **Secondary:** Cross Route 27 to reach the main part of Johto.
*   **Tertiary:** Find a rematch with Camper Todd on Route 34.

# Current Objective: Mom's Savings
*   **Situation:** After being blocked from using FLY, a scripted event warped me back to my house.
*   **Immediate Goal:** Complete the money-saving interaction with Mom.
*   **Hypothesis:** Completing this dialogue is required to unlock progression and allow me to travel again.
*   **Plan:**
    1.  Deposit a nominal amount of money to satisfy the script.
    2.  After the dialogue, attempt to use FLY to reach Goldenrod City again.
    3.  If still blocked, proceed to Professor Elm's Lab in New Bark Town.

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

# Misc Notes
*   **Bag is Full:** Cannot pick up the Rare Candy at (53, 12) until a slot is freed.
*   `ROOF`: Visually represented by `WALL` tiles. Confirmed impassable.