# Gem's Strategic Journal (v69 - Post-Critique & Cleanup)

## I. Core Principles & Lessons Learned
- **Trust the Data, Not Frustration:** Game State Information is the absolute source of truth. My own feeling of being "stuck" is a hallucination if the data (`reachable_unseen_tiles_count`, `navigable_warps`, etc.) contradicts it. I must trust the data over my feelings, especially when navigating.
- **Agent Protocol:**
    - **Agent Failure Log:** My `navigator_agent` has failed due to flawed logic. My `battle_advisor_agent` has provided incorrect directions. My `spinner_maze_solver_agent` has failed due to incomplete map data. I must refine and test agents thoroughly, especially after creation.
    - **Agent Consolidation:** Redundant agents are inefficient. I will consolidate agents with overlapping functionality. The `battle_strategy_agent` and `battle_menu_navigator` have been successfully merged into `battle_advisor_agent`.
- **Interaction Protocol:** If an interaction doesn't trigger a battle, it's a non-battling NPC or one I've already defeated. Do not repeat the interaction; mark the NPC and move on.
- **WKG & Marker Protocol (v3 - CRITICAL UPDATE):**
    - After any map transition, I must immediately add the nodes/edge to the WKG and mark both sides of the warp as 'Used'.
    - **Check-Then-Add Policy:** Before adding any new node or edge, I MUST query the WKG (using `run_code`) to ensure the element doesn't already exist.
    - **Correct ID Protocol:** I MUST follow a strict three-step process: 1. `add_node` for the source, retrieve its ID. 2. `add_node` for the destination, retrieve its ID. 3. `add_edge` using the *correct, retrieved IDs*. Hardcoding UUIDs is a critical failure.
    - **Consistent Map IDs:** I MUST use numerical map IDs (e.g., `200`) in all WKG operations, not string names (e.g., "ROCKET_HIDEOUT_B2F").

## II. Game Mechanics & Battle Intel
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Field Use (v2 - Confirmed):** HMs MUST be taught to a compatible Pokémon to enable their field use.
- **EXP. All:** Distributes EXP to all non-fainted party members. Pokémon at the level cap will not gain actual EXP.
- **Cuttable Tree Respawn:** Confirmed that cuttable trees can respawn *without leaving the map*.
- **Type Effectiveness (Confirmed):**
    - Poison-type moves are 'not very effective' against Flying/Poison types (Acid vs. Golbat).

## III. World Intel & Navigation
- **Rocket Hideout B2F & B3F:** These floors are spinner mazes. Standard navigation is ineffective. The `spinner_maze_solver_agent` is the required tool.
- **LIFT KEY Location:** The Rocket Grunt at B3F (11, 23) drops the LIFT KEY after dialogue. He does not battle.

## IV. Action Plans & Hypotheses
### Current Objectives
- **Primary Goal:** Clear the Rocket Hideout and defeat Giovanni.
- **Secondary Goal:** Obtain the Silph Scope.

### Current Plan (v17 - Rocket Hideout B4F Confrontation)
1. Use the elevator to reach B4F.
2. Confront and defeat Giovanni.
3. Acquire the Silph Scope.

### Hypotheses
- **Hypothesis 1 (Silph Scope):** The Silph Scope is the final reward in this hideout, held by Giovanni. (On Hold)
- **Hypothesis 2 (Snorlax):** The Snorlax on Route 16 requires the Poké Flute to be moved. (Unverified)

## V. Disproven Hypotheses & Failed Strategies
- **Giovanni Battle Attempt 1 (FAILED):** My team was unprepared. My `battle_strategy_agent` provided critically flawed advice.
- **Incorrect Pathfinding on B3F:** The warp at (20, 19) leads to an isolated dead-end room on B4F. The warp at (26, 7) leads back to B2F.
- **Route 8 Navigation (FAILED ATTEMPT 1):** I incorrectly assumed Route 8 was a dead end due to fences, ignoring game state data.
- **Thirsty Guards Hypothesis (FAILED):** The guard in the Route 8 Gatehouse is inaccessible from the west, blocking the path to Saffron City.

## VI. Completed Intel
- **Defeat Mechanic (Rocket Hideout):** Losing a battle to a trainer in the hideout does not send you back to the Pokémon Center.
- **Celadon Gym Bug:** Two trainers are stuck in a dialogue loop, blocking paths.
- **Spinner Maze Mapping (B3F & B2F):** All spinners on these floors have been manually mapped and their destinations recorded.

## VII. Agent Status & Refinement Log
- **`battle_advisor_agent` (REFINED - v2):** A consolidated agent for battle strategy and menu navigation. Initially provided a critically flawed switch recommendation based on hallucinated type data. Was immediately refined with a full Gen 1 type chart and more explicit instructions on weighing levels, stats, and status effects.
- **`spinner_maze_solver_agent` (STABLE - REFINED):** Specialized pathfinder for spinner mazes. Requires complete map data to function correctly; will fail if spinners are missing `end-coordinate` data. Was successfully refined to treat NPCs as impassable.
- **`navigator_agent` (STABLE - REFINED):** A general pathfinder. Had a history of critical logic failures. Was successfully refined on turn 21603 with a more robust BFS implementation and now correctly navigates open routes with obstacles. Requires continued monitoring in new environments.