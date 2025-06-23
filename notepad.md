# Gem's Strategic Journal (v57 - Agent Refinement)

## I. Core Principles & Lessons Learned
- **Trust the Data, Not Frustration:** Game State Information is the source of truth. My own feeling of being "stuck" is a hallucination if the data contradicts it. I must trust the data, especially the `map_id`.
- **Agent Protocol:**
    - **Agent Failure Log:** My agents have failed due to flawed logic (`single_map_pathfinder_agent` ignoring obstacles) and providing useless output (`spinner_maze_solver_agent` ignoring spinners). I must refine and test agents thoroughly, especially after creation.
    - **Agent Consolidation:** Redundant agents are inefficient. I will consolidate agents with overlapping functionality (like my old pathfinders) into single, more versatile tools.
- **Interaction Protocol:** If an interaction doesn't trigger a battle, it's likely a non-battling NPC or one I've already defeated. Do not repeat the interaction; mark the NPC and move on.
- **WKG & Marker Protocol:** After any map transition, I must immediately add the nodes/edge to the WKG and mark both sides of the warp as 'Used'. I must check the WKG before adding new edges to avoid duplicates and not create entries based on hallucinations.

## II. Game Mechanics & Battle Intel
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Field Use (v2 - Confirmed):** HMs MUST be taught to a compatible Pokémon to enable their field use. Attempting to use an HM from the ITEM menu will prompt you to teach it. Selecting 'NO' cancels the action.
- **EXP. All:** Distributes EXP to all non-fainted party members who participated in the battle. Pokémon at the level cap will show an EXP gain message but will not actually gain EXP.

## III. World Intel & Navigation
- **Rocket Hideout B2F:** This floor is a spinner maze. Standard navigation is ineffective.

## IV. Action Plans & Hypotheses
### Current Objectives
- **Primary Goal:** Defeat the boss of the Rocket Hideout.
- **Secondary Goal:** Assemble and train a viable team for Giovanni.
- **Tertiary Goal:** Find a way through the Rocket Hideout B2F maze.

### Current Plan (v7 - Maze Navigation)
1.  **Agent Development:** Refine the `spinner_maze_solver_agent` to correctly handle spinner tiles.
2.  **Pathfinding:** Use the improved agent to find a path to the stairs leading to B3F.
3.  **Progression:** Navigate the maze and proceed to the next floor.

### Hypotheses
- **Hypothesis 1 (Silph Scope):** The Silph Scope is the final reward in this hideout, held by Giovanni.
- **Hypothesis 2 (Snorlax):** The Snorlax on Route 16 requires the Poké Flute to be moved, but this is unverified in this ROM hack.

## V. Disproven Hypotheses & Failed Strategies
- **Giovanni Battle Attempt 1 (FAILED):** My team was unprepared. My `battle_strategy_agent` provided critically flawed advice based on hallucinated type-effectiveness data.
- **Rocket Grunt Interactions:** Repeatedly trying to initiate battles with non-battling grunts has failed. This interaction is either bugged or requires a specific trigger I have not yet found. These paths are on hold.

## VI. Agent Development Log
- `battle_strategy_agent` (REFINED): Updated to require confirmed type-effectiveness data to prevent hallucinations.
- `navigator_agent` (ACTIVE): A consolidated agent for both targeted pathfinding and exploration.
- `spinner_maze_solver_agent` (ACTIVE): A specialized agent for solving spinner tile mazes.

## VII. Completed Intel
- **Celadon Diner Tip:** An NPC at (2, 5) in the Celadon Diner revealed there is a secret basement under the Game Corner. This led to finding the poster switch.
- **Lift Key Location:** Discovered I already possessed the Lift Key.