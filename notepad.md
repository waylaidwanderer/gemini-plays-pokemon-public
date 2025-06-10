# Current Objectives
*   **Primary Goal:** Deliver OAK'S PARCEL to Professor Oak in Pallet Town.
*   **Secondary Goal:** Find the Viridian City Gym.
*   **Tertiary Goal:** Explore remaining unseen areas of Viridian City and its buildings.

# Event Triggers & Key Interactions
*   **Rival Battle 1 (Oak's Lab):** Triggered by attempting to leave the lab after receiving Pikachu and Oak's speech.
*   **Pikachu Following:** After the first rival battle, Oak mentions Pikachu dislikes Poké Balls. SPARKY will then follow.
*   **Town Map:** Obtained by interacting with the map object on the table in Rival's House.

# Lessons Learned
*   **Ledge Mechanics (CRITICAL - REVISED & REINFORCED):**
    *   Ledges are strictly ONE-WAY: you can only JUMP DOWN them.
    *   You CANNOT move UP onto a ledge from a lower Y-coordinate (e.g., from (X, Y+1) to (X,Y) if (X,Y) is a ledge).
    *   You CANNOT step onto the SIDE of a ledge if you are at a lower Y-coordinate than the ledge itself (e.g., from (X-1, Y) to (X,Y) if (X,Y) is a ledge and your current elevation is effectively below it).
    *   To bypass upward ledges, you MUST find a path AROUND them. This often means going significantly south, then using specific ground corridors or grass patches to ascend, then moving horizontally above the problematic ledges before jumping down.
*   The sign at (10,28) on Route 1 is IMPASSABLE and acts like a wall.
*   Route 1's easternmost strip (X=17-18, south of Y=24) is isolated by ledges from the south/west; access requires going far north on a main path and jumping down, or entering from Pallet Town and using the grass bypasses.
*   Follower Pokemon can block movement if approached from a non-facing direction, requiring an extra turn to step onto their tile.
*   **Potion Usage:** SPARKY is now regularly healed at Pokemon Centers. Potion usage is for emergencies or extended field exploration without access to a Center.

# Hard Mode Rules
*   Battle Style: Set.
*   No items in battle.
*   Level caps apply (Lt. Surge's cap is 24).

# Key Game Changes (ROM Hack)
*   HMs: Forgettable, usable from menu, not storable in PC.
*   All 151 Pokémon obtainable.
*   Trade evos by level.
*   Smarter AI, anti-sweep.
*   Tougher boss fights.
*   Dynamic scaling Gyms 4-6.
*   EXP. All available early.

# Route 1 - Ledge Navigation Strategy (MUST ADHERE - REVISED)
1.  **Identify Target Area:** Determine the general northern area to explore.
2.  **Find Valid Ascent Path:** From the southern part of Route 1 (e.g., near Pallet Town entrance at Y=36):
    *   **Option A (Western Corridors):** Navigate to columns X=7, X=8, or X=9. These columns have ground paths that bypass the Y=24 and Y=20 ledges. Proceed north along these columns. (Example: (9,29) -> (9,28) -> North)
    *   **Option B (Eastern Grass Bypass):** Navigate to the grass patches around (X=13-16, Y=23-Y=26). Use these to move north, bypassing the main Y=24 ledge system. (Example: (13,25) -> (13,24) -> (13,23) -> North)
    *   **Option C (Column 10 Northward Path - CRITICAL DETAIL):** Tile (10,20) is ground. From *south* of Y=20 (e.g., (10,21) or (10,20) itself after jumping down to it), proceed north along column 10. This path is clear up to Y=3. **DO NOT attempt to use this path by moving north from Y-coordinates higher than 20 (e.g., from (10,15) or (10,19)) as this will result in being blocked by ledges.**
3.  **Traverse North:** Once north of the major ledge systems (e.g., north of Y=20), you can navigate east/west to access all northern areas.
4.  **Explore by Descending:** Systematically jump down ledges to reveal unseen tiles and access isolated sections.
5.  **Verify EVERY step near a ledge against map memory.** Do not assume a path is clear.

# Agent Development Pipeline

## Active Agent Development: `ledge_navigator_agent`
*   **Status:** **CRITICALLY FLAWED - DO NOT USE.** Pathing logic for ledges is incorrect. Requires a complete system prompt rewrite. The new prompt must detail precise ledge mechanics (one-way down, no side-stepping from below, no ascending ledges) and instruct the agent to use its Python code tool to implement a pathfinding algorithm (e.g., A* or BFS variant) that respects these rules. **HIGHEST priority to fix or delete.**
*   **Input:** `{"type":"object","properties":{"start_x":{"type":"integer"},"start_y":{"type":"integer"},"end_x":{"type":"integer"},"end_y":{"type":"integer"}},"required":["start_x","start_y","end_x","end_y"]}`
*   **Output:** `{"type":"object","properties":{"path_found":{"type":"boolean"},"path":{"type":"array","items":{"type":"object","properties":{"x":{"type":"integer"},"y":{"type":"integer"}},"required":["x","y"]}}},"required":["path_found","path"]}`
*   **Capabilities:** Can run code.

## Agent Update Status: `exploration_planner`
*   **Status:** System prompt updated to better handle ledges. It now instructs the agent to suggest alternative approaches if direct paths are blocked by upward ledges and to remind the player to validate ledge traversal.

## Tabled Agent Ideas (Revisit Later):
*   `is_path_segment_valid_agent` (Discarded - scope too narrow, covered by improved ledge_navigator or manual check)
*   `wild_encounter_strategist_agent` (Discarded - too complex for current needs, manual strategy sufficient)

# Navigating within Northern Route 1 (Y < 20)
*If already north of the Y=20 ledge system (e.g., in the open area around Y=15-19) and needing to access areas further north (e.g. Y < 14, Y < 10, Y < 6):*
1.  **Eastern Ascent:** Move to the easternmost navigable column, which is X=18.
2.  **Proceed North:** Travel north along column X=18. This column is clear ground up to Y=6 (e.g., from (18,15) up to (18,6)).
3.  **Traverse West:** From (18,6) or (18,5), move west along row Y=6 or Y=5. These rows provide access to columns further west that lead to the northernmost parts of the map.
    *   Example path to (10,2) from (18,6): (18,6) -> (17,6) -> (16,6) -> (15,6) -> (15,5) -> (14,5) -> (13,5) -> (12,5) -> (11,5) -> (11,4) -> (11,3) -> (11,2) -> (10,2).

# Future Agent Ideas
*   `city_navigator_agent`: For pathfinding within cities, prioritizing key locations like Pokecenters, PokeMarts, and Gyms.
*   `item_finder_agent`: To scan map data for item balls and assist in pathing to them.
*   `npc_interaction_planner_agent`: Helps plan moves to correctly position for NPC interaction (adjacent and facing).
*   `map_analyzer_agent`: General purpose agent to query map XML for information like specific building locations or unvisited warps.
*   **Reminder:** Prioritize defining or discarding these agent ideas after initial Viridian City exploration.