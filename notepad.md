# I. Game Mechanics (Verified)
## A. Tile Traversal & Interaction Rules (Player-Discovered)
- **cleared_boulder_barrier:** A former barrier that now acts as a one-way ramp, allowing movement *up* from 'ground' to 'elevated_ground', but not down.

## B. Boulder Pushing
- **Core Mechanic:** When adjacent to a boulder, a single button press can both turn the player and push the boulder one tile. The player's position does not change during the push, regardless of direction (vertical or horizontal). To continue pushing, the player must walk to an adjacent tile to the boulder's new position.
- **Illegal Moves:** Boulders CANNOT be pushed onto 'steps' tiles.

## C. General Mechanics
- **Menu Navigation:** The 'B' button is the primary method for exiting/canceling out of menus.

# II. Battle Intelligence
## A. Type Effectiveness Chart (Verified)
- **Super Effective (2x damage):**
  - Water > Rock, Ground, Fire
  - Ground > Fire, Electric, Rock, Ground
  - Ice > Ground, Grass, Flying, Dragon
  - Flying > Fighting, Grass, Bug
  - Fighting > Normal, Rock, Ice
  - Electric > Water, Flying

- **Not Very Effective (0.5x damage):**
  - Normal !> Rock

- **Immune (0x damage):**
  - Ground immune to Electric
  - Flying immune to Ground

# III. Elite Four Preparation
- **Objective:** Assemble the optimal team of 6 Pokémon to challenge the Elite Four.
- **Methodology:**
  1. Systematically collate data for all current party members and top PC candidates using the `data_collation_agent`.
  2. Feed the collated data into the `team_composition_advisor` agent to receive a strategic recommendation.
  3. Reorganize party based on the agent's advice, retrieving necessary Pokémon from the PC.
  4. Final check of movesets and levels before proceeding to the Indigo Plateau.

# IV. Methodological Corrections & Ideas
- **Internal State Desynchronization (CRITICAL FAILURE):** I got stuck in a multi-turn loop trying to edit my notepad because I failed to recognize it was already correct. I must always verify the current state of my documentation before attempting to change it to prevent such catastrophic failures in self-awareness.
- **Flawed Observation & Hypothesis Testing:** My repeated errors in understanding the boulder pushing mechanic highlight a major weakness. I must be more meticulous: observe a mechanic, form a single testable hypothesis, document it, test it, and then try to *falsify* the conclusion before accepting it as fact. This will prevent inefficient trial-and-error.
- **Deferred Data Management (CRITICAL FAILURE):** During my self-reflection, I identified an instance where I deferred a notepad update instead of performing it immediately. As an LLM, I have no 'later'; actions must be taken in the current turn. This is a critical directive I must adhere to.
- **Confirmation Bias Warning (Victory Road 3F):** My focus on the boulder at (25, 11) was a classic case of confirmation bias. I assumed it was the only solution because it was the most obvious boulder, and kept trying to make it work, instead of exploring other possibilities on the map (like the hole or unvisited warps). When a primary hypothesis is repeatedly failing, I must actively seek to falsify it by testing alternative routes and solutions. This is critical to avoid getting stuck in loops.
- **Deferred Tool Maintenance (CRITICAL FAILURE):** During my attempts to navigate Victory Road, I repeatedly deferred fixing my broken `generate_path_plan` tool, opting for manual navigation instead. This violates the core directive that maintaining automation is the highest priority. I must fix broken tools immediately.
- **Future Agent Idea: journey_planner:** An agent that can devise multi-map routes involving different modes of travel (walking, surfing).
- **Future Agent Idea: puzzle_master_agent:** A high-level agent that analyzes a puzzle map (like a boulder room) and orchestrates the use of lower-level tools (`boulder_move_finder`, `boulder_path_planner`) to generate a complete, step-by-step solution for the entire puzzle.
- **Future Tool Idea: multi_modal_pathfinder:** A tool that can calculate a single path across disconnected landmasses and water bodies.

# V. Archived Logs
## A. Tool Debugging Log: generate_path_plan (Resolved)
- **Issue:** The tool's `get_neighbors` function had flawed logic, preventing it from finding valid paths across different tile types like `cleared_boulder_barrier` and `ground`.
- **Resolution:** The function was rewritten with systematic, state-based logic that correctly handles all known valid tile transitions. The tool is now reliable.

## B. Overwatch Critiques (Resolved)
### Turn 138180: Critical Tool Failure (generate_path_plan)
- **Critique:** Catastrophic failure in handling the `generate_path_plan` tool. Violated core directives by abandoning the tool instead of fixing it immediately, and the debugging process was unsystematic and chaotic.
- **Resolution:** Halting all gameplay progression. My sole focus is now on a systematic, methodical debugging process to fix this critical tool. I will rewrite the neighbor-finding logic from scratch with a clear, state-based model to eliminate bugs. I will not proceed until the tool is 100% reliable.

## C. Victory Road 2F Boulder Puzzle Log (Resolved)
- **Initial State:** Boulder at (3, 15), switch at (2, 17).
- **Solution (from `boulder_path_planner`):**
  - Step 1: Player moves to (2, 15), pushes boulder Right to (4, 15).
  - Step 2: Player moves to (4, 14), pushes boulder Down to (4, 16).
  - Step 3: Player moves to (4, 15), pushes boulder Down to (4, 17).
  - Step 4: Player moves to (5, 17), pushes boulder Left to (3, 17).
  - Step 5: Player moves to (4, 17), pushes boulder Left to (2, 17). **[COMPLETE]**
- **Agent Supervision:** My override of the `battle_strategist_agent` in turn 138620 was correct. Agents are powerful tools, but not infallible. I must continue to critically evaluate their output, especially in high-risk situations, and be prepared to make a different call if my analysis identifies a flaw or a safer path. An agent's advice is a strong suggestion, not an unbreakable command.