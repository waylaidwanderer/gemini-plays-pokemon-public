# Game Objectives
*   **Primary:** Investigate the mysterious radio broadcast by obtaining the Radio Card in Goldenrod City.
*   **Secondary:** Retrieve the Rare Candy from Route 27 after clearing bag space.
*   **Tertiary:** Find a rematch with Schoolboy Alan on Route 36.

# Development Pipeline
*   **New Pathfinding Tool:** HIGHEST PRIORITY. Manual pathing is inefficient and error-prone. The new tool must be built from the ground up with rigorous testing, capable of navigating around static and dynamic obstacles. (STATUS: BUILT! Now testing.)

# Tile Mechanics Testing
*This section tracks experiments to understand how different tiles work.*

### Untested Hypotheses
*   **Hypothesis: `PC` tiles are impassable.**
    *   **Test:** Attempt to walk into a `PC` tile.
    *   **Status:** Untested.
*   **Hypothesis: `HEADBUTT_TREE` can be interacted with using the move Headbutt.**
    *   **Test:** Stand next to a `HEADBUTT_TREE` and use Headbutt from the party menu.
    *   **Status:** Untested.
*   **Hypothesis: `WARP_CARPET_DOWN` has specific entry requirements.**
    *   **Conclusion:** The warp at (17, 31) in Union Cave 1F seems to be a one-way exit from Route 33. Will test entry from the Route 33 side when possible.

### Verified Tile Mechanics
*   **Traversable:**
    *   `FLOOR`: Standard ground.
    *   `TALL_GRASS`: Triggers wild encounters.
*   **Requires HM/Interaction:**
    *   `WATER`: Requires SURF. Can only be entered by facing the tile and pressing 'A'.
    *   `CUT_TREE`: Impassable, but can be cleared with HM01 CUT.
    *   `CAVE`/`DOOR`/`STAIRCASE`/`LADDER`: Warp point.
*   **Impassable:**
    *   `VOID`: Standard barrier.
    *   `BUOY`: Confirmed impassable after attempting to move onto the tile at (27, 16).
    *   `ROOF`/`TV`: Impassable.
    *   `COUNTER`: Confirmed impassable after attempting to move onto the tile at (3, 2).
    *   `WALL`: Standard impassable tile.
*   **Special Interaction:**
    *   `FRUIT_TREE`: Can be interacted with by facing it and pressing 'A' to receive a BERRY.

*   **One-Way Traversal:**
    *   `LEDGE_HOP_DOWN`: Can only be moved down from.
    *   `LEDGE_HOP_LEFT`: Can only be moved left from.
    *   `FLOOR_UP_WALL`: Can only be entered by moving up from the tile below.

# Misc Notes & Reminders
*   **Bag is Full:** Cannot pick up the Rare Candy at (53, 12) on Route 27 until a slot is freed.
*   **Pending Rematch:** Fisher Ralph on Route 32.
*   **Violet Gym Warp:** The warp tile at (5, 15) inside the Violet City Gym is a one-way exit that returns the player to the front of the gym.

# Lessons Learned (Recent Failures)
*   **Pathfinding Failure:** My manual pathing is highly unreliable. My new `pathfinder` tool should solve this. An alternative hypothesis for pathing failures is a bug in long path execution, not just moving NPCs. Test with short, simple paths.
*   **Tool Hallucination:** I hallucinated a `bfs_pathfinder` tool. I must only rely on tools confirmed to be in my available tool list. I have removed the reference from my notes.

*   **Route 30 Failure:** My fixation on the western path after using CUT was a major failure in flexibility. I ignored repeated evidence that it was a dead end. I must be quicker to abandon a failed hypothesis.
*   **Route 30 Catastrophe:** My fixation on a northern path on the southern section of Route 30 was a massive failure. After dozens of failed attempts, I've confirmed the route is a one-way path south from the northern section. **Lesson: If a path repeatedly fails, don't just blame the execution or the tool; question the premise of the path itself. Trust the output of a reliable tool over a flawed assumption.**

*   **Route 46 Failure:** My `pathfinder` tool correctly determined there was no path north on Route 46. I failed to trust its output and assumed it was buggy. Route 46 is a one-way route south, filled with ledges. My assumption that this was the path to Violet City was a major strategic error. **Lesson: Trust my verified tools over my assumptions. If a path is not found, question the premise of the path itself, not just the tool's execution.**