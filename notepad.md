# Gem's Pokémon Crystal Notepad

## I. Current Strategy & Hypotheses

### Cianwood Gym - Boulder Puzzle Under Investigation
*   **Core Insight:** The reset tile at (4, 8) brings back ALL puzzle elements, including the boulders AND the trainers that appear with them. The trainer at (5, 5) is not permanently defeated. Exiting and re-entering the gym also seems to reset the boulders if they have been moved from their initial triggered position.
*   **FAILED HYPOTHESIS (The "Trainer First" Strategy):** The puzzle requires defeating the trainer at (5, 5) *before* clearing the final path. 
    *   **Outcome:** FAILED. After pushing the central boulder and navigating to (5, 6), movement to (5, 5) to initiate the battle was blocked. This indicates re-battling the trainer is not the intended solution.
*   **Current Hypothesis (The "Bypass" Strategy):** It's possible to solve the puzzle without fighting the trainer at (5,5) by pushing the boulders in a specific order.
    *   **Plan:**
        1. Push the boulder at (3,6) up first.
        2. Push the boulder at (5,7) up next.
        3. Finally, push the middle boulder at (4,4) up.
        4. This sequence might open a path to the leader while avoiding the trainer.

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

### Cianwood Gym - Boulder Puzzle Under Investigation (Update)
*   **FAILED HYPOTHESIS (The "Bypass" Strategy - Attempt 1):** The puzzle can be solved by pushing the left boulder at (3,6) up first. 
    *   **Outcome:** FAILED. Attempting to push the boulder from (3,7) was blocked, indicating a prerequisite has not been met.
*   **FAILED HYPOTHESIS (The "Yoshi First" Strategy):** Failed. Black Belt Yoshi at (2, 12) is not a battlable trainer.
*   FAILED HYPOTHESIS (The "Chain Reaction" Strategy - Attempt 2): Defeating Black Belt Nob unlocks the ability to push the leftmost boulder at (3, 6).
    *   **Outcome:** FAILED. Attempting to push the boulder from (3, 7) was blocked.
*   **CONFIRMED HYPOTHESIS (The "Chain Reaction" Strategy):** Defeating Black Belt Nob unlocked the ability to push the rightmost boulder at (5, 7).
*   **CONFIRMED HYPOTHESIS (Chain Reaction Pt. 2):** Pushing the boulder at (5, 7) unlocked the ability to push the leftmost boulder at (3, 6).
*   **CONFIRMED HYPOTHESIS (Chain Reaction Pt. 3):** Pushing the two side boulders unlocked the ability to battle the trainer at (5, 5).
*   **Current Hypothesis:** Defeating the trainer at (5, 5) has now unlocked the final, central boulder at (4, 4).