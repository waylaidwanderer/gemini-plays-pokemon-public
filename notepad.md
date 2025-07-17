# I. Core Principles & Lessons Learned
- **Immediate Action is Non-Negotiable:** Deferring tasks like tool fixes, agent creation, or documentation is a critical failure. All such actions must be performed in the current turn.
- **Systematic Testing:** When faced with a puzzle, I must form single, testable hypotheses and design minimal experiments to confirm or deny them. I will rigorously document each test and its outcome to avoid confirmation bias and repeated failures.
- **Trust The Agent:** I have powerful custom agents for a reason. I must trust their analysis and plans over my own manual trial-and-error, especially for complex, multi-stage problems.

# II. Game Intel
## A. Confirmed ROM Hack Mechanics
- **Type Effectiveness:**
    - Super Effective (2x): Psychic > Ghost/Poison; Ghost > Psychic; Electric > Rock/Water; CUT (Normal) > VICTREEBEL (Grass/Poison); Flying > Grass/Poison; Psychic > Flying; Ice > Ground; Ground > Poison; Ground > Fire; Rock > Fire.
    - Not Very Effective (0.5x): Normal !> Psychic; Electric !> Grass; Rock !> Ground; Psychic !> Psychic; Bite (Normal) !> HAUNTER (Ghost/Poison); Ice !> Gyarados (Water/Flying); Poison !> Poison; Ice !> Water; Poison !> Ground.
    - Immune (0x): Flying immune to Ground; Ground immune to Electric; MUK immune to Poison; HYPNO immune to STUN SPORE; MUK immune to THUNDER WAVE; MAROWAK immune to POISON GAS.

## B. Tile Mechanics & Movement Rules
- **Switch Interaction:** Switches must be activated by standing on the tile directly BELOW them (e.g., at (X, Y+1) for a switch at (X,Y)), facing UP, and then pressing A.
- **gate_offscreen:** The state of these gates can change based on switch presses on any floor. Their state is only revealed when they come on-screen.

# III. Pokémon Mansion Puzzle Log
- **Current Goal:** Find the Secret Key.
- **Overarching Strategy:** I will follow the 10-step plan provided by the `multi_floor_puzzle_strategist_agent`.

## A. Agent-Guided Strategic Plan
- **Step 1 (In Progress):** Start on 1F and press the Switch at (3,6).
- **Step 2:** Proceed to the Warp to 2F at (6,11).
- **Step 3:** On 2F, press the Switch at (3,12).
- **Step 4:** Take a warp to 3F (e.g., at (8,11)).
- **Step 5:** On 3F, press the Switch at (11,6).
- **Step 6:** Use the Hole to 2F at (20,15).
- **Step 7:** From the new area on 2F, use the Hole to 1F at (17,15).
- **Step 8:** In the new area on 1F, take the Warp to B1F at (22,24).
- **Step 9:** In the basement, press the final Switch at (19,26).
- **Step 10:** Explore the newly accessible rooms to find the Secret Key.