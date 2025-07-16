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

## B. Confirmed ROM Hack Mechanics
- **Type Matchups:** Psychic > Ghost/Poison; Ghost > Psychic; Electric > Rock/Water; CUT (Normal) > VICTREEBEL (Grass/Poison); Flying > Grass/Poison; Psychic > Flying; Ice > Ground; Ground > Poison; Ground > Fire; Rock > Fire.
- **Type Resistances:** Normal !> Psychic; Electric !> Grass; Rock !> Ground; Psychic !> Psychic; Bite (Normal) !> HAUNTER (Ghost/Poison); Ice !> Gyarados (Water/Flying); Poison !> Poison; Ice !> Water; Poison !> Ground.
- **Type Immunities:** Flying immune to Ground; Ground immune to Electric; MUK immune to Poison; HYPNO immune to STUN SPORE; MUK immune to THUNDER WAVE; MAROWAK immune to POISON GAS.
- **Field/Battle Rules:** Switches require standing below and facing up. Losing in a gym does not warp you out. FLY can end wild battles indoors. ROAR can end wild battles.

# III. Puzzle Logs & Hypotheses
## A. Pokémon Mansion Multi-Floor Switch Puzzle
- **Status:** In Progress
- **Knowns:** There are switches on 1F (3,6) and 2F (3,12). They control multiple sets of gates on 1F.
- **Current Hypothesis:** The state of the 2F switch acts as a 'mode selector' for the 1F switch. The 1F switch will toggle different sets of gates depending on the 2F switch's state.
- **Current State:** 2F switch has been toggled ON. Eastern gates at (17,8) are now closed. Southern gates at (25,14) are also closed.
- **Test Plan (Confirmation):**
    1. Interact with the 1F switch at (3,6) while the 2F switch is ON.
    2. **Expected Outcome:** The southern gates at (25,14) will open.
    3. **Action:** Proceed to the 1F switch now.
- **Test Plan (Falsification):**
    1. If the southern gates open, return to 2F and toggle the switch OFF.
    2. Return to 1F and observe if the southern gates close again.
    3. This will confirm the causal link.