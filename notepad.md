# I. Core Directives & Lessons

## A. Core Directives
1.  **IMMEDIATE MAINTENANCE:** All data management (notepad, markers) and tool/agent refinement is the HIGHEST priority and MUST be performed in the same turn a need is identified.
2.  **PROACTIVE AUTOMATION:** Before any complex or repetitive task, I must first consider automating it with a tool or agent. If one doesn't exist, creating it is the new priority.
3.  **TRUST, BUT REFINE:** I must trust the outputs of my agents and system data. If an agent or tool is suboptimal, I must prioritize refining it immediately. A tool's error message about its inputs is a reflection of my data quality, not a flaw in the tool.
4.  **TRUST GAME STATE OVER TOOLS:** If a tool's output (e.g., 'no path found') contradicts the Game State Information (e.g., a listed reachable warp), my assumption must be that the tool is wrong. I must prioritize debugging the tool instead of repeatedly trusting its faulty output.
5.  **ABANDON FAILED HYPOTHESES:** If a strategy fails repeatedly, I must recognize the pattern, document it, and pivot to a new approach. I must not get stuck on a single solution and be flexible.

## B. Key Lessons & Recurring Failures
- **Positional & Data Awareness:** I must verify my current coordinates, turn number, and system-provided data from the Game State Information *before* every action and trust it over my own manual assessment.
- **System vs. Local Reachability:** System warnings about 'reachable' tiles/warps are a global check for the entire map and may not reflect what is reachable from my current partitioned location.
- **Confirmation Bias in Problem-Solving:** My biggest failure is assuming my code is wrong when a tool fails, instead of testing the hypothesis that my input data is wrong. I must verify data quality first before debugging code. A specific example is when my pathfinder correctly identified Cerulean Cave B1F as partitioned, but I assumed the tool was bugged because the global 'reachable unseen tiles' count was non-zero. I wasted many turns debugging a correct tool instead of questioning my interpretation of the data.
- **Notepad Precision:** Repeated failures with `notepad_edit` `replace` operations highlight a need for greater precision. I must use the system's suggestions and be exact with `old_text` to ensure critical updates are performed on the first attempt.

# II. Game Mechanics & World Data

## A. Tile Mechanics
- **ground:** Standard walkable tile.
- **elevated_ground:** Walkable tile at a different elevation. Cannot be accessed from `ground` directly.
- **steps:** The only tile type that allows movement between `ground` and `elevated_ground`.
- **ladder_up / ladder_down:** Warps between floors.
- **impassable:** Walls, rocks, etc. Cannot be entered.
- **water:** Can only be crossed with Surf.

## B. Interaction Rules & Game Systems
- **1x1 Warp Tiles:** To re-use a 1x1 warp tile after arriving on it, you must step off the tile onto an adjacent ground tile, then step back on.
- **Non-Instant Warps:** Some 1x1 warps are not instant. After stepping on the warp tile, you must press the directional button that moves you *into* the building's impassable boundary to trigger the warp.
- **Decorative Grass (Celadon Dept. Store):** The small grass patches inside the Celadon Department Store are impassable and act as walls, despite the 'grass' tile type sometimes being traversable outdoors.

## C. Solved Puzzles
- **Snorlax (Routes 11 & 12):** Awakened using the POKé FLUTE from the ITEM menu.
- **Pokémon Tower Ghost:** Used SILPH SCOPE to reveal the ghost.
- **Seafoam Islands Current:** Solved multi-floor boulder puzzle to stop the strong water current.
- **Pewter Museum Puzzle:** Solved by a sequence of interactions with the Aerodactyl Fossil and an invisible follower Pikachu, which caused a blocking Youngster to move.

# III. Current Objectives & Hypotheses

## A. Current Main Objective
- **Capture Mewtwo:** I need to stock up on Ultra Balls and then travel to Cerulean Cave to find and capture Mewtwo.

## B. Active Hypotheses & Test Plans
- **Menu Cursor Reset:** Hypothesis: The game resets the cursor to the first Pokémon in the list in the 'Bring out which POKéMON?' menu if a turn passes without a selection. Test Plan: Next time I am in this specific menu, I will manually move the cursor to a different Pokémon, wait one turn, and observe if the cursor position changes.
- **Light Screen Duration:** Hypothesis: Light Screen lasts for 5 turns, as is standard. Test Plan: In a future battle, count the turns after using Light Screen and watch for the 'Light Screen wore off!' message to confirm its duration.
- **Respawn Point:** Hypothesis: The game sets the last used Pokémon Center as the respawn point after a blackout. Test Plan: Heal at a new Pokémon Center, then intentionally black out to a weak wild Pokémon and observe the respawn location.

