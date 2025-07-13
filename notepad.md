# Gem's Pokémon Crystal Notepad

## I. Current Strategy & Hypotheses

### Cianwood Gym - Boulder Puzzle Under Investigation
*   **Core Insight:** The reset tile at (4, 8) brings back ALL puzzle elements, including the boulders AND the trainers that appear with them. The trainer at (5, 5) is not permanently defeated. Exiting and re-entering the gym also seems to reset the boulders if they have been moved from their initial triggered position.
*   **Current Hypothesis (The "Trainer First" Strategy - Attempt #5):** The puzzle requires defeating the trainer at (5, 5) *before* clearing the final path. This requires a specific sequence of boulder pushes.
    *   **Plan:**
        1.  Ensure puzzle is triggered (boulders and trainers are present).
        2.  From below the central boulder, push the boulder at (4, 7) up to (4, 6).
        3.  Move to (4, 5) to battle and defeat the trainer at (5, 5).
        4.  After the trainer is defeated, push the remaining boulders at (3, 7) and (5, 7) upwards to clear the path.
        5.  Walk to the Gym Leader.
    *   **CRITICAL:** Do NOT walk up the central path. The tile at (4, 8) is a trap that resets the puzzle. Use the side paths.
*   **Alternative Hypothesis (The "Bypass" Strategy):** It may be possible to solve the puzzle without fighting the trainer at (5,5).
    *   **Plan:**
        1.  Push the boulder at (3,7) up first.
        2.  Push the boulder at (5,7) up next.
        3.  Finally, push the middle boulder at (4,7) up.
        4.  This sequence might open a path to the leader while avoiding the trainer. This needs to be tested if the "Trainer First" strategy fails.

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
*   **Trust Tools Over Perception:** My custom tool output is based on the game's ground truth. If it says 'no path', I must trust it and investigate my own understanding, not assume the tool is broken.
*   **Act Immediately:** I am an LLM. There is no 'later'. Tool/agent refinement and data management tasks must be performed in the current turn, overriding gameplay actions.
*   **Scientific Method:** For all puzzles, I will strictly follow: Observe -> Hypothesize -> Test -> Conclude. I will document every step and attempt to falsify my own conclusions to avoid confirmation bias.
*   **Map Corrections:** Map ID `20_1` is not just 'Pokecenter2F'. It also contains the Link Club and its associated record rooms. Interacting with a Link Receptionist can warp the player to one of these rooms. The visual content on screen is the only way to differentiate.

## IV. Tool Development & Maintenance
*   **Puzzle Reset Mechanic (New Insight):** The reset tile at (4, 8) does not remove the boulders from the gym once they have been triggered. It likely only resets their positions to the starting configuration. This means the boulders are a permanent part of the puzzle after stepping on the trigger at (8, 6).
*   **Future Agent Idea:** A `boulder_puzzle_strategist` agent could be created to help reason through the logic of this puzzle, considering the state changes and documented hypotheses.