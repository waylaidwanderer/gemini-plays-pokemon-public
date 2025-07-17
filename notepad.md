# I. Core Principles & Lessons Learned
- **Immediate Action is Non-Negotiable:** Deferring tasks like tool fixes, agent creation, or documentation is a critical failure. All such actions must be performed in the current turn.
- **Systematic Hypothesis Testing:** When faced with a puzzle, I must form single, testable hypotheses and design minimal experiments. I will document each test, its outcome, and my conclusion to avoid repeated failures.
- **Trust But Verify Agents:** Agents provide powerful plans, but they may lack complete information. Follow their plans, but be prepared to pivot and gather more data when a plan fails.

# II. Game Intel
## A. Confirmed ROM Hack Mechanics
- **Type Effectiveness:**
    - Super Effective (2x): Psychic > Ghost/Poison; Ghost > Psychic; Electric > Rock/Water; CUT (Normal) > VICTREEBEL (Grass/Poison); Flying > Grass/Poison; Psychic > Flying; Ice > Ground; Ground > Poison; Ground > Fire; Rock > Fire.
    - Not Very Effective (0.5x): Normal !> Psychic; Electric !> Grass; Rock !> Ground; Psychic !> Psychic; Bite (Normal) !> HAUNTER (Ghost/Poison); Ice !> Gyarados (Water/Flying); Poison !> Poison; Ice !> Water; Poison !> Ground.
    - Immune (0x): Flying immune to Ground; Ground immune to Electric; MUK immune to Poison; HYPNO immune to STUN SPORE; MUK immune to THUNDER WAVE; MAROWAK immune to POISON GAS.

## B. Tile Mechanics & Movement Rules
- **open_gate:** A previously closed gate that is now open and acts as `ground`.
- **closed_gate:** An impassable gate that is currently visible on the screen.
- **gate_offscreen:** A gate (either open or closed) that is not currently visible. Treat as potentially open for pathfinding.

# VIII. Pokémon Mansion Puzzle Log (Current)
## B1F
- **Map Layout:** B1F is divided into at least three sections: a western corridor, a central area, and an eastern area.
- **Puzzle Elements:**
    - Switch at (19,26).
    - Gates at (17,17) & (18,17) (Northern).
    - Gates at (10,7) & (10,8) (Western Entrance).
    - Gates at (14,23) & (14,24) (Western Corridor).
    - Gates at (27,18) & (28,18) (Eastern).
- **Puzzle Logic & History (Consolidated):**
    - The switch at (19,26) is a cyclical switch affecting multiple gate sets.
    - **State 1 (Initial):** All gates closed.
    - **State 2 (After 1st press):** Northern gates opened. Path was explored and confirmed to be a dead end.
    - **State 3 (After 2nd press):** Northern gates close. Western Entrance gates open, but Western Corridor gates are closed, blocking the path.
- **Current Situation & System Override:** My previous belief that the western corridor was reachable was a hallucination caused by the system's optimistic pathing for off-screen gates. I have now visually confirmed all exits from the central area are blocked by closed gates. I am trapped.
- **Current Hypothesis:** The switch at (19,26) is a cyclical switch. Pressing it a third time is the only logical action and will hopefully change the gate configuration to open a new path, likely the Eastern gates.