# I. Core Directives & Lessons

## A. Core Directives
1.  **IMMEDIATE MAINTENANCE:** All data management (notepad, markers) and tool/agent refinement is the HIGHEST priority and MUST be performed in the same turn a need is identified.
2.  **PROACTIVE AUTOMATION:** Before any complex or repetitive task, I must first consider automating it with a tool or agent. If one doesn't exist, creating it is the new priority.
3.  **TRUST, BUT REFINE:** I must trust the outputs of my agents and system data. If an agent or tool is suboptimal, I must prioritize refining it immediately. A tool's error message about its inputs is a reflection of my data quality, not a flaw in the tool.
4.  **TRUST GAME STATE OVER TOOLS:** If a tool's output contradicts the Game State Information, my assumption must be that the tool is wrong. I must prioritize debugging the tool.
5.  **ABANDON FAILED HYPOTHESES:** If a strategy fails repeatedly, I must recognize the pattern, document it, and pivot to a new approach. I must not get stuck on a single solution and be flexible.

## B. Key Lessons & Recurring Failures
- **CRITICAL: DATA VERIFICATION:** My most severe failures stem from hallucinating my location or other game state variables. I MUST verify my current map ID, coordinates, and other data from the Game State Information *before* every single action. Trust the data, not my memory.
- **Positional & Data Awareness:** I must verify my current coordinates, turn number, and system-provided data from the Game State Information *before* every action and trust it over my own manual assessment.
- **Confirmation Bias:** My biggest failure is assuming my code is wrong when a tool fails, instead of testing the hypothesis that my input data is wrong (e.g., Cerulean Cave B1F partition issue). I must verify data quality first before debugging code. I must also actively try to disprove my own assumptions (e.g., assuming high encounter rate was a puzzle, or that 3 failed escapes was just RNG).
- **Notepad Precision:** Repeated failures with `notepad_edit` `replace` operations highlight a need for greater precision. I must use the system's suggestions and be exact with `old_text`.
- **Deferred Maintenance:** I have a history of identifying broken tools (like `automated_path_navigator`, `menu_analyzer`, `auto_battle_selector`) and failing to fix them immediately. This is a critical violation of my core directives and must be corrected.
- **State Tracking:** I must improve my tracking of my own actions to avoid repeating tasks I have already completed (e.g., deleting an agent twice, redefining a fixed tool).

# II. Game Mechanics & World Data

## A. Discovered Mechanics
- **System 'Dead End' Definition:** An area is NOT a 'dead end' if the total of reachable non-adjacent warps (or warp groups) and reachable map connections is 2 or more. This is evaluated on a whole-map basis, even if the player is in a partition with only one exit. (Corrected on Turn 200952 after system warning).
- **Trap Battles:** Certain wild encounters, particularly in late-game areas like Cerulean Cave, appear to be 'trap' battles where the 'RUN' option is disabled. This was observed with a Wigglytuff, suspected with a Ditto, and confirmed with a KADABRA.
- **Fainted HM Usage:** HMs like Surf can be used outside of battle even if the Pokémon that knows the move has fainted. (Confirmed by system notice on Turn 199815).
- **1x1 Warp Tiles (Instant):** Most 1x1 warps trigger instantly upon stepping on them. To re-use the warp, you must step off the tile and then back on.
- **1x1 Warp Tiles (Non-Instant):** Some 1x1 warps require a second input. After stepping on the warp tile, you must press the directional button that moves you *into* the building's impassable boundary to trigger the warp.
- **Lead Pokémon HM Bug:** Using an HM move (like SURF) with a Pokémon that is not in the first party slot can cause the lead Pokémon to use a different HM instead (e.g., STRENGTH). Hypothesis: The Pokémon using the HM must be in the lead to function correctly. Test Plan: After this battle, attempt to use SURF with TITANESS in the second party slot to see if the bug is consistently reproducible. This will help confirm if the 'lead Pokémon' is the only variable.
- **Potential Ground Immunity:** A wild LICKITUNG (Lv 61) in Cerulean Cave took no damage from the Ground-type move EARTHQUAKE. It was defeated by the Rock-type move ROCK SLIDE. This suggests a potential type immunity or a specific battle mechanic. **Test Plan:** Encounter another Lickitung and test with a different Ground move (e.g., Bonemerang) to confirm.

## B. Solved Puzzles
- **Snorlax (Routes 11 & 12):** Awakened using the POKé FLUTE from the ITEM menu.
- **Pokémon Tower Ghost:** Used SILPH SCOPE to reveal the ghost.
- **Seafoam Islands Current:** Solved multi-floor boulder puzzle to stop the strong water current.
- **Pewter Museum Puzzle:** Solved by a sequence of interactions with the Aerodactyl Fossil and an invisible follower Pikachu, which caused a blocking Youngster to move.
- **Cerulean Cave B1F Encounter Trap:** The high encounter rate at (2, 7) was not a scripted puzzle but simply high RNG. The solution was to move one tile at a time and run from each battle.

