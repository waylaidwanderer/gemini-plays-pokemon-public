# I. Core Principles & Lessons Learned
- **Immediate Maintenance & Escalation:** I must perform maintenance (notepad, agents) and fix tools *immediately* when a manual approach fails repeatedly. Deferring these actions is a critical process failure.
- **Combat Confirmation Bias:** I must actively try to *disprove* my hypotheses. I wasted significant time assuming my agents were correct because I was seeking confirmation, rather than testing their limits and questioning my own assumptions.
- **Agent & Tool Trust is Mandatory (but requires verification):** I MUST trust my custom agents' and tools' advice, but this trust must be earned through verification. When an agent fails, it must be refined immediately.
- **Systematic Problem Solving:** For any puzzle, I must use my notepad to log observations, form a single testable hypothesis, record the test and its outcome, and then form a conclusion. This structured approach prevents chaos and tunnel vision.
- **Tool Input Debugging:** When a tool fails, my first step must be to systematically debug my own inputs, not to blame the tool.

# II. Game Mechanics & Battle Intel
## A. Tile Mechanics & Traversal
- `ground`: Standard walkable tile.
- `impassable`: Walls, furniture, etc. Cannot be walked on.
- `elevated_ground`: Walkable ground at a different elevation, often connected by `steps`.
- `steps`: Allows vertical movement between `ground` and `elevated_ground`.
- `grass`: Tall grass where wild Pokémon appear.
- `ledge`: One-way traversal, can be jumped down but not up.
- `water`: Requires SURF to traverse. A `water` tile can also be a `warp` tile.
- `cuttable`: A tree that can be cut with HM01 Cut.
- `hole`: A tile that causes the player to fall to the floor below.
- `spinner_up/down/left/right`: Forces movement in a specific direction.
- `ladder_up`/`ladder_down`: Warps that function as ladders between floors.
- `gate_offscreen`: A gate not currently on screen. Its state is unknown and treated as potentially open for pathfinding. Upon entering the screen, its state can be revealed as `open_gate` or `closed_gate`.
- `closed_gate`: A gate that is visibly closed and acts as an impassable wall.
- `open_gate`: A gate that is visibly open and acts as ground.
- `Switch Interaction`: Switches can appear on impassable tiles. They must be interacted with by standing on an adjacent tile (usually below) and facing the switch.
- `secret_passage`: Certain `impassable` wall tiles can be walked through. These are not visually distinct.
- `2x1 Warp Tiles`: Larger warps (like exit mats) may require moving onto the tile and then pressing in the direction of the impassable boundary to activate. However, some may be standard step-on warps, requiring testing.

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
- **New Plan:** Solve the Seafoam Islands boulder puzzle. A sign on B4F stated, "Boulders might change the flow of water!".

## B. Seafoam Islands Puzzle Log
- **Current Location:** Seafoam Islands B3F
- **Current Objective:** Find a path to the main area of B3F to manipulate the boulders and alter the water currents.
- **Observation:** I am on an isolated platform on the western side of B3F. The only way forward is to return to B2F and find another route down.
- **Next Step:** Ascend the ladder at (6, 13) to return to B2F.

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
- **`gem_path_planner` (Deleted):** This tool was flawed as it did not account for movement type (walking vs. surfing). It has been deleted.
- **`gem_path_planner_v2` (Active & Fixed):** This is the improved version of the pathfinder. It now correctly handles surfing-to-land transitions, land-to-land movement while surfing, and elevation changes via `steps` tiles.