# Gem's Strategic Journal (v79 - Post-Giovanni, Correcting Hallucination)

## I. Core Principles & Lessons Learned
- **Trust the Data, Not Frustration:** Game State Information is the absolute source of truth. My own feeling of being "stuck" or having moved maps is a hallucination if the data (`map_id`, `current_position`, `navigable_warps`, etc.) contradicts it. I must trust the data over my feelings.
- **Interaction Protocol:** If an interaction doesn't trigger a battle, it's a non-battling NPC or one I've already defeated. Do not repeat the interaction; mark the NPC and move on.
- **WKG & Marker Protocol (v8 - CRITICAL UPDATE):**
    - After any map transition, I must immediately add the nodes/edge to the WKG and mark both sides of the warp as 'Used'.
    - **Check-Then-Add Policy:** Before adding any new node or edge, I MUST query the WKG (using `run_code`) to ensure the element doesn't already exist.
    - **Correct ID Protocol:** I MUST follow a strict three-step process: 1. `add_node` for the source, retrieve its ID. 2. `add_node` for the destination, retrieve its ID. 3. `add_edge` using the *correct, retrieved IDs*. Hardcoding UUIDs is a critical failure that I have committed and must not repeat.
    - **Location Verification (CRITICAL):** I MUST verify my current `map_id` and coordinates from Game State Info before any WKG modification to prevent hallucination-based errors, as demonstrated during the Rocket Hideout Elevator sequence.
- **Self-Correction Protocol:** My own recorded plans and strategic insights are valuable. I must act on them, especially when they address identified weaknesses in my gameplay (e.g., failing to use preparation agents before major battles).

## II. Hallucination & Correction Log
- **MAJOR (T22035): Rocket Hideout B4F -> B2F Hallucination.** Believed I had successfully taken the elevator from B4F to B2F. In reality, I was still on B4F (ID: 202) at (25, 16). This led to creating incorrect WKG nodes and map markers for B2F. **Lesson:** ALWAYS verify `map_id` and `current_position` from Game State Info *after* a warp attempt, *before* updating any logs or knowledge bases. Corrective action: Deleting incorrect WKG entries and markers.

## III. Game Mechanics & Battle Intel
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Field Use:** HMs MUST be taught to a compatible Pokémon to enable their field use.
- **EXP. All:** Distributes EXP to all non-fainted party members. Pokémon at the level cap will not gain actual EXP.
- **Type Effectiveness (Confirmed):**
    - Poison-type moves are 'not very effective' against Flying/Poison types (Acid vs. Golbat).
- **Visual Bug:** During the Giovanni battle, my Golbat ECHO's type was displayed as GHOST instead of Flying/Poison. Unclear if this is just a visual glitch or has mechanical implications.

## IV. Action Plans & Hypotheses
### Current Objectives
- **Primary Goal:** Use the Silph Scope to clear the Pokémon Tower.
- **Secondary Goal:** Heal the party at a Pokémon Center.
### Current Plan (v26 - Escape Rocket Hideout - CORRECTED)
1. Navigate out of Rocket Hideout B4F using the elevator.
2. Navigate from B2F -> B1F -> Game Corner -> Celadon City.
3. Fly to a Pokémon Center to heal.
4. Fly to Lavender Town and clear the Pokémon Tower.
### Future Plans & Hypotheses
- **Team Composition:** I must use my `team_composition_advisor_agent` *before* major battles to build a more effective team. This was a major strategic error for the Giovanni fight.
- **Hypothesis 1 (Snorlax):** The Snorlax on Route 16 requires the Poké Flute to be moved.

## V. Completed Intel & Disproven Hypotheses
- **LIFT KEY Location:** Dropped by a non-battling Rocket Grunt at Rocket Hideout B3F (11, 23).
- **Giovanni Defeated:** Defeated Giovanni on Rocket Hideout B4F. He dropped the Silph Scope.
- **Defeat Mechanic (Rocket Hideout):** Losing a battle to a trainer in the hideout does not send you back to the Pokémon Center.
- **Celadon Gym Bug:** Two trainers are stuck in a dialogue loop, blocking paths. Gym is currently impassable.
- **Spinner Maze Mapping (B2F & B3F):** All spinners on these floors have been manually mapped and solved.
- **Route 8 Navigation (FAILED ATTEMPT 1):** I incorrectly assumed Route 8 was a dead end due to fences, ignoring game state data.

## VI. Agent Status & Refinement Log
- **`battle_advisor_agent` (DECOMMISSIONED PENDING REVIEW):** This agent has a persistent history of critical failures but provided a critical winning suggestion (FLY) vs Giovanni's Persian. Its logic is inconsistent. It will not be used until it is rebuilt from scratch.
- **`team_composition_advisor_agent` (UNDERUTILIZED):** I have not been using this agent to its full potential. I must use it to prepare for major battles. This was a major strategic error leading into the Giovanni fight.
- **`spinner_maze_solver_agent` (STABLE - REFINED):** Specialized pathfinder for spinner mazes. Was successfully refined to treat NPCs as impassable.
- **`navigator_agent` (UNSTABLE):** A general pathfinder. Failed to find a path on Rocket Hideout B4F. Seems unreliable in complex mazes.

- **Agent Refinement (High Priority):** Per critique, I must rebuild the `battle_advisor_agent` and refine/consolidate the `navigator_agent` and `spinner_maze_solver_agent` as soon as I am out of this crisis.