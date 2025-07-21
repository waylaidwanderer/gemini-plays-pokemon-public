# Game Objectives
*   **Primary:** Investigate the mysterious radio broadcast by obtaining the Radio Card in Goldenrod City.
*   **Secondary:** Find a rematch with Camper Todd on Route 34.
*   **Tertiary:** Retrieve the Rare Candy from Route 27 after clearing bag space.

# Current Objective: Leaving Home
*   **Situation:** After being blocked from using FLY, a scripted event warped me back to my house and forced a dialogue with Mom.
*   **Immediate Goal:** Exit the house and proceed to Goldenrod City.
*   **Hypothesis:** The warp at (7, 7) is non-functional. The warp at (6, 7) should work.
*   **Plan:**
    1.  Move to tile (6, 7) to attempt to trigger the warp.
    2.  If successful, fly to Goldenrod City.

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
    *   `CAVE`/`DOOR`/`STAIRCASE`: Warp point.
*   **Verified Impassable:**
    *   `WALL`/`VOID`: Standard barriers.
    *   `HEADBUTT_TREE`: Impassable, can be headbutted.
    *   `BUOY`: Confirmed impassable after attempting to move onto the tile at (27, 16).
    *   `ROOF`/`TV`: Impassable.
*   **One-Way Traversal (Verified):**
    *   `LEDGE_HOP_DOWN`: Can only be moved down from.
    *   `LEDGE_HOP_LEFT`: Can only be moved left from.
*   **Needs Further Testing:**
    *   `WARP_CARPET_DOWN`: Appears to be a warp tile. Need to test if it can be entered from the sides or only from above.

# Misc Notes
*   **Bag is Full:** Cannot pick up the Rare Candy at (53, 12) until a slot is freed.