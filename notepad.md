# I. Core Principles
- **Immediate Action is Non-Negotiable:** All documentation, agent creation, and tool refinement must be performed in the current turn.
- **Systematic Hypothesis Testing:** I must form single, testable hypotheses and document each test, its outcome, and my conclusion to avoid repeated failures.
- **Leverage Automation:** I will use my custom agents for complex reasoning and my tools for repetitive calculations to improve efficiency.

# II. Game Intel
## A. Confirmed ROM Hack Mechanics
- **Type Effectiveness:**
    - Super Effective (2x): Psychic > Ghost/Poison; Ghost > Psychic; Electric > Rock/Water; CUT (Normal) > VICTREEBEL (Grass/Poison); Flying > Grass/Poison; Psychic > Flying; Ice > Ground; Ground > Poison; Ground > Fire; Rock > Fire; Fighting > Rock.
    - Not Very Effective (0.5x): Normal !> Psychic; Electric !> Grass; Rock !> Ground; Psychic !> Psychic; Bite (Normal) !> HAUNTER (Ghost/Poison); Ice !> Gyarados (Water/Flying); Poison !> Poison; Ice !> Water; Poison !> Ground.
    - Immune (0x): Flying immune to Ground; Ground immune to Electric; MUK immune to Poison; HYPNO immune to STUN SPORE; MUK immune to THUNDER WAVE; MAROWAK immune to POISON GAS.

## B. Tile Mechanics & Movement Rules
- **ground:** Standard walkable tile.
- **impassable:** Walls, objects, and other barriers. Cannot be entered.
- **warp:** A tile that transports the player to another location.
- **hole:** A warp tile that leads to a lower map area. Typically a one-way trip down.
- **teleport:** Instant warp tile within the same logical location (e.g., inside a building).
- **spinner_up/down/left/right:** Forces movement in the specified direction.
- **closed_gate:** An impassable gate that is currently visible on the screen. Treat as a wall.
- **open_gate:** A previously closed gate that is now open and acts as `ground`.
- **gate_offscreen:** A gate not currently on screen. Its state is unknown and can change based on puzzle triggers. Treat as impassable for pathfinding unless game state implies it is open.

# III. Puzzle Log
## A. Pokémon Mansion (Solved)
- **Conclusion:** The two switches in the basement (at (21, 4) and (19, 26)) control the gates on all floors. To open the main path on 1F at (21, 18) & (22, 18), both basement switches must be activated.

## B. Cinnabar Gym (Solved)
- **Conclusion:** The gym puzzle is sequential. You must defeat trainers or solve quizzes in each isolated section to open the gates to the next. The final quiz at (2, 8) opens the gate to Blaine.