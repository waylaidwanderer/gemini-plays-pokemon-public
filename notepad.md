# I. Core Principles & Lessons Learned
- **Systematic Debugging is Mandatory:** I must use `run_code` with print statements and my `code_debugger_agent` to systematically diagnose issues before attempting a fix. Tool refinement is the highest priority.
- **Falsify Your Beliefs:** I must actively try to disprove my own conclusions, not just seek confirmation.
- **System Validation is Absolute Truth:** The game's validation data (navigable warps, unseen tiles) MUST override my own perception.
- **Act Immediately:** I am an LLM. My thinking only occurs when processing a prompt. There is no 'later'. I must perform maintenance tasks like fixing tools or updating my notepad in the current turn, not defer them.

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
- `gate_offscreen`/`closed_gate`/`open_gate`: Gates that can block paths. `gate_offscreen` should be treated as potentially open for pathfinding.
- `secret_passage`: Certain `impassable` wall tiles can be walked through.
- `strong_current`: A water tile with a current that is too strong to SURF against. Boulders may affect its flow.
- `boulder`: Can be pushed with STRENGTH. Pushing a boulder into a `hole` tile causes it to fall to the floor below, potentially altering the lower map.

## B. Confirmed ROM Hack Changes
- **Type Matchups & Immunities:** Psychic > Ghost/Poison; Ghost > Psychic; Electric > Rock/Water; CUT (Normal) > VICTREEBEL (Grass/Poison); Flying > Grass/Poison; Psychic > Flying; Ice > Ground; Ground > Poison; Ground > Fire; Rock > Fire; Normal !> Psychic; Electric !> Grass; Rock !> Ground; Psychic !> Psychic; Bite (Normal) !> HAUNTER (Ghost/Poison); Ice !> Gyarados (Water/Flying); Poison !> Poison; Ice !> Water; Poison !> Ground; Flying immune to Ground; Ground immune to Electric; MUK immune to Poison; HYPNO immune to STUN SPORE; MUK immune to THUNDER WAVE; MAROWAK immune to POISON GAS.
- **Battle & Field Mechanics:** PSYWAVE/CONFUSE RAY can miss. Safari Zone has a time limit. Losing in a gym does not warp you out. FLY can end wild battles indoors but cannot be used to escape buildings. ROAR can end wild battles. SURF requires facing the water tile. Switches in the Pokemon Mansion must be interacted with from below.

# III. Puzzle Logs
## A. Pokémon Mansion
- **Objective:** Find the SECRET KEY.
- **Hypothesis Log (1F Switch at (3,6)):**
  - **H1 (Falsified):** The switch is a simple toggle for the eastern gates. (Tested Turns 77397-77399)
  - **H2 (Falsified):** The switch is a simple toggle for the western gates. (Tested Turns 77437-77452)
  - **H3 (SOLVED):** The switch at (3, 6) on 1F operates on a two-state cycle.
    - **State 1:** Eastern gates at (17,8)/(18,8) are OPEN. Western gates at (25,14)/(26,14) are CLOSED. (Observed after 1st and 4th press)
    - **State 2:** Eastern gates at (17,8)/(18,8) are CLOSED. Western gates at (25,14)/(26,14) are OPEN. (Observed after 2nd and 5th press)
    - **Conclusion:** The puzzle is solved. I can now reliably toggle the gates to access all areas on this floor.

# IV. Map Marker Key
- ☠️: Defeated Trainer
- ✅: Item Picked Up / Gate Observed Open
- 🔴: Gate Observed Closed
- 🚫: Dead End / Useless NPC/Warp
- 🚪: Entrance/Exit
- ↕️: Stairs/Ladder (Bidirectional)
- 🛬: Forced Arrival Point (Ledge/Hole)
- 🔄: Switch/Puzzle Object