# Current Objectives
*   **Primary Goal:** Deliver OAK'S PARCEL to Professor Oak in Pallet Town.
*   **Secondary Goal:** Find the Viridian City Gym.
*   **Tertiary Goal:** Explore remaining unseen areas of Viridian City and its buildings.

# Event Triggers & Key Interactions
*   **Rival Battle 1 (Oak's Lab):** Triggered by attempting to leave the lab after receiving Pikachu and Oak's speech.
*   **Pikachu Following:** After the first rival battle, Oak mentions Pikachu dislikes Poké Balls. SPARKY will then follow.
*   **Town Map:** Obtained by interacting with the map object on the table in Rival's House.
*   **Oak's Parcel:** Obtained from the Viridian City PokeMart clerk.

# Lessons Learned
*   **Ledge Mechanics (CRITICAL - REVISED & REINFORCED):**
    *   Ledges are strictly ONE-WAY: you can only JUMP DOWN them.
    *   You CANNOT move UP onto a ledge from a lower Y-coordinate (e.g., from (X, Y+1) to (X,Y) if (X,Y) is a ledge).
    *   You CANNOT step onto the SIDE of a ledge if you are at a lower Y-coordinate than the ledge itself (e.g., from (X-1, Y) to (X,Y) if (X,Y) is a ledge and your current elevation is effectively below it).
    *   To bypass upward ledges, you MUST find a path AROUND them. This often means going significantly south/west/east, then using specific ground corridors or grass patches to ascend, then moving horizontally above the problematic ledges before jumping down.
*   The sign at (10,28) on Route 1 is IMPASSABLE and acts like a wall.
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

# Route 1 - General Ledge Navigation Principles
*   **Goal:** Access northern areas of Route 1 from the south (e.g., Pallet Town entrance).
*   **Strategy:** Identify clear northward paths (e.g., ground corridors like X=7-9, X=10 from Y<=20, or eastern grass patches) to bypass major ledge systems (Y=24, Y=20). Once north of these, navigate laterally and descend ledges as needed. Always verify ledge properties in map memory.

# Agent Development Pipeline

## Agent Update Status: `exploration_planner`
*   **Status:** System prompt updated to better handle ledges. It now instructs the agent to suggest alternative approaches if direct paths are blocked by upward ledges and to remind the player to validate ledge traversal. Player must still critically evaluate paths for ledge issues.

# Future Agent Ideas (To Be Implemented or Discarded)
*   `map_analyzer_agent`: General purpose agent to query map XML for information like specific building locations or unvisited warps. (Priority: Define next)
*   `city_navigator_agent`: For pathfinding within cities, prioritizing key locations like Pokecenters, PokeMarts, and Gyms. (Lower priority)
*   `item_finder_agent`: To scan map data for item balls and assist in pathing to them. (Lower priority)
*   `npc_interaction_planner_agent`: Helps plan moves to correctly position for NPC interaction (adjacent and facing). (Lower priority)