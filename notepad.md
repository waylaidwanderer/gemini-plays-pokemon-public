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
- **Confirmation Bias Kills Progress:** I have a history of repeating failed actions (e.g., trying the broken `use_hm_from_party` tool 3 times before debugging) or blaming tools for my own errors. I must trust my tools' outputs (like a calculated path) and meticulously verify my own actions before concluding a tool is faulty. When stuck, I MUST use my `puzzle_solver_agent` to generate new, testable hypotheses.
- **Navigational Hallucinations are Real:** I have a history of incorrectly concluding I am trapped or misidentifying map states (dead ends, unseen tiles). I must develop a tool for reliable map analysis and trust system warnings.

# II. Game & World Mechanics

## A. Map Marker System
- `🚪 Used Warp`: For any warp that has been traversed.
- `☠️ Defeated Trainer`: For any trainer that has been battled.
- `✅ Item Picked Up`: For any overworld item that has been collected.
- `🚫 Dead End`: For paths that have been confirmed to lead nowhere.
- `🗝️ Puzzle Solved/Obstacle Cleared`: For puzzles or obstacles that have been overcome.
- `💬 Non-Battling NPC`: For NPCs that have been confirmed to not engage in battle.
- `💖 Healing Zone`: For tiles that provide party healing.

## B. Tile & Movement Mechanics
- **Traversable Tiles:**
  - `ground`, `grass`: Standard walkable ground.
  - `elevated_ground`: Walkable, but only accessible via `steps`.
  - `steps`: Allows movement between `ground` and `elevated_ground`.
  - `water`: Requires Surf HM to cross.
  - `warp`, `ladder_up`, `ladder_down`, `hole`, `teleport`: Tiles that trigger a map transition.
- **Conditional/One-Way Tiles:**
  - `ledge`: Can only be jumped down. A jump from (X, Y) lands at (X, Y+2).
  - `cuttable`: An obstacle that can be temporarily cleared with Cut HM.
  - `boulder_switch`: A tile that a boulder can be pushed onto.
- **Impassable Tiles:**
  - `impassable`: Standard walls, objects, trees, etc.
  - `boulder_barrier`: A wall that is removed when a corresponding `boulder_switch` is activated.
- **Special Mechanics:**
  - **Healing Zone:** A tile described as a "purified, protected zone" that fully heals all Pokémon in the party's HP and restores all their PP.
  - **Menu Input Blocking (CRITICAL):** Facing an impassable tile blocks that directional input in menus.
  - **HM Usage:** Must be adjacent to and facing the target object before opening the party menu.
  - **Boulder Pushing:** A multi-turn action. Cannot be done while surfing.
  - **Dead End Definition:** A map is only a dead end if it has only one exit warp/connection and no reachable unseen tiles. The nature of the destination map is irrelevant to this classification.

## C. Type Effectiveness & Insights
- **Wild Pokémon Speed (Cerulean Cave):** Wild Pokémon are deceptively fast.
- **SELFDESTRUCT:** Not very effective vs. Rock/Ground; Neutrally effective vs. Ground.
- **Type Immunity:** Electric moves have no effect on Ground-types.

## D. Known Pokemon Locations
- **Cerulean Cave:** Ditto, Wigglytuff, Electrode, Golem, Raichu, Sandslash, Parasect, Lickitung, Magneton, Dodrio, RHYDON, VICTREEBEL.
- **Pokémon Tower:** GASTLY, CUBONE.

# III. Active Puzzles & Navigation Strategy

## A. Pokémon Tower 7F (Dead End Puzzle)
- **Observation:** Reached the top floor (7F) of the Pokémon Tower. The path is a confirmed dead end with no visible exits or interactable objects.
- **Hypothesis 1 (Failed - 15+ attempts):** Interacting with Pikachu or the environment would trigger a cutscene. **Test:** Pressed 'A', 'B', 'Start', and directional buttons repeatedly at (12, 3). **Result:** No event triggered. **Conclusion:** This was a severe case of Confirmation Bias. Standard interaction is not the solution.
- **Hypothesis 2 (Failed - Agent Suggestion):** Use the POKé FLUTE at the northernmost point (12, 3) to trigger a spectral event. **Test:** Navigated to (12, 3) and used POKé FLUTE from the item menu. **Result:** The game displayed text confirming the flute was played ("Now, that's a catchy tune!"), but no event occurred. **Conclusion:** The POKé FLUTE has no special effect on this floor. The area remains a dead end.

## B. Cerulean City Navigation
- The city is divided by a river. The western section (where you arrive from Route 4) and the eastern section (where the path to Route 9 is) are separated. To cross between them, I must use Surf.

## C. Mt. Moon Navigation
- **Two Entrances:** There are two entrances to Mt. Moon from Route 4. The western entrance at (19, 6) leads to an isolated, dead-end section. The eastern entrance at (25, 6) leads to the main cave system and the path forward to Cerulean City.

# IV. Solved Puzzles & Mechanics Reference

## A. Silph Co. Puzzles
- **Gate Mechanic:** Standing adjacent to a closed gate and pressing 'A' automatically uses the CARD KEY to open it.
- **Elevator:** A two-step process. First, interact with the control panel to select a floor. Second, walk onto a warp pad and press 'Down' to travel.

## B. Snorlax Puzzle (Route 12)
- The item menu is a single, scrollable list. After selecting 'ITEM' from the main menu, scroll down past the HMs (indicated by a '↓' arrow) to find Key Items like the POKé FLUTE. Using it from this menu wakes the Snorlax.

