# Gem's Pokémon Crystal Notepad

## I. Game Systems & Mechanics

### Tile Traversal Protocol
- **Testing Mandate:** When a new, reachable tile type is seen, I MUST test it immediately.
- **Movement Test:** Attempt to move *into* and *out of* the tile from all 4 cardinal directions. Document results.
- **Interaction Test:** If movement fails, I must attempt to interact with the tile by facing it and pressing 'A'. Document results.
- **Ledge Test:** For any ledge-like tile, I must attempt to move against the apparent direction of the ledge to confirm if it is a one-way path. Document results.

### Verified Tile Types
*   **Impassable (Verified):** `WALL`, `PILLAR`, `BOOKSHELF`, `TV`, `RADIO`, `TOWN_MAP`, `STATUE`, `TABLE`, `CHAIR`, `BIRD` (Farfetch'd), `MART_SHELF`, `PC`, `LINK_CABLE`, `TRADE_MACHINE`, `INCENSE_BURNER`, `ROOF`, `CHIMNEY`, `SIGN`, `FLOWER`, `TREE_TOP`, `WATER_EDGE_UP`, `WATER_EDGE_DOWN`, `WATER_EDGE_LEFT`, `WATER_EDGE_RIGHT`, `VOID`, `COUNTER`, `FENCE`, `LINK_RECEPTIONIST`, `WEIRD_TREE`, `PRINTER`, `BUOY`, `WINDOW`.
*   **Traversable (Verified):** `FLOOR`, `GRASS`, `TALL_GRASS`, `LONG_GRASS`, `RAILING`, `PIPE_HORIZONTAL`, `PIPE_VERTICAL`, `CUT_TREE` (becomes traversable after using CUT).
*   **Warps (Verified):** `DOOR`, `CAVE`, `LADDER`, `STAIRCASE` (Move onto tile), `PIT` (Acts as a one-way warp when stepped on).
*   **One-Way Ledges (Verified):**
    *   `LEDGE_HOP_DOWN`: A one-way ledge that can only be hopped **DOWN**.
    *   `LEDGE_HOP_DOWN/RIGHT`: A one-way ledge that can only be hopped in the specified direction.
    *   `LEDGE_HOP_LEFT`: A one-way ledge that can only be hopped **LEFT**.
    *   `FLOOR_UP_WALL`: A complex one-way ledge. Can move **UP** from `FLOOR` to `FLOOR_UP_WALL`. Can move **DOWN** from `FLOOR_UP_WALL` to `FLOOR` (the jump). Cannot move **DOWN** from `FLOOR` to `FLOOR_UP_WALL`.
*   **Special Requirement (Verified):**
    *   `WATER` (Requires HM03 Surf, must be used from adjacent `FLOOR` tile).
    *   `BREAKABLE_ROCK` (Requires Rock Smash).
*   **Complex Tiles (Verified):**
    *   `WARP_CARPET_DOWN/LEFT/RIGHT`: Traversable. Activated by pressing the corresponding direction while standing on the tile to trigger a warp.
    *   `WARP_CARPET_DOWN`: Traversable. Activated by pressing 'Down' while standing on the tile to trigger a warp.
    *   `WARP_CARPET_LEFT`: Traversable. Activated by pressing 'Left' while standing on the tile to trigger a warp.

### Other Mechanics
*   **Object Impassability:** All Map Objects (NPCs, items, signs, etc.) are impassable.
*   **Haircuts:** Increases a Pokémon's happiness.

## II. Strategic Plans & Hypotheses

### Current Quest: The Sick Ampharos
*   **Goal:** Find the special medicine to cure the sick Ampharos in the Olivine Lighthouse.
*   **Current Hypothesis:** The special medicine is located in a new town across the sea to the west of Olivine, accessible via SURF.
*   **Alternative Hypothesis 1:** The medicine is in a location I've already visited, but is now accessible because of a story trigger I've completed. I should check with key NPCs in Ecruteak and Goldenrod.
*   **Alternative Hypothesis 2:** The medicine is not an item, but a person I need to talk to in an area I haven't fully explored, like southern Route 39.

### Verified Conclusions
*   The way forward is not currently in the Olivine Lighthouse. I have exhausted all paths.
*   The sailor on the pier in Olivine City has no new information about the special medicine.
*   The southern and western water routes in Union Cave B2F are isolated dead ends.
*   The southwestern part of Union Cave 1F is a dead end due to one-way ledges.
*   `HEADBUTT_TREE`s might be passable by using the move 'Headbutt'. (Requires testing).