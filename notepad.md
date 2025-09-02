# I. Core Directives & Lessons Learned
## A. Core Directives
- **DIRECTIVE 1: IMMEDIATE DATA MANAGEMENT.** All data management (notepad updates, map markers, tool/agent refinement) is the HIGHEST priority and MUST be performed in the same turn a need is identified.
- **DIRECTIVE 2: ACT ON DOCUMENTATION.** A documented lesson that does not result in a behavioral change is a critical failure of the learning loop.
- **DIRECTIVE 3: ABANDON FAILED HYPOTHESES.** If a strategy fails repeatedly, I must recognize the pattern, document it, and pivot to a new approach.
- **DIRECTIVE 4: TRUST, BUT REFINE, AGENTS & TOOLS.** I must trust the outputs of my agents and system data over my own intuition. If an agent or tool is suboptimal, I must prioritize refining it.
- **DIRECTIVE 5: PROACTIVELY AUTOMATE.** Before performing any complex or repetitive task, I must first consider if it can be automated with a new agent or tool.
- **DIRECTIVE 6: PROACTIVE AGENT USE.** I must leverage existing agents when encountering navigational or environmental puzzles, instead of defaulting to manual trial-and-error.
- **DIRECTIVE 7: ADHERE TO DATA STANDARDS.** My automation tools depend on consistent, standardized map markers. Failure to adhere to my own documented standards is a self-inflicted critical failure that wastes time and sabotages my own efforts.

## B. Lessons Learned from Critiques & Self-Assessments
- **Confirmation Bias & Flawed Tools (`find_path` Failures):** Multiple critiques and self-assessments have identified the `find_path` tool's lack of diagnostic feedback as a critical flaw. This repeatedly led to incorrect conclusions about being trapped (e.g., Cerulean Cave, Cerulean City), causing severe confirmation bias and a failure to consider correct solutions like using Surf. This highlights a core failure in prioritizing immediate tool maintenance and abandoning flawed hypotheses.
- **Tool & Data Management Failures:**
  - **`find_path` User Error:** I repeatedly target impassable tiles instead of adjacent, traversable ones. This is a user error, not a tool flaw.
  - **Map Marker Standardization:** My failure to adhere to my own documented marker standards has directly caused my automation tools to fail. Consistent data management is a prerequisite for effective gameplay.
- **Overwatch Critique (Turn 180201):** Failure to act on documented information and underdeveloped use of map markers.
- **Self-Assessment (Turn 180373):** Correctly identified an automation opportunity (`item_restock_agent`) and acted immediately.
- **Confirmation Bias in Tool Debugging (Turns ~177769-177818):** `fly_menu_navigator` failures highlighted the need to actively disprove my own assumptions during debugging.
- **Procedural Lesson (Notepad Usage):** Large `overwrite` actions on the notepad are prone to failure. I must break down major updates into smaller, targeted `replace` actions to ensure immediate and successful documentation.
- **Procedural Lesson (LLM Reality):** As an LLM, I cannot defer tasks. Any identified need for data management or tool refinement MUST be acted upon in the same turn. Creating a mental 'to-do list' is a critical failure of my core nature.
- **Procedural Lesson (Tool Execution):** Tools within the same `tools_to_call` array operate on the game state from the *beginning* of the turn. Data created by one tool (e.g., a map marker) will not be visible to another tool in the same turn's execution.
- **Confirmation Bias in Silph Co. (Turn ~182950):** I incorrectly concluded I was trapped on 5F due to a closed gate, ignoring multiple reachable warps. This was a critical failure of observation. **Corrective Action:** Before ever concluding I am trapped, I MUST use the `navigation_troubleshooter` agent to get an objective analysis of all possible exits.
- **Confirmation Bias in Silph Co. (Elevator Loop - Turns ~183500-183550):** I fell into a severe, multi-turn confirmation bias loop while trying to use the Silph Co. elevator. I repeatedly attempted the same failed action (pressing 'A' at (4,2)) despite numerous system warnings and a documented lesson in this very notepad warning against this exact behavior. This was a critical failure to act on documented knowledge and to abandon a failed hypothesis. **Corrective Action:** When stuck, I MUST use my new `puzzle_solver_agent` to generate new hypotheses instead of repeating failed actions.
- **Lessons from Self-Assessment (Turn 183144):**
  - **Deferred Automation:** I failed to create the `elevator_navigator` tool at the first sign of trouble, violating my directive to proactively automate. This cost me significant time and frustration. I must be more vigilant in identifying these opportunities and acting on them immediately.
  - **Confirmation Bias (Elevator Puzzle):** I incorrectly assumed the elevator panel was a single-step interaction and repeatedly failed by trying the same action. I failed to hypothesize and test an alternative (the two-step select-then-walk mechanic), which is a critical lapse in my problem-solving process. I must actively try to disprove my own assumptions.

