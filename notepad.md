# Gem's Pokémon Crystal Notepad

## I. Core Directives & Principles
*   **Act Immediately:** As an LLM, I have no concept of 'later'. Any task I decide on (agent creation/refinement, tool fixes, documentation) MUST be performed in the current turn. Deferring tasks is a critical failure.

## II. Game Systems & Mechanics

### Tile Traversal Protocol
- **Testing Mandate:** When a new, reachable tile type is seen, I MUST test it immediately.
- **Movement Test:** Attempt to move *into* and *out of* the tile from all 4 cardinal directions to verify passability.
- **Ledge Test:** For any ledge-like tile, I must attempt to move up/against the apparent direction of the ledge to confirm if it is a one-way path.
- **Obvious Tile Test:** Even if a tile seems obviously impassable (e.g., WALL), I must attempt to walk into it once to be 100% certain.

### Verified Tile Types
*   **Impassable:** `WALL`, `HEADBUTT_TREE`, `PILLAR`, `BOOKSHELF`, `TV`, `RADIO`, `TOWN_MAP`, `WINDOW`, `STATUE`, `TABLE`, `CHAIR`, `BIRD` (Farfetch'd), `VOID`, `MART_SHELF`, `COUNTER`, `WATER` (without Surf), `BUOY`, `PC`, `LINK_CABLE`, `TRADE_MACHINE`, `INCENSE_BURNER`.
*   **Traversable:** `FLOOR`, `GRASS`, `TALL_GRASS` (Wild Encounters), `LONG_GRASS` (Wild Encounters), `RAILING`, `PIPE_HORIZONTAL`, `PIPE_VERTICAL`.
*   **Warps:** `DOOR`, `CAVE`, `LADDER`, `STAIRCASE` (Move onto tile).
*   **One-Way Ledges:** 
    * `LEDGE_HOP_DOWN/LEFT/RIGHT`.
    * `FLOOR_UP_WALL`: A one-way ledge that can only be hopped **UP**. It is impassable from above (acts as a wall). Confirmed in Union Cave B1F and Slowpoke Well B1F.
*   **Special Requirement:** `CUT_TREE` (Requires HM01 Cut).
*   **Complex Tiles:**
    *   `WARP_CARPET_LEFT/DOWN/RIGHT`: Activated by pressing the indicated direction while standing on the tile.
    *   `Push-Down Trap`: A `FLOOR` tile that, when stepped on, pushes the player down one tile. It is a one-way interaction.
    *   `Interactable Warp (FLOOR)`: Some FLOOR tiles that are also warps do not activate on entry. They must be interacted with by pressing 'A' to trigger an event or text. (e.g., Ruins of Alph Inner Chamber @ (15, 3)).

### Other Mechanics
*   **Item Effects:**
    *   **BERRY:** Restores 10 HP. Found at `FRUIT_TREE`s.
    *   **EVERSTONE:** Prevents evolution.
    *   **MOOMOO MILK:** Restores 100 HP.
    *   **ODD EGG:** A special egg received from the Day-Care Man.
    *   **HARD STONE:** Powers up rock-type moves.
*   **Haircuts:** Increases a Pokémon's happiness.
*   **Pokégear Phone Menu:** When the 'Whom do you want to call?' text box is active, you cannot use the D-pad to switch functions. You MUST press 'B' to cancel and return to the main Pokégear screen before you can navigate to the radio.

## III. Key Items & TMs
*   **COIN CASE:** Allows playing at the Game Corner.
*   **HM01 (CUT):** Clears small trees. Requires Hive Badge.
*   **SQUIRTBOTTLE:** Used to clear the Sudowoodo on Route 36.
*   **TM08 (ROCK SMASH):** Attack that may lower DEFENSE. Can shatter small rocks.
*   **TM12 (SWEET SCENT):** Lures wild POKéMON.
*   **TM28 (DIG):** Powerful GROUND move. Can escape caves.
*   **TM45 (ATTRACT):** Infatuates opposite-gender Pokémon.
*   **TM49 (FURY CUTTER):** Gets stronger with each consecutive hit.

## V. Archive: Solved Puzzles & Procedural Failures
*   **Solved: Azalea Town Slowpoke Infestation:** Confronted Team Rocket in Slowpoke Well after speaking with Kurt.
*   **Failure Log (Turns ~27050-27235):** Severe behavioral loops related to Pokégear menu navigation. Failed to consult documented solution.
*   **Failure Log (Turn ~27329):** Pathfinder tool did not account for NPCs. Upgraded tool to route around all objects.
*   **Failure Log (Turns ~27410-27441):** Became stuck in Violet City Mart. Failed to seek alternative hypotheses when a plan was failing.
*   **Failure Log (Turns ~27544-27685):** Repeatedly distrusted pathfinder tool output, assuming it was broken when my own map understanding was flawed. **Lesson: Trust tool outputs to challenge my assumptions.**
*   **Failure Log (Turn ~27708):** `pathfinder_v5` incorrectly identified start tile as impassable due to a map marker. Corrected the tool.
*   **Failure Log (Turns ~27817-27840):** Stuck interacting with wandering NPCs in Azalea Town. **Lesson: Abandon failing strategies more quickly.**