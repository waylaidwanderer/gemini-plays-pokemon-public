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
*   **Status:** Believed to be accessible via Route 43. The path was previously blocked by trainers, but solving the puzzle in the Mahogany Mart is hypothesized to have cleared this blockage.
*   **Next Step:** Proceed to the gate at Mahogany Town (9, 1) and travel north onto Route 43 to test this hypothesis.

## IV. Puzzle Logs

### Mahogany Mart Puzzle Log
*   **Objective:** Find the secret Team Rocket entrance.
*   **Key Discovery:** The puzzle is a sequence of events. 1) Approaching the bookshelf at (7, 1) causes a Black Belt guard at (1, 6) to disappear. 2) Interacting with the bookshelf triggers a scripted event. 3) Interacting with the Black Belt guard at (1, 6) after the bookshelf event causes him to reveal he is Team Rocket and then vanish.
*   **Hypothesis 1 (Invalidated):** The secret entrance is the warp at (7, 3). **Test Result:** All attempts to activate the warp after the sequence failed.
*   **Hypothesis 2 (Invalidated):** The Pharmacist at (4, 3) is involved. **Test Result:** His dialogue and function remain unchanged.
*   **Hypothesis 3 (Invalidated):** The Incense Burner at (6, 1) is the switch. **Test Result:** It only produces flavor text.
*   **Hypothesis 4 (Invalidated):** The puzzle opens the path to the Mahogany Gym. **Test Result:** The Fisher at (6, 14) remains, blocking the path.
*   **Final Conclusion:** The puzzle's purpose is not to open a passage *inside* the mart or to the gym. Its completion must have triggered an event elsewhere, most likely clearing the path on Route 43.

## V. Future Development Ideas

### Agent Ideas
*   **Repel Advisor:** An agent to recommend when to use a Repel based on party level and goal.
*   **Sequential Puzzle Agent:** An agent designed to solve state-dependent puzzles that require a specific sequence of actions. This will be created this turn.