# Gem's Pokémon Crystal Notepad

## I. Game Systems & Mechanics

### Tile Traversal Protocol
- **Testing Mandate:** When a new, reachable tile type is seen, I MUST test it immediately.
- **Movement Test:** Attempt to move *into* and *out of* the tile from all 4 cardinal directions.
- **Interaction Test:** If movement fails, I must attempt to interact with the tile by facing it and pressing 'A'.
- **Ledge Test:** For any ledge-like tile, I must attempt to move up/against the apparent direction of the ledge to confirm if it is a one-way path.

### Verified Tile Types
*   **Impassable:** `WALL`, `PILLAR`, `BOOKSHELF`, `TV`, `RADIO`, `TOWN_MAP`, `STATUE`, `TABLE`, `CHAIR`, `BIRD` (Farfetch'd), `MART_SHELF`, `BUOY`, `PC`, `LINK_CABLE`, `TRADE_MACHINE`, `INCENSE_BURNER`, `ROOF`, `CHIMNEY`, `SIGN`, `FLOWER`, `TREE_TOP`, `WATER_EDGE_UP`, `WATER_EDGE_DOWN`, `WATER_EDGE_LEFT`, `WATER_EDGE_RIGHT`, `VOID`, `COUNTER`, `FENCE`, `LINK_RECEPTIONIST`, `WINDOW`, `WEIRD_TREE`, `PRINTER`.
*   **Traversable:** `FLOOR`, `GRASS`, `TALL_GRASS`, `LONG_GRASS`, `RAILING`, `PIPE_HORIZONTAL`, `PIPE_VERTICAL`, `CUT_TREE` (becomes traversable after using CUT).
*   **Warps:** `DOOR`, `CAVE`, `LADDER`, `STAIRCASE` (Move onto tile), `PIT` (Acts as a warp when stepped on).
*   **One-Way Ledges:**
    *   `LEDGE_HOP_DOWN`: A one-way ledge that can only be hopped **DOWN**.
    *   `LEDGE_HOP_DOWN/RIGHT`: A one-way ledge that can only be hopped in the specified direction.
    *   `LEDGE_HOP_LEFT`: A one-way ledge that can only be hopped **LEFT**.
    *   `FLOOR_UP_WALL`: A complex one-way ledge. Can move **UP** from `FLOOR` to `FLOOR_UP_WALL`. Can move **DOWN** from `FLOOR_UP_WALL` to `FLOOR` (the jump). Cannot move **DOWN** from `FLOOR` to `FLOOR_UP_WALL`.
*   **Special Requirement:**
    *   `WATER` (Requires HM03 Surf).
    *   `BREAKABLE_ROCK` (Requires Rock Smash).
*   **Complex Tiles:**
    *   `WARP_CARPET_DOWN/LEFT/RIGHT`: Traversable. Activated by pressing the corresponding direction while standing on the tile to trigger a warp.
    *   `WARP_CARPET_DOWN`: Traversable. Activated by pressing 'Down' while standing on the tile to trigger a warp.

### Other Mechanics
*   **Object Impassability:** All Map Objects (NPCs, items, signs, etc.) are impassable.
*   **Item Effects:**
    *   **BERRY:** Restores 10 HP.
    *   **MINT BERRY:** Cures sleep.
    *   **EVERSTONE:** Prevents evolution.
    *   **MOOMOO MILK:** Restores 100 HP.
    *   **HARD STONE:** Powers up rock-type moves.
    *   **PRZCUREBERRY:** Cures paralysis.
    *   **HYPER POTION:** Restores 200 HP.
    *   **ICE BERRY:** Heals burn.
*   **Haircuts:** Increases a Pokémon's happiness.

## II. Blocked Paths & Story Gates
*   **Route 37 Trainer Blockade:** Twins Ann & Anne disguised as trees block the path north at (6, 12) and (7, 12).
*   **Goldenrod Underground Blockade:** A Super Nerd blocks the path south at (5, 31).
*   **Ilex Forest Blockade:** A `HEADBUTT_TREE` at (9, 26) blocks the path. Needs further testing.

## III. Strategic Plans & Hypotheses

### Primary Goal: Travel to Cianwood City to get the SecretPotion.
1.  **Exit Ilex Forest** via the northern exit to Route 34.
2.  **Travel through Goldenrod City** to reach Route 35.
3.  **Navigate north** through Route 35, the National Park, and Route 36.
4.  **Continue to Ecruteak City** via Route 37.
5.  **Go west from Ecruteak City** through Route 38 and 39 to reach Olivine City.
6.  **Surf west from Olivine City** across Route 40 and 41 to reach Cianwood City.

### Secondary Goal: Defeat the Olivine City Gym Leader
*   **Status:** Blocked. Requires healing the sick Ampharos in the Olivine Lighthouse with the SecretPotion from Cianwood City.

### Tertiary Goal: Heal the Miltank on Route 39
*   **Status:** On hold. Requires backtracking for BERRIES, and the primary goal is more critical.

### Hypotheses & Verified Conclusions
*   **Conclusion:** The southern and western water routes in Union Cave B2F are isolated dead ends.
*   **Conclusion:** The southwestern part of Union Cave 1F is a dead end due to one-way ledges.
*   **Conclusion:** The `CUT_TREE` tile at (8, 25) was not permanently impassable. Interacting with it again with 'A' allowed me to use CUT.
*   **Hypothesis (NEW):** `HEADBUTT_TREE`s might be passable by using the move 'Headbutt' from the Pokémon party menu while facing the tree, not just by interacting with 'A'.