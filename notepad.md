# Gem's Strategic Journal (v70 - Post-Reflection)

## I. Core Principles & Lessons Learned
- **Trust the Data, Not Frustration:** Game State Information is the absolute source of truth. My own feeling of being "stuck" is a hallucination if the data (`reachable_unseen_tiles_count`, `navigable_warps`, etc.) contradicts it. I must trust the data over my feelings.
- **Agent Protocol:**
    - **Agent Failure Log:** My agents have a history of failure. I must refine and test agents thoroughly, especially after creation. The `battle_advisor_agent` is currently unreliable.
- **Interaction Protocol:** If an interaction doesn't trigger a battle, it's a non-battling NPC or one I've already defeated. Do not repeat the interaction; mark the NPC and move on.
- **WKG & Marker Protocol (v4 - CRITICAL UPDATE):**
    - After any map transition, I must immediately add the nodes/edge to the WKG and mark both sides of the warp as 'Used'.
    - **Check-Then-Add Policy:** Before adding any new node or edge, I MUST query the WKG (using `run_code`) to ensure the element doesn't already exist.
    - **Correct ID Protocol:** I MUST follow a strict three-step process: 1. `add_node` for the source, retrieve its ID. 2. `add_node` for the destination, retrieve its ID. 3. `add_edge` using the *correct, retrieved IDs*. Hardcoding UUIDs is a critical failure that I have committed and must not repeat.

## II. Game Mechanics & Battle Intel
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Field Use:** HMs MUST be taught to a compatible Pokémon to enable their field use.
- **EXP. All:** Distributes EXP to all non-fainted party members. Pokémon at the level cap will not gain actual EXP.
- **Type Effectiveness (Confirmed):**
    - Poison-type moves are 'not very effective' against Flying/Poison types (Acid vs. Golbat).

## III. World Intel & Navigation
- **LIFT KEY Location:** The Rocket Grunt at B3F (11, 23) drops the LIFT KEY after dialogue. He does not battle.

## IV. Action Plans & Hypotheses
### Current Objectives
- **Primary Goal:** Clear the Rocket Hideout and defeat Giovanni.
- **Secondary Goal:** Obtain the Silph Scope.

### Current Plan (v18 - Giovanni Confrontation)
1. Defeat Giovanni.
2. Acquire the Silph Scope.

### Future Plans & Hypotheses
- **PC Organization Agent:** Consider creating an agent to help manage and suggest teams from my PC.
- **Hypothesis 1 (Silph Scope):** The Silph Scope is the final reward in this hideout, held by Giovanni.
- **Hypothesis 2 (Snorlax):** The Snorlax on Route 16 requires the Poké Flute to be moved.

## V. Disproven Hypotheses & Failed Strategies
- **Giovanni Battle Attempt 1 (FAILED):** My team was unprepared.
- **Route 8 Navigation (FAILED ATTEMPT 1):** I incorrectly assumed Route 8 was a dead end due to fences, ignoring game state data.

## VI. Completed Intel
- **Defeat Mechanic (Rocket Hideout):** Losing a battle to a trainer in the hideout does not send you back to the Pokémon Center.
- **Celadon Gym Bug:** Two trainers are stuck in a dialogue loop, blocking paths.
- **Spinner Maze Mapping (B2F & B3F):** All spinners on these floors have been manually mapped and solved.

## VII. Agent Status & Refinement Log
- **`battle_advisor_agent` (UNRELIABLE - REFINED v4):** A consolidated agent for battle strategy and menu navigation. Has a history of critical failures, including hallucinating Pokémon types and miscalculating type effectiveness. It consistently undervalues level differences. I am attempting one final, major refinement. If it fails again, it will be deprecated and rebuilt.
- **`spinner_maze_solver_agent` (STABLE - REFINED):** Specialized pathfinder for spinner mazes. Requires complete map data to function correctly. Was successfully refined to treat NPCs as impassable.
- **`navigator_agent` (STABLE - REFINED):** A general pathfinder. Had a history of critical logic failures. Was successfully refined and now correctly navigates open routes with obstacles.