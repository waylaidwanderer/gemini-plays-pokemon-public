# Gem's Pokémon Crystal Notepad

## I. Core Principles & Lessons Learned

*   **Data Integrity is Paramount:** My internal state (notepad, markers) MUST be 100% accurate. I will not defer data correction. Assumptions must be rigorously tested before being recorded as fact. A trainer is only defeated after a battle victory is confirmed by the game.
*   **Trust Tools Over Perception:** My `pathfinder` tool's output is based on the game's ground truth. If it says 'no path', I must trust it and investigate my own understanding, not assume the tool is broken.
*   **Act Immediately:** I am an LLM. There is no 'later'. Tool/agent refinement and data management tasks must be performed in the current turn, overriding gameplay actions.
*   **Scientific Method:** For all puzzles, I will strictly follow: Observe -> Hypothesize -> Test -> Conclude. I will document every step and attempt to falsify my own conclusions to avoid confirmation bias.

## II. Game Systems & Mechanics

### Tile Traversal Protocol
*   **Testing Mandate:** When a new, reachable tile type is seen, I MUST test it immediately.
*   **Movement Test:** Attempt to move *into* and *out of* the tile from all 4 cardinal directions.
*   **Interaction Test:** If movement fails, I must attempt to interact with the tile by facing it and pressing 'A'.
*   **Ledge Test:** For any ledge-like tile, I must attempt to move against the apparent direction of the ledge to confirm if it is a one-way path.

### Verified Tile Types
*   **Impassable (Verified):** `WALL`, `PILLAR`, `BOOKSHELF`, `TV`, `RADIO`, `TOWN_MAP`, `STATUE`, `TABLE`, `CHAIR`, `BIRD`, `MART_SHELF`, `PC`, `LINK_CABLE`, `TRADE_MACHINE`, `INCENSE_BURNER`, `ROOF`, `CHIMNEY`, `SIGN`, `FLOWER`, `TREE_TOP`, `WATER_EDGE_UP`, `WATER_EDGE_DOWN`, `WATER_EDGE_LEFT`, `WATER_EDGE_RIGHT`, `VOID`, `COUNTER`, `FENCE`, `LINK_RECEPTIONIST`, `WEIRD_TREE`, `PRINTER`, `BUOY`, `ROCK`.
*   **Traversable (Verified):** `GRASS`, `TALL_GRASS`, `LONG_GRASS`, `RAILING`, `PIPE_HORIZONTAL`, `PIPE_VERTICAL`, `FLOOR`, `WATER` (Requires HM03 Surf).
*   **Warps (Verified):** `DOOR`, `CAVE`, `LADDER`, `STAIRCASE`, `PIT` (One-way).
*   **Special Warps (Verified):** 
    *   `WARP_CARPET_DOWN`: To activate, stand on the tile and press **Down**.
*   **One-Way Ledges (Verified):**
    *   `LEDGE_HOP_DOWN`: Can only be hopped **DOWN**.
    *   `LEDGE_HOP_DOWN/RIGHT`: Can only be hopped in the specified direction.
    *   `LEDGE_HOP_LEFT`: Can only be hopped **LEFT**.
*   **Special Requirement (Verified):**
    *   `CUT_TREE`: Becomes traversable after using CUT.
    *   `BREAKABLE_ROCK`: Requires Rock Smash.
*   **Special Requirement (Hypothesized):**
    *   `WHIRLPOOL` (Requires HM).

### Tiles Under Investigation (High Priority)
*   `FLOOR_UP_WALL`: Attempting to move south from a `FLOOR` tile at (27, 45) onto this tile at (27, 46) failed. Hypothesis: This is a one-way ledge that can only be hopped **DOWN** (south). Test required: Find a path to the upper level to test jumping down.

## III. Strategic Plans & Hypotheses

### Cianwood Gym Puzzle
*   **Confirmed Mechanic 1 (Boulder Reset):** Stepping on the tile at (8, 6) causes the Gym Leader and three boulders to appear. Exiting and re-entering the gym removes the boulders, but the Gym Leader remains.
*   **Confirmed Mechanic 2 (Central Path Trap):** After resetting the boulders, stepping on at least one tile on the central path (between y=6 and y=12) causes the boulders to reappear, resetting the puzzle.
*   **Confirmed Mechanic 3 (Side Paths):** The eastern and western side paths are physically disconnected from the northern section where the Gym Leader is. They are not a valid route.
*   **Failed Hypothesis 1 (Statue Interaction):** Interacting with the statues at (3, 15) and (6, 15) has no effect on the gym's state.
*   **Current Plan (Systematic Trap Identification):**
    1.  Perform the boulder reset procedure (step on (8, 6), exit, re-enter).
    2.  Carefully test each tile on the central path, one by one, to identify the exact location of the trap trigger(s). Move onto a tile, then move off it to see if the boulders reappear. This will isolate the unsafe tile(s).