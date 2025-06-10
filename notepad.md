# Current Objectives
*   **Primary Goal:** Obtain the Boulder Badge from the Pewter City Gym Leader, Brock.
*   **Secondary Goal:** Navigate Viridian Forest to reach Pewter City by exploring all remaining reachable unseen areas and collecting items.
*   **Tertiary Goal:** Defeat remaining trainers in Viridian Forest.

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
*   **Trainer Battle Initiation (CRITICAL):** Battles are primarily triggered by entering a trainer's direct line of sight. Observe their facing direction and move onto a tile directly in front of them. Repeatedly pressing 'A' or trying to step on their tile when not in their LoS is ineffective. Dialogue loops can sometimes be broken with 'B' or by moving away. Non-battling NPCs may still have trainer sprites.
*   **Exploration Planner Paths:** If the `exploration_planner` provides a very long or scattered path, consider breaking it into smaller, logical segments or re-running the planner after a short manual move to a new area. This can lead to more manageable and efficient exploration.

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

# Agent Development & Pathing Notes
## Active Agents
*   `exploration_planner`: Analyzes map XML and reachable unseen tiles for efficient exploration.
    *   **Lesson Reinforced (Turn 961, 979, 982):** ALWAYS provide the *complete and exact* list of 'Reachable Unseen Tiles' from the Game State Information. Double-check input.
*   `map_analyzer_agent`: Analyzes map XML to answer specific questions. (Use more actively for pathing issues when `run_code` script fails or for complex manual navigation planning. Could have helped around (26,28) blockage.)
## Planned Agents (URGENT - DEFINE ASAP)
*   `pathing_script_analyzer_agent`: To debug and optimize the `run_code` pathing script, or explain failures. (**CRITICAL PRIORITY** - Define ASAP due to persistent script failures.)
*   `battle_strategist_agent`: To assist with Hard Mode boss fight planning.
## Pathing Script (`run_code`) Behavior (**MAJOR & PERSISTENT ISSUE - CONSOLIDATED**)
*   The `run_code` script for path generation has shown **EXTREME unreliability** (Turns 983, 990, 992, 993, 1006, 1007, 1009, 1010, 1017, 1024, 1025, 1026, and many others).
    *   It frequently produces insufficient/incorrect move lists, gets blocked by simple obstacles (walls, Pikachu), misinterprets facing/position, or generates paths into impassable tiles.
    *   **Current Strategy (REINFORCED):** AVOID using this script for long or complex paths. Prioritize **MANUAL NAVIGATION** or use the script **ONLY for very short, easily verifiable segments (1-5 steps)**. Break down `exploration_planner` paths into tiny chunks if attempting script use.
    *   The `pathing_script_analyzer_agent` is crucial for addressing these deficiencies. Repeatedly re-running the script without understanding the failure is inefficient.

# Map Discoveries
*   **Pallet Town:** Reachable, undiscovered map connection south at (4,18) or (3,18).
*   **Viridian City:** The Old Man tutorial for catching Pokémon opens the path to Route 22 (West), NOT Route 2 (North).

# Critical Route Information
*   **Route 2 (NORTH of Viridian City):** Leads to Viridian Forest, then Pewter City (Brock). THIS IS THE CORRECT PATH.
*   **Route 22 (WEST of Viridian City):** Leads to the Pokemon League. THIS IS A DETOUR if aiming for Pewter City.

# Viridian Forest Notes
*   Youngster (ID 1, VIRIDIANFOREST_YOUNGSTER1) at (17,44): Encountered dialogue loop. `map_analyzer_agent` (Turn 877) confirmed this trainer blocks the direct path north and cannot be bypassed. Battle is likely mandatory.
*   Youngster (ID 10, VIRIDIANFOREST_YOUNGSTER6) at (28,41): Confirmed non-battling NPC. Dialogue: "You should carry extras!". Blocks direct westward movement along row 41. The tile (28,41) is non-navigable.
*   Bug Catcher (ID 3, VIRIDIANFOREST_YOUNGSTER3) at (28,20): **Defeated**.
*   Items Collected:
    *   Potion at (26,12) - Collected (Turn 981).

# Battle Notes
*   Record insights for specific Pokémon/trainers, especially Hard Mode implications.
*   SPARKY learned TAIL WHIP, replacing GROWL at Lv11 (Turn 1004).

# Pewter City Prep
*   Find out Brock's Ace level / level cap for Hard Mode.
*   Plan party composition/training for Brock.