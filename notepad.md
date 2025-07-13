# Gem's Pokémon Crystal Notepad

## I. Game Systems & Mechanics

### Tile Traversal Protocol
*   **Testing Mandate:** When a new, reachable tile type is seen, I MUST test it immediately.
*   **Movement Test:** Attempt to move *into* and *out of* the tile from all 4 cardinal directions.
*   **Interaction Test:** If movement fails, I must attempt to interact with the tile by facing it and pressing 'A'.
*   **Ledge Test:** For any ledge-like tile, I must attempt to move against the apparent direction of the ledge to confirm if it is a one-way path.

### Verified Tile Types
*   **Impassable (Verified):** `WALL`, `PILLAR`, `BOOKSHELF`, `TV`, `RADIO`, `TOWN_MAP`, `TABLE`, `CHAIR`, `BIRD`, `MART_SHELF`, `PC`, `LINK_CABLE`, `TRADE_MACHINE`, `INCENSE_BURNER`, `ROOF`, `CHIMNEY`, `SIGN`, `FLOWER`, `TREE_TOP`, `WATER_EDGE_UP`, `WATER_EDGE_DOWN`, `WATER_EDGE_LEFT`, `WATER_EDGE_RIGHT`, `VOID`, `COUNTER`, `FENCE`, `LINK_RECEPTIONIST`, `WEIRD_TREE`, `PRINTER`, `BUOY`, `ROCK`.
*   **Traversable (Verified):** `GRASS`, `TALL_GRASS`, `LONG_GRASS`, `RAILING`, `PIPE_HORIZONTAL`, `PIPE_VERTICAL`, `FLOOR`.
*   **Warps (Verified):** `DOOR`, `CAVE`, `LADDER`, `STAIRCASE`, `PIT` (One-way), `WARP_CARPET_DOWN` (Requires pressing 'Down' while standing on tile).
*   **One-Way Ledges (Verified):** `LEDGE_HOP_DOWN`, `LEDGE_HOP_DOWN/RIGHT`, `LEDGE_HOP_LEFT`.
*   **Special Requirement (Verified):** `CUT_TREE` (Requires HM01 Cut), `BREAKABLE_ROCK` (Requires Rock Smash), `WATER` (Requires HM03 Surf, which must be activated manually from the Pokémon's move list in the party menu when used for traversal).
*   **Special Requirement (Hypothesized):** `WHIRLPOOL` (Requires HM).

### Tiles Under Investigation (High Priority)
*   `FLOOR_UP_WALL`: Attempting to move south from a `FLOOR` tile at (27, 45) onto this tile at (27, 46) failed. Hypothesis: This is a one-way ledge that can only be hopped **DOWN** (south). Test required: Find a path to the upper level to test jumping down.

## II. Core Principles & Lessons Learned

*   **Data Integrity is Paramount:** My internal state (notepad, markers) MUST be 100% accurate. I will not defer data correction. Assumptions must be rigorously tested before being recorded as fact.
*   **Trust Automation:** My custom tools (`pathfinder`, `boulder_scanner`) are more reliable than my manual navigation and analysis. I must prioritize using them to avoid unforced errors.
*   **Act Immediately:** I am an LLM. There is no 'later'. Tool/agent refinement and data management tasks must be performed in the current turn, overriding gameplay actions.
*   **Scientific Method:** For all puzzles, I will strictly follow: Observe -> Hypothesize -> Test -> Conclude. I will document every step and attempt to falsify my own conclusions to avoid confirmation bias.

## III. Current Plans & Investigations

### Current Objective: Obtain SECRETMEDICINE
*   **Status:** In progress. Cianwood City has been confirmed as a dead end.
*   **Goal:** Obtain the SECRETMEDICINE for the sick Ampharos in the Olivine Lighthouse.
*   **Current Plan:** All leads in Cianwood City have been exhausted. The Pharmacist did not have the SECRETMEDICINE, and multiple NPCs had bugged/unhelpful dialogue. My new plan is to return to Olivine City and re-investigate the Lighthouse and surrounding areas for clues.
*   **Alternative Hypothesis:** If the re-investigation of Olivine City fails, it's possible that I must first resolve the events at the Lake of Rage (near Mahogany Town) to trigger the availability of the SECRETMEDICINE.

## IV. Archived Investigations

### Investigation: The Missing HM02 (Fly)
*   **Status:** Investigation on hold. Current priority is obtaining the SECRETMEDICINE.
*   **Anomaly:** After defeating Gym Leader Chuck, his wife gave me HM02 (Fly). However, the HM is not in my bag.
*   **Hypothesis:** This was a misunderstood event, a temporary item, or a game bug.
*   **Verification Plan:** After dealing with the Olivine Lighthouse, travel to Cianwood City and speak to Chuck's wife again.

### Investigation: The Battle Tower
*   **Status:** Investigation complete. The Battle Tower appears to be a self-contained loop with no key items or story progression elements. All warps lead back to the gatehouse or the exterior area. No further investigation is warranted at this time.
*   **Warp (FLOOR):** Does not activate with 'A'. Pressing 'Down' while standing on the tile moves the player one tile down. Observed at Olivine Lighthouse 2F (16, 11).