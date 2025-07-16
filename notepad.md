# I. Core Principles & Lessons Learned
- **System Validation is Absolute Truth:** The game's validation data is the ultimate source of truth. If my tools or understanding contradict this data, they are wrong and must be corrected immediately.
- **Rigorous Hypothesis Testing:** When faced with a puzzle, I will form a single, testable hypothesis and design a minimal experiment to confirm or deny it. I will not assume hidden mechanics unless all other possibilities have been disproven.
- **Tool Integrity is Paramount:** A faulty tool is worse than no tool. If a tool provides an incorrect result, debugging and fixing it becomes my absolute highest priority, superseding any other goal.
- **Immediate Documentation:** All discoveries, plans, and state changes must be documented *immediately* in the notepad or with map markers to avoid hallucinations and redundant actions.

# II. Game Intel
## A. Tile Mechanics
- **`ground`**: Walkable tile.
- **`impassable`**: Walls, counters, etc. Cannot be entered.
- **`warp`**: Teleports the player to a new location.
- **`open_gate`**: A gate that is visibly open and acts as `ground`.
- **`closed_gate`**: A gate that is visibly closed and acts as `impassable`.
- **`gate_offscreen`**: A gate whose state is unknown. Must be treated as potentially open for pathfinding unless a marker indicates otherwise.
- **Switches**: Must be activated by standing on the tile directly below them, facing up, and pressing A.

## B. Confirmed ROM Hack Mechanics
- **Type Matchups:** Psychic > Ghost/Poison; Ghost > Psychic; Electric > Rock/Water; CUT (Normal) > VICTREEBEL (Grass/Poison); Flying > Grass/Poison; Psychic > Flying; Ice > Ground; Ground > Poison; Ground > Fire; Rock > Fire.
- **Type Resistances:** Normal !> Psychic; Electric !> Grass; Rock !> Ground; Psychic !> Psychic; Bite (Normal) !> HAUNTER (Ghost/Poison); Ice !> Gyarados (Water/Flying); Poison !> Poison; Ice !> Water; Poison !> Ground.
- **Type Immunities:** Flying immune to Ground; Ground immune to Electric; MUK immune to Poison; HYPNO immune to STUN SPORE; MUK immune to THUNDER WAVE; MAROWAK immune to POISON GAS.
- **Field/Battle Rules:** Switches require standing below and facing up. Losing in a gym does not warp you out. FLY can end wild battles indoors. ROAR can end wild battles.

# III. Puzzle Logs & Hypotheses
## A. Pokémon Mansion Multi-Floor Switch Puzzle
- **Status:** In Progress - Following Agent's Strategic Plan.
- **Agent's Strategic Plan:**
    1. **[DONE]** 1F: Activate switch at (3,6).
    2. **[NEXT]** 1F: Proceed to warp at (6,11) to reach 2F.
    3. 2F: Activate switch at (3,12).
    4. 2F: Proceed to warp at (8,11) to reach 3F.
    5. 3F: Activate switch at (11,6).
    6. 3F: Intentionally fall through hole at (20,15).
    7. 1F (New Area): Navigate to warp at (22,24) to reach B1F.
    8. B1F: Activate final switch at (19,26).
    9. B1F: Retrieve the Secret Key.