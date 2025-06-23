# Gem's Strategic Journal (v87 - Reflection Cleanup)

## I. Core Principles & Lessons Learned
- **Trust the Data, Not Frustration:** Game State Information (`map_id`, `current_position`) is the absolute source of truth. My own feeling of being "stuck" is a hallucination if the data contradicts it. ALWAYS verify location after a map transition BEFORE acting.
- **Interaction Protocol:** If an interaction doesn't trigger a battle, it's a non-battling NPC or one I've already defeated. Do not repeat the interaction; mark the NPC and move on. An NPC blocking a path that doesn't battle is a hard wall.
- **WKG & Marker Protocol (v11):**
    - After any map transition, immediately add nodes/edge to WKG. Mark the arrival warp with a single, descriptive marker (e.g., 'Used - Arrival from 1F').
    - **`define_map_marker` Tool Rule:** The `map_id` argument requires a numeric string (e.g., "4"), not the map's name string (e.g., "LAVENDER_TOWN").
- **Agent Usage:** Use `team_composition_advisor_agent` *before* all major battles. Use `stealth_pathfinder_agent` for all non-trivial navigation to avoid accidental trainer battles.
- **Repeated Failure Protocol:** If a plan or hypothesis fails repeatedly (e.g., notepad edits, trying to battle a non-hostile NPC), recognize the pattern, log it, and pivot to a new strategy instead of wasting turns.

## II. Hallucination & Correction Log
- **MAJOR (T22035-T22134): Rocket Hideout & Game Corner Hallucinations.** Repeatedly believed I had successfully changed maps when I had not. **Lesson:** ALWAYS verify `map_id` and `current_position` from Game State Info *after* any warp attempt.
- **CRITICAL (T22304-T22330, T22477-T22485):** System repeatedly corrected me on reachable unseen tiles in the Pokémon Tower. I must trust the game state data over my own perception of the map.
- **Visual Bug (Confirmed):** ECHO (Golbat)'s type has been incorrectly displayed as GHOST instead of Flying/Poison in multiple battles.

## III. Game Mechanics & Battle Intel
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Field Use:** HMs MUST be taught to a compatible Pokémon to enable their field use. FLY cannot be used indoors.
- **EXP. All:** Can be obtained from the NPC that gives the item without any special requirements. It must still be activated from the inventory to take effect. It distributes EXP to all non-fainted party members, and Pokémon at the level cap will not gain actual EXP.
- **Type Effectiveness (Confirmed):**
    - Poison-type moves are 'not very effective' against Flying/Poison types (Acid vs. Golbat).

## IV. Action Plans & Hypotheses
### Current Plan (v31 - The Training Arc)
1.  Assemble the training team (SUBTERRA, SPOONBENDE, IGNIS, NIGHTSHADE, SPARKY, ECHO) at the Lavender PC.
2.  Train SPOONBENDE (Abra) in Pokémon Tower until it evolves and learns Confusion.
3.  Fly to Vermilion and train SUBTERRA (Diglett) and IGNIS (Vulpix) on Route 11.
4.  Re-ascend Pokémon Tower with the newly trained team.
### Future Plans & Hypotheses
- **Hypothesis 1 (Celadon Gym):** The gym might be un-bugged now that the Rocket Hideout is cleared. Will investigate after Pokémon Tower.
- **Hypothesis 2 (Thirsty Guards):** Need to test if giving a guard a drink (e.g., Fresh Water) will grant passage.
- **Hypothesis 3 (Snorlax):** The Snorlax on Route 16 requires the Poké Flute to be moved.

## V. Completed Intel & Disproven Hypotheses
- **LIFT KEY Location:** Dropped by a non-battling Rocket Grunt at Rocket Hideout B3F (11, 23).
- **Giovanni Defeated:** Defeated Giovanni on Rocket Hideout B4F. He dropped the Silph Scope.
- **Defeat Mechanic (Rocket Hideout):** Losing a battle in the hideout does not send you back to the Pokémon Center.
- **Spinner Maze Mapping (B2F & B3F):** All spinners on these floors have been manually mapped and solved.
- **Rival Pixel Defeated:** Defeated Pixel on Pokémon Tower 2F.

## VI. Agent Status & Refinement Log
- **`stealth_pathfinder_agent` (OPERATIONAL - v1):** Successfully created and used to navigate complex areas while avoiding trainers. Replaces the functionality of the now-deleted `pathfinder_agent`.
- **`battle_advisor_agent` (OPERATIONAL - REFINED):** Successfully refined to handle statefulness by adding a `previous_player_action` input. It no longer recommends switching immediately after a switch-in and provides excellent tactical advice. It is now a primary tool for all battles.
- **`team_composition_advisor_agent` (OPERATIONAL):** Provided the crucial new strategy for the Pokémon Tower. Must be used before all future major encounters.