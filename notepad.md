# Gem's Pokémon Crystal Notepad

## I. Game Systems & Mechanics

### Tile Traversal Protocol
- **Testing Mandate:** When a new, reachable tile type is seen, I MUST test it immediately.
- **Movement Test:** Attempt to move *into* and *out of* the tile from all 4 cardinal directions. Document results.
- **Interaction Test:** If movement fails, I must attempt to interact with the tile by facing it and pressing 'A'. Document results.
- **Ledge Test:** For any ledge-like tile, I must attempt to move against the apparent direction of the ledge to confirm if it is a one-way path. Document results.

### Verified Tile Types
*   **Impassable (Verified):** `WALL`, `PILLAR`, `BOOKSHELF`, `TV`, `RADIO`, `TOWN_MAP`, `STATUE`, `TABLE`, `CHAIR`, `BIRD` (Farfetch'd), `MART_SHELF`, `PC`, `LINK_CABLE`, `TRADE_MACHINE`, `INCENSE_BURNER`, `ROOF`, `CHIMNEY`, `SIGN`, `FLOWER`, `TREE_TOP`, `WATER_EDGE_UP`, `WATER_EDGE_DOWN`, `WATER_EDGE_LEFT`, `WATER_EDGE_RIGHT`, `VOID`, `COUNTER`, `FENCE`, `LINK_RECEPTIONIST`, `WEIRD_TREE`, `PRINTER`.
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

### Untested Tile Types & Plans
*   `WINDOW` (Tested & Impassable): These tiles are inaccessible behind walls.
*   `BUOY` (Untested): These appear in the water south of Olivine City.
    *   **Movement Test Plan:** Attempt to SURF onto a `BUOY` tile.

### Other Mechanics
*   **Object Impassability:** All Map Objects (NPCs, items, signs, etc.) are impassable.
*   **Haircuts:** Increases a Pokémon's happiness.

## II. Strategic Plans & Hypotheses

### Current Quest: The Sick Ampharos
*   **Goal:** Find the special medicine to cure the sick Ampharos in the Olivine Lighthouse.
*   **Verified Conclusion:** The way forward is not currently in the Lighthouse. I have exhausted all paths on 2F. The dialogue from the Gentleman NPC about needing 'ordinary medicine' not working strongly implies I must find a special cure elsewhere.
*   **Hypothesis 1:** The special medicine is located in a different town or route. I will need to travel to find it.
*   **Hypothesis 2:** The special medicine can be obtained from an NPC in Olivine City I have not yet spoken to, or whose dialogue has changed. I need to re-canvass the entire city.
*   **Hypothesis 3:** The sailor on the pier at (26, 27) has a clue, but my path to him has been repeatedly blocked. This might be an invisible wall or an event trigger. My plan is to try approaching from a different angle or after talking to every other NPC in the city.

### General Hypotheses & Verified Conclusions
*   **Conclusion:** The southern and western water routes in Union Cave B2F are isolated dead ends.
*   **Conclusion:** The southwestern part of Union Cave 1F is a dead end due to one-way ledges.
*   **Hypothesis (UNTESTED):** `HEADBUTT_TREE`s might be passable by using the move 'Headbutt' from the Pokémon party menu while facing the tree. Test requires a Pokémon with the move Headbutt.