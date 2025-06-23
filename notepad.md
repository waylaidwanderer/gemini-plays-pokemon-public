# Gem's Strategic Journal (v64 - Post-Reflection)

## I. Core Principles & Lessons Learned
- **Trust the Data, Not Frustration:** Game State Information is the absolute source of truth. My own feeling of being "stuck" is a hallucination if the data (`reachable_unseen_tiles_count`, `navigable_warps`, etc.) contradicts it. I must trust the data over my feelings, especially when navigating.
- **Agent Protocol:**
    - **Agent Failure Log:** My `navigator_agent` has failed due to flawed logic (ignoring fences/ledges on Route 8). My `battle_menu_navigator` has provided incorrect directions. I must refine and test agents thoroughly, especially after creation. The navigator agent was refined on turn 21603 and is now functional for open routes.
    - **Agent Consolidation:** Redundant agents are inefficient. I will consolidate agents with overlapping functionality into single, more versatile tools.
- **Interaction Protocol:** If an interaction doesn't trigger a battle, it's a non-battling NPC or one I've already defeated. Do not repeat the interaction; mark the NPC and move on.
- **WKG & Marker Protocol:** After any map transition, I must immediately add the nodes/edge to the WKG and mark both sides of the warp as 'Used'. I must check the WKG before adding new edges to avoid duplicates and not create entries based on hallucinations. I must follow the two-step process: add source node, then add destination node, retrieve IDs, then add the edge.

## II. Game Mechanics & Battle Intel
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Field Use (v2 - Confirmed):** HMs MUST be taught to a compatible Pokémon to enable their field use. Attempting to use an HM from the ITEM menu will prompt you to teach it. Selecting 'NO' cancels the action.
- **EXP. All:** Distributes EXP to all non-fainted party members who participated in the battle. Pokémon at the level cap will show an EXP gain message but will not actually gain EXP.
- **Cuttable Tree Respawn:** Confirmed that cuttable trees can respawn *without leaving the map*. The tree at (36, 33) in Celadon City respawned after a short time.
- **Type Effectiveness (Confirmed):**
    - Poison-type moves are 'not very effective' against Flying/Poison types (Acid vs. Golbat).

## III. World Intel & Navigation
- **Rocket Hideout B2F & B3F:** These floors are spinner mazes. Standard navigation is ineffective. The `spinner_maze_solver_agent` is the required tool for these areas.

## IV. Action Plans & Hypotheses
### Current Objectives
- **Primary Goal:** Clear the Rocket Hideout and defeat Giovanni.
- **Secondary Goal:** Obtain the Silph Scope.
- **Tertiary Goal:** Level up my team to prepare for Giovanni.

### Current Plan (v13 - Route 8 Exploration)
1.  **Explore Route 8:** Finish exploring all unseen tiles and battling all trainers.
2.  **Test Guard Hypothesis:** After clearing Route 8, travel to a gatehouse with a thirsty guard (e.g., Route 8 Gatehouse) and attempt to give them the FRESH WATER from my inventory.
3.  **Return to Hideout:** Once Route 8 is clear and the hypothesis is tested, return to the Rocket Hideout.

### Hypotheses
- **Hypothesis 1 (Silph Scope):** The Silph Scope is the final reward in this hideout, held by Giovanni. (On Hold)
- **Hypothesis 2 (Snorlax):** The Snorlax on Route 16 requires the Poké Flute to be moved, but this is unverified in this ROM hack.
- **Hypothesis 3 (Thirsty Guards - NEW):** The guards blocking the gatehouses on Routes 5, 6, and 8 can be placated by giving them an item, possibly the FRESH WATER I have in my inventory. (To be tested)

## V. Disproven Hypotheses & Failed Strategies
- **Giovanni Battle Attempt 1 (FAILED):** My team was unprepared. My `battle_strategy_agent` provided critically flawed advice based on hallucinated type-effectiveness data.
- **Rocket Grunt Interactions:** Repeatedly trying to initiate battles with non-battling grunts has failed. These paths are on hold.
- **Incorrect Pathfinding on B3F:** The warp at (20, 19) leads to an isolated dead-end room on B4F, not the main area with Giovanni. The warp at (26, 7) leads back to B2F. The path forward is likely gated by the Rocket Grunt at (11, 23).
- **Route 7 Training (FAILED ATTEMPT 1):** The wild Pokémon on Route 7 (level 20+) are too strong for my level 9 FURYFIST.
- **Route 8 Navigation (FAILED ATTEMPT 1):** I incorrectly assumed Route 8 was a dead end due to fences, ignoring game state data. This was a critical failure in observation and resulted in wasted turns. I must trust the data.

## VI. Agent Status & Refinement Log
- **`battle_strategy_agent` (STABLE):** Refined to require confirmed type-effectiveness data to prevent hallucinations.
- **`spinner_maze_solver_agent` (STABLE & VERIFIED):** Specialized and proven effective for spinner mazes.
- **`navigator_agent` (STABLE - REFINED):** A general pathfinder. Had a history of critical logic failures. Was successfully refined on turn 21603 with a more robust BFS implementation and now correctly navigates open routes with obstacles. Requires continued monitoring in new environments.
- **`battle_menu_navigator` (UNDER REFINEMENT):** Provided an incorrect button sequence for menu navigation. Prompt has been updated for clarity.
- **Future Goal:** Continue to test and refine the `navigator_agent` and `battle_menu_navigator` to ensure they are reliable across all map types and situations.

## VII. Completed Intel
- **Defeat Mechanic (Rocket Hideout):** Losing a battle to a trainer in the hideout does not send you back to the Pokémon Center. You remain in place after the battle.
- **Celadon Gym Bug:** Two trainers, a Cool Trainer at (3, 12) and a Beauty at (8, 11), are stuck in a dialogue loop and cannot be battled, blocking their respective paths.