# I. Core Principles & Lessons Learned
- **Trust the Data:** I must trust my verified conclusions documented in the notepad and the output of my tools/agents over my own perception. My failure to trust my conclusion that the western Seafoam Islands was a dead end led to a significant waste of time.
- **Immediate Maintenance is Mandatory:** I must perform maintenance (notepad, agents) and fix tools *immediately*. Deferring these actions is a critical process failure for an LLM.
- **Systematic Problem Solving:** For any puzzle, I must use my notepad to log observations, form a single testable hypothesis, record the test and its outcome, and then form a conclusion. This structured approach prevents chaos and tunnel vision.

# II. Game Mechanics & Battle Intel
## A. Tile Mechanics & Traversal
- `ground`: Standard walkable tile.
- `impassable`: Walls, furniture, etc. Cannot be walked on.
- `elevated_ground`: Walkable ground at a different elevation. Traversal to/from `ground` requires `steps`. Cannot initiate SURF from here.
- `steps`: Allows vertical movement between `ground` and `elevated_ground`. To begin surfing from `steps` adjacent to water, the SURF move must be used from the party menu.
- `grass`: Tall grass where wild Pokémon appear.
- `ledge`: One-way traversal, can be jumped down but not up.
- `water`: Requires SURF to traverse.
- `cuttable`: A tree that can be cut with HM01 Cut.
- `hole`: A tile that causes the player to fall to the floor below.
- `spinner_up/down/left/right`: Forces movement in a specific direction.
- `ladder_up`/`ladder_down`: Warps that function as ladders between floors.
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
- **Current Plan:** Solve the Seafoam Islands boulder puzzle, as a sign on B4F stated, "Boulders might change the flow of water!".

## B. Seafoam Islands Puzzle Log
- **Current Location:** Route 19, heading towards the eastern entrance of Seafoam Islands.
- **Hypothesis:** The main boulder puzzle is located within the eastern section of the Seafoam Islands, which must be accessed by traveling from Fuchsia City south to Route 19, and then west to Route 20.
- **Conclusion (Western Entrance):** The western entrance of Seafoam Islands is a navigational dead end for reaching the eastern side of the islands. The two sections of Route 20 are separated by impassable rock formations.

# IV. Archived Logs
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