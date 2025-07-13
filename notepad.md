# Gem's Pokémon Crystal Notepad

## I. Game Systems & Mechanics

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

## II. Core Principles & Lessons Learned

*   **Data Integrity is Paramount:** My internal state (notepad, markers) MUST be 100% accurate. I will not defer data correction. Assumptions must be rigorously tested before being recorded as fact.
*   **Trust Automation:** My custom tools (`pathfinder`, `boulder_scanner`) are more reliable than my manual navigation and analysis. I must prioritize using them to avoid unforced errors.
*   **Act Immediately:** I am an LLM. There is no 'later'. Tool/agent refinement and data management tasks must be performed in the current turn, overriding gameplay actions.
*   **Scientific Method:** For all puzzles, I will strictly follow: Observe -> Hypothesize -> Test -> Conclude. I will document every step and attempt to falsify my own conclusions to avoid confirmation bias.

## III. Future Agent & Tool Ideas
*   `puzzle_strategist` agent: Could take the output of `boulder_scanner` and the map layout to devise a multi-step solution for complex boulder puzzles.

## Cianwood Gym Puzzle Log
*   **Hypothesis 1:** Interacting with the boulder at (5, 6) is a global switch that makes all other boulders pushable by walking into them.
*   **Test 1:** Interacted with boulder at (5, 6). Moved to (3, 7). Pushed 'Up' to move boulder at (3, 6).
*   **Result 1:** Boulder at (3, 6) did not move.
*   **Conclusion 1:** Hypothesis 1 is FALSE. The interaction at (5, 6) does not make other boulders pushable by walking.
*   **Hypothesis 2:** STRENGTH must be activated by pressing 'A' while facing a movable boulder.
*   **Test 2:** Stand at (3, 7) facing the boulder at (3, 6) and press 'A'.