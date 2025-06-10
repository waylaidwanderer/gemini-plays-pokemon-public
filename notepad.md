# Current Objectives
*   **Primary Goal:** Obtain the Boulder Badge from the Pewter City Gym Leader, Brock.
*   **Secondary Goal:** Travel to Pewter City via Route 2 and Viridian Forest.
*   **Tertiary Goal:** Catch new Pokémon species encountered on Route 2 and in Viridian Forest to progress the Pokédex.

# Event Triggers & Key Interactions
*   **Rival Battle 1 (Oak's Lab):** Triggered by attempting to leave the lab after receiving Pikachu and Oak's speech.
*   **Pikachu Following:** After the first rival battle, Oak mentions Pikachu dislikes Poké Balls. SPARKY will then follow.
*   **Town Map:** Rival SPB mentioned he'd get one from his sister and tell her not to lend one to me. I should check Rival's house in Pallet Town for a Town Map.
*   **Oak's Parcel:** Obtained from the Viridian City PokeMart clerk. Delivered to Professor Oak.
*   **Pokédex:** Obtained from Professor Oak after delivering the parcel. Mission is to complete it.

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

# General Ledge Navigation Principles
*   **Problem:** Ledges block upward movement.
*   **Strategy:** To bypass upward ledges, you MUST find a path AROUND them. This often means going significantly south/west/east of the ledges, then using clear ground corridors or specific patches (like grass if it allows passage) to ascend to a higher elevation. Once above the problematic ledges, navigate laterally and then descend ledges as needed to reach the target area. Always verify ledge properties in map memory and visually inspect the screen. Critically evaluate agent-provided paths for ledge issues.

# Agent Development Pipeline

## Active Agents
*   `exploration_planner`: Analyzes map XML and reachable unseen tiles for efficient exploration. Player must critically evaluate paths for ledge issues.
*   `map_analyzer_agent`: Analyzes map XML to answer specific questions. (Untested)

# Future Agent Ideas
(Section cleared for now to focus on main objectives and existing agent refinement.)

# Map Discoveries
*   **Pallet Town:** There's a reachable, undiscovered map connection to the south at (4,18) or (3,18). Worth investigating later.