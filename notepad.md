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
- **Switch Interaction:** Switches must be activated by standing on the tile directly BELOW them (e.g., at (X, Y+1) for a switch at (X,Y)), facing UP, and then pressing A.
- **gate_offscreen:** The state of these gates can change based on switch presses on any floor. Their state is only revealed when they come on-screen.

# III. Pokémon Mansion Puzzle Log
- **Current Goal:** Find the Secret Key.
- **Critical Lesson:** System warnings (e.g., 'not a dead end') are absolute truth, even if they contradict map data or pathfinding. This implies hidden passages or misleading tile types exist. I must trust the system over my own interpretation.

# V. Pokémon Mansion Event Log (Consolidated - NEW)
- **3F:** Pressed switch at (11,6). This is a toggle.
- **B1F:** Gates at (27,18) and (28,18) are now CLOSED, trapping me in the eastern section.

# V. Pokémon Mansion Event Log (Consolidated - NEW)
- **3F:** Pressed switch at (11,6). This is a toggle.
- **1F:** Toggling 3F switch opened gates at (16,12) and (21,18).
- **B1F:** Arrived from 1F warp (22,24 -> 24,23).
- **B1F:** Pressed switch at (19,26). This is a toggle.
- **B1F:** Gates at (17,17) and (18,17) are now OPEN.
- **B1F:** Gates at (14,23) and (14,24) are now CLOSED.
- **1F:** Gates at (21,18) and (22,18) are now OPEN.
- **1F:** Gates at (25,14) and (26,14) are now CLOSED.
- **B1F:** Gates at (27,18) and (28,18) are now CLOSED, trapping me in the eastern section.