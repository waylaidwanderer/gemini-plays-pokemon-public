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
*   **Directional Warps (Verified):**
    *   `WARP_CARPET_DOWN`: Requires pressing 'Down' to activate.
*   **Special Requirement (Verified):** 
    *   `CUT_TREE` (Requires HM01 Cut).
    *   `BREAKABLE_ROCK` (Requires Rock Smash).
*   **Conditional Traversal (Verified):**
    *   `FLOOR_UP_WALL`: A one-way ledge, hoppable from the top. My test on Route 42 confirmed this.

### Tiles Under Investigation (High Priority)
*   **Special Requirement (Hypothesized):**
    *   `WATER` (Hypothesis: Requires HM03 Surf.)
    *   `WHIRLPOOL` (Requires HM).
    *   `HEADBUTT_TREE` (Hypothesis: Can be interacted with using the move Headbutt.)

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
*   **Key Observation:** A Black Belt (BB) guard at (1, 6) disappears when I approach the bookshelf at (7, 1). He reappears if I move too far away, confirming the solution is localized and likely timed.
*   **Current Hypothesis:** The bookshelf at (7, 1) becomes an interactable switch *only after* the BB has vanished.
*   **Test Plan:** 
    1. Move to (7, 2) to trigger the BB's disappearance.
    2. Immediately face the bookshelf at (7, 1) and press 'A'.
*   **Alternative Hypotheses (If current fails):**
    1. The trigger is external. After the BB vanishes, an NPC's dialogue in Mahogany Town might change, providing the next clue.
    2. The trigger is item-based. An item in my inventory needs to be used.
*   **Failed Hypotheses Log:**
    1. The Pharmacist is the trigger. (Failed: He's a normal shopkeeper, and moving to him resets the puzzle).
    2. The incense burner or bookshelf are direct switches. (Failed: They only provide flavor text without the BB trigger).
    3. The warp tile at (7, 3) is the trigger. (Failed: Stepping on it and interacting does nothing).
    4. The BB's original spot (1, 6) is a pressure plate. (Failed: Moving there resets the puzzle).

## V. Future Development Ideas

### Agent Ideas
*   **Repel Advisor:** An agent to recommend when to use a Repel based on party level and goal.
*   **Sequential Puzzle Agent:** An agent designed to solve state-dependent puzzles that require a specific, timed sequence of actions.