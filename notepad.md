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

# III. Pokémon Mansion Puzzle Strategy
## A. Puzzle Observation Log
- **Observation 1:** Moved near (27, 18), observed eastern gates at (27,18) and (28,18) open.
- **Observation 2:** Moved near (18, 17), observed northern gates at (18,17) and (17,17) close.
- **Observation 3:** Moved near (10, 7), observed western gates at (10,7) and (10,8) close.
- **Observation 4:** Moved near (14, 23), observed western gates at (14,23) and (14,24) open.

## B. Agent Analysis & New Hypothesis
- **Agent Deduction:** The puzzle is controlled by proximity triggers, not switches. Moving to a specific coordinate opens or closes a pair of gates.
- **Hypothesis (Attempt 4):** The switches at (19, 26) and (21, 4) modify the behavior of the proximity-based gate triggers.
- **Test Plan:**
    1. Navigate to the switch at (19, 26) and activate it.
    2. Return to a known proximity trigger, such as (14, 23).
    3. Observe if the trigger's behavior has changed (e.g., does it still open the gates, or does it do nothing/something else?).
    4. Record the outcome in the observation log.

# IV. Tool & Agent Ideas
- **Exploration Agent:** An agent to suggest an optimal path for exploring all `Reachable Unseen Tiles`.
- **Exploration Path Planner Tool:** A computational tool to solve the Traveling Salesperson Problem for a list of coordinates, finding the shortest path to visit all of them.