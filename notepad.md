# I. Core Principles & Lessons Learned
- **Immediate Action is Non-Negotiable:** Deferring tasks like tool fixes, agent creation, or documentation is a critical failure. All such actions must be performed in the current turn.
- **Systematic Testing:** When faced with a puzzle, I must form single, testable hypotheses and design minimal experiments to confirm or deny them. I will rigorously document each test and its outcome to avoid confirmation bias and repeated failures.
- **Tool & Agent Integrity is Paramount:** A faulty tool or agent is worse than none. Debugging and refining them is my absolute highest priority, superseding any other goal.

# II. Game Intel
## A. Confirmed ROM Hack Mechanics
- **Type Effectiveness:**
    - Super Effective (2x): Psychic > Ghost/Poison; Ghost > Psychic; Electric > Rock/Water; CUT (Normal) > VICTREEBEL (Grass/Poison); Flying > Grass/Poison; Psychic > Flying; Ice > Ground; Ground > Poison; Ground > Fire; Rock > Fire.
    - Not Very Effective (0.5x): Normal !> Psychic; Electric !> Grass; Rock !> Ground; Psychic !> Psychic; Bite (Normal) !> HAUNTER (Ghost/Poison); Ice !> Gyarados (Water/Flying); Poison !> Poison; Ice !> Water; Poison !> Ground.
    - Immune (0x): Flying immune to Ground; Ground immune to Electric; MUK immune to Poison; HYPNO immune to STUN SPORE; MUK immune to THUNDER WAVE; MAROWAK immune to POISON GAS.

## B. Tile Mechanics & Movement Rules
- **Switches:** Interactable background objects. Activating them can toggle the state of gates, potentially across multiple floors.
- **Gates (`open_gate`, `closed_gate`, `gate_offscreen`):** Barriers whose state is controlled by switches. Their state can change even when they are off-screen, but the visual update only occurs when they are on-screen.

# III. Pokémon Mansion Puzzle Log
- **Current Goal:** Find the Secret Key.
- **Key Discoveries:** The mansion contains a multi-floor switch puzzle. The state of gates depends on the sequence of switch activations.
- **Puzzle State:**
    - 1F Switch at (3,6)
    - 2F Switch at (3,12)
- **Confirmed Sequence:** `1F Switch -> 2F Switch -> 1F Switch` opens the gates at (17, 8) and (18, 8) on 1F, but closes the gates at (25, 14) and (26, 14).

## A. Systematic Testing Plan
- **Goal:** Fully understand the logic of the two main switches.
- **Hypothesis 1 (CONFIRMED):** The switches operate on a simple toggle state. Pressing a switch reverses its previous effect.
- **Test 1.1 (Concluded):** Pressed the 1F switch at (3,6) again. **Outcome:** The gates at (25,14)/(26,14) **opened**. **Conclusion:** The 1F switch operates on a simple toggle, reversing the state of both western and eastern gate sets.
- **Test 1.1 (Concluded):** Pressed the 1F switch at (3,6) again. **Outcome:** The gates at (25,14)/(26,14) **opened**. **Conclusion:** The 1F switch operates on a simple toggle, reversing the state of both western and eastern gate sets.
- **Test 1.2 (Next Step):** Go to 2F and press the switch at (3,12). Observe the state of all known gates.
- **Switch Interaction:** Switches must be activated by standing on the tile directly BELOW them (e.g., at (X, Y+1) for a switch at (X,Y)), facing UP, and then pressing A.