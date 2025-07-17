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
- **teleport:** Instant warp tile within the same logical location (e.g., inside a building).
- **spinner_up/down/left/right:** Forces movement in the specified direction.
- **closed_gate:** An impassable gate that is currently visible on the screen. Treat as a wall.
- **open_gate:** A previously closed gate that is now open and acts as `ground`.
- **gate_offscreen:** A gate (either open or closed) that is not currently visible. Treat as potentially open for pathfinding.

# III. Solved Puzzles
## A. Pokémon Mansion
- **Conclusion:** The two switches in the basement (at (21, 4) and (19, 26)) control the gates on all floors. To open the main path on 1F at (21, 18) & (22, 18), both basement switches must be activated. The puzzle is now solved.

# IV. Active Puzzles
## A. Cinnabar Gym
- **Observation:** The gym is split into rooms separated by gates. I've explored both the eastern and western corridors and hit dead ends in both. The trainers in the eastern room at (12, 5) and (17, 9) are stuck in dialogue loops, and the western room is blocked by closed gates I cannot open.
- **Hypothesis 1 (Failed):** Answering the first quiz correctly will open the left gate. (Outcome: opened right gate).
- **Hypothesis 2 (Failed):** The trainer at (12, 5) is the next step. (Outcome: Stuck in dialogue loop).
- **Hypothesis 3 (Failed):** Defeating the trainer at (17, 9) is the next step. (Outcome: Stuck in pre-battle dialogue loop).
- **Hypothesis 4 (Failed):** Interacting with the quiz machine at (16, 8) and intentionally answering incorrectly might activate one of the previously looping trainers. (Outcome: Received 'Sorry! Bad call!' message, no other apparent change).
- **Hypothesis 5 (Current):** Answering the quiz at (16, 8) incorrectly has changed the state of the trainer at (17, 9), making them battle-ready.
- **Test 5:** Interact with the trainer at (17, 9).

## B. Cinnabar Gym (Decoy)
- **Conclusion:** This building is a decoy. The puzzle is a red herring with looping trainers and quiz machines that lead to dead ends. The game state confirms there are no reachable unseen tiles and the only exit is the entrance warp. The true solution to progressing in Cinnabar is to use the SECRET KEY on the locked gym door on the main island. Puzzle solved.