# I. Core Principles & Lessons Learned
- **Systematic Debugging is Mandatory:** My previous brute-force method of fixing tools was a critical failure. I must use `run_code` with print statements and my `code_debugger_agent` to systematically diagnose issues before attempting a fix.
- **Falsify Your Beliefs:** I must actively try to disprove my own conclusions with alternative tests after an initial hypothesis is confirmed. My assumption that B2F was disconnected was a major case of confirmation bias, which the system warnings corrected.

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

# III. Puzzle Logs & Future Development
## A. Seafoam Islands Boulder Puzzle
- **Goal:** Stop the strong water current on Seafoam Islands B4F.
- **Current Hypothesis:** The solution involves a complex, multi-floor boulder puzzle. The system has confirmed that B2F is fully connected, meaning there is a path from the western platforms to the eastern platforms on that floor. I must find this path.
- **Previous Failed Hypotheses:**
  1. The boulders on B3F's eastern platform would stop the current. (Failed, couldn't reach the southern boulders).
  2. The path to the southern B3F boulders was through 1F. (Failed, 1F is disconnected).
  3. The western B2F ladder was a dead end. (Failed, system confirmed all B2F ladders are connected).

## B. Future Development Ideas
- Create a new agent, `debug_log_interpreter`, that can analyze the output of `run_code` with debugging print statements to identify the root cause of a script failure.
## D. Seafoam Islands Puzzle Log
- **Current Hypothesis:** The path connecting the western and eastern sections of the cave is on B2F. All other floors appear to be disconnected.
- **Current Plan:** Use the pathfinder to check for a route from the western side of B2F to the eastern side.
- **Failed Hypothesis #4 (B3F Connection):** The boulder puzzle on B3F could not be solved from the western access point. The ground level of B3F is disconnected, making the boulders unreachable. The pathfinder confirmed no walkable path to the eastern ladders exists from the west.