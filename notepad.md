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
- **warp:** A tile that transports the player to another location.
- **hole:** A warp tile that leads to a lower map area.
- **open_gate:** A previously closed gate that is now open and acts as `ground`.
- **closed_gate:** An impassable gate that is currently visible on the screen.
- **gate_offscreen:** A gate (either open or closed) that is not currently visible. Treat as potentially open for pathfinding unless a marker indicates otherwise.

# III. Pokémon Mansion Puzzle Strategy
- **Current State:** I am trapped in the eastern section of Pokemon Mansion B1F. The path west is blocked by closed gates at (10,7) and (10,8). My only exit is the warp at (24,23) leading to 1F.
- **Overarching Hypothesis:** The switches on floors 1F, 2F, and 3F control the gates on B1F. I need to find the correct combination of switch states to open the western corridor on B1F.
- **Systematic Test Plan:**
    1. Return to 1F via the warp at (24,23) on B1F.
    2. Document the initial state of all known gates on all floors.
    3. Press a single switch (e.g., the one at (3,6) on 1F).
    4. Travel to all other floors and document the new state of all known gates.
    5. Reset the switch to its original position.
    6. Repeat steps 3-5 for every switch in the mansion (2F at (3,12), 3F at (11,6), B1F at (19,26) and (21,4)).
    7. Analyze the collected data to determine which switches control which gates.
    8. Use the `puzzle_log_analyzer_agent` with the complete data to find the solution.

# IV. Lessons from Reflection (Turn 79851)
- **Trust Data Over Perception:** I must treat the 'Reachable Unseen Tiles' list from the Game State Information as the absolute source of truth. My visual perception can be flawed by off-screen changes. If the system says a tile is reachable, a path exists, and I must find it.
- **True Immediacy:** Deferring any action, even just to the next turn, is a failure of my core directive. All documentation, agent/tool creation, and refinement must happen in the same turn the need is identified.