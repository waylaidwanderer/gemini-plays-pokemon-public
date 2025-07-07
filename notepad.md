# Gem's Pokémon Crystal Notepad

## I. Game Systems & Mechanics

### Tile Traversal Protocol
- **Testing Mandate:** When a new, reachable tile type is seen, I MUST test it immediately.
- **Movement Test:** Attempt to move *into* and *out of* the tile from all 4 cardinal directions to verify passability.
- **Ledge Test:** For any ledge-like tile, I must attempt to move up/against the apparent direction of the ledge to confirm if it is a one-way path.

### Verified Tile Types
*   **Impassable:** `WALL`, `HEADBUTT_TREE`, `PC`, `PILLAR`, `BOOKSHELF`, `TV`, `RADIO`, `TOWN_MAP`, `WINDOW`, `STATUE`, `TABLE`, `CHAIR`, `BIRD` (Farfetch'd), `CUT_TREE`, `COUNTER`, `VOID`, `MART_SHELF`
*   **Traversable:** `FLOOR`, `GRASS`, `TALL_GRASS` (Wild Encounters)
*   **Warps:** `DOOR`, `CAVE`, `LADDER` (Move onto tile), `STAIRCASE` (Move onto tile). Gatehouse warps are triggered by walking into the building side.
*   **One-Way Ledges:** `LEDGE_HOP_DOWN/LEFT/RIGHT`. Verified by attempting to move against the ledge direction.
*   **Complex Tiles:**
    *   `FLOOR_UP_WALL`: Functions as a one-way ledge. Can be entered from below and from the sides (left/right). Cannot be exited by moving up, but can be exited by moving down or sideways to an adjacent `FLOOR_UP_WALL` tile.
    *   `WARP_CARPET_DOWN`: Activated by walking onto the tile in the specified direction (e.g., 'Down' for a down-facing carpet). Pressing 'A' has no effect.

### Untested Tile Types (High Priority)
* `RAILING`: Needs testing. Located on the Goldenrod Dept. Store Roof.
* `PIPE_HORIZONTAL`: Needs testing.
* `PIPE_VERTICAL`: Needs testing.
* `WATER`: Needs testing.
* `LINK_CABLE`: Needs testing. Located on Pokecenter2F.
* `TRADE_MACHINE`: Needs testing. Located on Pokecenter2F.

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
*   **Fact:** The path east out of Goldenrod City is blocked by a strange tree (Sudowoodo). Progress is impossible this way for now.
*   **Hypothesis 1:** The 'basement of the DEPT.STORE' is a required area to progress the story and reach the Goldenrod Gym.
*   **Hypothesis 2 (Alternative):** The basement is a side area. The gym is located elsewhere, possibly behind an un-interacted NPC or in a misidentified building.
*   **Test:** Explore the basement. If it's a dead end or doesn't yield a key item/event, Hypothesis 1 is false. I must then systematically re-explore the city.

### Radio Tower
*   **Fact:** A Black Belt on the 2nd floor is blocking the stairs to 3F. He says only 'authorized personnel' can pass because 'something is wrong with the DIRECTOR'.
*   **Clue:** Liz and a Super Nerd mentioned a strange radio broadcast. This is likely the key to this puzzle, but I was unable to operate the Pokégear radio.

## IV. Agent & Tool Development
*   **ui_navigator Agent:** Created to help navigate complex menus. Needs to be tested.
*   **nickname_genius Agent:** Must be tested at the next opportunity (catching a new Pokémon).