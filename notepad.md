# Current Objectives
*   **Primary Goal:** Obtain the Boulder Badge from the Pewter City Gym Leader, Brock.
*   **Secondary Goal:** Navigate Viridian Forest to reach Pewter City.
*   **Tertiary Goal:** Catch new Pokémon species encountered in Viridian Forest to progress the Pokédex.

# Event Triggers & Key Interactions
*   **Rival Battle 1 (Oak's Lab):** Triggered by attempting to leave the lab after receiving Pikachu and Oak's speech.
*   **Pikachu Following:** After the first rival battle, Oak mentions Pikachu dislikes Poké Balls. SPARKY will then follow.
*   **Town Map:** Rival SPB mentioned he'd get one from his sister and tell her not to lend one to me. I should check Rival's house in Pallet Town for a Town Map.
*   **Oak's Parcel:** Obtained from the Viridian City PokeMart clerk. Delivered to Professor Oak.
*   **Pokédex:** Obtained from Professor Oak after delivering the parcel. Mission is to complete it.
*   **Viridian City Old Man (Coffee):** Blocks path west to Route 22. After dialogue about coffee, he moves and offers a catching tutorial (failed).

# Lessons Learned
*   **Ledge Mechanics (CRITICAL - REVISED & REINFORCED):**
    *   Ledges are strictly ONE-WAY: you can only JUMP DOWN them.
    *   You CANNOT move UP onto a ledge from a lower Y-coordinate.
    *   You CANNOT step onto the SIDE of a ledge if you are at a lower Y-coordinate than the ledge itself.
    *   To bypass upward ledges, you MUST find a path AROUND them. This often means going significantly south/west/east, then using specific ground corridors or grass patches to ascend, then moving horizontally above the problematic ledges before jumping down.
*   The sign at (10,28) on Route 1 is IMPASSABLE and acts like a wall.
*   Follower Pokemon can block movement if approached from a non-facing direction, requiring an extra turn to step onto their tile.
*   **Potion Usage:** SPARKY is now regularly healed at Pokemon Centers. Potion usage is for emergencies or extended field exploration without access to a Center.
*   **Map Connections:** ALWAYS double-check the *direction* (North, South, East, West) and *destination* of a map connection in the Game State Information before committing to a route. A wrong turn can lead to significant detours (e.g., Route 22 instead of Route 2).

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

# General Ledge Navigation Principles
*   **Problem:** Ledges block upward movement.
*   **Strategy:** To bypass upward ledges, find a path AROUND. Move away from the ledges (laterally or downwards) to find a clear corridor or grass patch allowing ascent *above* the problematic ledges. Then, navigate laterally above and descend as needed. Verify ledge properties in map memory and visually inspect. Critically evaluate agent-provided paths for ledge issues.
*   **Agent Use for Ledges:** If manual pathing or `exploration_planner` struggles with complex verticality/blockages by ledges, consider using `map_analyzer_agent` to query for clear paths or alternative exits (e.g., 'Find a path from (X,Y) to (A,B) avoiding upward ledges').

# Agent Development Pipeline

## Active Agents
*   `exploration_planner`: Analyzes map XML and reachable unseen tiles for efficient exploration. Player must critically evaluate paths for ledge issues.
*   `map_analyzer_agent`: Analyzes map XML to answer specific questions. (Needs testing - prioritize finding a use case or consider deletion if unused for too long).

## Future Agent Ideas
*   **Trainer Battle Strategist:** Input: current party, enemy trainer's visible Pokémon (if any), current battle state. Output: suggested moves, switch-ins. (Might be complex to define well with limited initial info).
*   **Resource Management Agent:** Tracks Potion usage, PP, and advises when to return to a Pokémon Center or be cautious with resources.

# Map Discoveries
*   **Pallet Town:** Reachable, undiscovered map connection south at (4,18) or (3,18).
*   **Viridian City:** The Old Man tutorial for catching Pokémon opens the path to Route 22 (West), NOT Route 2 (North).

# Critical Route Information
*   **Route 2 (NORTH of Viridian City):** Leads to Viridian Forest, then Pewter City (Brock). THIS IS THE CORRECT PATH.
*   **Route 22 (WEST of Viridian City):** Leads to the Pokemon League. THIS IS A DETOUR if aiming for Pewter City.

# Active Pathing Notes & Strategies
*   **Ledge Bypass (General):** When faced with upward ledges, always look for a route *around* them. This usually involves moving significantly away from the ledge (laterally or downwards) to find a clear corridor or grass patch that allows ascent to a higher elevation *above* the problematic ledges. Then, navigate laterally above the ledges before descending.
*   **Agent Usage for Complex Paths:** If manual pathing to an objective (unseen tile, warp, item) is blocked more than once, use the `exploration_planner` agent. Critically review agent paths for ledge issues before execution.
*   **Map Analyzer Agent Reminder:** Evaluate the `map_analyzer_agent` for a specific, immediate use case. Proactively use `map_analyzer_agent` to confirm exits or locate key features before long travel sequences, especially when leaving a city or entering a complex new area. If it remains unused, consider deleting it to free up an agent slot.

# Viridian Forest Notes
*   (Track trainers, items, and path through here)

# Lessons Learned
*   **Trainer Battle Initiation (CRITICAL):** Battles are primarily triggered by entering a trainer's direct line of sight. Observe their facing direction and move onto a tile directly in front of them. Repeatedly pressing 'A' or trying to step on their tile when not in their LoS is ineffective.

# Viridian Forest Notes
*   Youngster at (17,44) - initial battle.

# Active Pathing Notes & Strategies
*   Proactively use `map_analyzer_agent` for pathing queries or locating features if manual pathing becomes difficult or when entering complex new areas. If it remains unused after a few more sessions, consider deleting it.