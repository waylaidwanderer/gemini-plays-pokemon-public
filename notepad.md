# Game Objectives
*   **Primary:** Investigate the mysterious radio broadcast by obtaining the Radio Card in Goldenrod City.
*   **Secondary:** Find a rematch with Camper Todd on Route 34.
*   **Tertiary:** Retrieve the Rare Candy from Route 27 after clearing bag space.

# Game Systems & Tools
*   **`bfs_pathfinder` Tool:** 
    *   **Status:** Fixed and operational. The logic now correctly identifies 'WALL' as an impassable tile type.
*   **`strategy_advisor` Agent:** Its system prompt was refined to forbid suggesting fainting. Needs to be tested to confirm the fix.
*   **Future Agent Idea:** An `scripted_event_solver` agent could analyze NPC dialogue and map info to suggest the next logical interaction to try.

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
    *   `COUNTER`/`PC`: Assumed impassable. Need to verify by attempting to walk into them.
*   **One-Way Traversal (Verified):**
    *   `LEDGE_HOP_DOWN`: Can only be moved down from.
    *   `LEDGE_HOP_LEFT`: Can only be moved left from.
*   **Needs Further Testing:**
    *   `WARP_CARPET_DOWN`: Appears to be a warp tile. Need to test if it can be entered from the sides or only from above.

# Misc Notes
*   **Bag is Full:** Cannot pick up the Rare Candy at (53, 12) on Route 27 until a slot is freed.