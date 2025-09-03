# I. Core Directives & Lessons Learned
## A. Core Directives
- **D1: IMMEDIATE DATA MANAGEMENT:** All data management (notepad, markers, tool/agent refinement) is the HIGHEST priority and MUST be performed in the same turn a need is identified.
- **D2: ACT ON DOCUMENTATION:** A documented lesson that does not result in a behavioral change is a critical failure.
- **D3: ABANDON FAILED HYPOTHESES:** If a strategy fails repeatedly, I must recognize the pattern, document it, and pivot to a new approach.
- **D4: TRUST, BUT REFINE:** I must trust the outputs of my agents and system data. If an agent or tool is suboptimal, I must prioritize refining it.
- **D5: PROACTIVELY AUTOMATE:** Before performing any complex or repetitive task, I must first consider if it can be automated.
- **D6: PROACTIVE AGENT USE:** I must leverage existing agents for complex puzzles instead of defaulting to manual trial-and-error.
- **D7: ADHERE TO DATA STANDARDS:** My automation tools depend on consistent map markers. Failure to adhere to my own standards is a self-inflicted critical failure.

## B. Lessons Learned from Critiques & Self-Assessments
- **Confirmation Bias:** I have a tendency to repeat failed actions instead of hypothesizing and testing alternatives (e.g., Silph Co. Elevator, `use_hm_from_party` debugging). I must actively seek to disprove my own assumptions.
- **Tool & Data Management:** Inconsistent map marker usage and user error with tools (e.g., targeting impassable tiles) have directly sabotaged my automation. Adherence to my own data standards is critical.
- **Procedural Lessons:** I must act on data/tool needs in the same turn (LLM Reality). Data management and analysis must be in separate turns (Tool Execution Order).
- **Navigational Hallucinations:** I have a history of incorrectly concluding I am trapped (Silph Co. 5F, Cerulean City, Seafoam Islands B2F). I must use `navigation_troubleshooter` to verify exits before assuming a dead end.
- **Confirmation Bias in Silph Co. (Elevator Loop - Turns ~183500-183550):** I fell into a severe, multi-turn confirmation bias loop while trying to use the Silph Co. elevator. I repeatedly attempted the same failed action (pressing 'A' at (4,2)) despite numerous system warnings and a documented lesson in this very notepad warning against this exact behavior. This was a critical failure to act on documented knowledge and to abandon a failed hypothesis. **Corrective Action:** When stuck, I MUST use my new `puzzle_solver_agent` to generate new hypotheses instead of repeating failed actions.
- **Self-Assessment (Silph Co. Elevator):** I failed to proactively automate a repetitive task (`elevator_navigator`) and fell into a confirmation bias loop by repeating a failed action instead of hypothesizing and testing alternatives. This highlights a critical need to act on my core directives immediately.
- **Flawed Debugging Process (`use_hm_from_party`):** I repeatedly attempted to fix the `use_hm_from_party` tool based on untested assumptions about menu cursor behavior instead of gathering observational data first. This led to over 20 wasted turns and multiple critical failures. **Corrective Action:** Before writing or fixing any tool that interacts with a menu, I MUST first manually navigate the menu to observe and document its exact structure and cursor behavior. Data gathering must precede coding.
- **Failure of Proactive Agent Use (Badge House Hallucination):** I failed to use the `puzzle_solver_agent` to break my severe, multi-turn hallucination loop while stuck in the Badge House. I must be more proactive in using my cognitive agents for complex problem-solving, not just environmental puzzles.
- **Catastrophic Tool Debugging Failure (use_hm_from_party):** For over 50 turns, I violated my core directives by repeatedly trying to fix a broken tool with untested assumptions about static menu cursors. This was a severe confirmation bias loop. The correct process, which I failed to follow, is to immediately stop, abandon the failed hypothesis, gather empirical data via manual testing, and then redefine the tool. This failure wasted significant time and highlights the criticality of a data-driven debugging process.
- **Tunnel Vision & Dead End Hallucination (Turn 185291):** I incorrectly identified a walled-off area in Cerulean City as a 'dead end' because I was hyper-focused on a single blocked path (a cuttable tree). I completely ignored multiple other reachable warps that served as valid exits. This was a critical failure of situational awareness. **Corrective Action:** Before concluding an area is a dead end, I MUST systematically check all reachable warps and map connections. A true dead end has one or zero exits. An area with multiple exits is a pathway, even if the most obvious route is blocked.
- **Dead End Hallucination (Seafoam Islands B2F - Turn 185984):** I repeated my Cerulean City mistake. I incorrectly concluded I was in an isolated dead end on B2F because the path I took led to a dead end on B3F. I failed to check for other reachable warps on B2F before making this assumption. **Corrective Action:** I MUST systematically check ALL reachable warps and map connections using game state data before ever concluding an area is a dead end. A true dead end has one or zero exits.

