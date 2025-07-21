# Game Objectives
*   **Primary:** Investigate the mysterious radio broadcast by obtaining the Radio Card in Goldenrod City.

# Side Quests & Rematches
*   **Camper Todd:** Wants a rematch on Route 34.

# Current Hypotheses & Investigations
*   **Route 29 Navigation:** My Fly was glitched, dropping me on the southern path of Route 29. My current hypothesis is that this entire southern section is a one-way path forcing eastward travel towards New Bark Town due to numerous ledges. All attempts to find a path west back to Cherrygrove have failed. The current plan is to complete the long detour through New Bark Town.
*   **`bfs_pathfinder` Tool Bug:** The tool has repeatedly failed, generating invalid paths that ignore one-way ledges.
    *   **Hypothesis 1:** The `is_valid_move` function logic is still flawed, despite multiple attempts to fix it. It might be misinterpreting specific ledge interactions.
    *   **Hypothesis 2:** I might be providing incorrect start/end coordinates, causing the tool to fail. (Tested and corrected, but the tool still failed).
    *   **Hypothesis 3:** The tool is not correctly parsing the map XML, leading to an inaccurate internal representation of the map.
    *   **Status:** The tool is currently unreliable and abandoned in favor of manual navigation until it can be definitively fixed.
*   **`strategy_advisor` Agent Flaw:** The agent suggested fainting the party as a solution to being stuck, a violation of core directives.
    *   **Action Taken:** Refined the agent's system prompt to explicitly forbid this strategy. The agent needs to be tested again in a similar situation to confirm the fix.

# Tile Mechanics
*   **General:**
    *   `FLOOR`: Standard traversable ground.
    *   `TALL_GRASS`: Traversable, triggers wild encounters.
    *   `HEADBUTT_TREE`: Impassable barrier.
    *   `WALL`: Impassable barrier.
    *   `VOID`: Impassable barrier, represents out-of-bounds areas.
*   **One-Way Traversal:**
    *   `LEDGE_HOP_DOWN`: Can only be moved down from the tile above it.
*   `WATER`: Requires SURF to traverse.