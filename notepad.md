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
- **Confirmation Bias Kills Progress:** I have a history of repeating failed actions (e.g., `use_hm_from_party` tool). When stuck, I MUST use my `puzzle_solver_agent` to generate new, testable hypotheses.
- **Navigational Hallucinations are Real:** I have a history of incorrectly concluding I am trapped or misidentifying map states (dead ends, unseen tiles). I must develop a tool for reliable map analysis and trust system warnings.

# II. Game & World Mechanics

## A. Map Marker System
- `🚪 Used Warp`: For any warp that has been traversed.
- `☠️ Defeated Trainer`: For any trainer that has been battled.
- `✅ Item Picked Up`: For any overworld item that has been collected.
- `🚫 Dead End`: For paths that have been confirmed to lead nowhere.
- `🗝️ Puzzle Solved/Obstacle Cleared`: For puzzles or obstacles that have been overcome.
- `💬 Non-Battling NPC`: For NPCs that have been confirmed to not engage in battle.

## B. Tile & Movement Mechanics
- **Menu Input Blocking (CRITICAL):** If the player is facing an impassable tile in the overworld, the corresponding directional input will be blocked within menus. This can abort automated tool sequences. To avoid this, I must ensure I am not facing an obstacle before using a tool that relies on directional inputs.
- **Cuttable Trees:** Can respawn after being cut.
- **Ledges:** One-way traversal only. Can be jumped down, but not climbed up. A jump down from Y to Y+1 lands the player at Y+2.
- **HM Usage:** Must be used from the Pokémon party menu. A fainted Pokémon cannot use an HM. To use an HM on an object, the player must be standing on an adjacent tile and *facing* the object *before* opening the menu.
- **Item Menu Anomaly:** Selecting 'ITEM' from the main menu can sometimes lead to an HM-only list, not the full inventory. The trigger for this is currently unknown. To use an HM on an object, the player must be standing on an adjacent tile and *facing* the object *before* opening the menu.
- **Boulder Pushing:** A multi-turn action. Must be adjacent. First press turns/pushes one tile. Subsequent pushes require walking to the new adjacent tile first. Cannot push boulders while surfing.
- **Dead End Definition:** An area is considered a dead end if it has only one group of reachable exits (warps/map connections) and no reachable unseen tiles.

# III. Battle & Item Knowledge

## A. Type Effectiveness & Insights
- **Wild Pokémon Speed (Cerulean Cave):** Wild Pokémon are deceptively fast.
- **SELFDESTRUCT:** Not very effective vs. Rock/Ground; Neutrally effective vs. Ground.
- **Type Immunity:** Electric moves have no effect on Ground-types.

## B. Known Pokemon Locations
- **Cerulean Cave:** Ditto, Wigglytuff, Electrode, Golem, Raichu, Sandslash, Parasect, Lickitung, Magneton, Dodrio, RHYDON, VICTREEBEL.

## C. Item & Store Data
### Item Locations & Vendors
- **Route 12 Super Rod House:** Fishing Guru gives the SUPER ROD.

### Celadon Department Store (Reference)
- **5F:** Sells TMs (WATRGUN, PAYDAY, SMCTOSS, TELEPRT) and stat-boosters (HP UP, PROTEIN, etc.).
- **4F:** Sells POKé DOLL and evolution stones (FIRE, THUNDER, WATER).
- **2F:** Sells POKé BALLs, Potions, and TMs (MEGPNCH, RZRWIND, etc.).

# IV. Navigation Strategy
## A. Cerulean City Navigation
- The city is divided by a river. The western section (where you arrive from Route 4) and the eastern section (where the path to Route 9 is) are separated. To cross between them, I must use Surf.

## B. Mt. Moon Navigation
- **Two Entrances:** There are two entrances to Mt. Moon from Route 4. The western entrance at (19, 6) leads to an isolated, dead-end section. The eastern entrance at (25, 6) leads to the main cave system and the path forward to Cerulean City.

# V. Puzzles & Obstacles

## A. Solved Puzzles
- **Silph Co. Gate Mechanic:** Standing adjacent to a closed gate and pressing 'A' automatically uses the CARD KEY to open it.
- **Silph Co. Elevator:** A two-step process. First, interact with the control panel to select a floor. Second, walk onto a warp pad and press 'Down' to travel.

## B. Boulder Puzzle Mechanics
- **Objective:** Boulders are often pushed into holes to block water currents on lower floors.
- **Movement:** Pushing is a multi-turn action. Must be adjacent. First press turns/pushes. Subsequent pushes require moving to the new adjacent tile first.
- **Surfing Limitation:** Cannot push boulders while surfing (confirmed on Seafoam Islands B3F).

# VI. Agent & Tool Development

## A. Development Principles
- **Data-Driven Debugging (CRITICAL):** My repeated failures with menu-navigation tools (`use_hm_from_party`) stemmed from fixing them based on assumptions rather than evidence. **Corrective Action:** Before writing or fixing any tool that interacts with a menu, I MUST first manually navigate it step-by-step, meticulously documenting the exact button presses and cursor behavior. This data gathering is a mandatory prerequisite to any coding.
- **Tool Execution Order:** A tool that reads map data cannot see changes made by another tool in the same turn. Data management and data analysis must happen in separate, sequential turns.
- **`find_path` Limitation:** This tool is limited to single-map navigation and cannot plan routes across disconnected map sections. For complex dungeons, I must rely on manual exploration and my `navigation_troubleshooter` agent.

## B. Future Development Ideas
- **`find_path` Tool Improvement:** Refine the tool to provide contextual failure reports, such as identifying the specific obstacle (e.g., 'cuttable_tree') that is blocking a path.
- **'Stuck Loop Detector' Agent:** Could analyze move history and game state to identify and diagnose repetitive failures, suggesting alternative hypotheses.
- **'Map Analyzer' Tool/Agent:** A reliable tool to calculate reachable unseen tiles and determine if an area is a dead end to prevent navigational hallucinations.
- **'High-Level Planner' Agent:** Could analyze the primary goal and suggest a sequence of maps or major objectives to achieve it.
- **'Team Composition' Agent:** Could analyze the party and PC to suggest optimal teams for specific challenges (e.g., a specific Gym Leader rematch).
- **'Inventory/PC Summary' Tool:** Could provide a quick summary of current items without manual checking.

# VII. Data-Driven Debugging Logs
## A. `use_hm_from_party` Manual Test (Cut)
- **Attempt 1 (Failure):** Selected 'CUT'. Game returned error "There isn't anything to CUT!". **Conclusion:** Player must be facing the target object *before* opening the menu to use an HM.
- **Attempt 2 (Success):** Faced tree, then navigated menu. **Discovery:** Party screen cursor position is not reliably at the top. A cursor-resetting sequence (e.g., spamming 'Up') is necessary for a robust tool.

## C. Snorlax Puzzle (Route 12)
- **Hypothesis 1 (Failed):** Use POKé FLUTE from 'ITEM' menu. Result: Led to an HM-only screen.
- **Hypothesis 2 (Failed - Agent Suggestion):** Switch inventory 'pockets' with Left/Right. Result: No effect. The inventory does not appear to have pockets.
- **Hypothesis 3 (Failed):** Interact directly with Snorlax using 'A'. Result: No effect.