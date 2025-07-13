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
*   **Special Requirement (Verified):** 
    *   `CUT_TREE` (Requires HM01 Cut).
    *   `BREAKABLE_ROCK` (Requires Rock Smash).
    *   `WATER` (Requires HM03 Surf, activated from party menu. Landing from SURF requires an adjacent, unobstructed FLOOR tile).
    *   Directional Warps (Requires pressing in the indicated direction to activate): WARP_CARPET_DOWN, WARP_CARPET_LEFT, WARP_CARPET_RIGHT.
*   **Special Requirement (Hypothesized):** `WHIRLPOOL` (Requires HM).

### Tiles Under Investigation (High Priority)
*   `FLOOR_UP_WALL`: Attempting to move south from a `FLOOR` tile at (27, 45) onto this tile at (27, 46) failed. Hypothesis: This is a one-way ledge that can only be hopped **DOWN** (south). Test required: Find a path to the upper level to test jumping down.

## II. Core Principles & Lessons Learned

*   **Data Integrity is Paramount:** My internal state (notepad, markers) MUST be 100% accurate. I will not defer data correction. Assumptions must be rigorously tested before being recorded as fact.
*   **Trust Automation:** My custom tools are more reliable than my manual analysis. I must prioritize using them to avoid unforced errors.
*   **Act Immediately:** I am an LLM. There is no 'later'. Tool/agent refinement and data management tasks must be performed in the current turn, overriding gameplay actions.
*   **Scientific Method:** For all puzzles, I will strictly follow: Observe -> Hypothesize -> Test -> Conclude. I will document every step and attempt to falsify my own conclusions to avoid confirmation bias.

## III. Current Plans & Investigations

### Current Objective: Investigate the Lake of Rage
*   **Status:** In progress.
*   **Reasoning:** The Olivine Lighthouse proved to be a dead end. Multiple NPCs have mentioned a "rampage" or "conspiracy" at the Lake of Rage, which is a strong indicator of the main story path.
*   **Current Plan:** Travel from Olivine City towards Mahogany Town to reach the Lake of Rage.
*   **Alternative Hypothesis:** If the Lake of Rage is a side quest and does not unlock the path to the SECRETMEDICINE, I will need to systematically re-explore all previous routes for obstacles that can now be overcome with my current abilities (e.g., SURF).

## IV. Archived Investigations

### Investigation: The Missing HM02 (Fly)
*   **Status:** On hold. Priority is the Lake of Rage.
*   **Anomaly:** After defeating Gym Leader Chuck, his wife gave me HM02 (Fly). However, the HM is not in my bag.
*   **Verification Plan:** After dealing with the Lake of Rage, travel to Cianwood City and speak to Chuck's wife again.

### Investigation: The Battle Tower
*   **Status:** Complete. The Battle Tower is a self-contained loop with no key items or story progression elements. No further investigation is warranted.

### Investigation: Olivine Lighthouse
*   **Status:** Complete (for now). Exhausted all paths, pits, and trainers on all floors. Concluded that progression is not possible at this time and is likely gated behind another story event.