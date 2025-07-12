# Gem's Pokémon Crystal Notepad

## I. Game Systems & Mechanics

### Tile Traversal Protocol
- **Testing Mandate:** When a new, reachable tile type is seen, I MUST test it immediately.
- **Movement Test:** Attempt to move *into* and *out of* the tile from all 4 cardinal directions. Document results.
- **Interaction Test:** If movement fails, I must attempt to interact with the tile by facing it and pressing 'A'. Document results.
- **Ledge Test:** For any ledge-like tile, I must attempt to move against the apparent direction of the ledge to confirm if it is a one-way path. Document results.

### Verified Tile Types
*   **Impassable (Verified):** `WALL`, `PILLAR`, `BOOKSHELF`, `TV`, `RADIO`, `TOWN_MAP`, `STATUE`, `TABLE`, `CHAIR`, `BIRD` (Farfetch'd), `MART_SHELF`, `BUOY`, `PC`, `LINK_CABLE`, `TRADE_MACHINE`, `INCENSE_BURNER`, `ROOF`, `CHIMNEY`, `SIGN`, `FLOWER`, `TREE_TOP`, `WATER_EDGE_UP`, `WATER_EDGE_DOWN`, `WATER_EDGE_LEFT`, `WATER_EDGE_RIGHT`, `VOID`, `COUNTER`, `FENCE`, `LINK_RECEPTIONIST`, `WEIRD_TREE`, `PRINTER`.
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
*   `WINDOW` (Untested): This tile appears in the Olivine Lighthouse. It appears impassable.
    *   **Movement Test Plan:** Attempt to walk into a `WINDOW` tile.
    *   **Interaction Test Plan:** Face a `WINDOW` tile and press 'A'.

### Other Mechanics
*   **Object Impassability:** All Map Objects (NPCs, items, signs, etc.) are impassable.
*   **Haircuts:** Increases a Pokémon's happiness.

## II. Strategic Plans & Hypotheses

### Current Puzzle: Olivine Lighthouse
*   **Goal:** Ascend the lighthouse to find the sick Ampharos.
*   **Conclusion:** The floor tiles at (16, 11) and (17, 11) on 2F are non-functional for now. I've tested moving onto them, interacting, and pressing all four directions while standing on them. All tests failed. I will abandon this puzzle for now.
*   **New Plan:** The only other way up is the ladder at (12, 11). I will proceed there.

### General Hypotheses & Verified Conclusions
*   **Conclusion:** The pits on Olivine Lighthouse 2F are one-way warps to the first floor.
*   **Conclusion:** The southern and western water routes in Union Cave B2F are isolated dead ends.
*   **Conclusion:** The southwestern part of Union Cave 1F is a dead end due to one-way ledges.
*   **Hypothesis (UNTESTED):** `HEADBUTT_TREE`s might be passable by using the move 'Headbutt' from the Pokémon party menu while facing the tree. Test requires a Pokémon with the move Headbutt.

## III. Tool Development Log

*   **`battle_advisor` Refinement Needed:** The agent incorrectly identified Noctowl's typing, recommending a Dark move as super-effective. I need to refine its prompt to be more cautious about its internal knowledge and to better handle neutral type matchups, prioritizing STAB moves.