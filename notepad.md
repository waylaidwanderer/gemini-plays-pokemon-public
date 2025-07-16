# I. Core Principles & Lessons Learned
- **Systematic Debugging is Mandatory:** My previous brute-force method of fixing tools was a critical failure. I must use `run_code` with print statements and my `code_debugger_agent` to systematically diagnose issues before attempting a fix. Tool refinement is the highest priority.
- **Falsify Your Beliefs:** I must actively try to disprove my own conclusions. My assumption that the Seafoam Islands cave was a single interconnected dungeon was a major case of confirmation bias.

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
- `gate_offscreen`/`closed_gate`/`open_gate`: Gates that can block paths.
- `secret_passage`: Certain `impassable` wall tiles can be walked through.
- `strong_current`: A water tile with a current that is too strong to SURF against. Boulders may affect its flow.

## B. Confirmed ROM Hack Changes
- **Type Matchups & Immunities:** Psychic > Ghost/Poison; Ghost > Psychic; Electric > Rock/Water; CUT (Normal) > VICTREEBEL (Grass/Poison); Flying > Grass/Poison; Psychic > Flying; Ice > Ground; Ground > Poison; Ground > Fire; Rock > Fire; Normal !> Psychic; Electric !> Grass; Rock !> Ground; Psychic !> Psychic; Bite (Normal) !> HAUNTER (Ghost/Poison); Ice !> Gyarados (Water/Flying); Poison !> Poison; Ice !> Water; Poison !> Ground; Flying immune to Ground; Ground immune to Electric; MUK immune to Poison; HYPNO immune to STUN SPORE; MUK immune to THUNDER WAVE; MAROWAK immune to POISON GAS.
- **Battle & Field Mechanics:** PSYWAVE/CONFUSE RAY can miss. Safari Zone has a time limit. Losing in a gym does not warp you out. FLY can end wild battles indoors but cannot be used to escape buildings. ROAR can end wild battles.

# III. Puzzle Logs
## A. Seafoam Islands Boulder Puzzle
- **Goal:** Stop the strong water current on Seafoam Islands B4F.
- **Current Hypothesis:** The Seafoam Islands consist of two separate, disconnected caves. The western cave is a dead end for the puzzle. The solution must be in the eastern cave. Access to the eastern section of Route 20 (and thus the eastern cave entrance) must be found by navigating the water routes from Route 19, not by direct surfing from the western part of Route 20.
- **Current Plan:** The Route 19 path has been exhausted. The new plan is to travel to Cinnabar Island and explore the sea routes east of it.
- **Falsified Hypothesis Log:**
  1. The western and eastern sections of the cave are connected internally. (Failed, pathfinder confirmed no path exists on any floor).
  2. The eastern island on Route 20 is reachable by surfing directly from the western part of the route. (Failed, pathfinder v14 confirmed no path exists).
  3. The path to the eastern Seafoam Islands entrance is accessible from a southern connection on Route 19. (Failed, both southern connections on Route 19 led to isolated, dead-end sections of Route 20).
- **Falsified Hypothesis Log:**
  1. The western and eastern sections of the cave are connected internally. (Failed, pathfinder confirmed no path exists on any floor).
  2. The eastern island on Route 20 is reachable by surfing directly from the western part of the route. (Failed, pathfinder v14 confirmed no path exists).
- **SURF Field Move:** To use SURF, you must be standing on a valid land tile (e.g., `ground`) directly adjacent to a `water` tile and be *facing* the water before opening the menu to select the move.