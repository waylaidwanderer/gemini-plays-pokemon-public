# Gem's Strategic Journal (v80 - Reflection & Post-Hideout Plans)

## I. Core Principles & Lessons Learned
- **Trust the Data, Not Frustration:** Game State Information is the absolute source of truth. My own feeling of being "stuck" is a hallucination if the data (`map_id`, `current_position`, etc.) contradicts it.
- **Interaction Protocol:** If an interaction doesn't trigger a battle, it's a non-battling NPC or one I've already defeated. Do not repeat the interaction; mark the NPC and move on.
- **WKG & Marker Protocol (v8):**
    - After any map transition, immediately add nodes/edge to WKG and mark both sides of the warp as 'Used'.
    - **Check-Then-Add Policy:** Before adding any new node or edge, query the WKG (using `run_code`) to ensure the element doesn't already exist.
    - **Correct ID Protocol:** Follow a strict three-step process: 1. `add_node` for source, retrieve ID. 2. `add_node` for destination, retrieve ID. 3. `add_edge` using the *correct, retrieved IDs*.
    - **Location Verification (CRITICAL):** ALWAYS verify `map_id` and `current_position` from Game State Info *after* a warp attempt, *before* updating any logs.
- **Handling Bugs:** If a menu appears stuck on one option, test other options (like moving the cursor or selecting 'CANCEL') before assuming the game is frozen. Repeatedly trying the bugged option is inefficient.

## II. Hallucination & Correction Log
- **MAJOR (T22035-T22060): Rocket Hideout B4F -> B2F Hallucination.** Believed I had successfully taken the elevator from B4F to B2F. In reality, I was still on B4F. This led to creating incorrect WKG nodes and map markers. **Lesson:** ALWAYS verify `map_id` and `current_position` from Game State Info *after* a warp attempt.

## III. Game Mechanics & Battle Intel
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Field Use:** HMs MUST be taught to a compatible Pokémon to enable their field use.
- **EXP. All:** Distributes EXP to all non-fainted party members. Pokémon at the level cap will not gain actual EXP.
- **Type Effectiveness (Confirmed):**
    - Poison-type moves are 'not very effective' against Flying/Poison types (Acid vs. Golbat).
- **Visual Bug:** During the Giovanni battle, my Golbat ECHO's type was displayed as GHOST instead of Flying/Poison.

## IV. Action Plans & Hypotheses
### Current Objectives
- **Primary Goal:** Use the Silph Scope to clear the Pokémon Tower.
- **Secondary Goal:** Heal the party at a Pokémon Center.
### Current Plan (v27 - Escape Rocket Hideout)
1. Navigate from B2F -> B1F -> Game Corner -> Celadon City.
2. Fly to a Pokémon Center to heal.
3. Fly to Lavender Town and clear the Pokémon Tower.
### Future Plans & Hypotheses
- **Team Composition:** I must use my `team_composition_advisor_agent` *before* major battles.
- **Hypothesis 1 (Snorlax):** The Snorlax on Route 16 requires the Poké Flute to be moved.

## V. Completed Intel & Disproven Hypotheses
- **LIFT KEY Location:** Dropped by a non-battling Rocket Grunt at Rocket Hideout B3F (11, 23).
- **Giovanni Defeated:** Defeated Giovanni on Rocket Hideout B4F. He dropped the Silph Scope.
- **Defeat Mechanic (Rocket Hideout):** Losing a battle in a trainer in the hideout does not send you back to the Pokémon Center.
- **Celadon Gym Bug:** Two trainers are stuck in a dialogue loop, blocking paths. Gym is currently impassable.
- **Spinner Maze Mapping (B2F & B3F):** All spinners on these floors have been manually mapped and solved.

## VI. Agent Status & Refinement Log
- **Agent Refinement (High Priority):** Per critique, I must consolidate my navigation agents.
    - **Plan:** Create a new, robust `pathfinder_agent`. This agent will replace the deleted `navigator_agent` and the specialized `spinner_maze_solver_agent`. It should handle both standard and spinner mazes by parsing the `map_xml_string` and building a graph, treating NPCs as impassable walls.
    - **Usage:** Be more flexible with agent use. A stable pathfinding agent could have navigated this B2F maze, preventing manual errors.
- **`battle_advisor_agent` (DECOMMISSIONED PENDING REBUILD):** Inconsistent logic. Awaiting a full rebuild.
- **`team_composition_advisor_agent` (UNDERUTILIZED):** Must be used before major battles.
- **`spinner_maze_solver_agent` (STABLE - TO BE CONSOLIDATED):** Logic will be the basis for the new `pathfinder_agent`.
- **`navigator_agent` (DELETED):** Unstable and unreliable.