## C. Disproven Hypotheses
- **Menu Selection Bug:** Hypothesis: Selecting a Pokémon in the 'Bring out which POKéMON?' menu consistently opens the sub-menu for a different Pokémon. **(Disproven on Turn 197844)** Test: Selected REVENANT. Result: REVENANT's sub-menu opened. Conclusion: The bug is not a simple mis-selection of an adjacent Pokémon.

# IV. Tool & Agent Development

## A. Defined Tools & Agents
### Custom Tools
- **menu_analyzer:** Parses menu screen text to identify options and cursor position.
- **automated_path_navigator:** Finds the shortest path between two points on the current map.
- **elevator_navigator:** Parses the Celadon Dept. Store elevator menu screen text, and given a target floor (e.g., '2F'), calculates the button presses needed to select it.
### Custom Agents
- **exploration_strategist_agent:** Analyzes a high-level exploration goal, a list of previously failed/explored locations, and the current map's connections to suggest the next most logical area (map or warp) to investigate.
- **puzzle_solver_agent:** Generates new hypotheses for complex puzzles.
- **notepad_refactor_agent:** Generates `replace` operations for major notepad reorganization.
- **comprehensive_battle_agent:** Provides both pre-battle team composition advice and turn-by-turn tactical recommendations.
- **store_navigator_agent:** A high-level agent to devise exploration strategies for multi-floor buildings like department stores or Silph Co.

## B. Development Ideas
- **Debugging Assistant Agent:** An agent that could take a tool's code, error messages, and debug logs as input to suggest potential bugs and more effective test cases. This would streamline the debugging process for complex tool failures.

# V. Major Battle Data

### 1. Sabrina (Saffron City Gym)
- **Roster:**
    - MR. MIME (Lv 65) - Moves: PSYCHIC
    - HYPNO (Lv 64) - Moves: PSYWAVE
    - SLOWBRO (Lv 64) - Moves: PSYCHIC
    - JYNX (Lv 64) - Moves: BLIZZARD, BUBBLEBEAM, DREAM EATER, LOVELY KISS
    - GENGAR (Lv 64) - Moves: NIGHT SHADE, PSYCHIC
    - ALAKAZAM (Lv 65) - Moves: THUNDER WAVE, PSYCHIC

# VI. Long-Term Plans & Strategies

## A. Operation: Capture Mewtwo
- **Location:** Cerulean Cave (accessed via Cerulean Gym).
- **Team Strategy:**
    - **Status Inflictor:** TITANESS (Body Slam for paralysis) or SPARKY (Thunder Wave). Sleep is preferable if available. NIGHTSHADE's Sleep Powder could work if it can survive.
    - **Damage Dealer:** REVENANT (Bonemerang/Earthquake) to lower Mewtwo's health carefully. Need to avoid a critical hit KO.
    - **Utility:** A Pokémon with Surf is required for cave navigation (TITANESS or NEPTUNE).
- **Required Items:**
    - Purchase a large stock of Ultra Balls from a Poké Mart.
    - Bring Max Potions and Full Heals for the battle.
    - The MASTER BALL is the final fallback option.
- **Execution Plan:**
    1. Heal party at a Pokémon Center.
    2. Fly to a city with a Mart (like Celadon) to stock up on Ultra Balls.
    3. Fly to Cerulean City.
    4. Enter Cerulean Cave and navigate to Mewtwo's location.
    5. Save before initiating the battle.
    6. Inflict status, lower HP, and begin throwing Ultra Balls.

# VII. Active Puzzles

## A. Cerulean Cave B1F - Encounter Trap
- **Observation:** At tile (2, 7), any attempt to move triggers a wild Pokemon encounter with what appears to be a 100% success rate. This effectively traps me. The goal is to reach the ladder at (4, 7).
- **Failed Hypotheses:**
    - H1: Brute-force movement will eventually succeed. (Failed 8+ times)
    - H2: Moving in a different direction (e.g., up) will bypass the trigger. (Failed 1 time)
    - H3: Interacting with the adjacent follower Pikachu will resolve the puzzle. (Failed 1 time)