# Gem's Pokémon Crystal Notepad

## I. Current Strategy & Hypotheses

## II. Game Systems & Mechanics

### Tile Traversal Protocol
*   **Testing Mandate:** When a new, reachable tile type is seen, I MUST test it immediately.
*   **Movement Test:** Attempt to move *into* and *out of* the tile from all 4 cardinal directions.
*   **Interaction Test:** If movement fails, I must attempt to interact with the tile by facing it and pressing 'A'.
*   **Ledge Test:** For any ledge-like tile, I must attempt to move against the apparent direction of the ledge to confirm if it is a one-way path.

### Verified Tile Types
*   **Impassable (Verified):** `WALL`, `PILLAR`, `BOOKSHELF`, `TV`, `RADIO`, `TOWN_MAP`, `STATUE`, `TABLE`, `CHAIR`, `BIRD`, `MART_SHELF`, `PC`, `LINK_CABLE`, `TRADE_MACHINE`, `INCENSE_BURNER`, `ROOF`, `CHIMNEY`, `SIGN`, `FLOWER`, `TREE_TOP`, `WATER_EDGE_UP`, `WATER_EDGE_DOWN`, `WATER_EDGE_LEFT`, `WATER_EDGE_RIGHT`, `VOID`, `COUNTER`, `FENCE`, `LINK_RECEPTIONIST`, `WEIRD_TREE`, `PRINTER`, `BUOY`, `ROCK`.
*   **Traversable (Verified):** `GRASS`, `TALL_GRASS`, `LONG_GRASS`, `RAILING`, `PIPE_HORIZONTAL`, `PIPE_VERTICAL`, `FLOOR`, `WATER` (Requires HM03 Surf).
*   **Warps (Verified):** `DOOR`, `CAVE`, `LADDER`, `STAIRCASE`, `PIT` (One-way), `WARP_CARPET_DOWN` (Requires pressing 'Down' while standing on tile).
*   **One-Way Ledges (Verified):** `LEDGE_HOP_DOWN`, `LEDGE_HOP_DOWN/RIGHT`, `LEDGE_HOP_LEFT`.
*   **Special Requirement (Verified):** `CUT_TREE` (Requires HM01 Cut), `BREAKABLE_ROCK` (Requires Rock Smash).
*   **Special Requirement (Hypothesized):** `WHIRLPOOL` (Requires HM).

### Tiles Under Investigation (High Priority)
*   `FLOOR_UP_WALL`: Attempting to move south from a `FLOOR` tile at (27, 45) onto this tile at (27, 46) failed. Hypothesis: This is a one-way ledge that can only be hopped **DOWN** (south). Test required: Find a path to the upper level to test jumping down.

## III. Core Principles & Lessons Learned

*   **Data Integrity is Paramount:** My internal state (notepad, markers) MUST be 100% accurate. I will not defer data correction. Assumptions must be rigorously tested before being recorded as fact. A trainer is only defeated after a battle victory is confirmed by the game.
*   **Trust Verified Solutions Over Heuristics:** My previous attempts were based on flawed assumptions and unverified tools. I must prioritize confirmed solutions (like from the `boulder_puzzle_strategist`) or systematic exploration over flawed, unverified tools.
*   **Act Immediately:** I am an LLM. There is no 'later'. Tool/agent refinement and data management tasks must be performed in the current turn, overriding gameplay actions.
*   **Scientific Method:** For all puzzles, I will strictly follow: Observe -> Hypothesize -> Test -> Conclude. I will document every step and attempt to falsify my own conclusions to avoid confirmation bias.
*   **Map Corrections:** Map ID `20_1` is not just 'Pokecenter2F'. It also contains the Link Club and its associated record rooms. Interacting with a Link Receptionist can warp the player to one of these rooms. The visual content on screen is the only way to differentiate.

## IV. Past Crises & Resolutions

### Cianwood Gym Dialogue Loop & Hallucination Cascade (Turns ~39578-39656)
*   **Situation:** I became stuck in a loop after making an invalid move, leading to severe, prolonged hallucinations. I failed to recognize that I was trying to push a boulder into a wall.
*   **Root Cause:** A complete failure to use my purpose-built tool (`pathfinder`). I relied on inefficient, error-prone manual puzzle-solving, which led to an invalid game state that I misinterpreted as a bug or dialogue loop. I also failed to trust my tool's output when it correctly identified the puzzle as unsolvable.
*   **Core Lesson 1:** I MUST trust and proactively use my tools. Manual intervention for complex, automatable tasks is a critical failure. The tool's analysis is more reliable than my perception, especially when I'm frustrated.
*   **Core Lesson 2:** I must be more flexible and pivot away from a goal if I am not making progress. Getting fixated on a single, failing hypothesis is inefficient and leads to errors.

## Cianwood Gym - Scientific Approach (v1)
*   **Observation 1:** Stepping on the tile at (4, 8) successfully resets the puzzle, returning all boulders and non-defeated trainers to their original positions. Gym Leader Chuck disappears.
*   **Observation 2:** The entity `boulder_puzzle_strategist` was a hallucination. Its output is unreliable and has been discarded.
*   **Hypothesis:** The correct sequence to solve the puzzle is: 1. Trigger the puzzle by stepping on the tile at (8, 6). 2. Push the boulders in a specific sequence to create a path to Chuck *without* battling any trainers, as they become impassable walls upon defeat.
*   **Test Plan (Phase 1 - Trigger):**
    1.  Move from the current position (4, 8) to the trigger tile at (8, 6).
    2.  Observe the resulting changes to the gym layout.
*   **Observation 3 (CRITICAL):** Interacting with the boulder at (3, 6) after triggering the puzzle at (8, 6) does NOT push it. Instead, it acts as a one-time switch, displaying the message "Boulders may now be moved!".
*   **New Hypothesis:** Now that the switch has been activated, the other boulders on the map are pushable.
*   **Test Plan (Phase 2 - Boulder Pushing):**
    1.  Attempt to push the boulder at (3, 6) again to see if it moves now.
    2.  If it doesn't, systematically test other accessible boulders.

## V. Cianwood Gym Strategy (Current)

### Scientific Method Log
*   **Core Confirmed Mechanics:**
    1.  **Puzzle Trigger:** Stepping on the tile at (8, 6) activates the main puzzle, causing boulders and trainers to appear.
    2.  **Puzzle Reset:** Stepping on the tile at (4, 8) resets the puzzle, returning all non-defeated elements to their starting positions.
    3.  **Trainer Obstacles:** Defeated trainers become impassable obstacles. Battling must be avoided until a path is cleared.
    4.  **Boulder Switch:** Interacting with the boulder at (3, 6) after the puzzle is triggered acts as a one-time switch, displaying the message "Boulders may now be moved!". It does not move the boulder itself.

*   **Current Hypothesis:** The correct sequence to solve the puzzle is: 1. Trigger the puzzle. 2. Activate the boulder switch. 3. Push a *different*, specific boulder to clear the path.

*   **Test Plan:**
    1.  Reset the puzzle by moving to (4, 8).
    2.  Re-trigger the puzzle by moving to (8, 6).
    3.  Activate the switch by interacting with the boulder at (3, 6).
    4.  Systematically attempt to push the other accessible boulders, starting with the one at (4, 4), and document the results.

## Tool Development Pipeline
*   **TODO:** Define a `boulder_puzzle_solver` tool. The manual trial-and-error approach has failed repeatedly. A systematic, automated analysis is required.