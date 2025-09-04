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
- **Confirmation Bias Kills Progress:** I have a history of repeating failed actions or blaming tools for my own errors. I must trust my tools' outputs and meticulously verify my own actions before concluding a tool is faulty. When stuck, I MUST use my `puzzle_solver_agent` to generate new, testable hypotheses.
- **Escape is Not Guaranteed (CRITICAL LESSON):** I incorrectly assumed fleeing from wild battles was always possible. The DODRIO in Cerulean Cave proved this wrong by preventing escape, leading to a party wipe. I must not rely on running as a guaranteed safe option, especially when at low health.

# II. Game & World Mechanics

## A. Map Marker System
- `🚪 Used Warp`: For any warp that has been traversed.
- `☠️ Defeated Trainer`: For any trainer that has been battled.
- `✅ Item Picked Up`: For any overworld item that has been collected.
- `🚫 Dead End`: For paths that have been confirmed to lead nowhere.
- `🗝️ Puzzle Solved/Obstacle Cleared`: For puzzles or obstacles that have been overcome.
- `💬 Non-Battling NPC`: For NPCs that have been confirmed to not engage in battle.
- `💖 Healing Zone`: For tiles that provide party healing.

## B. Special Mechanics & Discoveries
- **Menu Input Blocking (CRITICAL):** Facing an impassable tile blocks that directional input in menus. This makes any menu navigation tool that relies on fixed directional inputs fundamentally unreliable unless the player is in an open space.
- **HM Usage:** Must be adjacent to and facing the target object before opening the party menu.
- **Boulder Pushing:** A multi-turn action. Cannot be done while surfing.
- **Dead End Definition:** A map is only a dead end if it has only one exit warp/connection and no reachable unseen tiles. The nature of the destination map is irrelevant to this classification.
- **SURF vs. DIG:** The move SURF will miss an opponent that is underground from using DIG.

## C. Type Effectiveness & Insights
- Electric is not very effective against Electric-types.
- Electric is not very effective against Grass/Poison dual-types.
- **Wild Pokémon Speed (Cerulean Cave):** Wild Pokémon are deceptively fast.
- **Wild Pokémon Moves (Cerulean Cave):** GOLEM can use SELFDESTRUCT. It dealt significant neutral damage to TITANESS (Normal-type).
- **SELFDESTRUCT:** Not very effective vs. Rock/Ground; Neutrally effective vs. Ground.
- **Type Immunity:** Electric moves have no effect on Ground-types.

## D. Known Pokemon Locations
- **Cerulean Cave:** Ditto, Wigglytuff, Electrode, Golem, Raichu, Sandslash, Parasect, Lickitung, Magneton, Dodrio, RHYDON, VICTREEBEL.
- **Pokémon Tower:** GASTLY, CUBONE.

## E. Tile Traversal Rules
- **Healing Zone:** A tile described as a "purified, protected zone" that fully heals all Pokémon in the party's HP and restores all their PP. Found on Pokémon Tower 5F.
- **Steps Tile:** Allows movement between 'ground' and 'elevated_ground' tiles.
- **Ground/Elevated Ground:** Standard walkable tiles. Cannot move between them directly.
- **Impassable:** Walls, rocks, etc. Cannot be entered.
- **Ladder (Up/Down):** Acts as a warp to a different floor.
- **Water:** Requires the HM Surf to cross. Can only be entered from an adjacent land tile.
- **Ledge:** A one-way obstacle. Can only be jumped down from above (Y-1). Attempting to move up or sideways into a ledge will fail.

# III. Active Puzzles & Navigation Strategy

## A. Pokémon Tower 7F (Dead End Puzzle)
- **Observation:** Reached the top floor (7F) of the Pokémon Tower. The path is a confirmed dead end with no visible exits or interactable objects.
- **Hypothesis 1 (Failed - 15+ attempts):** Interacting with Pikachu or the environment would trigger a cutscene. **Test:** Pressed 'A', 'B', 'Start', and directional buttons repeatedly at (12, 3). **Result:** No event triggered. **Conclusion:** This was a severe case of Confirmation Bias. Standard interaction is not the solution.
- **Hypothesis 2 (Failed - Agent Suggestion):** Use the POKé FLUTE at the northernmost point (12, 3) to trigger a spectral event. **Test:** Navigated to (12, 3) and used POKé FLUTE from the item menu. **Result:** The game displayed text confirming the flute was played ("Now, that's a catchy tune!"), but no event occurred. **Conclusion:** The POKé FLUTE has no special effect on this floor. The area remains a dead end.
- **Hypothesis 3 (Untested):** Use the SILPH SCOPE might reveal a hidden object or ghost, as simple interaction and the POKé FLUTE have failed.

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

## A. Data-Driven Debugging Logs
- **`use_hm_from_party` Manual Test (Cut):**
  - **Attempt 1 (Failure):** Selected 'CUT'. Game returned error "There isn't anything to CUT!". **Conclusion:** Player must be facing the target object *before* opening the menu to use an HM.
  - **Attempt 2 (Success):** Faced tree, then navigated menu. **Discovery:** Party screen cursor position is not reliably at the top. A cursor-resetting sequence (e.g., spamming 'Up') is necessary for a robust tool.
- **Snorlax Puzzle (Route 12):**
  - **Hypothesis 1 (Failed):** Use POKé FLUTE from 'ITEM' menu. Result: Led to an HM-only screen.