# II. Game Mechanics & World Knowledge
## A. Map Marker System
- **Standardization:**
    - `🚪 Used Warp`: For any warp that has been traversed.
    - `☠️ Defeated Trainer`: For any trainer that has been battled.
    - `✅ Item Picked Up`: For any overworld item that has been collected.
    - `🚫 Dead End`: For paths that have been confirmed to lead nowhere.
    - `🗝️ Puzzle Solved/Obstacle Cleared`: For puzzles or obstacles that have been overcome.
    - `🔄 Trap/Loop`: For tiles or warps that are part of a confusing loop or trap.
    - `💬 Non-Battling NPC`: For NPCs that have been confirmed to not engage in battle.

## B. Verified NPC Interactions
- **Magikarp Salesman:** Confirmed he is a one-time interaction and will not sell another Magikarp.

## C. World Mechanics & Discoveries
- **Respawning Obstacles:** Cuttable trees can respawn after being cut. This was observed on Route 12 at coordinate (10, 100).

## D. HM Usage Mechanic
- HMs must be used from the Pokémon party menu, not the item menu.
- A fainted Pokémon cannot use an HM move from the party menu.
- To use Surf, the player must be standing on a tile directly adjacent to a water tile and be facing it.

# III. Battle Knowledge
## A. Type Effectiveness & Battle Insights
- **Wild Pokémon Speed (Cerulean Cave):** Wild Pokémon are deceptively fast and can out-speed higher-level party members.
- **SELFDESTRUCT vs. Rock/Ground:** Not very effective.
- **SELFDESTRUCT vs. Ground:** Neutrally effective but very powerful.
- **Normal OHKO vs. Normal:** Ineffective against higher-level Normal-types.
- **Opponent Move Diversity:** Do not assume an opponent will only use its most obvious STAB move.
- **Type Immunity:** Electric-type moves have no effect on Ground-type Pokémon, regardless of level difference.

## B. Known Pokemon Locations
- **Cerulean Cave:** Ditto, Wigglytuff, Electrode, Golem, Raichu, Sandslash, Parasect, Lickitung, Magneton, Dodrio, RHYDON, VICTREEBEL.

# IV. Item & Store Data
## A. Celadon Department Store (Reference)
- **5F:** Sells TMs (WATRGUN, PAYDAY, SMCTOSS, TELEPRT) and stat-boosters (HP UP, PROTEIN, etc.).
- **4F:** Sells POKé DOLL and evolution stones (FIRE, THUNDER, WATER).
- **2F:** Sells POKé BALLs, Potions, and TMs (MEGPNCH, RZRWIND, etc.).

# V. Navigation Strategy
## A. Cerulean City Navigation
- The city is divided by a river. The western section (where you arrive from Route 4) and the eastern section (where the path to Route 9 is) are separated. To cross between them, I must use Surf.

## B. Mt. Moon Navigation
- **Two Entrances:** There are two entrances to Mt. Moon from Route 4. The western entrance at (19, 6) leads to an isolated, dead-end section. The eastern entrance at (25, 6) leads to the main cave system and the path forward to Cerulean City.

# VI. Puzzles & Obstacles
## A. Solved Puzzles
- **Silph Co. Gate Mechanic:**
  - **Observation:** Closed gates can be opened.
  - **Hypothesis 1 (Failed):** Using the CARD KEY from the inventory while adjacent to the gate does not work.
  - **Hypothesis 2 (Success!):** Standing adjacent to and facing a closed gate, then pressing 'A', will automatically use the CARD KEY and open the gate.
- **Silph Co. Elevator:**
  - **Mechanic:** The elevator is a two-step process.
  - **Step 1:** Interact with the control panel at (4, 1) to bring up the floor selection menu.
  - **Step 2:** After selecting a floor, walk onto one of the warp pads at (2, 4) or (3, 4) and press 'Down' to travel.

## B. Boulder Puzzle Mechanics
- **Objective:** Boulders must often be pushed into holes to affect lower floors, typically to block strong water currents and open new paths.
- **Movement:** Pushing a boulder is a multi-turn action. You must be adjacent to it. The first press turns you to face it (if not already facing) and pushes it one tile. Subsequent pushes require you to walk to the new adjacent tile first.
- **Surfing Limitation:** It is impossible to push a boulder while surfing, even if Strength is active. This was confirmed on Seafoam Islands B3F.

