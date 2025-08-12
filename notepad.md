# I. Game Mechanics (Verified)
## A. Tile Traversal & Interaction Rules
- **ground:** Standard walkable tile.
- **grass:** Tall grass where wild Pokémon appear. Walkable.
- **water:** Requires Surf to traverse. Cannot be walked on.
- **impassable:** Cannot be walked on. Includes walls, rocks, and some decorative objects.
- **elevated_ground:** Walkable, but at a different elevation. Can only be accessed via 'steps' or by dropping down from above.
- **steps:** Allows movement between 'ground' and 'elevated_ground'.
- **ladder_up / ladder_down:** Acts as a warp between floors.
- **ledge:** A one-way drop. Can be jumped down from an adjacent tile above, landing on the tile two spaces below the starting point.
- **cleared_boulder_barrier:** A former barrier that now acts as a one-way ramp, allowing movement *up* from 'ground' to 'elevated_ground', but not down.
- **hole:** A tile that drops a pushed boulder to the floor below.
- **boulder_barrier:** An impassable barrier that can be cleared by a `boulder_switch`.
- **boulder_switch:** A floor switch that opens a `boulder_barrier` when a boulder is pushed onto it.

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
- **Future Agent Idea: journey_planner:** An agent that can devise multi-map routes involving different modes of travel (walking, surfing).
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