- **Hypothesis 2 (Failed - Agent Suggestion):** Switch inventory 'pockets' with Left/Right. Result: No effect. The inventory does not appear to have pockets.
- **Hypothesis 3 (Failed):** Interact directly with Snorlax using 'A'. Result: No effect.
- **Hypothesis 4 (Success):** The item menu is a single, scrollable list. After selecting 'ITEM' from the main menu, scroll down past the HMs (indicated by a '↓' arrow) to find Key Items like the POKé FLUTE. Using it from this menu wakes the Snorlax.

## B. Tool Development Lessons
- **Menu Cursor Behavior (Critical Lesson):** Menu cursor starting positions are non-deterministic. A single manual test is insufficient to establish a reliable pattern. Tools that navigate menus MUST force a known state (e.g., by repeatedly pressing 'Up' to reset the cursor to the top) rather than assuming a specific starting position. This was the root cause of the `use_hm_from_party` failure loop.
- **SURF vs. DIG:** The move SURF will miss an opponent that is underground from using DIG.
- **Menu Navigation Tool Failures (CRITICAL):** My past menu tools (`use_hm_from_party`, `switch_pokemon_navigator`) were fundamentally flawed. My `menu_navigator` tool is also critically flawed due to the 'Menu Input Blocking' mechanic. Its cursor-resetting logic (spamming 'Up') will fail if the player is adjacent to an impassable tile, making it unreliable. **Conclusion:** These tools are effectively retired. A new, environment-aware solution using a 'Menu Analyzer' and a selection tool is the only path forward. I have since created `menu_analyzer` and `select_menu_option` to address this.

## C. Navigational Lessons
- **Dead End Definition (Correction):** A 'dead end area' assessment applies to the *entire map's* reachable exits (warps/connections). An isolated section is not a dead end if other exits exist elsewhere on the map, even if currently unreachable from my position. This was the cause of my hallucination on Cerulean Cave 2F.
- **Warp Reachability (Correction):** A warp being listed in `Map Events` does not guarantee it is reachable from the current position. The map is often partitioned. I must verify pathability by analyzing the map layout or using a pathfinding tool before assuming a warp is accessible. This was the cause of my hallucination on Cerulean Cave 1F.
- **Sequential Tool Call Failure:** Calling multiple tools that depend on menu state changes in the same turn (e.g., one tool to open a menu, a second to navigate it) is unreliable and can fail. Only one menu-altering tool should be called per turn to ensure the game state updates correctly before the next action.
- **Decoy Entrances:** I must be wary of decoy entrances that lead to isolated areas. If an entrance doesn't lead to the main part of a location, I should immediately suspect it's a trick and search for an alternative path instead of trying to force progress from the decoy spot (e.g., Cerulean Cave's fake entrance).
- **'Map Analyzer' Tool (HIGH PRIORITY):** To prevent future navigational hallucinations, I need a tool that can analyze the map XML to reliably report all reachable warps and unseen tiles from my current position. This is critical for accurate exploration.

## D. Self-Assessment Insights (Turn 188789)
- **Confirmation Bias (River Exploration):** I spent too long exploring the rivers in Cerulean City and Route 24 based on the weak hypothesis that a new entrance to Cerulean Cave must be there. I should have used the `map_analyzer` tool sooner to definitively prove it was a dead end instead of manually exploring every tile. This is a key lesson in trusting data over intuition.
- **Agent Opportunity (`maze_navigator_agent`):** My manual, step-by-step navigation of the Route 25 maze was effective but inefficient. This type of complex, multi-step pathing is a perfect candidate for a high-level reasoning agent that could analyze a maze layout and generate the sequence of intermediate goals for the `find_path` tool.
- **Task (Deferred):** Mark all non-battling NPCs on Route 25 when I return there.

# VI. Self-Correction & Hallucination Log
## A. Navigational Hallucinations
- **Route 24 Unseen Tiles (Turn 188804):** I incorrectly reported 67 reachable unseen tiles when the system confirmed there were 0. **Conclusion:** My manual assessment of map exploration status is highly unreliable. I MUST use the `map_analyzer` tool to get an accurate count of reachable unseen tiles and warps before making any exploration decisions. Trusting my own visual scan leads to critical errors.
- **Warp Hallucination (Cerulean Gym - Turn 188811):** I incorrectly reported 0 reachable warps when the exit warps at (5, 14) and (6, 14) were reachable. **Conclusion:** This is a repeat of the unseen tile hallucination. I MUST use the `map_analyzer` tool to verify reachable warps and tiles before making navigational claims or decisions. Manual assessment is proven to be unreliable.

## C. Cerulean Cave Entrance Puzzle
- **Hypothesis 1 (Failed):** Interacting with follower Pikachu at (5, 4) in the Cerulean Gym will open the path to Cerulean Cave. **Test:** Stood at (5, 4), faced Pikachu, and pressed 'A'. **Result:** No event triggered. **Conclusion:** This interaction is not the trigger, or it was a one-time event for the Misty rematch.

# VII. Self-Assessment & Correction Log (Turn 188841)

## A. Critical Failures Identified
- **Notepad Management:** My attempt to reorganize my notepad with `overwrite` failed due to a safeguard against massive data loss. This highlights a flaw in my approach to data management. I summarized too aggressively instead of purely restructuring. **Lesson:** For large reorganizations, I must be more careful, or break the process into smaller, verifiable steps using `replace`.
- **Navigational Hallucination (Route 4):** I had a severe hallucination, believing I was in Cerulean City when I was on Route 4. This led to a tool crash and a failed strategic plan. **Conclusion:** I must be more vigilant in verifying my location in the Game State Information after every map transition. This is a repeat failure and indicates a critical flaw in my verification process.