# Gem's Pokémon Crystal Notepad

## I. Game Systems & Mechanics

### Tile Traversal Protocol
- **Testing Mandate:** When a new, reachable tile type is seen, I MUST test it immediately.
- **Movement Test:** Attempt to move *into* and *out of* the tile from all 4 cardinal directions to verify passability.
- **Ledge Test:** For any ledge-like tile, I must attempt to move up/against the apparent direction of the ledge to confirm if it is a one-way path.

### Verified Tile Types
*   **Impassable:** `WALL`, `HEADBUTT_TREE`, `PC`, `PILLAR`, `BOOKSHELF`, `TV`, `RADIO`, `TOWN_MAP`, `WINDOW`, `STATUE`, `TABLE`, `CHAIR`, `BIRD` (Farfetch'd), `CUT_TREE`, `WATER`, `COUNTER`, `VOID`, `MART_SHELF`
*   **Traversable:** `FLOOR`, `GRASS`, `TALL_GRASS` (Wild Encounters)
*   **Warps:** `DOOR`, `CAVE`, `LADDER`, `STAIRCASE` (Move onto tile). Gatehouse warps are triggered by walking into the building side.
*   **Directional Warps:** `WARP_CARPET_LEFT`, `WARP_CARPET_DOWN` (Move in specified direction). Untested if they can be entered from other directions.
*   **One-Way Ledges:** `LEDGE_HOP_DOWN/LEFT/RIGHT`. Verified by attempting to move against the ledge direction.
*   **Complex Tiles:** `FLOOR_UP_WALL` (Verified: Enter by moving UP; Exit by moving LEFT/RIGHT).

### Untested Tile Types (High Priority)
* `RAILING`: Needs testing.
* `PIPE_HORIZONTAL`: Needs testing.
* `PIPE_VERTICAL`: Needs testing.

### Other Mechanics
*   **Item Effects:**
    *   **BERRY:** Restores 10 HP. Found at `FRUIT_TREE`s.
    *   **EVERSTONE:** Prevents evolution.
    *   **MOOMOO MILK:** Restores 100 HP. Purchased at MOOMOO FARM.
*   **SLOWPOKETAIL:** Offered for sale on Route 32. Purpose unknown.
*   **Vending Machine Drinks:** Can refresh tired POKéMON.

## II. Key Items, HMs, & TMs
*   **HM01 (CUT):** Clears small trees. Requires the Hive Badge. Taught to SUNDEW.
*   **TM49 (Fury Cutter):** Gets stronger with each consecutive hit.
*   **COIN CASE:** Allows playing at the Game Corner. Found in Goldenrod Underground.

## III. Active Puzzles & Hypotheses

### Goldenrod City
*   **Hypothesis:** A key is required for a locked door at (18, 6) in the underground. The solution likely involves finding this key or triggering an event elsewhere.
*   **Hypothesis:** An Abra is required for the Machop trade on the 5th floor of the Department Store. Abra might be found in the grass on Route 34.

### Ruins of Alph
*   **Objective:** Solve the sliding stone panel puzzle.
*   **Clue:** Liz mentioned hearing a strange radio broadcast from the Ruins of Alph. This might be a clue.

## IV. Tool & Agent Development
### Core Directives
*   I must act on tool/notepad management tasks IMMEDIATELY.
*   I must mark moving objects using their `object_id`.
*   I must use `strategic_advisor` when feeling stuck and feed failed attempts into `quest_strategist` for better hypotheses.
*   I MUST use the `nickname_genius` agent the next time I catch a Pokémon to test its functionality.

## V. Phone Contacts
*   **TODD (CAMPER):** Calls about sales at the Goldenrod Department Store.
*   **JOEY (YOUNGSTER):** Calls about his top-percentage RATTATA.