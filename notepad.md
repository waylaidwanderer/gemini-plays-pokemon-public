# I. Core Directives & Lessons

## A. Core Directives
1.  **IMMEDIATE MAINTENANCE:** All data management (notepad, markers) and tool/agent refinement is the HIGHEST priority and MUST be performed in the same turn a need is identified.
2.  **PROACTIVE AUTOMATION:** Before any complex or repetitive task, I must first consider automating it with a tool or agent. If one doesn't exist, creating it is the new priority.
3.  **TRUST, BUT REFINE:** I must trust the outputs of my agents and system data. If an agent or tool is suboptimal, I must prioritize refining it immediately. A tool's error message about its inputs is a reflection of my data quality, not a flaw in the tool.
4.  **TRUST GAME STATE OVER TOOLS:** If a tool's output contradicts the Game State Information, my assumption must be that the tool is wrong. I must prioritize debugging the tool.
5.  **ABANDON FAILED HYPOTHESES:** If a strategy fails repeatedly, I must recognize the pattern, document it, and pivot to a new approach. I must not get stuck on a single solution and be flexible.

## B. Key Lessons & Recurring Failures
- **Positional & Data Awareness:** I must verify my current coordinates, turn number, and system-provided data from the Game State Information *before* every action and trust it over my own manual assessment.
- **Confirmation Bias:** My biggest failure is assuming my code is wrong when a tool fails, instead of testing the hypothesis that my input data is wrong (e.g., Cerulean Cave B1F partition issue). I must verify data quality first before debugging code. I must also actively try to disprove my own assumptions (e.g., assuming high encounter rate was a puzzle, or that 3 failed escapes was just RNG).
- **Notepad Precision:** Repeated failures with `notepad_edit` `replace` operations highlight a need for greater precision. I must use the system's suggestions and be exact with `old_text`.
- **Deferred Maintenance:** I have a history of identifying broken tools (like `automated_path_navigator`, `menu_analyzer`, `auto_battle_selector`) and failing to fix them immediately. This is a critical violation of my core directives and must be corrected.
- **State Tracking:** I must improve my tracking of my own actions to avoid repeating tasks I have already completed (e.g., deleting an agent twice).

# II. Game Mechanics & World Data

## A. Tile Mechanics
- **ground:** Standard walkable tile.
- **elevated_ground:** Walkable tile at a different elevation. Cannot be accessed from `ground` directly.
- **steps:** The only tile type that allows movement between `ground` and `elevated_ground`.
- **impassable:** Walls, rocks, etc. Cannot be entered.
- **water:** Can only be crossed with Surf.
- **ledge:** One-way tile. Can be jumped down, but not climbed up.
- **cuttable:** A tree that can be cut with HM Cut. Becomes `ground` after cutting but respawns.
- **warp tiles:** Includes `ladder_up`, `ladder_down`, `teleport`, `hole`. These tiles move the player to a new location.

## B. Interaction Rules & Game Systems
- **1x1 Warp Tiles:** To re-use a 1x1 warp tile after arriving on it, you must step off the tile onto an adjacent ground tile, then step back on.
- **Non-Instant Warps:** Some 1x1 warps are not instant. After stepping on the warp tile, you must press the directional button that moves you *into* the building's impassable boundary to trigger the warp.
- **System 'Dead End' Definition:** An area is NOT a 'dead end' if the entire map contains 2 or more reachable warps/connections, even if those exits are in different, unreachable partitions from the player's current location.
- **Decorative Grass (Celadon Dept. Store):** The small grass patches inside the Celadon Department Store are impassable.

## C. Solved Puzzles
- **Snorlax (Routes 11 & 12):** Awakened using the POKé FLUTE from the ITEM menu.
- **Pokémon Tower Ghost:** Used SILPH SCOPE to reveal the ghost.
- **Seafoam Islands Current:** Solved multi-floor boulder puzzle to stop the strong water current.
- **Pewter Museum Puzzle:** Solved by a sequence of interactions with the Aerodactyl Fossil and an invisible follower Pikachu, which caused a blocking Youngster to move.
- **Cerulean Cave B1F Encounter Trap:** The high encounter rate at (2, 7) was not a scripted puzzle but simply high RNG. The solution was to move one tile at a time and run from each battle.

