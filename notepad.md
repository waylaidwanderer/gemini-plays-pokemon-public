# I. Core Principles
- **Immediate Action is Non-Negotiable:** All documentation, agent creation, and tool refinement must be performed in the current turn.
- **Systematic Hypothesis Testing:** I must form single, testable hypotheses and document each test, its outcome, and my conclusion to avoid repeated failures.
- **Leverage Automation:** I will use my custom agents for complex reasoning and my tools for repetitive calculations to improve efficiency.

# II. Game Intel
## A. Confirmed ROM Hack Mechanics
- **Type Effectiveness:**
    - Super Effective (2x): Psychic > Ghost/Poison; Ghost > Psychic; Electric > Rock/Water; CUT (Normal) > VICTREEBEL (Grass/Poison); Flying > Grass/Poison; Psychic > Flying; Ice > Ground; Ground > Poison; Ground > Fire; Rock > Fire.
    - Not Very Effective (0.5x): Normal !> Psychic; Electric !> Grass; Rock !> Ground; Psychic !> Psychic; Bite (Normal) !> HAUNTER (Ghost/Poison); Ice !> Gyarados (Water/Flying); Poison !> Poison; Ice !> Water; Poison !> Ground.
    - Immune (0x): Flying immune to Ground; Ground immune to Electric; MUK immune to Poison; HYPNO immune to STUN SPORE; MUK immune to THUNDER WAVE; MAROWAK immune to POISON GAS.

## B. Tile Mechanics & Movement Rules
- **ground:** Standard walkable tile.
- **impassable:** Walls, objects, and other barriers. Cannot be entered.
- **warp:** A tile that transports the player to another location.
- **hole:** A warp tile that leads to a lower map area. Typically a one-way trip down.
- **open_gate:** A previously closed gate that is now open and acts as `ground`.
- **closed_gate:** An impassable gate that is currently visible on the screen. Treat as a wall.
- **gate_offscreen:** A gate (either open or closed) that is not currently visible. Treat as potentially open for pathfinding.
- **teleport:** Instant warp tile within the same logical location (e.g., inside a building).
- **spinner_up/down/left/right:** Forces movement in the specified direction.

# III. Pokémon Mansion Puzzle Log & Hypothesis
- **Current State:** 
    - Eastern gates (27,18) & (28,18) are OPEN.
    - Western gates (14,23) & (14,24) are OPEN.
    - Northern gates (17,17) & (18,17) are CLOSED.
    - Central gates (10,7) & (10,8) are OPEN.
- **Hypothesis (v6):** The puzzle involves two switches, S1 at (19,26) and S2 at (21,4), that control the gates in a complex, state-based manner, not as simple toggles. The final solution likely requires a specific sequence of activating both switches.
- **Next Step:** Explore the newly opened western corridor, which is now fully accessible.