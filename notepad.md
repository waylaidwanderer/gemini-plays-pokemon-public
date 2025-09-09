# I. Core Directives & Lessons

## A. Core Directives
1.  **IMMEDIATE MAINTENANCE:** All data management (notepad, markers) and tool/agent refinement is the HIGHEST priority and MUST be performed in the same turn a need is identified. Deferring these tasks is a critical failure.
2.  **PROACTIVE AUTOMATION:** Before any complex or repetitive task, I must first consider automating it with a tool or agent. If one doesn't exist, creating it is the new priority.
3.  **TRUST, BUT REFINE:** I must trust the outputs of my agents and system data. If an agent or tool is suboptimal, I must prioritize refining it immediately. A tool's error message about its inputs is a reflection of my data quality, not a flaw in the tool.
4.  **TRUST GAME STATE OVER TOOLS:** If a tool's output contradicts the Game State Information, my assumption must be that the tool is wrong. I must prioritize debugging the tool.
5.  **ABANDON FAILED HYPOTHESES:** If a strategy fails repeatedly, I must recognize the pattern, document it, and pivot to a new approach. I must not get stuck on a single solution and be flexible.

## B. Key Lessons & Recurring Failures
- **CRITICAL: DATA VERIFICATION:** My most severe failures stem from hallucinating my location or other game state variables. I MUST verify my current map ID, coordinates, and other data from the Game State Information *before* every single action. Trust the data, not my memory.
- **Positional & Data Awareness:** I must verify my current coordinates, turn number, and system-provided data from the Game State Information *before* every action and trust it over my own manual assessment.
- **Confirmation Bias:** My biggest failure is assuming my code is wrong when a tool fails, instead of testing the hypothesis that my input data is wrong (e.g., trying to path through a fence on Route 2). I must verify data quality first before debugging code. I must also actively try to disprove my own assumptions.
- **Notepad Precision:** Repeated failures with `notepad_edit` `replace` operations highlight a need for greater precision. I must use the system's suggestions and be exact with `old_text`.
- **Deferred Maintenance:** I have a history of identifying broken tools (like `automated_path_navigator`) and failing to fix them immediately. This is a critical violation of my core directives and must be corrected.
- **State Tracking:** I must improve my tracking of my own actions to avoid repeating tasks I have already completed.

# II. Game Mechanics & World Data
- **Trap Battles:** Certain wild encounters appear to be 'trap' battles where the 'RUN' option is disabled (Observed: Wigglytuff, KADABRA; Suspected: Ditto).
- **Fainted HM Usage:** A fainted Pokémon can still use field moves like CUT and Surf outside of battle.
- **Cycling Road Forced Movement:** On certain routes like Route 18, the player character experiences forced, multi-tile movement in a single direction, especially when moving downhill.
- **Map Partitions & Reachability:** A single map can have physically disconnected areas (partitions). A path may be blocked by being in the wrong partition. I must analyze the map XML for physical barriers and not solely rely on the 'Reachable' flag in the Game State Information.

# III. Current Objectives & Hypotheses

## A. Current Main Objective
- **Investigate the Mt. Moon fossil event:** A Rocket Grunt on Mt. Moon B2F is blocking a path and needs a fossil. This seems to be a key post-game event.

## B. Active Hypotheses & Test Plans
- **Mt. Moon Rocket Grunt:** Hypothesis: Giving a fossil Pokémon to the Rocket Grunt at (30, 12) on Mt. Moon B2F will cause him to move and unblock the path. Test Plan: Withdraw a fossil Pokémon from the PC, travel to Mt. Moon, and interact with the grunt.
- **Fossil Type:** Hypothesis: The Rocket Grunt requires a fossil *item* (e.g., HELIX FOSSIL) and not a revived fossil *Pokémon*. Test Plan: If presenting the Pokémon fails, search for a fossil item and present that instead.
- **Light Screen Duration:** Hypothesis: Light Screen lasts for 5 turns. Test Plan: In a future battle, count the turns after using Light Screen to confirm its duration.
- **Respawn Point:** Hypothesis: The game sets the last used Pokémon Center as the respawn point after a blackout. Test Plan: Heal at a new Pokémon Center, then intentionally black out to a weak wild Pokémon and observe the respawn location.

