# I. Core Principles & Lessons Learned
- **Trust the Data & Your Tools:** I must trust the game's data and the output of my verified tools over my own flawed perception. My failure to trust `gem_path_planner_v4`'s complex but correct path led to a significant waste of time trying to manually navigate, which was impossible. When a tool gives an unexpected result, the first step is to analyze *why* it might be correct, not to assume it's broken.
- **Immediate Maintenance is Mandatory:** I must perform maintenance (notepad, agents) and fix tools *immediately*. Deferring these actions is a critical process failure. My delay in fixing the pathfinder was a major error.
- **Systematic Problem Solving:** For any puzzle, I must use my notepad to log observations, form a single testable hypothesis, record the test and its outcome, and then form a conclusion. This structured approach prevents chaos and tunnel vision.
- **Falsify Your Beliefs:** To avoid confirmation bias, I must actively try to disprove my own conclusions with alternative tests after an initial hypothesis is confirmed.

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
- **Current Plan:** Navigate the Seafoam Islands. The path seems to involve a series of boulder puzzles.
- **Seafoam Islands Puzzle Log:**
  - **B4F Water Current:** The boulders dropped from upper floors did NOT stop the strong water current at (21,17). The direct path south is blocked.
  - **Current Situation:** My pathfinding tool, `gem_path_planner_v5`, was bugged and could not find paths from water to land via `steps` tiles, making me believe I was trapped. I have since created `gem_path_planner_v6` to fix this.
  - **New Hypothesis:** With the fixed `gem_path_planner_v6`, I should be able to reach the western platform of B4F by surfing to the steps at (8, 4). The ladder on that platform at (12, 8) is the correct way forward.

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

## C. Confirmation Bias & The Route 20 Fiasco
- **Critical Failure:** I hallucinated that Route 20 was split into two impassable sections. I saw a rock wall and concluded it was a total barrier, leading to a massive, time-wasting detour back and forth between Cinnabar and Fuchsia City.
- **Core Lesson:** I MUST trust the game data (i.e., the system warnings that the area was not a dead end) over my own flawed perception. When the system flags an error in my reasoning, I must immediately halt my current plan and re-evaluate my assumptions from the ground up.
- **Water/Ground Traversal:** It is possible to move directly from a `water` tile to an adjacent `ground` tile (and vice-versa) while surfing. This is a key traversal mechanic not previously understood.
## Seafoam Islands Puzzle Log (West)

- **Action:** I am using my `code_debugger_agent` to diagnose the issue and will immediately use `define_tool` to deploy a fix. Deferring this critical maintenance is a process failure.