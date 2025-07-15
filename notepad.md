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
  - **Hypothesis 1:** To stop the current on B4F, I must push the boulders on B3F into the holes on B3F.
  - **Test (Turn 75987):** Pushed boulders at (6,15) and (4,16) into holes at (7,17) and (4,17). Then, attempted to SURF on B4F.
  - **Outcome:** Received message 'The current is much too fast!'.
  - **Conclusion:** Hypothesis 1 is FALSE. The boulders on B3F that I could access did not stop the current. There are more boulders on a southern platform I cannot reach. I need to find a path to this southern area.
  - **Hypothesis 2:** The path to the southern platform on B3F is accessible from B2F.
  - **Lesson Learned (B1F):** Repeatedly failed to path north from (14,15) due to an impassable wall. This confirms the need to verify paths and avoid repeating failed actions.
  - **Observation (B4F):** System states there are 15 reachable unseen tiles in the west. My pathfinder, based on the map XML, reports the west is unreachable due to an impassable wall at X=20.
  - **Hypothesis 3:** The map XML is incorrect, and the `impassable` tile at (20, 16) is secretly traversable.