# I. Core Directives & Lessons Learned

## A. Core Directives
- **D1: IMMEDIATE DATA & TOOL MANAGEMENT:** All data management (notepad, markers) and tool/agent refinement is the HIGHEST priority and MUST be performed in the same turn a need is identified. Deferring these actions is a critical failure.
- **D2: ACT ON DOCUMENTATION:** A documented lesson that does not result in a behavioral change is a critical failure.
- **D3: ABANDON FAILED HYPOTHESES:** If a strategy fails repeatedly, I must recognize the pattern, document it with attempt counts, and pivot to a new approach.
- **D4: TRUST, BUT REFINE:** I must trust the outputs of my agents and system data. If an agent or tool is suboptimal, I must prioritize refining it immediately.
- **D5: PROACTIVELY AUTOMATE:** Before performing any complex or repetitive task, I must first consider if it can be automated with a tool or agent.
- **D6: PROACTIVE AGENT USE:** I must leverage existing agents (like `puzzle_solver_agent`) for complex problems instead of defaulting to manual trial-and-error.

## B. Key Lessons Learned
- **Tool Maintenance is NOT a 'Task':** Listing tool repair as a 'to-do' item is a form of procrastination and a violation of D1. Tool refinement must be the immediate next action upon identifying a flaw.
- **Data-Driven Debugging is Mandatory:** Before writing or fixing any tool that interacts with a menu, I MUST first manually navigate the menu to observe and document its exact structure and cursor behavior. Assuming menu behavior without gathering data is a guaranteed failure.
- **Confirmation Bias Kills Progress:** I have a history of repeating failed actions (e.g., Silph Co. Elevator, `use_hm_from_party` tool). When stuck, I MUST use my `puzzle_solver_agent` to generate new, testable hypotheses.
- **Navigational Hallucinations are Real:** I have a history of incorrectly concluding I am trapped or misidentifying my location. I must use `navigation_troubleshooter` and trust system warnings to verify my position and available exits before making navigational decisions.

# II. Game & World Mechanics

## A. Map Marker System
- `🚪 Used Warp`: For any warp that has been traversed.
- `☠️ Defeated Trainer`: For any trainer that has been battled.
- `✅ Item Picked Up`: For any overworld item that has been collected.
- `🚫 Dead End`: For paths that have been confirmed to lead nowhere.
- `🗝️ Puzzle Solved/Obstacle Cleared`: For puzzles or obstacles that have been overcome.
- `🔄 Trap/Loop`: For tiles or warps that are part of a confusing loop or trap.
- `💬 Non-Battling NPC`: For NPCs that have been confirmed to not engage in battle.

## B. Tile & Movement Mechanics
- **Cuttable Trees:** Can respawn after being cut (observed on Route 12).
- **HM Usage:** Must be used from the Pokémon party menu. A fainted Pokémon cannot use an HM. To use Surf, the player must be standing on a tile directly adjacent to a water tile and be facing it.
- **Boulder Pushing:** A multi-turn action. You must be adjacent. First press turns/pushes one tile. Subsequent pushes require walking to the new adjacent tile first. Cannot push boulders while surfing.

## C. NPC Interactions & World State
- **Magikarp Salesman:** One-time interaction.

# III. Battle Knowledge

## A. Type Effectiveness & Insights
- **Wild Pokémon Speed (Cerulean Cave):** Wild Pokémon are deceptively fast.
- **SELFDESTRUCT:** Not very effective vs. Rock/Ground; Neutrally effective vs. Ground.
- **Type Immunity:** Electric moves have no effect on Ground-types.

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
- **Silph Co. Gate Mechanic:** Standing adjacent to a closed gate and pressing 'A' automatically uses the CARD KEY to open it.
- **Silph Co. Elevator:** A two-step process. First, interact with the control panel to select a floor. Second, walk onto a warp pad and press 'Down' to travel.

## B. Boulder Puzzle Mechanics
- **Objective:** Boulders are often pushed into holes to block water currents on lower floors.
- **Movement:** Pushing is a multi-turn action. Must be adjacent. First press turns/pushes. Subsequent pushes require moving to the new adjacent tile first.
- **Surfing Limitation:** Cannot push boulders while surfing (confirmed on Seafoam Islands B3F).

# VII. Agent & Tool Development
## A. Tool Notes & Limitations
- **`find_path` Tool Limitation:** The `find_path` tool is limited to single-map navigation and cannot plan routes that require using warps to connect otherwise disconnected areas on the same map. For complex, multi-map or multi-section dungeons, I must rely on manual exploration and my `navigation_troubleshooter` agent.
- **Procedural Lesson (Tool Execution Order):** A tool that reads map data (like map markers) cannot see changes made by another tool (like `define_map_marker`) in the same `tools_to_call` array. Data management and data analysis must happen in separate, sequential turns.
- **CRITICAL LESSON (use_hm_from_party):** Menu cursor starting positions are NOT static or predictable. Any tool that navigates a menu MUST first reset the cursor to a known state (e.g., by pressing 'Up' multiple times) before attempting to navigate. Assuming a static start position is a guaranteed failure.

## B. Completed Development Tasks
- **`path_trap_detector` Test (Completed):** Successfully tested on a valid ledge jump on Route 4. The tool is now considered validated and functional.

## C. Debunked Hypotheses
- **Cinnabar Gym Access:** The SECRET KEY was in the PC, not the Pokémon Mansion.

## D. Development Concepts
- **`dungeon_navigator_agent`:** An agent for complex, multi-floor dungeons.
- **`route_clearer_tool`:** A tool to calculate optimal paths to visit all un-marked trainers on a route.
- **`boulder_puzzle_solver_tool`:** A tool to solve boulder puzzles.
- **`saffron_gym_maze_solver`:** A tool to solve the Saffron Gym teleporter maze.

# VIII. High-Priority Tasks
## A. Tool Debugging
- **`use_hm_from_party` (CRITICAL):** Fundamentally broken. Requires full data-driven rewrite before next use.
- **`switch_pokemon_navigator` (CRITICAL):** Cursor-reset logic is flawed. Requires full data-driven rewrite before next use.

# IX. Core Debugging & Development Principles
- **Data-Driven Debugging (CRITICAL LESSON):** My repeated failures with menu-navigation tools (`use_hm_from_party`, `switch_pokemon_navigator`) stemmed from attempting to fix them based on assumptions rather than evidence. **Corrective Action:** Before writing or fixing any tool that interacts with a menu, I MUST first manually navigate the menu step-by-step, meticulously documenting the exact button presses and cursor behavior. This data gathering is a mandatory prerequisite to any coding and must be used to establish ground truth. Failure to do so is a guaranteed path to repeated critical failures. (Example data gathering sessions logged in previous versions of notepad).
- **Goal Setting & Procrastination:** I received a critical critique for setting tool maintenance as a secondary goal. This violates Core Directive D1 (IMMEDIATE DATA MANAGEMENT). Tool and agent refinement are not tasks to be deferred; they must be addressed in the same turn the need is identified. This is a form of procrastination that leads to repeated failures.

# X. Critical Game Mechanic Discoveries
- **Menu Input Blocking:** If the player is facing an impassable tile in the overworld, the corresponding directional input will be blocked within menus. For example, facing a wall to the north will prevent the 'Up' button from working in any menu. This can abort automated tool sequences. To avoid this, I must ensure I am not facing an obstacle before using a tool that relies on directional inputs.