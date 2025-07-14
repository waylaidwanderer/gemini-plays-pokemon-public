# Gem's Pokémon Crystal Notepad

## I. Game Systems & Mechanics

### Tile Traversal Protocol
*   **Testing Mandate:** When a new, reachable tile type is seen, I MUST test it immediately.
*   **Movement Test:** Attempt to move *into* and *out of* the tile from all 4 cardinal directions.
*   **Interaction Test:** If movement fails, I must attempt to interact with the tile by facing it and pressing 'A'.
*   **Ledge Test:** For any ledge-like tile, I must attempt to move against the apparent direction of the ledge to confirm if it is a one-way path.

### Verified Tile Types
*   **Impassable (Verified):** `WALL`, `PILLAR`, `BOOKSHELF`, `TV`, `RADIO`, `TOWN_MAP`, `TABLE`, `CHAIR`, `BIRD`, `MART_SHELF`, `PC`, `LINK_CABLE`, `TRADE_MACHINE`, `INCENSE_BURNER`, `ROOF`, `CHIMNEY`, `SIGN`, `FLOWER`, `TREE_TOP`, `WATER_EDGE_UP`, `WATER_EDGE_DOWN`, `WATER_EDGE_LEFT`, `WATER_EDGE_RIGHT`, `VOID`, `COUNTER`, `FENCE`, `LINK_RECEPTIONIST`, `WEIRD_TREE`, `PRINTER`, `BUOY`, `ROCK`, `WINDOW`.
*   **Traversable (Verified):** `GRASS`, `TALL_GRASS`, `LONG_GRASS`, `RAILING`, `PIPE_HORIZONTAL`, `PIPE_VERTICAL`, `FLOOR`.
*   **Warps (Verified):** `DOOR`, `CAVE`, `LADDER`, `STAIRCASE`.
*   **One-Way Traversal (Verified):** `PIT` (One-way down), `LEDGE_HOP_DOWN`, `LEDGE_HOP_DOWN/RIGHT`, `LEDGE_HOP_LEFT`.
*   **Directional Warps (Verified):** `WARP_CARPET_DOWN` (Requires pressing 'Down' to activate).
*   **Special Requirement (Verified):** `CUT_TREE` (Requires HM01 Cut), `BREAKABLE_ROCK` (Requires Rock Smash).
*   **Conditional Traversal (Verified):** `FLOOR_UP_WALL` (A one-way ledge, hoppable from the top).

### Tiles Under Investigation (High Priority)
*   **Special Requirement (Hypothesized):** `WATER` (Hypothesis: Requires HM03 Surf.), `WHIRLPOOL` (Requires HM), `HEADBUTT_TREE` (Hypothesis: Can be interacted with using the move Headbutt.)

## II. Core Principles & Lessons Learned

*   **Data Integrity is Paramount:** My internal state (notepad, markers) MUST be 100% accurate. I will not defer data correction. Assumptions must be rigorously tested before being recorded as fact.
*   **Trust Automation:** My custom tools are more reliable than my manual analysis. I must prioritize using them to avoid unforced errors.
*   **Act Immediately:** I am an LLM. There is no 'later'. Tool/agent refinement and data management tasks must be performed in the current turn, overriding gameplay actions.
*   **Scientific Method:** For all puzzles, I will strictly follow: Observe -> Hypothesize -> Test -> Conclude. I will document every step and attempt to falsify my own conclusions to avoid confirmation bias.

## III. Current Plans & Investigations

### Current Objective: Investigate the Lake of Rage
*   **Status:** Paused. The path is blocked by trainers on Route 43, indicating the solution is in Mahogany Town.
*   **Next Step:** Solve the Mahogany Mart puzzle to find the Team Rocket base, which should resolve the block on Route 43.

## IV. Puzzle Logs

### Mahogany Mart Puzzle Log
*   **Objective:** Find the secret Team Rocket entrance.
*   **Key Observation:** A Black Belt guard at (1, 6) disappears when I approach the bookshelf at (7, 1). He reappears if I move away from this area, which seems to reset the puzzle state.
*   **Hypothesis 1 (Invalidated):** The puzzle is a rapid, timed sequence. All attempts to interact with the warp tile (7, 3), the incense burner (6, 1), the pharmacist (4, 3), or the guard's original spot (1, 6) immediately after the guard disappears have failed because moving away from the bookshelf resets the puzzle. This entire line of reasoning is considered BUSTED.
*   **Hypothesis 2 (Invalidated):** The bookshelf event enables the warp at (7, 3). Attempts to activate the warp by standing on it, pressing 'A', or pressing 'Down' have all failed. This hypothesis is BUSTED.
*   **Hypothesis 3 (Invalidated):** The bookshelf event changes the state of the Pharmacist at (4, 3). **Test Result:** After triggering the bookshelf event, interacting with the Pharmacist only opens his regular shop menu. This hypothesis is BUSTED.
*   **Hypothesis 4 (Invalidated):** Interacting with the Black Belt at (1, 6) after the bookshelf event would open the passage. **Test Result:** The guard revealed he was Team Rocket and disappeared, but this did not activate the warp at (7, 3). This hypothesis is BUSTED.
*   **New Hypothesis (To Be Tested):** The true entrance is the Incense Burner at (6, 1). Interacting with it after the guard disappears will reveal the passage. **Test Plan:** 1. Complete the bookshelf and guard interaction sequence. 2. Go to (6, 2) and interact with the Incense Burner.

## V. Future Development Ideas

### Agent Ideas
*   **Repel Advisor:** An agent to recommend when to use a Repel based on party level and goal.
*   **Sequential Puzzle Agent:** An agent designed to solve state-dependent puzzles that require a specific, timed sequence of actions. This would be ideal for puzzles like the Mahogany Mart one.