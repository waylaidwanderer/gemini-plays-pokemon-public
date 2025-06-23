# Gem's Strategic Journal (v63 - Post-Reflection)

## I. Core Principles & Lessons Learned
- **Trust the Data, Not Frustration:** Game State Information is the source of truth. My own feeling of being "stuck" is a hallucination if the data contradicts it. I must trust the data, especially the `map_id` and `reachable` status of warps/NPCs.
- **Agent Protocol:**
    - **Agent Failure Log:** My agents have failed due to flawed logic (`navigator_agent` ignoring spinner maze mechanics) and providing useless output (an early version of `spinner_maze_solver_agent` also ignored spinners). My `battle_menu_navigator` provided incorrect directions. I must refine and test agents thoroughly, especially after creation.
    - **Agent Consolidation:** Redundant agents are inefficient. I will consolidate agents with overlapping functionality into single, more versatile tools.
- **Interaction Protocol:** If an interaction doesn't trigger a battle, it's likely a non-battling NPC or one I've already defeated. Do not repeat the interaction; mark the NPC and move on.
- **WKG & Marker Protocol:** After any map transition, I must immediately add the nodes/edge to the WKG and mark both sides of the warp as 'Used'. I must check the WKG before adding new edges to avoid duplicates and not create entries based on hallucinations. I must follow the two-step process: add source node, then add destination node, retrieve IDs, then add the edge.

## II. Game Mechanics & Battle Intel
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Field Use (v2 - Confirmed):** HMs MUST be taught to a compatible Pokémon to enable their field use. Attempting to use an HM from the ITEM menu will prompt you to teach it. Selecting 'NO' cancels the action.
- **EXP. All:** Distributes EXP to all non-fainted party members who participated in the battle. Pokémon at the level cap will show an EXP gain message but will not actually gain EXP.
- **Cuttable Tree Respawn:** Confirmed that cuttable trees can respawn *without leaving the map*. The tree at (36, 33) in Celadon City respawned after a short time.
- **Type Effectiveness (Confirmed):
    
    - Poison-type moves are 'not very effective' against Flying/Poison types (Acid vs. Golbat).

## III. World Intel & Navigation
- **Rocket Hideout B2F & B3F:** These floors are spinner mazes. Standard navigation is ineffective. The `spinner_maze_solver_agent` is the required tool for these areas.

## IV. Action Plans & Hypotheses
### Current Objectives
- **Primary Goal:** Clear the Rocket Hideout and defeat Giovanni.
- **Secondary Goal:** Obtain the Silph Scope.
- **Tertiary Goal:** Level up my team to prepare for Giovanni.

### Current Plan (v12 - Giovanni Rematch Prep)
1.  **Find a better training spot:** Route 7's wild Pokémon are too strong for my new recruits.
2.  **Train:** Level up FURYFIST and TORRENT.
3.  **Rematch:** Challenge Giovanni again with the prepared team.

### Hypotheses
- **Hypothesis 1 (Silph Scope):** The Silph Scope is the final reward in this hideout, held by Giovanni. (On Hold)
- **Hypothesis 2 (Snorlax):** The Snorlax on Route 16 requires the Poké Flute to be moved, but this is unverified in this ROM hack.
- **Hypothesis 3 (Route 7 Warps):** The warps on Route 7 lead back to the Celadon side of the Underground Path. I need to verify this by entering them.

## V. Disproven Hypotheses & Failed Strategies
- **Giovanni Battle Attempt 1 (FAILED):** My team was unprepared. My `battle_strategy_agent` provided critically flawed advice based on hallucinated type-effectiveness data.
- **Rocket Grunt Interactions:** Repeatedly trying to initiate battles with non-battling grunts has failed. These paths are on hold.
- **Incorrect Pathfinding on B3F:** The warp at (20, 19) leads to an isolated dead-end room on B4F, not the main area with Giovanni. The warp at (26, 7) leads back to B2F. The path forward is likely gated by the Rocket Grunt at (11, 23).
- **Route 7 Training (FAILED ATTEMPT 1):** The wild Pokémon on Route 7 (level 20+) are too strong for my level 9 FURYFIST.

## VI. Agent Status & Refinement Log
- **`battle_strategy_agent` (STABLE):** Refined to require confirmed type-effectiveness data to prevent hallucinations.
- **`spinner_maze_solver_agent` (STABLE & VERIFIED):** Specialized and proven effective for spinner mazes.
- **`navigator_agent` (UNRELIABLE - Under Refinement):** A general pathfinder. Has a history of critical logic failures, including improper handling of `cuttable` tiles, NPC obstacles, ledges, and `impassable` tiles. Requires further refinement and verification before it can be trusted.
- **`battle_menu_navigator` (UNDER REFINEMENT):** Provided an incorrect button sequence for menu navigation. Prompt has been updated for clarity.
- **Future Goal:** Continue to test and refine the `navigator_agent` and `battle_menu_navigator` to ensure they are reliable across all map types and situations.

## VII. Completed Intel
- **Celadon Diner Tip:** An NPC at (2, 5) in the Celadon Diner revealed there is a secret basement under the Game Corner. This led to finding the poster switch.
- **Lift Key Location:** Discovered I already possessed the Lift Key.
- **Defeat Mechanic (Rocket Hideout):** Losing a battle to a trainer in the hideout does not send you back to the Pokémon Center. You remain in place after the battle.
- **Celadon Gym Bug:** Two trainers, a Cool Trainer at (3, 12) and a Beauty at (8, 11), are stuck in a dialogue loop and cannot be battled, blocking their respective paths.