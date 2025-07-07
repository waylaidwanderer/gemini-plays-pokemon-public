# Gem's Pokémon Crystal Notepad

## I. Game Systems & Mechanics

### Tile Traversal Protocol
- **Testing Mandate:** When a new, reachable tile type is seen, I MUST test it immediately.
- **Movement Test:** Attempt to move *into* and *out of* the tile from all 4 cardinal directions to verify passability.
- **Ledge Test:** For any ledge-like tile, I must attempt to move up/against the apparent direction of the ledge to confirm if it is a one-way path.

### Verified Tile Types
*   **Impassable:** `HEADBUTT_TREE`, `PC`, `PILLAR`, `BOOKSHELF`, `TV`, `RADIO`, `TOWN_MAP`, `WINDOW`, `STATUE`, `TABLE`, `CHAIR`, `BIRD` (Farfetch'd), `CUT_TREE`, `VOID`, `MART_SHELF`, `COUNTER`
*   **Traversable:** `FLOOR`, `GRASS`, `TALL_GRASS` (Wild Encounters), `LONG_GRASS` (Wild Encounters, functions like TALL_GRASS)
*   **Warps:** `DOOR`, `CAVE`, `LADDER` (Move onto tile), `STAIRCASE` (Move onto tile). Gatehouse warps are triggered by walking into the building side.
*   **One-Way Ledges:** `LEDGE_HOP_DOWN/LEFT/RIGHT`. Verified by attempting to move against the ledge direction.
*   **Complex Tiles:**
    *   `FLOOR_UP_WALL`: One-way ledge. Enter from below/sides. Cannot exit by moving up.
    *   `WARP_CARPET_LEFT/DOWN`: Activated by pressing the indicated direction while standing on the tile.
    *   `WALL` (in National Park): The fence posts themselves are impassable, but the gaps between them on the same Y-axis are traversable `FLOOR` tiles. This allows passage through what appears to be a solid barrier.

### Untested Tile Types (High Priority)
* `RAILING`: Located on the Goldenrod Dept. Store Roof.
* `PIPE_HORIZONTAL`
* `PIPE_VERTICAL`
* `WATER`
* `LINK_CABLE`: Located on Pokecenter2F.
* `TRADE_MACHINE`: Located on Pokecenter2F.

### Other Mechanics
*   **Item Effects:**
    *   **BERRY:** Restores 10 HP. Found at `FRUIT_TREE`s.
    *   **EVERSTONE:** Prevents evolution.
    *   **MOOMOO MILK:** Restores 100 HP.
*   **SLOWPOKETAIL:** Offered for sale on Route 32. Purpose unknown.
*   **Vending Machine Drinks:** Can refresh tired POKéMON.
*   **Hidden Items:** Must be interacted with from an adjacent tile.
*   **Haircuts:** Increases a Pokémon's happiness.
*   **Pokégear UI:** The Phone function has a sub-menu ('Whom do you want to call?'). This is a modal state. Directional buttons are DISABLED. You MUST press 'B' to exit this sub-menu.

## II. Key Items & TMs
*   **COIN CASE:** Allows playing at the Game Corner. Found in the Goldenrod Underground.
*   **HM01 (CUT):** Clears small trees. Requires the Hive Badge.
*   **SQUIRTBOTTLE:** Used to reveal the Sudowoodo on Route 36.
*   **TM08 (ROCK SMASH):** An attack that may lower DEFENSE. Can be used to shatter small rocks outside of battle.
*   **TM28 (DIG):** A powerful GROUND-type move. Can also be used to escape from caves.
*   **TM45 (ATTRACT):** Makes full use of a POKéMON's charm.
*   **TM49 (FURY CUTTER):** Gets stronger with each consecutive hit.

## III. Active Puzzles & Hypotheses
*   **Radio Tower Side Quests:** Received a BLUE CARD from Buena on the 2nd floor. I can earn points by giving her passwords from the radio and trade them for prizes.
*   **Goldenrod Dept. Store Sale:** Camper Todd called to let me know there's a bargain sale on now.

## IV. Agent & Tool Development
*   **Current Tools:** `pathfinder_v2` (debug version), `quest_strategist`, `ui_navigator`.
*   **Development Idea:** Create a `puzzle_solver_agent` to help when stuck by analyzing map, inventory, and goals to suggest novel hypotheses.