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
- **Current State:** I am trapped on Pokemon Mansion 1F in the eastern section. Gates at (21, 18) & (22, 18) are CLOSED, blocking the path west.
- **Hypothesis (v7):** The puzzle state is controlled by switches on multiple floors. To escape my current predicament, I must return to the basement (B1F) via the warp at (22, 24) and interact with the switches there to change the gate configuration on 1F.
- **Next Step:** Take the warp at (22, 24) to go to Pokemon Mansion B1F.