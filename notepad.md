# I. Core Gameplay Mechanics & Rules

## A. Player-Imposed Rules (Hard Mode)
- **Battle Style:** Set mode.
- **Items in Battle:** Prohibited.
- **Level Caps:** Active and enforced.

## B. Tile Traversal & Interaction
- **cleared_boulder_barrier:** Acts as a one-way ramp, allowing movement *up* from 'ground' to 'elevated_ground', but not down.
- **PC Interaction:** To use a PC, stand on the tile directly *below* it and face *up* before pressing 'A'.

## C. Boulder Pushing Mechanics
- **Core Mechanic:** A single button press can both turn the player and push an adjacent boulder one tile. The player's position does not change during the push.
- **Illegal Moves:** Boulders CANNOT be pushed onto 'steps' tiles.

## D. General Mechanics
- **Menu Navigation:** The 'B' button is the primary method for exiting/canceling out of menus.
- **Opponent Abilities:** Some Pokémon, like Poliwrath, may have abilities like Water Absorb that nullify certain move types.

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

# V. Gameplay & Interaction Rules
- **PC Interaction:** To use a PC, the player must stand on the tile directly *below* it and be facing *up* before pressing 'A'. The object name in the map data is typically `OpenPokemonCenterPC`.

# VI. Future Automation Ideas
- **Tool Idea: `map_navigator_assistant`:** A tool that parses `map_xml_string` to find key interactable objects (e.g., 'PC', 'Nurse', 'Clerk') and returns their coordinates along with the correct tile to stand on for interaction. This would prevent wasting time on incorrect interaction attempts.
- **Agent Failure (`battle_strategist_agent`):** The agent has repeatedly recommended switching in a severely underleveled Pokémon (Lv33 Kadabra vs Lv57 Hitmonchan), ignoring the level disparity veto. This is a critical flaw. I am attempting a third, more forceful prompt revision to fix this before continuing.