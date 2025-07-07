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
    *   `FLOOR_UP_WALL`: One-way ledge. Enter from below/sides. Cannot exit by moving up.
    *   `WARP_CARPET_DOWN`: One-way warp. Activated by pressing 'Down' while standing on the tile.

### Untested Tile Types (High Priority)
* `RAILING`: Located on the Goldenrod Dept. Store Roof.
* `PIPE_HORIZONTAL`
* `PIPE_VERTICAL`
* `WATER`
* `LINK_CABLE`: Located on Pokecenter2F.
* `TRADE_MACHINE`: Located on Pokecenter2F.
* `LADDER`: One in Goldenrod Dept. Store basement is unreachable.

### Other Mechanics
*   **Item Effects:**
    *   **BERRY:** Restores 10 HP. Found at `FRUIT_TREE`s.
    *   **EVERSTONE:** Prevents evolution.
    *   **MOOMOO MILK:** Restores 100 HP.
*   **SLOWPOKETAIL:** Offered for sale on Route 32. Purpose unknown.
*   **Vending Machine Drinks:** Can refresh tired POKéMON.
*   **Hidden Items:** Must be interacted with from an adjacent tile.
*   **Haircuts:** Increases a Pokémon's happiness.

## II. Key Items & TMs
*   **COIN CASE:** Allows playing at the Game Corner. Found in the Goldenrod Underground.
*   **HM01 (CUT):** Clears small trees. Requires the Hive Badge.
*   **TM49 (Fury Cutter):** Gets stronger with each consecutive hit.

## III. Active Puzzles & Hypotheses

### Goldenrod City Path Forward
*   **Obstacle:** The path east out of Goldenrod City is blocked by a strange tree (Sudowoodo).
*   **Hypothesis 1:** The Goldenrod Gym Leader, Whitney, must be defeated. This may provide an item or trigger an event to clear the tree.
    *   **Test:** Locate and defeat the Goldenrod Gym Leader.
*   **Hypothesis 2 (Alternative):** Progress is tied to the Radio Tower issue. The 'something wrong with the DIRECTOR' must be resolved.
    *   **Test:** Find a way to get past the guard on Radio Tower 2F.

### Untested Assumptions
*   **Assumption:** The building at (31, 21) in Goldenrod is the Gym.
    *   **Alternative Hypothesis:** It's a regular building. The Gym is elsewhere, possibly behind an NPC I haven't spoken to or in a misidentified building.
    *   **Test to Disprove:** Explore the building. If it's not the gym, I must systematically re-explore Goldenrod City, talking to every single NPC again.
*   **Assumption:** I need a key item to get past the strange tree (Sudowoodo).
    *   **Alternative Hypothesis:** It requires a specific Pokémon, a story event trigger elsewhere, or a special interaction (like using a specific move).
    *   **Test to Disprove:** After exhausting item-based possibilities, return to the tree after major story events (like beating the gym) to check for changes.