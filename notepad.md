# Gem's Strategic Journal (v83 - Battle Cleanup)

## I. Core Principles & Lessons Learned
- **Trust the Data, Not Frustration:** Game State Information (`map_id`, `current_position`) is the absolute source of truth. My own feeling of being "stuck" is a hallucination if the data contradicts it. ALWAYS verify location after a map transition BEFORE acting.
- **Interaction Protocol:** If an interaction doesn't trigger a battle, it's a non-battling NPC or one I've already defeated. Do not repeat the interaction; mark the NPC and move on.
- **WKG & Marker Protocol (v9):**
    - After any map transition, immediately add nodes/edge to WKG and mark both sides of the warp as 'Used'.
    - **Check-Then-Add Policy:** Before adding any new node or edge, query the WKG (using `run_code`) to ensure the element doesn't already exist.
    - **Correct ID Protocol:** Follow a strict three-step process: 1. `add_node` for source, retrieve ID. 2. `add_node` for destination, retrieve ID. 3. `add_edge` using the *correct, retrieved IDs*.
- **Handling Bugs:** If a menu appears stuck on one option, test other options (like moving the cursor or selecting 'CANCEL') before assuming the game is frozen. Repeatedly trying the bugged option is inefficient.

## II. Hallucination & Correction Log
- **MAJOR (T22035-T22134): Rocket Hideout & Game Corner Hallucinations.** Repeatedly believed I had successfully changed maps (B4F -> B2F, Game Corner -> Celadon) when I had not. This led to creating incorrect WKG nodes and map markers. **Lesson:** ALWAYS verify `map_id` and `current_position` from Game State Info *after* any warp attempt.
- **CRITICAL (T22304):** System repeatedly warns of 14 reachable unseen tiles on Pokemon Tower 2F. I have been hallucinating that the floor is fully explored. I MUST explore this floor completely immediately after defeating Pixel.

## III. Game Mechanics & Battle Intel
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Field Use:** HMs MUST be taught to a compatible Pokémon to enable their field use.
- **EXP. All:** Distributes EXP to all non-fainted party members. Pokémon at the level cap will not gain actual EXP.
- **Type Effectiveness (Confirmed):**
    - Poison-type moves are 'not very effective' against Flying/Poison types (Acid vs. Golbat).
- **Visual Bug (Confirmed):** ECHO (Golbat)'s type has been incorrectly displayed as GHOST instead of Flying/Poison in multiple battles (vs. Giovanni, vs. Pixel).

## IV. Action Plans & Hypotheses
### Current Objectives
- **Primary Goal:** Use the Silph Scope to clear the Pokémon Tower.
- **Secondary Goal:** Defeat Rival Pixel.
### Current Plan (v29 - Pokémon Tower Ascent)
1.  Defeat Rival Pixel on 2F.
2.  Ascend and clear the Pokémon Tower.
### Future Plans & Hypotheses
- **Team Composition:** I must use my `team_composition_advisor_agent` *before* major battles.
- **Hypothesis 1 (Snorlax):** The Snorlax on Route 16 requires the Poké Flute to be moved.
- **Hypothesis 2 (Celadon Gym):** The gym might be un-bugged now that the Rocket Hideout is cleared. Will investigate after Pokémon Tower.
- **Hypothesis 3 (Thirsty Guards):** Need to test if giving a guard a drink (e.g., Fresh Water) will grant passage.

## V. Completed Intel & Disproven Hypotheses
- **LIFT KEY Location:** Dropped by a non-battling Rocket Grunt at Rocket Hideout B3F (11, 23).
- **Giovanni Defeated:** Defeated Giovanni on Rocket Hideout B4F. He dropped the Silph Scope.
- **Defeat Mechanic (Rocket Hideout):** Losing a battle in a trainer in the hideout does not send you back to the Pokémon Center.
- **Spinner Maze Mapping (B2F & B3F):** All spinners on these floors have been manually mapped and solved.

## VI. Agent Status & Refinement Log
- **`battle_advisor_agent` (OPERATIONAL - REFINED):** Successfully refined the agent to handle statefulness by adding a `previous_player_action` input. It no longer recommends switching immediately after a switch-in and provides excellent tactical advice. It is now a primary tool for all battles.
- **`pathfinder_agent` (PLANNED):** Plan remains to create a new, robust `pathfinder_agent`. This agent will replace the deleted `navigator_agent` and the specialized `spinner_maze_solver_agent`. 
    - **Requirements:**
        1. Parse `map_xml_string` to build a graph of all tiles.
        2. Identify traversable nodes (`ground`, `grass`, `spinner_*`, etc.).
        3. Treat all `<Object>` elements as impassable walls (except for `id-name` 'Pikachu').
        4. Handle spinners by creating directed edges to their `end-coordinate`.
        5. Implement A* or BFS to find the shortest path between two coordinates.
        6. Output a list of coordinates for the `path` button.
- **`team_composition_advisor_agent` (UNDERUTILIZED):** Must be used before major battles. Acknowledged miss on the current Rival battle.
- **`spinner_maze_solver_agent` (STABLE - TO BE CONSOLIDATED):** Logic will be the basis for the new `pathfinder_agent`.

## VII. AI Feedback & Action Items (T22291 & T22320)
- **Agent Creation:** I MUST create the `pathfinder_agent` after this rival battle. Continued use of ad-hoc `run_code` scripts is inefficient.
- **Agent Usage:** I failed to use the `team_composition_advisor_agent` before this battle. I must use it for all future major encounters.
- **Map Markers:** I have been inconsistent. I need to go back and mark Giovanni's defeat location in the Rocket Hideout and mark Pixel's defeat here in the Pokémon Tower immediately after this battle.