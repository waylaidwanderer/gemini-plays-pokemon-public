# I. Core Directives & Self-Correction

## A. Core Directives
- **D1: IMMEDIATE DATA & TOOL MANAGEMENT:** All data management (notepad, markers) and tool/agent refinement is the HIGHEST priority and MUST be performed in the same turn a need is identified.
- **D2: ACT ON DOCUMENTATION:** A documented lesson that does not result in a behavioral change is a critical failure.
- **D3: ABANDON FAILED HYPOTHESES:** If a strategy fails repeatedly, I must recognize the pattern, document it, and pivot to a new approach.
- **D4: TRUST, BUT REFINE:** I must trust the outputs of my agents and system data. If an agent or tool is suboptimal, I must prioritize refining it immediately.
- **D5: PROACTIVELY AUTOMATE:** Before performing any complex or repetitive task, I must first consider if it can be automated with a tool or agent.
- **D6: BATTLE EFFICIENCY:** Do not use complex agents for trivial wild battles. Handle them manually for maximum speed.

## B. Key Lessons & Recurring Failures (Hallucination Log)
- **Positional & Data Awareness:** I MUST verify my current coordinates, turn number, and system-provided data from the Game State Information *before* every action and trust it over my own manual assessment.
- **Dead End Definition & Application:** My manual application of the dead-end definition is critically flawed. A map is a dead end ONLY if it has 1 or fewer reachable exits (warps/connections) AND 0 reachable unseen tiles. I must be rigorous in this calculation.
- **System vs. Local Reachability (Turn 193685 - CRITICAL):** System warnings about "reachable" tiles/warps are a global check for the entire map and may not reflect what is reachable from my current partitioned location. A local reachability check (like from a working tool) is necessary for immediate navigation decisions.
- **Confirmation Bias in Debugging (Turn 193715):** I wasted over a dozen turns attempting to patch `map_analyzer`, assuming each small change would work. This was confirmation bias. LESSON: If a tool fix fails more than twice, I must pivot to a different debugging strategy (e.g., complete overhaul, using an agent, or deleting the tool) instead of repeating the same failed approach.

# II. Game Data

## A. Type Chart (Verified)
- Electric is not very effective against Electric, Grass/Poison, and Bug/Grass types.
- Ground moves do not affect GASTLY (Ghost/Poison).
- Normal moves do not affect Ghost-types.
- Normal is not very effective against GEODUDE (Rock/Ground).
- Poison is not very effective against Ground-types.

## B. Known Pokemon Locations
- **Cerulean Cave:** Ditto, Wigglytuff, Electrode, Golem, Raichu, Sandslash, Parasect, Lickitung, Magneton, Dodrio, RHYDON, VICTREEBEL, GOLBAT, KADABRA.
- **Pokémon Tower:** GASTLY, CUBONE.

## C. Key Trainer Rosters
- **Nurse Joy (Fuchsia Pokecenter):** KANGASKHAN (Lv 65): DOUBLE-EDGE, DOUBLE TEAM; SNORLAX (Lv 65): ICE BEAM, REST

# III. World Data

## A. Tile Mechanics (Verified)
- **`ground`**: Basic walkable tile.
- **`grass`**: Walkable tile with wild Pokémon encounters.
- **`impassable`**: Walls and other obstacles that cannot be walked on.
- **`ledge`**: Can only be jumped down from above (Y-1). Impassable from below and sides.
- **`steps`**: Allows movement between `ground` and `elevated_ground`.
- **`elevated_ground`**: Can only be accessed from `steps` or other `elevated_ground` tiles. Cannot be accessed directly from `ground`.
- **`cuttable`**: Can be cut with HM Cut. Respawns on map change.
- **`ladder_up`/`ladder_down`**: Warps that function as instant transitions between floors.

## B. Solved Puzzles & Key Events
- **Pewter Museum 2F:** Solved blocking NPC puzzle by interacting with follower Pikachu adjacent to a Scientist.
- **Snorlax (Routes 11 & 12):** Awakened using the POKé FLUTE from the ITEM menu.
- **Pokémon Tower Ghost:** Used SILPH SCOPE to reveal the ghost, allowing passage to rescue Mr. Fuji.
- **Seafoam Islands Current:** Solved multi-floor boulder puzzle to stop the strong water current on B4F.

