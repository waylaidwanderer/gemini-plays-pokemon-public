# I. Core Principles
- **Immediate Action is Non-Negotiable:** All documentation, agent creation, and tool refinement must be performed in the current turn.
- **Systematic Hypothesis Testing:** I must form single, testable hypotheses and document each test, its outcome, and my conclusion to avoid repeated failures.
- **Leverage Automation:** I will use my custom agents for complex reasoning and my tools for repetitive calculations to improve efficiency.

# II. Game Intel
## A. Confirmed ROM Hack Mechanics
- **Type Effectiveness:**
    - Super Effective (2x): Psychic > Ghost/Poison; Ghost > Psychic; Electric > Rock/Water; CUT (Normal) > VICTREEBEL (Grass/Poison); Flying > Grass/Poison; Psychic > Flying; Ice > Ground; Ground > Poison; Ground > Fire; Rock > Fire; Fighting > Rock; Flying > Fighting; Water > Fire.
    - Not Very Effective (0.5x): Normal !> Psychic; Electric !> Grass; Rock !> Ground; Psychic !> Psychic; Bite (Normal) !> HAUNTER (Ghost/Poison); Ice !> Gyarados (Water/Flying); Poison !> Poison; Ice !> Water; Poison !> Ground; Normal !> Rock.
    - Immune (0x): Flying immune to Ground; Ground immune to Electric; MUK immune to Poison; HYPNO immune to STUN SPORE; MUK immune to THUNDER WAVE; MAROWAK immune to POISON GAS.
- **Tile Mechanics:**
    - `ground`: Walkable.
    - `impassable`: Cannot be walked on.
    - `grass`: Walkable, triggers wild encounters.
    - `warp`: Teleports player to another location.
    - `spinner`: Forces movement in a specific direction.
    - `ledge`: Can be jumped down (one-way).
    - `cuttable`: Tree that can be cut with HM Cut.
    - `water`: Crossable using HM Surf.
    - `unknown`: Tile not yet seen.

# III. Puzzle Log
## A. Pokémon Mansion (Solved)
- **Conclusion:** The mansion contains multiple switch-based puzzles. The switch at (3, 6) on 1F toggles the gates at (17, 8) and (18, 8). The two switches in the basement (at (21, 4) and (19, 26)) control other gates on all floors. To open the main path on 1F at (21, 18) & (22, 18), both basement switches must be activated.

## B. Cinnabar Gym (Solved)
- **Conclusion:** The gym puzzle is sequential. You must defeat trainers or solve quizzes in each isolated section to open the gates to the next. The final quiz at (2, 8) opens the gate to Blaine.

## C. Viridian Gym (In Progress)
- **Goal:** Navigate the spinner maze to reach the Gym Leader.
- **Strategy:** Use the `spinner_maze_solver` custom tool to find the optimal path.
        - `gate_offscreen`: A gate whose state (open/closed) is unknown because it's not on screen. Treat as potentially open for pathfinding.