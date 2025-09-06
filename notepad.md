# I. Core Directives & Lessons

## A. Core Directives
1.  **IMMEDIATE MAINTENANCE:** All data management (notepad, markers) and tool/agent refinement is the HIGHEST priority and MUST be performed in the same turn a need is identified.
2.  **PROACTIVE AUTOMATION:** Before any complex or repetitive task, I must first consider automating it with a tool or agent. If one doesn't exist, creating it is the new priority.
3.  **TRUST, BUT REFINE:** I must trust the outputs of my agents and system data. If an agent or tool is suboptimal, I must prioritize refining it immediately.
4.  **ABANDON FAILED HYPOTHESES:** If a strategy fails repeatedly, I must recognize the pattern, document it, and pivot to a new approach.

## B. Key Lessons & Recurring Failures
- **Positional & Data Awareness:** I must verify my current coordinates, turn number, and system-provided data from the Game State Information *before* every action and trust it over my own manual assessment.
- **Dead End Definition:** A map is a dead end ONLY if it has 1 or fewer reachable exits (warps/connections) AND 0 reachable unseen tiles. I must be rigorous in this calculation.
- **System vs. Local Reachability:** System warnings about "reachable" tiles/warps are a global check for the entire map and may not reflect what is reachable from my current partitioned location.
- **Confirmation Bias in Debugging:** Wasting multiple turns on small, failed fixes for a tool is a critical error. If a tool fix fails more than twice, I must pivot to a different debugging strategy (e.g., complete overhaul or using `run_code` to test logic).
- **Simple Solutions First:** When stuck, I must test the most basic solutions (e.g., closing a dialogue box with 'A') before hypothesizing complex puzzles.
- **`define_tool` Staleness:** The `define_tool` system can serve a stale version of a script. If a tool fails after a fix, I must test the raw code with `run_code` to differentiate between logic errors and system issues.

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
- **Mt. Moon:** ZUBAT, SANDSHREW.

## C. Key Trainer Rosters
- **Nurse Joy (Fuchsia Pokecenter):** KANGASKHAN (Lv 65): DOUBLE-EDGE, DOUBLE TEAM; SNORLAX (Lv 65): ICE BEAM, REST

# III. World Data

## A. Tile Mechanics (Verified)
- **`ground`**: Basic walkable tile.
- **`grass`**: Walkable tile with wild Pokémon encounters.
- **`impassable`**: Walls and other obstacles that cannot be walked on.
- **`ledge`**: Can only be jumped down from above (Y-1). Impassable from below and sides.
- **`steps`**: Allows movement between `ground` and `elevated_ground`.
- **`elevated_ground`**: Can only be accessed from `steps` or other `elevated_ground` tiles.
- **`cuttable`**: Can be cut with HM Cut. Respawns on map change.
- **`ladder_up`/`ladder_down`**: Warps that function as instant transitions between floors.
- **`water`**: Impassable without the SURF ability.

## B. Solved Puzzles & Key Events
- **Snorlax (Routes 11 & 12):** Awakened using the POKé FLUTE from the ITEM menu.
- **Pokémon Tower Ghost:** Used SILPH SCOPE to reveal the ghost.
- **Seafoam Islands Current:** Solved multi-floor boulder puzzle to stop the strong water current.
- **Mt. Moon Super Nerd Block (Turn 194398):** NPC at (25, 32) on 1F creates a dialogue trigger on tile (25, 31) that blocks all movement. Solution is to press 'A' to dismiss the dialogue.

## C. Obstacles & Solutions
- **Rocket Grunt (Mt. Moon B2F at 30, 12):** Confirmed via dialogue that he is blocking the path south and demands a fossil to pass.
- **Officer Jenny (Cerulean City):** Blocking path east due to Team Rocket robbery. All attempts to move her by interacting with NPCs, Pikachu, and items in the Trashed House have failed.

# IV. Active Hypotheses & Test Results
- **Hypothesis 1 (Active):** The trigger to move Officer Jenny is located on Route 24 (Nugget Bridge), another known Team Rocket area. **Test Plan:** Proceed north to Route 24 and investigate.
- **Hypothesis 2 (Active):** The fossil needed for the Mt. Moon Rocket Grunt is located on a lower floor of Mt. Moon (B1F or B2F). **Test Plan:** Systematically re-explore all paths on B1F and B2F, starting from known ladders.

# V. Tool & Agent Development

## A. Active Agents & Tools
- **`stuck_navigator_agent`**: Suggests high-level navigational pivots when tools fail.
- **`map_connectivity_analyzer`**: Analyzes map XML to identify partitioned areas.

## B. Development Lessons
- **Lesson: Menu Cursor Behavior:** Menu cursor starting positions are non-deterministic.
- **Lesson: Battle Move Selection:** The move selection menu is a single-column list navigated with UP/DOWN only. LEFT/RIGHT have no effect.

## C. New Tool Ideas
- **`automated_battle_move_selector`**: A tool that takes the output of `battle_strategist_agent` and fully automates the move selection process.
- **`automated_pokecenter_healer`**: A tool to automate the dialogue sequence for healing Pokémon at any Pokémon Center.
- **`puzzle_solver_agent`**: Takes current puzzle context and generates new hypotheses to test.

# VI. Exploration Log
- **Mt. Moon 1F Eastern Corridor (Turn 194646):** Confirmed that the entire eastern corridor originating from the Super Nerd at (25, 32) is a dead end. This invalidates the hypothesis that the fossil is accessible from this part of 1F.
- **Cerulean City Team Rocket Event (Turns 194892-194900):** Confirmed that all interactions within the Trashed House and its backyard (talking to NPCs, interacting with Pikachu, interacting with the hole) do not trigger Officer Jenny to move. This invalidates the hypothesis that the solution is contained solely within that partitioned area.