# IV. Solved Puzzles & Disproven Hypotheses
- **PC Interaction:** The PC at a Pokémon Center must be interacted with from the tile directly below it (Y+1), while facing up. **(Proven on Turn 202507)**
- **Pokémon PC Menu:** Hypothesis: "Gem's PC" leads to Pokémon Storage. **(Disproven over ~20 turns)** Test: Selected "Gem's PC". Result: Consistently led to Item Storage. Conclusion: "Gem's PC" is for items. **New Hypothesis:** "BILL's PC" leads to Pokémon Storage. **(Proven on Turn 202198)** Test: Selected "BILL's PC". Result: Successfully accessed Pokémon Storage System.
- **S.S. TICKET:** Hypothesis: The S.S. TICKET from the Silph Co. President allows access to a new ship or area at the Vermilion City port. **(Disproven on Turn 202143)** Test: Went to the S.S. Anne dock entrance at (19, 32) and interacted with the sailor. Result: The sailor gave the standard "The ship set sail" dialogue, indicating no new event was triggered.
- **Route 2 Gatehouse Path:** Hypothesis: The gatehouse at (17, 36) connects the eastern and western partitions of Route 2. **(Disproven on Turn 201910)** Test: Entered the gatehouse warp. Result: Emerged on the same side of the route after a brief loading screen, indicating it's not a partition connector. Conclusion: The gatehouse is a simple pass-through building on one side of the route.
- **Route 2 Northern Path:** Hypothesis: The path north to Pewter City from the eastern partition of Route 2 is directly accessible. **(Disproven on Turn 201874)** Test: Used `automated_path_navigator`. Result: No path found due to an impassable fence. Conclusion: The map is partitioned.
- **Menu Selection Bug:** Hypothesis: Selecting a Pokémon in the 'Bring out which POKéMON?' menu consistently opens the sub-menu for a different Pokémon. **(Disproven on Turn 197844)**
- **Route 7 Training Spot:** Hypothesis: Route 7 is a good location for training NIGHTSHADE. **(Disproven on Turn 200582)**
- **Route 4 Dead End:** Hypothesis: The western part of Route 4 is a direct path from Cerulean to Mt. Moon. **(Disproven on Turn 202331)** Test: Attempted to navigate west on Route 4 from Cerulean. Result: The path is blocked by a series of one-way ledges that can only be jumped down from east to west. Conclusion: It is impossible to travel from Cerulean City to Mt. Moon via Route 4; the path is one-way from Mt. Moon to Cerulean.

# V. Major Battle Data

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

### 3. Brock (Pewter City Gym)
- **Roster:**
    - OMASTAR (Lv 64) - Moves: HYDRO PUMP, BLIZZARD
    - ONIX (Lv 65) - Moves: EARTHQUAKE, ROCK SLIDE
    - KABUTOPS (Lv 64) - Moves: SWORDS DANCE, SLASH
    - GOLEM (Lv 64) - Moves: ROCK SLIDE
    - NINETALES (Lv 64) - Moves: REFLECT
    - AERODACTYL (Lv 65) - Moves: FLY

### 4. Cerulean Cave Wild Pokémon
- **Observed Species & Moves:**
    - WIGGLYTUFF (Lv 62) - Moves: LOVELY KISS, DOUBLE-EDGE, REST
    - SANDSLASH (Lv 63) - Moves: SWORDS DANCE, EARTHQUAKE
    - GOLEM (Lv 64) - Moves: EXPLOSION
    - NINETALES (Lv 64) - Moves:
    - AERODACTYL (Lv 65) - Moves:
    - LICKITUNG (Lv 61): Moves: WRAP
    - CHANSEY (Lv 63): Moves: DEFENSE CURL, MEGA PUNCH
    - RAICHU (Lv 64): Moves: AGILITY

# VI. Technical Documentation

## A. Automation & Tool Development Ideas
- **`room_explorer`:** A tool that takes a list of coordinates (from `map_partition_analyzer`) and generates an efficient 'snaking' path to visit every tile. This would automate the process of thoroughly searching small, isolated rooms for hidden triggers.
- **HM Automation Toolchain:** A toolchain to automate using HMs outside of battle.
- **Pathing Strategist/Chunker:** A tool to break down long paths on maps with forced movement (like Cycling Road).
- **`battle_matchup_analyzer`:** A tool that takes my party and an opponent's Pokémon species as input, analyzes type matchups, and suggests the optimal Pokémon to switch to.
- **PC Automation Suite:** A high-level agent (`pc_task_agent`) that takes a complex goal (e.g., "Withdraw HELIX, Deposit GUILLOTIN") and uses a toolchain of menu parsers and navigators to execute the multi-step process automatically.

# VII. Lessons from Tool Failures & Debugging
## A. automated_path_navigator on Mt. Moon B2F (Turn 202577)
- **Symptom:** Tool returned "No path found. Path blocked by impassable terrain." when attempting to path from (22, 18) to (30, 11).
- **Initial Hypothesis:** The tool's logic for handling `elevated_ground` and `steps` was flawed.
- **Investigation:** Manually traced the map XML. Discovered an `impassable` wall at (25, 18) that completely isolates the starting platform from the `steps` needed to reach the ground level.
- **Conclusion:** The tool was **correct**. My manual map assessment was flawed; I failed to account for a partition wall.
- **Lesson:** TRUST THE TOOL. Before debugging the tool's code, perform a rigorous manual trace of the map XML to verify that a path is *physically possible*. A "no path found" result is often an accurate reflection of a partitioned map.

## B. Agent-Generated Hypotheses (Turn 202785)
1.  **Hidden Trigger:** The dead-end room on B2F (accessed via ladder at B1F (14, 28)) contains a hidden trigger, like an invisible warp or a secret switch.
    - Test Plan: Go to the B2F dead-end room. Walk over every tile. Interact with every wall and rock.
2.  **Fossil Lead:** Having the fossil Pokémon (HELIX) in the lead party slot triggers a special event.
    - Test Plan: Put HELIX in the lead. Re-explore the isolated B1F partition and the B2F dead-end room, interacting with objects.
3.  **Item/Move Subversion:** An Escape Rope or the move Dig has a unique, non-standard function in the B2F dead-end room.
    - Test Plan: Go to the center of the B2F dead-end room. Use Escape Rope. If that fails, use Dig (if available).