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
- **Confirmation Bias & Data Integrity:** I have a history of repeating failed actions instead of hypothesizing alternatives (e.g., Silph Co. Elevator, `use_hm_from_party` debugging). This is often compounded by inconsistent data management (map markers, tool inputs). **Corrective Action:** I must actively seek to disprove my own assumptions, use agents like `puzzle_solver_agent` when stuck, and adhere strictly to my own data standards.
- **Procedural Lessons:** I must act on data/tool needs in the same turn (LLM Reality). Data management and analysis must be in separate turns (Tool Execution Order).
- **Navigational Hallucinations:** I have a history of incorrectly concluding I am trapped (Silph Co. 5F, Cerulean City, Seafoam Islands B2F). I must use `navigation_troubleshooter` to verify exits before assuming a dead end.
- **Procrastination on Maintenance (CRITICAL LESSON):** I have a history of deferring critical tool/agent maintenance by setting it as a 'goal' or adding it to a 'to-do list'. This is a direct violation of D1 (IMMEDIATE DATA MANAGEMENT) and a misunderstanding of my nature as an LLM. Maintenance is not a goal; it is an immediate, high-priority action that must never be deferred.
- **Confirmation Bias (Silph Co. Elevator):** I fell into a severe loop attempting the same failed action. This was a critical failure to act on documented knowledge and abandon a failed hypothesis. **Corrective Action:** When stuck, I MUST use my `puzzle_solver_agent` to generate new hypotheses.
- **Self-Assessment (Silph Co. Elevator):** I failed to proactively automate a repetitive task (`elevator_navigator`) and fell into a confirmation bias loop by repeating a failed action instead of hypothesizing and testing alternatives. This highlights a critical need to act on my core directives immediately.
- **Flawed Debugging Process:** I have a history of attempting to fix tools based on untested assumptions (e.g., `use_hm_from_party` menu navigation). **Corrective Action:** Before writing or fixing any tool that interacts with a menu, I MUST first manually navigate the menu to observe and document its exact structure and cursor behavior. Data gathering must precede coding.
- **Failure of Proactive Agent Use (Badge House Hallucination):** I failed to use the `puzzle_solver_agent` to break my severe, multi-turn hallucination loop while stuck in the Badge House. I must be more proactive in using my cognitive agents for complex problem-solving, not just environmental puzzles.
- **Catastrophic Tool Debugging Failure (`use_hm_from_party`):** A >50 turn loop occurred from violating core directives by repeatedly trying to fix a broken tool with untested assumptions. The correct process is to stop, abandon the failed hypothesis, gather data manually, then redefine the tool.
- **Navigational Hallucinations:** I have a history of incorrectly concluding I am trapped (Silph Co. 5F, Cerulean City, Seafoam Islands B2F). I must use `navigation_troubleshooter` to verify exits before assuming a dead end.
- **Procrastination on Maintenance (CRITICAL LESSON):** I have a history of deferring critical tool/agent maintenance by setting it as a 'goal' or adding it to a 'to-do list'. This is a direct violation of D1 (IMMEDIATE DATA MANAGEMENT) and a misunderstanding of my nature as an LLM. Maintenance is not a goal; it is an immediate, high-priority action that must never be deferred.

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
## D. Debunked Hypotheses
- **Cinnabar Gym Access:** I assumed the SECRET KEY was in the Pokémon Mansion. This was false. I failed to check my PC, where the key was already stored.

## D. Development Concepts
- **`dungeon_navigator_agent` (Consolidated Concept):** An agent to handle complex, multi-floor dungeons by analyzing connections between map IDs to plan routes and identify cross-floor puzzles.
- **`route_clearer_tool` (Consolidated Concept):** A computational tool that takes map XML and defeated trainer markers to calculate an optimal path to visit every *un-marked* trainer on a route.
- **`boulder_puzzle_solver_tool` (Tool Concept):** A computational tool to solve boulder puzzles by taking map XML and calculating the optimal sequence of pushes.
- **`saffron_gym_maze_solver` (Tool Concept):** A tool to solve the Saffron Gym teleporter maze by taking the map layout and warp connections as input to deterministically calculate the correct sequence.
- **Seafoam Islands Connection:** The hole on B2F at (20, 7) leads to B3F at (19, 8).

# VIII. High-Priority Tasks
## A. Tool Debugging
- **`use_hm_from_party` (CRITICAL):** This tool is fundamentally broken and caused a >20 turn loop. It fails to navigate the sub-menu correctly, selecting 'SWITCH' instead of the specified move. **Task:** Perform a full, data-driven debugging session. Manually navigate the menu step-by-step, documenting the exact button presses required for each slot and move index. Use this data to completely rewrite and validate the tool's logic. Do not attempt to use it again until this is complete.
- **`switch_pokemon_navigator` (CRITICAL):** This tool has failed twice in a row, selecting the wrong Pokémon (slot 5, then slot 3) when slot 4 was the target. The cursor-resetting logic is fundamentally flawed and cannot be trusted. **Task:** Perform a full, data-driven debugging session as soon as possible. Do not use this tool again until it is completely rewritten and validated.

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

## B. `use_hm_from_party` Manual Execution Log (Pallet Town)
- **Turn 186398:** Faced water at (5, 14).
- **Turn 186399:** Pressed Start.
- **Turn 186400:** Pressed A (cursor was on POKEMON).

# X. New Tool & Agent Concepts
- **`route_20_maze_solver` (Tool Concept):** A computational tool that will analyze the `map_xml_string` for Route 20 to find a traversable path through the water and around the impassable rock formations, guiding navigation from the eastern entrance to the western exit that leads to Cinnabar Island.

## A. `route_20_maze_solver` Refinement Note
- The tool correctly identified that Route 20 is partitioned by failing to find a path. This is a good outcome, but the tool should be refined to explicitly report "Path failed due to map partition" instead of a generic "No path found." This will provide better diagnostic information for future complex navigation.

# X. Live Debugging Sessions
## A. `use_hm_from_party` Data Gathering 2 (Turn 186663)
- **Objective:** Document the exact, manual button sequence to use Surf from the overworld.
- **Procedure:**
  - **Turn 186662:** Pressed Start. Menu opens, cursor on 'ITEM'.

# XII. Core Debugging & Development Principles
- **Data-Driven Debugging (CRITICAL LESSON):** My repeated failures with menu-navigation tools (`use_hm_from_party`, `switch_pokemon_navigator`) stemmed from attempting to fix them based on assumptions rather than evidence. **Corrective Action:** Before writing or fixing any tool that interacts with a menu, I MUST first manually navigate the menu step-by-step, meticulously documenting the exact button presses and cursor behavior. This data gathering is a mandatory prerequisite to any coding and must be used to establish ground truth. Failure to do so is a guaranteed path to repeated critical failures.
- **Goal Setting & Procrastination:** I received a critical critique for setting tool maintenance as a secondary goal. This violates Core Directive D1 (IMMEDIATE DATA MANAGEMENT). Tool and agent refinement are not tasks to be deferred; they must be addressed in the same turn the need is identified. This is a form of procrastination that leads to repeated failures.