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
*   **Potion Usage (REVISED):** SPARKY should be healed with Potions proactively outside of battle if HP is low and a Pokémon Center isn't immediately accessible, especially before engaging trainers or exploring deep into an area. Relying solely on Pokémon Centers for healing can lead to blackouts if unexpected battles occur or poison takes its toll.
*   **Map Connections:** ALWAYS double-check the *direction* (North, South, East, West) and *destination* of a map connection in the Game State Information before committing to a route. A wrong turn can lead to significant detours (e.g., Route 22 instead of Route 2).
*   **Trainer Battle Initiation (CRITICAL):** Battles are primarily triggered by entering a trainer's direct line of sight. Observe their facing direction and move onto a tile directly in front of them. Repeatedly pressing 'A' or trying to step on their tile when not in their LoS is ineffective. Dialogue loops can sometimes be broken with 'B' or by moving away. Non-battling NPCs may still have trainer sprites.
*   **Exploration Planner Paths:** If the `exploration_planner` provides a very long or scattered path, consider breaking it into smaller, logical segments or re-running the planner after a short manual move to a new area. This can lead to more manageable and efficient exploration.
*   **Type Matchups (CRITICAL REMINDER):** Pay closer attention to type matchups. Electric-type moves (like THUNDERSHOCK) are NOT VERY EFFECTIVE against Grass/Poison types like Oddish. This was a critical error leading to SPARKY taking unnecessary damage and getting poisoned.
*   **Status Conditions (Poison):** Poison is a serious threat in Hard Mode, especially with no in-battle items. If SPARKY gets poisoned, prioritize reaching a Pokémon Center or using an Antidote (if available) ASAP. Do not continue to battle or explore extensively while poisoned, as the damage accumulates quickly and can lead to fainting.

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

# Agent Development & Pathing Strategy (**REVISED POST-CRITIQUE & BLACKOUT**)
## Active Agents
*   `exploration_planner`: Analyzes map XML and reachable unseen tiles for efficient exploration. (Continue using, but break down long paths. Ensure Pikachu's health is stable before long explorations.)
*   `map_analyzer_agent`: Analyzes map XML to answer specific questions. (Use proactively for navigation issues, pathfinding queries if stuck, or understanding blockages.)
*   `pathing_script_analyzer_agent`: Analyzes pathing scripts. (**HIGHEST PRIORITY AFTER STABILIZING CURRENT SITUATION:** Use this agent to diagnose and fix the `run_code` pathing script. Do NOT use the `run_code` pathing script for anything beyond 1-2 manual steps until this analysis is complete and fixes are implemented.)
## Planned Agents
*   `battle_strategist_agent`: To assist with Hard Mode boss fight planning. (Define after current critical issues are resolved and Viridian Forest is cleared, or if stuck on a major trainer.)
## Pathing Script (`run_code`) Behavior (**CRITICAL - DO NOT USE UNTIL FIXED - IMMEDIATE ACTION REQUIRED**)
*   The `run_code` script for path generation is **FUNDAMENTALLY FLAWED** and **UNRELIABLE**.
    *   **NEW STRATEGY (MANDATORY):** **DO NOT USE THIS SCRIPT for any path longer than 1-2 easily verifiable steps.** Prioritize **MANUAL NAVIGATION**. If stuck, use `map_analyzer_agent` to query for paths.
    *   **IMMEDIATE NEXT STEP AFTER REACHING VIRIDIAN FOREST SOUTH GATE:** Use the `pathing_script_analyzer_agent` to diagnose and begin fixing the `run_code` pathing script. This is the **HIGHEST PRIORITY** after ensuring immediate safety and access to a stable location (like the gatehouse). All agent development is secondary to ensuring SPARKY's safety and fixing this script.

# Map Discoveries
*   **Pallet Town:** Reachable, undiscovered map connection south at (4,18) or (3,18).
*   **Viridian City:** The Old Man tutorial for catching Pokémon opens the path to Route 22 (West), NOT Route 2 (North).

# Critical Route Information
*   **Route 2 (NORTH of Viridian City):** Leads to Viridian Forest, then Pewter City (Brock). THIS IS THE CORRECT PATH.
*   **Route 22 (WEST of Viridian City):** Leads to the Pokemon League. THIS IS A DETOUR if aiming for Pewter City.

# Viridian Forest Notes
*   Youngster (ID 1, VIRIDIANFOREST_YOUNGSTER1) at (17,44): Confirmed non-battling NPC after direct interaction. Path north appears to be around this NPC via (16,44) or (18,44).
*   Youngster (ID 10, VIRIDIANFOREST_YOUNGSTER6) at (28,41): Confirmed non-battling NPC. Dialogue: "You should carry extras!". Blocks direct westward movement along row 41.
*   Bug Catcher (ID 3, VIRIDIANFOREST_YOUNGSTER3) at (28,20): **Defeated**.
*   Items Collected:
    *   Potion at (26,12) - Collected (Turn 981).

# Battle Notes
*   SPARKY learned TAIL WHIP, replacing GROWL at Lv11 (Turn 1004).
*   Defeated by Bug Catcher (ID: VIRIDIANFOREST_YOUNGSTER5) at (17,18) in Viridian Forest after its Caterpie and Metapod. SPARKY fainted due to poison and accumulated damage, resulting in a blackout. Returned to Viridian City Pokemon Center. (Turn 1104)

# Pewter City Prep
*   Find out Brock's Ace level / level cap for Hard Mode.
*   Plan party composition/training for Brock.

*   **Horizontal Ledge Movement (AI Critique):** The AI noted that assuming one can step horizontally onto a ledge from an adjacent ground tile at the same Y-level is generally a flawed assumption, even if specific map data shows `navigable="true"`. It's better to verify this on a case-by-case basis and be cautious about general ledge traversal rules.