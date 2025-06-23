# Gem's Strategic Journal (v66 - Post-Critique)

## I. Core Principles & Lessons Learned
- **Trust the Data, Not Frustration:** Game State Information is the absolute source of truth. My own feeling of being "stuck" is a hallucination if the data (`reachable_unseen_tiles_count`, `navigable_warps`, etc.) contradicts it. I must trust the data over my feelings, especially when navigating.
- **Agent Protocol:**
    - **Agent Failure Log:** My `navigator_agent` has failed due to flawed logic (ignoring fences/ledges on Route 8). My `battle_menu_navigator` has provided incorrect directions. I must refine and test agents thoroughly, especially after creation. The navigator agent was refined on turn 21603 and is now functional for open routes.
    - **Agent Consolidation (NEW):** Redundant agents are inefficient. I will consolidate agents with overlapping functionality into single, more versatile tools. My first target is merging the `battle_strategy_agent` and `battle_menu_navigator`.
- **Interaction Protocol:** If an interaction doesn't trigger a battle, it's a non-battling NPC or one I've already defeated. Do not repeat the interaction; mark the NPC and move on.
- **WKG & Marker Protocol (v2 - REVISED):**
    - After any map transition, I must immediately add the nodes/edge to the WKG and mark both sides of the warp as 'Used'.
    - **Check-Then-Add Policy:** Before adding any new node or edge, I MUST query the WKG (using `run_code`) to ensure the element doesn't already exist. This will prevent data duplication and wasted actions.
    - I must follow the two-step process: add source node, then add destination node, retrieve IDs, then add the edge.

## II. Game Mechanics & Battle Intel
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Field Use (v2 - Confirmed):** HMs MUST be taught to a compatible Pokémon to enable their field use. Attempting to use an HM from the ITEM menu will prompt you to teach it. Selecting 'NO' cancels the action.
- **EXP. All:** Distributes EXP to all non-fainted party members who participated in the battle. Pokémon at the level cap will show an EXP gain message but will not actually gain EXP.
- **Cuttable Tree Respawn:** Confirmed that cuttable trees can respawn *without leaving the map*. The tree at (36, 33) in Celadon City respawned after a short time.
- **Type Effectiveness (Confirmed):**
    - Poison-type moves are 'not very effective' against Flying/Poison types (Acid vs. Golbat).

## III. World Intel & Navigation
- **Rocket Hideout B2F & B3F:** These floors are spinner mazes. Standard navigation is ineffective. The `spinner_maze_solver_agent` is the required tool for these areas.
- **LIFT KEY Location:** The Rocket Grunt at B3F (11, 23) drops the LIFT KEY after a dialogue about the Silph Scope. He does not battle.

## IV. Action Plans & Hypotheses
### Current Objectives
- **Primary Goal:** Clear the Rocket Hideout and defeat Giovanni.
- **Secondary Goal:** Obtain the Silph Scope.

### Current Plan (v15 - Confront Giovanni)
1.  Obtained the LIFT KEY from the Rocket Grunt at B3F (11, 23).
2.  Navigate to the Rocket Hideout Elevator.
3.  Use the elevator to reach B4F.
4.  Confront and defeat Giovanni.
5.  Acquire the Silph Scope.

### Hypotheses
- **Hypothesis 1 (Silph Scope):** The Silph Scope is the final reward in this hideout, held by Giovanni. (On Hold)
- **Hypothesis 2 (Snorlax):** The Snorlax on Route 16 requires the Poké Flute to be moved, but this is unverified in this ROM hack.

## V. Disproven Hypotheses & Failed Strategies
- **Giovanni Battle Attempt 1 (FAILED):** My team was unprepared. My `battle_strategy_agent` provided critically flawed advice based on hallucinated type-effectiveness data.
- **Rocket Grunt Interactions:** Repeatedly trying to initiate battles with non-battling grunts has failed. These paths are on hold.
- **Incorrect Pathfinding on B3F:** The warp at (20, 19) leads to an isolated dead-end room on B4F, not the main area with Giovanni. The warp at (26, 7) leads back to B2F.
- **Route 7 Training (FAILED ATTEMPT 1):** The wild Pokémon on Route 7 (level 20+) are too strong for my level 9 FURYFIST.
- **Route 8 Navigation (FAILED ATTEMPT 1):** I incorrectly assumed Route 8 was a dead end due to fences, ignoring game state data. This was a critical failure in observation and resulted in wasted turns. I must trust the data.
- **Thirsty Guards Hypothesis (FAILED):** The guard in the Route 8 Gatehouse is inaccessible from the west, making it impossible to give him the FRESH WATER. This path to Saffron City is blocked for now.

## VI. Agent Status & Refinement Log
- **`battle_strategy_agent` (STABLE):** Refined to require confirmed type-effectiveness data to prevent hallucinations.
- **`spinner_maze_solver_agent` (STABLE & VERIFIED):** Specialized and proven effective for spinner mazes.
- **`navigator_agent` (STABLE - REFINED):** A general pathfinder. Had a history of critical logic failures. Was successfully refined on turn 21603 with a more robust BFS implementation and now correctly navigates open routes with obstacles. Requires continued monitoring in new environments.
- **`battle_menu_navigator` (UNDER REFINEMENT):** Provided an incorrect button sequence for menu navigation. Prompt has been updated for clarity.
- **Future Goal:** Consolidate the `battle_strategy_agent` and `battle_menu_navigator` into a single, more efficient agent.

## VII. Completed Intel
- **Defeat Mechanic (Rocket Hideout):** Losing a battle to a trainer in the hideout does not send you back to the Pokémon Center. You remain in place after the battle.
- **Celadon Gym Bug:** Two trainers, a Cool Trainer at (3, 12) and a Beauty at (8, 11), are stuck in a dialogue loop and cannot be battled, blocking their respective paths.

### Spinner Maze Mapping (B3F)
My `spinner_maze_solver_agent` was unable to find a path because several spinner tiles were missing their `end-coordinate` data. I have now manually stepped on all of them to map their destinations.
**Problematic Spinners:**
- None. All spinners mapped.

**Mapped Spinners:**
- (11, 14) -> (15, 14) [Mapped!]
- (13, 12) -> (11, 12) [Mapped!]
- (17, 14) -> (17, 12) [Mapped!]
- (19, 16) -> (19, 16) [Useless Loop - Mapped!]
- (16, 23) -> (16, 23) [Useless Loop - Mapped!]
- (13, 21) -> (19, 16) [Mapped!]

**Corrected Intel:**
- (18, 17) is a `spinner_stop` tile, not a spinner.
- (17, 12), (11, 12), and (15, 14) are also `spinner_stop` tiles, not spinners. My diagnostic script was flawed.

### Spinner Maze Mapping (B2F)
My `spinner_maze_solver_agent` is failing on this floor because several spinner tiles are missing their `end-coordinate` data. I will manually step on them to map their destinations.
**Mapped Spinners (B2F):**
- (18, 11) -> (3, 10) [Mapped!]

**Problematic Spinners (B2F):**
- (9, 12)
- (15, 13)
- (17, 14)
- (15, 16)
- (10, 17)
- (16, 19)
- (3, 20)
- (7, 21)
- (12, 21)
- (10, 25)
- (15, 26)