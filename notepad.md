# Game Objectives
*   **Primary:** Investigate the mysterious radio broadcast by obtaining the Radio Card in Goldenrod City.

# Side Quests & Rematches
*   **Camper Todd:** Wants a rematch on Route 34.

# Current Puzzle: Tohjo Falls
*   **Status:** Stuck on the lower level after coming down the waterfall.
*   **Hypothesis 1 (Failed):** The western island contains the path forward. **Result:** Dead end. Path is blocked by a MOON STONE I cannot pick up because my bag is full and the 'TOSS' command appears to be non-functional.
*   **Hypothesis 2 (Failed):** The `WARP_CARPET_DOWN` at (13, 15) is the exit. **Result:** The warp is unresponsive to all attempts to activate it.
*   **Current Hypothesis:** There is a hidden path behind the waterfall.

# Game Systems & Tools
*   **`bfs_pathfinder` Tool:** Appears to work for basic navigation but has failed on complex paths. Reliability is still under evaluation.
*   **`strategy_advisor` Agent:** Its system prompt was refined to forbid suggesting fainting. Needs to be tested to confirm the fix.
*   **Future Agent Idea:** A `debugging_assistant` agent could be created to analyze tool code and debug logs to provide systematic suggestions for fixes.

# Tile Mechanics
*   **General:**
    *   `FLOOR`: Traversable.
    *   `TALL_GRASS`: Traversable, triggers wild encounters.
    *   `WALL`/`VOID`/`BUOY`: Impassable barriers.
    *   `WATER`: Requires SURF to traverse.
    *   `WATERFALL`: Traversable downwards. Requires the Waterfall HM to ascend.
    *   `CAVE`: Warp point.
    *   `WARP_CARPET_DOWN`: Warp point. Note: The one at Tohjo Falls (13, 15) is unresponsive.
*   **One-Way Traversal:**
    *   `LEDGE_HOP_DOWN`: Can only be moved down from.
    *   `LEDGE_HOP_LEFT`: Can only be moved left from.
    *   `FLOOR_UP_WALL`: A one-way ledge. Can only be moved up from the tile below it.

## Bag Mechanics
*   **Tossing Items (Under Investigation):** My attempts to toss items to free an inventory slot have all failed, regardless of item, stack size, or bag pocket. The 'TOSS' function may be bugged or have a very specific, undiscovered condition for use. My hypothesis that the entire stack must be tossed was not validated.