# III. Current Objectives & Hypotheses

## A. Current Main Objective
- **Heal Party:** My party is in critical condition, with two Pokémon fainted. I must find an exit from Cerulean Cave and get to a Pokémon Center.
- **Find Exit:** The immediate goal is to navigate the cave's floors to find the main entrance/exit.

## B. Active Hypotheses & Test Plans
- **Light Screen Duration:** Hypothesis: Light Screen lasts for 5 turns, as is standard. Test Plan: In a future battle, count the turns after using Light Screen and watch for the 'Light Screen wore off!' message to confirm its duration.
- **Respawn Point:** Hypothesis: The game sets the last used Pokémon Center as the respawn point after a blackout. Test Plan: Heal at a new Pokémon Center, then intentionally black out to a weak wild Pokémon and observe the respawn location.
- **Cerulean Cave Exit Path:** Hypothesis: The ladder at (20, 8) on 2F is the next step in the path to the main cave area and the exit. Test Plan: Navigate to and use the ladder at (20, 8).

## C. Disproven Hypotheses
- **Menu Selection Bug:** Hypothesis: Selecting a Pokémon in the 'Bring out which POKéMON?' menu consistently opens the sub-menu for a different Pokémon. **(Disproven on Turn 197844)** Test: Selected REVENANT. Result: REVENANT's sub-menu opened. Conclusion: The bug is not a simple mis-selection of an adjacent Pokémon.
- **Cerulean Cave 'Trap' Battle:** Hypothesis: The wild Wigglytuff encounter on Cerulean Cave 2F is a 'trap' battle where running is impossible. **(Confirmed on Turn 199572)** Test: Attempted to run 10 times consecutively, all failed. Switched to an offensive strategy, which successfully ended the encounter.

# IV. Tool & Agent Development

## A. Defined Tools & Agents
### Custom Tools
- **menu_analyzer:** Parses menu screen text to identify options and cursor position.
- **select_menu_option:** Calculates button presses to navigate menus based on `menu_analyzer` output.
- **automated_path_navigator:** Finds the shortest path between two points on the current map.
- **elevator_navigator:** Automates floor selection in the Celadon Dept. Store elevator.
- **auto_battle_selector:** Reliably selects a main battle menu option (FIGHT, PKMN, ITEM, RUN).
### Custom Agents
- **navigation_strategist_agent:** Suggests high-level exploration strategies for complex areas.
- **puzzle_solver_agent:** Generates new hypotheses for complex puzzles.
- **notepad_refactor_agent:** Generates `replace` operations for major notepad reorganization.
- **comprehensive_battle_agent:** Provides pre-battle and in-battle tactical advice.
- **battle_anomaly_detector_agent:** Analyzes repeated battle events for hidden mechanics.

## B. Future Development Ideas
- **`comprehensive_battle_agent` (Enhancements):**
    - **Run vs. Fight Logic:** Add a module to decide whether to run from or fight a wild encounter based on party health, goal priority, and opponent threat level.
    - **Switch Advisor:** Incorporate logic to recommend the optimal Pokémon to switch to mid-battle, considering type matchups, HP, and status.
    - **Action Orchestrator:** Develop a high-level function that takes simple commands (e.g., 'switch to REVENANT') and orchestrates the necessary sequence of tool calls to execute it, streamlining complex menu navigation.

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

# VII. Area-Specific Data

## A. Cerulean Cave
- **Wild Pokémon Encounters:**
    - WIGGLYTUFF (Lv 62) - Moves: LOVELY KISS, DOUBLE-EDGE, DOUBLE-EDGE
    - SANDSLASH (Lv 63) - Moves: SWORDS DANCE
- `run_or_fight_agent` A specialized agent to decide whether to run from or fight a wild encounter based on current party HP/status, the wild Pokémon's species and level, and the current primary goal (e.g., prioritize running if the goal is to escape a dangerous area).