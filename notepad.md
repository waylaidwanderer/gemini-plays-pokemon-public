# Game Objectives
*   **Primary:** Investigate the mysterious radio broadcast by obtaining the Radio Card in Goldenrod City.
*   **Secondary:** Find a rematch with Camper Todd on Route 34.
*   **Tertiary:** Retrieve the Rare Candy from Route 27 after clearing bag space.

# Game Systems & Tools
*   **`bfs_pathfinder` Tool:** 
    *   **Status:** DELETED. The tool was fundamentally flawed and failed multiple debugging attempts. Manual navigation is required until a new, reliable pathfinding tool can be created.
*   **`strategy_advisor` Agent:** Its system prompt was refined to forbid suggesting fainting. Needs to be tested to confirm the fix.
*   **Future Agent Idea:** An `scripted_event_solver` agent could analyze NPC dialogue and map info to suggest the next logical interaction to try.

# Tile Mechanics Testing
*This section tracks experiments to understand how different tiles work.*
*   **Hypothesis: `PC` tiles are impassable.**
    *   **Test:** Attempt to walk into a `PC` tile.
    *   **Status:** Untested.
*   **Hypothesis: `WARP_CARPET_DOWN` has specific entry requirements.**
    *   **Test 1 (Entry from Above):** Moving from (17,30) to (17,31) did not trigger the warp.
    *   **Next Test (Entry from Side):** Will attempt to enter from (16,31).

# Verified Tile Mechanics
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
    *   `COUNTER`: Confirmed impassable after attempting to move onto the tile at (3, 2).
*   **One-Way Traversal (Verified):**
    *   `LEDGE_HOP_DOWN`: Can only be moved down from.
    *   `LEDGE_HOP_LEFT`: Can only be moved left from.
*   **Needs Further Testing:**
    *   `WARP_CARPET_DOWN`: Appears to be a warp tile. Need to test if it can be entered from the sides or only from above.
    *   `PC`: Assumed impassable. Need to verify by attempting to walk into it.

# Misc Notes & Reminders
*   **Bag is Full:** Cannot pick up the Rare Candy at (53, 12) on Route 27 until a slot is freed.
*   **Pending Rematch:** Fisher Ralph on Route 32.
*   **Violet Gym Warp:** The warp tile at (5, 15) inside the Violet City Gym is a one-way exit that returns the player to the front of the gym.