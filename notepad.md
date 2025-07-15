# I. Core Principles & Lessons Learned
- **Trust the Data & Your Tools:** I must trust the game's data and the output of my verified tools over my own flawed perception. My failure to trust `gem_path_planner_v4`'s complex but correct path led to a significant waste of time trying to manually navigate, which was impossible. When a tool gives an unexpected result, the first step is to analyze *why* it might be correct, not to assume it's broken.
- **Immediate Maintenance is Mandatory:** I must perform maintenance (notepad, agents) and fix tools *immediately*. Deferring these actions is a critical process failure. My delay in fixing the pathfinder was a major error.
- **Systematic Problem Solving:** For any puzzle, I must use my notepad to log observations, form a single testable hypothesis, record the test and its outcome, and then form a conclusion. This structured approach prevents chaos and tunnel vision.
- **Falsify Your Beliefs:** To avoid confirmation bias, I must actively try to disprove my own conclusions with alternative tests after an initial hypothesis is confirmed. My repeated failures with the pathfinding tool stemmed from only testing if it worked and not actively trying to find ways it would fail.

# II. Game Mechanics & Battle Intel
## A. Tile Mechanics & Traversal
- `ground`: Standard walkable tile.
- `impassable`: Walls, furniture, etc. Cannot be walked on.
- `elevated_ground`: Walkable ground at a different elevation. Traversal to/from `ground` requires `steps`.
- `steps`: Allows vertical movement *only* between adjacent `ground` and `elevated_ground` tiles. Cannot be used to transition between two `ground` tiles or two `elevated_ground` tiles.
- `grass`: Tall grass where wild Pokémon appear.
- `ledge`: One-way traversal, can be jumped down but not up.
- `water`: Requires SURF to traverse.
- `cuttable`: A tree that can be cut with HM01 Cut.
- `hole`: A tile that causes the player to fall to the floor below.
- `spinner_up/down/left/right`: Forces movement in a specific direction.
- `ladder_up`/`ladder_down`: Warps that function as ladders between floors.
- `gate_offscreen`/`closed_gate`/`open_gate`: Gates that can block paths.
- `secret_passage`: Certain `impassable` wall tiles can be walked through.

## B. Confirmed ROM Hack Changes
- **Type Matchups & Immunities:** Psychic > Ghost/Poison; Ghost > Psychic; Electric > Rock/Water; CUT (Normal) > VICTREEBEL (Grass/Poison); Flying > Grass/Poison; Psychic > Flying; Ice > Ground; Ground > Poison; Ground > Fire; Rock > Fire; Normal !> Psychic; Electric !> Grass; Rock !> Ground; Psychic !> Psychic; Bite (Normal) !> HAUNTER (Ghost/Poison); Ice !> Gyarados (Water/Flying); Poison !> Poison; Ice !> Water; Poison !> Ground; Flying immune to Ground; Ground immune to Electric; MUK immune to Poison; HYPNO immune to STUN SPORE; MUK immune to THUNDER WAVE; MAROWAK immune to POISON GAS.
- **Battle & Field Mechanics:** PSYWAVE/CONFUSE RAY can miss. Safari Zone has a time limit. Losing in a gym does not warp you out. FLY can end wild battles indoors but cannot be used to escape buildings. ROAR can end wild battles.

# III. Current Objective & Puzzle Logs
## A. Find the Secret Key (Cinnabar Gym)
- **Current Plan:** Navigate the Seafoam Islands. The path seems to involve a series of boulder puzzles and water currents.
- **Seafoam Islands Puzzle Log:**
  - **B4F Water Current:** The boulders dropped from upper floors did NOT stop the strong water current at (21,17). The direct path south is blocked.
  - **Current Situation:** I am on an isolated western platform on B4F. The ladder to B3F at (12, 8) leads to a dead end. The NPC Kris at (8, 3) is unreachable from my current position. The only way forward appears to be the southern steps at (8, 12).
  - **Pathfinder Tool Status:** `gem_path_planner_v8` is still bugged. It cannot correctly path between land and water via `steps` tiles. Manual navigation is required for now. My top priority is to fix this tool.