# VII. Agent & Tool Development
## A. Tool Notes & Limitations
- **`find_path` Tool Limitation:** The `find_path` tool is limited to single-map navigation and cannot plan routes that require using warps to connect otherwise disconnected areas on the same map. For complex, multi-map or multi-section dungeons, I must rely on manual exploration and my `navigation_troubleshooter` agent.
- **Procedural Lesson (Tool Execution Order):** A tool that reads map data (like map markers) cannot see changes made by another tool (like `define_map_marker`) in the same `tools_to_call` array. Data management and data analysis must happen in separate, sequential turns.
- **CRITICAL LESSON (use_hm_from_party):** Menu cursor starting positions are NOT static or predictable. Any tool that navigates a menu MUST first reset the cursor to a known state (e.g., by pressing 'Up' multiple times) before attempting to navigate. Assuming a static start position is a guaranteed failure.

## B. Completed Development Tasks
- **`path_trap_detector` Test (Completed):** Per Overwatch critique, testing this tool became the highest priority. After correcting several navigational hallucinations, I successfully reached Route 4 (west of Mt. Moon) and tested the tool on a valid ledge jump from (11, 11) to (11, 13). The tool correctly identified the ledge jump and accurately determined it was not a trap. The tool is now considered validated and functional.

## C. Untested Hypotheses & Development Concepts
- **Snorlax Interaction:** I am assuming the POKé FLUTE is needed to wake the Snorlax on Route 12. This is based on external knowledge. **Hypothesis:** Interacting with Snorlax directly might trigger a different event or provide a clue. **Test:** Find the Snorlax and press 'A' on it before attempting to use any item.
- **`saffron_gym_maze_solver` (Tool Concept):** A tool to solve the Saffron Gym teleporter maze. Per Overwatch critique, this is a computational task better suited for a tool than an agent. It will take the map layout and warp connections as input to deterministically calculate the correct sequence.
- **`multi_map_dungeon_solver` (Agent Concept):** An agent to handle complex, multi-floor dungeons like Rock Tunnel or Cerulean Cave by planning routes across different map IDs.
- **`route_verifier_agent` (Agent Concept):** An agent that takes a list of NPCs and defeated trainer markers for a map, then generates a plan to systematically visit and confirm the status of each trainer, ensuring no one is missed.
- **`route_clearer_tool` (Tool Concept):** A computational tool that takes the map XML and a list of defeated trainer markers, then calculates an optimal path to visit every *un-marked* trainer on the route.
- **`dungeon_navigator` (Agent Concept):** An agent designed for complex, multi-floor dungeons. It would analyze connections between map IDs to plan routes, identify key items or puzzles blocking paths across floors, and avoid getting stuck in loops that a single-map navigator might fall into.
- **`boulder_puzzle_solver_tool` (Tool Concept):** A computational tool to solve the Seafoam Islands boulder puzzles. It would take the map XML as input, identify all boulders, switches, holes, and barriers, and then calculate the optimal sequence of pushes required to solve the puzzle for a given floor.
- **System Reachability Data as Source of Truth:** The system's global reachability data is the absolute source of truth. The system's check is optimistic and global (ignoring partitions), telling me what is *possible* on the map. My `find_path` tool provides practical, local pathfinding, telling me what is *achievable* from my current position. A discrepancy where the system shows a path but my tool does not indicates a flaw in my tool's logic that must be debugged immediately. A discrepancy where my tool shows no path but the system also shows limited reachability can indicate I am in a partitioned section of the map and need to find an alternate route.
- **Seafoam Islands Connection:** The hole on B2F at (20, 7) leads to B3F at (19, 8).

# VIII. High-Priority Tasks
## A. Tool Debugging
- **`use_hm_from_party` (CRITICAL):** This tool is fundamentally broken and caused a >20 turn loop. It fails to navigate the sub-menu correctly, selecting 'SWITCH' instead of the specified move. **Task:** Perform a full, data-driven debugging session. Manually navigate the menu step-by-step, documenting the exact button presses required for each slot and move index. Use this data to completely rewrite and validate the tool's logic. Do not attempt to use it again until this is complete.

# IX. Live Debugging Sessions
## A. `use_hm_from_party` Data Gathering (Turn 186248)
- **Objective:** Document the exact, manual button sequence to use Surf from the overworld.
- **Procedure:**
  1. Start from overworld.
  2. Press Start.
  3. Navigate to POKéMON.
  4. Press A.
  5. Navigate to TITANESS (Slot 4).
  6. Press A.
  7. Navigate to SURF (Move 1).
  8. Press A.
  9. Press A to confirm.
- **Execution Log:**