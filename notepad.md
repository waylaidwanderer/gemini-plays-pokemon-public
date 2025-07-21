# Game Objectives
*   **Primary:** Investigate the mysterious radio broadcast by obtaining the Radio Card in Goldenrod City.
*   **Secondary:** Find a rematch with Camper Todd on Route 34.
*   **Tertiary:** Retrieve the Rare Candy from Route 27 after clearing bag space.

# Future Development Pipeline
*   **New Pathfinding Tool:** HIGHEST PRIORITY. The lack of a reliable pathfinder is a major handicap. The new tool must be built from the ground up with rigorous testing.
*   **`scripted_event_solver` Agent:** An agent that can analyze NPC dialogue, item descriptions, and map info to suggest the next logical interaction to trigger a scripted event.

# Tile Mechanics Testing
*This section tracks experiments to understand how different tiles work.*
*   **Hypothesis: `PC` tiles are impassable.**
    *   **Test:** Attempt to walk into a `PC` tile.
    *   **Status:** Untested.
*   **Hypothesis: `WARP_CARPET_DOWN` has specific entry requirements.**
    *   **Test 1 (Entry from Above):** Moving from (17,30) to (17,31) did not trigger the warp.
    *   **Test 2 (Entry from Side):** Moving from (16,31) to (17,31) did not trigger the warp.
    *   **Conclusion:** The warp at (17, 31) in Union Cave 1F seems to be a one-way exit from Route 33. Will test entry from the Route 33 side when possible.

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
    *   `FLOOR_UP_WALL`: Can only be entered by moving up from the tile below.

# Misc Notes & Reminders
*   **Bag is Full:** Cannot pick up the Rare Candy at (53, 12) on Route 27 until a slot is freed.
*   **Pending Rematch:** Fisher Ralph on Route 32.
*   **Violet Gym Warp:** The warp tile at (5, 15) inside the Violet City Gym is a one-way exit that returns the player to the front of the gym.

# Lessons Learned (Recent Failures)
*   **Pathfinding Failure:** My manual pathing has been highly unreliable, leading to getting "stuck" in areas that were not actually traps. I must be more careful and methodical when navigating complex terrain.
*   **Tool Over-Reliance/Fixation:** I wasted many turns trying to fix the `bfs_pathfinder` tool instead of recognizing it was fundamentally flawed and pivoting to a different strategy (like manual navigation or using an HM). If a tool is broken, I must delete it and build a better one, not get stuck in a debugging loop.
*   **Agent Logic Flaw:** The `strategy_advisor` agent provided incorrect advice (using DIG on an outdoor route). This highlights the need for extremely precise and context-rich system prompts. Agents must be given all relevant game mechanics to function correctly.