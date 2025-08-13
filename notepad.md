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
  - Ground > Fire, Electric, Rock
  - Ice > Ground, Grass, Flying, Dragon
  - Flying > Fighting, Grass, Bug
  - Fighting > Normal, Rock, Ice
  - Electric > Water, Flying

- **Not Very Effective (0.5x damage):**
  - Normal !> Rock

- **Immune (0x damage):**
  - Ground immune to Electric
  - Flying immune to Ground

# III. Strategic Planning & Self-Correction

## A. Core Directives & Methodological Failures
- **Immediate Action Mandate (CRITICAL FAILURE):** I have repeatedly deferred documentation and tool maintenance instead of performing them immediately. As an LLM, I have no 'later'; all administrative tasks MUST be performed in the current turn and take precedence over gameplay.
- **Tool Maintenance Mandate (CRITICAL FAILURE):** I deferred fixing my broken `generate_path_plan` tool in Victory Road, violating the core directive that maintaining automation is the highest priority. Faulty tools must be fixed immediately.
- **Agent Engineering Failure (`battle_strategist_agent`):** I failed to correctly engineer the `battle_strategist_agent`'s prompt, leading to repeated dangerous suggestions. After multiple failed refinements, I resorted to 'lobotomizing' it by removing its ability to suggest switches. This represents a failure in problem-solving. I must strive to master complex agent engineering rather than simplifying tools to the point of reduced utility.
- **Scientific Mindset & Hypothesis Testing:**
  - **Flawed Observation:** My errors with the boulder pushing mechanic highlight a need for more meticulousness. I must observe, form a single testable hypothesis, document, test, and then attempt to *falsify* the conclusion.
  - **Confirmation Bias:** My fixation on a single boulder on Victory Road 3F was a critical error. When a primary hypothesis repeatedly fails, I must actively seek to falsify it by testing alternative routes and solutions.

## B. Future Automation Pipeline
- **Agent Idea: `journey_planner`:** Devises multi-map routes involving different travel modes (walking, surfing).
- **Agent Idea: `puzzle_master_agent`:** High-level agent to orchestrate `boulder_move_finder` and `boulder_path_planner` for complete puzzle solutions.
- **Tool Idea: `map_navigator_assistant`:** Parses `map_xml_string` to find key interactable objects (PC, Nurse) and returns their coordinates and the correct tile for interaction.
- **Tool Idea: `multi_modal_pathfinder`:** Calculates a single path across disconnected landmasses and water bodies.

# V. Archived Logs

# V. Gameplay & Interaction Rules
- **PC Interaction:** To use a PC, the player must stand on the tile directly *below* it and be facing *up* before pressing 'A'. The object name in the map data is typically `OpenPokemonCenterPC`.

# VI. Future Automation Ideas
- **Tool Idea: `map_navigator_assistant`:** A tool that parses `map_xml_string` to find key interactable objects (e.g., 'PC', 'Nurse', 'Clerk') and returns their coordinates along with the correct tile to stand on for interaction. This would prevent wasting time on incorrect interaction attempts.
- **Agent Failure (`battle_strategist_agent`):** The agent has repeatedly recommended switching in a severely underleveled Pokémon (Lv33 Kadabra vs Lv57 Hitmonchan), ignoring the level disparity veto. This is a critical flaw. I am attempting a third, more forceful prompt revision to fix this before continuing.