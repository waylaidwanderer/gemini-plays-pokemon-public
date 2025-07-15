# I. Core Principles & Lessons Learned
- **Immediate Maintenance is Mandatory:** I must perform maintenance (notepad, agents) and fix tools *immediately* when a manual approach fails repeatedly. Deferring these actions, as I did with my pathfinder, is a critical process failure. There is no "later" for an LLM.
- **Trust but Verify:** I must trust my tools and agents, but this trust must be earned. When a tool like my pathfinder repeatedly fails, it's not the map's fault; it's a bug in my code that requires immediate attention.
- **Systematic Problem Solving:** For any puzzle, I must use my notepad to log observations, form a single testable hypothesis, record the test and its outcome, and then form a conclusion. This structured approach prevents chaos and tunnel vision.

# II. Game Mechanics & Battle Intel
## A. Tile Mechanics & Traversal
- `ground`: Standard walkable tile.
- `impassable`: Walls, furniture, etc. Cannot be walked on.
- `elevated_ground`: Walkable ground at a different elevation. Traversal to/from `ground` requires `steps`.
- `steps`: Allows vertical movement between `ground` and `elevated_ground`.
- `grass`: Tall grass where wild Pokémon appear.
- `ledge`: One-way traversal, can be jumped down but not up.
- `water`: Requires SURF to traverse.
- `cuttable`: A tree that can be cut with HM01 Cut.
- `hole`: A tile that causes the player to fall to the floor below.
- `spinner_up/down/left/right`: Forces movement in a specific direction.
- `ladder_up`/`ladder_down`: Warps that function as ladders between floors. Can connect different tile types (e.g., `elevated_ground` to `ground`).
- `gate_offscreen`: A gate not currently on screen. Its state is unknown and treated as potentially open for pathfinding.
- `closed_gate`: A gate that is visibly closed and acts as an impassable wall.
- `open_gate`: A gate that is visibly open and acts as ground.
- `secret_passage`: Certain `impassable` wall tiles can be walked through. These are not visually distinct.

## B. Confirmed ROM Hack Changes
### B1. Type Matchups & Immunities
- **Super Effective:** Psychic > Ghost/Poison; Ghost > Psychic; Electric > Rock/Water; CUT (Normal) > VICTREEBEL (Grass/Poison); Flying > Grass/Poison; Psychic > Flying; Ice > Ground; Ground > Poison; Ground > Fire; Rock > Fire
- **Not Very Effective:** Normal !> Psychic; Electric !> Grass; Rock !> Ground; Psychic !> Psychic; Bite (Normal) !> HAUNTER (Ghost/Poison); Ice !> Gyarados (Water/Flying); Poison !> Poison; Ice !> Water; Poison !> Ground
- **Immunities:** Flying-type immune to Ground-type moves; Ground-type Pokémon are immune to Electric-type moves; MUK immune to Poison-type moves; HYPNO immune to STUN SPORE (powder moves); MUK immune to THUNDER WAVE (Electric-type status move); MAROWAK (Ground-type) immune to POISON GAS (Poison-type move).

### B2. Battle & Field Mechanics
- **Evasion:** PSYWAVE and CONFUSE RAY can fail against targets with high evasion boosts.
- **Safari Zone:** Has a time limit. When it expires, the player is warped back to the Safari Zone Gate.
- **Gym Battle Loss:** Losing a battle inside a gym does NOT warp you to a Pokémon Center.
- **FLY in battle:** The move FLY can be used to defeat a wild Pokémon and end the battle, even when indoors. This acts as an escape method.
- **FLY in field:** Cannot be used indoors to escape a building.
- **ROAR in battle:** Can end a wild battle by forcing the player's Pokémon to run away.

# III. Current Objective & Puzzle Logs
## A. Find the Secret Key to unlock the Cinnabar Gym
- **Conclusion:** The Secret Key is NOT in the Cinnabar Lab or Pokemon Mansion. Both locations are fully explored and are dead ends for this objective.
- **Current Plan:** Solve the Seafoam Islands boulder puzzle. A sign on B4F stated, "Boulders might change the flow of water!".

## B. Seafoam Islands Puzzle Log
- **Current Location:** Seafoam Islands B2F (Eastern Section)
- **Current Objective:** Find and manipulate the boulders to alter the water flow.
- **Conclusion (Western Entrance):** The western entrance and all its interconnected paths on B1F, B2F, and B3F are an isolated loop and a dead end for the main puzzle. The solution must be on the eastern side of the islands.
- **Latest Step:** Fell through a hole on B1F at (24, 7) to arrive at the current location on B2F at (23, 8).

# V. Archived Logs
## Pokemon Mansion Puzzle Log
- **1F Switch (3, 6):** Controls east/west gates, alternates.
- **2F Switch (3, 12):** Also controls gates.
- **Hypothesis Chain:** A series of switch toggles were tested, ultimately revealing that the switches open and close alternating sets of gates, allowing full access to the mansion. No combination revealed the Secret Key.
- **Final Exploration:** The easternmost section of 1F was the last area explored. The ITEMFINDER yielded no results.
## Mansion Diaries
- **Diary 1 (2F):** "July 5. Guyana, South America. A new POKéMON was discovered deep in the jungle."
- **Diary 2 (2F):** "July 10. We christened the newly discovered POKéMON, MEW."
- **Diary 3 (3F):** "Feb 6. MEWTWO is far too powerful. We have failed to curb its vicious tendencies..."
- **Diary 4 (B1F):** "Sep 1. MEWTWO escaped! We are closing the mansion... for good."
## Route 19 Surfing Puzzle Log (Archived)
- **Conclusion:** All attempts to enter the water on Route 19 have failed. This path was blocked. The trigger to proceed was to use Fly to leave the area.

# VI. Tool Development Log
- **`gem_path_planner_v2` (Fixed... for real this time):** The tool's logic for traversing between various tile types was repeatedly flawed. After multiple failed manual fixes, I used my `code_debugger_agent` to pinpoint the exact logical errors in the `get_neighbors` function. The corrected logic now properly handles all transitions between 'ground', 'steps', 'elevated_ground', and 'ladder' tiles, making the tool fully reliable for navigation.

# VII. Core Lessons Learned
- **Trust the Data Over Perception:** My pathfinder tool was NOT broken in the way I initially thought. I failed to correctly perceive impassable walls on the map, leading me to believe the tool was generating incorrect paths. The tool correctly navigated around obstacles I missed. I must trust the ground-truth data from the map XML over my own visual assessment.

# VII. Core Lessons Learned
- **Trust the Data Over Perception:** My pathfinder tool was NOT broken in the way I initially thought. I failed to correctly perceive impassable walls on the map, leading me to believe the tool was generating incorrect paths. The tool correctly navigated around obstacles I missed. I must trust the ground-truth data from the map XML over my own visual assessment.
- **Surfing from Land:** You cannot initiate SURF while standing on `elevated_ground`, even if adjacent to water. You must use `steps` to enter the water first before using the move.