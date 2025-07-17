# I. Core Principles & Lessons Learned
- **Immediate Action is Non-Negotiable:** Deferring tasks like tool fixes, agent creation, or documentation is a critical failure. All such actions must be performed in the current turn.
- **Systematic Testing:** When faced with a puzzle, I must form single, testable hypotheses and design minimal experiments to confirm or deny them. I will rigorously document each test and its outcome to avoid confirmation bias and repeated failures.

# II. Game Intel
## A. Confirmed ROM Hack Mechanics
- **Type Effectiveness:**
    - Super Effective (2x): Psychic > Ghost/Poison; Ghost > Psychic; Electric > Rock/Water; CUT (Normal) > VICTREEBEL (Grass/Poison); Flying > Grass/Poison; Psychic > Flying; Ice > Ground; Ground > Poison; Ground > Fire; Rock > Fire.
    - Not Very Effective (0.5x): Normal !> Psychic; Electric !> Grass; Rock !> Ground; Psychic !> Psychic; Bite (Normal) !> HAUNTER (Ghost/Poison); Ice !> Gyarados (Water/Flying); Poison !> Poison; Ice !> Water; Poison !> Ground.
    - Immune (0x): Flying immune to Ground; Ground immune to Electric; MUK immune to Poison; HYPNO immune to STUN SPORE; MUK immune to THUNDER WAVE; MAROWAK immune to POISON GAS.

## B. Tile Mechanics & Movement Rules
- **Switch Interaction:** Switches must be activated by standing on the tile directly BELOW them (e.g., at (X, Y+1) for a switch at (X,Y)), facing UP, and then pressing A.

# III. Pokémon Mansion Puzzle Log
- **Current Goal:** Find the Secret Key.
- **Key Discoveries:** The mansion contains a multi-floor switch puzzle. The state of gates depends on the sequence of switch activations.

## A. Systematic Testing Plan
- **Goal:** Fully understand the logic of the two main switches.
- **Hypothesis 1 (CONFIRMED):** The 1F switch at (3,6) operates on a simple toggle state. Pressing it reverses its previous effect on both the western gates (17,8)/(18,8) and the eastern gates (25,14)/(26,14).
- **Hypothesis 2:** The 2F switch at (3,12) also affects the gates.
- **Test 1.2 (Concluded - Part 1):** Pressed the 2F switch. **Outcome:** The western gates at (17,8)/(18,8) **closed**.
- **Test 1.2 (Current Action):** Check the state of the eastern gates at (25,14)/(26,14).