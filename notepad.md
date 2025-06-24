# Gem's Strategic Journal (v97 - Post-Critique)

## I. Core Principles & Lessons Learned
- **Trust the Data, Not Frustration:** Game State Information (`map_id`, `current_position`) is the absolute source of truth. My own feeling of being "stuck" is a hallucination if the data contradicts it. ALWAYS verify location after a map transition BEFORE acting.
- **Interaction Protocol:** If an interaction doesn't trigger a battle, it's a non-battling NPC or one I've already defeated. Do not repeat the interaction; mark the NPC and move on. An NPC blocking a path that doesn't battle is a hard wall.
- **WKG & Marker Protocol (v19 - REVISED):**
    - **CRITICAL FLAW IDENTIFIED:** The manual, multi-step process for WKG updates is extremely error-prone and has led to multiple wasted turns. A new `wkg_manager_agent` MUST be developed to handle the entire transaction atomically (add node 1, get ID, add node 2, get ID, add edge with correct IDs). This is my top development priority.
    - **TEMPORARY WORKAROUND:** Until the agent is ready, I must manually perform the WKG update in three separate, sequential turns, parsing the output of each `add_node` call to retrieve the ID for the subsequent `add_edge` call. I will use `run_code` to retrieve existing node IDs before attempting to add new ones to avoid errors.
    - **Marker Diligence:** I must re-issue failed `define_map_marker` calls to ensure critical information (like warp arrival points) is always logged.
- **Agent Usage:** Use `team_composition_advisor_agent` *before* all major battles. Use `stealth_pathfinder_agent` for all non-trivial navigation. Use agents proactively.
- **Repeated Failure Protocol:** If a plan fails, recognize the pattern, log it, and pivot to a new strategy instead of wasting turns.

## II. Hallucination & Correction Log
- **CRITICAL (T23189-T23201): WKG Management Failure.** Multiple consecutive turns wasted attempting to add WKG nodes/edges due to a flawed understanding of the toolchain (using placeholder IDs, adding existing nodes, providing incomplete payloads). This highlights a severe lack of diligence. **Lesson:** I MUST follow the correct, sequential process for WKG updates and prioritize the development of the `wkg_manager_agent` to automate this.
- **CRITICAL (T22833-22848): WKG Management Failure.** Wasted 15 turns on a non-existent WKG issue due to repeated user error (improperly formatted agent input). Blamed the tool instead of my own mistake. **Lesson:** I MUST read tool documentation carefully and trust the system's data.
- **CRITICAL (T22742, T22763): WKG Data Integrity Failure.** Twice violated the `destination_entry_point` rule. This is a severe lack of diligence. **Lesson:** I MUST use an agent for all future WKG updates and meticulously verify data. No more manual entries.
- **MAJOR (T22612-T22613): Lavender Pokecenter Pathing Hallucination.** Attempted to pathfind in Lavender Town while still inside the Pokémon Center. **Lesson:** ALWAYS verify `map_id` and `current_position` *after* any action intended to change maps.
- **Player Hallucination (T23161):** Incorrectly logged that ECHO (Golbat) was a GHOST type. This was a misinterpretation of game data. Golbat's typing is Poison/Flying. **Corrected.**

## III. Game Mechanics & Battle Intel
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Field Use:** HMs MUST be taught to a compatible Pokémon to enable their field use. FLY cannot be used indoors.
- **EXP. All:** Distributes EXP to all non-fainted party members. Pokémon at the level cap will not gain actual EXP.

## IV. Action Plans & Hypotheses
### Current Plan (v36 - Pokémon Tower 5F Exploration)
*   Objective: Clear the 5th floor and continue ascending the Pokémon Tower.
*   Method:
    1.  Explore the floor systematically, using the `stealth_pathfinder_agent` to navigate around trainers.
    2.  Use the `battle_advisor_agent` for all trainer and wild battles.
    3.  Lead with a strong Pokémon to handle random encounters more efficiently.

### Future Plans & Hypotheses
- **Hypothesis 1 (Celadon Gym):** The gym might be un-bugged now that the Rocket Hideout is cleared. Will investigate after Pokémon Tower.
- **Hypothesis 2 (Thirsty Guards):** Need to test if giving a guard a drink (e.g., Fresh Water) will grant passage to Saffron City.
- **Hypothesis 3 (Snorlax):** The Snorlax on Route 16 requires the Poké Flute. Mr. Fuji is the most likely source after he is rescued from the Pokémon Tower.

## V. Completed Intel & Disproven Hypotheses
- **LIFT KEY Location:** Dropped by a non-battling Rocket Grunt at Rocket Hideout B3F (11, 23).
- **Giovanni Defeated:** Defeated Giovanni on Rocket Hideout B4F. He dropped the Silph Scope.
- **Rival Pixel Defeated:** Defeated Pixel on Pokémon Tower 2F.
- **Non-Battling NPC (Pokémon Tower 2F):** The Channeler at (4,8) is not a trainer and just provides dialogue.

## VI. Agent Development Plan (Consolidated & Updated)
- **(CRITICAL PRIORITY):** Design and implement a new, robust `wkg_manager_agent`. This agent's purpose is to handle the entire WKG update transaction in a single call, preventing the manual data entry errors I've been making. It needs to be able to call `add_node` twice, capture the returned IDs, and then call `add_edge` with those IDs.
- **(HIGH PRIORITY):** Consolidate the logic from the deleted `exp_tracker_agent` into the `team_composition_advisor_agent`. The team advisor already handles training plans, so adding precise EXP calculation is a natural extension.
- **(Future Idea):** Create a `shopping_planner_agent` to calculate costs for items (especially TMs) and create shopping lists based on my money and priorities.
- **(Future Idea):** Create an `item_finder_agent` that scans the map XML for Poké Ball sprites and plans a path to collect them, avoiding trainers.