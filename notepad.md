# Gem's Pokémon Crystal Notepad

## I. Game Systems & Mechanics

### Tile Traversal Protocol
*   **Testing Mandate:** When a new, reachable tile type is seen, I MUST test it immediately.
*   **Movement Test:** Attempt to move *into* and *out of* the tile from all 4 cardinal directions.
*   **Interaction Test:** If movement fails, I must attempt to interact with the tile by facing it and pressing 'A'.
*   **Ledge Test:** For any ledge-like tile, I must attempt to move against the apparent direction of the ledge to confirm if it is a one-way path.

### Verified Tile Types
*   **Impassable (Verified):** `WALL`, `PILLAR`, `BOOKSHELF`, `TV`, `RADIO`, `TOWN_MAP`, `TABLE`, `CHAIR`, `BIRD`, `MART_SHELF`, `PC`, `LINK_CABLE`, `TRADE_MACHINE`, `INCENSE_BURNER`, `ROOF`, `CHIMNEY`, `SIGN`, `FLOWER`, `TREE_TOP`, `WATER_EDGE_UP`, `WATER_EDGE_DOWN`, `WATER_EDGE_LEFT`, `WATER_EDGE_RIGHT`, `VOID`, `COUNTER`, `FENCE`, `LINK_RECEPTIONIST`, `WEIRD_TREE`, `PRINTER`, `BUOY`, `ROCK`.
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

## Cianwood Gym Puzzle Log
*   **Hypothesis 1:** Interacting with the boulder at (5, 6) is a global switch that makes all other boulders pushable by walking into them.
*   **Conclusion 1:** FALSE. The interaction at (5, 6) does not make other boulders pushable by walking.
*   **Hypothesis 2:** STRENGTH must be activated by pressing 'A' while facing a movable boulder.
*   **Conclusion 2:** FALSE. Pressing 'A' on a boulder seems to be a global switch, not a targeted push.
*   **Hypothesis 3:** Pushing the boulders at (3, 7), (4, 7), and (5, 7) up will form a traversable bridge to the Gym Leader.
*   **Conclusion 3:** FALSE. The pushed boulders do not form a traversable bridge and remain impassable objects.
*   **Hypothesis 4:** Defeating the Black Belt at (5, 5) is the trigger to solve the puzzle.
*   **Conclusion 4:** Untestable. Pathfinder confirmed the platforms are separate.
*   **Hypothesis 5:** The statues at (6, 15) and (3, 15) are switches that alter the gym layout.
*   **Conclusion 5:** FALSE. Interacting with both statues had no effect. The puzzle inside the gym seems unsolvable with current knowledge.
*   **New Lead:** A Gym Guide mentioned the leader trains under a waterfall. I will now leave the gym to investigate this clue.