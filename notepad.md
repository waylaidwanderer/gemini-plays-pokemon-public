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
    * `FLOOR_UP_WALL` (Under Re-evaluation): Overwatch critique noted my documentation is flawed. This tile appears to be the benches in the train station. My previous tests were inconclusive. I will now conduct a thorough test of movement on, off, and between these tiles from all directions to create an accurate entry.
    * `WARP_CARPET_DOWN` (Verified: Currently non-functional. Extensive testing by stepping on it from all directions and pressing 'A' has yielded no results. Likely requires an external trigger or key item.)

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
* **Objective:** Escape the station.
* **Clue:** An Officer is blocking the path north and mentions the train isn't running. His presence is scripted (he appears and disappears).
* **Failed Hypotheses:**
    1. Waiting for a time-based event. (Failed after multiple turns of waiting).
    2. Saving and reloading the game. (Failed, no change in state).
    3. Using the `WARP_CARPET_DOWN` exit. (Failed, warp is non-functional).
    4. Interacting with unique objects (plant). (Failed, non-interactable).
* **Current Hypothesis:** There is a hidden, non-obvious trigger tile in the room. A full systematic search is in progress.
* **Alternative Hypothesis:** A key item, like a "Train Pass," is required from another location.

## IV. Tool & Agent Development
### Core Directives
*   I must act on tool/notepad management tasks IMMEDIATELY.
*   I must mark moving objects using their `object_id`.
*   I will use `quest_strategist` for future complex puzzles.
*   I will use `nickname_genius` the next time I catch a Pokémon.