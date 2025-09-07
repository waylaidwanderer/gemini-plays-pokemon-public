# I. Core Directives & Lessons

## A. Core Directives
1.  **IMMEDIATE MAINTENANCE:** All data management (notepad, markers) and tool/agent refinement is the HIGHEST priority and MUST be performed in the same turn a need is identified.
2.  **PROACTIVE AUTOMATION:** Before any complex or repetitive task, I must first consider automating it with a tool or agent. If one doesn't exist, creating it is the new priority.
3.  **TRUST, BUT REFINE:** I must trust the outputs of my agents and system data. If an agent or tool is suboptimal, I must prioritize refining it immediately. A tool's error message about its inputs is a reflection of my data quality, not a flaw in the tool.
4.  **ABANDON FAILED HYPOTHESES:** If a strategy fails repeatedly, I must recognize the pattern, document it, and pivot to a new approach. I must not get stuck on a single solution and be flexible.

## B. Key Lessons & Recurring Failures
- **Positional & Data Awareness:** I must verify my current coordinates, turn number, and system-provided data from the Game State Information *before* every action and trust it over my own manual assessment.
- **System vs. Local Reachability:** System warnings about "reachable" tiles/warps are a global check for the entire map and may not reflect what is reachable from my current partitioned location.
- **Confirmation Bias in Problem-Solving:** My biggest failure is assuming my code is wrong when a tool fails, instead of testing the hypothesis that my input data is wrong. I must verify data quality first before debugging code.
- **Notepad Precision:** Repeated failures with `notepad_edit` `replace` operations highlight a need for greater precision. I must use the system's suggestions and be exact with `old_text` to ensure critical updates are performed on the first attempt.

# II. Game Mechanics & World Data

## A. Tile Traversal Rules
- **ground:** Standard walkable tile.
- **impassable:** Cannot be entered. Walls, rocks, etc.
- **elevated_ground:** Walkable, but can only be accessed from `steps` tiles or other `elevated_ground` tiles.
- **steps:** Allows movement between `ground` and `elevated_ground`.
- **ladder_up / ladder_down:** Acts as a warp to a different floor.
- **ledge:** A one-way obstacle. Can be jumped down (from Y-1 to Y+2 in one move), but not climbed up.
- **grass:** Tall grass where wild Pokémon can be encountered.
- **teleport:** An instant warp tile within the same logical location (e.g., inside a building).
- **unknown:** Tile type has not been visually confirmed.

## B. Solved Puzzles
- **Snorlax (Routes 11 & 12):** Awakened using the POKé FLUTE from the ITEM menu.
- **Pokémon Tower Ghost:** Used SILPH SCOPE to reveal the ghost.
- **Seafoam Islands Current:** Solved multi-floor boulder puzzle to stop the strong water current.
- **Pewter Museum Puzzle:** Solved by a sequence of interactions with the Aerodactyl Fossil and an invisible follower Pikachu, which caused a blocking Youngster to move.

## C. Obstacles & Solutions
- **Rocket Grunt (Mt. Moon B2F at 30, 12):** Blocking path south, demands a fossil to pass.
- **Officer Jenny (Cerulean City):** Blocking path east. The trigger is likely in another city.

# III. Current Objectives & Hypotheses

## A. Saffron Gym Maze
**Status:** Unsolved. My initial belief that the maze was solved was incorrect. Currently re-exploring warps systematically to map all connections and find the correct path to Sabrina.
**Goal:** Find the warp that connects to the final area with Sabrina and the exit at (9, 18).
**Method:** Systematically explore every warp departure point until all connections are mapped. Use the `stuck_navigator_agent` to identify the next unexplored, reachable warp. If all are explored, begin systematic re-exploration.

## B. Untested Hypotheses & Test Plans
- **Menu Cursor Reset:** Hypothesis: The game resets the cursor to the first Pokémon in the list in the 'Bring out which POKéMON?' menu if a turn passes without a selection. Test Plan: Next time I am in this specific menu, I will manually move the cursor to a different Pokémon, wait one turn, and observe if the cursor position changes.
- **Menu Selection Bug:** Hypothesis: The menu bug where selecting one Pokémon (CRAG) opened the sub-menu for another (ECHO) was a one-time glitch. Test Plan: I will attempt the same switch action again. If the bug reoccurs, it is a consistent, albeit strange, mechanic that needs to be documented and worked around.

# IV. Tool & Agent Development

## A. Defined Tools
- **menu_analyzer:** Parses menu screen text to identify options and cursor position.
- **select_battle_option:** Calculates button presses to navigate menus based on `menu_analyzer` output.
- **automated_path_navigator:** Finds the shortest path between two points on the current map.
- **automated_battle_move_selector:** Calculates button presses to select a move in battle.

## B. Defined Agents
- **stuck_navigator_agent:** Suggests high-level navigational pivots when pathfinding fails.
- **battle_strategist_agent:** Recommends the best action (move or switch) during a battle.
- **puzzle_solver_agent:** Generates new hypotheses for complex puzzles.
- **notepad_refactor_agent:** Generates `replace` operations for major notepad reorganization.
- **major_battle_strategist_agent:** Analyzes an opponent's known roster and the player's current party to suggest an optimal team order and lead Pokémon for any major battle.

## C. Future Development Ideas
- **Exploration Master Tool:** A high-level tool to automate the maze exploration loop.
- **Team Builder Agent:** An agent that can analyze my entire PC box and suggest an optimal team for a specific upcoming challenge.
- **Pokémon Switcher Tool:** A high-level tool that automates the entire process of switching Pokémon. It would take an agent's recommendation (e.g., 'Switch to Marowak'), then internally call `select_battle_option`, `menu_analyzer`, and `select_menu_option` to execute the necessary menu navigation automatically.

# V. Major Battle Data

### 1. Sabrina (Saffron City Gym)
- **Roster:**
    - MR. MIME (Lv 65) - Moves: PSYCHIC
    - HYPNO (Lv 64) - Moves: PSYWAVE
    - SLOWBRO (Lv 64) - Moves: PSYCHIC
    - JYNX (Lv 64) - Moves: BLIZZARD
    - GENGAR (Lv 64) - Moves: NIGHT SHADE
    - ALAKAZAM (Lv 65) - Moves: THUNDER WAVE, PSYCHIC

# VI. Interaction Rules
- **1x1 Warp Tiles:** To re-use a 1x1 warp tile after arriving on it, you must step off the tile onto an adjacent ground tile, then step back on. Attempting to press the direction of an impassable boundary while on the tile will not work.