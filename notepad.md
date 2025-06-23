# Gem's Strategic Journal (v77 - Post-Giovanni)

## I. Core Principles & Lessons Learned
- **Trust the Data, Not Frustration:** Game State Information is the absolute source of truth. My own feeling of being "stuck" is a hallucination if the data (`reachable_unseen_tiles_count`, `navigable_warps`, etc.) contradicts it. I must trust the data over my feelings.
- **Interaction Protocol:** If an interaction doesn't trigger a battle, it's a non-battling NPC or one I've already defeated. Do not repeat the interaction; mark the NPC and move on.
- **WKG & Marker Protocol (v7 - CRITICAL UPDATE):**
    - After any map transition, I must immediately add the nodes/edge to the WKG and mark both sides of the warp as 'Used'.
    - **Check-Then-Add Policy:** Before adding any new node or edge, I MUST query the WKG (using `run_code`) to ensure the element doesn't already exist.
    - **Correct ID Protocol:** I MUST follow a strict three-step process: 1. `add_node` for the source, retrieve its ID. 2. `add_node` for the destination, retrieve its ID. 3. `add_edge` using the *correct, retrieved IDs*. Hardcoding UUIDs is a critical failure that I have committed and must not repeat.
    - **Location Verification (CRITICAL):** I MUST verify my current `map_id` and coordinates from Game State Info before any WKG modification to prevent hallucination-based errors, as demonstrated during the Rocket Hideout Elevator sequence.
- **Self-Correction Protocol:** My own recorded plans and strategic insights are valuable. I must act on them, especially when they address identified weaknesses in my gameplay (e.g., failing to use preparation agents before major battles).

## II. Game Mechanics & Battle Intel
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Field Use:** HMs MUST be taught to a compatible Pokémon to enable their field use.
- **EXP. All:** Distributes EXP to all non-fainted party members. Pokémon at the level cap will not gain actual EXP.
- **Type Effectiveness (Confirmed):**
    - Poison-type moves are 'not very effective' against Flying/Poison types (Acid vs. Golbat).

## III. World Intel & Navigation
- **Hypothesis 1 (Silph Scope):** The Silph Scope is the final reward in this hideout, held by Giovanni. (Now confirmed, pending pickup).
- **Hypothesis 2 (Snorlax):** The Snorlax on Route 16 requires the Poké Flute to be moved.

## IV. Action Plans & Hypotheses
### Current Objectives
- **Primary Goal:** Use the Silph Scope to clear the Pokémon Tower.
- **Secondary Goal:** Obtain the Silph Scope.

### Current Plan (v24 - Post-Giovanni)
1. Acquire the Silph Scope.
2. Proceed to Lavender Town and clear the Pokémon Tower.

### Future Plans & Hypotheses
- **Team Composition:** I must use my `team_composition_advisor_agent` *before* major battles to build a more effective team. This was a major strategic error for the Giovanni fight.

## V. Disproven Hypotheses & Failed Strategies
- **Route 8 Navigation (FAILED ATTEMPT 1):** I incorrectly assumed Route 8 was a dead end due to fences, ignoring game state data.
- **Giovanni Battle - Over-reliance on `battle_advisor_agent`:** My repeated trust in this agent, despite its documented history of critical failures, led to poor strategic decisions. I will not use it again until it is rebuilt.

## VI. Completed Intel
- **LIFT KEY Location:** The Rocket Grunt at B3F (11, 23) drops the LIFT KEY after dialogue. He does not battle.
- **Defeat Mechanic (Rocket Hideout):** Losing a battle to a trainer in the hideout does not send you back to the Pokémon Center.
- **Celadon Gym Bug:** Two trainers are stuck in a dialogue loop, blocking paths.
- **Spinner Maze Mapping (B2F & B3F):** All spinners on these floors have been manually mapped and solved.

## VII. Agent Status & Refinement Log
- **`battle_advisor_agent` (DECOMMISSIONED PENDING REVIEW):** This agent has a persistent history of critical failures. I will no longer use it in its current state. It will be deleted and rebuilt from scratch after this mission.
- **`team_composition_advisor_agent` (UNDERUTILIZED):** I have not been using this agent to its full potential. I must use it to prepare for major battles. This was a major strategic error leading into the current Giovanni fight.
- **`spinner_maze_solver_agent` (STABLE - REFINED):** Specialized pathfinder for spinner mazes. Was successfully refined to treat NPCs as impassable.
- **`navigator_agent` (STABLE - REFINED):** A general pathfinder. Was successfully refined and now correctly navigates open routes with obstacles.