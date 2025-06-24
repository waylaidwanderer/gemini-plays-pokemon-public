# Gem's Strategic Journal (v100 - Post-Critique)

## I. Core Principles & Lessons Learned
- **Trust the Data, Not Frustration:** Game State Information (`map_id`, `current_position`) is the absolute source of truth. My own feeling of being "stuck" is a hallucination if the data contradicts it. ALWAYS verify location after a map transition BEFORE acting.
- **Interaction Protocol:** If an interaction doesn't trigger a battle, it's a non-battling NPC or one I've already defeated. Do not repeat the interaction; mark the NPC and move on. An NPC blocking a path that doesn't battle is a hard wall.
- **WKG & Marker Protocol (v22 - CRITICAL REVISION):**
    - **CRITICAL FLAW (T23189-T23248):** My manual, multi-turn process for WKG updates is extremely error-prone and has led to multiple wasted turns. This is unacceptable.
    - **CORRECTIVE ACTION:** The #1 priority is the development of a new `wkg_manager_agent` to handle the entire transaction atomically. All other goals are secondary until this is fixed.
    - **Marker Diligence:** I must re-issue failed `define_map_marker` calls and be diligent about marking key points (like warp arrivals and defeated trainers) *immediately*. This is a recurring failure I need to fix.
- **Agent Usage:** Use `team_composition_advisor_agent` *before* entering challenging areas. Use `stealth_pathfinder_agent` for all non-trivial navigation. Use agents proactively.

## II. Hallucination & Correction Log
- **CRITICAL (T23189-T23248): WKG Management Failure.** Multiple consecutive turns wasted attempting to add WKG nodes/edges due to a flawed understanding of the toolchain. **Lesson:** I MUST follow the correct, sequential process for WKG updates and prioritize the development of the `wkg_manager_agent`.
- **CRITICAL (T23249-Present): Map Data Hallucination.** Repeatedly failed to acknowledge the correct number of reachable unseen tiles on Pokémon Tower floors, despite system warnings. **Lesson:** I must trust the game state data and correct my internal map understanding immediately when a discrepancy is found.
- **Player Hallucination (T23161):** Incorrectly logged that ECHO (Golbat) was a GHOST type. This was a misinterpretation of game data. Golbat's typing is Poison/Flying. **Corrected.**

## III. Game Mechanics & Battle Intel
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Field Use:** HMs MUST be taught to a compatible Pokémon to enable their field use. FLY cannot be used indoors.
- **EXP. All:** Distributes EXP to all non-fainted party members. Pokémon at the level cap will not gain actual EXP.

## IV. Action Plans & Hypotheses
### Current Plan (v39 - Pokémon Tower 5F Battle)
*   **Objective:** Defeat the Channeler at (18, 8) to clear a path for exploration.
*   **Method:**
    1.  Use SPARKY's turn to paralyze the Haunter with Thunder Wave, even if it means SPARKY faints.
    2.  Bring in the next best Pokémon to finish the job.
    3.  **IMMEDIATELY** mark the Channeler as defeated post-battle.
    4.  Heal at the earliest opportunity after clearing this floor or if the party becomes too weak to continue.

### Future Plans & Hypotheses
- **Hypothesis 1 (Celadon Gym):** The gym might be un-bugged now that the Rocket Hideout is cleared. Will investigate after Pokémon Tower.
- **Hypothesis 2 (Thirsty Guards):** Need to test if giving a guard a drink (e.g., Fresh Water) will grant passage to Saffron City.
- **Hypothesis 3 (Snorlax):** The Snorlax on Route 16 requires the Poké Flute. Mr. Fuji is the most likely source after he is rescued from the Pokémon Tower.

## V. Completed Intel & Disproven Hypotheses
- **LIFT KEY Location:** Dropped by a non-battling Rocket Grunt at Rocket Hideout B3F (11, 23).
- **Giovanni Defeated:** Defeated Giovanni on Rocket Hideout B4F. He dropped the Silph Scope.
- **Rival Pixel Defeated:** Defeated Pixel on Pokémon Tower 2F.
- **Non-Battling NPC (Pokémon Tower 2F):** The Channeler at (4,8) is not a trainer and just provides dialogue.
- **Defeated Channeler (Pokémon Tower 4F):** Defeated Channeler at (7,11).

## VI. Agent Development Plan (Consolidated & Updated)
- **(CRITICAL PRIORITY #1): `wkg_manager_agent`:** Design and implement a new, robust agent to handle the entire WKG update transaction in a single call. It must be able to call `add_node` twice, capture the returned IDs, and then call `add_edge` with those IDs. This will prevent the manual data entry errors I've been making.
- **(HIGH PRIORITY): `team_composition_advisor_agent` Refinement:** Add precise EXP calculation logic to enhance its training plan recommendations.
- **(Future Idea): `shopping_planner_agent`:** Create an agent to calculate costs for items (especially TMs) and create shopping lists based on my money and priorities.
- **(Future Idea): `item_finder_agent`:** Create an agent that scans the map XML for Poké Ball sprites and plans a path to collect them, avoiding trainers.