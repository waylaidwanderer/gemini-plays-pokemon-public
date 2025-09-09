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
- **Confirmation Bias:** My biggest failure is assuming my code is wrong when a tool fails, instead of testing the hypothesis that my input data is wrong (e.g., trying to path through a fence on Route 2). I must verify data quality first before debugging code. I must also actively try to disprove my own assumptions.
- **Notepad Precision:** Repeated failures with `notepad_edit` `replace` operations highlight a need for greater precision. I must use the system's suggestions and be exact with `old_text`.
- **Deferred Maintenance:** I have a history of identifying broken tools (like `automated_path_navigator`) and failing to fix them immediately. This is a critical violation of my core directives and must be corrected.
- **State Tracking:** I must improve my tracking of my own actions to avoid repeating tasks I have already completed.

# II. Game Mechanics & World Data
- **Trap Battles:** Certain wild encounters appear to be 'trap' battles where the 'RUN' option is disabled (Observed: Wigglytuff, KADABRA; Suspected: Ditto).
- **Fainted HM Usage:** A fainted Pokémon can still use field moves like CUT and Surf outside of battle.
- **Cycling Road Forced Movement:** On certain routes like Route 18, the player character experiences forced, multi-tile movement in a single direction, especially when moving downhill.
- **System 'Dead End' Definition:** An area is NOT a 'dead end' if the total of reachable non-adjacent warps (or warp groups) and reachable map connections is 2 or more. This is evaluated on a whole-map basis, even if the player is in a partition with only one exit.
- **Map Partitions & Reachability:** A single map can have physically disconnected areas (partitions). A path may be blocked by being in the wrong partition. I must analyze the map XML for physical barriers and not solely rely on the 'Reachable' flag in the Game State Information.

# III. Current Objectives & Hypotheses

## A. Current Main Objective
- **Reach Cerulean City:** Traverse the eastern routes to get to Cerulean City.

## B. Active Hypotheses & Test Plans
- **Route 2 Pathing:** Hypothesis: The path to the western side of Route 2 (and thus to Pewter City) is through the southern gatehouse at (17, 36). Test Plan: Navigate to the gatehouse and pass through it.
- **Light Screen Duration:** Hypothesis: Light Screen lasts for 5 turns. Test Plan: In a future battle, count the turns after using Light Screen to confirm its duration.
- **Respawn Point:** Hypothesis: The game sets the last used Pokémon Center as the respawn point after a blackout. Test Plan: Heal at a new Pokémon Center, then intentionally black out to a weak wild Pokémon and observe the respawn location.
- **Hidden Passages:** Hypothesis: Some 'impassable' walls in Cerulean Cave are secret passages. Test Plan: Systematically walk into different types of wall tiles in the current partition to test for fake walls. Mark tested walls with a map marker.
- **Scripted High Encounter Rate:** Hypothesis: Certain corridors and tiles in Cerulean Cave have a scripted, abnormally high encounter rate, rather than it being purely random chance. Test Plan: Once the party is healed, return to the corridors on 2F where encounters were frequent and walk back and forth on a small set of tiles for a fixed duration to measure the number of encounters.

## C. Disproven Hypotheses
- **Route 2 Northern Path:** Hypothesis: The path north to Pewter City from the eastern partition of Route 2 is directly accessible. **(Disproven on Turn 201874)** Test: Used `automated_path_navigator`. Result: No path found due to an impassable fence. Conclusion: The map is partitioned.
- **Menu Selection Bug:** Hypothesis: Selecting a Pokémon in the 'Bring out which POKéMON?' menu consistently opens the sub-menu for a different Pokémon. **(Disproven on Turn 197844)**
- **Route 7 Training Spot:** Hypothesis: Route 7 is a good location for training NIGHTSHADE. **(Disproven on Turn 200582)**

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

# V. Technical Documentation

## A. Automation & Tool Development Ideas
- **`pathfinding_debugger_agent`:** An agent that takes a pathfinder error, start/end coordinates, and map XML, then suggests specific, testable hypotheses for the failure.
- **`map_partition_analyzer`:** A tool that takes map XML and a start coordinate, performs a BFS, and returns all reachable tiles. This would programmatically verify reachability before pathfinding.
- **HM Automation Toolchain:** A toolchain to automate using HMs outside of battle.
- **Pathing Strategist/Chunker:** A tool to break down long paths on maps with forced movement (like Cycling Road).

## B. Tile Traversal Mechanics
- **ground:** Standard walkable tile.
- **impassable:** Walls, fences, and objects that cannot be walked on or through.
- **grass:** Tall grass where wild Pokémon can be encountered. Walkable.
- **cuttable:** A tree that can be removed with the HM move CUT. Respawns on map change.
- **ledge:** Can only be jumped down from above (Y-1). Impassable from below and sides.
- **Warp Tile (1x1 Instant):** Most 1x1 warps trigger instantly upon stepping on them. To re-use, step off and back on.
- **Warp Tile (1x1 Non-Instant):** Some 1x1 warps require a second input into the building's impassable boundary.