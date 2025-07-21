# Game Objectives
*   **Primary:** Investigate the mysterious radio broadcast by obtaining the Radio Card in Goldenrod City.
*   **Secondary:** Find a rematch with Camper Todd on Route 34.
*   **Tertiary:** Retrieve the Rare Candy from Route 27 after clearing bag space.

# Current Objective: Cherrygrove Detour
*   **Situation:** Unexpectedly warped to Cherrygrove City (29, 4) after attempting to use FLY from New Bark Town. Now on Pokecenter2F.
*   **Immediate Goal:** Investigate the reason for this scripted event, starting with the Pokémon Center's second floor.
*   **Hypothesis:** The event trigger is on the second floor, likely involving the Link Receptionist.

# Game Systems & Tools
*   **`bfs_pathfinder` Tool:** 
    *   **Status:** Needs fixing. The current logic does not correctly identify all impassable tiles, leading to pathing errors. Will be updated this turn.
*   **`strategy_advisor` Agent:** Its system prompt was refined to forbid suggesting fainting. Needs to be tested to confirm the fix.
*   **Future Agent Idea:** An `exploration_planner` agent could analyze the map's seen/unseen tiles to suggest the most efficient exploration targets.

# Tile Mechanics
*   **Verified Traversable:**
    *   `FLOOR`: Standard ground.
    *   `TALL_GRASS`: Triggers wild encounters.
    *   `WATER`: Requires SURF. Can only be entered by facing the tile and pressing 'A'.
    *   `CAVE`/`DOOR`/`STAIRCASE`/`LADDER`: Warp point.
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