# II. Game Mechanics & World Knowledge
## A. Verified Tile Traversal Rules
- **ground:** Standard walkable tile.
- **grass:** Tall grass where wild Pokémon appear. Walkable.
- **impassable:** Cannot be entered. Includes walls, rocks, etc.
- **water:** Traversable only with Surf.
- **cuttable:** A tree that can be cut using the Cut HM. Impassable without Cut.
- **ledge:** A one-way drop. Can be jumped down but not climbed up.
- **ladder_down / ladder_up:** Acts as a warp to another floor.
- **elevated_ground:** Walkable ground at a different elevation. Cannot be accessed from `ground` directly.
- **steps:** The only tile type that allows movement between `ground` and `elevated_ground`.
- **teleport:** An instant warp tile within the same logical location.
- **gate_offscreen:** A gate whose state is unknown. Treated as potentially open for pathfinding.
- **closed_gate:** An impassable gate that is currently visible on the screen. It may require a switch or key to open. For pathfinding purposes, any `closed_gate` that is *off-screen* is treated as potentially open to encourage exploration of alternate routes.
- **open_gate:** A previously closed gate that is now open and acts as `ground`. It is currently visible on the screen.

## B. Map Marker System
- **Standardization:**
    - `🚪 Used Warp`: For any warp that has been traversed.
    - `☠️ Defeated Trainer`: For any trainer that has been battled.
    - `✅ Item Picked Up`: For any overworld item that has been collected.
    - `🚫 Dead End`: For paths that have been confirmed to lead nowhere.
    - `🗝️ Puzzle Solved/Obstacle Cleared`: For puzzles or obstacles that have been overcome.
    - `🔄 Trap/Loop`: For tiles or warps that are part of a confusing loop or trap.
    - `💬 Non-Battling NPC`: For NPCs that have been confirmed to not engage in battle.

## C. Verified NPC Interactions
- **Magikarp Salesman:** Confirmed he is a one-time interaction and will not sell another Magikarp.

# III. Battle Knowledge
## A. Type Effectiveness & Battle Insights
- **Wild Pokémon Speed (Cerulean Cave):** Wild Pokémon are deceptively fast and can out-speed higher-level party members.
- **SELFDESTRUCT vs. Rock/Ground:** Not very effective.
- **SELFDESTRUCT vs. Ground:** Neutrally effective but very powerful.
- **Normal OHKO vs. Normal:** Ineffective against higher-level Normal-types.
- **Opponent Move Diversity:** Do not assume an opponent will only use its most obvious STAB move.

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

# VII. Agent & Tool Development
## A. Tool Notes & Limitations
- **`find_path` Tool Limitation:** The `find_path` tool is limited to single-map navigation and cannot plan routes that require using warps to connect otherwise disconnected areas on the same map. For complex, multi-map or multi-section dungeons, I must rely on manual exploration and my `navigation_troubleshooter` agent.
- **Procedural Lesson (Tool Execution Order):** A tool that reads map data (like map markers) cannot see changes made by another tool (like `define_map_marker`) in the same `tools_to_call` array. Data management and data analysis must happen in separate, sequential turns.

## B. Completed Development Tasks
- **`path_trap_detector` Test (Completed):** Per Overwatch critique, testing this tool became the highest priority. After correcting several navigational hallucinations, I successfully reached Route 4 (west of Mt. Moon) and tested the tool on a valid ledge jump from (11, 11) to (11, 13). The tool correctly identified the ledge jump and accurately determined it was not a trap. The tool is now considered validated and functional.

## C. Agent & Tool Concepts
- **`saffron_gym_maze_solver` (Tool Concept):** A tool to solve the Saffron Gym teleporter maze. Per Overwatch critique, this is a computational task better suited for a tool than an agent. It will take the map layout and warp connections as input to deterministically calculate the correct sequence.

## D. Mt. Moon Navigation
- **Two Entrances:** There are two entrances to Mt. Moon from Route 4. The western entrance at (19, 6) leads to an isolated, dead-end section. The eastern entrance at (25, 6) leads to the main cave system and the path forward to Cerulean City.

# VIII. Procedural Rules & Best Practices
- **Pathfinding First:** Before assuming an HM or key item is needed to overcome a navigational obstacle, I MUST first use the `find_path` tool to confirm that the destination is truly unreachable.
- **Proactive Maze Agents:** For complex mazes (e.g., teleporter puzzles, spinner mazes), I MUST prioritize creating a dedicated solver agent *before* attempting a manual solution. Manual attempts should only be for initial data gathering.
- **`nickname_automator` (Tool Concept):** A tool that takes a string as input and outputs the sequence of button presses required to enter it on the Pokémon nicknaming screen. This would automate a tedious, repetitive task.
- **`nickname_automator` (Tool Concept):** A tool that takes a string as input and outputs the sequence of button presses required to enter it on the Pokémon nicknaming screen. This would automate a tedious, repetitive task.