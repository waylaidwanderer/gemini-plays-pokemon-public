# I. Meta-Reflection & Strategy Pivot
- **Core Failure:** I deferred fixing a critical tool (`pathfinder`) instead of addressing it immediately, violating the core principle of maintaining a perfect internal state.
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

# III. Pokémon Mansion Puzzle Log
- **Current Goal:** Find the Secret Key.
- **Key Discoveries:**
    - The mansion contains a multi-floor switch puzzle. The state of gates depends on the sequence and location of switch activations.
    - The warps on 2F at (8,11) and (7,2) both lead back to 1F, not to 3F.
    - Interacting with the Super Nerd at (4,18) on 2F caused him to vanish and me to swap positions with him. This appears to have been a necessary trigger for the puzzle.
- **Hypothesis 1 (Active):** The order of switch activations is the key to solving the puzzle. Activating the 1F switch *before* the 2F switch will produce a different outcome.
- **Test 1 Plan:**
    1. (COMPLETE) Activate the switch at (3,6) on 1F. This action closed the eastern gates at (17,8) and (18,8).
    2. (NEXT) Travel to 2F via the warp at (6,11).
    3. Activate the switch at (3,12) on 2F.
    4. Observe any changes to the gates on 2F, specifically the ones at (10,5) and (10,6).
    2. (NEXT) Travel to 2F via the warp at (6,11).
    3. Activate the switch at (3,12) on 2F.
    4. Observe any changes to the gates on 2F, specifically the ones at (10,5) and (10,6).