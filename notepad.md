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
*   **Directional Warps:** `WARP_CARPET_LEFT`, `WARP_CARPET_DOWN`. Verified one-way; can only be entered by moving in the specified direction.
*   **One-Way Ledges:** `LEDGE_HOP_DOWN/LEFT/RIGHT`. Verified by attempting to move against the ledge direction.
*   **Complex Tiles:** `FLOOR_UP_WALL` (Verified: Enter by moving UP; Exit by moving LEFT/RIGHT).

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

## II. Key Items, HMs, & TMs
*   **HM01 (CUT):** Clears small trees. Requires the Hive Badge. Taught to SUNDEW.
*   **TM49 (Fury Cutter):** Gets stronger with each consecutive hit.
*   **COIN CASE:** Allows playing at the Game Corner. Lost by a man in the Goldenrod Underground.

## III. Active Puzzles & Hypotheses

### Goldenrod Underground Switch Room
*   **Objective:** Find a way to the eastern section of the underground.
*   **Hypothesis 1 (Failed):** A single switch press on one of the three objects on the north wall (18,23), (20,23), or (22,23) is the solution.
    *   **Test:** Interacted with all three objects individually. 
    *   **Conclusion:** None of the objects reacted. This hypothesis is incorrect.
*   **Hypothesis 2 (Current):** The puzzle requires pressing the switches in a specific sequence.
    *   **Next Step:** Finish testing the simplest sequence: Left (18,23), then Middle (20,23), then Right (22,23). If that fails, use the new `puzzle_solver` agent to generate more sequences.
*   **Alternative Hypothesis:** The solution does not involve these switches, but a hidden passage or item elsewhere.

### Goldenrod City
*   **Fact (from Agent):** The path east out of Goldenrod City is blocked by a strange tree (Sudowoodo). Progress is impossible this way for now.
*   **Hypothesis:** An Abra is required for the Machop trade on the 5th floor of the Department Store. Abra might be found in the grass on Route 34, which is south of the city.

### Ruins of Alph
*   **Objective:** Solve the sliding stone panel puzzle.
*   **Clue:** Liz mentioned hearing a strange radio broadcast from the Ruins of Alph. This might be a clue.

## IV. Tool & Agent Development
### Core Directives
*   I must act on tool/notepad management tasks IMMEDIATELY.
*   I must mark moving objects using their `object_id`.
*   I MUST use the `nickname_genius` agent the next time I catch a Pokémon to test its functionality.
*   I will use the new `puzzle_solver` agent to generate sequences for the Goldenrod Underground switch puzzle if my initial sequence test fails.

## V. Phone Contacts
*   **TODD (CAMPER):** Calls about sales at the Goldenrod Department Store.
*   **JOEY (YOUNGSTER):** Calls about his top-percentage RATTATA.
*   **LIZ (PICNICKER):** Gives gameplay tips.
*   **RALPH (FISHER):** Calls about his fishing exploits.