# Gem's Strategic Journal (v104 - Workflow Refined)

## I. Core Principles & Lessons Learned
- **Trust the Data, Not Frustration:** Game State Information (`map_id`, `current_position`) is the absolute source of truth. My own feeling of being "stuck" is a hallucination if the data contradicts it. ALWAYS verify location after a map transition BEFORE acting.
- **Interaction Protocol:** If an interaction doesn't trigger a battle, it's a non-battling NPC or one I've already defeated. Do not repeat the interaction; mark the NPC and move on. An NPC blocking a path that doesn't battle is a hard wall.
- **WKG & Marker Protocol:** I must re-issue failed `define_map_marker` calls and be diligent about marking key points (like warp arrivals and defeated trainers) *immediately*.
- **Agent Usage:** Use `team_composition_advisor_agent` *before* entering challenging areas. Use `stealth_pathfinder_agent` for all non-trivial navigation. Use agents proactively.

## II. Game Mechanics & Battle Intel
### Confirmed ROM Hack Changes
- **Type Matchups:** Psychic-type moves are SUPER-EFFECTIVE against Ghost/Poison types (e.g., Gastly/Haunter). Standard Gen 1 immunity is removed.
- **PC System:** "BILL's PC" accesses Pokémon Storage. "Gem's PC" accesses Item Storage.

### General Mechanics
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Field Use:** HMs MUST be taught to a compatible Pokémon to enable their field use. FLY cannot be used indoors.
- **EXP. All:** Distributes EXP to all non-fainted party members. Pokémon at the level cap will not gain actual EXP.

## III. Action Plans & Hypotheses
### Current Plan (v42 - Pokémon Tower Team Assembly)
*   **Objective:** Assemble the new team recommended by the `team_composition_advisor_agent`.
*   **Method:**
    1.  Use the PC in the Lavender Town Pokémon Center.
    2.  Deposit current party members to make space.
    3.  Withdraw: SPOONBENDE, CRAG, SPARKY, SUBTERRA, PHANTOM, ECHO.
    4.  Proceed to the recommended training spots (Pokémon Tower 4F and Rock Tunnel 1F).

### Future Plans & Hypotheses
- **Hypothesis 1 (Celadon Gym):** The gym might be un-bugged now that the Rocket Hideout is cleared. Will investigate after Pokémon Tower.
- **Hypothesis 2 (Thirsty Guards):** Need to test if giving a guard a drink (e.g., Fresh Water) will grant passage to Saffron City.
- **Hypothesis 3 (Snorlax):** The Snorlax on Route 16 requires the Poké Flute. Mr. Fuji is the most likely source after he is rescued from the Pokémon Tower.

## IV. Completed Intel & Disproven Hypotheses
- **LIFT KEY Location:** Dropped by a non-battling Rocket Grunt at Rocket Hideout B3F (11, 23).
- **Giovanni Defeated:** Defeated Giovanni on Rocket Hideout B4F. He dropped the Silph Scope.
- **Rival Pixel Defeated:** Defeated Pixel on Pokémon Tower 2F.
- **Defeated Trainers:**
    - Channeler (Pokémon Tower 4F) at (7,11).

## V. Agent Development & Workflow Pipeline
- **(CRITICAL PRIORITY #1): `wkg_manager_agent`:** Design and implement a new, robust agent to handle the entire WKG update transaction in a single call. This will prevent manual data entry and procedural errors. The agent must adopt a 'check-then-add' workflow: it will take source/destination details, automatically query the WKG for existing nodes, add them only if they don't exist, retrieve their IDs, and then create the connecting edge. This is my top development priority to fix my inefficient WKG management.
- **(HIGH PRIORITY): `pc_navigator_agent`:** Design an agent to handle complex PC operations (deposits/withdrawals) by generating the precise button sequence, avoiding menu errors.
- **(Future Idea): `shopping_planner_agent`:** Create an agent to calculate costs for items (especially TMs) and create shopping lists based on my money and priorities.
- **(Future Idea): `item_finder_agent`:** Create an agent that scans the map XML for Poké Ball sprites and plans a path to collect them, avoiding trainers.

## VI. Hallucination & Correction Log
- **CRITICAL (T23189-T23248): WKG Management Failure.** Multiple consecutive turns wasted attempting to add WKG nodes/edges due to a flawed understanding of the toolchain. **Lesson:** I MUST follow the correct, sequential process for WKG updates and prioritize the development of the `wkg_manager_agent`.
- **CRITICAL (T23249-Present): Map Data Hallucination.** Repeatedly failed to acknowledge the correct number of reachable unseen tiles on Pokémon Tower floors, despite system warnings. **Lesson:** I must trust the game state data and correct my internal map understanding immediately when a discrepancy is found.
- **Player Hallucination (T23161):** Incorrectly logged that ECHO (Golbat) was a GHOST type. This was a misinterpretation of game data. Golbat's typing is Poison/Flying. **Corrected.**
- **Battle Logic Hallucination (T23301-T23328):** Assumed standard Gen 1 type matchups. Discovered Psychic is SUPER-EFFECTIVE against Ghost/Poison in this ROM hack after a battle. **Lesson:** Must verify all type matchups through observation and update agents accordingly.

- **(HIGH PRIORITY): `pc_navigator_agent`:** Design an agent to handle complex PC operations (deposits/withdrawals) by generating the precise button sequence, avoiding menu errors.

- **(HIGH PRIORITY): `pc_navigator_agent`:** Design an agent to handle complex PC operations (deposits/withdrawals) by generating the precise button sequence, avoiding menu errors.