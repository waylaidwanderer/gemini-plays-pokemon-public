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
- **ground:** Standard walkable tile.
- **impassable:** Walls, objects, and other barriers. Cannot be entered.
- **open_gate:** A previously closed gate that is now open and acts as `ground`.
- **closed_gate:** An impassable gate that is currently visible on the screen.
- **gate_offscreen:** A gate (either open or closed) that is not currently visible. Treat as potentially open for pathfinding unless a marker indicates otherwise.
- **warp:** A tile that transports the player to another location.

# IX. Pokémon Mansion Puzzle Log (v10 - Corrected)
## B1F Puzzle Elements & State (Corrected)
- **Switches:**
    - Switch 1: (21,4)
    - Switch 2: (19,26) - This switch toggles gates on multiple floors.
- **Gate Status:**
    - Northern Gates [(17,17), (18,17)]: Currently **CLOSED**.
    - Western Entrance Gates [(10,7), (10,8)]: Currently **CLOSED**.
    - Western Corridor Gates [(14,23), (14,24)]: Currently **OPEN**.
    - Eastern Gates [(27,18), (28,18)]: Currently **OPEN**.
- **Current Hypothesis:** The western corridor contains the Secret Key. The path is now open and I must explore the 6 unseen tiles.