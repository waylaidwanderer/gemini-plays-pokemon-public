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

# IV. Pokémon Mansion Puzzle Log
- **Turn 79153:** On 3F, pressed switch at (11,6). Gates at (16,5), (16,6), (16,11), (16,12) closed. Path south blocked.
- **Turn 79283:** On 3F, pressed switch at (11,6) again. Confirmed it's a toggle. Path south opened.
- **Turn 79283:** On 1F, gates at (21,18) and (22,18) opened as a result of the 3F switch.
- **Turn 79283:** On B1F, pressed switch at (19,26). This is also a toggle.
- **Turn 79314:** On B1F, gates at (17,17) and (18,17) observed to be OPEN.
- **Turn 79317:** On B1F, gates at (14,23) and (14,24) observed to be CLOSED.
- **Turn 79360:** On B1F, gates at (27,18) and (28,18) observed to be CLOSED, trapping me in the eastern section.
- **Turn 79427:** On B1F, gates at (17,17) and (18,17) re-confirmed OPEN.
- **Turn 79438:** On B1F, gates at (27,18) and (28,18) confirmed CLOSED, blocking path.
- **Turn 79450:** Used warp at (24, 23) on B1F, arrived at (22, 25) on 1F. This confirms the warp connection between B1F and 1F.
- **Turn 79454:** On 1F, gates at (21,18) and (22,18) observed to be OPEN after returning from B1F.
- **Turn 79457:** On 1F, gates at (25,14) and (26,14) observed to be CLOSED after moving into the central chamber.
- **Turn 79458:** On 1F, gates at (25,14) and (26,14) observed to be CLOSED after entering the central chamber.
- **Turn 79459:** On 1F, gates at (25,14) and (26,14) confirmed CLOSED, trapping me in the central chamber. Only exit is the warp back to B1F at (22, 24).
- **Turn 79465:** Warped from 1F (22,24) to B1F (24,23). Confirmed this is a two-way connection.
- **Turn 79483:** On B1F, gates at (27,18) and (28,18) observed to be CLOSED, trapping me in the eastern section.
- **Turn 79486:** On B1F, gates at (17,17) and (18,17) observed to be OPEN.
- **Turn 79487:** On B1F, gates at (17,17) and (18,17) re-confirmed OPEN.
- **Turn 79493:** Gates at (17,17) and (18,17) opened, revealing a path to the west. Old hypothesis about needing the switch is discarded. New Plan: Explore the western corridor to reach the unseen tiles.
- **Turn 79509:** Movement interrupted, but it revealed that the gates at (17,17) and (18,17) are now OPEN. This is a huge breakthrough and confirms a new path to the west is available. All previous plans are obsolete. The new hypothesis is that the Secret Key is located in the unexplored western corridor.
- Turn 79520: Movement interrupted, but it revealed that the gates at (17,17) and (18,17) are now OPEN. This is a huge breakthrough and confirms a new path to the west is available. All previous plans are obsolete. The new hypothesis is that the Secret Key is located in the unexplored western corridor.
- Turn 79521: The gates at (17,17) and (18,17) are now OPEN, revealing a path to the west. My previous hypothesis about the switch is discarded. My new hypothesis is that the Secret Key is in this unexplored western corridor.
- Turn 79521: The gates at (17,17) and (18,17) are now OPEN, revealing a path to the west. My previous hypothesis about the switch is discarded. My new hypothesis is that the Secret Key is in this unexplored western corridor.
- Turn 79524: Explored the western corridor on B1F; it's a dead end. Hypothesis that the Secret Key was there is incorrect. New Hypothesis: The switch at (19, 26) must be toggled to change the gate states.
- Turn 79524: Explored the western corridor on B1F; it's a dead end. Hypothesis that the Secret Key was there is incorrect. New Hypothesis: The switch at (19, 26) must be toggled to change the gate states.
- Turn 79526: Gates at (27,18) and (28,18) are now CLOSED, trapping me in the eastern section. Western corridor is a dead end. New Hypothesis: Toggling the switch at (19, 26) is the only way to open a path forward.
- Turn 79528: Explored the western corridor on B1F; it's a dead end. Hypothesis that the Secret Key was there is incorrect. New Hypothesis: The switch at (19, 26) must be toggled to change the gate states.