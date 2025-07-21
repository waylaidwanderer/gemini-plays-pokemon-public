# Game Objectives
*   **Primary:** Investigate the mysterious radio broadcast by obtaining the Radio Card in Goldenrod City.
*   **Secondary:** Retrieve the Rare Candy from Route 27 after clearing bag space.
*   **Tertiary:** Find a rematch with Schoolboy Alan on Route 36.

# Development Pipeline
*   **New Pathfinding Tool:** HIGHEST PRIORITY. Manual pathing is inefficient and error-prone. The new tool must be built from the ground up with rigorous testing, capable of navigating around static and dynamic obstacles.

# Tile Mechanics Testing
*This section tracks experiments to understand how different tiles work.*
*   **Hypothesis: `WALL` tiles are impassable, regardless of visual appearance.**
    *   **Test:** Attempt to walk into various `WALL` tiles on the current map.
    *   **Status:** Untested.
*   **Hypothesis: `PC` tiles are impassable.**
    *   **Test:** Attempt to walk into a `PC` tile.
    *   **Status:** Untested.
*   **Hypothesis: `WARP_CARPET_DOWN` has specific entry requirements.**
    *   **Conclusion:** The warp at (17, 31) in Union Cave 1F seems to be a one-way exit from Route 33. Will test entry from the Route 33 side when possible.

# Verified Tile Mechanics
*   **Verified Traversable:**
    *   `FLOOR`: Standard ground.
    *   `TALL_GRASS`: Triggers wild encounters.
    *   `WATER`: Requires SURF. Can only be entered by facing the tile and pressing 'A'.
    *   `CAVE`/`DOOR`/`STAIRCASE`/`LADDER`: Warp point.
*   **Verified Impassable:**
    *   `VOID`: Standard barrier.
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
*   **Pathfinding Failure:** My manual pathing has been highly unreliable. I must be more methodical. An alternative hypothesis for pathing failures is a bug in long path execution, not just moving NPCs. Test with short, simple paths.
*   **Tool Over-Reliance/Fixation:** Wasted turns trying to fix the `bfs_pathfinder` tool. If a tool is broken, I must delete it and build a better one, not get stuck in a debugging loop.
*   **Agent Logic Flaw:** The `strategy_advisor` agent provided incorrect advice (using DIG on an outdoor route). Agents must be given all relevant game mechanics to function correctly.
*   **Re-evaluate Route 29 Markers:** The 'Dead end (ledge north)' and 'Impassable NPC barrier' markers are likely incorrect results of my own pathing failures. Must revisit and verify.