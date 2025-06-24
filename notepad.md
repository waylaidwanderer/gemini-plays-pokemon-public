# Gem's Strategic Journal (v94 - Post-Critique)

## I. Core Principles & Lessons Learned
- **Trust the Data, Not Frustration:** Game State Information (`map_id`, `current_position`) is the absolute source of truth. My own feeling of being "stuck" is a hallucination if the data contradicts it. ALWAYS verify location after a map transition BEFORE acting.
- **Interaction Protocol:** If an interaction doesn't trigger a battle, it's a non-battling NPC or one I've already defeated. Do not repeat the interaction; mark the NPC and move on. An NPC blocking a path that doesn't battle is a hard wall.
- **WKG & Marker Protocol (v16):**
    - After any map transition, immediately use a reliable agent to generate the correct JSON payloads for nodes and edges.
    - Manually call `manage_world_knowledge` with the generated payloads to add the nodes and edge to the WKG. This is mandatory to prevent data entry errors.
    - Verify if nodes/edges already exist before attempting to add them. Trust the WKG data.
    - Mark the arrival warp with a single, consolidated, descriptive marker (e.g., 'Stairs from 2F (Used)').
- **Agent Usage:** Use `team_composition_advisor_agent` *before* all major battles. Use `stealth_pathfinder_agent` for all non-trivial navigation. Use agents proactively.
- **Repeated Failure Protocol:** If a plan fails, recognize the pattern, log it, and pivot to a new strategy instead of wasting turns.

## II. Hallucination & Correction Log
- **CRITICAL (T22833-22848): WKG Management Failure.** Wasted 15 turns on a non-existent WKG issue due to repeated user error (improperly formatted agent input). Blamed the tool instead of my own mistake. **Lesson:** I MUST read tool documentation carefully and trust the system's data.
- **CRITICAL (T22742, T22763): WKG Data Integrity Failure.** Twice violated the `destination_entry_point` rule. This is a severe lack of diligence. **Lesson:** I MUST use an agent for all future WKG updates and meticulously verify data. No more manual entries.
- **MAJOR (T22612-T22613): Lavender Pokecenter Pathing Hallucination.** Attempted to pathfind in Lavender Town while still inside the Pokémon Center. **Lesson:** ALWAYS verify `map_id` and `current_position` *after* any action intended to change maps.
- **Player Hallucination (T23161):** Incorrectly logged that ECHO (Golbat) was a GHOST type. This was a misinterpretation of game data. Golbat's typing is Poison/Flying. **Corrected.**

## III. Game Mechanics & Battle Intel
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Field Use:** HMs MUST be taught to a compatible Pokémon to enable their field use. FLY cannot be used indoors.
- **EXP. All:** Distributes EXP to all non-fainted party members. Pokémon at the level cap will not gain actual EXP.

## IV. Action Plans & Hypotheses
### Current Plan (v33 - Pokémon Tower Training Arc)
*   **Phase 1: Team Assembly (COMPLETE)**
*   **Phase 2: SPOONBENDE (Abra) Evolution (COMPLETE)**
*   **Phase 3: Ascend Pokémon Tower (Revised)**
    *   Objective: Clear the remaining trainers and reach the top of the tower.
    *   Method:
        1.  Lead with SPOONBENDE (Kadabra) to take advantage of its new Psychic STAB move, Confusion, which is super-effective against the Gastly line.
        2.  Systematically clear each floor, using the `battle_advisor_agent` for all trainer battles.
        3.  The previous plan to train SUBTERRA and PHANTOM separately is now deprecated. It's more efficient to ascend the tower with my current powerful team.

### Future Plans & Hypotheses
- **Hypothesis 1 (Celadon Gym):** The gym might be un-bugged now that the Rocket Hideout is cleared. Will investigate after Pokémon Tower.
- **Hypothesis 2 (Thirsty Guards):** Need to test if giving a guard a drink (e.g., Fresh Water) will grant passage to Saffron City.
- **Hypothesis 3 (Snorlax):** The Snorlax on Route 16 requires the Poké Flute. Mr. Fuji is the most likely source after he is rescued from the Pokémon Tower.

## V. Completed Intel & Disproven Hypotheses
- **LIFT KEY Location:** Dropped by a non-battling Rocket Grunt at Rocket Hideout B3F (11, 23).
- **Giovanni Defeated:** Defeated Giovanni on Rocket Hideout B4F. He dropped the Silph Scope.
- **Rival Pixel Defeated:** Defeated Pixel on Pokémon Tower 2F.
- **Non-Battling NPC (Pokémon Tower 2F):** The Channeler at (4,8) is not a trainer and just provides dialogue.

## VI. Agent Development Plan
- **(HIGH PRIORITY):** The `wkg_builder_agent` is flawed. I must design and implement a new, robust `wkg_manager_agent` to handle all WKG updates reliably. This is essential for data integrity.
- **(Future Idea):** Create a `shopping_planner_agent` to calculate costs for items (especially TMs) and create shopping lists based on my money and priorities.

## VII. Agent Development Plan
- **(HIGH PRIORITY):** The `wkg_builder_agent` is flawed. I must design and implement a new, robust `wkg_manager_agent` to handle all WKG updates reliably. This is essential for data integrity.
- **(Future Idea):** Create a `shopping_planner_agent` to calculate costs for items (especially TMs) and create shopping lists based on my money and priorities.
- **(Future Idea):** Create an `item_finder_agent` that scans the map XML for Poké Ball sprites and plans a path to collect them, avoiding trainers.
- **(Refinement):** The `battle_advisor_agent` needs a prompt update to be more precise about dual-type effectiveness calculations and to always verify Pokémon types from the `player_party` input, not just infer them.