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
*   **Directional Warps (Verified):** `WARP_CARPET_DOWN`, `WARP_CARPET_LEFT`, `WARP_CARPET_RIGHT` (Requires pressing in the indicated direction to activate).
*   **Special Requirement (Verified):** 
    *   `CUT_TREE` (Requires HM01 Cut).
    *   `BREAKABLE_ROCK` (Requires Rock Smash).
*   **Conditional Traversal (Verified):**
    *   `FLOOR_UP_WALL`: This tile's function varies. It can be a one-way ledge (hoppable from the top) or completely impassable, as observed on Route 42's northern path. Verification is required for each instance.

### Tiles Under Investigation (High Priority)
*   **Special Requirement (Hypothesized):**
    *   `WATER` (Hypothesis: Requires HM03 Surf. Must be activated from the overworld by facing the water and pressing 'A'.)
    *   `WHIRLPOOL` (Requires HM).
    *   `HEADBUTT_TREE` (Hypothesis: Can be interacted with using the move Headbutt.)

## II. Core Principles & Lessons Learned

*   **Data Integrity is Paramount:** My internal state (notepad, markers) MUST be 100% accurate. I will not defer data correction. Assumptions must be rigorously tested before being recorded as fact.
*   **Trust Automation:** My custom tools are more reliable than my manual analysis. I must prioritize using them to avoid unforced errors.
*   **Act Immediately:** I am an LLM. There is no 'later'. Tool/agent refinement and data management tasks must be performed in the current turn, overriding gameplay actions.
*   **Scientific Method:** For all puzzles, I will strictly follow: Observe -> Hypothesize -> Test -> Conclude. I will document every step and attempt to falsify my own conclusions to avoid confirmation bias.

## III. Current Plans & Investigations

### Current Objective: Investigate the Lake of Rage
*   **Status:** In progress.
*   **Reasoning:** The Olivine Lighthouse proved to be a dead end. Multiple NPCs have mentioned a "rampage" or "conspiracy" at the Lake of Rage, which is a strong indicator of the main story path.
*   **Current Plan:** Travel from Ecruteak City towards Mahogany Town. The northern path on Route 42 is a dead end. The only viable path appears to be through one of the Mt. Mortar caves to cross to the southern part of the route.

## IV. Archived Investigations

### Investigation: The Missing HM02 (Fly)
*   **Status:** On hold. Priority is the Lake of Rage.
*   **Anomaly:** After defeating Gym Leader Chuck, his wife gave me HM02 (Fly). However, the HM is not in my bag.
*   **Verification Plan:** After dealing with the Lake of Rage, travel to Cianwood City and speak to Chuck's wife again.

### Investigation: The Battle Tower
*   **Status:** Complete. The Battle Tower is a self-contained loop with no key items or story progression elements. No further investigation is warranted.

### Investigation: Olivine Lighthouse
*   **Status:** Complete (for now). Exhausted all paths, pits, and trainers on all floors. Concluded that progression is not possible at this time and is likely gated behind another story event.

## V. Future Development Ideas

### Agent Ideas
*   **Repel Advisor:** An agent to recommend when to use a Repel based on party level, current location, and goal (e.g., training vs. exploration).

### Tool Ideas
*   **Unseen Tile Scanner:** A tool to scan the `map_xml_string` and return a list of all unseen tile coordinates (`❓`). This would help ensure systematic exploration of each map.

### Test Plans
*   **Mt. Mortar Waterfall:** After acquiring the `Waterfall` HM, I must return to Mt. Mortar to test if I can climb the waterfalls. This will confirm or deny my hypothesis that it is a completely optional area.