# I. Core Principles & Lessons Learned
- **System Validation is Absolute Truth:** The game's validation data is the ultimate source of truth. If my tools or understanding contradict this data, they are wrong and must be corrected immediately.
- **Rigorous Hypothesis Testing:** When faced with a puzzle, I will form a single, testable hypothesis and design a minimal experiment to confirm or deny it. I will not assume hidden mechanics unless all other possibilities have been disproven.
- **Tool Integrity is Paramount:** A faulty tool is worse than no tool. If a tool provides an incorrect result, debugging and fixing it becomes my absolute highest priority, superseding any other goal.
- **Immediate Documentation:** All discoveries, plans, and state changes must be documented *immediately* in the notepad or with map markers to avoid hallucinations and redundant actions.

# II. Game Intel
## A. Tile Mechanics
- `ground`: Walkable tile.
- `impassable`: Walls, counters, etc. Cannot be entered.
- `warp`: Teleports the player to a new location.
- `open_gate`: A gate that is visibly open and acts as `ground`.
- `closed_gate`: A gate that is visibly closed and acts as `impassable`.
- `gate_offscreen`: A gate whose state is unknown. Must be treated as potentially open for pathfinding unless a marker indicates otherwise.
- **Switches**: Must be activated by standing on the tile directly below them, facing up, and pressing A.
- `ledge`: Can be jumped down, but not climbed up. Acts as ground when approached from above (Y-1), but as a wall from all other directions.
- `hole`: Warps the player to a lower floor, usually into an isolated area.

## B. Confirmed ROM Hack Mechanics
- **Type Matchups:** Psychic > Ghost/Poison; Ghost > Psychic; Electric > Rock/Water; CUT (Normal) > VICTREEBEL (Grass/Poison); Flying > Grass/Poison; Psychic > Flying; Ice > Ground; Ground > Poison; Ground > Fire; Rock > Fire.
- **Type Resistances:** Normal !> Psychic; Electric !> Grass; Rock !> Ground; Psychic !> Psychic; Bite (Normal) !> HAUNTER (Ghost/Poison); Ice !> Gyarados (Water/Flying); Poison !> Poison; Ice !> Water; Poison !> Ground.
- **Type Immunities:** Flying immune to Ground; Ground immune to Electric; MUK immune to Poison; HYPNO immune to STUN SPORE; MUK immune to THUNDER WAVE; MAROWAK immune to POISON GAS.
- **Field/Battle Rules:** Switches require standing below and facing up. Losing in a gym does not warp you out. FLY can end wild battles indoors. ROAR can end wild battles.

# III. Tool Debugging Logs
## A. Pathfinder Tool
- **Status:** Critical Failure - Silent execution failure.
- **Symptom:** The tool produces no output, even with debug print statements. This suggests a silent crash or termination by the execution environment.
- **New Strategy: Incremental Re-Integration**
- The previous multi-step testing plan failed to isolate the issue. I will now adopt a more granular approach, adding back code one block at a time until the silent failure reoccurs.
- **Test 1 (New):** Minimal execution test. Redefine the tool with only `print('Start')` and `print('End')`. This will confirm if the tool can execute at all. [PENDING]
- **Test 2 (New):** Add back the initial `try...except` block for variable parsing. [PENDING]
- **Test 3 (New):** Add back the player position finding loop. [SUCCESS]
- **Test 4 (New):** Add back the grid initialization. [SUCCESS]
- **Test 5 (New):** Add back the grid population loop. [SUCCESS]
- **Test 6 (New):** Add back the A* initialization. [PENDING]
- **Test 7 (New):** Add back the A* search loop. [PENDING]