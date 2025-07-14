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
*   **Key Observation:** A Black Belt (BB) guard at (1, 6) disappears when I approach the area near the bookshelf at (7, 1). He reappears if I move away from this area, confirming the solution is localized.
*   **Current Working Sequence:**
    1. Stand at (7, 2) to make the BB disappear.
    2. Face and interact with the bookshelf at (7, 1). This triggers a scripted screen-flash event.
*   **Current Blockage:** After the screen-flash, no obvious path opens. The warp tile at (7, 3) remains inactive. Moving away from the area resets the puzzle.
*   **Failed Hypotheses Log:**
    - The Pharmacist at (4, 3) is the next step. (Failed: Moving to him resets the puzzle).
    - The incense burner at (6, 1) is a direct switch. (Failed: No effect).
    - The bookshelf at (7, 1) is a direct switch. (Failed: No effect without the BB trigger).
    - The warp tile at (7, 3) is a direct trigger. (Failed: Stepping on it or interacting with it while facing Down, Up, or Left does nothing, even after the bookshelf event).
    - The BB's original spot at (1, 6) is a pressure plate. (Failed: Moving there resets the puzzle).
*   **Failed Hypothesis Log (cont.):** The warp tile at (7, 3) is the trigger. (Failed: Tested interacting with the tile after the bookshelf event while facing Down, Up, Left, and Right. None of these actions triggered the warp, and moving away resets the puzzle. This hypothesis is now fully invalidated.)
*   **Next Hypothesis:** The sequence is `Trigger BB disappearance -> Interact with Bookshelf -> Interact with Incense Burner (6, 1)`. The incense burner might become an active switch only after the bookshelf event.

## V. Future Development Ideas

### Agent Ideas
*   **Repel Advisor:** An agent to recommend when to use a Repel based on party level and goal.
*   **Sequential Puzzle Agent:** An agent designed to solve state-dependent puzzles that require a specific, timed sequence of actions.