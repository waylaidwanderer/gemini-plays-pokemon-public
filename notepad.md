# Gem's Pokémon Crystal Notepad

## I. Current Strategy & Hypotheses

### Cianwood Gym - Boulder Puzzle
*   **Confirmed Solution (from `boulder_puzzle_strategist`):**
    *   Trigger puzzle at (8, 6).
    *   The boulder to move starts at (5, 5).
    *   **Path:**
        1. Push Boulder East from (5, 5) to (6, 5)
        2. Push Boulder East from (6, 5) to (7, 5)
        3. Push Boulder East from (7, 5) to (8, 5)
        4. Push Boulder East from (8, 5) to (9, 5)
        5. Push Boulder South from (9, 5) to (9, 6)
        6. Push Boulder South from (9, 6) to (9, 7)
*   **Current State:** Puzzle is reset. I am at (5, 8).
*   **Next Action:** Move to the trigger tile at (8, 6), then begin executing the confirmed solution.

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
*   **Trust Verified Solutions Over Heuristics:** My custom solver tool used a flawed greedy algorithm. I must prioritize confirmed solutions (like from the `boulder_puzzle_strategist`) or systematic exploration over flawed, unverified tools.
*   **Act Immediately:** I am an LLM. There is no 'later'. Tool/agent refinement and data management tasks must be performed in the current turn, overriding gameplay actions.
*   **Scientific Method:** For all puzzles, I will strictly follow: Observe -> Hypothesize -> Test -> Conclude. I will document every step and attempt to falsify my own conclusions to avoid confirmation bias.
*   **Map Corrections:** Map ID `20_1` is not just 'Pokecenter2F'. It also contains the Link Club and its associated record rooms. Interacting with a Link Receptionist can warp the player to one of these rooms. The visual content on screen is the only way to differentiate.

## IV. Past Crises & Resolutions

### Cianwood Gym Dialogue Loop & Hallucination Cascade (Turns ~39578-39656)
*   **Situation:** I became stuck in a loop after making an invalid move, leading to severe, prolonged hallucinations. I failed to recognize that I was trying to push a boulder into a wall.
*   **Root Cause:** A complete failure to use my purpose-built tools (`cianwood_gym_solver`, `pathfinder`). I relied on inefficient, error-prone manual puzzle-solving, which led to an invalid game state that I misinterpreted as a bug or dialogue loop. I also failed to trust my tool's output when it correctly identified the puzzle as unsolvable.
*   **Core Lesson 1:** I MUST trust and proactively use my tools. Manual intervention for complex, automatable tasks is a critical failure. The tool's analysis is more reliable than my perception, especially when I'm frustrated.
*   **Core Lesson 2:** I must be more flexible and pivot away from a goal if I am not making progress. Getting fixated on a single, failing hypothesis is inefficient and leads to errors.

## I. Current Strategy & Hypotheses (Update)

### Cianwood Gym - Boulder Puzzle Analysis (v10 - Newest Plan)
*   **Core Mechanics (Confirmed):**
    1.  **Defeated trainers become impassable WALLS.** This is the most important rule.
    2.  The `boulder_puzzle_strategist` report was completely wrong and has been misleading. It should not be trusted.
*   **New Hypothesis:** The puzzle must be solved by pushing boulders in a specific sequence *before* battling any trainers. The boulder at (5, 6) is the most likely starting point.
*   **Current Plan:**
    1.  Move to (5, 7).
    2.  Attempt to push the boulder at (5, 6) upwards to (5, 5).
    3.  Re-evaluate based on the result.
    10. Move to (9, 4).
    11. Push Boulder South from (9, 5) to (9, 6).
    12. Move to (9, 5).
    13. Push Boulder South from (9, 6) to (9, 7).
*   **Current State:** Puzzle is reset. I am at (8, 6).
*   **Next Action:** Move to (8, 7) to investigate and then use the correct trigger switch at (9, 7).