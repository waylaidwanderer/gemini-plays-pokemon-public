# I. Core Principles & Lessons Learned
- **Immediate Maintenance is Mandatory:** I must perform maintenance (notepad, agents) and fix tools *immediately*. Deferring these actions is a critical process failure. My delay in fixing the pathfinder was a major error.
- **Systematic Problem Solving:** For any puzzle, I must use my notepad to log observations, form a single testable hypothesis, record the test and its outcome, and then form a conclusion. This structured approach prevents chaos and tunnel vision.
- **Falsify Your Beliefs:** To avoid confirmation bias, I must actively try to disprove my own conclusions with alternative tests after an initial hypothesis is confirmed.

# II. Game Mechanics & Battle Intel
## A. Tile Mechanics & Traversal
- `ground`: Standard walkable tile.
- `impassable`: Walls, furniture, etc. Cannot be walked on.
- `elevated_ground`: Walkable ground at a different elevation. Traversal to/from `ground` requires `steps`.
- `steps`: Allows vertical movement *only* between adjacent `ground` and `elevated_ground` tiles.
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
  - **Observation:** The sign on B4F states "Boulders might change the flow of water!". The strong water current at (21,17) on B4F has not been stopped by the boulders I pushed from B1F and B2F.
  - **Hypothesis:** To stop the current on B4F, I must push the boulders on B3F into the holes on B3F. The boulders are at (6, 15), (4, 16), (9, 15), and (10, 15). The holes are at (4, 17) and (7, 17).
  - **Current Test:** I will navigate to the ground level of B3F and attempt to push the boulders at (9,15) and (10,15) into the hole at (7,17).

# IV. Ideas & Future Plans
- **Agent Idea:** Create a `multi_floor_puzzle_strategist_agent` that can analyze puzzle elements across different maps (e.g., Seafoam Islands) and devise a high-level, multi-step solution plan.