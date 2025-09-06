# I. Core Directives & Self-Correction

## A. Core Directives
- **D1: IMMEDIATE DATA & TOOL MANAGEMENT:** All data management (notepad, markers) and tool/agent refinement is the HIGHEST priority and MUST be performed in the same turn a need is identified.
- **D2: ACT ON DOCUMENTATION:** A documented lesson that does not result in a behavioral change is a critical failure.
- **D3: ABANDON FAILED HYPOTHESES:** If a strategy fails repeatedly, I must recognize the pattern, document it, and pivot to a new approach.
- **D4: TRUST, BUT REFINE:** I must trust the outputs of my agents and system data. If an agent or tool is suboptimal, I must prioritize refining it immediately.
- **D5: PROACTIVELY AUTOMATE:** Before performing any complex or repetitive task, I must first consider if it can be automated with a tool or agent.

## B. Key Lessons & Recurring Failures (Hallucination Log)
- **Positional & Data Awareness:** I MUST verify my current coordinates, turn number, and system-provided data from the Game State Information *before* every action and trust it over my own manual assessment.
- **Dead End Definition & Application:** My manual application of the dead-end definition is critically flawed. A map is a dead end ONLY if it has 1 or fewer reachable exits (warps/connections) AND 0 reachable unseen tiles. I must be rigorous in this calculation.
- **Map ID Mismatch (Turn 193072):** Hallucinated a map change that did not occur. LESSON: I MUST verify the `current_map_id` from Game State Information after every warp attempt.
- **Tool Failures in Partitioned Maps (`map_analyzer`/`find_path`):** My navigation tools have repeatedly failed in complex, partitioned maps (e.g., Mt. Moon, Safari Zone), causing incorrect reachability analysis and pathing failures. LESSON: Tool refinement is a non-deferrable, highest-priority action. I must fix faulty tools in the same turn a flaw is discovered and rely on system warnings until they are fixed.
- **Mt. Moon B1F Unseen Tiles (Turn 193077 - CRITICAL):** Received a system warning for reporting 57 reachable unseen tiles and numerous unreachable warps as reachable. This indicates a critical failure in my manual assessment and a bug in my `map_analyzer` tool's ability to detect map partitions. LESSON: I must ALWAYS trust system warnings over my own tools and manual checks, and I need to debug my map analysis tools.
- **Mt. Moon B1F Partition Failure (Turn 193078 - CRITICAL):** Received another system warning for hallucinating 57 reachable unseen tiles and multiple unreachable warps as reachable. This confirms my `map_analyzer` is critically bugged and cannot handle map partitions correctly. LESSON: I must completely distrust my tool's output in complex, multi-level maps and rely solely on system warnings for determining dead ends and reachability until the tool is fixed.
- **Mt. Moon B1F Dead End Miscalculation (Turn 193079 - CRITICAL):** Received a system warning for incorrectly identifying a non-dead-end area as a dead end. This is a recurring failure to correctly apply the definition (2 or more reachable exits = not a dead end). LESSON: I must be more rigorous in my analysis and always trust the system's dead-end calculation over my own flawed manual assessment.

# II. Battle Data

## A. Type Chart (Verified)
- Electric is not very effective against Electric, Grass/Poison, and Bug/Grass types.
- Ground moves do not affect GASTLY (Ghost/Poison).
- Normal moves do not affect Ghost-types.
- Normal is super-effective against Ground-types.
- Poison is not very effective against Ground-types.

## B. Known Pokemon Locations
- **Cerulean Cave:** Ditto, Wigglytuff, Electrode, Golem, Raichu, Sandslash, Parasect, Lickitung, Magneton, Dodrio, RHYDON, VICTREEBEL, GOLBAT, KADABRA.
- **Pokémon Tower:** GASTLY, CUBONE.

## C. Key Trainer Rosters
- **Nurse Joy (Fuchsia Pokecenter):** KANGASKHAN (Lv 65): DOUBLE-EDGE, DOUBLE TEAM; SNORLAX (Lv 65): ICE BEAM, REST

# III. World Data

## A. Solved Puzzles & Key Events
- **Pewter Museum 2F:** Solved blocking NPC puzzle by interacting with follower Pikachu adjacent to a Scientist.
- **Snorlax (Routes 11 & 12):** Awakened using the POKé FLUTE from the ITEM menu.
- **Pokémon Tower Ghost:** Used SILPH SCOPE to reveal the ghost, allowing passage to rescue Mr. Fuji.
- **Seafoam Islands Current:** Solved multi-floor boulder puzzle to stop the strong water current on B4F.

## B. Key Locations & Discoveries
- **Mt. Moon Entrances:** The eastern entrance (from Route 3) is the main path; the western entrance (from Route 4) is a dead end.
- **Celadon Dept. Store:** Sells TMs, stat-boosters, POKé DOLLs, and evolution stones.
- **Route 12:** Location of the Super Rod House.

## C. Active Hypotheses
- **Hypothesis 1:** The required fossil is located on the lower floors of Mt. Moon (B1F/B2F).
    - **Reasoning:** A Rocket Grunt on B2F is looking for one, suggesting their presence.
    - **Test Plan:** Systematically explore all reachable areas of B1F and B2F.
- **Untested Assumption:** The Officer Jenny blocking the path in Cerulean City is a permanent story block.

# IV. Tool & Agent Development

## A. Agent & Tool Ideas
- **`stuck_navigator_agent`**: Suggests high-level navigational pivots when tools fail.
- **`fossil_finder_agent`**: Analyzes world map data to suggest likely fossil locations.
- **`gym_prep_agent`**: Suggests an optimal team of 6 for a given gym type.
- **`puzzle_documentation_agent`**: Formats puzzle summaries for the notepad.
- **`notepad_organizer_agent`**: Automates notepad cleaning and reorganization.
- **`navigation_manager_agent`**: Remembers a long-term navigation goal and re-plans after interruptions.

## B. Key Development Lessons & Bugs
- **`use_hm_tool` Failure:** A single tool cannot perform a multi-stage, dynamic menu navigation task. The correct approach is a sequential, multi-turn process using `menu_analyzer` and `select_menu_option`.
- **Menu Cursor Behavior:** Menu cursor starting positions are non-deterministic. Tools must force a known state rather than assuming a start position.
- **`find_path` / `map_analyzer` Bug (Partitioned Maps):** Both tools have a critical, recurring bug where they fail to correctly parse partitioned map layouts (e.g., Safari Zone, Mt. Moon). This leads to incorrect reachability analysis, pathing failures, and dead-end miscalculations.
- **Overwatch Lesson (CRITICAL):** Tool refinement is a non-deferrable, highest-priority action. I MUST fix faulty tools in the same turn a flaw is discovered.

# V. Game Mechanics & Tile Data

## A. Tile Traversal Rules
- **Ledges:** Can only be jumped down (from Y-1 to Y+2 in one move). Impassable from below or sides.
- **Steps:** The only way to move between `ground` and `elevated_ground`.
- **Ladder Up/Down:** Acts as a warp to a different floor.

## C. New Tool & Agent Ideas (Post-Reflection)
- **`party_manager_agent`**: A specialized agent to automate the multi-step process of switching party members in the menu, combining menu analysis and selection logic.
- **`select_party_member_tool`**: A computational tool that takes a Pokémon's name and calculates the button presses needed to select it in the party menu. This would be a core component of the `party_manager_agent`.