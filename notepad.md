# I. Core Principles & Lessons Learned
- **System Validation is Absolute Truth:** The game's validation data (e.g., reachable warps) is the ultimate source of truth. If my tools or understanding contradict this data, my tools/understanding are wrong and must be corrected immediately. I will not proceed with actions based on faulty assumptions.
- **Rigorous Hypothesis Testing:** When faced with a puzzle, I will form a single, testable hypothesis and design a minimal experiment to confirm or deny it. I will not assume hidden mechanics like secret passages unless all other possibilities, especially tool failure, have been disproven through systematic debugging.
- **Tool Integrity is Paramount:** A faulty tool is worse than no tool. If a tool provides an incorrect result (e.g., `pathfinder` failing to find a confirmed reachable warp), debugging and fixing that tool becomes my absolute highest priority, superseding any navigational or puzzle-solving goal.

# II. Game Mechanics & Battle Intel
## A. Tile Mechanics & Traversal
- `ground`: Standard walkable tile.
- `impassable`: Walls, furniture, etc. Cannot be walked on.
- `elevated_ground`: Walkable ground at a different elevation. Traversal to/from `ground` requires `steps`.
- `steps`: Allows vertical movement *only* between adjacent `ground` and `elevated_ground` tiles.
- `grass`: Tall grass where wild Pokémon appear.
- `ledge`: One-way traversal, can be jumped down but not up.
- `water`: Requires SURF to traverse. Transition to/from land is only possible on `ground`, `grass`, or `steps` tiles.
- `cuttable`: A tree that can be cut with HM01 Cut.
- `hole`: A tile that causes the player to fall to the floor below.
- `spinner_up/down/left/right`: Forces movement in a specific direction.
- `ladder_up`/`ladder_down`: Warps that function as ladders between floors.
- `gate_offscreen`/`closed_gate`/`open_gate`: Gates that can block paths. `gate_offscreen` should be treated as potentially open for pathfinding unless a map marker indicates it is closed.
- `secret_passage`: Certain `impassable` wall tiles can be walked through.
- `strong_current`: A water tile with a current that is too strong to SURF against. Boulders may affect its flow.
- `boulder`: Can be pushed with STRENGTH. Pushing a boulder into a `hole` tile causes it to fall to the floor below, potentially altering the lower map.

## B. Confirmed ROM Hack Changes
- **Type Matchups & Immunities:** Psychic > Ghost/Poison; Ghost > Psychic; Electric > Rock/Water; CUT (Normal) > VICTREEBEL (Grass/Poison); Flying > Grass/Poison; Psychic > Flying; Ice > Ground; Ground > Poison; Ground > Fire; Rock > Fire; Normal !> Psychic; Electric !> Grass; Rock !> Ground; Psychic !> Psychic; Bite (Normal) !> HAUNTER (Ghost/Poison); Ice !> Gyarados (Water/Flying); Poison !> Poison; Ice !> Water; Poison !> Ground; Flying immune to Ground; Ground immune to Electric; MUK immune to Poison; HYPNO immune to STUN SPORE; MUK immune to THUNDER WAVE; MAROWAK immune to POISON GAS.
- **Battle & Field Mechanics:** PSYWAVE/CONFUSE RAY can miss. Safari Zone has a time limit. Losing in a gym does not warp you out. FLY can end wild battles indoors but cannot be used to escape buildings. ROAR can end wild battles. SURF requires facing the water tile. Switches (e.g., in statues or hidden on posters) must be activated by standing on the tile directly below them, facing up, and pressing A.

# III. Puzzle Logs & Future Plans
## A. Pokémon Mansion: Master Plan
- **Objective:** Find the SECRET KEY.
- **Guiding Strategy (from multi_floor_puzzle_strategist_agent):** The puzzle requires activating a sequence of four switches across four floors to open all gates and access the key.
- **Step 1 (Done):** On 1F, activate the switch at (3, 6).
- **Step 2 (Done):** Ascend to 2F via stairs at (6, 11).
- **Step 3 (Done):** On 2F, activate the switch at (3, 12).
- **Step 4 (Done):** Ascend to 3F and activate the switch at (11, 6).
- **Step 5 (Hypothesis):** The previous actions should have opened the Central Gates at (21, 18)/(22, 18).
- **Step 6 (Next):** Go to 1F and check the Central Gates. If open, proceed through them to the warp at (22, 24) to reach B1F.
- **Step 7:** On B1F, activate the final switch at (19, 26). This should open the Western Gates on 1F.
- **Step 8:** Return to 1F via the warp at (24, 23).
- **Step 9:** Navigate to the now-open Western Gates at (25, 14)/(26, 14) and retrieve the SECRET KEY.

## B. Future Tool Development
- **`grid_visualizer`:** Create a tool to print a formatted grid from the `map_xml_string` for easier pathfinding debugging. This would be more efficient than manually adding print statements to `run_code`.