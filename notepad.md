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
- **Mansion Switches:** Appear to operate on a toggle system. Pressing a switch reverses the state of associated gates. This needs further testing to confirm the exact interaction patterns between floors.

# III. Pokémon Mansion Puzzle Log
- **Current Goal:** Find the Secret Key.
- **Original Agent Plan:** A 10-step plan was provided by `multi_floor_puzzle_strategist_agent`.
- **Status:** Plan failed at Step 5. Pressing the switch at (11,6) on 3F resulted in a dead end.
- **Current Hypothesis (Confirmed):** The switch at (11,6) on 3F is a toggle. Pressing it a second time reopened the path south.
- The hole at (20,15) on 3F leads to the isolated room on 1F at (17,15).
- Toggling the switch at (11,6) on 3F also opened the gate at (16,12) and (21,18) on 1F.
- **Critical Lesson:** System warnings (e.g., 'not a dead end') are absolute truth, even if they contradict map data or pathfinding. This implies hidden passages or misleading tile types exist. I must trust the system over my own interpretation.

# IV. Tool & Agent Development
- **Known Bugs:** The `define_map_marker` tool is broken and cannot be fixed as it's a reserved name. Do not attempt to use it. Track spatial information in the notepad instead.
- **Agent Idea:** Create a 'Puzzle State Analyst' agent to analyze map XML and propose puzzle-solving hypotheses.
- The gate at (21, 18) on 1F is now confirmed open after toggling the switch on 3F.
- The gate at (22, 18) on 1F is also confirmed open.
- The warp at (22,24) on 1F leads to (24,23) on B1F.
- The switch at (19, 26) on B1F is a toggle. Pressing it closed the gates at (27, 18) and (28, 18).
- The switch at (19, 26) on B1F is a toggle. Pressing it closed the gates at (27, 18) and (28, 18).
- The gates at (17, 17) and (18, 17) on B1F are now confirmed open after pressing a switch on a different floor.