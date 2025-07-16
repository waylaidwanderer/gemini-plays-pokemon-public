# I. Meta-Reflection & Strategy Pivot
- **Core Failure:** I deferred fixing a critical tool (`pathfinder`) instead of addressing it immediately, violating the core principle of maintaining a perfect internal state. This led to a prolonged, unproductive loop.
- **Goal Discipline:** My goals must be *outcomes* (e.g., 'Obtain the Secret Key'), not *methods* (e.g., 'Fix the tool'). Fixing tools is an immediate, non-negotiable action, not a deferred goal.
- **Renewed Approach:** I will adhere to a strict, incremental debugging process and prioritize tool integrity above all else. I will not use a tool I know to be broken.

# II. Core Principles & Lessons Learned
- **System Validation is Absolute Truth:** The game's validation data is the ultimate source of truth. If my tools or understanding contradict this data, they are wrong and must be corrected immediately.
- **Rigorous Hypothesis Testing:** When faced with a puzzle, I will form a single, testable hypothesis and design a minimal experiment to confirm or deny it. I will not assume hidden mechanics unless all other possibilities have been disproven.
- **Tool Integrity is Paramount:** A faulty tool is worse than no tool. If a tool provides an incorrect result, debugging and fixing it becomes my absolute highest priority, superseding any other goal.
- **Immediate Documentation:** All discoveries, plans, and state changes must be documented *immediately* in the notepad or with map markers to avoid hallucinations and redundant actions.

# III. Game Intel
## A. Tile Mechanics
- `ground`: Walkable tile.
- `impassable`: Walls, counters, etc. Cannot be entered.
- `warp`: Teleports the player to a new location.
- `open_gate`: A gate that is visibly open and acts as `ground`.
- `closed_gate`: A gate that is visibly closed and acts as `impassable`.
- `gate_offscreen`: A gate whose state is unknown. Must be treated as potentially open for pathfinding unless a marker indicates otherwise.
- `ledge`: Can be jumped down, but not climbed up. Acts as ground when approached from above (Y-1), but as a wall from all other directions.
- `hole`: Warps the player to a lower floor, usually into an isolated area.

## B. Confirmed ROM Hack Mechanics
- **Type Matchups:** Psychic > Ghost/Poison; Ghost > Psychic; Electric > Rock/Water; CUT (Normal) > VICTREEBEL (Grass/Poison); Flying > Grass/Poison; Psychic > Flying; Ice > Ground; Ground > Poison; Ground > Fire; Rock > Fire.
- **Type Resistances:** Normal !> Psychic; Electric !> Grass; Rock !> Ground; Psychic !> Psychic; Bite (Normal) !> HAUNTER (Ghost/Poison); Ice !> Gyarados (Water/Flying); Poison !> Poison; Ice !> Water; Poison !> Ground.
- **Type Immunities:** Flying immune to Ground; Ground immune to Electric; MUK immune to Poison; HYPNO immune to STUN SPORE; MUK immune to THUNDER WAVE; MAROWAK immune to POISON GAS.
- **Field/Battle Rules:** Switches require standing below and facing up. Losing in a gym does not warp you out. FLY can end wild battles indoors. ROAR can end wild battles.

# IV. Pathfinder Tool Debugging Log (V2 - Incremental)
- **Hypothesis:** The `pathfinder` tool is failing due to a silent crash in the script.
- **Plan:** Rebuild the tool incrementally, testing one code block at a time.
- **Test 1:** Minimal execution (`print` statement only).
- **Test 2:** Add variable parsing (`target_x`, `map_width`, etc.).
- **Test 3:** Add player position finding loop.
- **Test 4:** Add grid initialization (`grid = [[...]]`).
- **Test 5:** Add grid population loop (simplified).
- **Test 6:** Add A* data structure initialization.
- **Test 7:** Add A* search loop (simplified grid).
- **Conclusion:** The silent crash hypothesis is definitively false. The tool executes fully but fails to find a path. The problem lies in the logic of the grid population or the A* search's interaction with it.
- **Next Step (Final Test):** Re-run the fully assembled script. The methodical tests have proven every individual component is syntactically correct and doesn't cause a crash. The failure is logical, not structural.