# I. Core Principles & Lessons Learned
- **Immediate Action is Non-Negotiable:** Deferring tasks like tool fixes, agent creation, or documentation is a critical failure. All such actions must be performed in the current turn.
- **Systematic Hypothesis Testing:** When faced with a puzzle, I must form single, testable hypotheses and design minimal experiments. I will document each test, its outcome, and my conclusion to avoid repeated failures.
- **Trust Data Over Perception:** I must treat the 'Reachable Unseen Tiles' list from the Game State Information as the absolute source of truth. My visual perception can be flawed by off-screen changes. If the system says a tile is reachable, a path exists, and I must find it.

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
- **closed_gate:** An impassable gate that is currently visible on the screen.
- **gate_offscreen:** A gate (either open or closed) that is not currently visible. Treat as potentially open for pathfinding.
- **teleport:** Instant warp tile within the same logical location (e.g., inside a building).
- **spinner_up/down/left/right:** Forces movement in the specified direction.

# III. Pokémon Mansion Puzzle Log
- **Observation 1:** Moved near (27, 18), observed eastern gates at (27,18) and (28,18) open.
- **Observation 2:** Moved near (18, 17), observed northern gates at (18,17) and (17,17) close.
- **Observation 3:** Moved near (10, 7), observed western gates at (10,7) and (10,8) close.
- **Observation 4:** Moved near (14, 23), observed western gates at (14,23) and (14,24) open.
- **Observation 5:** Pressed switch at (19, 26). Moved towards (14, 23). Observed western gates at (14,23) and (14,24) close, blocking the path.
- **Conclusion:** The puzzle is controlled by proximity triggers, and the switches modify the behavior of those triggers (e.g., from 'open on approach' to 'close on approach'). The switches appear to be toggles.

# IV. Tool & Agent Ideas
- **Exploration Path Planner Tool:** A computational tool to solve the Traveling Salesperson Problem for a list of coordinates, finding the shortest path to visit all of them. This should be a high priority to create.
- **Long-Term Training Advisor Agent:** An agent to analyze my full roster and suggest long-term training priorities for upcoming major challenges like the Elite Four.