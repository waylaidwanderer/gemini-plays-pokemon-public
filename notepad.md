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

## II. Key Items, HMs, & TMs
*   **HM01 (CUT):** Clears small trees. Requires the Hive Badge. Taught to SUNDEW.
*   **TM49 (Fury Cutter):** Gets stronger with each consecutive hit.
*   **COIN CASE:** Allows playing at the Game Corner. Lost by a man in the Goldenrod Underground.

## III. Active Puzzles & Hypotheses

### Goldenrod Underground
*   **Objective:** Find a way to the eastern section of the underground, likely through the locked door at (18, 6) or via a hidden switch room.
*   **Hypothesis 1 (Failed):** A hidden switch is located on the walls near the defeated trainers in the western section. (Tested multiple tiles, no results).
*   **Hypothesis 2 (Current):** A key or switch-triggering item is located at one of the hidden item spots. Currently investigating the one at (4, 18).
*   **Hypothesis 3:** A hidden passage exists along one of the walls.
*   **Hypothesis 4:** An object in the area can be removed with CUT.

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
*   I must use `strategic_advisor` or `quest_strategist` when feeling stuck.
*   I MUST use the `nickname_genius` agent the next time I catch a Pokémon to test its functionality.

## V. Phone Contacts
*   **TODD (CAMPER):** Calls about sales at the Goldenrod Department Store.
*   **JOEY (YOUNGSTER):** Calls about his top-percentage RATTATA.
- **Goldenrod Underground - Switch Room:**
  - **Hypothesis 1:** The objects on the northern wall are switches.
  - **Test 1:** Interacted with the object at (18, 23) from (18, 22). Result: Failed.
  - **Test 2:** Interacted with the object at (20, 23) from (20, 22). Result: Failed.
  - **Test 3:** Interacted with the object at (22, 23) from (22, 22). Result: Failed.
  - **Conclusion:** Interacting with the switches individually does not work.
  - **New Hypothesis:** The puzzle requires pressing the switches in a specific sequence.
  - **Next Step:** Test the simplest sequence: Left (18,23), then Middle (20,23), then Right (22,23).