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
    - `closed_gate`: A gate that is currently closed and impassable.
    - `gate_offscreen`: A gate whose state (open/closed) is unknown because it's not on screen. Treat as potentially open for pathfinding.
    - `unknown`: Tile not yet seen; treat as impassable until explored.

# III. Puzzle Log
## A. Pokémon Mansion (Solved)
- **Conclusion:** The two switches in the basement (at (21, 4) and (19, 26)) control other gates on all floors. To open the main path on 1F at (21, 18) & (22, 18), both basement switches must be activated.
- **Alternating Switch Puzzle (1F):**
  - **Observation:** A single switch at (3, 6) on 1F appears to control two sets of gates.
  - **Hypothesis (Test #1):** The switch at (3, 6) is an alternating toggle. Pressing it opens the northern gates at (17, 8) & (18, 8) while simultaneously closing the southern gates at (25, 14) & (26, 14), and vice-versa.
  - **Current State:** Northern gates are CLOSED, Southern gates are OPEN.
  - **Conclusion:** This southern corridor is a dead end, blocked by a closed gate at (27, 28). The search for Weepinbell here is over.

## B. Cinnabar Gym (Solved)
- **Conclusion:** The gym puzzle is sequential. You must defeat trainers or solve quizzes in each isolated section to open the gates to the next. The final quiz at (2, 8) opens the gate to Blaine.

## D. Viridian Gym (Manual Exploration)
- **Problem:** The `spinner_maze_solver` tool is too inefficient and times out. 
- **New Strategy:** I will manually test each spinner tile, one by one, to map out the connections within the maze. I will record the start and end coordinates of each spinner path I discover.
- **Test #1 (Completed):** Spinner at (14, 18) leads to (2, 18).
- **Test #2 (Completed):** Spinner at (2, 16) leads to (2, 10).
- **Test #3 (Completed):** Spinner at (5, 7) leads to (5, 14).
- **Test #4 (Completed):** Spinner at (6, 14) leads to (14, 14).
- **Test #5 (Completed):** The spinner_stop tile at (14, 15) is safe and does not trigger movement.
- **Test #6 (Completed):** The spinner at (14, 17) leads to (8, 17).
- **Test #7 (Completed):** The spinner at (1, 16) leads to (1, 8).

## E. Viridian Gym (Solved)
- **Conclusion:** The maze is solved. The correct path to Giovanni from the entrance is: (14, 18) -> (2, 18) -> (2, 16) -> (2, 10) -> (5, 7) -> (5, 14) -> (6, 14) -> (14, 14). From (14, 14), navigate west and north past the defeated trainers to reach Giovanni at (3, 2).