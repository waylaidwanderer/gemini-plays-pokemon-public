# Gem's Pokémon Crystal Notepad

## I. Game Systems & Mechanics

### Tile Traversal Protocol
- **Testing Mandate:** When a new, reachable tile type is seen, I MUST test it immediately.
- **Movement Test:** Attempt to move *into* and *out of* the tile from all 4 cardinal directions to verify passability.
- **Ledge Test:** For any ledge-like tile, I must attempt to move up/against the apparent direction of the ledge to confirm if it is a one-way path.

### Verified Tile Types
*   **Impassable:** `WALL`, `HEADBUTT_TREE`, `PC`, `PILLAR`, `BOOKSHELF`, `TV`, `RADIO`, `TOWN_MAP`, `WINDOW`, `STATUE`, `TABLE`, `CHAIR`, `BIRD` (Farfetch'd), `CUT_TREE`, `COUNTER`, `VOID`, `MART_SHELF`
*   **Traversable:** `FLOOR`, `GRASS`, `TALL_GRASS` (Wild Encounters)
*   **Warps:** `DOOR`, `CAVE`, `LADDER`, `STAIRCASE` (Move onto tile). Gatehouse warps are triggered by walking into the building side.
*   **One-Way Ledges:** `LEDGE_HOP_DOWN/LEFT/RIGHT`. Verified by attempting to move against the ledge direction.
*   **Complex Tiles:**
    * `FLOOR_UP_WALL`: Can be entered from the side (from a FLOOR tile). Cannot be exited by moving up. Further testing required.
    * `WARP_CARPET_DOWN`: Currently non-functional. Extensive testing by stepping on it from all directions and pressing 'A' has yielded no results. Likely requires an external trigger or key item.

### Untested Tile Types (High Priority)
* `RAILING`: Needs testing. Located on the Goldenrod Dept. Store Roof.
* `PIPE_HORIZONTAL`: Needs testing.
* `PIPE_VERTICAL`: Needs testing.
* `WATER`: Needs testing.

### Other Mechanics
*   **Item Effects:**
    *   **BERRY:** Restores 10 HP. Found at `FRUIT_TREE`s.
    *   **EVERSTONE:** Prevents evolution.
    *   **MOOMOO MILK:** Restores 100 HP. Purchased at MOOMOO FARM.
*   **SLOWPOKETAIL:** Offered for sale on Route 32. Purpose unknown.
*   **Vending Machine Drinks:** Can refresh tired POKéMON.
*   **Hidden Items:** Must be interacted with from an adjacent tile, not by standing on the item's tile. Exact orientation might matter.
*   **Haircuts:** Getting a haircut from the brothers in the Goldenrod Underground increases a Pokémon's happiness.

## II. Key Items, HMs, & TMs
*   **HM01 (CUT):** Clears small trees. Requires the Hive Badge. Taught to SUNDEW.
*   **TM49 (Fury Cutter):** Gets stronger with each consecutive hit.
*   **COIN CASE:** Allows playing at the Game Corner. Found in the Goldenrod Underground.

## III. Active Puzzles & Hypotheses

### Goldenrod City
*   **Fact (from Agent):** The path east out of Goldenrod City is blocked by a strange tree (Sudowoodo). Progress is impossible this way for now.
*   **Hypothesis:** An Abra is required for the Machop trade on the 5th floor of the Department Store. Abra might be found in the grass on Route 34, which is south of the city.

### Ruins of Alph
*   **Objective:** Solve the sliding stone panel puzzle.
*   **Clue:** Liz mentioned hearing a strange radio broadcast from the Ruins of Alph. This might be a clue.

### Goldenrod Magnet Train Station
* **Objective:** Explore the station.
* **Status:** The Officer who was blocking the path north has disappeared.
* **Current Investigation:** Systematically testing the `FLOOR_UP_WALL` tile type to understand its traversal mechanics.
    *   **Test 1:** Moved from `FLOOR` (8, 12) to `FLOOR_UP_WALL` (7, 12). **Result: Success.**
    *   **Test 2:** Attempted to move from `FLOOR_UP_WALL` (7, 12) to `FLOOR` (7, 11). **Result: Failure.**
    *   **Conclusion:** Cannot exit this tile by moving up.
    *   **Next Step:** Test moving down, left, and right from the tile.

## IV. Tool & Agent Development
### Core Directives
*   I must act on tool/notepad management tasks IMMEDIATELY.
*   I must mark moving objects using their `object_id`.
*   I will use `quest_strategist` for future complex puzzles.
*   I will use `nickname_genius` the next time I catch a Pokémon.