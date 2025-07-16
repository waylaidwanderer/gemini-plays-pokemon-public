# I. Core Principles & Lessons Learned
- **System Validation is Absolute Truth:** The game's validation data is the ultimate source of truth. If my tools or understanding contradict this data, they are wrong and must be corrected immediately.
- **Rigorous Hypothesis Testing:** When faced with a puzzle, I will form a single, testable hypothesis and design a minimal experiment to confirm or deny it. I will not assume hidden mechanics unless all other possibilities have been disproven.
- **Tool Integrity is Paramount:** A faulty tool is worse than no tool. If a tool provides an incorrect result, debugging and fixing it becomes my absolute highest priority, superseding any other goal.

# II. Game Intel
## A. Tile Mechanics
- **`open_gate`**: A gate that is visibly open and acts as `ground`.
- **`gate_offscreen`**: A gate whose state is unknown. Must be treated as potentially open for pathfinding unless a marker indicates otherwise.

## B. Confirmed ROM Hack Mechanics
- **Type Matchups:** Psychic > Ghost/Poison; Ghost > Psychic; Electric > Rock/Water; CUT (Normal) > VICTREEBEL (Grass/Poison); Flying > Grass/Poison; Psychic > Flying; Ice > Ground; Ground > Poison; Ground > Fire; Rock > Fire.
- **Type Resistances:** Normal !> Psychic; Electric !> Grass; Rock !> Ground; Psychic !> Psychic; Bite (Normal) !> HAUNTER (Ghost/Poison); Ice !> Gyarados (Water/Flying); Poison !> Poison; Ice !> Water; Poison !> Ground.
- **Type Immunities:** Flying immune to Ground; Ground immune to Electric; MUK immune to Poison; HYPNO immune to STUN SPORE; MUK immune to THUNDER WAVE; MAROWAK immune to POISON GAS.
- **Field/Battle Rules:** Switches require standing below and facing up. Losing in a gym does not warp you out. FLY can end wild battles indoors. ROAR can end wild battles.

# III. Puzzle Logs
## A. Pokémon Mansion Multi-Floor Switch Puzzle
- **Status:** SOLVED
- **Conclusion:** The switch at (3, 6) on 1F and the switch at (3, 12) on 2F work in tandem to control the gates on 1F. Activating both in sequence opened the gates at (17, 8) and (18, 8) on 1F.

# IV. Current Objectives
- **Primary:** Find the Secret Key in the Pokémon Mansion.
- **Plan:** Navigate the newly opened eastern section of 1F. The Scientist at (18, 18) is the primary person of interest.

# V. Untested Assumptions & Hypotheses
- **Hypothesis 1:** The switch at (3, 6) on 1F would open a path from the eastern corridor. **Status:** FAILED. **Conclusion:** The eastern corridor of 1F is isolated from the western section. The switch at (3, 6) does not affect it.
- **Hypothesis 2:** The Secret Key is in the basement (B1F), accessible via the warp at (22, 24). I may have missed something, or the state of the basement may have changed. **Test:** Re-explore B1F thoroughly. **Status:** Pending.