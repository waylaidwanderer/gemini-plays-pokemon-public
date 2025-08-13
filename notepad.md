# I. Core Gameplay & Battle Intelligence

## A. Game Mechanics (Verified)
- **Battle Style:** Set mode.
- **Items in Battle:** Prohibited.
- **Level Caps:** Active and enforced.
- **PC Interaction:** To use a PC, stand on the tile directly *below* it and face *up* before pressing 'A'.
- **Menu Navigation:** The 'B' button is the primary method for exiting/canceling out of menus.
- **Elite Four Room Progression:** Attempting to leave a room south triggers a 'Don't run away!' event, which is the key to unlocking the northern warp.
- **Defeated Elite Four Trainers:** Become impassable obstacles after their defeat speech.

## B. Tile Mechanics & Traversal
- **`cleared_boulder_barrier`:** Acts as a one-way ramp, allowing movement *up* from 'ground' to 'elevated_ground', but not down. (Hypothesis - needs more testing).
- **Boulder Pushing:** A single button press can both turn the player and push an adjacent boulder one tile. The player's position does not change during the push. Boulders CANNOT be pushed onto 'steps' tiles.

## C. Type Effectiveness Chart (Verified)
- **Super Effective (2x damage):**
  - Water > Rock, Ground, Fire
  - Ground > Fire, Electric, Rock, Ghost
  - Ice > Ground, Grass, Flying, Dragon
  - Flying > Fighting, Grass, Bug
  - Fighting > Normal, Rock, Ice
  - Grass > Ground, Rock

- **Not Very Effective (0.5x damage):**
  - Normal !> Rock
  - Ice !> Fighting

- **Immune (0x damage):**
  - Ground immune to Electric
  - Flying immune to Ground

# II. Strategic Directives & Automation

## A. Core Methodological Failures (Lessons Learned)
- **Immediate Action Mandate (CRITICAL FAILURE):** I have repeatedly deferred documentation and tool maintenance instead of performing them immediately. As an LLM, I have no 'later'; all administrative tasks MUST be performed in the current turn and take precedence over gameplay.
- **Tool Maintenance Mandate (CRITICAL FAILURE):** I deferred fixing my broken `generate_path_plan` tool in Victory Road, violating the core directive that maintaining automation is the highest priority. Faulty tools must be fixed immediately.
- **Agent Engineering Failure (`battle_strategist_agent`):** I failed to correctly engineer the `battle_strategist_agent`'s prompt and input schema, leading to suboptimal suggestions. I must prioritize iterative refinement of agents.
- **Scientific Mindset & Hypothesis Testing:** My fixation on a single solution path must be avoided. When a primary hypothesis repeatedly fails, I must actively seek to falsify it by testing alternative routes and solutions. I must be more meticulous in observing, forming a single testable hypothesis, documenting, testing, and then attempting to *falsify* the conclusion.

## B. Future Automation Pipeline
- **Agent Idea: `journey_planner`:** Devises multi-map routes involving different travel modes (walking, surfing).
- **Agent Idea: `puzzle_master_agent`:** High-level agent to orchestrate `boulder_move_finder` and `boulder_path_planner` for complete puzzle solutions.
- **Tool Idea: `map_navigator_assistant`:** Parses `map_xml_string` to find key interactable objects (PC, Nurse) and returns their coordinates and the correct tile for interaction.
- **Tool Idea: `multi_modal_pathfinder`:** Calculates a single path across disconnected landmasses and water bodies.
- **Agent Idea: `party_viability_assessor`:** Analyzes party HP, status, and type matchups against a known opponent to rank the survivability/viability of each potential switch-in during desperate situations.

# III. Battle Logs

## A. Elite Four Attempts

### Attempt 1 vs. Agatha (Loss)
- **Opponent's Pokémon:**
  - Gengar (Lv 57) - Known Moves: Mega Drain, Hypnosis, Night Shade
- **Key Learnings:**
  - Gengar's Grass-type move Mega Drain is devastating to Rock/Ground types (4x weakness).
  - Hypnosis is a major threat, capable of disabling key Pokémon. My current team lacks a reliable counter to sleep.
  - A high-level Psychic-type or a fast, powerful special attacker is needed to take out Gengar quickly. My current team composition is not viable for this fight.

# IV. Archived Logs
(Placeholder for future logs)
- **Indigo Plateau Lobby:** The lobby is split into two disconnected sections. The western side is the challenge area, and the eastern side has the Pokémon Center/Mart. Once you enter the western side, you cannot return to the eastern side to heal without defeating the Elite Four or blacking out.