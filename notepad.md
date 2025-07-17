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

# IX. Pokémon Mansion Puzzle Log (v6 - Final Consolidated)
## B1F
- **System Override:** I was previously hallucinating about being trapped due to misinterpreting game data. The system has confirmed there are 6 reachable unseen tiles in the western corridor, meaning a path MUST exist.
- **Puzzle Elements & State:**
    - Switch: (19,26).
    - Northern Gates [(17,17), (18,17)]: Currently CLOSED.
    - Western Entrance Gates [(10,7), (10,8)]: Currently OPEN.
    - Western Corridor Gates [(14,23), (14,24)]: Visually confirmed CLOSED.
    - Eastern Gates [(27,18), (28,18)]: Visually confirmed CLOSED.
- **Current Hypothesis:** Despite the visual blockage from the Western Corridor gates, there must be a navigable path to the 6 unseen tiles in the western section. My top priority is to explore this guaranteed path and find the Secret Key.