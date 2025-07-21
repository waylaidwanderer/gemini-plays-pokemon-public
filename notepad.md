### D. Tool Development & Bugs
*   **bfs_pathfinder:** This tool is currently flawed. It does not correctly interpret one-way tiles like `LEDGE_HOP_DOWN` or `FLOOR_UP_WALL`, treating them as normal traversable tiles in any direction. This can cause it to fail to find a valid path or suggest an impossible one. It needs to be updated to account for tile-specific movement restrictions.

### E. Tool Development Bugs (Overwatch Feedback)
*   **`bfs_pathfinder`:** Still broken. The logic for one-way tiles is incorrect. Must be fixed before next use.
*   **`ice_puzzle_solver`:** Reported as unreliable. Needs to be tested, debugged, or deleted.
*   **`stun_npc`:** This tool was a hallucination and does not exist. Do not attempt to use it.