## C. Boulder Puzzle Mechanics
- **Objective:** Boulders are often pushed into holes to block water currents on lower floors.
- **Movement:** Pushing is a multi-turn action. Must be adjacent. First press turns/pushes. Subsequent pushes require moving to the new adjacent tile first.
- **Surfing Limitation:** Cannot push boulders while surfing (confirmed on Seafoam Islands B3F).

## D. Item & Store Data
### Item Locations & Vendors
- **Route 12 Super Rod House:** Fishing Guru gives the SUPER ROD.

### Celadon Department Store (Reference)
- **5F:** Sells TMs (WATRGUN, PAYDAY, SMCTOSS, TELEPRT) and stat-boosters (HP UP, PROTEIN, etc.).
- **4F:** Sells POKé DOLL and evolution stones (FIRE, THUNDER, WATER).
- **2F:** Sells POKé BALLs, Potions, and TMs (MEGPNCH, RZRWIND, etc.).

# V. Agent & Tool Development

## A. Development Principles
- **Data-Driven Debugging (CRITICAL):** My repeated failures with menu-navigation tools (`use_hm_from_party`, `switch_pokemon_navigator`) stemmed from fixing them based on assumptions rather than evidence. **Corrective Action:** Before writing or fixing any tool that interacts with a menu, I MUST first manually navigate it step-by-step, meticulously documenting the exact button presses and cursor behavior. This data gathering is a mandatory prerequisite to any coding.
- **`find_path` Reliability:** This tool has been significantly improved with diagnostic reporting. Future issues should be addressed by analyzing its detailed failure reports to distinguish between tool bugs and in-game puzzles.

## B. Future Development Ideas
- **'Execute Battle Action' Tool:** A tool that takes an action type (MOVE/SWITCH) and target (move index/slot number) and outputs the button presses to automate battle menu navigation.
- **'Stuck Loop Detector' Agent:** Could analyze move history and game state to identify and diagnose repetitive failures, suggesting alternative hypotheses.
- **'Map Analyzer' Tool/Agent:** A reliable tool to calculate reachable unseen tiles and determine if an area is a dead end to prevent navigational hallucinations.
- **'High-Level Planner' Agent:** Could analyze the primary goal and suggest a sequence of maps or major objectives to achieve it.
- **'Team Composition' Agent:** Could analyze the party and PC to suggest optimal teams for specific challenges (e.g., a specific Gym Leader rematch).
- **'Inventory/PC Summary' Tool:** Could provide a quick summary of current items without manual checking.
- **'Wild Battle Automator V2' Agent:** An advanced version of the current tool that can handle non-trivial battles. It would analyze type matchups, select the best move from the full moveset (not just the first), and even recommend switching Pokémon if the current matchup is unfavorable.
  - **Improvement Idea (per Overwatch):** Instead of a small, hardcoded type dictionary, create a more robust solution, such as a dedicated 'type-checker' tool or a process to systematically expand the internal dictionary to prevent future failures.
- **'PC Summary' Tool:** A tool to quickly parse and display a summary of Pokémon stored in the PC, including species, level, and moves. This would save time compared to manually checking the PC.
- **'Grinding Spot Recommender' Agent:** An agent that analyzes my notepad's 'Known Pokemon Locations' section and my current party to suggest optimal grinding locations based on type advantages and EXP yield.
- **'Menu Analyzer' Tool:** A tool that can parse screen text from menus to determine cursor position, available options, and list structure. This would be invaluable for debugging and creating robust menu navigation tools.
- **'Pattern Recognition' Agent:** An agent that could analyze map sprite lists and existing map markers to identify patterns (e.g., 'all NPCs in this area are non-battlers') and form high-level hypotheses to guide exploration.

## C. Data-Driven Debugging Logs
- **`use_hm_from_party` Manual Test (Cut):**
  - **Attempt 1 (Failure):** Selected 'CUT'. Game returned error "There isn't anything to CUT!". **Conclusion:** Player must be facing the target object *before* opening the menu to use an HM.
  - **Attempt 2 (Success):** Faced tree, then navigated menu. **Discovery:** Party screen cursor position is not reliably at the top. A cursor-resetting sequence (e.g., spamming 'Up') is necessary for a robust tool.
- **Snorlax Puzzle (Route 12):**
  - **Hypothesis 1 (Failed):** Use POKé FLUTE from 'ITEM' menu. Result: Led to an HM-only screen.
  - **Hypothesis 2 (Failed - Agent Suggestion):** Switch inventory 'pockets' with Left/Right. Result: No effect. The inventory does not appear to have pockets.
  - **Hypothesis 3 (Failed):** Interact directly with Snorlax using 'A'. Result: No effect.
  - **Hypothesis 4 (Success):** The item menu is a single, scrollable list. After selecting 'ITEM' from the main menu, scroll down past the HMs (indicated by a '↓' arrow) to find Key Items like the POKé FLUTE. Using it from this menu wakes the Snorlax.
- **`use_hm_from_party` Manual Test (Fly - Pallet Town):**
  - **Step 1 (Open Menu):** Pressed 'Start'. Cursor defaults to 'POKéMON'. Result: Success.
  - **Step 2 (Enter Party):** Pressed 'A'. Cursor defaults to slot 2 (CRAG). Result: Success.
  - **Step 3 (Open Sub-Menu):** Pressed 'A'. Cursor defaults to the first move ('FLY'). Result: Success.
- **'Menu Analyzer' Tool:** A tool that can parse screen text from menus to determine cursor position, available options, and list structure. This would be invaluable for debugging and creating robust menu navigation tools.