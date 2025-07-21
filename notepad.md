# Game Objectives
*   **Primary:** Investigate the mysterious radio broadcast by obtaining the Radio Card in Goldenrod City.

# Side Quests & Rematches
*   **Camper Todd:** Wants a rematch on Route 34.

# Current Puzzle: Tohjo Falls
*   **Status:** Currently stuck on the entrance level. All paths are blocked by one-way ledges or impassable terrain, confirmed by `bfs_pathfinder`.
*   **Hypothesis 1:** The `WARP_CARPET_DOWN` at (13, 15) is the only way forward.
    *   **Test 1:** Stepping on the warp. **Result:** Failed.
    *   **Test 2:** Stepping on from above. **Result:** Failed.
    *   **Test 3:** Pressing 'A' on the warp while facing right. **Result:** Failed.
    *   **Next Test:** Press 'A' on the warp while facing up.
*   **Hypothesis 2:** It is possible to travel *down* `WATERFALL` tiles.
    *   **Status:** Untested. `bfs_pathfinder` reports the area above the waterfall is unreachable from my current position.

# Game Systems & Tools
*   **`bfs_pathfinder` Tool:** Recreated after accidental deletion. The tool appears to correctly handle basic navigation, wall collision, and one-way ledges for short paths. However, it has failed on longer, more complex paths, suggesting potential undiscovered bugs or map features it cannot parse. Its reliability is still under evaluation.
*   **`strategy_advisor` Agent:** The agent previously violated a core directive by suggesting fainting. Its system prompt has been refined to explicitly forbid this. It needs to be tested in a similar situation to confirm the fix.
*   **Future Agent Idea:** A `debugging_assistant` agent could be created to analyze tool code and debug logs to provide systematic suggestions for fixes.

# Tile Mechanics
*   **General:**
    *   `FLOOR`: Traversable.
    *   `TALL_GRASS`: Traversable, triggers wild encounters.
    *   `WALL`/`VOID`/`BUOY`: Impassable barriers.
    *   `WATER`: Requires SURF to traverse.
    *   `WATERFALL`: Traversable downwards (confirmed). Requires the Waterfall HM to ascend.
    *   `CAVE`/`WARP_CARPET_DOWN`: Warp points.
*   **One-Way Traversal:**
    *   `LEDGE_HOP_DOWN`: Can only be moved down from.
    *   `LEDGE_HOP_LEFT`: Can only be moved left from.
    *   `FLOOR_UP_WALL`: A one-way ledge. Can only be moved up from the tile below it; confirmed impassable from above, left, and right.

## Bag Mechanics
*   **Tossing Items:** To free up an inventory slot, you must toss the **entire stack** of an item (e.g., "Potion x5"). Tossing a single item from a stack (e.g., reducing it to "Potion x4") does not free up a slot.