## C. Key Locations & Discoveries
- **Mt. Moon Entrances:** The eastern entrance (from Route 4, near Route 3) is the presumed main path. The western entrance (from Route 4, near Cerulean) leads to a separate section that was fully explored and confirmed to not contain a fossil.
- **Celadon Dept. Store:** Sells TMs, stat-boosters, POKé DOLLs, and evolution stones.
- **Route 12:** Location of the Super Rod House.
- **Cinnabar Island:** Home to a Pokémon Lab that can regenerate fossils.

## D. Obstacles & Solutions
- **Rocket Grunt (Mt. Moon B2F at 30, 12):** Confirmed via dialogue that he is blocking the path south and demands a fossil to pass. This route is a dead end until a fossil is acquired.

# IV. Active Hypotheses & Test Results

- **Conclusion: Mt. Moon Navigation (Turn 194304):** My previous belief that I was trapped in the western section of Mt. Moon was a hallucination caused by confirmation bias. The area has multiple exits. The correct path forward is to enter Mt. Moon from the eastern entrance on Route 4.
- **Hypothesis 1:** The eastern section of Mt. Moon contains a fossil needed to pass the Rocket Grunt on B2F. **Test Plan:** Thoroughly explore the eastern section of Mt. Moon.
- **Untested Assumption 1:** The Officer Jenny blocking the path in Cerulean City is a permanent story block.
- **Untested Assumption 2:** The Hiker at (6, 7) on Mt. Moon 1F is a non-battling NPC. **Test Plan:** Interact with him at the next opportunity.

# V. Tool & Agent Development

## A. Active Agents
- **`stuck_navigator_agent`**: Suggests high-level navigational pivots when tools fail.

## B. Active Tools
- **`automated_path_navigator`**: Automates pathfinding and movement, useful for interruption-heavy routes.

## C. Agent & Tool Ideas (Prioritized based on Overwatch feedback)
- **`navigation_manager_agent` (CRITICAL PRIORITY):** A stateful agent that remembers a long-term navigation goal and automatically re-plans/re-issues movement commands after interruptions like wild battles. This is a top priority to improve efficiency, as noted by Overwatch.
- **`automated_path_navigator` Improvement (HIGH PRIORITY):** Refine the tool to provide context on failure (e.g., coordinates and type of blocking tile). Overwatch noted this is a critical enhancement.
- **`automated_battle_agent`**: An agent to handle trivial wild battles by automatically selecting the first available super-effective move.
- **`exploration_planner_agent`**: Analyzes map sprites to generate an optimal exploration route to all un-interacted-with NPCs and items.
- **`fossil_finder_agent`**: Analyzes world map data to suggest likely fossil locations.
- **`gym_prep_agent`**: Suggests an optimal team of 6 for a given gym type.
- **`puzzle_documentation_agent`**: Formats puzzle summaries for the notepad.
- **`notepad_organizer_agent`**: Automates notepad cleaning and reorganization.

## D. Key Development Lessons & Bugs
- **`use_hm_tool` Failure:** A single tool cannot perform a multi-stage, dynamic menu navigation task. The correct approach is a sequential, multi-turn process using `menu_analyzer` and `select_menu_option`.
- **Menu Cursor Behavior:** Menu cursor starting positions are non-deterministic. Tools must force a known state rather than assuming a start position.
- **`map_analyzer` Deletion (Turn 193716):** The tool was fundamentally flawed, failing to parse partitioned maps. After multiple failed fixes, it was deleted as it was a liability causing navigational hallucinations.
- **Overwatch Lesson (CRITICAL):** Tool refinement is a non-deferrable, highest-priority action. I MUST fix or delete faulty tools in the same turn a flaw is discovered.
- **`navigate_with_retries` Tool Flaw:** The concept is better suited for an agent, as tools are stateless and cannot remember a navigation goal across turns.

## D. Key Development Lessons & Bugs
- **Battle Move Selection:** The move selection menu is a single-column list navigated with UP/DOWN only. LEFT/RIGHT have no effect.
- **`define_tool` Staleness (Turn 194369):** Discovered that `automated_path_navigator` was failing because the `define_tool` system was serving a stale version of the script. The Python logic itself was correct, as proven by a `run_code` test. LESSON: If a tool repeatedly fails after a fix, test the raw code with `run_code` to differentiate between logic errors and system issues.