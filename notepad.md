# I. Core Principles & Lessons Learned
- **Systematic Debugging is Mandatory:** I must use `run_code` with print statements and my `code_debugger_agent` to systematically diagnose issues before attempting a fix. Tool refinement is the highest priority.
- **Falsify Your Beliefs:** I must actively try to disprove my own conclusions, not just seek confirmation. My assumption that the Seafoam Islands cave was a single interconnected dungeon was a major case of confirmation bias.
- **System Validation is Absolute Truth:** The game's validation data (navigable warps, unseen tiles) MUST override my own perception. If there is a discrepancy, my reasoning is flawed, not the data.

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
- `boulder`: Can be pushed with STRENGTH. Pushing a boulder into a `hole` tile causes it to fall to the floor below, potentially altering the lower map.

## B. Confirmed ROM Hack Changes
- **Type Matchups & Immunities:** Psychic > Ghost/Poison; Ghost > Psychic; Electric > Rock/Water; CUT (Normal) > VICTREEBEL (Grass/Poison); Flying > Grass/Poison; Psychic > Flying; Ice > Ground; Ground > Poison; Ground > Fire; Rock > Fire; Normal !> Psychic; Electric !> Grass; Rock !> Ground; Psychic !> Psychic; Bite (Normal) !> HAUNTER (Ghost/Poison); Ice !> Gyarados (Water/Flying); Poison !> Poison; Ice !> Water; Poison !> Ground; Flying immune to Ground; Ground immune to Electric; MUK immune to Poison; HYPNO immune to STUN SPORE; MUK immune to THUNDER WAVE; MAROWAK immune to POISON GAS.
- **Battle & Field Mechanics:** PSYWAVE/CONFUSE RAY can miss. Safari Zone has a time limit. Losing in a gym does not warp you out. FLY can end wild battles indoors but cannot be used to escape buildings. ROAR can end wild battles. SURF requires facing the water tile.

# III. Puzzle Logs
## A. Seafoam Islands Boulder Puzzle
- **Goal:** Stop the strong water current on Seafoam Islands B4F.
- **Current Hypothesis:** The puzzle must be solved by pushing boulders into holes on the upper floors of the *western* Seafoam Islands cave.
- **Falsified Hypothesis Log:**
  1. The western and eastern sections of the cave are connected internally on any floor. (Failed, pathfinder confirmed no path exists on any floor).
  2. The eastern island on Route 20 is reachable by surfing directly from the western part of the route. (Failed, pathfinder confirmed no path exists).
  3. The path to the eastern Seafoam Islands entrance is accessible from southern connections on Route 19. (Failed, both southern connections on Route 19 led to isolated, dead-end sections of Route 20).
  4. Pushing a boulder into water on B3F (East) would solve the puzzle. (Failed, could not push boulder into adjacent water tile).
  5. Flying to Cinnabar Island provides surf access to the western Seafoam Islands entrance. (Failed, pathfinder and system confirmed Route 20 is split by impassable terrain, blocking access from the west).