# III. Current Objectives & Hypotheses

## A. Current Main Objective
- **Defeat SMITH:** Prepare for and win the rematch against SMITH in Cerulean Cave.
- **Capture Mewtwo:** After defeating SMITH, find and capture the legendary Pokémon Mewtwo.

## B. Active Hypotheses & Test Plans
- **Light Screen Duration:** Hypothesis: Light Screen lasts for 5 turns, as is standard. Test Plan: In a future battle, count the turns after using Light Screen and watch for the 'Light Screen wore off!' message to confirm its duration.
- **Respawn Point:** Hypothesis: The game sets the last used Pokémon Center as the respawn point after a blackout. Test Plan: Heal at a new Pokémon Center, then intentionally black out to a weak wild Pokémon and observe the respawn location.
- **Hidden Passages:** Hypothesis: Some 'impassable' walls in Cerulean Cave are secret passages. Test Plan: Systematically walk into different types of wall tiles in the current partition to test for fake walls. Mark tested walls with a map marker.

## C. Disproven Hypotheses
- **Menu Selection Bug:** Hypothesis: Selecting a Pokémon in the 'Bring out which POKéMON?' menu consistently opens the sub-menu for a different Pokémon. **(Disproven on Turn 197844)** Test: Selected REVENANT. Result: REVENANT's sub-menu opened. Conclusion: The bug is not a simple mis-selection of an adjacent Pokémon.
- **Route 7 Training Spot:** Hypothesis: Route 7 is a good location for training NIGHTSHADE. **(Disproven on Turn 200582)** Test: Battled wild Pokémon. Result: Wild Pokémon were Lv 22-23, yielding minimal EXP. Conclusion: Route 7 is not a viable training spot for a Lv 44 Pokémon.

# IV. Major Battle Data

### 1. Sabrina (Saffron City Gym)
- **Roster:**
    - MR. MIME (Lv 65) - Moves: PSYCHIC
    - HYPNO (Lv 64) - Moves: PSYWAVE
    - SLOWBRO (Lv 64) - Moves: PSYCHIC
    - JYNX (Lv 64) - Moves: BLIZZARD, BUBBLEBEAM, DREAM EATER, LOVELY KISS
    - GENGAR (Lv 64) - Moves: NIGHT SHADE, PSYCHIC
    - ALAKAZAM (Lv 65) - Moves: THUNDER WAVE, PSYCHIC

### 2. SMITH (Cerulean Cave B1F)
- **Roster:**
    - AERODACTYL (Lv 65) - Moves: HYPER BEAM, ROCK SLIDE

### 3. Cerulean Cave Wild Pokémon
- **Observed Species & Moves:**
    - WIGGLYTUFF (Lv 62) - Moves: LOVELY KISS, DOUBLE-EDGE, REST
    - SANDSLASH (Lv 63) - Moves: SWORDS DANCE, EARTHQUAKE
    - GOLEM (Lv 64) - Moves: EXPLOSION
    - LICKITUNG (Lv 61): Moves: WRAP
    - CHANSEY (Lv 63): Moves: DEFENSE CURL, MEGA PUNCH
    - RAICHU (Lv 64): Moves: AGILITY

# V. New Ideas & Hypotheses (Post-Reflection)

## A. Tool Ideas
- **Persistent Navigator Tool:** Create a new tool that combines pathfinding with battle-interruption handling. It would take a destination, attempt to follow the path, and if a wild battle occurs, automatically execute the 'RUN' command and then attempt to resume pathing from the new location. This would automate the tedious and error-prone manual process I'm currently using.

## B. New Hypotheses
- **Scripted High Encounter Rate:** Hypothesis: Certain corridors and tiles in Cerulean Cave (especially on 2F) have a scripted, abnormally high encounter rate, rather than it being purely random chance. **Test Plan:** Once the party is healed, return to the corridors on 2F where encounters were frequent (e.g., around (26,8), (10,15)) and walk back and forth on a small set of tiles for a fixed duration (e.g., 2 minutes) to measure the number of encounters. Compare this to a control area on 1F. This will help determine if it's a feature of the area or just bad luck.
- **Sleeping HM Usage:** A Pokémon with the Sleep status condition CAN use an HM move (like Surf) outside of battle. (Confirmed on Turn 201076 in Cerulean Cave 1F).
- **Elevated Ground:** Movement between `ground` and `elevated_ground` is only possible via `steps` tiles. Direct movement between them is impossible.