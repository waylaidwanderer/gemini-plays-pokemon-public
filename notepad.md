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
- **puzzle_switch:** An interactable object that changes the state of other elements on the map, usually gates.
- **open_gate:** A previously closed gate that is now open and acts as `ground`.
- **closed_gate:** An impassable gate that is currently visible on the screen.
- **gate_offscreen:** A gate (either open or closed) that is not currently visible. Treat as potentially open for pathfinding unless a marker indicates otherwise.

# III. Pokémon Mansion Puzzle Strategy
- **Failed Hypothesis (Attempt 2):** I incorrectly assumed the western gates at (10,7) and (10,8) opened on their own. This was proven false when they closed in front of me. I am now blocked.
- **Revised Hypothesis (Attempt 3):** I am returning to my original theory. The switch at (19,26) is the most likely candidate to control the western gates. My next action is to test this switch.
- **Systematic Test Plan:**
    1. Navigate to the switch at (19,26) and activate it.
    2. Observe and document any immediate changes to gates on B1F.
    3. Attempt to reach the western corridor. If successful, the hypothesis is partially confirmed.
    4. If unsuccessful, return to the switch at (19,26), press it again to reset its state, and then proceed to test the switch at (21,4).
    5. Log every action and its outcome to feed into the `puzzle_log_analyzer_agent` if the logic is not immediately obvious.
- **Systematic Test Plan:**
    1. Navigate to the switch at (19,26) and activate it.
    2. Observe and document any immediate changes to gates on B1F.
    3. Attempt to reach the western corridor. If successful, the hypothesis is partially confirmed.
    4. If unsuccessful, return to the switch at (19,26), press it again to reset its state, and then proceed to test the switch at (21,4).
    5. Log every action and its outcome to feed into the `puzzle_log_analyzer_agent` if the logic is not immediately obvious.