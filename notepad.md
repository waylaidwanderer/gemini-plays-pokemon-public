# I. Core Directives & Lessons

## A. Core Directives
1.  **IMMEDIATE MAINTENANCE:** All data management (notepad, markers) and tool/agent refinement is the HIGHEST priority and MUST be performed in the same turn a need is identified.
2.  **PROACTIVE AUTOMATION:** Before any complex or repetitive task, I must first consider automating it with a tool or agent. If one doesn't exist, creating it is the new priority.
3.  **TRUST, BUT REFINE:** I must trust the outputs of my agents and system data. If an agent or tool is suboptimal, I must prioritize refining it immediately.
4.  **ABANDON FAILED HYPOTHESES:** If a strategy fails repeatedly, I must recognize the pattern, document it, and pivot to a new approach.

## B. Key Lessons & Recurring Failures
- **Positional & Data Awareness:** I MUST verify my current coordinates, turn number, and system-provided data from the Game State Information *before* every action and trust it over my own manual assessment.
- **Dead End Definition:** A map is a dead end ONLY if it has 1 or fewer reachable exits (warps/connections) AND 0 reachable unseen tiles. I must be rigorous in this calculation.
- **System vs. Local Reachability:** System warnings about "reachable" tiles/warps are a global check for the entire map and may not reflect what is reachable from my current partitioned location.
- **Confirmation Bias in Debugging:** Wasting multiple turns on small, failed fixes for a tool is a critical error. LESSON: If a tool fix fails more than twice, I must pivot to a different debugging strategy (e.g., complete overhaul or using `run_code` to test logic).
- **Simple Solutions First (Overwatch):** When stuck, I must test the most basic solutions (e.g., closing a dialogue box with 'A') before hypothesizing complex puzzles.
- **`define_tool` Staleness (Turn 194368):** The `define_tool` system can serve a stale version of a script. If a tool fails after a fix, I must test the raw code with `run_code` to differentiate between logic errors and system issues.

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

## B. Solved Puzzles & Key Events
- **Snorlax (Routes 11 & 12):** Awakened using the POKé FLUTE from the ITEM menu.
- **Pokémon Tower Ghost:** Used SILPH SCOPE to reveal the ghost.
- **Seafoam Islands Current:** Solved multi-floor boulder puzzle to stop the strong water current.
- **Mt. Moon Super Nerd Block (Turn 194398):** NPC at (25, 32) on 1F creates a dialogue trigger on tile (25, 31) that blocks all movement. Solution is to press 'A' to dismiss the dialogue.

## C. Obstacles & Solutions
- **Rocket Grunt (Mt. Moon B2F at 30, 12):** Confirmed via dialogue that he is blocking the path south and demands a fossil to pass.

# IV. Active Hypotheses & Test Results

- **Hypothesis 1:** The fossil needed to pass the Rocket Grunt is located in the lower floors of Mt. Moon, accessible from the western entrance. **Test Plan:** Thoroughly explore B1F and B2F via the ladder at (6, 6) on 1F.
- **Untested Assumption 1:** The Officer Jenny blocking the path in Cerulean City is a permanent story block.

# V. Tool & Agent Development

## A. Active Agents
- **`stuck_navigator_agent`**: Suggests high-level navigational pivots when tools fail.

## B. Development Lessons
- **Menu Cursor Behavior:** Menu cursor starting positions are non-deterministic.
- **Battle Move Selection:** The move selection menu is a single-column list navigated with UP/DOWN only. LEFT/RIGHT have no effect.

## C. Tool Ideas
- **Map Connectivity Analyzer:** A tool that takes the map XML and analyzes its structure to identify all distinct, partitioned areas. It would output which warps/connections belong to which partition. This would allow for much more strategic exploration of complex maps like Mt. Moon and prevent wasting time in dead-end zones.